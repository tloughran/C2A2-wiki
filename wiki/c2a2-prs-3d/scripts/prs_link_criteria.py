#!/usr/bin/env python3
"""Criteria for a semantically meaningful, plausibly causal link between PRS triplets.

WHY THIS EXISTS
---------------
The connectome's generative-coil layer scored candidate links with Jaccard overlap
on significant tokens. Five hand-checked, literature-attested dependencies in the
quantum/deep-learning fixture score 0.000 to 0.056 against a 0.15 threshold, while
the best-scoring pair anywhere in the fixture is 0.121 and is not a dependency at
all. Lowering the threshold far enough to admit de Broglie -> Schrodinger admits
essentially every ordered pair. That is not a tuning problem: bag-of-words overlap
measures SHARED TOPIC, and two entries about the same subject share vocabulary
whether or not one is built out of the other.

The criteria here look for the things a reader actually points at when asked why
one entry depends on another, and they keep the pieces separate rather than
averaging them into one number.

  C1  NAMING       The target's text names the source - by surname, by model name,
                   or by the distinctive phrase the source coined. "Taking Planck's
                   discrete energy elements" is not topic overlap; it is a citation
                   in prose.

  C2  INHERITANCE  The target reuses a DISTINCTIVE term (document frequency <= 3 of
                   20) that the source's label or solution introduced. Rare terms
                   carry the signal that common ones drown: one shared "attention"
                   or "photoelectric" outweighs four shared "quantum"s, which is
                   exactly the weighting Jaccard refuses to make.

  C3  PLACEMENT    WHERE in the target the evidence sits, reported but NOT used to
                   type the link. This criterion was written to decide the relation
                   - resource means the source supplied material, problem means the
                   source set the problem - and MEASUREMENT KILLED IT. In this prose
                   style the Problem sentence carries the historical setup, so the
                   strongest resource_supplying edge in the corpus, de Broglie ->
                   Schrodinger, announces itself in the target's PROBLEM: "de
                   Broglie's matter waves lack a governing equation of motion". So
                   does Einstein -> Compton, and so does Heisenberg -> Dirac. Bohr ->
                   de Broglie, a genuine problem_setting edge, sits in the same field
                   with the same shape. The two are separated by discourse framing -
                   a source that is COMPLETED versus a source that is DISSOLVED - and
                   nothing at the token level sees that difference. Only a hit in the
                   target's RESOURCE is typed; everything else is emitted as
                   `undetermined` for a human to type. Tom's question survives intact,
                   but placement is not the cheap answer to it.

  C4  DIRECTION    The source must be strictly earlier. Delegated to
                   extract_prs_data.gen_direction, which also reports whether the
                   ordering rests on a real publication year or on a filing date.

  C5  ASYMMETRY    The evidence must attach to what the source PRODUCED - its label
                   and solution at full weight, its resource at reduced weight,
                   because a resource can itself be handed on (the RL machinery in
                   RLHF is inherited by DeepSeek R1 without ever appearing in the
                   RLHF entry's solution). A term that also sits in the source's own
                   PROBLEM is shared framing rather than lineage, and is halved: two
                   entries worried about the same thing are contemporaries.

  C6  COINAGE      A shared distinctive term counts only if the SOURCE is the
                   earliest entry in the corpus that uses it. Without this, AlexNet
                   and ResNet link on `error`, `percent` and `roughly` - the shared
                   vocabulary of an ImageNet leaderboard, not a dependency - which is
                   the same failure as the lexical baseline wearing better clothes.

STATUS, NOT SCORE
-----------------
Per the epistemics ruling this script never emits `attested`. Neither link type can
be proven from the text - letters are lost, influence goes unrecorded - but claims
CAN be ruled out by the literature. So the output status is `plausible`, and only a
human reading the record may write `attested` or `ruled_out` into
testcorpus/dependencies.json. A confidence score would average evidence and absence
into a single number and hide precisely that distinction.
"""

import argparse
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract_prs_data as X  # noqa: E402


DF_DISTINCTIVE = 3      # a term in <= this many of the N entries counts as distinctive
MIN_TERM_LEN = 5
ALIAS_STOP = set("the a an of as at in on to and or for with is are its".split())


def norm(s):
    return re.sub(r"\s+", " ", X._deaccent(s or "").lower())


def content_tokens(s):
    return [w for w in re.findall(r"[a-z0-9][a-z0-9-]*", norm(s)) if w not in ALIAS_STOP]


def phrase_re(tokens):
    """Match these tokens in order, allowing one intervening word.

    'the light quantum' has to match 'The light quantum was still widely read';
    'scaling laws' has to match 'confirming the scaling laws in the direction'.
    One slot of slack picks up a possessive or an article without letting the
    phrase drift across a clause boundary.
    """
    gap = r"[^a-z0-9]+(?:[a-z0-9-]+[^a-z0-9]+)?"
    return re.compile(r"(?<![a-z0-9])" + gap.join(re.escape(t) for t in tokens) + r"(?![a-z0-9])")


def aliases_for(t):
    """Names by which the rest of the corpus could refer to this triplet.

    Labels are written 'Name (year) - subtitle', so the label carries both the
    proper name and the coinage. Both are used: Compton's entry never says
    'Einstein', it says 'The light quantum', which is Einstein's subtitle.
    """
    label = t.get("label", "")
    head = re.split(r"[(—–]", label, 1)[0].strip()
    sub = ""
    m = re.split(r"[—–]", label, 1)
    if len(m) > 1:
        sub = re.sub(r"^\s*", "", m[1]).strip()

    out = []
    for piece in re.split(r"\s*/\s*", head):
        toks = content_tokens(piece)
        if not toks:
            continue
        out.append(("name", toks))
        # A multi-word name is also referred to by its tail: 'Neural scaling laws'
        # appears downstream as 'the scaling laws'.
        if len(toks) > 2:
            out.append(("name", toks[-2:]))
        # 'AlphaFold 2' and 'DeepSeek R1' are cited without the version.
        if len(toks) == 2 and re.match(r"^[a-z]?[0-9]+$", toks[-1]):
            out.append(("name", toks[:1]))
    subtoks = content_tokens(sub)
    if len(subtoks) >= 2:
        out.append(("coinage", subtoks))
    # dedupe, keep order
    seen, uniq = set(), []
    for kind, toks in out:
        k = tuple(toks)
        if k in seen:
            continue
        seen.add(k)
        uniq.append((kind, toks))
    return uniq


def build_index(triplets):
    """Document frequency over entries, for the distinctiveness weighting."""
    df = Counter()
    for t in triplets:
        text = " ".join((t.get("label", ""), t.get("problem", ""),
                         t.get("resource", ""), t.get("solution", "")))
        terms = set(w for w in re.findall(r"[a-z]{%d,}" % MIN_TERM_LEN, norm(text))
                    if w not in X.GEN_STOP)
        for w in terms:
            df[w] += 1
    return df


def terms_of(s, df, n):
    return set(w for w in re.findall(r"[a-z]{%d,}" % MIN_TERM_LEN, norm(s))
               if w not in X.GEN_STOP and 0 < df.get(w, 0) <= DF_DISTINCTIVE)


# Only a hit inside the target's RESOURCE is typed automatically. See C3: the
# other two fields do not separate a source that was built on from one that was
# argued against, and guessing would put an orange arrow on a refutation.
FIELD_RELATION = {"resource": "resource_supplying",
                  "problem": "undetermined",
                  "solution": "undetermined"}
FIELD_ORDER = ("resource", "problem", "solution")


def _sort_key(t):
    y = t.get("pub_year") if isinstance(t.get("pub_year"), int) else 9999
    return (y, (t.get("date") or "9999")[:10], t["id"])


def coinage_owner(triplets, df):
    """For each shareable distinctive term, the earliest entry that uses it.

    C6. A term only counts as inherited if the source is where it enters the
    corpus. Without this the criteria rediscover shared benchmark vocabulary -
    AlexNet and ResNet both report `percent` top-5 `error` - and call it lineage.
    """
    owner = {}
    for t in sorted(triplets, key=_sort_key):
        text = " ".join((t.get("label", ""), t.get("problem", ""),
                         t.get("resource", ""), t.get("solution", "")))
        for w in set(re.findall(r"[a-z]{%d,}" % MIN_TERM_LEN, norm(text))):
            if w in X.GEN_STOP or not (0 < df.get(w, 0) <= DF_DISTINCTIVE):
                continue
            owner.setdefault(w, t["id"])
    return owner


def evaluate_pair(a, b, df, n, alias_cache, term_cache, owner):
    """All evidence that b depends on a. Returns None when nothing fires."""
    hits = []

    # C1 - naming. Search each of b's three fields separately so C3 can report
    # placement straight off the hit.
    for kind, toks in alias_cache[a["id"]]:
        rx = phrase_re(toks)
        for field in FIELD_ORDER:
            if rx.search(norm(b.get(field, ""))):
                hits.append({"criterion": "C1_naming", "kind": kind,
                             "phrase": " ".join(toks), "field": field,
                             "weight": 3.0 if kind == "name" else 2.5})
                break  # one hit per alias; the earliest field wins for placement

    # C2 - distinctive-term inheritance, weighted by inverse document frequency,
    # gated on C6 (the source must be where the term enters the corpus) and
    # scaled by C5 (where in the source it sits).
    for src_field, scale in (("produced", 1.0), ("resource", 0.6)):
        for field in FIELD_ORDER:
            shared = term_cache[a["id"]][src_field] & terms_of(b.get(field, ""), df, n)
            for w in sorted(shared):
                if owner.get(w) != a["id"]:
                    continue                      # C6: not this entry's coinage
                if any(h.get("term") == w for h in hits):
                    continue                      # already counted, best field first
                hits.append({"criterion": "C2_inheritance", "term": w,
                             "df": df[w], "field": field, "source_field": src_field,
                             "weight": round(math.log(n / df[w]) * scale, 3)})

    if not hits:
        return None

    # C5 - a term that also sits in the source's own PROBLEM is shared framing.
    a_problem = term_cache[a["id"]]["problem"]
    for h in hits:
        if h["criterion"] == "C2_inheritance" and h["term"] in a_problem:
            h["also_in_source_problem"] = True
            h["weight"] = round(h["weight"] * 0.5, 3)

    # QUALIFICATION, and the TIER that comes out of it. One shared term is not a
    # finding: in a corpus of 20 short entries almost every word is rare, so
    # "exclusive to this pair" is an accident of corpus size rather than evidence -
    # measured, it costs 14 false positives and buys no recall at all.
    #
    #   tier 'named'     - C1 fired. On this fixture that is 10 proposals and 10
    #                      attested dependencies: precision 1.00, recall 0.53.
    #   tier 'inherited' - no name, but two or more terms this source coined.
    #                      Raises recall to 0.89 and drops precision to 0.55.
    #
    # The two are kept apart rather than summed, for the same reason status is not
    # a score: they are different kinds of claim, and a reader is entitled to see
    # which one an arc rests on.
    named = any(h["criterion"] == "C1_naming" for h in hits)
    c2 = [h for h in hits if h["criterion"] == "C2_inheritance"]
    if not (named or len(c2) >= 2):
        return None
    tier = "named" if named else "inherited"

    direction, basis = X.gen_direction(a, b)      # C4

    fields_hit = set(h["field"] for h in hits)    # C3, reporting only
    relation = "undetermined"
    for f in FIELD_ORDER:
        if f in fields_hit:
            relation = FIELD_RELATION[f]
            break

    return {
        "source": a["id"], "target": b["id"],
        "relation": relation,
        "generative": relation == "resource_supplying",
        "status": "plausible",          # never 'attested' - see the module docstring
        "direction": direction, "direction_basis": basis,
        "strength": round(sum(h["weight"] for h in hits), 3),
        "tier": tier,
        "named": named,
        "evidence_fields": sorted(fields_hit),
        "criteria": sorted(set(h["criterion"] for h in hits)),
        "evidence": sorted(hits, key=lambda h: -h["weight"])[:8],
    }


def candidates(triplets, min_strength=1.5, require_forward=True):
    n = len(triplets)
    df = build_index(triplets)
    owner = coinage_owner(triplets, df)
    alias_cache = {t["id"]: aliases_for(t) for t in triplets}
    term_cache = {t["id"]: {
        "produced": terms_of(" ".join((t.get("label", ""), t.get("solution", ""))), df, n),
        "resource": terms_of(t.get("resource", ""), df, n),
        "problem": terms_of(t.get("problem", ""), df, n),
    } for t in triplets}

    space, out, rejected = 0, [], Counter()
    for a in triplets:
        for b in triplets:
            if a["id"] == b["id"]:
                continue
            space += 1
            c = evaluate_pair(a, b, df, n, alias_cache, term_cache, owner)
            if not c:
                rejected["no_qualifying_evidence"] += 1
                continue
            if require_forward and c["direction"] != "forward":
                rejected["not_forward"] += 1
                continue
            if c["strength"] < min_strength:
                rejected["below_strength"] += 1
                continue
            out.append(c)
    out.sort(key=lambda c: -c["strength"])
    return out, {"ordered_pairs": space, "kept": len(out), "rejected": dict(rejected),
                 "shareable_terms": sum(1 for w, k in df.items() if 2 <= k <= DF_DISTINCTIVE),
                 "vocabulary": len(df)}


# ---------------------------------------------------------------- evaluation

def load_gold(path):
    rows = json.load(open(path, encoding="utf-8"))["dependencies"]
    attested, ruled_out, gen, textual = set(), set(), set(), {}
    for r in rows:
        k = (r["source"], r["target"])
        if r["status"] == "attested":
            attested.add(k)
            if r["relation"] == "resource_supplying":
                gen.add(k)
        elif r["status"] == "ruled_out":
            ruled_out.add(k)
        # 'expressed' wins if any row for the pair says so
        rank = {"expressed": 2, "partial": 1, "unexpressed": 0}
        if rank[r["textual"]] >= rank.get(textual.get(k, "unexpressed"), 0):
            textual[k] = r["textual"]
    return {"rows": rows, "attested": attested, "ruled_out": ruled_out,
            "generative": gen, "textual": textual}


def prf(found, gold):
    tp = len(found & gold)
    p = tp / len(found) if found else 0.0
    r = tp / len(gold) if gold else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return tp, p, r, f


def baseline_pairs(triplets):
    edges, _ = X.gen_chains(triplets, min_shared=3, min_jaccard=0.15,
                            cross_tradition_only=False)
    return set((e["source"], e["target"]) for e in edges)


def report(triplets, cands, stats, gold):
    n = len(triplets)
    print("corpus: %d entries, %d ordered pairs, %d shareable distinctive terms of %d vocabulary"
          % (n, stats["ordered_pairs"], stats["shareable_terms"], stats["vocabulary"]))
    print("rejected: %s" % stats["rejected"])
    print()

    found = set((c["source"], c["target"]) for c in cands)
    found_gen = set((c["source"], c["target"]) for c in cands if c["generative"])
    base = baseline_pairs(triplets)

    gold_att = gold["attested"]
    # Three buckets, all reported. 'expressed' means both entries put the link in
    # words and is the only fair ceiling for a method that reads text; 'partial'
    # means one side says it and the other is silent, which no text matcher can
    # bridge; 'unexpressed' means the corpus never says it at all. Folding partial
    # into the ceiling would blame the method for the corpus.
    def bucket(g, want):
        return set(k for k in g if gold["textual"].get(k) == want)
    expressed = bucket(gold_att, "expressed")
    partial = bucket(gold_att, "partial")
    unexpressed = bucket(gold_att, "unexpressed")
    gold_gen = gold["generative"]
    gen_expressed = bucket(gold_gen, "expressed")

    named_only = set((c["source"], c["target"]) for c in cands if c["tier"] == "named")
    rows = [
        ("TIER 'named' (C1 fired)", named_only, gold_att),
        ("  ...textually expressed", named_only, expressed),
        ("ANY attested link", found, gold_att),
        ("  ...on pairs both entries express (the ceiling)", found, expressed),
        ("  ...on pairs only one side expresses", found, partial),
        ("  ...on pairs the corpus never expresses", found, unexpressed),
        ("GENERATIVE only (resource_supplying)", found_gen, gold_gen),
        ("  ...of those, textually expressed", found_gen, gen_expressed),
        ("BASELINE lexical Jaccard, any attested link", base, gold_att),
        ("BASELINE lexical Jaccard, on the ceiling set", base, expressed),
    ]
    print("%-48s %5s %6s %6s %6s %6s" % ("", "found", "gold", "tp", "prec", "recall"))
    for name, f, g in rows:
        tp, p, r, _ = prf(f, g)
        print("%-48s %5d %6d %6d %5.2f %6.2f" % (name, len(f), len(g), tp, p, r))
    print()

    miss = sorted(expressed - found)
    if miss:
        print("MISSED, though both entries express them (%d):" % len(miss))
        for k in miss:
            print("  %-24s -> %-24s [%s]" % (k[0], k[1], gold["textual"][k]))
    print("\nNOT RECOVERABLE from these summaries (%d) - one side silent (%d) or "
          "the corpus silent (%d):" % (len(partial) + len(unexpressed),
                                       len(partial), len(unexpressed)))
    for k in sorted(partial):
        print("  %-24s -> %-24s [one side silent]" % k)
    for k in sorted(unexpressed):
        print("  %-24s -> %-24s [corpus silent]" % k)

    # Ruled-out pairs must be reported as findings, never silently dropped.
    print("\nRULED OUT by the record, and whether the criteria proposed them anyway:")
    for k in sorted(gold["ruled_out"]):
        c = next((c for c in cands if (c["source"], c["target"]) == k), None)
        if c:
            print("  %-24s -> %-24s PROPOSED as %s (strength %.2f) - draw differently, do not delete"
                  % (k[0], k[1], c["relation"], c["strength"]))
        else:
            print("  %-24s -> %-24s not proposed" % k)

    fp = sorted(found - gold_att - gold["ruled_out"])
    print("\nPROPOSED but not in the gold set (%d) - unexamined, not wrong:" % len(fp))
    for k in fp[:20]:
        c = next(c for c in cands if (c["source"], c["target"]) == k)
        ev = c["evidence"][0]
        print("  %-24s -> %-24s %-18s %.2f  %s"
              % (k[0], k[1], c["relation"], c["strength"],
                 ev.get("phrase") or ev.get("term")))
    if len(fp) > 20:
        print("  ... %d more" % (len(fp) - 20))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--vault", default=os.path.join(here, "..", "testcorpus", "vault"))
    ap.add_argument("--gold", default=os.path.join(here, "..", "testcorpus", "dependencies.json"))
    ap.add_argument("--carryforward", help="curated pub_years, as the regen wrapper passes them")
    ap.add_argument("--min-strength", type=float, default=1.5)
    ap.add_argument("--keep-backward", action="store_true")
    ap.add_argument("--json", help="write candidates here")
    ap.add_argument("--no-eval", action="store_true")
    a = ap.parse_args()

    cf = json.load(open(a.carryforward, encoding="utf-8")) if a.carryforward else {}
    triplets, _ = X.extract_triplets(os.path.abspath(a.vault), cf)
    cands, stats = candidates(triplets, min_strength=a.min_strength,
                              require_forward=not a.keep_backward)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump({"_meta": {"criteria": "C1 naming, C2 inheritance, C3 placement, "
                                             "C4 direction, C5 asymmetry",
                                 "min_strength": a.min_strength, "stats": stats},
                       "candidates": cands}, fh, indent=1)
        print("wrote %s (%d candidates)" % (a.json, len(cands)))
    if not a.no_eval and os.path.isfile(a.gold):
        report(triplets, cands, stats, load_gold(a.gold))


if __name__ == "__main__":
    main()

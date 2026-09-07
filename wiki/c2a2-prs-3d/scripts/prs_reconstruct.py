#!/usr/bin/env python3
"""Rational reconstruction as a THIRD evidence class, with its negative control.

THE IDEA (Tom, 2026-09-01)
--------------------------
Testimony is not the only evidence available. Where the record does not state a
dependency, an ARGUMENT for it can still be constructed and checked: show that
solution S1 has resource R1's shape, that S1 does not stand without R1, and that
R1 was available. At the frontier we should expect many links to be like this -
reconstructible but never written down - because the concept has no name yet, or
transmission was a hallway rather than a bibliography, or the technique became
infrastructure and went invisible precisely by being universal.

That is a genuinely different object from a citation. `attested` CITES.
`reconstructed` ARGUES. Merging them into one score is the failure the epistemics
ruling exists to prevent, so `reconstructed` is a fifth status and the row must
carry the argument itself, not a flag, so a reader can attack the reasoning.

THE DANGER, AND WHY THE CONTROL SHIPS IN THE SAME COMMIT
--------------------------------------------------------
A model asked to construct an argument for a link will nearly always succeed.
Producing a plausible mechanism is the thing language models are best at and least
trustworthy at. Added without a control, this class manufactures a dense, elegant,
entirely fictional connectome that looks BETTER than the real one.

So the procedure is run over a mixed set and scored by condition:

  target            8 attested links the fixture's own text cannot express
  control_ruled_out 3 links the record contradicts
  control_random    9 pairs the criteria rejected outright, forward in time

If reconstructions pass their own checks on the controls at anything like the rate
they do on the targets, the class is worthless and we know it in one run.

WHAT THIS TEST IS, EXACTLY
--------------------------
It is NOT a blind trial. The same model that authors the reconstructions knows the
history of both traditions, so it cannot be made ignorant of which pairs are real.
Withholding the condition labels from the worksheet blinds the author to the
SAMPLING CONDITION, not to the subject matter, and that limit must be stated
wherever the numbers are.

What carries the weight instead is that the form demands commitments a bogus pair
cannot honestly meet:

  component     the specific part of S1 that fails without R1 - not a topic, a part
  necessity     required | used | dispensable | none
  alternatives  what else was on offer at the time
  trace         a VERBATIM phrase, machine-checked against the corpus, whose
                presence the dependency explains; or an external locator in the
                source literature, recorded as such
  refuters      what would falsify this, stated before anyone looks

`verdict: insufficient` is a first-class outcome. If it is never used the test is
rigged, and that is itself reportable.
"""

import argparse
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract_prs_data as X  # noqa: E402
import prs_link_criteria as C  # noqa: E402

SEED = 20260901          # fixed so the sample is reproducible, never re-rolled
N_RANDOM = 9


def load(vault):
    triplets, _ = X.extract_triplets(os.path.abspath(vault), {})
    return triplets, {t["id"]: t for t in triplets}


def entry_text(t):
    return " ".join((t.get("label", ""), t.get("problem", ""),
                     t.get("resource", ""), t.get("solution", "")))


def build_sample(triplets, gold):
    """Targets, ruled-out controls, and random controls - deterministically."""
    by_id = {t["id"]: t for t in triplets}
    # Targets: attested links the corpus cannot express (partial or unexpressed).
    targets = sorted(k for k in gold["attested"]
                     if gold["textual"].get(k) != "expressed")
    ruled = sorted(gold["ruled_out"])

    # Random controls: forward in time, not in the answer key, and rejected by the
    # criteria - i.e. drawn from the population where nothing at all was found.
    cands, _ = C.candidates(triplets)
    proposed = set((c["source"], c["target"]) for c in cands)
    known = set(gold["attested"]) | set(gold["ruled_out"])
    pool = []
    for a in triplets:
        for b in triplets:
            if a["id"] == b["id"]:
                continue
            k = (a["id"], b["id"])
            if k in proposed or k in known:
                continue
            if X.gen_direction(a, b)[0] != "forward":
                continue
            pool.append(k)
    rng = random.Random(SEED)
    randoms = sorted(rng.sample(pool, N_RANDOM))

    rows = ([{"pair": k, "condition": "target"} for k in targets]
            + [{"pair": k, "condition": "control_ruled_out"} for k in ruled]
            + [{"pair": k, "condition": "control_random"} for k in randoms])
    rng.shuffle(rows)
    for i, r in enumerate(rows, 1):
        r["item"] = "R%02d" % i
    return rows, by_id, len(pool)


def cmd_worksheet(a):
    triplets, _ = load(a.vault)
    gold = C.load_gold(a.gold)
    rows, by_id, pool_size = build_sample(triplets, gold)

    keypath = os.path.join(os.path.dirname(a.gold), "reconstruction_key.json")
    with open(keypath, "w", encoding="utf-8") as fh:
        json.dump({"_meta": {"seed": SEED, "random_pool_size": pool_size,
                             "warning": "Conditions. Do not read before authoring."},
                   "key": {r["item"]: {"pair": list(r["pair"]),
                                       "condition": r["condition"]} for r in rows}},
                  fh, indent=1)

    out = ["# Reconstruction worksheet",
           "",
           "%d items, shuffled. Conditions are withheld: they are in "
           "`reconstruction_key.json`, which must not be opened until every item "
           "below is authored." % len(rows),
           "",
           "For each item state whether an argument can be made that the EARLIER "
           "entry's solution is a resource the LATER entry's solution depends on. "
           "`insufficient` is a real answer.",
           ""]
    for r in rows:
        sa, sb = by_id[r["pair"][0]], by_id[r["pair"][1]]
        out.append("## %s" % r["item"])
        for role, t in (("EARLIER", sa), ("LATER", sb)):
            out.append("**%s — %s** (%s)" % (role, t["label"], t["id"]))
            for f in ("problem", "resource", "solution"):
                out.append("- *%s:* %s" % (f.capitalize(), t[f]))
            out.append("")
    open(a.out, "w", encoding="utf-8").write("\n".join(out))
    print("wrote %s (%d items: %d target, %d ruled_out, %d random from a pool of %d)"
          % (a.out, len(rows),
             sum(1 for r in rows if r["condition"] == "target"),
             sum(1 for r in rows if r["condition"] == "control_ruled_out"),
             sum(1 for r in rows if r["condition"] == "control_random"), pool_size))
    print("wrote %s - DO NOT READ until authoring is done" % keypath)


NEEDED = ("claim", "component", "necessity", "alternatives", "exclusivity",
          "trace", "trace_kind", "refuters", "verdict")
NECESSITY = ("required", "used", "dispensable", "none")
VERDICTS = ("reconstructed", "insufficient")


def check_row(r, by_id):
    """Mechanical checks. Returns (ok, problems)."""
    bad = []
    for f in NEEDED:
        if r.get(f) in (None, "", []):
            bad.append("missing %s" % f)
    if r.get("necessity") not in NECESSITY:
        bad.append("necessity not one of %s" % (NECESSITY,))
    if r.get("verdict") not in VERDICTS:
        bad.append("verdict not one of %s" % (VERDICTS,))
    # The verbatim check: a trace claimed to be in the corpus must actually be there.
    # This is the one check the author cannot talk their way past.
    if r.get("trace_kind") == "in_corpus":
        tgt = by_id.get(r["target"])
        hay = C.norm(entry_text(tgt)) if tgt else ""
        if C.norm(r.get("trace", "")) not in hay:
            bad.append("trace claimed in_corpus but is NOT a verbatim substring of "
                       "the target entry")
    elif r.get("trace_kind") == "in_literature":
        if not r.get("trace_locator"):
            bad.append("in_literature trace needs a trace_locator")
    else:
        bad.append("trace_kind must be in_corpus or in_literature")
    return (not bad), bad


def cmd_score(a):
    triplets, by_id = load(a.vault)
    key = json.load(open(os.path.join(os.path.dirname(a.gold),
                                      "reconstruction_key.json"), encoding="utf-8"))["key"]
    rows = json.load(open(a.reconstructions, encoding="utf-8"))["reconstructions"]
    got = {r["item"]: r for r in rows}

    missing = sorted(set(key) - set(got))
    if missing:
        print("NOT AUTHORED: %s" % ", ".join(missing))

    tally = {}
    print("%-5s %-18s %-14s %-11s %-6s %s" %
          ("item", "condition", "verdict", "necessity", "checks", "pair"))
    for item in sorted(key):
        r = got.get(item)
        cond = key[item]["condition"]
        t = tally.setdefault(cond, {"n": 0, "reconstructed": 0, "insufficient": 0,
                                    "failed_checks": 0, "required": 0})
        t["n"] += 1
        if not r:
            continue
        ok, bad = check_row(r, by_id)
        t[r.get("verdict", "insufficient")] = t.get(r.get("verdict", "insufficient"), 0) + 1
        if not ok:
            t["failed_checks"] += 1
        if r.get("necessity") == "required":
            t["required"] += 1
        print("%-5s %-18s %-14s %-11s %-6s %s -> %s" %
              (item, cond, r.get("verdict"), r.get("necessity"),
               "ok" if ok else "FAIL", key[item]["pair"][0], key[item]["pair"][1]))
        if bad:
            for p in bad:
                print("        ! %s" % p)

    print("\n%-18s %4s %14s %13s %10s" %
          ("condition", "n", "reconstructed", "insufficient", "necessity=required"))
    for cond in ("target", "control_ruled_out", "control_random"):
        t = tally.get(cond)
        if not t:
            continue
        print("%-18s %4d %13d%% %12d%% %9d%%" %
              (cond, t["n"], round(100 * t["reconstructed"] / t["n"]),
               round(100 * t["insufficient"] / t["n"]),
               round(100 * t["required"] / t["n"])))
    tg = tally.get("target", {"n": 0, "reconstructed": 0})
    ct = {"n": 0, "reconstructed": 0}
    for cond in ("control_ruled_out", "control_random"):
        for k in ct:
            ct[k] += tally.get(cond, {}).get(k, 0)
    tr = tg["reconstructed"] / tg["n"] if tg["n"] else 0
    cr = ct["reconstructed"] / ct["n"] if ct["n"] else 0
    print("\nVERDICT")
    print("  targets reconstructed  %.0f%%" % (100 * tr))
    print("  controls reconstructed %.0f%%" % (100 * cr))
    if cr >= tr * 0.75:
        print("  FAIL - the procedure fires on controls at a comparable rate. The class")
        print("  is a story generator; do not put it in the schema.")
    elif cr > 0:
        print("  MIXED - separation exists but controls are not clean. Report the rate.")
    else:
        print("  PASS - no control survived its own checks. The separation is the result.")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--vault", default=os.path.join(here, "..", "testcorpus", "vault"))
    ap.add_argument("--gold", default=os.path.join(here, "..", "testcorpus", "dependencies.json"))
    sub = ap.add_subparsers(dest="cmd", required=True)
    w = sub.add_parser("worksheet"); w.add_argument("--out", required=True)
    s = sub.add_parser("score"); s.add_argument("--reconstructions", required=True)
    a = ap.parse_args()
    (cmd_worksheet if a.cmd == "worksheet" else cmd_score)(a)


if __name__ == "__main__":
    main()

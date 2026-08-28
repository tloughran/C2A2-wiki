#!/usr/bin/env python3
"""
Reference-master harvester — foundation §7 step 2 (deterministic; Rule 5).

Scans the Summa vault's synthesis/ BODIES for the roster surnames + PRS/CROSS/FLAG/FINDING
ids + known work-title mentions, resolves each to a cite_key from works_cited.json, and emits:
  - reference_master.json  (machine source of truth for the reconcile/build steps)
  - Reference master.md    (human-readable per-thinker occurrence index — the "reference master page")

Body vs footer: each synthesis file ends in a YAML footer (day:, karpathy_wiki_sources:, ...) plus a
"Related tradition records" auto-link line. Per foundation §5/§6.4 the footer is INTERNAL sourcing
guidance, stripped at export — so body citations are harvested from the BODY only. The footer's
`karpathy_wiki_sources` is captured separately (JSON only) as the day's intended source list, for the
reconcile pass — never counted as a body citation.

Resolution (provisional; specific-vs-generic reconciliation is step 3):
  - a body mention of a KNOWN work title -> that work's cite_key            (specific)
  - a bare surname with no titled work     -> the thinker's canonical cite_key (generic -> flagged)
  - PRS/CROSS/FLAG/FINDING ids            -> recorded raw + scoped thinker (id->cite_key is step 3/4)

Usage:  python3 harvest_references.py <RCK_root> <SUMMA_root>
        (expects <RCK_root>/commentary-apparatus/works_cited.json and <SUMMA_root>/vault/synthesis/)
"""
import json, re, os, sys, glob

RCK = sys.argv[1] if len(sys.argv) > 1 else "mnt/RC Karpathy Wiki Project"
SUMMA = sys.argv[2] if len(sys.argv) > 2 else "mnt/Summa 2026 in a Year"

WC_PATH = os.path.join(RCK, "commentary-apparatus", "works_cited.json")
SYN_DIR = os.path.join(SUMMA, "vault", "synthesis")
OUT_JSON = os.path.join(RCK, "commentary-apparatus", "reference_master.json")
OUT_MD = os.path.join(RCK, "commentary-apparatus", "Reference master.md")

# tag -> surname as it appears in the bodies (roster 15 + shared refs actually cited in prose)
SURNAME = {
    "levin": "Levin", "friston": "Friston", "hoffman": "Hoffman", "hawkins": "Hawkins",
    "mcgilchrist": "McGilchrist", "fredrickson": "Fredrickson", "carroll": "Carroll",
    "arkanihamed": "Arkani-Hamed", "wolfram": "Wolfram", "kastrup": "Kastrup", "stump": "Stump",
    "wright": "Wright", "rohr": "Rohr", "loughran": "Loughran", "macintyre": "MacIntyre",
    "aquinas": "Aquinas", "kuhn": "Kuhn", "cunningham": "Cunningham",
}
ROSTER = ["levin", "friston", "hoffman", "hawkins", "mcgilchrist", "fredrickson", "carroll",
          "arkanihamed", "wolfram", "kastrup", "stump", "wright", "rohr", "loughran", "macintyre"]
NONROSTER = ["aquinas", "kuhn", "cunningham"]

ID_RE = re.compile(r"\b((?:PRS|CROSS|FLAG|FINDING)-\d+)\b")
SCOPE_RE = re.compile(r"in the ([A-Z][A-Za-z-]+)-tradition")
TRAD_NAME_TO_TAG = {v.replace("-", "").lower(): k for k, v in SURNAME.items()}  # "arkanihamed" etc.

# Pre-colon title phrases that are ALSO research-program/concept labels, so a body match is NOT by itself a
# citation of that specific work. They stay title CANDIDATES (for reconcile step 3) but never override the
# canonical default nor set specific:true. Distinguishing concept-vs-work is model judgment (Rule 5).
AMBIGUOUS_TITLE_PHRASES = {"active inference", "observer theory"}


def load_wc():
    wc = json.load(open(WC_PATH, encoding="utf-8"))["works"]
    canonical = {}
    title_index = []  # (search_phrase_lower, cite_key, tag)
    for k, w in wc.items():
        tag = w["thinker"]
        if w.get("canonical"):
            canonical[tag] = k
        # search phrase = title up to first colon, if long enough to be distinctive
        phrase = w["title"].split(":")[0].strip()
        if len(phrase) >= 12:
            title_index.append((phrase.lower(), k, tag))
    return wc, canonical, title_index


def split_body_footer(text):
    lines = text.split("\n")
    footer_start = None
    for i, l in enumerate(lines):
        if re.match(r"^day:\s", l):
            j = i - 1
            while j >= 0 and lines[j].strip() != "---":
                j -= 1
            footer_start = j if j >= 0 else i
            break
    if footer_start is None:
        return text, "", False
    return "\n".join(lines[:footer_start]), "\n".join(lines[footer_start:]), True


def day_num(fname):
    m = re.search(r"Day-(\d+)", fname)
    return int(m.group(1)) if m else None


def surname_re(surname):
    return re.compile(r"\b" + re.escape(surname) + r"\b")


def first_snippet(body, positions):
    if not positions:
        return ""
    pos = min(positions)
    start = max(body.rfind(". ", 0, pos) + 2, body.rfind("\n", 0, pos) + 1, 0)
    cands = [e for e in (body.find(". ", pos), body.find("\n", pos)) if e != -1]
    end = (min(cands) + 1) if cands else min(len(body), pos + 220)
    return re.sub(r"\s+", " ", body[start:end]).strip()[:240]


def parse_footer_sources(footer):
    out = {"karpathy_wiki_sources": [], "last_qc_at": None, "last_qc_outcome": None}
    in_block = False
    for l in footer.split("\n"):
        if re.match(r"^karpathy_wiki_sources:\s*$", l):
            in_block = True
            continue
        if in_block:
            m = re.match(r'^\s+-\s+"?(.*?)"?\s*$', l)
            if m:
                out["karpathy_wiki_sources"].append(m.group(1))
                continue
            if not l.startswith(" "):  # block ended
                in_block = False
        mo = re.match(r'^last_qc_at:\s*"?([^"]*)"?', l)
        if mo:
            out["last_qc_at"] = mo.group(1)
        mo = re.match(r'^last_qc_outcome:\s*"?([^"]*)"?', l)
        if mo:
            out["last_qc_outcome"] = mo.group(1)
    return out


def main():
    wc, canonical, title_index = load_wc()
    surname_res = {tag: surname_re(SURNAME[tag]) for tag in SURNAME}

    per_thinker = {tag: {"surname": SURNAME[tag], "canonical_cite_key": canonical.get(tag),
                         "days": [], "total_mentions": 0, "occurrences": []} for tag in SURNAME}
    per_day_footer = {}
    flags = {"files_without_footer": [], "unscoped_ids_by_day": {}, "days_scanned": 0,
             "title_hits": []}

    files = sorted(glob.glob(os.path.join(SYN_DIR, "Day-*.md")))
    for path in files:
        fname = os.path.basename(path)
        d = day_num(fname)
        text = open(path, encoding="utf-8").read()
        body, footer, has_footer = split_body_footer(text)
        if not has_footer:
            flags["files_without_footer"].append(fname)
        flags["days_scanned"] += 1

        # ids in body + scope
        ids_by_tag = {}
        unscoped = []
        for m in ID_RE.finditer(body):
            idv = m.group(1)
            window = body[m.end():m.end() + 60]
            sm = SCOPE_RE.search(window)
            if sm:
                tag = TRAD_NAME_TO_TAG.get(sm.group(1).replace("-", "").lower())
                if tag:
                    ids_by_tag.setdefault(tag, []).append(idv)
                    continue
            unscoped.append(idv)
        if unscoped:
            flags["unscoped_ids_by_day"][fname] = sorted(set(unscoped))

        # title-phrase hits per tag: (key, phrase, ambiguous?)
        titles_by_tag = {}
        blo = body.lower()
        for phrase, key, tag in title_index:
            if phrase in blo:
                ambiguous = phrase in AMBIGUOUS_TITLE_PHRASES
                titles_by_tag.setdefault(tag, []).append((key, phrase, ambiguous))
                if not ambiguous:
                    flags["title_hits"].append({"day": d, "cite_key": key})

        # surname mentions -> occurrence per tag
        for tag in SURNAME:
            positions = [m.start() for m in surname_res[tag].finditer(body)]
            hits = titles_by_tag.get(tag, [])
            mentioned = bool(positions) or bool(hits) or tag in ids_by_tag
            if not mentioned:
                continue
            title_candidates = sorted({k for k, _, _ in hits})
            firm = sorted({k for k, _, amb in hits if not amb})   # non-ambiguous specific-work matches
            if firm:
                resolved, is_specific = firm, True
            elif canonical.get(tag):
                resolved, is_specific = [canonical[tag]], False   # generic -> canonical default
            else:
                resolved, is_specific = [], False
            snip_positions = positions[:]
            for k, phrase, _ in hits:   # bias snippet toward a title-mention sentence
                p = blo.find(phrase)
                if p != -1:
                    snip_positions.append(p)
            occ = {"day": d, "resolved_cite_keys": resolved, "specific": is_specific,
                   "title_candidates": title_candidates,
                   "ids": sorted(set(ids_by_tag.get(tag, []))),
                   "mentions": len(positions), "snippet": first_snippet(body, snip_positions)}
            per_thinker[tag]["occurrences"].append(occ)
            per_thinker[tag]["days"].append(d)
            per_thinker[tag]["total_mentions"] += max(len(positions), 1)

        per_day_footer[f"{d:03d}"] = parse_footer_sources(footer) if has_footer else {}

    # ---- write JSON ----
    meta = {
        "generated_for": "foundation §7 step 2 (harvest)",
        "inputs": {"works_cited": WC_PATH, "synthesis_dir": SYN_DIR},
        "days_scanned": flags["days_scanned"],
        "note": "Body citations only. per_day_footer_sources is INTERNAL (foundation §5, stripped at export); "
                "never treat it as a body citation. Generic (surname-only) mentions resolve to the thinker's "
                "canonical cite_key and are flagged specific:false for the reconcile pass (step 3).",
    }
    doc = {"_meta": meta,
           "per_thinker": per_thinker,
           "per_day_footer_sources": per_day_footer,
           "flags": {k: v for k, v in flags.items() if k != "title_hits"}}
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)

    # ---- write MD ----
    L = []
    L.append("---")
    L.append("title: Reference Master — Summa 2026 Commentary")
    L.append("source: commentary-apparatus/reference_master.json (DERIVED — do not hand-edit)")
    L.append(f"days_scanned: {flags['days_scanned']}")
    L.append("---")
    L.append("")
    L.append("# Reference Master — per-thinker occurrence index")
    L.append("")
    L.append("_Foundation §7 step 2. Body mentions of the 15 roster thinkers (+ Aquinas/Kuhn/Cunningham) across the "
             f"{flags['days_scanned']} Summa `synthesis/` bodies, each resolved to a `works_cited.json` cite-key. "
             "**Generated from** `reference_master.json` — never hand-edit. `specific:false` (generic surname → "
             "canonical work) rows are the reconcile queue for step 3. Footer `karpathy_wiki_sources` are internal "
             "(stripped at export, foundation §5) and live in the JSON only._")
    L.append("")
    # summary table
    L.append("## Coverage summary")
    L.append("")
    L.append("| thinker | tag | days cited | body mentions | canonical cite-key |")
    L.append("|---|---|---:|---:|---|")
    for tag in ROSTER + NONROSTER:
        pt = per_thinker[tag]
        nd = len(sorted(set(pt["days"])))
        L.append(f"| {pt['surname']} | `{tag}` | {nd} | {pt['total_mentions']} | "
                 f"`{pt['canonical_cite_key'] or '—'}` |")
    L.append("")
    zero = [SURNAME[t] for t in ROSTER if not per_thinker[t]["days"]]
    if zero:
        L.append(f"> ⚠️ Roster thinkers with **zero** body mentions across the corpus: {', '.join(zero)} "
                 "(coverage gap — confirm expected).")
        L.append("")

    # per-thinker occurrence tables
    for tag in ROSTER + NONROSTER:
        pt = per_thinker[tag]
        if not pt["occurrences"]:
            continue
        L.append(f"## {pt['surname']}  \n`{tag}` — canonical `{pt['canonical_cite_key'] or '—'}`")
        L.append("")
        L.append("| day | resolved cite-key(s) | specific? | ids (body) | claim snippet |")
        L.append("|---:|---|:--:|---|---|")
        for o in sorted(pt["occurrences"], key=lambda x: (x["day"] is None, x["day"])):
            keys = ", ".join(f"`{k}`" for k in o["resolved_cite_keys"]) or "—"
            ids = ", ".join(o["ids"]) or "—"
            snip = o["snippet"].replace("|", "\\|")
            if o["specific"]:
                spec = "✓"
            else:
                cand = [k for k in o.get("title_candidates", []) if k not in o["resolved_cite_keys"]]
                spec = ("gen · cand " + ", ".join(f"`{k}`" for k in cand)) if cand else "gen"
            L.append(f"| {o['day']} | {keys} | {spec} | {ids} | {snip} |")
        L.append("")

    # flags
    L.append("## Flags")
    L.append("")
    L.append(f"- Files without a detected footer: {len(flags['files_without_footer'])}"
             + (f" — {', '.join(flags['files_without_footer'][:10])}" if flags["files_without_footer"] else ""))
    nun = sum(len(v) for v in flags["unscoped_ids_by_day"].values())
    L.append(f"- Unscoped ids in bodies (no `in the <Thinker>-tradition` anchor — mostly CROSS-* spanning two "
             f"thinkers): {nun} occurrences across {len(flags['unscoped_ids_by_day'])} days (see JSON `flags`).")
    L.append(f"- Specific work-title hits in bodies: {len(flags['title_hits'])} (rows marked `✓` above).")
    L.append("")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print(f"OK: scanned {flags['days_scanned']} days.")
    for tag in ROSTER + NONROSTER:
        pt = per_thinker[tag]
        print(f"  {pt['surname']:<14} days={len(set(pt['days'])):>3}  mentions={pt['total_mentions']:>4}  "
              f"canonical={pt['canonical_cite_key']}")


if __name__ == "__main__":
    main()

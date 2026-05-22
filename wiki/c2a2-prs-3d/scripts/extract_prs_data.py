#!/usr/bin/env python3
"""
extract_prs_data.py — Extract PRS-triplet visualization data from the C2A2 vault.

Emits a single JSON bundle (PRS_TRIPLETS, CROSS_CONNECTIONS, FINDINGS, COILS,
plus the THINKER_* maps and a summary) that generate_prs_3d.py injects into
prs_3d.html.

Design notes / standing decisions (2026-05-19):
  * pub_year is NOT stored in the source markdown. We source it, in order:
      1. carry-forward map (existing values baked into the prior prs_3d.html)
      2. citation year regex-extracted from the Resource text
      3. fall back to the Date-Added year  -> recorded as a FALLBACK (fail loud)
    The merged map is written to master/prs_pub_years.json so it is inspectable,
    hand-editable, and stable across nightly runs.
  * COILS (synergistic coils) are derived deterministically as the
    structural-bridge subset of the canonical cross-program connections.
Usage:
  python3 extract_prs_data.py <vault_root> [--carryforward carryforward_pub_years.json] \
      [--out prs_data.json]
"""
import argparse
import datetime
import json
import os
import re
import sys

# NOTE: these three maps are preserved verbatim from the prior prs_3d.html so the
# discipline-wedge layout and colors stay identical across regenerations.
THINKER_COLORS = {
    "levin": "#C45B5B", "friston": "#5A8EAF", "hoffman": "#C08B3E",
    "kastrup": "#8B5DAB", "mcgilchrist": "#3D9E89", "hawkins": "#B87D3E",
    "wolfram": "#4A5E6D", "carroll": "#4E8A5E", "arkanihamed": "#A85D3A",
    "fredrickson": "#C47A9A", "stump": "#A8923A", "rohr": "#9A7A5A",
    "wright": "#5A72A8", "macintyre": "#7A6A8A", "loughran": "#4A8A7A",
    "master": "#C9A84C",
}
THINKER_DISPLAY = {
    "levin": "Levin", "friston": "Friston", "hoffman": "Hoffman",
    "kastrup": "Kastrup", "mcgilchrist": "McGilchrist", "hawkins": "Hawkins",
    "wolfram": "Wolfram", "carroll": "Carroll", "arkanihamed": "Arkani-Hamed",
    "fredrickson": "Fredrickson", "stump": "Stump", "rohr": "Rohr",
    "wright": "Wright", "macintyre": "MacIntyre", "loughran": "Loughran",
    "master": "C2A2 Master",
}
# Primary discipline per tradition (drives the Disciplines cut-axis).
THINKER_DISC = {
    "levin": "Developmental Biology", "friston": "Computational Neuroscience",
    "hoffman": "Cognitive Science", "kastrup": "Philosophy of Mind",
    "mcgilchrist": "Neuropsychiatry", "hawkins": "Computational Neuroscience",
    "wolfram": "Mathematical Physics", "carroll": "Theoretical Physics",
    "arkanihamed": "Theoretical Physics", "fredrickson": "Positive Psychology",
    "stump": "Analytic Theology", "rohr": "Contemplative Theology",
    "wright": "Historical Theology", "macintyre": "Moral Philosophy",
    "loughran": "Systems Integration", "master": "Systems Integration",
}

# Substrings that mark a cross-connection as a synergistic coil (a shared
# Resource bridging multiple Problem->Solution chains across traditions).
COIL_MARKERS = (
    "structural analog", "structural homolog", "structural identit",
    "structural equivalen", "structural bridge", "explanatory bridge",
    "architectural homolog", "formal equivalen", "formal chain",
    "mechanistic bridge", "isomorph", "structural homo", "deep structural",
    "post-spacetime_convergence", "ontological_convergence",
    "structural_bridge", "bridge_candidate", "bridge_upgrade",
)

YEAR_RE = re.compile(r"\b(1[5-9]\d\d|20[0-2]\d)\b")
CUR_YEAR = datetime.date.today().year


def parse_blocks(text, id_prefix, allow_unindented=False):
    """Yield (id_num, {field: value}) blocks for lines like '<PREFIX>-NN:'.
    Triplet/cross fields are indented; the findings file is NOT, so pass
    allow_unindented=True there (otherwise its fields parse as empty)."""
    head = re.compile(r"^" + re.escape(id_prefix) + r"-(\d+)\s*:\s*$")
    indent = r"\s{0,4}" if allow_unindented else r"\s{1,4}"
    field = re.compile(r"^" + indent + r"([A-Za-z][A-Za-z /]*?):\s*(.*)$")
    cur_id, cur, last_key = None, None, None
    for raw in text.splitlines():
        m = head.match(raw)
        if m:
            if cur_id is not None:
                yield cur_id, cur
            cur_id, cur, last_key = m.group(1), {}, None
            continue
        if cur is None:
            continue
        fm = field.match(raw)
        if fm:
            last_key = fm.group(1).strip().lower()
            cur[last_key] = fm.group(2).strip()
        elif last_key and raw.strip():
            cur[last_key] += " " + raw.strip()
        elif not raw.strip():
            last_key = None
    if cur_id is not None:
        yield cur_id, cur


def derive_pub_year(resource, date_added):
    """Citation year from Resource text; else Date-Added year. Returns (year, is_fallback)."""
    cands = [int(y) for y in YEAR_RE.findall(resource or "") if int(y) <= CUR_YEAR]
    if cands:
        # Prefer a year in a citation-like context (", YYYY" or "(... YYYY)").
        cited = [int(y) for y in re.findall(r"[,(][^,()]*?\b(1[5-9]\d\d|20[0-2]\d)\b", resource or "")
                 if int(y) <= CUR_YEAR]
        return (cited[-1] if cited else cands[-1]), False
    if date_added:
        ym = re.match(r"(\d{4})", date_added)
        if ym:
            return int(ym.group(1)), True
    return CUR_YEAR, True


def extract_triplets(vault, carryforward):
    triplets, fallbacks, seen_ids = [], [], {}
    sources = []
    trad_dir = os.path.join(vault, "traditions")
    for thinker in sorted(os.listdir(trad_dir)):
        p = os.path.join(trad_dir, thinker, "prs_triplets.md")
        if os.path.isfile(p):
            sources.append((thinker, p))
    master = os.path.join(vault, "master", "C2A2_prs_triplets.md")
    if os.path.isfile(master):
        sources.append(("master", master))

    for thinker, path in sources:
        text = open(path, encoding="utf-8", errors="replace").read()
        for num, fields in parse_blocks(text, "PRS"):
            tid = "%s-PRS-%s" % (thinker, num)
            if tid in seen_ids:  # duplicate id within a tradition (e.g. arkanihamed PRS-10)
                seen_ids[tid] += 1
                tid = "%s-dup%d" % (tid, seen_ids[tid])
                fallbacks.append("DUPLICATE ID rewritten -> %s (in %s)" % (tid, path))
            else:
                seen_ids[tid] = 0
            resource = fields.get("resource", "")
            date_added = fields.get("date added", "")
            cf = carryforward.get(tid) or carryforward.get("%s-PRS-%s" % (thinker, num))
            if cf and isinstance(cf.get("pub_year"), int):
                pub_year, is_fb = cf["pub_year"], False
            else:
                pub_year, is_fb = derive_pub_year(resource, date_added)
                if is_fb:
                    fallbacks.append("pub_year fallback (Date-Added) -> %s = %d" % (tid, pub_year))
            triplets.append({
                "id": tid, "thinker": thinker, "prs_num": num,
                "label": fields.get("label", ""),
                "problem": fields.get("problem", ""),
                "resource": resource,
                "solution": fields.get("solution", ""),
                "date": (cf or {}).get("date") or date_added,
                "pub_year": pub_year,
                "confidence": fields.get("confidence", ""),
            })
    return triplets, fallbacks


CROSS_HEAD = re.compile(r"^CROSS-(\d+)\s*(?::|[—–-])\s*(.*)$")
CROSS_FIELD = re.compile(r"^\s{1,4}([A-Za-z][A-Za-z /]*?):\s*(.*)$")


def programs_from_title(title):
    """Em-dash entries encode programs as 'Levin x Hoffman x Wolfram (...)'."""
    head = re.split(r"[(—]", title, 1)[0]  # text before '(' or em-dash subtitle
    parts = [p.strip() for p in re.split(r"[×x]\s|\s[×x]\s|×", head) if p.strip()]
    return ", ".join(p + (" Agent" if not p.endswith(("Agent", "core", "C2A2")) else "") for p in parts)


def extract_cross(vault):
    """Handle BOTH header schemas: 'CROSS-NN:' (colon) and 'CROSS-NN - Title' (em-dash).
    Dedupe by id keeping the LAST (newer/richer em-dash) occurrence; flag dups."""
    p = os.path.join(vault, "master", "cross_program_index.md")
    text = open(p, encoding="utf-8", errors="replace").read()
    blocks, dups = {}, []
    cur_id, inline, cur, last_key = None, "", None, None
    order = []
    for raw in text.splitlines():
        m = CROSS_HEAD.match(raw)
        if m:
            if cur_id is not None:
                if cur_id in blocks:
                    dups.append(cur_id)
                blocks[cur_id] = (inline, cur)
                if cur_id not in order:
                    order.append(cur_id)
            cur_id, inline, cur, last_key = m.group(1), m.group(2).strip(), {}, None
            continue
        if cur is None:
            continue
        fm = CROSS_FIELD.match(raw)
        if fm:
            last_key = fm.group(1).strip().lower()
            cur[last_key] = fm.group(2).strip()
        elif last_key and raw.strip():
            cur[last_key] += " " + raw.strip()
        elif not raw.strip():
            last_key = None
    if cur_id is not None:
        if cur_id in blocks:
            dups.append(cur_id)
        blocks[cur_id] = (inline, cur)
        if cur_id not in order:
            order.append(cur_id)

    out = []
    for num in sorted(order, key=int):
        inline, f = blocks[num]
        nature = f.get("nature of connection") or f.get("type") or ""
        question = f.get("question/insight") or f.get("question") or f.get("insight") or inline
        programs = f.get("programs involved") or f.get("programs") or ""
        if not programs and inline:
            programs = programs_from_title(inline)
        # Discovery year: latest year mentioned in the entry (First appeared /
        # Source / Status / Notes / title). Drives coil altitude. Defaults 2026.
        blob = " ".join([inline] + [str(v) for v in f.values()])
        yrs = [int(y) for y in re.findall(r"\b(19\d\d|20[0-2]\d)\b", blob) if int(y) <= CUR_YEAR]
        year = max(yrs) if yrs else 2026
        out.append({
            "id": "CROSS-%s" % num,
            "question": question,
            "programs": programs,
            "nature": nature,
            "year": year,
            "notes": f.get("notes", ""),
        })
    out_dups = sorted(set(dups), key=int)
    return out, out_dups


def extract_findings(vault):
    p = os.path.join(vault, "flags", "pattern_detector_findings.md")
    text = open(p, encoding="utf-8", errors="replace").read()
    out = []
    for num, f in parse_blocks(text, "FINDING", allow_unindented=True):
        # The file carries two schemas: older entries use 'Finding:'; newer ones
        # use 'Title:' + 'Signal:'. Fall back across both so every entry has text.
        finding_text = f.get("finding") or " - ".join(
            x for x in [f.get("title"), f.get("signal")] if x) or ""
        out.append({
            "id": "FINDING-%s" % num,
            "date": f.get("date evaluated") or f.get("date") or "",
            "programs": f.get("programs", ""),
            "type": f.get("evaluation type") or f.get("type") or "",
            "finding": finding_text,
        })
    return out


def derive_coils(cross):
    """A coil = a structural-bridge cross-connection. Returns coil records."""
    coils = []
    for c in cross:
        nat = (c.get("nature") or "").lower()
        if any(m in nat for m in COIL_MARKERS):
            progs = [p.strip() for p in re.split(r"[,;]", c.get("programs", "")) if p.strip()]
            coils.append({
                "id": "COIL-" + c["id"].split("-", 1)[1],
                "cross_id": c["id"],
                "label": c["question"],
                "nature": c["nature"],
                "programs": c["programs"],
                "program_count": len(progs),
                "year": c.get("year", 2026),
                "notes": c.get("notes", ""),
            })
    return coils


GEN_STOP = set((
    "the a an of to and or in on for with as is are be by that this it its their his her "
    "from at into not but which can may also more such these those one two through over "
    "across each both per via they them then than what when where how why who whom whose "
    "we our you your i me my he she his hers theirs all any some no nor so if then else "
    "model models theory account framework approach problem resource solution agent agents "
    "system systems process processes level levels structure structures within between "
    "human humans world reality without using used use new same other another rather"
).split())


def gen_tokens(s):
    return set(w for w in re.findall(r"[a-z]{4,}", (s or "").lower()) if w not in GEN_STOP)


def gen_chains(triplets, min_shared=4, min_jaccard=0.18):
    """Directed 'generative coil': triplet A's SOLUTION feeds triplet B's RESOURCE,
    across traditions. Conservative significant-token overlap (descriptive, not exact)."""
    sol = {t["id"]: gen_tokens(t["solution"]) for t in triplets}
    res = {t["id"]: gen_tokens(t["resource"]) for t in triplets}
    out = []
    for a in triplets:
        sa = sol[a["id"]]
        if len(sa) < min_shared:
            continue
        for b in triplets:
            if a["id"] == b["id"] or a["thinker"] == b["thinker"]:
                continue
            rb = res[b["id"]]
            if len(rb) < min_shared:
                continue
            inter = sa & rb
            if len(inter) >= min_shared:
                j = len(inter) / len(sa | rb)
                if j >= min_jaccard:
                    out.append({
                        "source": a["id"], "target": b["id"],
                        "thinker_source": a["thinker"], "thinker_target": b["thinker"],
                        "shared": sorted(inter)[:6], "score": round(j, 3),
                    })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vault")
    ap.add_argument("--carryforward", default="")
    ap.add_argument("--out", default="prs_data.json")
    ap.add_argument("--write-pubmap", action="store_true",
                    help="Persist merged pub_year map into <vault>/master/prs_pub_years.json")
    args = ap.parse_args()

    carryforward = {}
    if args.carryforward and os.path.isfile(args.carryforward):
        carryforward = json.load(open(args.carryforward))

    triplets, fallbacks = extract_triplets(args.vault, carryforward)
    cross, cross_dups = extract_cross(args.vault)
    findings = extract_findings(args.vault)
    coils = derive_coils(cross)
    generative = gen_chains(triplets, min_shared=3, min_jaccard=0.15)
    if cross_dups:
        fallbacks.append("CROSS dup headers (kept newer em-dash form): " + ", ".join("CROSS-" + d for d in cross_dups))

    # Persist the merged pub_year map for inspection / hand-curation.
    pubmap = {t["id"]: {"date": t["date"], "pub_year": t["pub_year"]} for t in triplets}
    if args.write_pubmap:
        pubpath = os.path.join(args.vault, "master", "prs_pub_years.json")
        try:
            json.dump(pubmap, open(pubpath, "w"), indent=0)
            print("wrote %s" % pubpath)
        except OSError as e:
            print("WARN: could not write %s (%s)" % (pubpath, e), file=sys.stderr)

    disciplines = sorted({THINKER_DISC.get(t["thinker"], "Integration") for t in triplets})
    bundle = {
        "PRS_TRIPLETS": triplets,
        "CROSS_CONNECTIONS": cross,
        "FINDINGS": findings,
        "COILS": coils,
        "GENERATIVE": generative,
        "DISCIPLINES": disciplines,
        "THINKER_DISC": {t["thinker"]: THINKER_DISC.get(t["thinker"], "Integration") for t in triplets},
        "THINKER_COLORS": {t["thinker"]: THINKER_COLORS.get(t["thinker"], "#888888") for t in triplets},
        "THINKER_DISPLAY": {t["thinker"]: THINKER_DISPLAY.get(t["thinker"], t["thinker"]) for t in triplets},
        "summary": {
            "triplets": len(triplets),
            "traditions": len({t["thinker"] for t in triplets}),
            "cross_connections": len(cross),
            "coils": len(coils),
            "generative": len(generative),
            "findings": len(findings),
            "pub_year_fallbacks": len(fallbacks),
            "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        },
    }
    json.dump(bundle, open(args.out, "w"), ensure_ascii=False)

    s = bundle["summary"]
    print("=== extract_prs_data summary ===")
    for k in ("triplets", "traditions", "cross_connections", "coils", "generative", "findings", "pub_year_fallbacks"):
        print("  %-20s %s" % (k, s[k]))
    print("  pub_year carried-fwd  %d / %d" % (
        sum(1 for t in triplets if t["id"] in carryforward), len(triplets)))
    if fallbacks:
        print("--- FALLBACKS / FLAGS (fail loud) ---")
        for f in fallbacks:
            print("  " + f)


if __name__ == "__main__":
    main()

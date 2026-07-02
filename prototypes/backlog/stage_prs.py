#!/usr/bin/env python3
"""Track A PRS processor SKELETON — deterministic staging, no live writes.

This is build-order part 2: it does everything code can do (Rule 5), and STOPS at
the model-judgment boundary. For each manifest unit it:
  - reads the card's pre-drafted `PRS-CANDIDATE-NN` blocks (Problem/Resource/
    Solution/Confidence/Evidence),
  - computes the next live `PRS-NN` for that tradition by reading
    traditions/<key>/prs_triplets.md (so numbering is correct and contiguous),
  - renders a ready-to-paste append block (PRS-N: Problem/Resource/Solution +
    Date Added + Source w/ proposal_id + Confidence) into a per-unit staging file,
  - writes/updates prs_qc_trace.csv with n_candidates and first_prs_n.

It writes ONLY into <OUT>/prs_staging/ and the qc_trace — never into the live
traditions/ , master/ , or PROCESSED_LOG.md. The attended loop (part 3, metered)
reviews each staged block, accepts/trims/dedups against existing triplets, routes
cross-tradition signals into master/cross_program_index.md, then commits.

Guardrails honored: confidence labels pass through as authored (High/Medium/
Speculative — never Easy/Low/Hard); candidate COUNT comes from `PRS-CANDIDATE-`
lines in source, not rendered chips; provenance stays the card's own tradition_key
(the PRS method is Loughran's — never reattributed).

Usage:
  python3 stage_prs.py <vault_root> <prs_manifest.json> [OUT_DIR]
"""
import json, os, re, sys, csv, collections

VAULT = sys.argv[1]
MANIFEST = sys.argv[2]
OUT = sys.argv[3] if len(sys.argv) > 3 else "/tmp"
STAGE = os.path.join(OUT, "prs_staging")

FIELD = ("Problem", "Resource", "Solution", "Confidence", "Evidence")

def parse_candidates(txt):
    """Return list of dicts for each PRS-CANDIDATE-NN block."""
    blocks = re.split(r'^PRS-CANDIDATE-\d+\s*:\s*$', txt, flags=re.M)[1:]
    # re.split on the header line; each block is the indented body until next header
    # but headers may have trailing content; re-find precisely instead:
    out = []
    for m in re.finditer(r'^PRS-CANDIDATE-\d+\s*:\s*\n(.*?)(?=^PRS-CANDIDATE-\d+\s*:|^\#\#|\Z)',
                         txt, flags=re.M | re.S):
        body = m.group(1)
        d = {}
        for f in FIELD:
            fm = re.search(r'^\s*%s:\s*(.+?)(?=^\s*(?:Problem|Resource|Solution|Confidence|Evidence):|\Z)'
                           % f, body, flags=re.M | re.S)
            if fm:
                d[f] = " ".join(fm.group(1).split())
        if d.get("Problem") and d.get("Solution"):
            out.append(d)
    return out

def next_prs_n(vault, trad):
    p = os.path.join(vault, "traditions", trad, "prs_triplets.md")
    if not os.path.exists(p):
        return 1, None
    txt = open(p, errors="ignore").read()
    nums = [int(n) for n in re.findall(r'^PRS-(\d+)\s*:', txt, flags=re.M)]
    return (max(nums) + 1 if nums else 1), p

def render(prs_n, cand, source_date, source_title, pid):
    src = source_title
    if pid:
        src = (src + "; " if src else "") + pid
    return (
        "PRS-%d:\n" % prs_n +
        "  Problem: %s\n" % cand.get("Problem", "") +
        "  Resource: %s\n" % cand.get("Resource", "") +
        "  Solution: %s\n" % cand.get("Solution", "") +
        "  Date Added: %s\n" % source_date +
        "  Source: %s\n" % src +
        "  Confidence: %s\n" % cand.get("Confidence", "Medium")
    )

def main():
    units = json.load(open(MANIFEST))
    os.makedirs(STAGE, exist_ok=True)
    qc_path = os.path.join(OUT, "prs_qc_trace.csv")

    # load existing qc rows (keep status/notes the attended loop may have set)
    qc = {}
    if os.path.exists(qc_path):
        for row in csv.DictReader(open(qc_path)):
            qc[row["unit_id"]] = row

    # per-tradition running counter so multiple units in one tradition number forward
    trad_next = {}
    staged = 0
    total_candidates = 0
    for u in units:
        trad = u["tradition"]
        card = os.path.join(VAULT, u["primary_file"])
        txt = open(card, errors="ignore").read()
        cands = parse_candidates(txt)
        total_candidates += len(cands)

        if trad not in trad_next:
            trad_next[trad], _ = next_prs_n(VAULT, trad)
        start_n = trad_next[trad]

        out_lines = ["# STAGED PRS append for %s  (unit %s)" % (trad, u["unit_id"]),
                     "# source: %s  [%s]" % (u["title"], u["source_date"]),
                     "# files: %s" % ", ".join(u["files"]),
                     "# append target: traditions/%s/prs_triplets.md" % trad,
                     "# ATTENDED: vet/dedup against existing triplets before commit",
                     ""]
        n = start_n
        for c in cands:
            out_lines.append(render(n, c, u["source_date"], u["title"],
                                    u["proposal_ids"][0]))
            n += 1
        trad_next[trad] = n

        sp = os.path.join(STAGE, "%s__%s.txt" % (trad, u["unit_id"]))
        open(sp, "w").write("\n".join(out_lines) + "\n")
        staged += 1

        qc[u["unit_id"]] = dict(
            unit_id=u["unit_id"], tradition=trad, source_date=u["source_date"],
            n_candidates=len(cands), processed_by="stage_prs",
            date_processed="", triplets_emitted=len(cands),
            cross_refs="", first_prs_n=start_n,
            status="STAGED", notes=qc.get(u["unit_id"], {}).get("notes", ""))

    cols = ["unit_id", "tradition", "source_date", "n_candidates", "processed_by",
            "date_processed", "triplets_emitted", "cross_refs", "first_prs_n",
            "status", "notes"]
    with open(qc_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for u in units:
            w.writerow({k: qc[u["unit_id"]].get(k, "") for k in cols})

    # coverage gate
    ok = staged == len(units)
    print("units in manifest :", len(units))
    print("units staged      :", staged)
    print("candidate triplets:", total_candidates)
    print("staging dir       :", STAGE)
    print("coverage gate     :", "PASS" if ok else "FAIL")
    if not ok:
        print("COVERAGE FAIL: staged %d of %d units" % (staged, len(units)),
              file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()

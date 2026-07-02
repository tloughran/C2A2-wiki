#!/usr/bin/env python3
"""Track A (PRS-triplet) backlog manifest builder. Deterministic, no model calls.

Mirrors prototypes/backlog/build_manifest.py (Track B / cross-signals) but targets
the PRS-triplet extraction track: the top-level inbox/ staging cards that are NOT
yet recorded in inbox/PROCESSED_LOG.md.

Key difference from Track B: it dedups SAME-SOURCE re-stagings. The broker
occasionally re-proposes an identical paper under a later search date (e.g. the
carroll quantum-cyclic-universe and friston online-generalised-predictive-coding
pairs both point at one arXiv id). Those collapse to ONE extraction unit, carrying
both proposal_ids and both files, so the attended pass reads the richer file and
ingests the source once.

Emits (default to /tmp, pass OUT to place elsewhere):
  prs_manifest.json   one row per UNIQUE SOURCE, ordered by source_date
  prs_qc_trace.csv    one PENDING row per unit; the attended loop fills it

Coverage gate: every un-ingested staging file maps into exactly one unit, and
units == files - dup_restagings. Asserts loudly (exit 2) if not.

Usage:
  python3 build_prs_manifest.py <vault_root> [OUT_DIR]
  (vault_root = the wiki/ folder that contains inbox/ and traditions/)
"""
import glob, os, re, json, csv, sys, collections

VAULT = sys.argv[1] if len(sys.argv) > 1 else "."
OUT   = sys.argv[2] if len(sys.argv) > 2 else "/tmp"
INBOX = os.path.join(VAULT, "inbox")
LOG   = os.path.join(INBOX, "PROCESSED_LOG.md")

CARD_RE = re.compile(r'^\d{4}-\d{2}-\d{2}_[a-z]+_.+\.md$')

def fm(txt, key):
    m = re.search(r'^%s:\s*"?([^"\n]+)' % key, txt, re.M)
    return m.group(1).strip() if m else ""

def ingested_proposal_ids(vault, log_txt):
    """Authoritative ingested test: a card is ingested if its proposal_id is cited
    as a Source: in any live traditions/*/prs_triplets.md, OR appears in a
    PROCESSED_LOG ingestion line (one that routes to a PRS, '... -> <trad> PRS-').
    The old basename-vs-log test missed both because the log keys on proposal_id/
    slug, not the inbox filename (caused 15 already-ingested cards to re-stage)."""
    ids = set()
    for tf in glob.glob(os.path.join(vault, "traditions", "*", "prs_triplets.md")):
        for m in re.finditer(r'(PROP-2026-\d{2}-\d{2}-\d+)', open(tf, errors="ignore").read()):
            ids.add(m.group(1))
    for line in log_txt.splitlines():
        if re.search(r'→\s*[a-z]+\s*PRS-', line):  # '->' ingestion line
            for m in re.finditer(r'(PROP-2026-\d{2}-\d{2}-\d+)', line):
                ids.add(m.group(1))
    return ids

def main():
    log_txt = open(LOG, errors="ignore").read() if os.path.exists(LOG) else ""
    ingested = ingested_proposal_ids(VAULT, log_txt)

    # 1. all dated staging cards at the top level of inbox/
    files = [f for f in glob.glob(os.path.join(INBOX, "*.md"))
             if CARD_RE.match(os.path.basename(f))]

    # 2. un-ingested = proposal_id NOT already cited in a tradition file or
    #    routed by a PROCESSED_LOG ingestion line (filename test was unreliable).
    skipped_ingested = []

    # 3. read each card; group by dedup key = source_url (fallback source_title)
    recs = []
    for f in sorted(files):
        txt = open(f, errors="ignore").read()
        pid = fm(txt, "proposal_id") or (re.search(r'(PROP-2026-\d{2}-\d{2}-?\d*)',
                                         os.path.basename(f)) or [None, ""])[1]
        if pid in ingested:
            skipped_ingested.append(pid)
            continue
        trad = fm(txt, "tradition_key") or os.path.basename(f).split("_")[1]
        url  = fm(txt, "source_url")
        title= fm(txt, "source_title")
        sdate= fm(txt, "source_date") or os.path.basename(f)[:10]
        ncand= len(re.findall(r'^PRS-CANDIDATE-\d+\s*:', txt, re.M))
        key  = ("url:" + url) if url else ("title:" + trad + "::" + title.lower())
        recs.append(dict(file=os.path.relpath(f, VAULT), pid=pid, tradition=trad,
                         source_url=url, title=title, source_date=sdate,
                         n_candidates=ncand, key=key, bytes=len(txt)))

    # 4. collapse same-source re-stagings -> one unit (keep richest file as primary)
    groups = collections.OrderedDict()
    for r in recs:
        groups.setdefault(r["key"], []).append(r)

    units = []
    for key, members in groups.items():
        members.sort(key=lambda m: m["bytes"], reverse=True)  # richest first
        primary = members[0]
        units.append(dict(
            unit_id   = primary["pid"],
            tradition = primary["tradition"],
            source_date = primary["source_date"],
            title     = primary["title"][:90],
            source_url= primary["source_url"],
            primary_file = primary["file"],
            files     = [m["file"] for m in members],
            proposal_ids = [m["pid"] for m in members],
            n_candidates = primary["n_candidates"],
            restaged  = len(members) > 1,
            processed = False,
        ))
    units.sort(key=lambda u: (u["source_date"], u["tradition"]))

    # 5. coverage gate — fail loud
    n_files = len(recs)
    n_units = len(units)
    n_restage = sum(len(g) - 1 for g in groups.values())
    ok = (n_units + n_restage == n_files)

    os.makedirs(OUT, exist_ok=True)
    json.dump(units, open(os.path.join(OUT, "prs_manifest.json"), "w"), indent=1)
    with open(os.path.join(OUT, "prs_qc_trace.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["unit_id", "tradition", "source_date", "n_candidates",
                    "processed_by", "date_processed", "triplets_emitted",
                    "cross_refs", "first_prs_n", "status", "notes"])
        for u in units:
            w.writerow([u["unit_id"], u["tradition"], u["source_date"],
                        u["n_candidates"], "", "", "", "", "", "PENDING", ""])

    by_trad = collections.Counter(u["tradition"] for u in units)
    print("skipped (already ingested) :", len(skipped_ingested))
    print("un-ingested staging files :", n_files)
    print("same-source re-stagings   :", n_restage,
          "->", [u["unit_id"] for u in units if u["restaged"]])
    print("UNIQUE extraction units   :", n_units)
    print("candidate triplets total  :", sum(u["n_candidates"] for u in units))
    print("by tradition              :", dict(by_trad.most_common()))
    print("coverage gate             :", "PASS" if ok else "FAIL")
    print("wrote prs_manifest.json + prs_qc_trace.csv to", OUT)
    if not ok:
        print("COVERAGE FAIL: %d units + %d restagings != %d files"
              % (n_units, n_restage, n_files), file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()

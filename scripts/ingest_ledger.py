#!/usr/bin/env python3
"""Derived compile-state ledger: how many proposals are actually un-ingested?

WHY THIS EXISTS
---------------
Three different backlog figures circulated in this project for eight weeks -- 315
(file mtime), 158 (stale note), 99 (PROCESSED_LOG slug diff). All three were
artifacts of the measuring instrument. The real number on 2026-08-26 was 2.

The authoritative test already existed, in prototypes/backlog/build_prs_manifest.py
(2026-06-30): a card is ingested iff its proposal_id is cited in a live
traditions/*/prs_triplets.md, OR routed by a PROCESSED_LOG ingestion line. That test
is right in concept. Nothing ever called it on a schedule, so the wrong numbers kept
circulating -- and its implementation carried two defects (below).

A correct measurement that nothing schedules or reports is indistinguishable from one
that does not exist. This module is the caller.

TWO DEFECTS FIXED HERE (both measured against the live vault, 2026-08-26)
------------------------------------------------------------------------
1. ARROW FORM. The original matched only the Unicode arrow:  r'→\\s*[a-z]+\\s*PRS-'
   The live log uses BOTH: 79 lines with U+2192, 61 lines with ASCII '->'.
   61 ingestion lines were invisible to that branch of the gate.

2. PROPOSAL-ID SHAPE. The original id pattern was  r'PROP-2026-\\d{2}-\\d{2}-\\d+'
   which cannot match PROP-2026-04-09-SUPP-001 (13 occurrences in the vault) or the
   placeholder ids PROP-2026-07-28-00x / -07-29-00x.
   Consequence, already paid once: the Hawkins Thousand Brains supplement produced six
   triplets (hawkins PRS-10..15) and was still read as un-ingested. It was re-staged and
   re-derived, and qc_prs.py caught "6 hawkins SUPP-001 re-derivation dups" downstream.
   That was recorded as a QC catch. It was a gate defect.

SCOPE
-----
Read-only. Reports; does not write to the vault and does not mutate PROCESSED_LOG.
Two queues are reported separately because they are different things:
  - proposals/approved/  -> the COMPILE queue (Tom said yes, pipeline has not ingested)
  - inbox/*.md top level -> the staging cards build_prs_manifest.py works from
proposals/pending/ is deliberately EXCLUDED. Pending means awaiting Tom's approval
decision. It is a review queue, not a compile queue, and counting it as backlog is how
the 78/80 figure would come back.

USAGE
    python3 scripts/ingest_ledger.py <vault_root>            # human report
    python3 scripts/ingest_ledger.py <vault_root> --json     # machine readable
    python3 scripts/ingest_ledger.py <vault_root> --max-open N   # exit 1 if open > N
<vault_root> is the wiki/ folder containing inbox/ and traditions/.
"""
import glob
import json
import os
import re
import sys

# Accepts PROP-2026-04-16-006, PROP-2026-04-09-SUPP-001, PROP-2026-07-28-00x.
PROP_ID = re.compile(r'PROP-\d{4}-\d{2}-\d{2}-[A-Za-z0-9]+(?:-\d+)?')

# Both arrow forms. The live log contains both and always has.
INGEST_LINE = re.compile(r'(?:→|->)\s*[a-z]+\s*PRS-')

# A DECIDED outcome that yielded no triplet. This is a recorded decision, NOT a gap.
# Conflating it with "never looked at" is the original sin this whole module exists to
# undo: on the live vault it is the difference between OPEN=20 and OPEN=5.
ZERO_YIELD = re.compile(r'\+0\b|no-net-new|citation-upgrade|\bHELD\b|\bNO-OP\b', re.I)


def ingested_proposal_ids(vault, log_txt):
    """Proposal ids with evidence of having produced at least one triplet.

    Two independent sources of evidence, unioned:
      A. cited inside a live traditions/*/prs_triplets.md (the PRIMARY record --
         each triplet names the proposal that produced it in its Label:)
      B. routed by a PROCESSED_LOG line that reaches a PRS ('-> <trad> PRS-')

    Source A is authoritative. Source B catches proposals whose triplets were later
    edited or renumbered out of recognition.
    """
    ids = set()
    for tf in sorted(glob.glob(os.path.join(vault, "traditions", "*", "prs_triplets.md"))):
        with open(tf, errors="ignore") as fh:
            ids.update(PROP_ID.findall(fh.read()))
    for line in log_txt.splitlines():
        if INGEST_LINE.search(line):
            ids.update(PROP_ID.findall(line))
    return ids


def decided_zero_ids(log_txt):
    """Proposal ids the log records as DECIDED with zero yield.

    '+0', 'no-net-new', 'citation-upgrade', 'HELD', 'NO-OP' are all outcomes somebody
    reached on purpose -- the McGilchrist commencement card, for instance, is HELD at a
    verification gate because no transcript could be found. Reporting these as backlog
    would recreate the phantom debt in a new costume.

    An id that is BOTH ingested and zero-marked counts as ingested; the caller
    subtracts. A zero-yield line that names no id contributes nothing.
    """
    ids = set()
    for line in log_txt.splitlines():
        if ZERO_YIELD.search(line) and not INGEST_LINE.search(line):
            ids.update(PROP_ID.findall(line))
    return ids


def _proposal_id(path):
    """proposal_id from frontmatter, falling back to one embedded in the filename."""
    with open(path, errors="ignore") as fh:
        txt = fh.read()
    m = re.search(r'^proposal_id:\s*"?([^"\n]+)', txt, re.M)
    if m:
        return m.group(1).strip()
    m = PROP_ID.search(os.path.basename(path))
    return m.group(0) if m else None


def survey(vault):
    log_path = os.path.join(vault, "inbox", "PROCESSED_LOG.md")
    log_txt = open(log_path, errors="ignore").read() if os.path.exists(log_path) else ""
    ingested = ingested_proposal_ids(vault, log_txt)
    zero = decided_zero_ids(log_txt) - ingested

    queues = {
        "approved": sorted(glob.glob(os.path.join(vault, "inbox", "proposals", "approved", "*.md"))),
        "staging": [f for f in sorted(glob.glob(os.path.join(vault, "inbox", "*.md")))
                    if re.match(r'^\d{4}-\d{2}-\d{2}_[a-z]+_.+\.md$', os.path.basename(f))],
    }

    out = {"ingested_ids": len(ingested), "decided_zero_ids": len(zero),
           "queues": {}, "no_proposal_id": []}
    for name, files in queues.items():
        n_ing = n_zero = 0
        open_files = []
        for f in files:
            pid = _proposal_id(f)
            if pid is None:
                out["no_proposal_id"].append(os.path.relpath(f, vault))
                continue
            if pid in ingested:
                n_ing += 1
            elif pid in zero:
                n_zero += 1
            else:
                open_files.append({"file": os.path.relpath(f, vault), "proposal_id": pid})
        out["queues"][name] = {
            "total": len(files),
            "ingested": n_ing,
            "decided_zero": n_zero,
            "open": len(open_files),
            "open_files": open_files,
        }
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip().splitlines()[0], file=sys.stderr)
        print("usage: ingest_ledger.py <vault_root> [--json] [--max-open N]", file=sys.stderr)
        return 2
    vault = argv[1]
    if not os.path.isdir(os.path.join(vault, "traditions")):
        print("not a vault root (no traditions/): %s" % vault, file=sys.stderr)
        return 2

    data = survey(vault)

    if "--json" in argv:
        print(json.dumps(data, indent=1))
    else:
        print("distinct proposal ids: ingested=%d  decided-zero=%d"
              % (data["ingested_ids"], data["decided_zero_ids"]))
        for name, q in data["queues"].items():
            print("\n%-9s total=%-4d ingested=%-4d decided-zero=%-3d OPEN=%d"
                  % (name, q["total"], q["ingested"], q["decided_zero"], q["open"]))
            for row in q["open_files"]:
                print("    OPEN  %s  (%s)" % (row["file"], row["proposal_id"]))
        if data["no_proposal_id"]:
            print("\nfiles with NO proposal_id (cannot be judged):")
            for f in data["no_proposal_id"]:
                print("    %s" % f)

    if "--max-open" in argv:
        limit = int(argv[argv.index("--max-open") + 1])
        total_open = sum(q["open"] for q in data["queues"].values())
        if total_open > limit:
            print("\nOPEN=%d exceeds --max-open %d" % (total_open, limit), file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

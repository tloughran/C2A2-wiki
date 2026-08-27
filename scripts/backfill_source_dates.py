#!/usr/bin/env python3
"""backfill_source_dates.py -- give PRS triplets a real PUBLICATION date.

THE PROBLEM
  extract_prs_data.py sets a triplet's `date` to `carryforward.date or date_added`.
  Where no curated date exists it falls back to Date-Added -- when C2A2 *noticed*
  the source, not when the thinker published it. The vertical axis of the
  connectome therefore mixes two different meanings, and its largest cluster is an
  ingestion event (80 triplets on 2026-08-09), not a publication event.

  Meanwhile the proposal that produced each triplet already carries `source_date`
  in its frontmatter -- a genuine publication date -- and nothing ever read it.

WHAT THIS DOES
  Enriches the carryforward map (wiki/c2a2-prs-3d/prs_pub_years.json) with
  source_date, keyed by triplet id, so the EXISTING regen path picks it up with no
  change to extract_prs_data.py or regen_prs_connectome.sh.

DELIBERATELY CONSERVATIVE
  * Tier A joins only. build_provenance.py also emits fuzzy B/C matches (ratio
    >= 0.60). A fuzzy match is fine for *reporting* a lineage; it is not fine for
    silently stamping a DATE onto a node, where a wrong answer is invisible.
    B/C are counted and reported, never applied.
  * Fills holes freely. For an entry that ALREADY carries a date, overwrites only
    when that date provably came from capture rather than curation -- i.e. it
    equals the triplet's own ingested_date in the provenance join. Measured
    2026-08-27: 97 tier-A entries were already dated, ALL 97 disagreed with their
    proposal's source_date, 95 were LATER than it (median 41 days, max 543), and
    they clustered on ingestion days (2026-04-16 x25, 2026-04-28 x21). The
    carryforward map, documented as holding curated pub dates, had been polluted
    with Date-Added values persisted by --write-pubmap. A blanket "never
    overwrite" rule would have preserved exactly the corruption being fixed.
    Anything else that is already dated is left alone.
  * Well-formed YYYY-MM-DD only. Year-only ("2026") and month-only ("2026-07")
    source_dates are rejected -- coercing them to Jan 1 would manufacture a false
    cluster, which is the exact failure being fixed.

Usage:
  python3 scripts/build_provenance.py wiki /tmp/prov && \\
  python3 scripts/backfill_source_dates.py wiki /tmp/prov/triplet_provenance.json [--apply]

Dry run by default: prints what it would change and writes nothing.
"""
import json, sys, os, re, glob, collections, shutil

DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")


def load_source_dates(vault):
    out = {}
    for f in glob.glob(os.path.join(vault, "inbox", "proposals", "**", "*.md"), recursive=True):
        try:
            t = open(f, encoding="utf-8").read()
        except OSError:
            continue
        pid = re.search(r"^(?:proposal_id|prop_id):\s*(.*)$", t, re.M)
        sd = re.search(r"^source_date:\s*(.*)$", t, re.M)
        if pid and sd:
            out[pid.group(1).strip()] = sd.group(1).strip().strip('"').strip("'")
    return out


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    vault, prov_path = sys.argv[1], sys.argv[2]
    apply_ = "--apply" in sys.argv
    cf_path = os.path.join(vault, "c2a2-prs-3d", "prs_pub_years.json")

    prov = json.load(open(prov_path))
    src = load_source_dates(vault)
    cf = json.load(open(cf_path))

    n = collections.Counter()
    changes = {}
    for r in prov.get("rows", []):
        tid = "%s-%s" % (r.get("tradition", ""), r.get("triplet_id", ""))
        tier = r.get("match_tier", "")
        pid = r.get("source_proposal_id", "")
        n["rows"] += 1
        if tier != "A":
            n["skip_tier_%s" % (tier or "none")] += 1
            continue
        if not pid or pid not in src:
            n["skip_no_proposal_source_date"] += 1
            continue
        v = src[pid]
        m = DATE_RE.match(v)
        if not m:
            n["skip_malformed_source_date"] += 1
            continue
        cur = cf.get(tid)
        if isinstance(cur, dict) and cur.get("date"):
            if cur["date"] == v:
                n["skip_already_correct"] += 1
                continue
            if cur["date"] == (r.get("ingested_date") or "\x00"):
                n["OVERWRITE_capture_date"] += 1          # provably a Date-Added value
                changes[tid] = {"date": v, "pub_year": int(m.group(1))}
                continue
            n["skip_dated_and_not_capture"] += 1
            continue
        changes[tid] = {"date": v, "pub_year": int(m.group(1))}
        n["WOULD_SET"] += 1

    print("backfill_source_dates -- %s" % ("APPLY" if apply_ else "DRY RUN"))
    print("  carryforward: %s (%d entries, %d dated)"
          % (cf_path, len(cf), sum(1 for v in cf.values() if isinstance(v, dict) and v.get("date"))))
    print("  proposals carrying source_date: %d" % len(src))
    for k in sorted(n):
        print("  %-34s %d" % (k, n[k]))

    if changes:
        ys = collections.Counter(v["pub_year"] for v in changes.values())
        print("  new entries by year: %s" % sorted(ys.items()))
        sample = list(changes.items())[:3]
        for k, v in sample:
            print("    e.g. %s -> %s" % (k, v))

    if not apply_:
        print("\n  (dry run -- nothing written; re-run with --apply)")
        return

    shutil.copyfile(cf_path, cf_path + ".bak")
    cf.update(changes)
    with open(cf_path, "w", encoding="utf-8") as fh:
        json.dump(cf, fh, indent=1, sort_keys=True)
    print("\n  WROTE %s (+%d entries); backup at %s.bak" % (cf_path, len(changes), cf_path))


if __name__ == "__main__":
    main()

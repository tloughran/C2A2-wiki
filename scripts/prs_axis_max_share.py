#!/usr/bin/env python3
"""prs_axis_max_share.py -- the falsifier SPEC_prs_time_axis_2026-08-27.md specified
but did not implement.

METRIC
  max_share = the largest fraction of nodes landing on a single rendered z level.
  A degenerate axis is one where max_share is large: the axis has stopped
  discriminating, so the picture cannot change no matter how much the corpus grows.
  This failure is silent and progressive -- no freshness gate catches it, because
  the data is current and the count keeps rising. Run it as a standing check.

WHY IT READS THE BAKED ARTIFACT
  The number that matters is what a viewer actually sees, so this parses
  PRS_TRIPLETS out of the built prs_3d.html rather than trusting a source file
  or a generator's intent. Same discipline as the Level-2 regen's guards.

MODES (all over the same node set, so they are directly comparable)
  rendered      what the artifact does TODAY: day-precision ordinal scale, shared
                by dateToZ and yearToZ. THIS MUST TRACK template_prs_3d.html --
                if the template's z model changes and this does not, the check
                silently reports the old model's number. That happened once
                already, on 2026-08-27, within minutes of the template patch.
  legacy_year   the pre-2026-08-27 model: z = yearToZ(year(date)) on a pub_year
                scale. Kept because it is the historical control (0.905) and the
                tau->infinity regression target.
  pub_year      z = yearToZ(pub_year) -- the axis the spec BELIEVED was live (0.857).

Usage:  python3 scripts/prs_axis_max_share.py [path/to/prs_3d.html] [--json]
"""
import json, sys, collections, datetime

PRECISION = 3           # decimals; two nodes agreeing to this are coplanar on screen
Z_HEIGHT = 40.0         # must match template_prs_3d.html


def load(path):
    h = open(path, encoding="utf-8").read()
    i = h.index("var PRS_TRIPLETS = ") + len("var PRS_TRIPLETS = ")
    t, _ = json.JSONDecoder().raw_decode(h, i)
    return t


def year_to_z(year, lo, hi):
    """Port of yearToZ() in template_prs_3d.html."""
    if hi == lo:
        return Z_HEIGHT / 2
    return 2 + ((year - lo) / (hi - lo)) * (Z_HEIGHT - 4)


def share(zs):
    """max_share, distinct level count, and the top few levels."""
    b = collections.Counter(round(z, PRECISION) for z in zs)
    top = b.most_common(3)
    return top[0][1] / len(zs), len(b), top


def date_ord(s):
    try:
        return datetime.date.fromisoformat(s[:10]).toordinal()
    except (ValueError, TypeError):
        return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args else "wiki/prs_3d.html"
    t = load(path)
    n = len(t)

    # The live scale: minYear/maxYear come from pub_year, NOT from date.
    years = [r.get("pub_year") or 2020 for r in t]
    lo, hi = min(years), max(years)

    out = {}

    # rendered -- port of the CURRENT template: one ordinal scale, day precision.
    ords = [date_ord(r.get("date")) for r in t]
    good = [o for o in ords if o is not None]
    undated = len(ords) - len(good)
    if good:
        omin, omax = min(good), max(good)
        span = (omax - omin) or 1
        out["rendered"] = share([
            2 + ((o - omin) / span) * (Z_HEIGHT - 4) if o is not None else Z_HEIGHT / 2
            for o in ords])

    # legacy_year -- the pre-2026-08-27 model; historical control and regression target
    out["legacy_year"] = share([
        year_to_z(int((r.get("date") or "0000")[:4]) if (r.get("date") or "")[:4].isdigit()
                  else 2020, lo, hi) for r in t])

    # pub_year -- what the spec thought was live
    out["pub_year"] = share([year_to_z(r.get("pub_year") or 2020, lo, hi) for r in t])

    have_source = sum(1 for r in t if r.get("source_date"))

    if "--json" in sys.argv:
        print(json.dumps({"file": path, "nodes": n, "year_scale": [lo, hi],
                          "source_date_present": have_source, "undated": undated,
                          "max_share": {k: round(v[0], 4) for k, v in out.items()},
                          "levels": {k: v[1] for k, v in out.items()}}, indent=1))
        return

    print("prs_axis_max_share -- %s" % path)
    print("  nodes: %d   yearToZ scale (from pub_year): %d..%d" % (n, lo, hi))
    print("  source_date present on %d/%d nodes" % (have_source, n))
    print("  UNDATED (no parseable date -- all stacked at the midpoint): %d" % undated)
    print()
    print("  %-11s %9s %8s   %s" % ("z source", "max_share", "levels", "top levels (z: count)"))
    for k in ("rendered", "legacy_year", "pub_year"):
        if k not in out:
            continue
        ms, lv, top = out[k]
        tops = "  ".join("%.3f: %d" % (z, c) for z, c in top)
        print("  %-11s %8.1f%% %8d   %s" % (k, ms * 100, lv, tops))
    print()
    print("  TARGET (spec): max_share < 0.10")


if __name__ == "__main__":
    main()

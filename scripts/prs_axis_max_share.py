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
import json, sys, collections, datetime, math, re

PRECISION = 3           # decimals; two nodes agreeing to this are coplanar on screen
Z_HEIGHT = 40.0         # must match template_prs_3d.html


def load(path):
    h = open(path, encoding="utf-8").read()
    i = h.index("var PRS_TRIPLETS = ") + len("var PRS_TRIPLETS = ")
    t, _ = json.JSONDecoder().raw_decode(h, i)
    m = re.search(r"^var TAU_DAYS = ([0-9.eE+]+);", h, re.M)
    if not m:
        raise SystemExit("FAIL: no TAU_DAYS in %s -- the axis model moved and this "
                         "check would report the wrong one" % path)
    return t, float(m.group(1))


def ord_to_z(o, omin, omax, tau):
    """Port of ordToZ() in template_prs_3d.html, INCLUDING the log-on-age transform
    and the clamp. Kept exact so a non-monotonic change to the template cannot pass
    unnoticed here. (max_share alone would not notice: it counts exact ties, and every
    monotonic transform preserves ties -- which is why this port sat linear from
    2026-08-27 to 2026-09-01 while the template was logarithmic, and reported the
    right number anyway.)"""
    if omax == omin:
        return Z_HEIGHT / 2
    age_max = omax - omin
    oc = max(omin, min(omax, o))
    u = math.log(1 + (omax - oc) / tau) / math.log(1 + age_max / tau)
    return 2 + (1 - u) * (Z_HEIGHT - 4)


def rate_spread(triplets, omin, omax, tau):
    """THE METRIC max_share CANNOT SEE.

    max_share asks whether nodes land on the SAME level. It is invariant under every
    monotonic transform, so an axis that is perfectly discriminating and still
    unreadable -- one tradition spread over the column, another squeezed into a mat --
    scores healthy. That is the 2026-09-01 failure.

    This asks a different question: how many column units does each tradition get per
    year it actually spans? On an honest axis those rates are within a small factor of
    each other. rate_spread = max(rate) / min(rate) over traditions with >= 2 distinct
    dates and >= 1 year of span. Measured on the domino test corpus: 34.89 at tau=90,
    1.04 at tau -> linear."""
    by = collections.defaultdict(list)
    for r in triplets:
        o = date_ord(r.get("date"))
        if o is not None:
            by[r.get("thinker", "?")].append(o)
    rows = []
    for th, ords in sorted(by.items()):
        if len(set(ords)) < 2:
            continue
        yrs = (max(ords) - min(ords)) / 365.25
        if yrs < 1.0:
            continue
        zs = [ord_to_z(o, omin, omax, tau) for o in ords]
        span = max(zs) - min(zs)
        rows.append({"tradition": th, "n": len(ords), "years": round(yrs, 1),
                     "z_span": round(span, 2), "units_per_year": round(span / yrs, 4)})
    if len(rows) < 2:
        return rows, None
    rates = [r["units_per_year"] for r in rows if r["units_per_year"] > 0]
    return rows, (max(rates) / min(rates) if rates else None)


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
    t, tau = load(path)
    n = len(t)

    # The live scale: minYear/maxYear come from pub_year, NOT from date.
    years = [r.get("pub_year") or 2020 for r in t]
    lo, hi = min(years), max(years)

    out = {}

    # rendered -- port of the CURRENT template: one ordinal scale, day precision.
    ords = [date_ord(r.get("date")) for r in t]
    good = [o for o in ords if o is not None]
    undated = len(ords) - len(good)
    rates, spread = [], None
    if good:
        omin, omax = min(good), max(good)
        out["rendered"] = share([
            ord_to_z(o, omin, omax, tau) if o is not None else Z_HEIGHT / 2
            for o in ords])
        rates, spread = rate_spread(t, omin, omax, tau)

    # legacy_year -- the pre-2026-08-27 model; historical control and regression target
    out["legacy_year"] = share([
        year_to_z(int((r.get("date") or "0000")[:4]) if (r.get("date") or "")[:4].isdigit()
                  else 2020, lo, hi) for r in t])

    # pub_year -- what the spec thought was live
    out["pub_year"] = share([year_to_z(r.get("pub_year") or 2020, lo, hi) for r in t])

    have_source = sum(1 for r in t if r.get("source_date"))

    if "--json" in sys.argv:
        print(json.dumps({"file": path, "nodes": n, "tau_days": tau, "year_scale": [lo, hi],
                          "rate_spread": None if spread is None else round(spread, 2),
                          "per_tradition_rate": rates,
                          "source_date_present": have_source, "undated": undated,
                          "max_share": {k: round(v[0], 4) for k, v in out.items()},
                          "levels": {k: v[1] for k, v in out.items()}}, indent=1))
        return

    print("prs_axis_max_share -- %s" % path)
    print("  nodes: %d   TAU_DAYS=%g   yearToZ scale (from pub_year): %d..%d" % (n, tau, lo, hi))
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
    print()
    print("  RATE SPREAD -- column units per year of span, per tradition.")
    print("  max_share cannot see this: it is invariant under monotonic transforms,")
    print("  so a perfectly discriminating axis can still be unreadable.")
    if spread is None:
        print("    n/a -- fewer than two traditions span a year or more")
    else:
        for r in sorted(rates, key=lambda r: -r["units_per_year"]):
            print("    %-14s %3d nodes  %6.1f yr  z-span %6.2f  %8.4f units/yr"
                  % (r["tradition"], r["n"], r["years"], r["z_span"], r["units_per_year"]))
        print("    rate_spread = %.2fx   (1.0 = every tradition gets the same column "
              "per year; > 4 means the axis is telling a different story than the data)"
              % spread)
        if "--check" in sys.argv and spread > 4.0:
            print("    FAIL: rate_spread %.2fx exceeds 4.0" % spread)
            sys.exit(3)


if __name__ == "__main__":
    main()

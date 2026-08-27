#!/usr/bin/env python3
"""Edge-provenance census for the Sociogram graph.

Companion to check_bridge_dist.py. That script asks whether a candidate Z
variable stratifies the corpus. This one asks the PRIOR question: are the
edges it stratifies over there for a reason?

    python3 edge_census.py [path/to/wiki_narration.html]

Default is the LIVE artifact wiki/wiki_narration.html (the one
regen_sociogram.sh writes), NOT c2a2-wiki-narration/output/, which is a dead
May-2026 build location with an old string-id link schema.

Read-only. Writes nothing. Prints six sections:

  1  edge census by type, and what the untyped edges actually are
  2  which identifier tokens manufacture the reference edges
  3  the sliding-window artifact, and a falsifiable test of its ordering
  4  which edge type carries the cross-boundary ("bridging") signal
  5  node population vs edge incidence, by group and by architecture subdir
  6  edge multiplicity: how many identifiers a joined file pair really shares

Sections 3 and 6 are the load-bearing ones. Everything else is context for
reading them.

First run: 2026-08-25, against the 4,454-node / 125,372-link build of
2026-08-24 17:30. Findings written up in handoffs/edge-provenance-census.md.
"""
import collections
import json
import re
import sys

DEFAULT = "wiki_narration.html"
PATH = sys.argv[1] if len(sys.argv) > 1 else DEFAULT


def grab(src, name):
    """Pull `const NAME = <json>;` by scanning for the balanced terminator."""
    marker = "const %s = " % name
    i = src.index(marker) + len(marker)
    depth = 0
    instr = False
    esc = False
    for j in range(i, len(src)):
        c = src[j]
        if esc:
            esc = False
            continue
        if c == "\\":
            esc = True
            continue
        if c == '"':
            instr = not instr
            continue
        if instr:
            continue
        if c in "[{":
            depth += 1
        elif c in "]}":
            depth -= 1
            if depth == 0:
                return json.loads(src[i:j + 1])
    raise SystemExit("could not parse %s" % name)


def main():
    src = open(PATH, encoding="utf-8").read()
    NODES = grab(src, "NODES")
    LINKS = grab(src, "LINKS")
    n = len(NODES)
    idx = {nd["id"]: i for i, nd in enumerate(NODES)}

    # Link endpoints are INTEGER INDICES into NODES. An older build used string
    # ids; d3 rewrites either to object refs once the simulation runs. Handle
    # all three or every node reads as degree 0.
    def rs(v):
        if isinstance(v, int):
            return v if 0 <= v < n else None
        if isinstance(v, dict):
            return idx.get(v.get("id"))
        return idx.get(v)

    deg = collections.Counter()
    for l in LINKS:
        s, t = rs(l["source"]), rs(l["target"])
        if s is not None:
            deg[s] += 1
        if t is not None:
            deg[t] += 1

    print("file : %s" % PATH)
    print("nodes: %d   links: %d" % (n, len(LINKS)))

    # ---- 1. edge census by type, and what the untyped edges are -------------
    ltypes = collections.Counter(l.get("type") for l in LINKS)
    print("\n=== 1. EDGE CENSUS BY TYPE ===")
    for t, c in ltypes.most_common():
        print("  %-12s %7d  %5.1f%%" % (str(t), c, 100.0 * c / len(LINKS)))

    untyped = [l for l in LINKS if not l.get("type")]
    print("\n  untyped edges: %d" % len(untyped))
    for ks, c in collections.Counter(
            tuple(sorted(l.keys())) for l in untyped).most_common(5):
        print("    %6d  keys=%s" % (c, list(ks)))
    print("    by layer: %s" % dict(collections.Counter(
        l.get("layer") for l in untyped)))
    ug = collections.Counter()
    trad_touch = 0
    for l in untyped:
        s, t = rs(l["source"]), rs(l["target"])
        if s is None or t is None:
            continue
        gs, gt = NODES[s].get("group"), NODES[t].get("group")
        ug[(gs, gt)] += 1
        if str(gs).startswith("traditions/") or str(gt).startswith("traditions/"):
            trad_touch += 1
    print("    top endpoint group-pairs:")
    for (a, b), c in ug.most_common(5):
        print("      %6d  %s -> %s" % (c, a, b))
    print("    with a traditions/ endpoint: %d  (nonzero => the agent layer DOES"
          " enter bridge_raw)" % trad_touch)

    # ---- 2. shared_reference provenance ------------------------------------
    print("\n=== 2. REFERENCE EDGES: which identifiers manufacture them ===")
    refe = [l for l in LINKS if l.get("type") == "reference"]
    byref = collections.Counter(l.get("reference") for l in refe)
    tot = len(refe)
    print("  reference edges: %d   distinct identifiers: %d" % (tot, len(byref)))
    cum = 0
    for r, c in byref.most_common(15):
        cum += c
        print("    %-16s %7d  %5.1f%%  (cum %5.1f%%)"
              % (r, c, 100.0 * c / tot, 100.0 * cum / tot))
    top10 = sum(c for _, c in byref.most_common(10))
    print("  top 10 identifiers = %.1f%% of reference edges, %.1f%% of the whole graph"
          % (100.0 * top10 / tot, 100.0 * top10 / len(LINKS)))
    fam = collections.Counter(re.sub(r'[-\d]+$', '', str(r)) for r in byref.elements())
    print("  by identifier family:")
    for f, c in fam.most_common():
        print("    %-14s %7d  %5.1f%%" % (f, c, 100.0 * c / tot))

    # ---- 3. the sliding-window artifact ------------------------------------
    print("\n=== 3. SLIDING-WINDOW ARTIFACT (extract_vault_data.py:728) ===")
    print("  Reference edges join each file only to the next 24 files sharing")
    print("  that identifier, in `files` list order. For any identifier shared")
    print("  by more than 25 files the emitted set is an arbitrary SUBSET of")
    print("  the clique -- selected by list position, which nobody chose.")
    print("  Emitted count for k files is ~24k-300, which recovers k:")
    for r, c in byref.most_common(6):
        k = 1
        while k * (k - 1) // 2 - max(0, (k - 25) * (k - 25 + 1) // 2) < c and k < 4000:
            k += 1
        full = k * (k - 1) // 2
        print("    %-16s emitted %6d   clique for ~%3d files = %7d   (%.1f%%)"
              % (r, c, k, full, 100.0 * c / full if full else 0))

    print("\n  FALSIFIER for the ordering. extract_vault_data.py's own comment")
    print("  says the window runs over ALPHABETICALLY sorted files. If true, no")
    print("  edge for one identifier spans more than 24 positions in alphabetical")
    print("  filepath order. Measured 2026-08-25: REFUTED -- see below. The count")
    print("  arithmetic above still holds, so the window is real; the ORDER is")
    print("  directory-walk order, and the comment is wrong.")
    order = {nd["id"]: k for k, nd in enumerate(sorted(NODES, key=lambda x: x["id"]))}
    for target in [r for r, _ in byref.most_common(3)]:
        gaps = []
        for l in refe:
            if l.get("reference") != target:
                continue
            s, t = rs(l["source"]), rs(l["target"])
            if s is None or t is None:
                continue
            gaps.append(abs(order[NODES[s]["id"]] - order[NODES[t]["id"]]))
        if not gaps:
            continue
        over = sum(1 for g in gaps if g > 24)
        print("    %-16s edges=%5d  max gap=%5d  median=%4d  over 24: %d (%.1f%%)"
              % (target, len(gaps), max(gaps), sorted(gaps)[len(gaps) // 2],
                 over, 100.0 * over / len(gaps)))

    # ---- 4. what carries the cross-boundary signal --------------------------
    print("\n=== 4. CROSS-BOUNDARY EDGES BY TYPE (the 'bridging' substrate) ===")
    xb = collections.Counter()
    for l in LINKS:
        if l.get("bridge") == "cross":
            xb[l.get("type")] += 1
    xt = sum(xb.values())
    print("  cross edges: %d of %d (%.1f%%)" % (xt, len(LINKS), 100.0 * xt / len(LINKS)))
    for t, c in xb.most_common():
        print("    %-12s %7d  %5.1f%% of cross" % (str(t), c, 100.0 * c / xt))

    # ---- 5. node population vs edge incidence ------------------------------
    print("\n=== 5. NODE POPULATION vs EDGE INCIDENCE ===")
    gN, gE = collections.Counter(), collections.Counter()
    for i, nd in enumerate(NODES):
        g = nd.get("group") or "?"
        g = g.split("/")[0] if g.startswith("traditions/") else g
        gN[g] += 1
        gE[g] += deg[i]
    te = sum(gE.values())
    print("  %-18s %6s %6s   %9s %6s" % ("group", "nodes", "%", "edge-ends", "%"))
    for g, c in gN.most_common():
        print("  %-18s %6d %5.1f%%   %9d %5.1f%%"
              % (g, c, 100.0 * c / n, gE[g], 100.0 * gE[g] / te))

    sub, sube = collections.Counter(), collections.Counter()
    for i, nd in enumerate(NODES):
        fid = nd.get("id") or ""
        if not fid.startswith("architecture/"):
            continue
        parts = fid.split("/")
        key = parts[1] if len(parts) > 2 else "(top level)"
        sub[key] += 1
        sube[key] += deg[i]
    print("\n  architecture/ breakdown (the dominant group):")
    print("  %-26s %6s %6s   %9s" % ("subdir", "nodes", "% all", "edge-ends"))
    for k, c in sub.most_common():
        print("  %-26s %6d %5.1f%%   %9d" % (k, c, 100.0 * c / n, sube[k]))

    # ---- 6. edge multiplicity ----------------------------------------------
    print("\n=== 6. HOW MANY IDENTIFIERS DOES A JOINED PAIR REALLY SHARE? ===")
    print("  generate_visualization.py:_emit dedupes on the unordered pair (s,t)")
    print("  with NO type in the key, emitting wikilink -> mention -> reference.")
    print("  So a pair sharing twelve identifiers survives as ONE edge whose")
    print("  `reference` field names whichever identifier iterated first.")
    pair = collections.Counter()
    for l in refe:
        s, t = rs(l["source"]), rs(l["target"])
        if s is None or t is None:
            continue
        pair[(min(s, t), max(s, t))] += 1
    dist = collections.Counter(pair.values())
    tp = sum(dist.values())
    print("  distinct file pairs joined by a reference edge: %d" % tp)
    for k in sorted(dist):
        print("    %2d shared identifier(s): %6d pairs  %5.1f%%"
              % (k, dist[k], 100.0 * dist[k] / tp))
    print("  A flat 100% at 1 confirms the dedup: multiplicity is not in the")
    print("  artifact at all, so no downstream reader can recover it.")


if __name__ == "__main__":
    main()

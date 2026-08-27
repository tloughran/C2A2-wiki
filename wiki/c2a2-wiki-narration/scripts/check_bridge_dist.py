#!/usr/bin/env python3
"""Measure whether a candidate Z variable stratifies the Sociogram corpus.

    python3 check_bridge_dist.py [path/to/wiki_narration.html]

Default path is the LIVE artifact: wiki/wiki_narration.html — the one
regen_sociogram.sh writes. NOT c2a2-wiki-narration/output/, which is a dead
leftover from an old build location (4MB, May 2026, string-id link schema).

Gate for a usable Z variable: >=5% of nodes off the floor value, >=3 levels.

Reports three candidate metrics because they disagree sharply (top-100 overlap
between raw and density was 7/100 on the 2026-08-24 build). Choosing among them
is a judgement about what the project means by "bridging", not a technical
detail — look at what rises to the top of each, don't pick from the summary
statistics alone.
"""
import collections
import json
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
    nodes = grab(src, "NODES")
    links = grab(src, "LINKS")
    n = len(nodes)

    # Link endpoints are INTEGER INDICES into NODES in the current generator.
    # (An older build used string ids; d3 rewrites them to object refs once the
    # simulation runs. Handle all three or every node reads as degree 0.)
    idx = {node["id"]: i for i, node in enumerate(nodes)}

    def resolve(v):
        if isinstance(v, int):
            return v if 0 <= v < n else None
        if isinstance(v, dict):
            return idx.get(v.get("id"))
        return idx.get(v)

    adj = collections.defaultdict(set)
    cross = collections.Counter()
    deg_e = collections.Counter()
    ltypes = collections.Counter()
    for l in links:
        s, t = resolve(l["source"]), resolve(l["target"])
        ltypes[l.get("type")] += 1
        if s is None or t is None:
            continue
        adj[s].add(t)
        adj[t].add(s)
        deg_e[s] += 1
        deg_e[t] += 1
        if l.get("bridge") == "cross":
            cross[s] += 1
            cross[t] += 1

    print("file:  %s" % PATH)
    print("nodes: %d   links: %d" % (n, len(links)))
    print("link types:", dict(ltypes))
    isolated = sum(1 for i in range(n) if not adj[i])
    degs = sorted(len(adj[i]) for i in range(n))
    print("degree-0 nodes: %d   median degree: %d" % (isolated, degs[n // 2]))

    if isolated == n:
        raise SystemExit("\n!! EVERY node has degree 0 with links present -- the "
                         "endpoint schema changed again. Fix resolve() before "
                         "trusting anything below.")
    if "mention" not in ltypes:
        print("\n!! No 'mention' edges. Bridging is carried by these; a zero "
              "result means the BUILD cannot answer, not that the variable "
              "is unreadable.")

    def tradition(i):
        g = nodes[i].get("group", "") or ""
        return g.split("/")[1] if g.startswith("traditions/") else None

    raw = [len({tradition(m) for m in adj[i]} - {None}) for i in range(n)]
    density = [(raw[i] / len(adj[i])) if adj[i] else 0.0 for i in range(n)]
    cfrac = [(cross[i] / deg_e[i]) if deg_e[i] else 0.0 for i in range(n)]

    def report(title, vals, note):
        nz = sum(1 for v in vals if v > 0)
        levels = len(set(vals))
        pct = 100.0 * nz / n
        gate = "PASS" if pct >= 5.0 and levels >= 3 else "FAIL"
        print("\n=== %s ===" % title)
        print("nonzero %d/%d = %.1f%%   levels %d   GATE: %s" % (nz, n, pct, levels, gate))
        print("caveat: %s" % note)
        for i in sorted(range(n), key=lambda k: -vals[k])[:8]:
            print("  %7.3f  raw=%2d deg=%3d  %-44s %s"
                  % (vals[i], raw[i], len(adj[i]), nodes[i]["id"][:44],
                     nodes[i].get("group")))

    dist = collections.Counter(raw)
    print("\nraw bridge-count distribution:", dict(sorted(dist.items())))

    report("A. RAW COUNT - distinct traditions one hop away", raw,
           "top is dominated by registry files (open_questions, THINKERS) that "
           "name every thinker by construction. Rewards scaffolding.")
    report("B. DENSITY - traditions / neighbours", density,
           "saturates at 1.000 for degree-1 nodes. Rewards noise.")
    report("C. CROSS-EDGE FRACTION - uses the generator's own bridge field", cfrac,
           "same small-denominator problem as B, but the numerator is the "
           "generator's own cross/same classification rather than ours.")

    top_raw = set(sorted(range(n), key=lambda i: -raw[i])[:100])
    top_den = set(sorted(range(n), key=lambda i: -density[i])[:100])
    top_crs = set(sorted(range(n), key=lambda i: -cfrac[i])[:100])
    print("\ntop-100 agreement:  raw^density %d   raw^cross %d   density^cross %d"
          % (len(top_raw & top_den), len(top_raw & top_crs), len(top_den & top_crs)))
    print("Low agreement means the metric choice IS the claim. Decide it by "
          "looking at what rises in the probe, not from these numbers.")


if __name__ == "__main__":
    main()

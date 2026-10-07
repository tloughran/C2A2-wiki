#!/usr/bin/env python3
"""Merge the three evidence classes into one tiered generative-link list.

Each output link carries a `tier`, which decides how the connectome draws it:

  named          criteria C1 fired: the target's text names the source    (solid)
  inherited      criteria C2 only: a distinctive term carried over         (dashed, a lead)
  reconstructed  an argued reconstruction the criteria did not find        (distinct; argued,
                 not accepted -- the model never writes its own status)
  ruled_out      the answer key rules the pair out                         (struck, never deleted)

Precedence: a key `ruled_out` overrides any criteria candidate for the same pair -- a
disproved link is a finding, and drawing it as a lead would hide that. A reconstruction
is only added where the criteria found nothing, so it never relabels a textual hit.

Deterministic (Rule 5): no model call. Inputs are files other scripts write.

    python3 build_tiered_links.py --candidates cands.json --gold dependencies.json \
        --reconstructions reconstructions_designed.json --out links.json
"""
import argparse
import json
from collections import Counter


def load_list(path, key):
    d = json.load(open(path, encoding="utf-8"))
    return d[key] if isinstance(d, dict) else d


def build(cands, gold, recons):
    links = {}
    for c in cands:
        if not c.get("generative"):
            continue
        links[(c["source"], c["target"])] = {
            "source": c["source"], "target": c["target"], "tier": c["tier"],
            "relation": c.get("relation", ""), "strength": c.get("strength"),
            "basis": ", ".join(c.get("criteria", [])),
        }
    for r in recons:
        if r.get("verdict") != "reconstructed":
            continue
        pair = (r["source"], r["target"])
        if pair in links:
            continue
        links[pair] = {
            "source": r["source"], "target": r["target"], "tier": "reconstructed",
            "relation": "resource_supplying", "strength": None,
            "basis": r.get("claim", ""),
        }
    for g in gold:
        if g.get("status") != "ruled_out":
            continue
        pair = (g["source"], g["target"])
        links[pair] = {
            "source": g["source"], "target": g["target"], "tier": "ruled_out",
            "relation": g.get("relation", ""), "strength": None,
            "basis": g.get("basis", ""),
        }
    return sorted(links.values(), key=lambda l: (l["tier"], l["source"], l["target"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--candidates", required=True, help="prs_link_criteria.py --json output")
    ap.add_argument("--gold", required=True, help="answer key (dependencies.json)")
    ap.add_argument("--reconstructions", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    links = build(load_list(a.candidates, "candidates"),
                  load_list(a.gold, "dependencies"),
                  load_list(a.reconstructions, "reconstructions"))
    if not links:
        raise SystemExit("FAIL: no links built -- refusing to write an empty layer")
    json.dump(links, open(a.out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("wrote %s: %s" % (a.out, dict(sorted(Counter(l["tier"] for l in links).items()))))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the published "Sources monitored" roster from the runtime source config.

The runtime's config/sources.json is the single source of truth for WHAT the
heartbeat monitors (its schema is fixed by the Source dataclass, so it carries no
category field). This script joins each source to a display lane and writes a
published, GitHub-Pages-safe roster the tab renders so the breadth of inflow is
both real and visible. Deterministic, stdlib-only, idempotent.

Lane membership lives here (not in sources.json) on purpose: adding a feed means
adding its id to LANES below. Any config source not mapped here is bucketed into
"Other" AND logged loudly to stderr, so an unmapped feed can never silently
vanish from the roster.
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

# Ordered display lanes. Each value is the list of source ids in that lane.
LANES = [
    ("labs", "Research labs", ["openai_blog", "huggingface_blog", "google_ai_blog", "deepmind_blog"]),
    ("papers", "Papers", ["arxiv_csai", "arxiv_cslg", "arxiv_cscl"]),
    ("journalism", "Journalism", ["the_decoder", "venturebeat_ai"]),
    ("analysis", "Independent analysis", ["import_ai", "simonwillison"]),
    ("community", "Community", ["hn_ai"]),
    ("video", "Video", ["yt_two_minute_papers", "yt_yannic", "yt_matthew_berman", "yt_david_shapiro", "yt_nate_b_jones"]),
    ("social", "Social (Bluesky/Mastodon)", ["bsky_karpathy", "bsky_bender"]),
]


def lane_of(source_id: str):
    for key, label, ids in LANES:
        if source_id in ids:
            return key, label
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, help="path to runtime config/sources.json")
    ap.add_argument("--data-dir", required=True, help="published tab data dir (writes sources_roster.json here)")
    args = ap.parse_args()

    raw = json.loads(Path(args.config).read_text())
    by_id = {s["id"]: s for s in raw if s.get("enabled", True)}

    # Bucket sources into lanes in declared order; collect unmapped loudly.
    lanes_out = []
    placed = set()
    for key, label, ids in LANES:
        members = []
        for sid in ids:
            s = by_id.get(sid)
            if not s:
                continue  # configured-but-disabled or removed; just omit
            members.append({"id": s["id"], "name": s["name"], "home_url": s.get("home_url", "")})
            placed.add(sid)
        if members:
            lanes_out.append({"key": key, "label": label, "sources": members})

    unmapped = [sid for sid in by_id if sid not in placed]
    if unmapped:
        print(f"[roster] WARN: {len(unmapped)} source(s) not assigned to a lane: "
              f"{', '.join(unmapped)} -> bucketed into 'Other'", file=sys.stderr)
        lanes_out.append({
            "key": "other", "label": "Other",
            "sources": [{"id": by_id[s]["id"], "name": by_id[s]["name"],
                         "home_url": by_id[s].get("home_url", "")} for s in unmapped],
        })

    total = sum(len(l["sources"]) for l in lanes_out)
    roster = {
        "generated": datetime.date.today().isoformat(),
        "total": total,
        "lane_count": len(lanes_out),
        "lanes": lanes_out,
    }

    out = Path(args.data_dir) / "sources_roster.json"
    out.write_text(json.dumps(roster, indent=2) + "\n")
    print(f"[roster] wrote {out}: {total} sources across {len(lanes_out)} lanes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

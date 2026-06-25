#!/usr/bin/env python3
"""Write data/snapshots/index.json — the manifest the History tab reads.

GitHub Pages has no directory listing, so the History view needs an explicit
manifest of which dated snapshots exist. This scans data/snapshots/digest-*.json
and writes a small index (newest first) with each snapshot's headline counts.
Deterministic, stdlib only, idempotent. Run at the end of the refresh pipeline.

Usage:
  python3 build_manifest.py --data-dir data
"""

import argparse
import json
import re
import sys
from pathlib import Path

DATE_RE = re.compile(r"digest-(\d{4}-\d{2}-\d{2})\.json$")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--data-dir", default=str(Path(__file__).resolve().parent.parent / "data"))
    args = p.parse_args(argv)

    snap_dir = Path(args.data_dir) / "snapshots"
    snap_dir.mkdir(parents=True, exist_ok=True)

    entries = []
    for f in sorted(snap_dir.glob("digest-*.json")):
        m = DATE_RE.search(f.name)
        if not m:
            continue
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        metrics = d.get("metrics", {})
        entries.append({
            "date": m.group(1),
            "file": f.name,
            "window": d.get("window", ""),
            "signals": len(d.get("signals", [])),
            "items_checked": metrics.get("items_checked"),
            "sources_reached": metrics.get("sources_reached"),
            "high_relevance": metrics.get("high_relevance"),
            "primary_themes": metrics.get("primary_themes", ""),
        })

    entries.sort(key=lambda e: e["date"], reverse=True)  # newest first
    out = {"generated": __import__("datetime").datetime.now(
        __import__("datetime").timezone.utc).strftime("%Y-%m-%d"),
        "count": len(entries), "snapshots": entries}
    (snap_dir / "index.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote {0} ({1} snapshots)".format(snap_dir / "index.json", len(entries)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Keep only the most recent N heartbeat History snapshots (cloud space governor).

Snapshots are timestamped `digest-YYYYMMDD-HHMMSS.json`, so a lexical sort is also
chronological. We remove the oldest beyond --keep. `index.json` (the manifest) is rebuilt
afterward by build_manifest.py, so this step only touches `digest-*.json` files.
Idempotent; `--dry-run` prints what would go without deleting.

Why this exists: an autonomous cloud cron commits a new snapshot on every content change,
so without a cap `data/snapshots/` would grow unbounded in git history. Keeping the last N
(default 60) bounds it while preserving a meaningful History window.
"""
import argparse
import re
import sys
from pathlib import Path

SNAP_RE = re.compile(r"^digest-\d{8}-\d{6}\.json$")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", required=True)
    ap.add_argument("--keep", type=int, default=60)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    snaps = Path(args.data_dir) / "snapshots"
    if not snaps.is_dir():
        print(f"[prune] no snapshots dir at {snaps}; nothing to do")
        return 0
    if args.keep < 1:
        print("[prune] ERROR: --keep must be >= 1", file=sys.stderr)
        return 1

    files = sorted(p for p in snaps.iterdir() if SNAP_RE.match(p.name))
    if len(files) <= args.keep:
        print(f"[prune] {len(files)} snapshots <= keep={args.keep}; nothing to remove")
        return 0

    to_remove = files[: len(files) - args.keep]
    for p in to_remove:
        if args.dry_run:
            print(f"[prune] would remove {p.name}")
        else:
            p.unlink()
            print(f"[prune] removed {p.name}")
    print(f"[prune] kept newest {args.keep}, removed {len(to_remove)}"
          + (" (dry-run)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

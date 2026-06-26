#!/usr/bin/env python3
"""Archive the enriched digest.json as a per-update History snapshot.

Runs AFTER enrich_summaries.py, so the archived copy already carries its long
summaries. Each archive is timestamped (digest-YYYYMMDD-HHMMSS.json) so the
History tab gains one entry per *actual update*. To avoid noise, it only writes
a new snapshot when the content changed since the most recent snapshot
(signature = sorted signal URLs + items_checked + high_relevance); an unchanged
run prints "no change" and writes nothing.

Deterministic, stdlib only. Usage:
  python3 archive_snapshot.py --data-dir data
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

STAMP_RE = re.compile(r"digest-(\d{8})-(\d{6})\.json$")   # new: digest-YYYYMMDD-HHMMSS
DATE_RE = re.compile(r"digest-(\d{4}-\d{2}-\d{2})\.json$")  # legacy: digest-YYYY-MM-DD


def signature(digest: dict) -> list:
    sigs = sorted((s.get("url", "") or s.get("title", "")) for s in digest.get("signals", []))
    m = digest.get("metrics", {})
    return [m.get("items_checked"), m.get("high_relevance"), sigs]


def latest_snapshot(snap_dir: Path):
    """Most recent snapshot file by stamp (new timestamped beats legacy date)."""
    best = None
    best_key = ""
    for f in snap_dir.glob("digest-*.json"):
        m = STAMP_RE.search(f.name)
        key = (m.group(1) + m.group(2)) if m else None
        if key is None:
            dm = DATE_RE.search(f.name)
            key = dm.group(1).replace("-", "") + "000000" if dm else None
        if key and key > best_key:
            best_key, best = key, f
    return best


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--data-dir", default=str(Path(__file__).resolve().parent.parent / "data"))
    args = p.parse_args(argv)

    data_dir = Path(args.data_dir)
    snap_dir = data_dir / "snapshots"
    snap_dir.mkdir(parents=True, exist_ok=True)
    digest_path = data_dir / "digest.json"
    if not digest_path.exists():
        raise SystemExit("error: digest.json not found in " + str(data_dir))

    digest = json.loads(digest_path.read_text(encoding="utf-8"))

    prev = latest_snapshot(snap_dir)
    if prev is not None:
        try:
            if signature(json.loads(prev.read_text(encoding="utf-8"))) == signature(digest):
                print("no change since {0} — not archiving".format(prev.name))
                return 0
        except Exception:
            pass  # unreadable previous → archive fresh

    ga = digest.get("generated_at") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        dt = datetime.strptime(ga, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        dt = datetime.now(timezone.utc)
    stamp = dt.strftime("%Y%m%d-%H%M%S")
    out = snap_dir / ("digest-" + stamp + ".json")
    out.write_text(json.dumps(digest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("archived {0} ({1} signals, items={2})".format(
        out.name, len(digest.get("signals", [])), digest.get("metrics", {}).get("items_checked")))
    return 0


if __name__ == "__main__":
    sys.exit(main())

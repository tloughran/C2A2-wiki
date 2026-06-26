#!/usr/bin/env python3
"""Deterministically stamp heartbeat index.html asset includes with a content hash.

Why this exists
---------------
explorer.html force-freshes each tab's iframe document (`?v=Date.now()`), but it
cannot reach inside that document. So any asset the sub-page loads with a bare
`src="app.js"` is served from the browser cache even though the HTML is fresh —
a guaranteed stale-asset mismatch on every edit (the 2026-06-26 "What is a lens?"
dead-click bug). The fragile fix is to hand-bump `?v=N` on each edit; the robust
fix is to make the version a function of file content, so it is always correct
and no human has to remember.

This script rewrites the `?v=` of each local asset include in index.html to the
first 10 hex of the file's SHA-1. Idempotent: unchanged assets -> identical HTML.

Run standalone after editing any asset, or let refresh_snapshot.sh run it.
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

# Local asset includes that must be content-stamped. (CDN/remote includes are
# intentionally excluded — they are versioned at the source.)
ASSETS = ("styles.css", "heartbeat-config.js", "app.js", "auth.js")


def short_hash(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()[:10]


def stamp(html: str, name: str, ver: str) -> tuple[str, int]:
    # Anchor on the attribute quote so we only touch the real include, never a
    # coincidental substring elsewhere in the document.
    pat = re.compile(
        r'((?:href|src)=")' + re.escape(name) + r'(?:\?v=[A-Za-z0-9]+)?(")'
    )
    return pat.subn(r'\g<1>' + name + '?v=' + ver + r'\g<2>', html)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parent.parent),
        help="heartbeat dir containing index.html and the assets",
    )
    args = ap.parse_args()
    root = Path(args.root)
    index = root / "index.html"
    if not index.is_file():
        print(f"[stamp] ERROR: no index.html at {index}", file=sys.stderr)
        return 1

    html = index.read_text()
    changed = []
    for name in ASSETS:
        asset = root / name
        if not asset.is_file():
            print(f"[stamp] WARN: asset missing, skipping: {name}", file=sys.stderr)
            continue
        ver = short_hash(asset)
        html, n = stamp(html, name, ver)
        if n == 0:
            print(f"[stamp] WARN: include not found in index.html: {name}", file=sys.stderr)
        else:
            changed.append(f"{name}?v={ver}")

    if html != index.read_text():
        index.write_text(html)
        print("[stamp] updated index.html:", ", ".join(changed))
    else:
        print("[stamp] OK: asset versions already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

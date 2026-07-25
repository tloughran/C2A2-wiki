#!/usr/bin/env python3
"""Deterministically stamp a page's local asset includes with a content hash.

Why this exists
---------------
explorer.html force-freshes each tab's iframe document (`?v=Date.now()`), but it
cannot reach inside that document. So any asset the sub-page loads with a bare
`src="app.js"` is served from the browser cache even though the HTML is fresh —
a guaranteed stale-asset mismatch on every edit (the 2026-06-26 "What is a lens?"
dead-click bug). The fragile fix is to hand-bump `?v=N` on each edit; the robust
fix is to make the version a function of file content, so it is always correct
and no human has to remember.

This script rewrites the `?v=` of each local asset include to the first 10 hex
of the file's SHA-1. Idempotent: unchanged assets -> identical HTML.

Targets (--target)
------------------
`heartbeat` (DEFAULT) -- heartbeat/index.html. The default is deliberately NARROW:
    refresh_snapshot.sh runs this script with no arguments inside the heartbeat
    cron, and that cron's constitutional carve-out lets it push ONLY data files.
    If the default stamped explorer.html too, a stale stamp would make an
    unattended job commit HTML -- exactly what the carve-out forbids.
`explorer`  -- explorer.html's shared CCL engine include. The shell is a normal
    cacheable document loading a SEPARATE lib file, so it has the same
    stale-asset exposure as an iframe tab and the same fix applies.
`all`       -- both. Use before a human-reviewed push.

Run standalone after editing any asset, or let refresh_snapshot.sh run it.
`--check` stamps nothing and exits non-zero if any include is stale -- for use
as a loud pre-push gate rather than a silent fixer.
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

# Local asset includes that must be content-stamped, per target. Paths are
# relative to the page's own directory, exactly as they appear in the HTML.
# (CDN/remote includes are intentionally excluded — they are versioned at the
# source.)
TARGETS = {
    "heartbeat": ("heartbeat/index.html", ("styles.css", "heartbeat-config.js", "app.js", "auth.js")),
    "explorer": ("explorer.html", ("lib/c2a2-commandline.js",)),
}


def short_hash(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()[:10]


def stamp(html: str, name: str, ver: str) -> tuple[str, int]:
    # Anchor on the attribute quote so we only touch the real include, never a
    # coincidental substring elsewhere in the document.
    pat = re.compile(
        r'((?:href|src)=")' + re.escape(name) + r'(?:\?v=[A-Za-z0-9]+)?(")'
    )
    return pat.subn(r'\g<1>' + name + '?v=' + ver + r'\g<2>', html)


def stamp_page(wiki: Path, page_rel: str, assets: tuple[str, ...], check: bool) -> int:
    """Stamp (or check) one page. Returns 0 ok, 1 error/stale."""
    page = wiki / page_rel
    if not page.is_file():
        print(f"[stamp] ERROR: no page at {page}", file=sys.stderr)
        return 1

    before = page.read_text()
    html = before
    changed = []
    for name in assets:
        asset = page.parent / name
        if not asset.is_file():
            print(f"[stamp] WARN: asset missing, skipping: {name}", file=sys.stderr)
            continue
        ver = short_hash(asset)
        html, n = stamp(html, name, ver)
        if n == 0:
            print(f"[stamp] WARN: include not found in {page_rel}: {name}", file=sys.stderr)
        else:
            changed.append(f"{name}?v={ver}")

    if html == before:
        print(f"[stamp] OK: {page_rel} asset versions already current")
        return 0
    if check:
        # Loud on purpose: a stale include ships fresh HTML against a cached
        # asset, which is invisible in tests and only breaks in a real browser.
        print(f"[stamp] STALE: {page_rel} needs {', '.join(changed)}", file=sys.stderr)
        return 1
    page.write_text(html)
    print(f"[stamp] updated {page_rel}:", ", ".join(changed))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--target",
        choices=("heartbeat", "explorer", "all"),
        default="heartbeat",
        help="which page(s) to stamp; default is heartbeat only (see module docstring)",
    )
    ap.add_argument(
        "--wiki",
        default=str(Path(__file__).resolve().parents[2]),
        help="wiki dir the target paths are relative to",
    )
    ap.add_argument(
        "--check",
        action="store_true",
        help="stamp nothing; exit non-zero if any include is stale (pre-push gate)",
    )
    args = ap.parse_args()

    wiki = Path(args.wiki)
    names = tuple(TARGETS) if args.target == "all" else (args.target,)
    rc = 0
    for name in names:
        page_rel, assets = TARGETS[name]
        rc |= stamp_page(wiki, page_rel, assets, args.check)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())

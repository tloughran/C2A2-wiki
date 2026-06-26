#!/usr/bin/env python3
"""Deterministic exporter: Heartbeat runtime /api/digest -> tab snapshot.

Phase 1 of Pathway 30. Maps the runtime's window_report payload into the static
`data/digest.json` the tab reads (schema: data/README.md), and keeps a dated
snapshot for historical depth. This is a plain field map with NO model in the
loop — see the project working agreement, Rule 5 ("if code can answer, code
answers") and AGENTS.md ("never invent source claims").

Input (one of):
  --from-file PATH   a saved /api/digest JSON response
  --url URL          fetch it directly (stdlib urllib), e.g.
                     http://127.0.0.1:8765/api/digest?window=weekly

Output:
  <data-dir>/digest.json                      (latest; what the tab loads)
  <data-dir>/snapshots/digest-YYYY-MM-DD.json (dated; historical depth)

Stdlib only. Runs on the Mac next to the runtime; not in the Cowork sandbox.
"""

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

SCHEMA_VERSION = 1


def load_report(args) -> dict:
    if args.from_file:
        return json.loads(Path(args.from_file).read_text(encoding="utf-8"))
    if args.url:
        req = Request(args.url, headers={"Accept": "application/json"})
        if args.token:
            req.add_header("Authorization", "Bearer " + args.token)
        with urlopen(req, timeout=args.timeout) as resp:  # noqa: S310 (local, operator-supplied URL)
            return json.loads(resp.read().decode("utf-8"))
    raise SystemExit("error: provide --from-file PATH or --url URL")


def prettify_theme(tag: str) -> str:
    # governance_policy -> Governance Policy ; capability_jump -> Capability Jump
    return " ".join(w.capitalize() for w in str(tag).replace("-", "_").split("_") if w)


def derive_primary_themes(stories: list, summary: str) -> str:
    """Top 2 tags by frequency across the shown stories; deterministic."""
    counter = Counter()
    for s in stories:
        for t in (s.get("tags") or []):
            counter[t] += 1
    top = [prettify_theme(t) for t, _ in counter.most_common(2)]
    if top:
        return " + ".join(top)
    # fall back to the runtime's own summary phrasing if no tags present
    m = re.search(r"Top risk themes:\s*([^.]+)\.", summary or "")
    return m.group(1).strip() if m else "—"


def derive_high_relevance(stories: list, summary: str, count_total: int) -> int:
    """Prefer the runtime's exact 'N items flagged high C2A2 relevance' count;
    fall back to counting relevance>=2 among the shown stories."""
    m = re.search(r"(\d+)\s+items?\s+flagged\s+high", summary or "")
    if m:
        return int(m.group(1))
    return sum(1 for s in stories if int(s.get("relevance", 0)) >= 2)


def map_signal(story: dict) -> dict:
    url = story.get("url") or story.get("source_url") or ""
    return {
        "title": story.get("title", ""),
        "source": story.get("source_name", ""),
        "url": url,
        "relevance": int(story.get("relevance", 0)),
        "tags": list(story.get("tags") or []),
        "summary": story.get("summary", ""),
        "implication": story.get("implications", ""),
    }


def build_digest(report: dict, limit: int) -> dict:
    stories = report.get("top_stories") or []
    sources = report.get("sources") or []
    summary = report.get("summary") or ""
    shown = stories[:limit]
    now = datetime.now(timezone.utc)
    return {
        "seed": False,
        "generated": now.strftime("%Y-%m-%d"),
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "window": report.get("window", "weekly"),
        "metrics": {
            "sources_reached": len(sources),
            "items_checked": int(report.get("count", len(stories))),
            "high_relevance": derive_high_relevance(stories, summary, int(report.get("count", 0))),
            "primary_themes": derive_primary_themes(shown, summary),
        },
        "signals": [map_signal(s) for s in shown],
        "schema_ver": SCHEMA_VERSION,
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--from-file", help="path to a saved /api/digest JSON response")
    src.add_argument("--url", help="runtime /api/digest URL to fetch")
    p.add_argument("--token", help="bearer token, if the runtime requires one")
    p.add_argument("--timeout", type=float, default=15.0)
    p.add_argument("--limit", type=int, default=12, help="max signals to write (default 12)")
    p.add_argument("--data-dir", default=str(Path(__file__).resolve().parent.parent / "data"),
                   help="output dir (default: ../data next to this script)")
    args = p.parse_args(argv)

    report = load_report(args)
    if not isinstance(report, dict) or "top_stories" not in report:
        raise SystemExit("error: input does not look like an /api/digest response (no 'top_stories')")

    digest = build_digest(report, args.limit)

    data_dir = Path(args.data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)

    # Write only the latest digest.json. Per-update History snapshots are written
    # AFTER enrichment by archive_snapshot.py, so each archived snapshot already
    # carries its long summaries.
    text = json.dumps(digest, indent=2, ensure_ascii=False) + "\n"
    latest = data_dir / "digest.json"
    latest.write_text(text, encoding="utf-8")

    m = digest["metrics"]
    print("wrote {0}".format(latest))
    print("  window={0} sources={1} items={2} high_rel={3} themes={4!r} signals={5}".format(
        digest["window"], m["sources_reached"], m["items_checked"],
        m["high_relevance"], m["primary_themes"], len(digest["signals"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())

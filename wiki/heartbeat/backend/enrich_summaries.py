#!/usr/bin/env python3
"""Deterministic Distill-layer merge: long_summaries sidecar -> digest.json.

Pathway 30 §4 (Distill) + Pathway 14 (honesty layer). This step is the
*model-free* half of the summary pipeline: the ~150-word summaries are written
by a model into `data/long_summaries.json` (keyed by signal URL, with model+date
provenance), and THIS script merely merges them into `data/digest.json` and the
matching dated snapshot. Keeping the merge deterministic means a rebuild never
re-pays tokens and never invents text (working-agreement Rule 5; AGENTS.md
"never invent source claims").

It also performs one deterministic display cleanup: stripping the
"arXiv:NNNN.NNNNNvN Announce Type: ... Abstract:" boilerplate that arXiv RSS
prepends to the short `summary`, so the short blurb reads cleanly. No model.

Idempotent: re-running yields the same file. Signals whose URL is absent from
the sidecar are left untouched (graceful degradation; the tab shows the short
summary only).

Usage:
  python3 enrich_summaries.py                      # uses ../data next to script
  python3 enrich_summaries.py --data-dir /path/to/wiki/heartbeat/data
  python3 enrich_summaries.py --check              # report only, write nothing

Stdlib only.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# arXiv RSS prepends e.g. "arXiv:2606.24112v1 Announce Type: new Abstract: ..."
ARXIV_BOILERPLATE = re.compile(
    r"^\s*arXiv:\s*\S+\s+Announce\s+Type:\s*\w+\s+Abstract:\s*",
    re.IGNORECASE,
)


def clean_short_summary(text: str) -> str:
    if not text:
        return text
    return ARXIV_BOILERPLATE.sub("", text).strip()


def load_sidecar(data_dir: Path) -> dict:
    p = data_dir / "long_summaries.json"
    if not p.exists():
        return {}
    raw = json.loads(p.read_text(encoding="utf-8"))
    # Accept either {"entries": {...}} or a bare {url: {...}} mapping.
    return raw.get("entries", raw) if isinstance(raw, dict) else {}


def enrich_digest(digest: dict, sidecar: dict) -> tuple[dict, int, int]:
    matched = 0
    cleaned = 0
    for sig in digest.get("signals", []):
        new_short = clean_short_summary(sig.get("summary", ""))
        if new_short != sig.get("summary", ""):
            sig["summary"] = new_short
            cleaned += 1
        entry = sidecar.get(sig.get("url", ""))
        if entry and entry.get("long_summary"):
            sig["long_summary"] = entry["long_summary"]
            sig["summary_provenance"] = {
                "model": entry.get("model", ""),
                "generated": entry.get("generated", ""),
                "kind": entry.get("kind", "machine-generated"),
            }
            matched += 1
    return digest, matched, cleaned


def process_file(path: Path, sidecar: dict, write: bool) -> str:
    digest = json.loads(path.read_text(encoding="utf-8"))
    digest, matched, cleaned = enrich_digest(digest, sidecar)
    if write:
        path.write_text(
            json.dumps(digest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return "{0}: {1} signals, {2} long-summary matches, {3} short-summaries cleaned".format(
        path.name, len(digest.get("signals", [])), matched, cleaned
    )


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument(
        "--data-dir",
        default=str(Path(__file__).resolve().parent.parent / "data"),
        help="dir holding digest.json + long_summaries.json (default: ../data)",
    )
    p.add_argument("--check", action="store_true", help="report only; write nothing")
    p.add_argument(
        "--all-snapshots",
        action="store_true",
        help="also enrich every dated file under snapshots/",
    )
    args = p.parse_args(argv)

    data_dir = Path(args.data_dir)
    sidecar = load_sidecar(data_dir)
    if not sidecar:
        print("warning: no long_summaries.json found (or empty); only cleaning short summaries")

    # Enrich digest.json (latest). Per-update snapshots are archived AFTER this
    # step (archive_snapshot.py copies the already-enriched digest.json), so we
    # don't target dated snapshots here. --all-snapshots can still backfill old ones.
    targets = [data_dir / "digest.json"]
    if args.all_snapshots:
        targets += sorted((data_dir / "snapshots").glob("digest-*.json"))

    for t in targets:
        if not t.exists():
            print("skip (missing):", t)
            continue
        print(process_file(t, sidecar, write=not args.check))
    if args.check:
        print("(--check: no files written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env bash
# refresh_review_log.sh — deterministic regen of the Review Log.
# Run AFTER the daily decision-processing/ingest step. Pure transform: no LLM,
# no Gmail. (New decision emails must already be appended to
# provenance/decision_emails.json by the daily agent's Gmail step — see CLAUDE.md.)
#
# Usage:  bash scripts/refresh_review_log.sh
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HERE"

python3 scripts/build_provenance.py wiki provenance --threshold 0.60
python3 scripts/assemble_review_log.py wiki provenance wiki/review_log.html

# Fail loud if the output is missing or suspiciously small.
test -s wiki/review_log.html
SIZE=$(wc -c < wiki/review_log.html)
if [ "$SIZE" -lt 500000 ]; then
  echo "FAIL: review_log.html only ${SIZE} bytes (<500KB) — aborting." >&2
  exit 1
fi
echo "OK: wiki/review_log.html refreshed (${SIZE} bytes)."

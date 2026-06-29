#!/usr/bin/env bash
# PHASE 2: commit the staged changes and push to GH main.
# Run ONLY after Phase 1 staged cleanly AND the HTML review passed sign-off.
set -euo pipefail

REPO="/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
cd "$REPO"

# Re-assert hep-det is not staged before committing.
if git diff --cached --name-only | grep -q '^hep-det/'; then
  echo "ABORT: hep-det files are staged. Unstage with: git reset -- hep-det"
  exit 1
fi

git commit -m "Daily agent output 2026-06-26..28 + L2 signal-stream tab

- architecture logs, lit-search for/against, metrics snapshots, daily_sync
- proposal lifecycle: pending -> approved/denied, new 06-27/06-28 proposals
- 9 synthesis bridges; community_interactions.html, prs_3d.html (reviewed)
- publish Level-2 signal stream: prototypes/ + wiki/level2_signal_stream.html
- exclude running HEP-DET session scratch (hep-det/)"

# Pushes this commit AND the already-made ca9ea23 (Summa vault sync 06-27).
git push origin main

echo "=== pushed; confirm parity ==="
git log --oneline -3
git status -sb | head -1

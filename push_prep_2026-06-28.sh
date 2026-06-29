#!/usr/bin/env bash
# Push-prep for RC Karpathy Wiki -> GH main, 2026-06-28
# PHASE 1 only: clean, stage (excluding the running HEP-DET session),
# and start a local HTTP server for the constitutional HTML review.
# It does NOT commit or push. Commit/push is Phase 2, after sign-off.
set -euo pipefail

REPO="/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
cd "$REPO"

# 1. Clear the stale lock left by the HEP-DET session (00:39 today).
if [ -f .git/index.lock ]; then
  echo "Removing stale .git/index.lock"
  rm -f .git/index.lock
fi

# 2. Remove the empty sewing/janitor unlink-test artifact (junk, not for commit).
rm -f "wiki/synthesis/__unlinktest_maUx.md"

# 3. Stage everything EXCEPT the running HEP-DET session scratch.
#    prototypes/ and wiki/level2_signal_stream.html ARE included (publish: yes).
git add -A -- . ':!hep-det' ':!hep-det/**'

# 4. Safety check: confirm hep-det was NOT staged.
echo "=== sanity: hep-det must show nothing below this line ==="
git diff --cached --name-only | grep '^hep-det/' || echo "OK - hep-det excluded"
echo "=== staged file count ==="
git diff --cached --name-only | wc -l

# 5. Start the local HTTP server for the constitutional review.
#    Default review target: http://localhost:8080/explorer.html
echo "Starting http.server on 8080 (Ctrl-C to stop after review)"
cd wiki && python3 -m http.server 8080

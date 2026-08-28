#!/usr/bin/env bash
# git_unlock.sh -- clear STALE git lock files, and only stale ones.
#
# The recurring failure: a git process dies mid-write (a sandbox call whose
# transport times out, a killed worktree add) and leaves a 0-byte .git/index.lock
# behind. Every later git write in the repo then fails with "Another git process
# seems to be running", and stays failing until a human notices. There are 23
# quarantined lock corpses in _to_delete/ and _stale_locks/ recording how often
# this has happened, plus a runbook, plus a weekly verifier -- all of which
# describe the problem rather than clear it.
#
# A lock is treated as STALE only when BOTH hold:
#   1. no git process is running against this repo, AND
#   2. the lock is at least MIN_AGE_SECONDS old (default 120)
# Either condition failing means a real git operation may be in flight, and this
# script does nothing. Removing a live lock corrupts the index; refusing to
# remove a dead one only costs a retry. The asymmetry sets the default.
#
# Removed locks are MOVED to _stale_locks/ (gitignored), never deleted, because
# check_scheduler_health's git-debris check reads them as evidence.
#
# Exit 0 = repo is writable now (whether or not anything was cleared)
# Exit 2 = a lock is present and looks LIVE; caller should back off, not retry

set -euo pipefail

REPO="${REPO:-/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project}"
MIN_AGE_SECONDS="${MIN_AGE_SECONDS:-120}"
QUARANTINE="$REPO/_stale_locks"

cd "$REPO"
STAMP=$(date '+%Y-%m-%dT%H:%M:%S%z')
say() { printf '[%s] %s\n' "$STAMP" "$*"; }

LOCKS=$(find .git -maxdepth 3 -name '*.lock' -type f 2>/dev/null || true)
if [ -z "$LOCKS" ]; then
  say "no locks present"
  exit 0
fi

# Any git process with this repo in its command line, excluding ourselves.
if pgrep -fl 'git ' 2>/dev/null | grep -F "$REPO" | grep -qv git_unlock; then
  say "LIVE: a git process is running against this repo. Nothing cleared."
  pgrep -fl 'git ' | grep -F "$REPO" | sed 's/^/    /'
  exit 2
fi

NOW=$(date +%s)
mkdir -p "$QUARANTINE"
CLEARED=0; HELD=0
while IFS= read -r lk; do
  [ -e "$lk" ] || continue
  mtime=$(stat -f %m "$lk")
  age=$((NOW - mtime))
  if [ "$age" -lt "$MIN_AGE_SECONDS" ]; then
    say "HOLD  $lk -- only ${age}s old (< ${MIN_AGE_SECONDS}s); may be live"
    HELD=$((HELD+1))
    continue
  fi
  dest="$QUARANTINE/$(basename "$lk").$(date +%s)"
  mv "$lk" "$dest"
  say "CLEARED $lk (age ${age}s, size $(stat -f %z "$dest")) -> ${dest#$REPO/}"
  CLEARED=$((CLEARED+1))
done <<< "$LOCKS"

if [ "$HELD" -gt 0 ]; then
  say "$CLEARED cleared, $HELD held as possibly live"
  exit 2
fi
say "$CLEARED stale lock(s) cleared; repo is writable"
exit 0

#!/bin/bash
# Drive every path of sync_vault.sh's git-lock handling.
#
# The block under test replaced an unconditional `rm -f` of .git/index.lock,
# HEAD.lock and refs/heads/main.lock. That rm was justified as safe because the
# script is "the only scheduled writer of wiki/vault/" -- true about wiki/vault/,
# false about the lock, which is repo-global. Stealing a lock a live git holds kills
# that process mid-write and strands .git/objects/**/tmp_obj_* (535 of them,
# 2026-07-31..08-13).
#
# So the case that matters most is #4: a lock HELD by a live process must still be
# there when the script gives up. A test that only covers the happy path would have
# passed against the old broken code too.
#
# The opposite regression matters as much: the rm existed because a crashed daily-run
# left a 0-byte HEAD.lock that blocked the sync for ~17h. Case 2 is that one -- an
# abandoned lock must still get cleared, or this "fix" trades a silent steal for a
# silent stall.
#
#     bash scripts/test_sync_vault_locks.sh

set -uo pipefail

SRC="$(cd "$(dirname "$0")/.." && pwd)/sync_vault.sh"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

FAILURES=0
expect() {
  if [ "$2" = "$3" ]; then
    echo "  ok   $1"
  else
    echo "  FAIL $1"
    echo "         expected: $3"
    echo "         got:      $2"
    FAILURES=$(( FAILURES + 1 ))
  fi
}

# Lift the lock block out of sync_vault.sh rather than copying it here: a copy would
# keep passing after the real script changed, which is the classic way a test starts
# lying. Everything from GIT_LOCKS= down to (not including) the bare call.
HARNESS="$WORK/harness.sh"
{
  # `set -euo pipefail` verbatim from sync_vault.sh:18, NOT a relaxed variant. errexit
  # is the whole hazard here: `[ -z "$x" ] && return 0` and a bare `lsof` that exits 1
  # on no-match are exactly the shapes that kill a script under -e, and that is how
  # publish_metabolism.sh died wordlessly on 2026-08-09. Testing without -e would
  # exercise a script that does not exist.
  echo 'set -euo pipefail'
  echo 'REPO="$1"'
  echo 'log() { echo "$*"; }'
  echo 'fail_loud() { echo "FAIL_LOUD $1"; exit 1; }'
  sed -n '/^GIT_LOCKS="\$REPO/,/^wait_for_git_locks$/p' "$SRC" | sed '$d'
  echo 'wait_for_git_locks'
  echo 'echo "PROCEEDED"'
} > "$HARNESS"

# If the extraction silently caught nothing, every case below would "pass" against an
# empty harness. Assert the shape before trusting a single result.
extracted=$(grep -c 'wait_for_git_locks()' "$HARNESS")
expect "the lock block was extracted from the real sync_vault.sh" "$extracted" "1"
# The call itself, not the word: `lsof` also appears in the comments explaining why
# the holder test is not an age test, and matching those would pass on a harness that
# extracted only prose.
expect "extraction pulled in the lsof-based holder test" \
  "$(grep -c 'LSOF" -t --' "$HARNESS")" "1"
expect "extraction pulled in the missing-lsof fail-safe" \
  "$(grep -c 'unknown-no-lsof' "$HARNESS")" "1"

fresh_repo() {
  rm -rf "$WORK/repo"
  mkdir -p "$WORK/repo/.git/refs/heads"
  echo "$WORK/repo"
}

run() {  # run <repo> -> stdout+exit, with the waits collapsed so this finishes
  GIT_LOCK_ATTEMPTS=2 GIT_LOCK_WAIT_SECS=1 GIT_LOCK_STALE_AGE=2 \
    /bin/bash "$HARNESS" "$1" 2>&1
}

echo
echo "1. a clean repo just proceeds:"
R=$(fresh_repo)
OUT=$(run "$R"); RC=$?
expect "no locks -> exit 0" "$RC" "0"
expect "no locks -> reaches the git work" \
  "$(echo "$OUT" | grep -c PROCEEDED)" "1"

echo
echo "2. an ABANDONED lock is still cleared (the ~17h HEAD.lock case):"
R=$(fresh_repo)
: > "$R/.git/HEAD.lock"
touch -t 202601010000 "$R/.git/HEAD.lock"   # older than GIT_LOCK_STALE_AGE
OUT=$(run "$R"); RC=$?
expect "abandoned lock -> exit 0" "$RC" "0"
expect "abandoned lock -> removed" "$([ -e "$R/.git/HEAD.lock" ] && echo present || echo gone)" "gone"
expect "abandoned lock -> said so out loud" \
  "$(echo "$OUT" | grep -c 'ABANDONED')" "1"
expect "abandoned lock -> proceeds to the git work" \
  "$(echo "$OUT" | grep -c PROCEEDED)" "1"

echo
echo "3. a lock HELD by a live process is NOT stolen (the bug this fixes):"
R=$(fresh_repo)
: > "$R/.git/index.lock"
touch -t 202601010000 "$R/.git/index.lock"  # old enough that AGE ALONE would clear it
/bin/bash -c 'exec 9>"$1"; sleep 6' _ "$R/.git/index.lock" &
HOLDER=$!
sleep 0.5
OUT=$(run "$R"); RC=$?
wait "$HOLDER" 2>/dev/null
expect "held lock -> refuses, exit 1" "$RC" "1"
expect "held lock -> the lock SURVIVES (never stolen)" \
  "$([ -e "$R/.git/index.lock" ] && echo present || echo gone)" "present"
expect "held lock -> never reaches the git work" \
  "$(echo "$OUT" | grep -c PROCEEDED)" "0"
expect "held lock -> reported as held, not as abandoned" \
  "$(echo "$OUT" | grep -c 'HELD by a live process')" "2"
expect "held lock -> fails loud rather than logging quietly" \
  "$(echo "$OUT" | grep -c 'FAIL_LOUD')" "1"
expect "held lock -> never claims to have cleared anything" \
  "$(echo "$OUT" | grep -c 'ABANDONED')" "0"

echo
echo "4. an unheld lock TOO YOUNG to call abandoned is left alone:"
R=$(fresh_repo)
: > "$R/.git/index.lock"                    # age 0, no holder
# Staleness threshold far beyond the total wait (2 attempts x 1s), or the lock ages
# out mid-test and this silently becomes a second copy of case 5. It did exactly
# that at 2s/2s -- the two cases differ ONLY by that margin, so it has to be explicit.
OUT=$(GIT_LOCK_ATTEMPTS=2 GIT_LOCK_WAIT_SECS=1 GIT_LOCK_STALE_AGE=600 \
        /bin/bash "$HARNESS" "$R" 2>&1); RC=$?
expect "young unheld lock -> refuses rather than guessing, exit 1" "$RC" "1"
expect "young unheld lock -> survives" \
  "$([ -e "$R/.git/index.lock" ] && echo present || echo gone)" "present"
expect "young unheld lock -> says why it would not act" \
  "$(echo "$OUT" | grep -c 'too soon to call it abandoned')" "2"

echo
echo "5. a young unheld lock that ages out mid-wait IS then cleared:"
R=$(fresh_repo)
: > "$R/.git/refs/heads/main.lock"
OUT=$(GIT_LOCK_ATTEMPTS=4 GIT_LOCK_WAIT_SECS=1 GIT_LOCK_STALE_AGE=2 \
        /bin/bash "$HARNESS" "$R" 2>&1); RC=$?
expect "aged-out lock -> exit 0" "$RC" "0"
expect "aged-out lock -> removed once it was old enough" \
  "$([ -e "$R/.git/refs/heads/main.lock" ] && echo present || echo gone)" "gone"

echo
echo "6. a MISSING lsof must not silently turn every lock into 'abandoned':"
# sync_vault.sh sets no PATH and launchd's default is not the shell's, so an
# unreachable /usr/sbin/lsof is a live possibility. If that degraded to "no holder"
# the script would steal every lock again -- the original bug, restored by the back
# door, and invisible because the happy path still passes.
R=$(fresh_repo)
: > "$R/.git/index.lock"
touch -t 202601010000 "$R/.git/index.lock"  # old enough that age ALONE would clear it
OUT=$(LSOF="$WORK/no-such-lsof" GIT_LOCK_ATTEMPTS=2 GIT_LOCK_WAIT_SECS=1 \
      GIT_LOCK_STALE_AGE=2 /bin/bash "$HARNESS" "$R" 2>&1); RC=$?
expect "no lsof -> refuses rather than guessing, exit 1" "$RC" "1"
expect "no lsof -> the lock SURVIVES" \
  "$([ -e "$R/.git/index.lock" ] && echo present || echo gone)" "present"
expect "no lsof -> never claims the lock was abandoned" \
  "$(echo "$OUT" | grep -c 'ABANDONED')" "0"
expect "no lsof -> names the missing detector in the log" \
  "$(echo "$OUT" | grep -c 'unknown-no-lsof')" "3"

echo
echo "7. all three lock paths are watched, not just index.lock:"
for name in index.lock HEAD.lock refs/heads/main.lock; do
  R=$(fresh_repo)
  : > "$R/.git/$name"
  touch -t 202601010000 "$R/.git/$name"
  OUT=$(run "$R")
  expect "$name is seen and cleared" \
    "$([ -e "$R/.git/$name" ] && echo present || echo gone)" "gone"
done

echo
if [ "$FAILURES" -ne 0 ]; then
  echo "$FAILURES FAILED"
  exit 1
fi
echo "all assertions passed"

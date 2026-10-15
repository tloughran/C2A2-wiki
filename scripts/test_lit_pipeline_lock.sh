#!/bin/bash
# Drive every path of lit_pipeline_lock.sh.
#
# WHAT THIS TEST IS ABOUT
# -----------------------
# Not "does a lock file exist". A lock file existed on 2026-10-15 -- the losing
# instance wrote LOCKED at 04:34:38Z -- and the pipeline still lost 8-9 KB of
# abstract- and full-text literature reads per file, four files, because a second
# copy overwrote them at 04:38:13Z and the first copy then withdrew its own
# register appends to avoid duplicating the second's dispositions.
#
# So the thing under test is the PROPERTY THAT MATTERED: when two copies race,
# exactly one may proceed, and the loser must leave the winner's result files
# byte-identical. Case 2 asserts the bytes, not the lock. Case 3 runs the OLD
# mechanism -- read the free-text status word, then write it -- against the same
# race and shows two winners, which is why a test of lock-file existence would
# have passed against the code that lost the data.
#
# Case 6 is the opposite regression and matters as much. A stale timeout set too
# short turns a long-but-healthy run into a broken lock and reproduces the
# overwrite with extra steps. Case 5 and case 6 bracket it: 6h+1s breaks, 6h-1s
# does not.
#
#     bash scripts/test_lit_pipeline_lock.sh

set -uo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)/lit_pipeline_lock.sh"
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

export LIT_PIPELINE_LOCK_DIR="$WORK/lit_pipeline.lock.d"
export LIT_PIPELINE_LOCK_AUDIT="$WORK/lit_pipeline.lock"
export LIT_PIPELINE_LOCK_STALE_HOURS=6

lock() { bash "$SRC" "$@" 2>>"$WORK/stderr.log"; echo "rc=$?"; }
rc()   { bash "$SRC" "$@" >/dev/null 2>>"$WORK/stderr.log"; echo "$?"; }
reset_lock() { rm -rf "$LIT_PIPELINE_LOCK_DIR" "$LIT_PIPELINE_LOCK_DIR.break"; }

# The four files the 10-15 run lost, at the size it lost them at.
RESULTS="$WORK/lit_search_results"
mkdir -p "$RESULTS"
seed_results() {  # seed_results <marker> <kb>
  for n in 1141_for 1141_against 1146_for 1146_against; do
    { echo "WRITER=$1"; head -c "$(( $2 * 1024 ))" /dev/zero | tr '\0' 'x'; } > "$RESULTS/$n.md"
  done
}

echo "0. the script is the real one and is executable:"
expect "lit_pipeline_lock.sh exists" "$([ -f "$SRC" ] && echo yes || echo no)" "yes"
expect "acquisition is an atomic mkdir, not a test-then-create" \
  "$(grep -c 'if mkdir "\$LOCKDIR" 2>/dev/null; then' "$SRC")" "1"
# The two `[ ! -d "$LOCKDIR" ]` tests in the script are AFTER the mkdir (a
# could-not-create sanity check, and release's already-gone check). What must not
# exist is an existence test BEFORE it, which is the shape that races.
expect "nothing tests the lock dir's existence before the mkdir" \
  "$(sed -n '/^  acquire)/,/if mkdir "\$LOCKDIR"/p' "$SRC" | grep -c '\-d "\$LOCKDIR"')" "0"

echo
echo "1. a free lock is acquired, and status reports it:"
reset_lock
expect "status on a free lock -> 0 FREE" "$(rc status)" "0"
expect "acquire on a free lock -> 0" "$(rc acquire --run-id A1)" "0"
expect "the lock directory now exists" \
  "$([ -d "$LIT_PIPELINE_LOCK_DIR" ] && echo yes || echo no)" "yes"
expect "status on a held lock -> 3" "$(rc status)" "3"
expect "the acquisition is recorded in the audit file" \
  "$(grep -c '^LOCKED .* by A1 ' "$LIT_PIPELINE_LOCK_AUDIT")" "1"

echo
echo "2. THE 10-15 CASE: the second copy must exit without touching the results."
echo "   (A holds the lock and has written 9 KB result files; B fires.)"
seed_results A 9
before=$(cat "$RESULTS"/*.md | shasum | cut -d' ' -f1)
b_rc=$(rc acquire --run-id B)
# A losing copy that respected the exit code would stop here. One that wrote
# anyway is what cost the data, so model both: only the honoured path may write.
if [ "$b_rc" = "0" ]; then seed_results B 2; fi
after=$(cat "$RESULTS"/*.md | shasum | cut -d' ' -f1)
expect "B's acquire -> 3 (HELD), not 0" "$b_rc" "3"
expect "A's four result files are byte-identical after B ran" "$after" "$before"
expect "A is still the recorded owner" \
  "$(cut -d' ' -f3 "$LIT_PIPELINE_LOCK_DIR/owner")" "A1"
expect "B's refusal is recorded, not silent" \
  "$(grep -c '^SKIPPED .* by B: lock held' "$LIT_PIPELINE_LOCK_AUDIT")" "1"
expect "B said so on stderr too" \
  "$(grep -c 'Exiting without writing' "$WORK/stderr.log")" "1"

echo
echo "3. the SAME race against the OLD mechanism (read the status word, then"
echo "   write it). This is the case that must fail, and does:"
old_lock="$WORK/old.lock"
echo "RELEASED 2026-10-14T00:00:00Z" > "$old_lock"
old_try() {   # the 10-02..10-15 protocol, verbatim in shape: read, then write
  local id="$1"
  if grep -q '^LOCKED' "$old_lock" 2>/dev/null; then echo "skip"; return; fi
  sleep 0.1                                   # the window between test and act
  echo "LOCKED by $id" > "$old_lock"
  echo "win"
}
old_wins=$( { old_try A & old_try B & wait; } | grep -c '^win' )
expect "the old read-then-write protocol lets BOTH copies proceed" "$old_wins" "2"

reset_lock
new_wins=$( { rc acquire --run-id A & rc acquire --run-id B & wait; } | grep -c '^0$' )
expect "the atomic lock lets exactly ONE of the same two copies proceed" "$new_wins" "1"

echo
echo "4. eight copies firing at once still yield exactly one writer:"
reset_lock
eight=$( { for i in 1 2 3 4 5 6 7 8; do rc acquire --run-id "R$i" & done; wait; } | grep -c '^0$' )
expect "8 concurrent acquires -> 1 winner" "$eight" "1"

echo
echo "5. release frees the lock, and the next run gets it:"
reset_lock
rc acquire --run-id A >/dev/null
expect "release -> 0" "$(rc release --run-id A --note 'test run')" "0"
expect "the lock directory is gone" \
  "$([ -d "$LIT_PIPELINE_LOCK_DIR" ] && echo present || echo gone)" "gone"
expect "the release is recorded" \
  "$(grep -c '^RELEASED .* by A ' "$LIT_PIPELINE_LOCK_AUDIT")" "1"
expect "the next run acquires cleanly" "$(rc acquire --run-id C)" "0"

echo
echo "6. a lock 1s SHORT of the stale limit is NOT broken."
echo "   (A timeout set too short reproduces the overwrite, so this is the"
echo "    regression that matters as much as case 7.)"
reset_lock
mkdir -p "$LIT_PIPELINE_LOCK_DIR"
printf '%s %s %s %s %s\n' "$(( $(date -u +%s) - 6*3600 + 1 ))" "stamp" "DEAD" "host" "999" \
  > "$LIT_PIPELINE_LOCK_DIR/owner"
expect "5h59m59s-old lock -> 3 (still held)" "$(rc acquire --run-id D)" "3"
expect "no STALE-BREAK was recorded for it" \
  "$(grep -c '^STALE-BREAK .* by D' "$LIT_PIPELINE_LOCK_AUDIT")" "0"

echo
echo "7. a lock 1s PAST the stale limit is broken, loudly and on the record:"
reset_lock
: > "$WORK/stderr.log"
mkdir -p "$LIT_PIPELINE_LOCK_DIR"
printf '%s %s %s %s %s\n' "$(( $(date -u +%s) - 6*3600 - 1 ))" "stamp" "DEAD" "host" "999" \
  > "$LIT_PIPELINE_LOCK_DIR/owner"
expect "6h00m01s-old lock -> 0 (broken and taken)" "$(rc acquire --run-id E)" "0"
expect "the break is recorded in the audit file, naming the dead owner" \
  "$(grep -c '^STALE-BREAK .* by E: previous owner \[.*DEAD' "$LIT_PIPELINE_LOCK_AUDIT")" "1"
expect "the break is loud on stderr, not just filed" \
  "$(grep -c 'STALE-BREAK' "$WORK/stderr.log")" "1"
expect "the breaker is now the owner" \
  "$(cut -d' ' -f3 "$LIT_PIPELINE_LOCK_DIR/owner")" "E"

echo
echo "8. two copies meeting the SAME stale lock: breaking is single-winner too."
echo "   (A non-atomic stale break would re-introduce the defect at the one"
echo "    moment the lock is most likely to be contended.)"
reset_lock
mkdir -p "$LIT_PIPELINE_LOCK_DIR"
printf '%s %s %s %s %s\n' "$(( $(date -u +%s) - 99*3600 ))" "stamp" "DEAD" "host" "999" \
  > "$LIT_PIPELINE_LOCK_DIR/owner"
breakers=$( { rc acquire --run-id F & rc acquire --run-id G & wait; } | grep -c '^0$' )
expect "2 concurrent stale-breakers -> 1 winner" "$breakers" "1"

echo
echo "9. an owner file with no parseable stamp ages from the directory mtime,"
echo "   so a half-written owner cannot wedge the pipeline forever:"
reset_lock
mkdir -p "$LIT_PIPELINE_LOCK_DIR"
echo "garbage-no-epoch" > "$LIT_PIPELINE_LOCK_DIR/owner"
touch -t 202601010000 "$LIT_PIPELINE_LOCK_DIR"
expect "unparseable owner on an old dir -> broken, not wedged" "$(rc acquire --run-id H)" "0"

reset_lock
mkdir -p "$LIT_PIPELINE_LOCK_DIR"
echo "garbage-no-epoch" > "$LIT_PIPELINE_LOCK_DIR/owner"
expect "unparseable owner on a FRESH dir -> still held" "$(rc acquire --run-id I)" "3"

echo
echo "10. releasing a lock that is already gone is a no-op, not a crash:"
reset_lock
expect "release with no lock -> 0" "$(rc release --run-id J)" "0"
expect "it is recorded as a no-op" \
  "$(grep -c '^RELEASE-NOOP .* by J' "$LIT_PIPELINE_LOCK_AUDIT")" "1"

echo
echo "11. the audit file is append-only (it is the evidence of who ran):"
expect "the case-1 LOCKED line is still present at the end of the run" \
  "$(grep -c '^LOCKED .* by A1 ' "$LIT_PIPELINE_LOCK_AUDIT")" "1"

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "ALL PASS"
  exit 0
fi
echo "$FAILURES FAILURE(S)"
exit 1

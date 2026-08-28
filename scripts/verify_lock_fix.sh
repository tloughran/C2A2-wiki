#!/bin/bash
# Verify the 2026-08-13 git-lock work the morning after it went live.
#
# Answers the two time-gated questions from handoffs/sandbox-storage-cleanup.md
# that could not be answered the day they were written:
#
#   item 3  did the 21:00 sync_vault run take the clean path through the new
#           wait_for_git_locks(), or did it fail_loud?
#   item 4  the git-debris verdict on a store that was clean at session end --
#           the first true baseline. If tmp_obj files came back, the oldest and
#           newest mtimes name the job that stranded them.
#
# Runs DAILY 07:30 while Tom is away 2026-08-14..24, because "did the debris come
# back" is a question about a series, not a morning. One clean day proves nothing;
# ten days of readings, with the misses visible as gaps, is the actual evidence.
#
# Performs ZERO git writes -- pure reads plus its own two report files. A job that
# exists to measure lock contention must not add any, least of all unattended.
# Never commits, never pushes. Exit code is always 0: this is an instrument, and a
# WARN here is a finding to read, not a failure to run.
#
# $OUT is rewritten each run (latest detail); $HIST is appended one line per run
# and is the file to read on return. A day with no HIST line is a day this did not
# run -- almost always the Mac asleep, which silently drops the calendar fire.

set -uo pipefail

REPO="/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
OUT="$REPO/scheduler/lock_fix_verify.md"
HIST="$REPO/scheduler/lock_fix_history.tsv"
SYNC_LOG="$REPO/sync_vault.log"
COMMIT_LOG="$HOME/Library/Logs/c2a2-scheduled-commit-check.log"
AGE_FLOOR_MIN=60   # matches check_scheduler_health.py: younger than this is a live write

cd "$REPO" || { echo "FATAL: repo not found at $REPO"; exit 0; }
mkdir -p "$REPO/scheduler"

emit() { printf '%s\n' "$*" | tee -a "$OUT"; }

: >"$OUT"
emit "# Lock-fix verification — $(date '+%Y-%m-%d %H:%M:%S %Z')"
emit ""

# --- item 3: did last night's 21:00 sync take the clean path? --------------
emit "## Item 3 — sync_vault.sh, first unattended run of wait_for_git_locks()"
emit ""

SYNC_STATE=unknown
if [ -f "$REPO/sync_vault.FAILED" ]; then
  SYNC_STATE=REFUSED
  emit "**FAIL MARKER PRESENT** — the sync refused and published nothing. Reason:"
  emit ""
  emit '```'
  sed 's/^/    /' "$REPO/sync_vault.FAILED" | tee -a "$OUT" >/dev/null
  sed 's/^/    /' "$REPO/sync_vault.FAILED"
  emit '```'
  emit ""
  emit "A fail_loud from the lock code is the fix WORKING (it refused rather than"
  emit "stealing a live lock) -- but the vault did not publish either way, so read"
  emit "the reason above before deciding which."
else
  emit "No \`sync_vault.FAILED\` marker — the run did not refuse."
fi
emit ""

if [ -f "$SYNC_LOG" ]; then
  # The log is append-only across runs; the LAST "=== Summa vault sync started ==="
  # opens the run we want. Everything below is scoped to that block on purpose --
  # grepping the whole log surfaces lock fatals from months of earlier runs, undated,
  # which reads exactly like the new code failing tonight. (Caught 2026-08-13: a
  # whole-file grep returned ten identical pre-fix HEAD.lock fatals.)
  BLOCK=$(awk '/=== Summa vault sync started ===/{buf=""} {buf=buf $0 "\n"} END{printf "%s", buf}' "$SYNC_LOG")
  started=$(printf '%s' "$BLOCK" | grep -m1 '=== Summa vault sync started ===')

  emit "Last run block (${started:-no start line found}):"
  emit ""
  emit '```'
  printf '%s\n' "$BLOCK" | grep -vE '^\[.*\] +[A-Za-z0-9_/.-]+\.md$' | tail -25 | tee -a "$OUT"
  emit '```'
  emit ""
  emit "Expected on the clean path: 'Committed N change(s). Pushing...' then 'Push succeeded.'"
  emit ""
  emit "Lock lines **from that block only** — this is the new code reporting itself:"
  emit ""
  emit '```'
  if printf '%s\n' "$BLOCK" | grep -i 'lock' | tee -a "$OUT" | grep -q .; then
    :
  else
    emit "    (none — no lock was waited on, and none was removed: the clean path)"
  fi
  emit '```'

  # Two facts the history line needs: did last night's sync publish, and WHICH
  # night it was. A sync that did not run leaves yesterday's block in place and
  # would otherwise be logged as a fresh success every morning.
  SYNC_RUN_DATE=$(printf '%s' "$started" | sed -n 's/^\[\([0-9-]*\) .*/\1/p')
  [ -n "$SYNC_RUN_DATE" ] || SYNC_RUN_DATE=unknown
  if [ "$SYNC_STATE" != REFUSED ]; then
    if printf '%s\n' "$BLOCK" | grep -q 'Push succeeded'; then
      SYNC_STATE=pushed
    else
      SYNC_STATE=no-push-line
    fi
  fi
else
  SYNC_STATE=no-log
  SYNC_RUN_DATE=none
  emit "**No \`sync_vault.log\` at $SYNC_LOG** — the 21:00 job did not run at all."
fi
emit ""

# ANSWERED 2026-08-14, and deliberately removed rather than left running.
#
# Both commits are on origin (67d12ea, 734d2cd) -- the 08-13 21:00 push carried
# them. That question is closed, so the `git fetch` that answered it is gone too.
# This script now performs ZERO git writes: a fetch takes ref locks, and a job
# that exists to measure lock contention should not add any, least of all
# unattended for ten days.
#
# The subject-matching version is in git history if it is ever needed again.
# Do NOT restore the SHA-based form: sync_vault rebases before pushing, so the
# original SHAs stop being ancestors of origin/main the moment the push succeeds.

# --- item 4: the git-debris verdict on a store that started clean ----------
emit "## Item 4 — git debris, first true baseline"
emit ""
emit "The store was clean when session 2 ended on 08-13, so anything below arrived since."
emit ""

emit "What \`check_scheduler_health.py\` recorded at 05:45:"
emit ""
emit '```'
{ grep -i 'git debris' "$REPO/scheduler/scheduler_health.md" 2>/dev/null | tail -5
  grep -i 'git debris' "$COMMIT_LOG" 2>/dev/null | tail -5
} | tee -a "$OUT" | grep -q . || emit "    (no 'git debris' line in either file — either the 05:45 job did not run, or
    it ran an older check_scheduler_health.py without verdict_git_debris(). The
    verdict code was added 2026-08-13 at 14:28, AFTER that morning's 05:45 fire,
    so its absence is expected on 08-13 and only meaningful from 08-14 on.)"
emit '```'
emit ""

GITDIR=$(git rev-parse --git-common-dir 2>/dev/null)
case "$GITDIR" in
  /*) : ;;
  *)  GITDIR="$REPO/$GITDIR" ;;
esac

tmp_total=$(find "$GITDIR/objects" -name 'tmp_obj_*' 2>/dev/null | wc -l | tr -d ' ')
tmp_old=$(find "$GITDIR/objects" -name 'tmp_obj_*' -mmin "+$AGE_FLOOR_MIN" 2>/dev/null | wc -l | tr -d ' ')
emit "Live count right now: **$tmp_total** tmp_obj files, of which **$tmp_old** are older than ${AGE_FLOOR_MIN}m."
emit "(Younger than that is a healthy concurrent write, not debris.)"
emit ""

if [ "$tmp_old" -gt 0 ]; then
  emit "Stranded object mtimes — **this is the attribution session 2 could not make**,"
  emit "because session 1 deleted the 535 originals before reading their distribution:"
  emit ""
  emit '```'
  find "$GITDIR/objects" -name 'tmp_obj_*' -mmin "+$AGE_FLOOR_MIN" -exec stat -f '%Sm %N' -t '%Y-%m-%d %H:%M:%S' {} \; 2>/dev/null \
    | sort | sed -n '1p;$p' | tee -a "$OUT"
  emit '```'
  emit ""
  emit "**The leak survived the sync_vault fix.** Read the newest mtime — it names the"
  emit "slot. Next suspects are the sandboxed scheduled runs themselves (they bind-mount"
  emit "the real .git and are SIGKILLed at teardown), not sync_vault."
else
  emit "**OK — no stranded objects.** Consistent with sync_vault's lock-stealing having"
  emit "been the cause, but ONE clean day is not proof. Give it a week before believing it."
fi
emit ""

locks=$(find "$GITDIR" -maxdepth 3 \( -name 'index.lock' -o -name 'HEAD.lock' -o -name 'main.lock' \) -mmin "+$AGE_FLOOR_MIN" 2>/dev/null)
if [ -n "$locks" ]; then
  emit "**STALE LOCK — this blocks the next daily commit.** Held or abandoned is decided"
  emit "by lsof, not by age; check before removing anything:"
  emit ""
  emit '```'
  printf '%s\n' "$locks" | tee -a "$OUT"
  emit '```'
else
  emit "No stale lock files."
fi
emit ""

# --- the series ------------------------------------------------------------
# One line per run. This is the file to read on return: a gap in the date column
# is a morning this did not run at all, which is itself the finding.
stale_n=$(printf '%s' "$locks" | grep -c . )
debris_line=absent
{ grep -qi 'git debris' "$REPO/scheduler/scheduler_health.md" 2>/dev/null || \
  grep -qi 'git debris' "$COMMIT_LOG" 2>/dev/null; } && debris_line=present

if [ ! -f "$HIST" ]; then
  printf 'run_date\tsync_night\tsync_state\ttmp_total\ttmp_over_%dm\tstale_locks\t0545_debris_line\n' \
    "$AGE_FLOOR_MIN" >"$HIST"
fi
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
  "$(date '+%Y-%m-%d')" "$SYNC_RUN_DATE" "$SYNC_STATE" \
  "$tmp_total" "$tmp_old" "$stale_n" "$debris_line" >>"$HIST"

emit "## The series so far"
emit ""
emit "A missing date is a morning this did not run — the Mac asleep silently drops"
emit "the calendar fire, it is not replayed on wake."
emit ""
emit '```'
column -t -s "$(printf '\t')" "$HIST" 2>/dev/null | tail -15 | tee -a "$OUT" \
  || tail -15 "$HIST" | tee -a "$OUT"
emit '```'
emit ""
emit "---"
emit "Latest detail: \`scheduler/lock_fix_verify.md\`. Series: \`scheduler/lock_fix_history.tsv\`."
exit 0

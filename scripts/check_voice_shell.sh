#!/bin/bash
# check_voice_shell.sh -- the CCL shell suite (scripts/test_voice_shell.cjs) as a
# gated daily job, so RED is seen the day it happens.
#
# WHY: the suite was red from at least 2026-08-12 to 2026-09-17 (23 inherited
# failures: manifest catch-up, one harness expectation, one wrong flag name)
# and nobody knew, because it cannot run in the task sandbox (it drives a real
# Chrome over CDP) and no scheduled job ran it. The 2026-09-03 audit had already
# found that 0 of 69 scheduled tasks run any test.
#
# SHAPE (feedback: the clock polls, the gate decides, the lock protects):
#   clock  -- launchd, daily 05:20 (com.c2a2.voice-shell-check). Cheap when idle.
#   gate   -- a STATE COMPARISON, never a stored flag: run only when some file the
#             suite exercises is newer than the last verdict, and none of them was
#             touched in the last QUIET_MIN minutes (a regen may be mid-write).
#   lock   -- an atomic mkdir; a second firing exits.
#
# WRITES (all gitignored):
#   scheduler/voice_shell.json   -- the verdict the health checker reads. `checked_at`
#                                   is stamped on EVERY fire (no-ops included) so the
#                                   freshness row measures liveness; `ran_at` and the
#                                   counts move only when the suite actually ran.
#   scheduler/voice_shell.md     -- one line per fire, same shape as commit_check.md
#   voice_shell.FAILED           -- repo-root marker, present exactly while the last
#                                   real run was RED (first line "[stamp] reason").
#   ~/Library/Logs/c2a2-voice-shell-check.log via the plist; the suite's own
#   output goes to /tmp/voice_shell_last.log (346 rows; not for the launchd log).
#
# VERDICT: GREEN/RED is decided against a DECLARED BASELINE (see PENDING_BASELINE
#       below), not against `failed == 0`. The suite reports some failures by
#       design; this wrapper interprets them. It never changes what the suite
#       reports, and a partial run (no `rows:` line) is never scored at all.
#
# EXIT: 0 green or no-op | 3 RED (a VERDICT, excused in check_scheduler_health.py's
#       VERDICT_EXITS) | 2 cannot run (no Chrome, no node, no harness) | 1 script error
#       (including: the harness died before its summary -- a broken check, not a verdict)
#
# Usage:  bash scripts/check_voice_shell.sh [--dry-run] [--force]
#   --dry-run  evaluate the gate, write nothing
#   --force    skip the gate (a human asking for a verdict now)
set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

# The two overrides exist for scripts/test_check_voice_shell.sh, which drives the
# RED / GREEN / died paths through a stub harness in a fixture repo. Production
# never sets them.
REPO="${VOICE_SHELL_REPO:-$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project}"
HARNESS="${VOICE_SHELL_HARNESS:-scripts/test_voice_shell.cjs}"
STATE="scheduler/voice_shell.json"
LINES="scheduler/voice_shell.md"
MARKER="voice_shell.FAILED"
SUITE_LOG="${VOICE_SHELL_LOG:-/tmp/voice_shell_last.log}"
LOCKDIR="${VOICE_SHELL_LOCK:-/tmp/check_voice_shell.lock}"
PORT=8087
QUIET_MIN=20
CHROME_BIN="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

# --- THE DECLARED BASELINE ---------------------------------------------------
# READ THIS BEFORE "TIDYING" ANY OF IT TO ZERO.
#
# The suite reports a set of failures BY DESIGN, and it is right to. Each one is
# a live record of a capability the system has not finished spreading. Rule 12:
# "completed" would be a lie if a skipped tab were silently omitted, so the
# harness records them as FAIL rather than hiding them. This wrapper is the one
# place that knows which of those failures are expected -- it changes how the
# result is INTERPRETED, never what the suite reports.
#
# PENDING_BASELINE -- how many FAIL rows carrying PENDING_MARK are expected at
#   the known-good state. It is a CAPABILITY ROSTER, NOT A DEFECT COUNT. The six
#   are tabs in the harness's FIND_TABS table that are required to implement the
#   c2a2Find / c2a2Clear / c2a2ReadCut contract and have not yet. The number must
#   FALL as tabs land the contract: lower it (never raise it) when one does.
#   Setting it to 0 today does not make the check stricter -- it only restores
#   the daily false alarm that this block exists to end.
#
# KNOWN_EXCEPTION -- the one page exception present at the known-good state,
#   matched BY TEXT rather than counted, so a DIFFERENT exception appearing is
#   RED even though the count did not move. Delete the line when it is fixed.
#   Set to the empty string to require a clean page.
#
# Why a declared baseline at all: from 2026-10 the wrapper scored RED whenever
# `failed` was non-zero, so it cried RED every morning at a state Tom had
# declared good. On 2026-11-06 a genuine seventh failure appeared
# ("interT_study.html built from its markdown", carrying no `pending`) and
# arrived looking identical to a week of false alarm. A daily false alarm is how
# a signal becomes background noise.
PENDING_MARK='pending'
PENDING_BASELINE=6
KNOWN_EXCEPTION="TypeError: Cannot read properties of undefined (reading 'toFixed')"

DRY=0; FORCE=0
for a in "$@"; do
  case "$a" in
    --dry-run) DRY=1 ;;
    --force)   FORCE=1 ;;
    *) echo "unknown arg: $a" >&2; exit 1 ;;
  esac
done

stamp() { date '+%F %T'; }
log()   { echo "$(stamp) $*"; }
line()  { [ "$DRY" = 1 ] && return 0; mkdir -p "$(dirname "$LINES")"; echo "$(stamp) $*" >> "$LINES"; }

cd "$REPO" || { echo "$(stamp) ERROR repo-not-found: $REPO"; exit 1; }

# --- lock ------------------------------------------------------------------
if [ "$DRY" = 0 ]; then
  if ! mkdir "$LOCKDIR" 2>/dev/null; then
    log "another check_voice_shell is running (lock $LOCKDIR); exiting"
    exit 0
  fi
  trap 'rmdir "$LOCKDIR" 2>/dev/null' EXIT
fi

# --- can it run at all? (exit 2, and say why) --------------------------------
if [ ! -f "$HARNESS" ]; then log "ERROR harness missing: $HARNESS"; line "ERROR harness missing"; exit 2; fi
if ! command -v node >/dev/null 2>&1; then log "ERROR node not on PATH"; line "ERROR node missing"; exit 2; fi
if [ ! -x "$CHROME_BIN" ]; then log "ERROR Chrome not found at: $CHROME_BIN"; line "ERROR chrome missing"; exit 2; fi

# --- gate: newest tested surface vs the last verdict -------------------------
# The list mirrors what the harness drives: the shell, its engine and manifests,
# the knowledge files, and every tab document (including the nested apps).
newest_f=""; newest_t=0
while IFS= read -r f; do
  t=$(stat -f %m "$f" 2>/dev/null || echo 0)
  if [ "$t" -gt "$newest_t" ]; then newest_t=$t; newest_f=$f; fi
done < <(
  ls -1 wiki/explorer.html wiki/lib/*.js wiki/voice_guide/*.json wiki/voice_guide/knowledge/*.md \
        wiki/*.html wiki/community/*.html wiki/community/*.js wiki/heartbeat/index.html wiki/heartbeat/app.js \
        wiki/metabolism/*.html wiki/commentary-explorer/*.html "$HARNESS" 2>/dev/null
)
now=$(date +%s)
last_run=0
if [ -f "$STATE" ]; then
  last_run=$(python3 -c 'import json,sys; print(int(json.load(open(sys.argv[1])).get("ran_at_epoch") or 0))' "$STATE" 2>/dev/null || echo 0)
fi
age_min=$(( (now - newest_t) / 60 ))
branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "?")
head=$(git rev-parse --short HEAD 2>/dev/null || echo "?")

# $1 ran (0/1)  $2 rows $3 passed $4 failed $5 exit $6 note $7 verdict $8 extra-json
# The verdict is PASSED IN, not inferred here from `failed == 0`. That inference
# was the bug: it could not tell a declared pending row from a regression.
write_state() {
  [ "$DRY" = 1 ] && return 0
  local ws_verdict="${7:-}" ws_extra="${8:-}"
  [ -n "$ws_extra" ] || ws_extra='{}'
  mkdir -p "$(dirname "$STATE")"
  python3 - "$STATE" "$1" "$2" "$3" "$4" "$5" "$6" "$ws_verdict" "$ws_extra" "$branch" "$head" "$newest_f" "$now" <<'PY'
import json, sys, os, datetime
p, ran, rows, passed, failed, code, note, verdict, extra, branch, head, newest, now = sys.argv[1:]
old = {}
if os.path.exists(p):
    try: old = json.load(open(p))
    except Exception: old = {}
iso = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
d = dict(old)
d["checked_at"] = iso
d["branch"] = branch; d["head"] = head; d["newest_source"] = newest; d["note"] = note
if ran == "1":
    d["ran_at"] = iso; d["ran_at_epoch"] = int(now)
    d["rows"] = int(rows); d["passed"] = int(passed); d["failed"] = int(failed); d["exit"] = int(code)
    d["verdict"] = verdict
    try: d.update(json.loads(extra or "{}"))
    except Exception: pass
json.dump(d, open(p, "w"), indent=2); open(p, "a").write("\n")
PY
}

if [ "$FORCE" = 0 ]; then
  if [ "$newest_t" -le "$last_run" ]; then
    log "no-op: nothing the suite covers is newer than the last verdict ($(date -r "$last_run" '+%F %T'))"
    write_state 0 0 0 0 0 "no-op: no source newer than last verdict"
    line "no-op (no source newer than last verdict; newest=$newest_f)"
    exit 0
  fi
  if [ "$age_min" -lt "$QUIET_MIN" ]; then
    log "deferring: $newest_f changed ${age_min}m ago (< ${QUIET_MIN}m quiet period); may be mid-write"
    write_state 0 0 0 0 0 "deferred: source in quiet period"
    line "deferred (quiet period; newest=$newest_f ${age_min}m ago)"
    exit 0
  fi
fi

if [ "$DRY" = 1 ]; then
  log "dry-run: WOULD run the suite (newest=$newest_f, ${age_min}m old; last verdict $( [ "$last_run" -gt 0 ] && date -r "$last_run" '+%F %T' || echo never ))"
  exit 0
fi

# --- run -----------------------------------------------------------------------
log "running $HARNESS on $branch@$head (newest source: $newest_f, ${age_min}m old)"
CHROME="$CHROME_BIN" node "$HARNESS" --port "$PORT" > "$SUITE_LOG" 2>&1
rc=$?
summary=$(grep -E '^rows: ' "$SUITE_LOG" | tail -1)
rows=$(echo "$summary" | sed -n 's/.*rows: *\([0-9]*\).*/\1/p');   rows=${rows:-0}
passed=$(echo "$summary" | sed -n 's/.*passed: *\([0-9]*\).*/\1/p'); passed=${passed:-0}
failed=$(echo "$summary" | sed -n 's/.*failed: *\([0-9]*\).*/\1/p'); failed=${failed:-0}
if [ -z "$summary" ]; then
  # The harness died before its summary line: that is not a verdict, it is a
  # broken check. Say so with the tail of its log, never a silent 0.
  log "ERROR harness produced no summary line (exit $rc); tail of $SUITE_LOG:"
  # 24, not 5: the harness now prints a PARTIAL block (rows that ran, last row
  # reached, page exceptions) ahead of its stack, and at 5 the launchd log saw
  # only the stack -- which is what made 2026-11-04 look like a run that never
  # started rather than one that died 130 rows in.
  tail -24 "$SUITE_LOG"
  # Scored against NOTHING: a partial run is not a result. It never reaches the
  # baseline comparison below, which is why the harness deliberately does not
  # print a `rows:` line on this path.
  write_state 1 0 0 0 "$rc" "harness produced no summary (exit $rc)" "DIED"
  line "ERROR harness died (exit $rc, no summary)"
  printf '[%s] voice-shell check could not complete: harness exit %s, no summary line; see %s\n' "$(stamp)" "$rc" "$SUITE_LOG" > "$MARKER"
  exit 1
fi

# --- verdict: the baseline, not a bare count --------------------------------
# Two independent questions, and the SECOND matters more than the first:
#   1. is the pending roster still at or under PENDING_BASELINE?
#   2. is EVERY failure one of the declared pending ones?
# A single failure without PENDING_MARK is a regression at ANY count -- six
# failures where one is unmarked is RED, because the roster shrank by one and a
# new defect took its slot. Reducing this to "failed <= 6" would pass that.
#
# Row names are split off their detail on the THREE-space ' -- ' that record()
# writes, not the first ' -- ': the pending rows carry a single-spaced ' -- '
# inside their own name ("X prs_3d -- pending: ...").
fail_names=$(grep -E '^  FAIL  ' "$SUITE_LOG" | sed -E 's/^  FAIL  //; s/   -- .*$//')
unmarked=$(printf '%s\n' "$fail_names" | grep -vF -- "$PENDING_MARK" | grep -c . | tr -d ' ')
pending_n=$(printf '%s\n' "$fail_names" | grep -cF -- "$PENDING_MARK" | tr -d ' ')
unmarked_list=$(printf '%s\n' "$fail_names" | grep -vF -- "$PENDING_MARK" | head -12 | paste -sd ';' -)

# Page exceptions and console errors are failures the suite reports OUTSIDE the
# row count (they are why the harness can exit 1 at `failed: 0`). They were
# folded into the old verdict only through $rc; now that $rc is no longer the
# gate they are asked for by name, and matched by TEXT so a swapped exception
# cannot hide behind an unchanged count.
all_exc=$(grep -E '^  EXCEPTION  ' "$SUITE_LOG" | sed -E 's/^  EXCEPTION  //')
if [ -n "$KNOWN_EXCEPTION" ]; then
  undeclared_exc=$(printf '%s\n' "$all_exc" | grep . | grep -vF -- "$KNOWN_EXCEPTION" | head -4 | paste -sd ';' -)
else
  undeclared_exc=$(printf '%s\n' "$all_exc" | grep . | head -4 | paste -sd ';' -)
fi
undeclared_cerr=$(grep -E '^  CONSOLE    ' "$SUITE_LOG" | sed -E 's/^  CONSOLE    //' | head -4 | paste -sd ';' -)

reasons=""
[ "$failed" -gt "$PENDING_BASELINE" ] && reasons="${reasons}failed $failed exceeds declared pending baseline $PENDING_BASELINE; "
[ "$unmarked" -gt 0 ] && reasons="${reasons}$unmarked failure(s) not marked '$PENDING_MARK' [$unmarked_list]; "
[ -n "$undeclared_exc" ] && reasons="${reasons}undeclared page exception [$undeclared_exc]; "
[ -n "$undeclared_cerr" ] && reasons="${reasons}console error(s) [$undeclared_cerr]; "

fails=$(printf '%s\n' "$fail_names" | grep . | sed -E 's/ +-- .*$//' | head -12 | paste -sd ';' -)
roster="pending $pending_n/$PENDING_BASELINE, unmarked $unmarked"
extra=$(printf '{"pending_failed": %s, "unmarked_failed": %s, "pending_baseline": %s}' \
         "$pending_n" "$unmarked" "$PENDING_BASELINE")

if [ -z "$reasons" ]; then
  write_state 1 "$rows" "$passed" "$failed" "$rc" "$summary ($roster)" "GREEN" "$extra"
  rm -f "$MARKER"
  # Say the roster out loud even when green: the six are still outstanding work,
  # and a GREEN that hides them is the other half of Rule 12.
  log "GREEN at declared baseline: $summary -- $roster${fails:+ -- $fails}"
  line "GREEN $summary ($branch@$head) -- $roster${fails:+ -- $fails}"
  exit 0
fi

write_state 1 "$rows" "$passed" "$failed" "$rc" "$summary ($roster)" "RED" "$extra"
log "RED: $summary (exit $rc) -- ${reasons%; } -- $fails"
line "RED $summary ($branch@$head) -- ${reasons%; } -- $fails"
{
  printf '[%s] voice-shell suite RED: %s (exit %s) on %s@%s\n' "$(stamp)" "$summary" "$rc" "$branch" "$head"
  printf 'why RED: %s\n' "${reasons%; }"
  printf 'declared baseline: %s pending rows marked %s%s\n' "$PENDING_BASELINE" "$PENDING_MARK" \
         "${KNOWN_EXCEPTION:+, plus the known exception: $KNOWN_EXCEPTION}"
  printf 'failed rows: %s\n' "$fails"
  printf 'full output: %s\n' "$SUITE_LOG"
} > "$MARKER"
exit 3

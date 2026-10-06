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
# EXIT: 0 green or no-op | 3 RED (a VERDICT, excused in check_scheduler_health.py's
#       VERDICT_EXITS) | 2 cannot run (no Chrome, no node, no harness) | 1 script error
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

write_state() {  # $1 = ran (0/1)  $2 rows $3 passed $4 failed $5 exit $6 note
  [ "$DRY" = 1 ] && return 0
  mkdir -p "$(dirname "$STATE")"
  python3 - "$STATE" "$1" "$2" "$3" "$4" "$5" "$6" "$branch" "$head" "$newest_f" "$now" <<'PY'
import json, sys, os, datetime
p, ran, rows, passed, failed, code, note, branch, head, newest, now = sys.argv[1:]
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
    d["verdict"] = "GREEN" if int(failed) == 0 and int(code) == 0 else "RED"
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
  tail -5 "$SUITE_LOG"
  write_state 1 0 0 0 "$rc" "harness produced no summary (exit $rc)"
  line "ERROR harness died (exit $rc, no summary)"
  printf '[%s] voice-shell check could not complete: harness exit %s, no summary line; see %s\n' "$(stamp)" "$rc" "$SUITE_LOG" > "$MARKER"
  exit 1
fi
write_state 1 "$rows" "$passed" "$failed" "$rc" "$summary"
fails=$(grep -E '^  FAIL ' "$SUITE_LOG" | sed -E 's/^  FAIL +//; s/ +-- .*$//' | head -12 | paste -sd ';' -)
if [ "$failed" = 0 ] && [ "$rc" = 0 ]; then
  rm -f "$MARKER"
  log "GREEN: $summary"
  line "GREEN $summary ($branch@$head)"
  exit 0
fi
log "RED: $summary (exit $rc) -- $fails"
line "RED $summary ($branch@$head) -- $fails"
{
  printf '[%s] voice-shell suite RED: %s (exit %s) on %s@%s\n' "$(stamp)" "$summary" "$rc" "$branch" "$head"
  printf 'failed rows: %s\n' "$fails"
  printf 'full output: %s\n' "$SUITE_LOG"
} > "$MARKER"
exit 3

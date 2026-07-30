#!/bin/bash
# openstory-watchdog.sh — liveness watchdog for the OpenStory backend.
#
# WHY THIS EXISTS (2026-07-20): launchd KeepAlive only restarts a process that
# EXITS. It is blind to the three failure modes we actually hit:
#   (a) alive but not serving (hung, or DB stalled) — KeepAlive never fires;
#   (b) crash-looping — launchd keeps respawning, so the service *looks* managed
#       while never once reaching a healthy state;
#   (c) a missing precondition (H-Drive unmounted → dangling symlinks) where
#       restarting is futile and just masks the real cause.
# The backend sat dead from 2026-07-06 to 07-20 because of (b)+(c), and nothing
# surfaced it. This pings the backend's own /health and restarts ONLY when a
# restart can actually help — otherwise it says why, loudly.
#
# 2026-07-29 — INGEST FRESHNESS IS NOW CHECKED HERE. This file used to say:
#
#     "Deliberately NOT checked here: ingest freshness. The OpenStory refresh
#      guard already owns that (REFRESH_STATUS.md). Do not duplicate."
#
# That stance is what failed. On 2026-07-27 the kqueue watcher hit EMFILE and
# stopped delivering events while the HTTP thread kept answering /health 200 —
# failure mode (a), the one this watchdog was written for, in the one shape it
# could not see. It reported "healthy" for 53h. The refresh guard did detect it,
# but it runs once a day and can only refuse to refresh feeds; it cannot restart.
# Detection without remediation, on a 24h period, is not a watchdog.
#
# The no-duplication instinct was right, so freshness is NOT reimplemented here:
# both this script and refresh_openstory_feeds.sh shell out to the SAME assertion,
# scripts/openstory_ingest_lag.py. One question, one answer, two callers.

set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"

LABEL="com.tomloughran.openstory.backend"
HEALTH="http://127.0.0.1:3002/health"
ARCHIVE="/Volumes/H-Drive/Claude-OpenStory-live/OpenStory-data-older-than-24h"
STATE="$HOME/Library/Application Support/openstory-watchdog"
LOG="$HOME/Library/Logs/openstory-watchdog.log"
FAILS="$STATE/consecutive_failures"
MAX_RESTARTS=3
# Seconds a freshly-started backend is left alone before it counts as unhealthy.
# Measured cold start (build + 72h backfill + archive reconcile) ran ~10 min.
STARTUP_GRACE=900
# Anchor for the grace window when no `open-story serve` process exists yet — see
# the grace gate below for why the process age alone is not enough.
KICKSTAMP="$STATE/last_kickstart"
# The shared ingest assertion (see header). Repo-relative to this script so the
# worktree and primary tree each use their own copy.
LAG_SCRIPT="$(cd "$(dirname "$0")" && pwd)/openstory_ingest_lag.py"
# Lag tolerated before ingest counts as stalled. Deliberately far above the
# script's own 1800s default: a restart re-runs a 72h backfill, so the bar for
# spending one must be high enough that only a real stall clears it.
MAX_LAG=${OPENSTORY_MAX_LAG:-5400}

mkdir -p "$STATE"

log()    { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG"; }
notify() { osascript -e "display notification \"$1\" with title \"OpenStory watchdog\"" 2>/dev/null || true; }
ping_ok(){ [ "$(curl -s -o /dev/null -m 5 -w '%{http_code}' "$HEALTH" 2>/dev/null)" = "200" ]; }

# Ingest progress. Exit 2 from the assertion means "cannot determine" — treated as
# NOT-stalled on purpose: a missing DB or an empty watch root is a different fault
# with a different remedy, and restarting the backend cannot fix either. It is
# logged so it can never pass silently (house Rule 12).
LAG_LINE=""
# Own baseline file, so an operator running openstory_ingest_lag.py by hand cannot
# reset the window this restart decision depends on. See the --state comment there.
LAG_STATE="$STATE/ingest_total_bytes.watchdog"
lag_ok() {
  LAG_LINE=$(python3 "$LAG_SCRIPT" --max-lag "$MAX_LAG" --state "$LAG_STATE" 2>&1)
  case $? in
    0) return 0 ;;
    1) return 1 ;;
    *) log "ingest lag UNDETERMINED (not treating as a stall): $LAG_LINE"; return 0 ;;
  esac
}

# ── Healthy = answering AND ingesting ───────────────────────────────────────
# Order matters: a backend that is not answering cannot be judged on lag, and the
# ping is the cheaper question. Only one reason is reported, the first that fires.
REASON=""
if ! ping_ok; then
  REASON="PING FAILED — no 200 from $HEALTH"
elif ! lag_ok; then
  REASON="INGEST STALLED — $LAG_LINE"
fi

if [ -z "$REASON" ]; then
  if [ -s "$FAILS" ] && [ "$(cat "$FAILS" 2>/dev/null || echo 0)" != "0" ]; then
    log "healthy again (clearing $(cat "$FAILS") consecutive failure(s))"
    notify "OpenStory backend is healthy again."
  fi
  echo 0 > "$FAILS"
  exit 0
fi

log "$REASON"

# ── Precondition gate: a restart cannot fix a missing archive volume ─────────
# This is the check that would have saved two weeks. Restarting into a dangling
# symlink just crash-loops; say the real reason instead.
if [ ! -d "$ARCHIVE" ]; then
  log "PRECONDITION MISSING: $ARCHIVE absent (H-Drive unmounted). NOT restarting."
  notify "H-Drive not mounted — OpenStory cannot start. Plug the drive in."
  exit 1
fi

# ── Startup grace: never kill a backend that is merely still booting ─────────
# A cold start does a cargo build, a 72h backfill, and (with H-Drive mounted) an
# archive reconcile — minutes, not seconds. Measured 2026-07-20: ~10 min before
# /health answered. Without this gate the watchdog would restart a perfectly
# healthy backend mid-boot, forever. Verification is deferred to the NEXT run
# rather than a blocking sleep, so this job always exits promptly.
#
# 2026-07-29: the process age alone was not enough. openstory-backend.sh runs
# `cargo build` BEFORE it execs the binary, so during the first ~minute of a cold
# start there is no `open-story serve` process to age — pgrep came back empty, the
# gate was skipped entirely, and the watchdog restarted a backend that was merely
# booting. Observed live at 15:18 on 2026-07-29: it killed a backfill that was
# recovering a 53h gap, and the 72h replay had to start over. So the grace window
# now anchors on whichever start signal is more recent — the running process, or
# the last kickstart THIS script issued.
AGE=999999
# `pgrep -x open-story`, NOT `pgrep -f 'open-story serve'`. The -f form matches any
# process whose FULL COMMAND LINE contains that string, which includes shells that
# merely mention it -- monitoring one-liners, other watchdogs, an operator's own
# `watch` loop. On 2026-07-29 that made this script pick up a long-lived helper
# shell instead of the backend, compute a large AGE from it, skip the startup-grace
# gate below, and restart a backend that was 200s into a boot. -x matches the
# executable name exactly, so only the real process can satisfy it.
PID=$(pgrep -x open-story | head -1)
if [ -n "$PID" ]; then
  A=$(ps -p "$PID" -o etimes= 2>/dev/null | tr -d ' ')
  case "$A" in ''|*[!0-9]*) A=999999 ;; esac
  [ "$A" -lt "$AGE" ] && AGE=$A
fi
if [ -f "$KICKSTAMP" ]; then
  S=$(cat "$KICKSTAMP" 2>/dev/null || echo 0)
  case "$S" in ''|*[!0-9]*) S=0 ;; esac
  if [ "$S" -gt 0 ]; then
    A=$(( $(date +%s) - S ))
    [ "$A" -ge 0 ] && [ "$A" -lt "$AGE" ] && AGE=$A
  fi
fi
if [ "$AGE" -lt "$STARTUP_GRACE" ]; then
  log "backend started ${AGE}s ago (< ${STARTUP_GRACE}s grace) — still booting/backfilling, not restarting"
  exit 0
fi

# ── Bounded restart, so a hard fault cannot become a restart storm ───────────
n=$(cat "$FAILS" 2>/dev/null || echo 0)
case "$n" in ''|*[!0-9]*) n=0 ;; esac
n=$((n + 1))
echo "$n" > "$FAILS"

if [ "$n" -gt "$MAX_RESTARTS" ]; then
  log "giving up: $n consecutive failures, exceeds MAX_RESTARTS=$MAX_RESTARTS"
  notify "OpenStory still down after $MAX_RESTARTS restarts. Manual fix needed."
  exit 1
fi

# ── Name fd exhaustion when that is what this is ─────────────────────────────
# 2026-07-29: a ~20-minute restart cycle showed up (fail, restart, healthy 5 min
# later, repeat ~3x/hour) and looked like a mystery hang. It is not. The kqueue
# watcher takes one fd per watched DIRECTORY, and config.toml's pi_watch_dir
# points at the Cowork store, which is 29231 directories -- against a hard
# kern.maxfilesperproc of 10240, so the tree can NEVER be fully registered. Once
# the process is fd-saturated, accept() on a new HTTP connection fails with
# EMFILE, /health goes unanswered, and this watchdog restarts a backend whose
# ingest is actually fine. The restart does restore service for a while, so we
# still perform it -- but a recurring symptom with a known structural cause must
# not read as an unexplained fault in the log. The real remedy is a bounded dir
# budget with LRU eviction in kqueue_watcher.rs (dirs are budgeted like files);
# raising RLIMIT_NOFILE cannot help, 10240 is the kernel's ceiling.
if [ -n "${PID:-}" ]; then
  FDS=$(lsof -p "$PID" 2>/dev/null | wc -l | tr -d ' ')
  # The BACKEND's ceiling, not this script's. `ulimit -n` here would report the
  # watchdog's own limit (256, straight from launchd) and make the threshold
  # meaningless, so read it from the one place it is actually set.
  SOFT=$(sed -n 's/^ulimit -n \([0-9]*\).*/\1/p' \
           "$(dirname "$0")/openstory-backend.sh" 2>/dev/null | head -1)
  case "${FDS:-}" in ''|*[!0-9]*) FDS=0 ;; esac
  case "${SOFT:-}" in ''|*[!0-9]*) SOFT=0 ;; esac
  if [ "$FDS" -gt 0 ] && [ "$SOFT" -gt 0 ] && [ "$FDS" -ge $(( SOFT * 9 / 10 )) ]; then
    log "FD EXHAUSTION (structural, not a hang): pid $PID holds $FDS fds. The watcher takes one fd per watched directory and pi_watch_dir is a 29k-dir tree vs a 10240 kernel cap, so accept() fails and /health cannot answer. Restarting restores service temporarily; the fix is a bounded dir budget in kqueue_watcher.rs."
    notify "OpenStory: fd exhaustion (pi_watch_dir tree exceeds the kernel fd cap). Restarting is palliative."
  fi
fi

log "restart attempt $n/$MAX_RESTARTS via launchctl kickstart (verify next run)"
# Stamp BEFORE kickstarting: the grace gate above reads this, and a restart that
# is issued but never stamped would let the next run restart it again mid-boot.
date +%s > "$KICKSTAMP"
launchctl kickstart -k "gui/$(id -u)/$LABEL" >> "$LOG" 2>&1
exit 0

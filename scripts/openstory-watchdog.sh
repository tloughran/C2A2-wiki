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
# Deliberately NOT checked here: ingest freshness. The OpenStory refresh guard
# already owns that (see wiki/agents/openstory/REFRESH_STATUS.md). Do not duplicate.

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

mkdir -p "$STATE"

log()    { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG"; }
notify() { osascript -e "display notification \"$1\" with title \"OpenStory watchdog\"" 2>/dev/null || true; }
ping_ok(){ [ "$(curl -s -o /dev/null -m 5 -w '%{http_code}' "$HEALTH" 2>/dev/null)" = "200" ]; }

# ── Healthy: clear any prior failure streak and go quiet ─────────────────────
if ping_ok; then
  if [ -s "$FAILS" ] && [ "$(cat "$FAILS" 2>/dev/null || echo 0)" != "0" ]; then
    log "healthy again (clearing $(cat "$FAILS") consecutive failure(s))"
    notify "OpenStory backend is healthy again."
  fi
  echo 0 > "$FAILS"
  exit 0
fi

log "PING FAILED — no 200 from $HEALTH"

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
PID=$(pgrep -f 'open-story serve' | head -1)
if [ -n "$PID" ]; then
  AGE=$(ps -p "$PID" -o etimes= 2>/dev/null | tr -d ' ')
  case "$AGE" in ''|*[!0-9]*) AGE=999999 ;; esac
  if [ "$AGE" -lt "$STARTUP_GRACE" ]; then
    log "process $PID is only ${AGE}s old (< ${STARTUP_GRACE}s grace) — still booting, not restarting"
    exit 0
  fi
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

log "restart attempt $n/$MAX_RESTARTS via launchctl kickstart (verify next run)"
launchctl kickstart -k "gui/$(id -u)/$LABEL" >> "$LOG" 2>&1
exit 0

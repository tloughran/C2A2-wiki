#!/bin/bash
# hdrive_keepalive.sh — keep H-Drive awake so it never idles off the bus.
#
# Why: pmset reports `disksleep 10`, so macOS spins idle disks down after ten
# minutes. Some external enclosures do not come back from that as a mount --
# they drop off the bus entirely, and the volume simply vanishes. OpenStory's
# backend then cannot start (its archive lives on H-Drive), the watchdog
# correctly refuses to restart into a dangling symlink, and ingest dies quietly.
# That happened 2026-07-06..07-20 and again 2026-08-15..08-24.
#
# A periodic small read keeps the enclosure from ever reaching its idle timeout.
# This is a preventative, NOT a repair: once the drive is off the bus only a
# replug brings it back, and this script says so rather than pretending.
#
# State changes are logged; steady state is silent, so the log stays readable.
set -uo pipefail

ARCHIVE="/Volumes/H-Drive/Claude-OpenStory-live/OpenStory-data-older-than-24h"
LOG="$HOME/Library/Logs/hdrive-keepalive.log"
STATE="$HOME/Library/Application Support/openstory-watchdog/hdrive_present"

mkdir -p "$(dirname "$LOG")" "$(dirname "$STATE")"
log() { printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >>"$LOG"; }

was="absent"
[ -f "$STATE" ] && was=$(cat "$STATE" 2>/dev/null || echo absent)

if [ -d "$ARCHIVE" ]; then
  # The touch that does the work: a cheap directory read resets the idle timer.
  ls -d "$ARCHIVE" >/dev/null 2>&1 || true
  now="present"
else
  now="absent"
fi

if [ "$now" != "$was" ]; then
  if [ "$now" = "present" ]; then
    log "H-Drive PRESENT again — keepalive resuming"
  else
    log "H-Drive VANISHED — keepalive cannot bring it back; replug required"
  fi
  printf '%s' "$now" >"$STATE"
fi

#!/bin/bash
# rotate_openstory_logs.sh — size-based rotation for the launchd-managed
# OpenStory logs in ~/Library/Logs.
#
# WHY THIS EXISTS (2026-08-01): openstory-backend-error.log reached 177.6 MB
# (931,532 lines) with no rotation of any kind. It is not an error spew — the
# Rust backend writes its normal per-session `broadcast`/`persist`/`patterns`
# tracing to stderr, so the file grows in proportion to how much work the
# system does (~13 MB/day measured 07-29 → 08-01). Nothing was ever going to
# stop it, and nothing reads past the tail.
#
# WHY COPY-TRUNCATE AND NOT RENAME-AND-RECREATE. launchd — not the program —
# opens StandardOutPath/StandardErrorPath, once, with O_APPEND, and holds that
# descriptor for the life of the job. There is no SIGHUP-reopen to ask for,
# because the writer does not own the file. Rename the log and launchd keeps
# writing into the RENAMED inode forever: the fresh file stays 0 bytes while
# the "archive" is the one still growing. So we copy the contents out, then
# truncate the SAME inode. O_APPEND is what makes the truncate safe — the next
# write lands at offset 0 instead of punching a 177 MB sparse hole at the old
# offset.
#
# The cost of copy-truncate is a race: anything written between the copy and
# the truncate is lost. At ~150 bytes/sec that is a line or two. Deliberate
# trade — a couple of lost lines beats an unbounded log.
#
# ORDER MATTERS AND IS ASSERTED: the archive is written AND verified before
# the live log is touched. If gzip fails, the log is left alone and the script
# exits non-zero. Truncating first would mean a failed archive = deleted logs.
#
# Usage:  bash scripts/rotate_openstory_logs.sh [--dry-run]
# Env overrides (used by the test, not in production):
#   LOG_DIR    directory to scan          (default $HOME/Library/Logs)
#   PATTERN    glob within LOG_DIR        (default openstory-*.log)
#   THRESHOLD  rotate at >= this many bytes (default 20971520 = 20 MB)
#   KEEP       gzipped generations to keep  (default 5)

set -uo pipefail
export PATH="/usr/bin:/bin:/usr/sbin:/sbin"

LOG_DIR="${LOG_DIR:-$HOME/Library/Logs}"
PATTERN="${PATTERN:-openstory-*.log}"
THRESHOLD="${THRESHOLD:-20971520}"
KEEP="${KEEP:-5}"
DRY=0
[ "${1:-}" = "--dry-run" ] && DRY=1

STAMP=$(date +%Y%m%d-%H%M%S)
rc=0
rotated=0

size_of(){ stat -f %z "$1" 2>/dev/null || echo 0; }

for log in "$LOG_DIR"/$PATTERN; do
  [ -f "$log" ] || continue
  sz=$(size_of "$log")
  if [ "$sz" -lt "$THRESHOLD" ]; then
    echo "skip    $(basename "$log") ($sz bytes < $THRESHOLD)"
    continue
  fi

  if [ "$DRY" = 1 ]; then
    echo "WOULD   $(basename "$log") ($sz bytes)"
    rotated=$((rotated+1))
    continue
  fi

  arc="$log.$STAMP.gz"
  tmp="$arc.partial"

  if ! gzip -c "$log" > "$tmp" 2>/dev/null; then
    echo "FAIL    $(basename "$log"): gzip failed; log left intact" >&2
    rm -f "$tmp"; rc=1; continue
  fi
  # Verify the archive is readable BEFORE destroying the source. An archive
  # nobody has decompressed is not a backup.
  if ! gzip -t "$tmp" 2>/dev/null || [ "$(size_of "$tmp")" -eq 0 ]; then
    echo "FAIL    $(basename "$log"): archive did not verify; log left intact" >&2
    rm -f "$tmp"; rc=1; continue
  fi
  mv "$tmp" "$arc"

  : > "$log"
  after=$(size_of "$log")
  if [ "$after" -ge "$THRESHOLD" ]; then
    echo "FAIL    $(basename "$log"): truncate did not shrink it ($after bytes)" >&2
    rc=1; continue
  fi

  echo "rotated $(basename "$log")  $sz -> $after bytes, archive $(size_of "$arc") bytes"
  rotated=$((rotated+1))

  # Prune. The stamp is YYYYmmdd-HHMMSS, so lexical order IS chronological.
  n=$(ls -1 "$log".*.gz 2>/dev/null | wc -l | tr -d ' ')
  if [ "$n" -gt "$KEEP" ]; then
    ls -1 "$log".*.gz | sort | head -n $((n - KEEP)) | while read -r old; do
      rm -f "$old" && echo "pruned  $(basename "$old")"
    done
  fi
done

echo "rotate_openstory_logs: $rotated rotated, rc=$rc"
exit $rc

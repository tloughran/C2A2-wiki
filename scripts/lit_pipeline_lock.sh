#!/bin/bash
#
# lit_pipeline_lock.sh -- exclusive-writer lock for c2a2-lit-search-pipeline.
#
# WHY THIS EXISTS
# ---------------
# Before this script there was NO LOCK. `wiki/review/lit_pipeline.lock` is a
# plain text file holding the word LOCKED or RELEASED, written and read by the
# pipeline agent purely by convention -- a convention carried forward in prose
# from one run note to the next, never in the task spec. for_lit_search.md says
# so in as many words on 2026-10-03: "This check was done because the 10-02
# notes describe it, NOT because the task spec requires it."
#
# So a concurrent copy did not "ignore" the lock. Nothing told it to look, and
# even a copy that did look would have been doing read-then-write on a free-text
# status word: a check-then-act race with no atomic step anywhere in it.
#
# That is why 2026-10-15 cost data. One instance wrote LOCKED at 04:34:38Z; a
# second committed at 04:38:13Z and overwrote all four of the first instance's
# 15a/15b result files (8-9 KB of abstract- and full-text reads replaced by 2-3
# KB of title-level reads). The first instance then withdrew its own register
# appends to avoid duplicating the second's. Same shape on 2026-10-01.
#
# WHAT CHANGED
# ------------
# Acquisition is now ONE atomic filesystem operation -- `mkdir` of a directory
# that either exists or does not. There is no window between the test and the
# create, because there is no test. This follows publish_prs_connectome.sh's
# Gate 0, which has held the same property since it was written; macOS has no
# usable flock(1), so mkdir is the idiom here.
#
# The lock lives in the VAULT, not in /tmp, deliberately. The two copies of this
# task do not share a machine: one fires from the local registry on the Mac and
# one from a cloud routine that reaches the Mac through its mounted folders. A
# /tmp lock would be per-host and would serialize nothing. The vault path is the
# only surface both writers demonstrably touch.
#
# `wiki/review/lit_pipeline.lock` is KEPT, unchanged in format, as the audit
# trail the run notes already cite. It is no longer what grants the lock.
#
# STALE BREAKING
# --------------
# A held lock older than LIT_PIPELINE_LOCK_STALE_HOURS (6h, about four times the
# longest observed run) is broken, because an agent that dies mid-run cannot
# release and a permanently wedged lock would silently stop the pipeline -- the
# ~17h HEAD.lock stall in a new coat. The break is LOUD: it goes to stderr, it is
# appended to the audit file as STALE-BREAK with the dead owner's identity, and
# it is the only path here that writes that word. Breaking is itself
# single-winner (a break token, same mkdir idiom), so two copies arriving at a
# stale lock together cannot both proceed.
#
# USAGE
#   scripts/lit_pipeline_lock.sh acquire --run-id <id>
#   scripts/lit_pipeline_lock.sh release --run-id <id> [--note "text"]
#   scripts/lit_pipeline_lock.sh status
#
# EXIT CODES -- the caller MUST branch on these:
#   0  acquire: this run owns the lock, proceed.  release: released.  status: free.
#   3  HELD by a live owner. The caller must WRITE NOTHING and exit cleanly.
#      status also returns 3 when held.
#   1  usage error, or the lock directory could not be created at all.
#
set -uo pipefail

REPO="${LIT_PIPELINE_REPO:-/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project}"
LOCKDIR="${LIT_PIPELINE_LOCK_DIR:-$REPO/wiki/review/lit_pipeline.lock.d}"
AUDIT="${LIT_PIPELINE_LOCK_AUDIT:-$REPO/wiki/review/lit_pipeline.lock}"
STALE_HOURS="${LIT_PIPELINE_LOCK_STALE_HOURS:-6}"

OWNER="$LOCKDIR/owner"
BREAKDIR="$LOCKDIR.break"

ts()  { date -u "+%Y-%m-%dT%H:%M:%SZ"; }
now() { date -u "+%s"; }

# Append-only. The audit file is evidence about who ran; truncating it would
# destroy exactly the record that made the 10-15 conflict reconstructable.
audit() { printf '%s\n' "$1" >> "$AUDIT"; }

usage() {
  echo "usage: $(basename "$0") acquire|release|status [--run-id ID] [--note TEXT]" >&2
  exit 1
}

ACTION="${1:-}"; shift || true
RUN_ID=""; NOTE=""
while [ $# -gt 0 ]; do
  case "$1" in
    --run-id) RUN_ID="${2:-}"; shift 2 || usage ;;
    --note)   NOTE="${2:-}";   shift 2 || usage ;;
    *) usage ;;
  esac
done

# Who holds it: "<epoch> <iso> <run-id> <host> <pid>", or "" if unreadable.
read_owner() { [ -f "$OWNER" ] && head -1 "$OWNER" || true; }

owner_epoch() {
  local line; line="$(read_owner)"
  case "$line" in
    [0-9]*) echo "${line%% *}" ;;
    # No parseable stamp (a half-written owner file, or one from an older
    # version). Fall back to the directory's own mtime rather than treating the
    # lock as ageless, which would wedge the pipeline forever.
    *) stat -f %m "$LOCKDIR" 2>/dev/null || echo 0 ;;
  esac
}

write_owner() {
  printf '%s %s %s %s %s\n' "$(now)" "$(ts)" "${RUN_ID:-unidentified}" \
    "$(hostname -s 2>/dev/null || echo unknown-host)" "$$" > "$OWNER"
}

case "$ACTION" in

  status)
    if [ -d "$LOCKDIR" ]; then
      echo "HELD: $(read_owner)"
      exit 3
    fi
    echo "FREE"
    exit 0
    ;;

  acquire)
    mkdir -p "$(dirname "$LOCKDIR")" 2>/dev/null

    # THE atomic step. Succeeds for exactly one caller.
    if mkdir "$LOCKDIR" 2>/dev/null; then
      write_owner
      audit "LOCKED $(ts) by ${RUN_ID:-unidentified} (host $(hostname -s 2>/dev/null || echo unknown-host), pid $$)"
      echo "ACQUIRED ${RUN_ID:-unidentified}"
      exit 0
    fi

    if [ ! -d "$LOCKDIR" ]; then
      echo "FAIL: cannot create lock at $LOCKDIR and it does not exist. Refusing to run unlocked." >&2
      exit 1
    fi

    held="$(read_owner)"
    age=$(( $(now) - $(owner_epoch) ))
    limit=$(( STALE_HOURS * 3600 ))

    if [ "$age" -lt "$limit" ]; then
      audit "SKIPPED $(ts) by ${RUN_ID:-unidentified}: lock held by [$held], ${age}s old. Wrote nothing."
      echo "HELD by [$held] (${age}s old, under ${STALE_HOURS}h). Exiting without writing." >&2
      exit 3
    fi

    # Stale. Break it, loudly, and only once.
    if ! mkdir "$BREAKDIR" 2>/dev/null; then
      audit "SKIPPED $(ts) by ${RUN_ID:-unidentified}: another run is breaking the stale lock. Wrote nothing."
      echo "HELD: another run is already breaking the stale lock. Exiting without writing." >&2
      exit 3
    fi
    audit "STALE-BREAK $(ts) by ${RUN_ID:-unidentified}: previous owner [$held] held the lock ${age}s (> ${STALE_HOURS}h) and never released. Assuming it died; taking the lock."
    echo "STALE-BREAK: previous owner [$held] held $LOCKDIR for ${age}s (> ${STALE_HOURS}h). Taking it. INVESTIGATE why that run never released." >&2
    write_owner
    rmdir "$BREAKDIR" 2>/dev/null
    echo "ACQUIRED ${RUN_ID:-unidentified} (after stale break)"
    exit 0
    ;;

  release)
    if [ ! -d "$LOCKDIR" ]; then
      audit "RELEASE-NOOP $(ts) by ${RUN_ID:-unidentified}: lock was already gone.${NOTE:+ $NOTE}"
      echo "RELEASE-NOOP: no lock at $LOCKDIR" >&2
      exit 0
    fi
    held="$(read_owner)"
    rm -f "$OWNER"
    rmdir "$LOCKDIR" 2>/dev/null
    audit "RELEASED $(ts) by ${RUN_ID:-unidentified} (was [$held]).${NOTE:+ $NOTE}"
    echo "RELEASED ${RUN_ID:-unidentified}"
    exit 0
    ;;

  *) usage ;;
esac

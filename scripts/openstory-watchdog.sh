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
# One ping is not evidence. A single 5s timeout buys a 4m15s cold boot (measured
# 2026-07-29), so the cheap question gets asked three times over ~20s before it is
# allowed to cost that. Observed 2026-07-29/30: four restarts between 23:03 and
# 00:05 each followed ONE failed ping on a backend that was serving in ~2ms
# milliseconds later and ingesting the whole time.
ping_once(){ [ "$(curl -s -o /dev/null -m 5 -w '%{http_code}' "$HEALTH" 2>/dev/null)" = "200" ]; }
ping_ok(){
  local i
  for i in 1 2 3; do
    ping_once && return 0
    [ "$i" -lt 3 ] && sleep 4
  done
  return 1
}

# Ingest progress. Exit 2 from the assertion means "cannot determine" — treated as
# NOT-stalled on purpose: a missing DB or an empty watch root is a different fault
# with a different remedy, and restarting the backend cannot fix either. It is
# logged so it can never pass silently (house Rule 12).
LAG_LINE=""
# Own baseline file, so an operator running openstory_ingest_lag.py by hand cannot
# reset the window this restart decision depends on. See the --state comment there.
LAG_STATE="$STATE/ingest_total_bytes.watchdog"
# Frontier progress across runs, for the veto below. Read straight from the store
# rather than through the lag script: the question here is not "is the frontier
# close to wall clock" (that is lag_ok's question) but the strictly weaker "did it
# move since last run", which is true even when the backend is minutes behind and
# catching up -- exactly the state a restart destroys.
OS_DB="$HOME/Documents/Non-Claude Projects/OpenStory/data/open-story.db"
FRONTIER_STATE="$STATE/last_frontier"
VETOES="$STATE/progress_vetoes"
# After this many consecutive vetoes (~5 min apart) restart anyway. Without a bound
# a permanently dead HTTP thread on a live ingest would never be restarted, which
# is the opposite failure and just as silent.
MAX_VETOES=3
# The leash above is correct for the case it was written for -- port dead, ingest
# fine -- because a permanently broken SERVING path must eventually be restarted.
# It is the wrong leash when the port is HEALTHY and only the store looks still.
# There the process is answering, working, and holding an uncommitted transaction,
# and a restart does not just cost the 4m15s boot: it discards that transaction and
# (with pi_watch_dir set) buys a boot measured at 8h46m. Restarting is far more
# destructive than waiting, so waiting gets a much longer leash. Still bounded --
# a store that never commits IS eventually a fault, it is just not a 15-minute one.
MAX_STORE_VETOES=36        # ~3h at the 5-minute cadence
# ── Boot phase ──────────────────────────────────────────────────────────────
# WHY (2026-07-30): pid 64213 exec'd at 03:01:17, printed "Serving on:" ~4 min
# later, then emitted NOTHING for 8h46m before /health finally answered at
# 11:54. STARTUP_GRACE=900 is off by a factor of 35 against a 31800s boot, so
# every guard below treated a legitimate boot as a dead backend: 3 restarts,
# then 105 "giving up ... Manual fix needed" notifications while the process was
# working the whole time. The trigger was ours -- pi_watch_dir was restored at
# 00:10 to a 29458-dir / 40186-file tree, and the startup scan over it is not
# bounded the way the kqueue dir budget bounds watches.
#
# The fix is NOT a bigger constant; 900 -> 36000 would just be a new number to
# be wrong about. This file already holds the right principle -- believe
# progress over a silent port -- and applies it only to ingest. A booting
# process has no frontier to advance, so the same principle needs a different
# witness: CPU time. A process that has never answered since exec is BOOTING,
# and it keeps its grace for as long as it is demonstrably still working.
# Bounded the same way the ingest veto is: CPU flat across MAX_BOOT_STALLS runs
# means wedged, not booting, and that still restarts.
HEALTHY_PID="$STATE/healthy_pid"   # pid last seen answering /health
BOOT_CPU="$STATE/boot_cpu"         # "pid|cpu_seconds" from the previous run
BOOT_STALLS="$STATE/boot_stalls"   # consecutive runs with CPU flat while booting
MAX_BOOT_STALLS=3
# ps reports etime as [[DD-]HH:]MM:SS but time as [[DD-]HH:]MM:SS.FF -- the CPU
# form carries HUNDREDTHS and the elapsed form does not. Measured on the live
# backend 2026-07-30: etime "09:22:31", time " 82:16.43". An early version of
# this parser rejected the fraction and returned the 999999 sentinel, which is
# CONSTANT, which reads as flat CPU, which would have restarted a healthy boot
# after three checks -- the precise failure the boot gate exists to prevent.
# The fraction is dropped rather than parsed: sub-second CPU is noise here, and
# the only question asked of this number is "did it go up".
# Parsed, never assumed: the 2026-07-30 etimes/etime bug got here by trusting a
# shape, and this is now read twice, so it is read in exactly one place.
ps_time_secs(){
  awk -v t="$1" 'BEGIN{
        gsub(/ /, "", t);
        sub(/\.[0-9]+$/, "", t);
        n=split(t, p, /[-:]/); s=0;
        if (n==0) { print 999999; exit }
        # seconds, minutes, hours, days from the right
        mult[1]=1; mult[2]=60; mult[3]=3600; mult[4]=86400;
        for (i=0; i<n; i++) {
          v=p[n-i]+0;
          if (p[n-i] !~ /^[0-9]+$/) { print 999999; exit }
          s += v*mult[i+1];
        }
        print s
      }'
}
# Two signals, not one. MAX(last_event) only moves when an event NEWER than every
# event already stored lands, so it can sit still for a minute at a time while the
# backend is ingesting perfectly well -- observed doing exactly that on 2026-07-30,
# which made an early version of the veto below restart on every other check. The
# event COUNT moves on any ingested event, so the pair is far harder to fool than
# either alone.
# The witness is the COMMITTED pair, and deliberately nothing else.
#
# An earlier version of this function (2026-07-30 ~12:50) also mixed in the -wal
# file's size and mtime, on the theory that the frozen frontier was one long
# uncommitted transaction and a moving wal meant "mid-transaction progress".
# BOTH HALVES OF THAT THEORY WERE WRONG, and the same day proved it:
#
#   - The freeze was not a long transaction. It was lock contention: a read
#     consumer (admin_broadcaster) full-scanned every session on every broadcast
#     and held the store's single shared connection. Fixed upstream in the
#     OpenStory repo; boot went 8h46m -> 5m55s.
#   - A moving -wal does NOT imply ingest progress. Measured at 13:13, eleven
#     minutes into a boot that had not yet committed its first event: events
#     pinned at 768692 and frontier pinned at 16:07:52Z (the backend's own
#     /api/sessions agreeing), while the db file still grew 53 MB and the wal
#     mtime still advanced -- because the backend was writing PATTERNS (588799
#     rows) and FTS for events it already had. A wal-mtime witness would have
#     called that "the store is moving". It would have been reporting pattern
#     churn, not ingest, and it cannot tell the two apart. (Ingest did start at
#     t+689s and cleared an hour of backlog in ~90s, so that particular window
#     was a slow start rather than a fault -- but the witness would have said
#     "progressing" either way, which is exactly why it is worthless here.)
#
# Also note a constant wal SIZE is not evidence of a stall either: SQLite resets
# a wal on checkpoint but leaves the file at its high-water mark, so a steady size
# with a moving mtime is ordinary healthy operation. There is no cheap signal in
# that file that means "ingest advanced". The committed pair is the only honest
# one, and now that a boot costs ~6 minutes rather than nine hours, being wrong in
# the restart direction is cheap again.
frontier_now(){ sqlite3 "file:$OS_DB?mode=ro" \
  "SELECT COALESCE(MAX(last_event),'')||'|'||(SELECT COUNT(*) FROM events) FROM sessions;" \
  2>/dev/null | tr -d ' '; }
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
SERVING=0        # did the port answer this run? decides the veto leash below
if ! ping_ok; then
  REASON="PING FAILED — no 200 from $HEALTH"
else
  SERVING=1
  lag_ok || REASON="INGEST STALLED — $LAG_LINE"
fi

if [ -z "$REASON" ]; then
  if [ -s "$FAILS" ] && [ "$(cat "$FAILS" 2>/dev/null || echo 0)" != "0" ]; then
    log "healthy again (clearing $(cat "$FAILS") consecutive failure(s))"
    notify "OpenStory backend is healthy again."
  fi
  echo 0 > "$FAILS"
  echo 0 > "$VETOES"
  echo 0 > "$BOOT_STALLS"
  # THIS is what makes "has it ever answered since exec" answerable. Recorded
  # only here, where a 200 was actually observed, so the boot gate below can
  # never mistake a process that has served for one that has not.
  P=$(pgrep -x open-story | head -1); [ -n "$P" ] && echo "$P" > "$HEALTHY_PID"
  # Keep the frontier baseline current while healthy, so the veto's first look
  # after a failure compares against ~5 minutes ago rather than against whenever
  # the last failure happened to be.
  F=$(frontier_now); [ -n "$F" ] && echo "$F" > "$FRONTIER_STATE"
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
  # `etime`, NOT `etimes`. BSD/macOS ps has no `etimes` keyword -- it fails with
  # "ps: etimes: keyword not found" and prints the keyword list to stderr, so the
  # numeric guard below saw non-numeric text and fell through to AGE=999999. That
  # meant the PROCESS half of this gate never once worked on this machine: only the
  # KICKSTAMP half below did, which is why the gate holds after a restart this
  # script issued and not after one launchd KeepAlive or an operator issued.
  # Verified 2026-07-30 by running both forms against the live pid.
  # etime is [[DD-]HH:]MM:SS, so parse it rather than assuming a shape.
  A=$(ps_time_secs "$(ps -p "$PID" -o etime= 2>/dev/null)")
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

# ── Boot gate: a process that has never answered is booting, not hung ────────
# See the MAX_BOOT_STALLS block at the top for the 8h46m boot this exists for.
# Deliberately placed BEFORE the ingest veto: a booting backend has not opened
# the store for writing yet, so its frontier cannot move, and the veto would
# read that stillness as "a restart is justified" -- the exact wrong call.
if [ -n "${PID:-}" ]; then
  SERVED=$(cat "$HEALTHY_PID" 2>/dev/null || echo "")
  if [ "$PID" != "$SERVED" ]; then
    # This pid has never been observed answering /health. It is booting.
    CPU_NOW=$(ps_time_secs "$(ps -p "$PID" -o time= 2>/dev/null)")
    case "$CPU_NOW" in ''|*[!0-9]*) CPU_NOW=0 ;; esac
    CPU_PREV=""
    if [ -f "$BOOT_CPU" ]; then
      IFS='|' read -r BP BC < "$BOOT_CPU" 2>/dev/null || true
      [ "${BP:-}" = "$PID" ] && CPU_PREV="${BC:-}"
    fi
    echo "$PID|$CPU_NOW" > "$BOOT_CPU"
    bs=$(cat "$BOOT_STALLS" 2>/dev/null || echo 0)
    case "$bs" in ''|*[!0-9]*) bs=0 ;; esac
    if [ -z "$CPU_PREV" ] || [ "$CPU_NOW" -gt "$CPU_PREV" ]; then
      # Still burning CPU => still doing boot work. Reset the stall counter:
      # unlike the ingest veto (where a quiet interval is not evidence the
      # episode ended), CPU that moves is direct evidence THIS process is alive
      # and working right now, so it earns a clean slate.
      echo 0 > "$BOOT_STALLS"
      log "BOOTING, not restarting ($REASON) — pid $PID has never answered /health since exec ${AGE}s ago and is still working (cpu ${CPU_PREV:-n/a}s -> ${CPU_NOW}s). Observed 2026-07-30: a boot over pi_watch_dir took 8h46m."
      exit 0
    fi
    bs=$((bs + 1))
    echo "$bs" > "$BOOT_STALLS"
    if [ "$bs" -lt "$MAX_BOOT_STALLS" ]; then
      log "BOOTING but CPU is flat ($CPU_NOW s) — pid $PID has never answered and did no work this interval. Stall $bs/$MAX_BOOT_STALLS before it counts as wedged."
      exit 0
    fi
    log "boot is WEDGED, not slow: pid $PID has never answered /health and burned no CPU across $bs consecutive checks (~$((bs * 5)) min). Restarting."
    notify "OpenStory: boot wedged (no CPU, never served). Restarting."
  fi
fi

# ── Progress veto: never restart a backend that is demonstrably ingesting ────
# WHY (2026-07-30): between 23:03 and 00:05 this script restarted the backend four
# times. Each restart followed a single failed ping on a process that was answering
# /health in ~2ms moments later and was ingesting throughout -- measured mid-cycle
# at ~11x realtime, closing a 62-minute backlog. Every restart threw away a boot
# that costs 4m15s (reconcile ~165s + reproject + 72h backfill), so the frontier
# could never actually catch up. The watchdog was the outage.
#
# The header already says liveness is not progress. The converse is the missing
# half: an unanswered HTTP port is not death either, and progress is the stronger
# signal of the two. When they disagree, believe progress and say so.
#
# Bounded, because a permanently hung HTTP thread over a healthy ingest must still
# be restarted eventually -- it just must not be restarted on the first flap.
FRONT_NOW=$(frontier_now)
FRONT_PREV=""
[ -f "$FRONTIER_STATE" ] && FRONT_PREV=$(cat "$FRONTIER_STATE" 2>/dev/null)
[ -n "$FRONT_NOW" ] && echo "$FRONT_NOW" > "$FRONTIER_STATE"
v=$(cat "$VETOES" 2>/dev/null || echo 0)
case "$v" in ''|*[!0-9]*) v=0 ;; esac
# A healthy port makes waiting cheap and restarting expensive, so it buys the long
# leash. A dead port keeps the original short one.
if [ "$SERVING" = "1" ]; then LEASH=$MAX_STORE_VETOES; else LEASH=$MAX_VETOES; fi
if [ -n "$FRONT_NOW" ] && [ -n "$FRONT_PREV" ] && [ "$FRONT_NOW" != "$FRONT_PREV" ]; then
  v=$((v + 1))
  echo "$v" > "$VETOES"
  if [ "$v" -le "$LEASH" ]; then
    log "NOT RESTARTING ($REASON) — the store IS moving: $FRONT_PREV -> $FRONT_NOW (frontier|events|wal). A restart discards any uncommitted transaction and buys a boot measured at up to 8h46m. Veto $v/$LEASH."
    exit 0
  fi
  if [ "$SERVING" = "1" ]; then
    log "restarting DESPITE progress: $v consecutive vetoes exceeds MAX_STORE_VETOES=$MAX_STORE_VETOES (~$((v * 5)) min). The port answers and the store keeps moving ($FRONT_PREV -> $FRONT_NOW) but the ingest frontier has not caught up in that time, so this is no longer a long transaction."
    notify "OpenStory: store moving but frontier stuck ${v} checks. Restarting."
  else
    log "restarting DESPITE progress: $v consecutive vetoes exceeds MAX_VETOES=$MAX_VETOES. Ingest advances ($FRONT_PREV -> $FRONT_NOW) but HTTP has stayed unanswered across ~$((v * 5)) minutes, so the serving path is separately broken."
    notify "OpenStory: ingest fine, HTTP dead ${v} checks running. Restarting."
  fi
else
  # Deliberately NOT clearing the veto counter here. It counts how long this
  # episode has been "unanswered but alive", and a single no-progress interval is
  # not evidence the episode ended -- ingest is bursty. Clearing it here let an
  # alternating progress / no-progress sequence restart on every other check while
  # never reaching MAX_VETOES, which is the exact bug this line used to have.
  # The counter is cleared in the healthy branch above, where it is earned.
  log "no ingest progress since last check ($FRONT_PREV -> $FRONT_NOW, frontier|events) — a restart is justified"
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

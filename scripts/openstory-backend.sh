#!/usr/bin/env bash
# openstory-backend.sh — OpenStory capture backend, supervised by launchd
# (com.tomloughran.openstory.backend, RunAtLoad + KeepAlive).
#
# Waits for local-only NATS (its own agent, com.tomloughran.openstory.nats), then
# runs the Rust `serve` backend IN THE FOREGROUND via exec, so this process IS what
# launchd watches — if the backend dies, launchd restarts it. This is the durable feed
# that writes open-story.db (which the C2A2 wiki reads). 2026-06-25.
set -euo pipefail
export PATH="/opt/homebrew/bin:$HOME/.cargo/bin:$PATH"

# 0) File-descriptor ceiling. The macOS kqueue watcher (rs/src/kqueue_watcher.rs)
#    holds one fd per watched DIRECTORY and budgets only its *file* watches, on the
#    documented assumption that "dirs are few". The bridge falsifies that: it gives
#    every Cowork per-run sandbox its own top-level project dir (2787 dirs on
#    2026-07-29). Under launchd the soft RLIMIT_NOFILE is 256, so on 2026-07-27 the
#    watcher hit EMFILE partway through registration, stopped delivering events, and
#    left the HTTP thread answering /health 200 — a 53h silent ingest stall that the
#    liveness-only watchdog could not see. 8192 is well under kern.maxfilesperproc
#    (10240). Set HERE, not in the plist, so manual runs and `launchctl kickstart`
#    inherit it too. This raises the ceiling; bounding the watch tree is the real
#    fix and belongs in openstory-bridge.sh.
ulimit -n 8192 || { echo "[backend] FATAL: could not raise RLIMIT_NOFILE" >&2; exit 1; }
echo "[backend] fd limit: $(ulimit -n)"

# 0b) Capture WHY the process exits. 2026-07-29: after the fd ceiling was raised
#     the backend began exiting on its own every few minutes, with launchd
#     KeepAlive respawning it -- at only ~318 fds, with no crash report in
#     ~/Library/Logs/DiagnosticReports, no OOM (RSS ~537MB), and no graceful
#     "Shutting down" line before the death. Diagnosing that from logs alone
#     failed twice, so make the process report itself instead of guessing again.
#     Pure instrumentation: affects output only, never behaviour.
export RUST_BACKTRACE=1
echo "[backend] RUST_BACKTRACE=1 (diagnosing unexplained self-exits)"

OS_ROOT="$HOME/Documents/Non-Claude Projects/OpenStory"
cd "$OS_ROOT"

# 1) Local NATS JetStream on :4222 is supervised SEPARATELY, by
#    com.tomloughran.openstory.nats (RunAtLoad + KeepAlive). This script no longer
#    starts it, only waits for it.
#
#    Why it moved out, 2026-07-29: nats-server was started here and `disown`ed.
#    disown removes the job from this shell's table but does NOT detach the process
#    group, so launchd stopping the backend took NATS down with it — confirmed by
#    ancestry, nats-server's PPID was the backend's own pid. Every respawn therefore
#    raced a cold NATS, and the backend bails out of main() when it cannot reach
#    JetStream at startup (rs/cli/src/main.rs:680, "NATS unavailable" / "NATS stream
#    setup failed"). That is a clean non-zero exit, so KeepAlive relaunched this
#    script and rolled the same dice again — a restart loop with no crash report and
#    no "Shutting down" line, which is exactly how it presented.
#
#    A readiness probe inside this script cannot close that race, which is why the
#    first attempt at fixing it did not: the probe runs in the very process that NATS
#    is about to be a child of. It proves NATS was listening a moment ago, not that
#    it will outlive the exec below.
#
#    The race was expensive because a boot is not cheap: reconcile (~150-190s, and it
#    adds 0 events — it skips ~724k), reproject (~669k events), then the 72h backfill
#    (~23k events, the small part). About 4m15s before the HTTP listener answers, so
#    /health returning nothing during that window is normal, not a fault. An exit at
#    3 minutes discards the whole boot; a few in a row froze the ingest frontier for
#    an hour. Measured 2026-07-29.
#
#    NATS now outlives any backend restart, and if NATS itself dies its own KeepAlive
#    brings it back. The wait below still matters at login, when both jobs start at
#    once and this one can win.
echo "[backend] waiting for NATS on :4222 ..."
for _ in $(seq 1 60); do
  if nc -z -G 1 127.0.0.1 4222 >/dev/null 2>&1; then
    echo "[backend] NATS accepting connections"
    break
  fi
  sleep 0.5
done
if ! nc -z -G 1 127.0.0.1 4222 >/dev/null 2>&1; then
  echo "[backend] FATAL: NATS never came up on :4222 after 30s. It has its own agent:" >&2
  echo "[backend]   launchctl print gui/\$(id -u)/com.tomloughran.openstory.nats" >&2
  echo "[backend]   tail ~/Library/Logs/openstory-nats.log" >&2
  exit 1
fi

# 2) Bounded backfill window (matches up-local.sh): re-reads recent events on each
#    start; the SQLite store is idempotent (event id PK) so re-replay is harmless.
WATCH_ROOT="${OPENSTORY_WATCH_ROOT:-$HOME/.claude/projects}"
BACKFILL_HOURS="${OPEN_STORY_WATCH_BACKFILL_HOURS:-72}"
echo "[backend] serve on :3002 (watch=$WATCH_ROOT, backfill=${BACKFILL_HOURS}h)"

# 3) Build once, then exec the BINARY directly (NOT `cargo run`). `cargo run` leaves a
#    cargo parent that launchd supervises while the real `open-story` runs as its
#    child; on `launchctl bootout` cargo is signalled but open-story is ORPHANED —
#    the cause of stranded writers (e.g. pid 79324 on 2026-06-29) and the restart bug.
#    Exec'ing the binary makes launchd supervise open-story itself, so stop/restart is
#    clean and KeepAlive tracks the real process.
echo "[backend] building open-story (debug)"
cargo build --manifest-path rs/cli/Cargo.toml --bin open-story
BIN="$OS_ROOT/rs/target/debug/open-story"
[ -x "$BIN" ] || { echo "[backend] FATAL: build did not produce $BIN" >&2; exit 1; }
echo "[backend] exec $BIN serve"
exec env OPEN_STORY_WATCH_BACKFILL_HOURS="$BACKFILL_HOURS" \
  "$BIN" serve --watch-dir "$WATCH_ROOT"

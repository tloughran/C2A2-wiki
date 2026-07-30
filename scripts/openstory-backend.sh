#!/usr/bin/env bash
# openstory-backend.sh — OpenStory capture backend, supervised by launchd
# (com.tomloughran.openstory.backend, RunAtLoad + KeepAlive).
#
# Ensures local-only NATS is up (token-free, deploy/nats-local.conf), then runs the
# Rust `serve` backend IN THE FOREGROUND via exec, so this process IS what launchd
# watches — if the backend dies, launchd restarts it. This is the durable feed that
# writes open-story.db (which the C2A2 wiki reads). 2026-06-25.
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

# 1) Local NATS JetStream on :4222 — start only if the port is free. Disowned: if it
#    dies, the backend below loses :4222 and exits, and launchd reruns this whole
#    script, which restarts NATS. So NATS is self-healed without its own agent.
if ! lsof -i :4222 >/dev/null 2>&1; then
  echo "[backend] starting local NATS on :4222"
  nats-server -c deploy/nats-local.conf > /tmp/nats-local.log 2>&1 &
  disown
  sleep 1
else
  echo "[backend] NATS already on :4222"
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

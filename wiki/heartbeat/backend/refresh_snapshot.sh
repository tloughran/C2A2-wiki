#!/usr/bin/env bash
# Self-contained snapshot refresh for the Heartbeat tab.
#
# Pipeline (each step deterministic except the model summary step):
#   export_digest  -> data/digest.json (+ dated snapshot)   [no model]
#   generate_summaries -> fill MISSING long summaries via cc-broker [model]
#   enrich_summaries   -> merge sidecar + clean boilerplate  [no model]
#   build_manifest     -> data/snapshots/index.json (History) [no model]
#
# TWO ways to provide the runtime data, auto-selected:
#   (A) HB_RUNTIME_DIR set  -> this script STARTS the runtime itself (one poll),
#       reads /api/digest, then shuts it down. Nothing else to keep running.
#       This is the mode to schedule (launchd / cron / Cowork task).
#   (B) HB_URL set (or default) -> use an already-running runtime at that URL.
#
# Examples:
#   HB_RUNTIME_DIR="/Users/you/Documents/C2A2 Heartbeat/c2a2_heartbeat" bash refresh_snapshot.sh
#   HB_URL="http://127.0.0.1:8787/api/digest?window=weekly" bash refresh_snapshot.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$(cd "$HERE/.." && pwd)/data"
PORT="${HB_PORT:-8799}"
RUNTIME_DIR="${HB_RUNTIME_DIR:-}"
SRV_PID=""

cleanup() { if [ -n "$SRV_PID" ]; then kill "$SRV_PID" 2>/dev/null || true; fi; }
trap cleanup EXIT

if [ -n "$RUNTIME_DIR" ]; then
  if [ ! -f "$RUNTIME_DIR/app.py" ]; then
    echo "[refresh] ERROR: no app.py under HB_RUNTIME_DIR=$RUNTIME_DIR" >&2; exit 1
  fi
  echo "[refresh] starting ephemeral runtime from: $RUNTIME_DIR (port $PORT)"
  ( cd "$RUNTIME_DIR" && exec python3 app.py --host 127.0.0.1 --port "$PORT" ) >/tmp/hb_runtime.log 2>&1 &
  SRV_PID=$!
  # Wait (up to ~40s) for the bootstrap poll + server to come up.
  up=""
  for _ in $(seq 1 40); do
    if curl -sS -m 3 "http://127.0.0.1:$PORT/health" >/dev/null 2>&1; then up=1; break; fi
    sleep 1
  done
  if [ -z "$up" ]; then echo "[refresh] ERROR: runtime did not become healthy (see /tmp/hb_runtime.log)" >&2; exit 1; fi
  URL="http://127.0.0.1:$PORT/api/digest?window=weekly"
else
  URL="${HB_URL:-http://127.0.0.1:8787/api/digest?window=weekly}"
fi

echo "[refresh] runtime URL: $URL"
echo "[refresh] data dir:    $DATA_DIR"

# 1) Export (deterministic field map, no model).
python3 "$HERE/export_digest.py" --url "$URL" --data-dir "$DATA_DIR"

# 2) Generate long summaries for any NEW items via the cc-broker (Pathway 00).
#    Non-fatal: if the broker is down or the daily cap is hit, we keep going and
#    those items simply show the short summary until the next run fills them.
if ! python3 "$HERE/generate_summaries.py" --data-dir "$DATA_DIR" --max-new 12; then
  echo "[refresh] WARN: summary generation step failed/partial — continuing with cached summaries"
fi

# 3) Merge long-summary sidecar + clean boilerplate (deterministic, no model).
python3 "$HERE/enrich_summaries.py" --data-dir "$DATA_DIR"

# 4) Archive a per-update History snapshot (only if content changed).
python3 "$HERE/archive_snapshot.py" --data-dir "$DATA_DIR"

# 4b) Prune old History snapshots (space governor) BEFORE rebuilding the manifest,
#     so the manifest reflects only the kept files. Default keep=60, override with
#     HB_KEEP_SNAPSHOTS.
python3 "$HERE/prune_snapshots.py" --data-dir "$DATA_DIR" --keep "${HB_KEEP_SNAPSHOTS:-60}"

# 5) Rebuild the History manifest (data/snapshots/index.json).
python3 "$HERE/build_manifest.py" --data-dir "$DATA_DIR"

# 6) Rebuild the published "Sources monitored" roster from the runtime source
#    config (deterministic, no model) so the breadth of inflow is visible even
#    when a given snapshot surfaces only a few sources.
CFG="${HB_SOURCES_CONFIG:-${RUNTIME_DIR:+$RUNTIME_DIR/config/sources.json}}"
if [ -n "$CFG" ] && [ -f "$CFG" ]; then
  python3 "$HERE/build_roster.py" --config "$CFG" --data-dir "$DATA_DIR"
else
  echo "[refresh] WARN: no sources config (set HB_SOURCES_CONFIG or HB_RUNTIME_DIR) — keeping existing roster"
fi

# 7) Stamp asset includes in index.html with content hashes (deterministic, no
#    model). Makes the ?v= cache-bust a function of file content so it is always
#    correct without a manual bump — guards the explorer iframe stale-asset trap.
python3 "$HERE/stamp_assets.py"

# 5) Guard: refuse to leave a seed-flagged or empty snapshot in place.
python3 - "$DATA_DIR/digest.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
assert d.get("seed") is False, "digest.json still flagged seed:true"
assert d.get("signals"), "digest.json has no signals"
print("[refresh] OK: seed=%s, signals=%d, generated=%s"
      % (d.get("seed"), len(d["signals"]), d.get("generated")))
PY

echo "[refresh] done."

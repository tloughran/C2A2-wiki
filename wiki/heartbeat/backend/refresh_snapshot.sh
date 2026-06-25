#!/usr/bin/env bash
# Deterministic snapshot refresh for the Heartbeat tab (Mac-side).
#
# Chains the two model-free steps: export the live runtime's /api/digest into
# data/digest.json (+ dated snapshot), then merge any existing long-summary
# sidecar entries and clean the short summaries. Safe to schedule (launchd).
#
# It does NOT generate new long summaries (that is the model step, still manual
# or future-broker-routed). New items simply show the short summary until a
# model enrich pass adds them to long_summaries.json — graceful by design.
#
# Prereq: the Heartbeat runtime is running locally and serving /api/digest.
#   cd "/path/to/c2a2_heartbeat" && python3 app.py     # serves on 127.0.0.1:8787
#
# Usage:
#   bash refresh_snapshot.sh                      # uses default URL below
#   HB_URL="http://127.0.0.1:8787/api/digest?window=weekly" bash refresh_snapshot.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$(cd "$HERE/.." && pwd)/data"
URL="${HB_URL:-http://127.0.0.1:8787/api/digest?window=weekly}"

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

# 4) Rebuild the History manifest (data/snapshots/index.json).
python3 "$HERE/build_manifest.py" --data-dir "$DATA_DIR"

# 3) Guard: refuse to leave a seed-flagged or empty snapshot in place.
python3 - "$DATA_DIR/digest.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
assert d.get("seed") is False, "digest.json still flagged seed:true"
assert d.get("signals"), "digest.json has no signals"
print("[refresh] OK: seed=%s, signals=%d, generated=%s"
      % (d.get("seed"), len(d["signals"]), d.get("generated")))
PY

echo "[refresh] done. Review locally over HTTP, then commit + push from the Mac."

#!/usr/bin/env bash
# refresh_openstory_feeds.sh — Mac-local runner for the C2A2 OpenStory agent feeds.
#
# Mirrors the scheduled-task steps but runs on the Mac, where open-story.db is on
# local disk: the extractors' byte-copy snapshot takes seconds, so the copy window
# rarely overlaps a WAL checkpoint (the sandbox keeps tearing it over the slow FUSE
# mount). Fail-loud per house Rule 12; writes REFRESH_STATUS.md on PASS and FAIL.
#
# Usage:  bash refresh_openstory_feeds.sh
set -uo pipefail

WIKI="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki"
AGD="$WIKI/agents/openstory"
DB="$HOME/Documents/Non-Claude Projects/OpenStory/data/open-story.db"
STATUS="$AGD/REFRESH_STATUS.md"
NOW="$(date -u +%Y-%m-%dT%H:%MZ)"
TODAY="$(date +%Y-%m-%d)"

fail() {  # $1 = which-step, $2 = first-error-line
  echo "$NOW  FAIL  $1 — $2 | DB age ${AGE_H:-?}h" > "$STATUS"
  echo "⚠️ OPENSTORY REFRESH FAILED: $1 — $2"
  exit 1
}

cd "$AGD" || { echo "no agent dir $AGD"; exit 2; }

# 1) FRESHNESS GUARD (36h)
#
# 2026-07-29: this used to compare `stat` mtime of open-story.db against 36h. Two
# ways that lied. In WAL mode the main DB file only changes on checkpoint, so it
# reads stale while ingest is perfectly healthy; and any *reader* opening the DB
# touches -shm/-wal, so it can read fresh while ingest is dead. What we actually
# need to know is whether ingest has fallen behind the transcripts on disk, so the
# question now goes to the shared assertion — the same one openstory-watchdog.sh
# asks, so the two can never form different opinions about whether ingest is alive.
# The 36h tolerance is unchanged, just expressed as lag (36 * 3600) instead of age.
LAG_SCRIPT="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project/scripts/openstory_ingest_lag.py"
[ -f "$DB" ] || fail "step1 freshness" "DB not found: $DB"
[ -f "$LAG_SCRIPT" ] || fail "step1 freshness" "shared assertion missing: $LAG_SCRIPT"
LAG_OUT=$(python3 "$LAG_SCRIPT" --db "$DB" --max-lag 129600 2>&1); LAG_RC=$?
# AGE_H feeds the REFRESH_STATUS.md line written by fail(); keep it defined on
# every path, including the undetermined one.
AGE_H=$(echo "$LAG_OUT" | sed -n 's/.*lag=\([0-9]*\)s.*/\1/p' | head -1)
case "$AGE_H" in ''|*[!0-9]*) AGE_H="?" ;; *) AGE_H=$(( AGE_H / 3600 )) ;; esac
if [ "$LAG_RC" -eq 1 ]; then
  fail "step1 freshness" "OpenStory ingest stalled ($LAG_OUT) — runtime likely down; feeds NOT refreshed"
elif [ "$LAG_RC" -ne 0 ]; then
  fail "step1 freshness" "cannot determine ingest lag ($LAG_OUT) — refusing to build feeds on unverified data"
fi
echo "[1] freshness OK: $LAG_OUT"

# 2) REFRESH BOTH FEEDS (extractors copy DB to local temp + retry on contention)
echo "[a] telemetry…"
python3 extract_openstory_agent_data.py --db "$DB" --map "$AGD/agent_map.json" --out "$AGD/agent_telemetry.json" \
  || fail "step2a extract_openstory_agent_data.py" "non-zero exit (see stderr above)"
echo "[a] inject…"
INJ=$(python3 inject_telemetry.py --telemetry "$AGD/agent_telemetry.json" --html "$WIKI/agents_tab.html") \
  || fail "step2a inject_telemetry.py" "non-zero exit"
echo "$INJ"
echo "[b] node-edges…"
python3 extract_agent_node_refs.py --db "$DB" --vault "$WIKI" --out "$AGD/agent_node_edges.json" \
  || fail "step2b extract_agent_node_refs.py" "non-zero exit (see stderr above)"

# 3) VALIDATE telemetry: injected (not no-op), embedded generated date == today, JS parses
echo "$INJ" | grep -q "Injected" || fail "step3 validate-telemetry" "inject reported no change (N=0) — feed not updated"
python3 - "$WIKI/agents_tab.html" "$TODAY" <<'PY' || fail "step3 validate-telemetry" "embedded telemetry bad / not today"
import re,sys,json
html=open(sys.argv[1]).read(); today=sys.argv[2]
m=re.search(r"/\* TELEMETRY_DATA_START \*/(.*?)/\* TELEMETRY_DATA_END \*/",html,re.DOTALL)
if not m: print("markers missing"); sys.exit(1)
js=m.group(1)
mj=re.search(r"const TELEMETRY = (\{.*\});",js,re.DOTALL)
if not mj: print("TELEMETRY const missing"); sys.exit(1)
d=json.loads(mj.group(1))
gen=d.get("_meta",{}).get("generated","")
if not gen.startswith(today): print("generated=%r not %s"%(gen,today)); sys.exit(1)
print("telemetry generated=%s agents=%d"%(gen,len(d.get("agents",{}))))
PY
# house rule: node --check the extracted JS block if node is present
if command -v node >/dev/null 2>&1; then
  python3 - "$WIKI/agents_tab.html" > /tmp/_tel_block.js <<'PY'
import re,sys
html=open(sys.argv[1]).read()
m=re.search(r"/\* TELEMETRY_DATA_START \*/(.*?)/\* TELEMETRY_DATA_END \*/",html,re.DOTALL)
sys.stdout.write(m.group(1) if m else "")
PY
  node --check /tmp/_tel_block.js || fail "step3 validate-telemetry" "node --check failed on TELEMETRY block"
  rm -f /tmp/_tel_block.js
fi

# 4) VALIDATE node-edges: parses, has agent_nodes, generated/mtime today
NE_DATE=$(python3 - "$AGD/agent_node_edges.json" "$TODAY" <<'PY' || true
import json,sys,os,datetime
p,today=sys.argv[1],sys.argv[2]
d=json.load(open(p))
nodes=d.get("agent_nodes") or d.get("nodes") or []
if not nodes: print("NO_NODES"); sys.exit(1)
gen=(d.get("_meta",{}) or {}).get("generated","")
if not gen: gen=datetime.datetime.fromtimestamp(os.path.getmtime(p)).isoformat()
if not str(gen).startswith(today): print("STALE:%s"%gen); sys.exit(1)
print("%s/%dnodes"%(gen[:19],len(nodes)))
PY
)
case "$NE_DATE" in
  NO_NODES) fail "step4 validate-node-edges" "agent_node_edges.json has no agent_nodes" ;;
  STALE:*)  fail "step4 validate-node-edges" "agent_node_edges.json not regenerated today ($NE_DATE)" ;;
  "")       fail "step4 validate-node-edges" "agent_node_edges.json failed to parse/validate" ;;
esac

# 5) STATUS (PASS) + 6) HEADLINE
TEL_AGENTS=$(echo "$INJ" | sed -n 's/.*Injected \([0-9]*\) agents.*/\1/p')
echo "$NOW  PASS  telemetry=$TODAY/${TEL_AGENTS:-?} agents  node_edges=$TODAY  | DB age ${AGE_H}h" > "$STATUS"
echo "✅ OPENSTORY REFRESH OK: telemetry=$TODAY (${TEL_AGENTS:-?} agents), node_edges=$NE_DATE | DB age ${AGE_H}h"
echo "   Publish is manual: git add/commit agents_tab.html + agents/openstory/agent_node_edges.json,"
echo "   then re-run the Summa sociogram regen (it re-embeds agent_node_edges.json)."

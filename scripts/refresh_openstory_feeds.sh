#!/bin/bash
#
# refresh_openstory_feeds.sh -- rebuild the wiki's two OpenStory-derived agent feeds
# ON THE MAC, where the database is.
#
# Why this exists
# ---------------
# The "openstory agents telemetry refresh" job moved to a cloud routine in September.
# Its extractors must read a local copy of open-story.db (reading the live WAL file
# trips quick_check mid-write -- see openstory_db.py), and the db is 7.5 GB. The cloud
# sandbox has about 9.6 GB of disk, so the copy died with ENOSPC (2026-10-01, 10-03),
# and on unattended mornings the fallback to a Mac shell was auto-declined. The Mac has
# the disk and the db is local to it, so the job runs here, under launchd
# (com.c2a2.openstory-feeds), the same way metabolism-publish does. Plan item 1.2.
#
# It is the old routine's five steps, as code (CLAUDE.md Rule 5):
#   1. freshness guard -- a db not written for 36h means OpenStory is down; refuse
#      rather than publish stale telemetry as current
#   2. the three extract/inject commands, with explicit paths
#   3. validate the telemetry feed: the date embedded in agents_tab.html is today and
#      the injected block passes `node --check`
#   4. validate the node-edges feed: parses, has agent_nodes, written today
#   5. append one dated PASS/FAIL line to REFRESH_STATUS.md, on EVERY run -- the feeds
#      were frozen 06-08..06-26 because failures only reached a log nobody read
#
# It never commits or pushes. The 05:45 commit step names these outputs as a post-run
# producer (POST_RUN_PRODUCERS in commit_daily_run.sh) and commits them next morning.
#
# Exit: 0 PASS, 1 FAIL (the status line says which step).
# Paths can be overridden for tests: REPO, DB, PYTHON, NODE.

set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="${REPO:-$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project}"
DB="${DB:-$HOME/Documents/Non-Claude Projects/OpenStory/data/open-story.db}"
PYTHON="${PYTHON:-python3}"
NODE="${NODE:-node}"
WIKI="$REPO/wiki"
AGD="$WIKI/agents/openstory"
STATUS="$AGD/REFRESH_STATUS.md"
MAX_DB_AGE_HOURS=36

stamp() { date -u "+%Y-%m-%dT%H:%MZ"; }
today=$(date "+%Y-%m-%d")

fail() {
  echo "$(stamp)  FAIL  $*" | tee -a "$STATUS"
  exit 1
}

cd "$AGD" 2>/dev/null || { echo "$(stamp) FAIL cannot cd to $AGD"; exit 1; }

# --- 1. freshness guard -----------------------------------------------------
[ -f "$DB" ] || fail "step 1 -- db not found: $DB"
db_age_h=$("$PYTHON" -c "import os,sys,time; print(int((time.time()-os.path.getmtime(sys.argv[1]))//3600))" "$DB")
[ "$db_age_h" -gt "$MAX_DB_AGE_HOURS" ] && \
  fail "step 1 -- OpenStory db last written ${db_age_h}h ago (> ${MAX_DB_AGE_HOURS}h); runtime likely down; feeds NOT refreshed"

# --- 2. refresh both feeds ----------------------------------------------------
run() {  # step-label, command...
  local label="$1"; shift
  local out
  out=$("$@" 2>&1) || fail "step 2 ($label) -- $(printf '%s\n' "$out" | grep -v '^\s*$' | tail -1)"
  printf '%s\n' "$out"
}
run extract-telemetry "$PYTHON" extract_openstory_agent_data.py --db "$DB" --map "$AGD/agent_map.json" --out "$AGD/agent_telemetry.json"
inject_out=$(run inject "$PYTHON" inject_telemetry.py --telemetry "$AGD/agent_telemetry.json" --html "$WIKI/agents_tab.html") || exit 1
printf '%s\n' "$inject_out"
run extract-node-edges "$PYTHON" extract_agent_node_refs.py --db "$DB" --vault "$WIKI" --out "$AGD/agent_node_edges.json"

# --- 3. validate the telemetry feed ------------------------------------------
check=$("$PYTHON" - "$WIKI/agents_tab.html" "$today" "$NODE" <<'PY'
import json, re, subprocess, sys, tempfile
html, today, node = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(html, encoding="utf-8").read()
m = re.search(r"/\* TELEMETRY_DATA_START \*/(.*?)/\* TELEMETRY_DATA_END \*/", text, re.S)
if not m:
    sys.exit("telemetry block markers missing from agents_tab.html")
block = m.group(1)
g = re.search(r'"generated":"(\d{4}-\d{2}-\d{2})', block)
if not g or g.group(1) != today:
    sys.exit(f"embedded telemetry generated {g.group(1) if g else '?'}, not today ({today})")
with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as t:
    t.write(block)
r = subprocess.run([node, "--check", t.name], capture_output=True, text=True)
if r.returncode:
    sys.exit("injected telemetry block fails node --check: " +
             next((l for l in r.stderr.splitlines() if "Error" in l), r.stderr.strip()[:200]))
n = len(json.loads(re.search(r"=\s*(\{.*\})\s*;?\s*$", block.strip(), re.S).group(1)).get("agents", {}))
print(f"telemetry={today}/{n} agents")
PY
) || fail "step 3 (validate telemetry) -- $check"

# --- 4. validate the node-edges feed ------------------------------------------
edges=$("$PYTHON" - "$AGD/agent_node_edges.json" "$today" <<'PY'
import datetime, json, os, sys
path, today = sys.argv[1], sys.argv[2]
d = json.load(open(path))
if not d.get("agent_nodes"):
    sys.exit("agent_node_edges.json has no agent_nodes")
written = datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()
if written != today:
    sys.exit(f"agent_node_edges.json last written {written}, not today")
print(f"node_edges={today}/{len(d['agent_nodes'])} agents")
PY
) || fail "step 4 (validate node-edges) -- $edges"

# --- 5. status line -------------------------------------------------------------
echo "$(stamp)  PASS  $check  $edges  | DB age ${db_age_h}h (launchd, on the Mac)" | tee -a "$STATUS"
exit 0

#!/bin/bash
#
# publish_metabolism.sh -- validate-then-push for the weekly Metabolism Monitor.
#
# Replaces the manual "eyeball then push" step for the generated metabolism
# view ONLY. Scoped so it can never stage or commit anything outside
# wiki/metabolism/. Fails loud and pushes nothing on any validation failure.
#
# Intended to run on the Mac (which has git push creds) AFTER the Cowork
# scheduled task has regenerated the files in the sandbox-mounted repo.
# It does NOT regenerate anything itself; it only validates and publishes
# what is already on disk.
#
# Exit codes:
#   0 = pushed, or nothing to publish (no diff)
#   1 = validation failed / freshness failed / push rejected (NO push happened
#       on validation/freshness fail; on push-reject the local commit remains)
#
# Safety properties:
#   - Never force-pushes.
#   - Commits ONLY the two metabolism files via pathspec; leaves the rest of
#     your working tree and index untouched.
#   - Refuses to publish stale files (guards against a failed sandbox regen).

set -euo pipefail

REPO="/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
HTML="wiki/metabolism/metabolism_view.html"
JSON="wiki/metabolism/metabolism_data.json"
VALIDATOR="wiki/c2a2-wiki-narration/scripts/validate_html.py"
MAX_AGE_HOURS=36          # files older than this = stale = refuse to publish
LOG="$REPO/metabolism-monitor/publish.log"

ts() { date "+%Y-%m-%dT%H:%M:%S%z"; }
log() { echo "[$(ts)] $*" | tee -a "$LOG"; }
fail() { log "FAIL: $*"; log "No push performed."; exit 1; }

cd "$REPO" || fail "repo not found: $REPO"
mkdir -p "$(dirname "$LOG")"

log "=== publish_metabolism start ==="

# --- 0. Files must exist ---
[ -f "$HTML" ] || fail "missing $HTML"
[ -f "$JSON" ] || fail "missing $JSON"

# --- 1. Freshness: refuse to publish a stale regen (sandbox run may have failed) ---
now=$(date +%s)
json_mtime=$(stat -f %m "$JSON")              # BSD stat (macOS)
age_h=$(( (now - json_mtime) / 3600 ))
if [ "$age_h" -gt "$MAX_AGE_HOURS" ]; then
  fail "FRESHNESS: $JSON is ${age_h}h old (> ${MAX_AGE_HOURS}h). Sandbox regen likely did not run."
fi
log "freshness OK: data is ${age_h}h old"

# --- 2. Nothing to publish? Exit clean. ---
if git diff --quiet HEAD -- "$HTML" "$JSON"; then
  log "no changes in metabolism files vs HEAD; nothing to publish."
  log "=== publish_metabolism done (noop) ==="
  exit 0
fi

# --- 3. Structural validation (JS syntax + brace balance via node --check) ---
log "validating $HTML ..."
if ! python3 "$VALIDATOR" "$HTML" >>"$LOG" 2>&1; then
  fail "validate_html.py reported structural errors (see $LOG). Generator likely broken."
fi
log "structural validation PASS"

# --- 4. Metabolism data sanity (guards the schema-drift / blank-render failure mode) ---
log "checking metabolism data sanity ..."
if ! python3 - "$JSON" >>"$LOG" 2>&1 <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
lanes = d.get("lanes") or d.get("agents") or []
# Count total runs robustly. The metabolism schema stores, per lane, an int
# "runs" (the count) and a list "rows" (the runs themselves) -- NOT a list under
# "runs". The prior `sum(len(l.get("runs", [])) ...)` therefore did len(int) and
# crashed with TypeError on every real file (the live one included); it never
# fired only because the upstream freshness guard short-circuited for weeks.
# Prefer the authoritative _meta.total_runs; fall back to summing per lane,
# tolerating runs-as-int, runs-as-list, or the rows list.
def lane_runs(l):
    r = l.get("runs")
    if isinstance(r, int):
        return r
    if isinstance(r, list):
        return len(r)
    return len(l.get("rows", []))
runs = (d.get("_meta") or {}).get("total_runs")
if runs is None:
    runs = d.get("runs")
if isinstance(runs, list):
    runs = len(runs)
if runs is None:
    runs = sum(lane_runs(l) for l in lanes) if isinstance(lanes, list) else 0
assert lanes, "no lanes/agents in metabolism_data.json"
assert int(runs) > 0, "zero runs in metabolism_data.json (blank render?)"
print(f"  [PASS] data sanity: {len(lanes) if isinstance(lanes,list) else lanes} lanes, {runs} runs")
PY
then
  fail "metabolism data sanity check failed (empty/blank/schema drift). See $LOG."
fi
log "data sanity PASS"

# --- 5. Commit ONLY the two metabolism files (pathspec keeps it surgical) ---
branch=$(git symbolic-ref --short HEAD)
log "committing metabolism files on branch '$branch' ..."
git commit -q -m "metabolism: weekly auto-publish ($(date +%Y-%m-%d))" -- "$HTML" "$JSON"

# Belt-and-suspenders: assert the commit we just made touched ONLY our two paths.
changed=$(git show --name-only --pretty=format: HEAD | grep -v '^$' | sort)
expected=$(printf '%s\n%s\n' "$HTML" "$JSON" | sort)
if [ "$changed" != "$expected" ]; then
  fail "ABORT: latest commit touched unexpected paths:\n$changed\n(left commit in place for manual review; NOT pushed)"
fi
log "commit scoped correctly to metabolism files only"

# --- 6. Push (never force). On non-fast-forward, fail loud and leave commit. ---
log "pushing to origin/$branch ..."
if ! git push origin "$branch" >>"$LOG" 2>&1; then
  fail "push rejected (likely non-fast-forward; origin moved). Commit is local. Run 'git pull --rebase' on the Mac, then re-run this script. NOT force-pushing."
fi

log "PUSH OK -> origin/$branch"
log "=== publish_metabolism done (published) ==="
exit 0

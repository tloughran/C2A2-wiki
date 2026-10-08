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
MAX_AGE_HOURS=36          # data generated longer ago than this = stale = refuse
                          # to publish. Measured from _meta.generated, NOT mtime.
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
#
# Read the date the GENERATOR wrote into the file (_meta.generated), never the
# file's mtime. This used to be `stat -f %m "$JSON"`, and that failed in the
# DANGEROUS direction: the 22:00 summa-vault-sync rebase rewrites working-tree
# files, which resets their mtimes, so a file whose data had been stale for days
# looked minutes old and sailed through this gate. The connectome bug had the
# same root cause (git not preserving mtimes) but failed safe -- it refused to
# publish fresh work. This one would have published stale data believing it
# fresh. Same remedy as there: compare against the artifact's own build stamp.
#
# _meta.generated is the field check_scheduler_health.py already reads for this
# artifact (see its ARTIFACTS table), so the checker and the publisher now agree
# on what "fresh" means.
#
# A missing or unparseable stamp is a FAIL, not a fallback to mtime: an
# unstamped file is exactly the case this gate cannot judge, and silently
# reverting to mtime would reinstate the bug on the one file that needs the gate
# most.
# The 2>&1 belongs on THIS line, before the heredoc body. Written after the PY
# terminator it parses as a separate null command, which swallows python's exit
# status and makes the `if !` always false -- i.e. a missing stamp would pass
# the gate silently, the exact failure this block exists to prevent.
if ! age_h=$(python3 - "$JSON" 2>&1 <<'PY'
import json, sys
from datetime import datetime, timezone

try:
    meta = (json.load(open(sys.argv[1])) or {}).get("_meta") or {}
except (OSError, ValueError) as exc:
    sys.exit(f"cannot read JSON: {exc}")

stamp = meta.get("generated")
if stamp is None:
    sys.exit("_meta.generated is absent -- the file does not date itself")
try:
    generated = datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
except ValueError:
    sys.exit(f"_meta.generated is not an ISO-8601 timestamp: {stamp!r}")
if generated.tzinfo is None:
    generated = generated.astimezone()

print(int((datetime.now(timezone.utc) - generated).total_seconds() // 3600))
PY
); then
  fail "FRESHNESS: cannot read a build stamp from $JSON: $age_h. Refusing to fall back to mtime -- the rebase resets mtimes, so that check would read a stale file as fresh. Fix the generator to stamp _meta.generated."
fi
if [ "$age_h" -gt "$MAX_AGE_HOURS" ]; then
  fail "FRESHNESS: $JSON was generated ${age_h}h ago (> ${MAX_AGE_HOURS}h) per its own _meta.generated. Sandbox regen likely did not run."
fi
log "freshness OK: data was generated ${age_h}h ago (per _meta.generated)"

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

# Sunday 06:30 lands inside a cluster of other git-touching jobs -- janitor
# 05:45, metabolism-monitor 06:05, voice-faq and connector-health 06:15, the
# telemetry refresh 06:05 -- and .git/index.lock is held for as long as whichever
# one is mid-write. 2026-08-09: the commit hit a held lock, git exited 128, and
# `set -e` killed the script before fail() could log a word; the launchd exit code
# was the only evidence it left. A held lock is transient by nature, so wait it
# out. Anything else is a real failure and stops immediately.
#
# The date is stamped once, before the loop: a retry must not produce a commit
# message dated differently from the run that started it.
commit_msg="metabolism: weekly auto-publish ($(date +%Y-%m-%d))"
committed=0
for attempt in 1 2 3 4 5 6; do
  if commit_err=$(git commit -q -m "$commit_msg" -- "$HTML" "$JSON" 2>&1); then
    committed=1
    break
  fi
  case "$commit_err" in
    *index.lock*)
      log "git index locked by another process (attempt $attempt/6); waiting 15s"
      sleep 15
      ;;
    *)
      fail "git commit failed: $commit_err"
      ;;
  esac
done
if [ "$committed" -ne 1 ]; then
  fail "git index still locked after 6 attempts (90s). Another process is holding $REPO/.git/index.lock. NOT pushed."
fi

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

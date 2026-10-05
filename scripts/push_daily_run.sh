#!/bin/bash
#
# push_daily_run.sh -- publish the daily run's commits to GitHub, behind a gate.
#
# Why this exists
# ---------------
# commit_daily_run.sh commits the run's output on the Mac and, by design, never
# pushes. Pushing stayed a human act -- and on 2026-09-30 and 10-01 nobody did it.
# Two days of output sat on the Mac, the nightly vault sync then failed rebasing
# across the gap, and no watchdog noticed, because every check looked at the local
# commit and none looked at GitHub. Tom decided on 2026-10-05: auto-push, behind a
# check. This is that check.
#
# It is the second carve-out from CLAUDE.md's no-blind-push rule (the first is the
# heartbeat's data-only refresh). That rule exists because an unreviewed code/HTML
# push broke rendering. So the gate here is aimed at exactly that failure, and at
# the other ways an unattended push can publish the wrong thing:
#
#   - WHOSE commits: every commit between origin/main and HEAD must carry the
#     "C2A2 daily run" subject. Anything else ahead of origin -- Tom's own work, a
#     vault-sync commit that failed to push -- belongs to somebody who has not
#     asked for it to be published. Refuse, never sweep it up.
#   - WHAT paths: the outgoing diff must stay inside commit_daily_run.sh's
#     allowlist. A forged subject cannot widen the scope.
#   - The personal address, again: re-checked on the OUTGOING diff, so it covers
#     commits this script did not watch being made.
#   - Does it still render: every changed .html file's inline <script> blocks must
#     pass `node --check`, and every changed .json file must parse. A syntax error
#     in inline JS is the exact "page loads blank" failure the rule protects.
#
# Getting level with GitHub uses MERGE, never rebase. The heartbeat Action pushes
# to main every day, so the Mac is routinely one commit behind. On 2026-09-30 the
# vault sync's rebase across that gap died on files changing mid-replay; the merge
# done by hand on 10-01 touched only the incoming heartbeat files and went through.
# A merge conflict aborts cleanly and refuses.
#
# Never force-pushes. A rejected push gets one fetch-merge-retry (the heartbeat
# can land between our fetch and our push -- it did on 10-01), then refuses.
#
# Exit codes:
#   0 = pushed, or nothing to push (clean no-op)
#   1 = refused or failed; nothing was pushed (a local merge commit may remain,
#       which is harmless and the next run reuses it)
#
# Every run writes scheduler/daily_push.json (gitignored) with the date of the
# newest daily-run commit ON GITHUB. check_scheduler_health.py alarms when that
# date is stale -- the question nothing asked on 09-30.
#
# Usage:
#   bash scripts/push_daily_run.sh
#   bash scripts/push_daily_run.sh --dry-run
#   bash scripts/push_daily_run.sh --repo /tmp/fixture

set -uo pipefail

REPO_DEFAULT="/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
REMOTE="origin"
BRANCH="main"

# Must keep matching commit_daily_run.sh's subject and check_scheduled_commits.py.
SUBJECT_RE='^C2A2 daily run'

# Must keep matching commit_daily_run.sh's ALLOWED_RE (section 5 there).
ALLOWED_RE='^(wiki/|prototypes/(level2_build_meta\.json|signals\.json|signals_grown\.json|level2_signal_stream\.html|backlog/(backlog_manifest\.json|qc_trace\.csv))$)'

STATUS_JSON="scheduler/daily_push.json"
STATUS_LOG="scheduler/daily_push.md"

REPO="$REPO_DEFAULT"
DRY_RUN=0
while [ $# -gt 0 ]; do
  case "$1" in
    --repo) REPO="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    *) echo "unknown argument: $1" >&2; exit 1 ;;
  esac
done

ts() { date "+%Y-%m-%dT%H:%M:%S%z"; }
log() { echo "[$(ts)] $*"; }
g() { git -C "$REPO" "$@"; }

# One status write per run, on every path, so the health row always has a fresh
# reading of where GitHub stands -- including on the days this refuses.
write_status() {  # verdict, detail
  [ "$DRY_RUN" -eq 1 ] && return 0
  mkdir -p "$REPO/scheduler"
  local origin_at
  origin_at=$(g log -1 --format=%cI -E --grep="$SUBJECT_RE" "$REMOTE/$BRANCH" 2>/dev/null || true)
  VERDICT="$1" DETAIL="$2" ORIGIN_AT="$origin_at" HEAD_SHA="$(g rev-parse --short HEAD 2>/dev/null)" \
  OUT="$REPO/$STATUS_JSON" python3 - <<'PY'
import json, os
from datetime import datetime, timezone
json.dump({
    "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "verdict": os.environ["VERDICT"],
    "detail": os.environ["DETAIL"],
    "head": os.environ["HEAD_SHA"],
    "origin_daily_run_at": os.environ["ORIGIN_AT"] or None,
}, open(os.environ["OUT"], "w"), indent=2)
PY
  printf '%s  %-7s %s\n' "$(ts)" "$1" "$2" >> "$REPO/$STATUS_LOG"
}

refuse() {
  log "REFUSED: $*"
  write_status "REFUSED" "$*"
  log "nothing pushed"
  exit 1
}

[ -d "$REPO/.git" ] || { log "REFUSED: not a git repo: $REPO"; exit 1; }
log "=== push_daily_run start ($REPO) ==="

# --- 1. Same preconditions as the commit step ------------------------------
for marker in MERGE_HEAD REBASE_HEAD CHERRY_PICK_HEAD BISECT_LOG; do
  [ -e "$REPO/.git/$marker" ] && refuse "$marker present -- repo is mid-operation"
done
for lock in "$REPO"/.git/*.lock; do
  [ -e "$lock" ] && refuse "git lock present: $lock"
done
[ "$(g symbolic-ref --short HEAD 2>/dev/null)" = "$BRANCH" ] || refuse "not on $BRANCH"

g fetch -q "$REMOTE" "$BRANCH" || refuse "git fetch $REMOTE $BRANCH failed"

# --- 2. Whose commits ------------------------------------------------------
ahead=$(g log --no-merges --format='%h %s' "$REMOTE/$BRANCH..HEAD")
if [ -z "$ahead" ]; then
  log "nothing ahead of $REMOTE/$BRANCH; nothing to push"
  write_status "OK" "nothing to push"
  log "=== push_daily_run done (noop) ==="
  exit 0
fi
foreign=$(printf '%s\n' "$ahead" | cut -d' ' -f2- | grep -vE "$SUBJECT_RE" || true)
if [ -n "$foreign" ]; then
  refuse "commits ahead of $REMOTE/$BRANCH that are not daily-run commits -- their author has not asked to publish them:
$(printf '%s\n' "$ahead" | grep -vE "^[0-9a-f]+ ${SUBJECT_RE#^}" | sed 's/^/  /')"
fi
n_ahead=$(printf '%s\n' "$ahead" | grep -c .)
log "$n_ahead daily-run commit(s) ahead of $REMOTE/$BRANCH"

# --- 3. What paths, and the address ----------------------------------------
# Three-dot: only what OUR side changed since the common ancestor, not the
# heartbeat's incoming changes.
paths=$(g diff --name-only "$REMOTE/$BRANCH...HEAD")
escaped=$(printf '%s\n' "$paths" | grep . | grep -vE "$ALLOWED_RE" || true)
[ -n "$escaped" ] && refuse "outgoing paths outside the daily-run allowlist:
$escaped"
if g diff "$REMOTE/$BRANCH...HEAD" | grep -qi 'thomas\.loughran@gmail\.com'; then
  refuse "personal address present in the outgoing diff"
fi
log "scope and address checks clean ($(printf '%s\n' "$paths" | grep -c .) path(s))"

# --- 4. Does it still render ------------------------------------------------
command -v node >/dev/null 2>&1 || refuse "node not found -- cannot verify inline JS, so not publishing"
render=$(cd "$REPO" && printf '%s\n' "$paths" | python3 -c '
import json, os, re, subprocess, sys, tempfile
SCRIPT = re.compile(r"<script\b([^>]*)>(.*?)</script\s*>", re.S | re.I)
NOT_JS = re.compile(r"type\s*=\s*[\"\x27]?(application/(ld\+)?json|text/(template|x-template|plain))", re.I)
bad = []
for path in filter(None, (l.strip() for l in sys.stdin)):
    if not os.path.exists(path):
        continue  # deleted by the run; nothing left to render
    if path.endswith(".json"):
        try: json.load(open(path, encoding="utf-8"))
        except Exception as e: bad.append(f"{path}: invalid JSON ({e})")
    elif path.endswith(".html"):
        html = open(path, encoding="utf-8", errors="replace").read()
        for i, m in enumerate(SCRIPT.finditer(html)):
            attrs, body = m.group(1), m.group(2)
            if re.search(r"\bsrc\s*=", attrs, re.I) or NOT_JS.search(attrs) or not body.strip():
                continue
            ext = ".mjs" if re.search(r"type\s*=\s*[\"\x27]?module", attrs, re.I) else ".js"
            with tempfile.NamedTemporaryFile("w", suffix=ext, delete=False, encoding="utf-8") as t:
                t.write(body)
            r = subprocess.run(["node", "--check", t.name], capture_output=True, text=True)
            os.unlink(t.name)
            if r.returncode:
                lines = r.stderr.strip().splitlines() or ["?"]
                first = next((l for l in lines if "Error" in l), lines[0])
                bad.append(f"{path}: inline <script> #{i} fails node --check: {first}")
print("\n".join(bad))
')
[ -n "$render" ] && refuse "outgoing content would not render cleanly:
$render"
log "render check clean (inline JS + JSON)"

if [ "$DRY_RUN" -eq 1 ]; then
  log "--dry-run: all gates pass; would merge $REMOTE/$BRANCH if behind, then push"
  log "=== push_daily_run done (dry run) ==="
  exit 0
fi

# --- 5. Level with GitHub (merge, never rebase), then push ------------------
# Content from origin is already public, so merging it in needs no re-check.
merge_origin() {
  g merge-base --is-ancestor "$REMOTE/$BRANCH" HEAD && return 0
  if ! g merge -q --no-edit "$REMOTE/$BRANCH" >/dev/null 2>&1; then
    g merge --abort 2>/dev/null || true
    refuse "merging $REMOTE/$BRANCH conflicted (or the working tree overlaps it); merge aborted"
  fi
  log "merged $REMOTE/$BRANCH"
}
merge_origin
if ! g push -q "$REMOTE" "HEAD:$BRANCH" 2>/dev/null; then
  log "push rejected; one fetch-merge-retry (another job may have pushed meanwhile)"
  g fetch -q "$REMOTE" "$BRANCH" || refuse "git fetch failed on retry"
  # A retry must not smuggle in what the gate never saw: re-run section 2's test.
  late=$(g log --no-merges --format=%s "$REMOTE/$BRANCH..HEAD" | grep -vE "$SUBJECT_RE" || true)
  [ -n "$late" ] && refuse "non-daily-run commits appeared ahead of $REMOTE/$BRANCH during the retry"
  merge_origin
  g push -q "$REMOTE" "HEAD:$BRANCH" 2>/dev/null || refuse "push rejected twice -- NOT force-pushing"
fi
g fetch -q "$REMOTE" "$BRANCH" 2>/dev/null || true
log "pushed $(g rev-parse --short HEAD): $n_ahead daily-run commit(s)"
write_status "PUSHED" "$n_ahead daily-run commit(s) at $(g rev-parse --short HEAD)"
log "=== push_daily_run done ==="
exit 0

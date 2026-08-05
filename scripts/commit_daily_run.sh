#!/bin/bash
#
# commit_daily_run.sh -- commit the daily run's output ON THE MAC, because the
# sandbox cannot.
#
# Why this exists
# ---------------
# c282-wiki-agent-daily-run does its whole job and then reports, verbatim:
#
#     Phase 6 (Commit/push): BLOCKED -- sandbox cannot write .git objects.
#                            Must run on Mac.
#
# That is not a hang and not a permission prompt. The scheduled task is
# structurally unable to write git objects, so every day's output stays in the
# working tree. By 2026-08-05 that was 74 uncommitted paths, and
# check_scheduled_commits.py had been failing daily for a thing the sandbox can
# never do. This closes that loop from the Mac side, which is where the git
# credentials and the write access actually are.
#
# It replicates Phase 6 of the run's own SKILL.md exactly -- the same pathspec,
# the same community_explorer.html guard, the same commit-message shape (which
# check_scheduled_commits.py greps for) -- and adds the guards a sandboxed model
# cannot enforce on itself.
#
# It DOES NOT PUSH. That is deliberate and not an oversight. The standing rule in
# CLAUDE.md is that nothing reaches GitHub without a human looking at it first;
# the one carve-out is the heartbeat's data-only refresh behind a CI gate. Daily
# run output is wiki content -- HTML and prose -- which is exactly the class that
# rule exists to protect. Committing converts an unbounded working-tree pile into
# a reviewable commit; pushing stays a human act.
#
# Exit codes:
#   0 = committed, or nothing to commit (clean no-op)
#   1 = refused; nothing was committed and the working tree is untouched
#
# Usage:
#   bash scripts/commit_daily_run.sh
#   bash scripts/commit_daily_run.sh --dry-run
#   bash scripts/commit_daily_run.sh --repo /tmp/fixture --registry-glob '/tmp/reg/*.json'

set -uo pipefail

REPO_DEFAULT="/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
REGISTRY_DEFAULT="$HOME/Library/Application Support/Claude/*/*/*/scheduled-tasks.json"
TASK_ID="c282-wiki-agent-daily-run"

# The run starts 04:30 and takes ~6 minutes. 25h lets one missed day pass without
# committing yesterday's leftovers under today's date, while still catching the
# normal case. If the run has not run this recently, whatever is dirty is somebody
# else's work and must not be swept up.
MAX_RUN_AGE_HOURS=25

# A ceiling, not a target. The daily run touches tens of files; hundreds means
# something else happened -- a branch switch, a bulk regen, a vault sync mid-flight.
# Fail loud rather than commit a surprise.
MAX_STAGED_FILES=400

# Named paths only. `git add -A` is forbidden in this repo -- it once published a
# spend-on-load spike file. wiki/ is the run's output tree; the six prototypes/
# paths are what Phase 5.6's Level-2 wrapper rewrites, including the guard's own
# baseline.
PATHSPEC=(
  "wiki/"
  "prototypes/level2_build_meta.json"
  "prototypes/signals.json"
  "prototypes/signals_grown.json"
  "prototypes/level2_signal_stream.html"
  "prototypes/backlog/backlog_manifest.json"
  "prototypes/backlog/qc_trace.csv"
)

# Generated, data-inlined, and NOT built by the daily run. A clobbered working-tree
# copy published by this script is exactly what broke the Graph/Cards bar on
# 2026-06-07. Regenerate it deliberately or leave it alone.
NEVER_COMMIT=("wiki/community_explorer.html")

# How long after the run starts its own writes can still land. Same 45 minutes
# check_daily_run_stall.py uses, and for the same reason: the longest clean run
# measured across 110 transcripts is 535s, so 45 minutes is five times the real
# ceiling. Anything under wiki/ touched after that was written by somebody else.
RUN_WRITE_WINDOW_SECONDS=2700

# The exceptions: automated producers that legitimately write into the run's
# output tree LATER in the morning, whose output this script is still the right
# one to commit. refresh_openstory_feeds.sh rewrites both of these around 06:19,
# roughly two hours after the run. Add a prefix here only for a scheduled,
# deterministic producer -- never to silence a refusal you did not understand.
POST_RUN_PRODUCERS=(
  "wiki/agents/openstory/"
  "wiki/agents_tab.html"
)

# Repo-relative. Same status-file shape as scheduler/commit_check.md and
# scheduler/run_stall.md: one appended dated line per run, so a held path is still
# legible tomorrow when the launchd log has scrolled. gitignored like the rest of
# scheduler/.
HELD_STATUS_FILE="scheduler/held_paths.md"

REPO="$REPO_DEFAULT"
REGISTRY_GLOB="$REGISTRY_DEFAULT"
DRY_RUN=0
SKIP_RUN_CHECK=0
RUN_START_EPOCH=""

while [ $# -gt 0 ]; do
  case "$1" in
    --repo) REPO="$2"; shift 2 ;;
    --registry-glob) REGISTRY_GLOB="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    --skip-run-check) SKIP_RUN_CHECK=1; shift ;;
    *) echo "unknown argument: $1" >&2; exit 1 ;;
  esac
done

ts() { date "+%Y-%m-%dT%H:%M:%S%z"; }
log() { echo "[$(ts)] $*"; }

# Every refusal path unstages first. A script that bails with a half-built index
# leaves the next run -- and the next human -- looking at state nobody created on
# purpose.
fail() {
  log "REFUSED: $*"
  git -C "$REPO" reset -q 2>/dev/null || true
  log "index reset; nothing committed"
  exit 1
}

[ -d "$REPO/.git" ] || { log "REFUSED: not a git repo: $REPO"; exit 1; }

log "=== commit_daily_run start ($REPO) ==="

# --- 1. Refuse on a repo that is mid-operation ------------------------------
# An unfinished merge sat in this repo for two days once, and the daily run
# correctly declined to commit into it. Same judgement, in code.
for marker in MERGE_HEAD REBASE_HEAD CHERRY_PICK_HEAD BISECT_LOG; do
  [ -e "$REPO/.git/$marker" ] && fail "$marker present -- repo is mid-operation"
done
for lock in "$REPO"/.git/index.lock "$REPO"/.git/*.lock; do
  [ -e "$lock" ] && fail "stale git lock present: $lock"
done

branch=$(git -C "$REPO" symbolic-ref --short HEAD 2>/dev/null)
[ -n "$branch" ] || fail "detached HEAD -- refusing to commit"
[ "$branch" = "main" ] || fail "on branch '$branch', not main -- refusing to commit"

# --- 2. Refuse unless the daily run actually ran recently -------------------
# Without this, a dirty tree from any source would get committed under a
# "C2A2 daily run" message, which is a lie in the log and hides the real author.
if [ "$SKIP_RUN_CHECK" -eq 0 ]; then
  age=$(REGISTRY_GLOB="$REGISTRY_GLOB" TASK_ID="$TASK_ID" python3 - <<'PY'
import glob, json, os, sys
from datetime import datetime, timezone
newest = None
for path in glob.glob(os.environ["REGISTRY_GLOB"]):
    try:
        tasks = json.load(open(path)).get("scheduledTasks", [])
    except (OSError, ValueError):
        continue
    for task in tasks:
        if task.get("id") != os.environ["TASK_ID"]:
            continue
        stamp = task.get("lastRunAt")
        if stamp and (newest is None or stamp > newest):
            newest = stamp
if newest is None:
    print("NONE"); sys.exit(0)
ran = datetime.fromisoformat(newest.replace("Z", "+00:00"))
print(f"{(datetime.now(timezone.utc) - ran).total_seconds() / 3600:.1f} {ran.timestamp():.0f}")
PY
) || fail "could not read the task registry"
  [ "$age" = "NONE" ] && fail "$TASK_ID is not in any registry -- cannot confirm a run"
  # The block prints "<hours> <epoch>"; the authorship guard below needs the epoch.
  RUN_START_EPOCH="${age##* }"
  age="${age%% *}"
  if awk "BEGIN{exit !($age > $MAX_RUN_AGE_HOURS)}"; then
    fail "$TASK_ID last ran ${age}h ago (> ${MAX_RUN_AGE_HOURS}h) -- the dirty tree is not its output"
  fi
  log "run freshness OK: $TASK_ID ran ${age}h ago"
fi

# --- 3. Stage, by name only ------------------------------------------------
git -C "$REPO" reset -q || fail "could not reset the index"

# `git add` is fatal on a pathspec that matches nothing, and the six prototypes
# files only exist once Phase 5.6 has run at least once. Narrow to what is
# actually there -- on disk, OR tracked in HEAD, so a file the run DELETED still
# gets its deletion staged.
present=()
for path in "${PATHSPEC[@]}"; do
  if [ -e "$REPO/$path" ] || git -C "$REPO" ls-files --error-unmatch -- "$path" >/dev/null 2>&1; then
    present+=("$path")
  fi
done
if [ "${#present[@]}" -eq 0 ]; then
  log "none of the expected output paths exist yet; nothing to commit"
  log "=== commit_daily_run done (noop) ==="
  exit 0
fi
git -C "$REPO" add -- "${present[@]}" || fail "git add failed"

# --- 4. Unstage the artifacts this run does not build -----------------------
for path in "${NEVER_COMMIT[@]}"; do
  if git -C "$REPO" diff --cached --name-only -- "$path" | grep -q .; then
    git -C "$REPO" restore --staged -- "$path" 2>/dev/null || true
    log "GUARD: unstaged $path (generated elsewhere; never auto-commit)"
  fi
done

staged=$(git -C "$REPO" diff --cached --name-only)
if [ -z "$staged" ]; then
  log "nothing staged; working tree has no daily-run output to commit"
  log "=== commit_daily_run done (noop) ==="
  exit 0
fi
count=$(printf '%s\n' "$staged" | wc -l | tr -d ' ')
log "staged $count path(s)"

# --- 5. Assert the index escaped nowhere -----------------------------------
# Belt-and-suspenders against a pathspec typo or a future edit widening the list.
# Anything staged that is not under wiki/ or one of the six named prototypes
# files means the scope broke, and the whole point of the named pathspec is gone.
#
# Written as a regex rather than a `case`: a `)` in a case pattern inside `$( )`
# closes the command substitution early, and bash reports the syntax error on a
# line that looks fine.
ALLOWED_RE='^(wiki/|prototypes/(level2_build_meta\.json|signals\.json|signals_grown\.json|level2_signal_stream\.html|backlog/(backlog_manifest\.json|qc_trace\.csv))$)'
escaped=$(printf '%s\n' "$staged" | grep -vE "$ALLOWED_RE" || true)
[ -n "$escaped" ] && fail "staged paths outside the allowlist:
$escaped"

[ "$count" -gt "$MAX_STAGED_FILES" ] && \
  fail "$count staged paths exceeds the $MAX_STAGED_FILES ceiling -- this is not a normal daily run"

# --- 5b. Hold back what the run did not write, commit the rest, report --------
# The run-age guard in section 2 answers WHEN the run happened. It never answers
# WHICH files the run wrote. On any normal morning the run is a few hours old, so
# every dirty path under wiki/ is staged regardless of who wrote it.
#
# On 2026-08-05 that would have committed a concurrent session's front-door
# redesign: start_here.html had been rewritten to link what_is_saying.html, a page
# that session had not finished writing. A dead link on the wiki's entry page,
# committed under a "C2A2 daily run" subject, with the real author erased.
#
# Anything staged whose mtime is past the run's write window, and that is not a
# named post-run producer, is unstaged and held. The run's own output still gets
# committed -- refusing the whole run would strand a legitimate day's work every
# time somebody edits wiki/ in the morning.
#
# The held paths are NOT silently skipped. They are named on stdout (which lands in
# the launchd log) and appended to scheduler/held_paths.md, the same status-file
# shape check_scheduled_commits.py and check_daily_run_stall.py use, so a held path
# outlives the log line. A skip nobody can see afterwards is the failure this whole
# script exists to end.
#
# mtime is a sound signal here only because these are local writes to a live tree.
# A branch switch or fresh clone restamps everything and holds the lot -- loud, and
# correct, on a tree nobody built on purpose.
mkdir -p "$REPO/$(dirname "$HELD_STATUS_FILE")"
held_line="$(ts)  OK    nothing held; every staged path is the run's own output"
if [ -n "$RUN_START_EPOCH" ]; then
  cutoff=$(( RUN_START_EPOCH + RUN_WRITE_WINDOW_SECONDS ))
  held=""
  held_names=""
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    produced=0
    for prefix in "${POST_RUN_PRODUCERS[@]}"; do
      case "$f" in "$prefix"*) produced=1; break ;; esac
    done
    [ "$produced" -eq 1 ] && continue
    mtime=$(stat -f %m "$REPO/$f" 2>/dev/null) || continue
    if [ "$mtime" -gt "$cutoff" ]; then
      held="$held
  $f (written run+$(( (mtime - RUN_START_EPOCH) / 60 ))m)"
      held_names="$held_names $f (run+$(( (mtime - RUN_START_EPOCH) / 60 ))m)"
      git -C "$REPO" restore --staged -- "$f" 2>/dev/null || true
    fi
  done <<EOF
$(git -C "$REPO" diff --cached --name-only --diff-filter=d)
EOF
  if [ -n "$held" ]; then
    held_n=$(printf '%s\n' "$held" | grep -c . )
    log "HELD $held_n path(s) written after the run's $(( RUN_WRITE_WINDOW_SECONDS / 60 ))-minute window -- not this run's output, left in the working tree:$held"
    log "     commit them yourself, or re-run once their author is done"
    held_line="$(ts)  HELD  $held_n path(s) not written by the run:$held_names"
  else
    log "authorship check clean: every staged path predates run+$(( RUN_WRITE_WINDOW_SECONDS / 60 ))m or is a named producer"
  fi
else
  log "GUARD SKIPPED: --skip-run-check leaves no run timestamp; staged-path authorship NOT verified"
  held_line="$(ts)  SKIP  --skip-run-check: staged-path authorship not verified"
fi
[ "$DRY_RUN" -eq 0 ] && printf '%s\n' "$held_line" >> "$REPO/$HELD_STATUS_FILE"

# Holding may have emptied the index. That is a no-op, not a failure -- but the
# held report above has already been written, so it does not read as a clean tree.
staged=$(git -C "$REPO" diff --cached --name-only)
if [ -z "$staged" ]; then
  log "everything staged was held; nothing of the run's own to commit"
  log "=== commit_daily_run done (noop) ==="
  exit 0
fi
count=$(printf '%s\n' "$staged" | wc -l | tr -d ' ')
log "$count path(s) remain after the authorship check"

# --- 6. The address check ---------------------------------------------------
# The wiki is public and the agents keep regenerating files that carry Tom's
# personal address; 8 such files are already on origin. This commit is not pushed,
# but a commit is where the address becomes permanent -- history survives deletion
# of the file. Cheaper to refuse here than to rewrite history later.
if git -C "$REPO" diff --cached | grep -qi 'thomas\.loughran@gmail\.com'; then
  offenders=$(git -C "$REPO" diff --cached --name-only | while read -r f; do
    git -C "$REPO" diff --cached -- "$f" | grep -qi 'thomas\.loughran@gmail\.com' && echo "  $f"
  done)
  fail "personal address present in the staged diff:
$offenders"
fi
log "address check clean"

if [ "$DRY_RUN" -eq 1 ]; then
  log "--dry-run: would commit $count path(s); leaving them staged is not desired, resetting"
  git -C "$REPO" reset -q
  log "=== commit_daily_run done (dry run) ==="
  exit 0
fi

# --- 7. Commit. Never push. ------------------------------------------------
# The subject must keep matching check_scheduled_commits.py's '^C2A2 daily run'
# grep, or that assertion goes blind the moment this starts working.
subject="C2A2 daily run — $(date +%Y-%m-%d) (committed on the Mac; sandbox cannot write .git)"
if ! git -C "$REPO" commit -q -m "$subject"; then
  fail "git commit failed"
fi
head=$(git -C "$REPO" rev-parse --short HEAD)
log "committed $head: $count path(s)"
log "NOT pushed, by design -- a human reviews wiki content before it reaches GitHub"
log "=== commit_daily_run done ==="
exit 0

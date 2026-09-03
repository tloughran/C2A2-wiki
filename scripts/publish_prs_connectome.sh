#!/bin/bash
#
# publish_prs_connectome.sh -- gated regen-then-publish for the Narrative (PRS)
# Connectome, wiki/prs_3d.html.
#
# Runs ON THE MAC (which has git push creds). It replaces the two-stage
# arrangement -- a weekly Cowork task that regenerates but cannot push, plus a
# manual push -- with ONE job. Fewer scheduled agents, not more, and the live
# page stops being a week stale.
#
# THE CLOCK IS ONLY A POLL. Firing costs nothing when there is no work: the job
# exits at gate 2 without touching git, the vault, or the artifact. What decides
# whether work happens is the source-newer-than-artifact test, not the hour.
#
# Exit codes:
#   0 = pushed, or nothing to do (no new triplets / no diff)
#   1 = a gate failed, validation failed, or the push was rejected. On any
#       pre-commit failure NOTHING was written. On push reject the local commit
#       remains and the tree is clean-ish; re-run after `git pull --rebase`.
#
# Safety properties:
#   - Single instance: an atomic mkdir lock, so two firings can never overlap.
#   - Never force-pushes. Never `git add -A`. Commits ONE file by pathspec.
#   - Refuses to run off `main` -- deploy is origin/main, and a push to a
#     feature branch would look like success while the live site stayed stale.
#   - Waits out a held .git/index.lock rather than dying on it (the vault-sync
#     agent, the daily-run commit and the telemetry refresh all contend for it).
#   - Verifies AFTER commit that exactly one file was committed.
#
# Usage: publish_prs_connectome.sh [--dry-run]
#   --dry-run does every gate, the regen and the validation, then stops before
#   `git commit`. Use it to see what the job would do tonight.

set -uo pipefail

REPO="/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
ART="wiki/prs_3d.html"
REGEN="scripts/regen_prs_connectome.sh"
VALIDATOR="wiki/c2a2-prs-3d/scripts/validate_prs_3d.py"
EXTRACT="wiki/c2a2-prs-3d/scripts/extract_prs_data.py"
CARRY="wiki/c2a2-prs-3d/prs_pub_years.json"
TPL="wiki/c2a2-prs-3d/template_prs_3d.html"
DEPLOY_BRANCH="main"
QUIET_MINUTES=20      # a source touched more recently than this may still be mid-write
LOCKDIR="/tmp/publish_prs_connectome.lock"
LOG="$HOME/Library/Logs/c2a2-prs-connectome-publish.log"

DRYRUN=0
[ "${1:-}" = "--dry-run" ] && DRYRUN=1

ts() { date "+%Y-%m-%dT%H:%M:%S%z"; }
log() { echo "[$(ts)] $*" | tee -a "$LOG"; }
fail() { log "FAIL: $*"; log "Nothing published."; rmdir "$LOCKDIR" 2>/dev/null; exit 1; }
done_ok() { log "$*"; log "=== publish_prs_connectome done ==="; rmdir "$LOCKDIR" 2>/dev/null; exit 0; }

cd "$REPO" || { echo "repo not found: $REPO"; exit 1; }
mkdir -p "$(dirname "$LOG")"

# --- Gate 0: single instance. mkdir is atomic; macOS has no flock. ------------
if ! mkdir "$LOCKDIR" 2>/dev/null; then
  log "another publish_prs_connectome is running (lock $LOCKDIR held). Exiting."
  exit 0
fi

if [ "$DRYRUN" -eq 1 ]; then log "=== publish_prs_connectome start (DRY RUN) ==="; else log "=== publish_prs_connectome start ==="; fi

# --- Gate 1: the deploy branch. ---------------------------------------------
branch=$(git symbolic-ref --short HEAD 2>/dev/null) || fail "cannot read current branch"
[ "$branch" = "$DEPLOY_BRANCH" ] || fail \
  "on branch '$branch', not '$DEPLOY_BRANCH'. Deploy is origin/$DEPLOY_BRANCH; publishing from here would not update the live site."
log "branch OK: $branch"

for f in "$ART" "$REGEN" "$VALIDATOR" "$EXTRACT" "$CARRY" "$TPL"; do
  [ -f "$f" ] || fail "missing $f"
done

# --- Gate 2: IS THERE WORK? The logic gate the clock only polls. -------------
# Newest source mtime vs the artifact's. Sources = the vault triplet files, the
# cross/coil/findings inputs, the curated pub-year map, the template, and the
# generator itself (a generator change is work even when the vault is quiet).
art_m=$(stat -f %m "$ART")
newest=0; newest_f=""
while IFS= read -r f; do
  m=$(stat -f %m "$f")
  [ "$m" -gt "$newest" ] && { newest=$m; newest_f=$f; }
done < <(
  ls wiki/traditions/*/prs_triplets.md wiki/master/prs_triplets.md 2>/dev/null
  ls wiki/master/cross_program_index.md wiki/flags/pattern_detector_findings.md 2>/dev/null
  echo "$CARRY"; echo "$TPL"
  echo "wiki/c2a2-prs-3d/scripts/generate_prs_3d.py"; echo "$EXTRACT"
)
if [ "$newest" -le "$art_m" ]; then
  done_ok "no source newer than $ART (newest: $newest_f). Nothing to regenerate."
fi
log "work found: $newest_f is newer than $ART"

# --- Gate 3: quiet period. The daily thinker agents write ~02:11; a source -----
# touched in the last $QUIET_MINUTES may still be half-written, and half a
# markdown file parses into a plausible-looking short corpus rather than an error.
now=$(date +%s)
quiet_cut=$(( QUIET_MINUTES * 60 ))
if [ $(( now - newest )) -lt "$quiet_cut" ]; then
  done_ok "$newest_f was written $(( (now - newest) / 60 ))m ago (< ${QUIET_MINUTES}m). A writer may still be mid-file; deferring to the next run."
fi
log "quiet period OK: newest source is $(( (now - newest) / 60 ))m old"

# --- Regenerate. The script validates on a temp copy and only then overwrites. -
before=$(grep -oE '"id"[[:space:]]*:[[:space:]]*"[a-z]+-PRS-[0-9]+' "$ART" | wc -l | tr -d ' ')
regen_out=$(bash "$REGEN" "$REPO" 2>&1) || { log "$regen_out"; fail "regen failed (artifact left untouched)"; }
log "$(echo "$regen_out" | grep -E '^RESULT' || echo 'regen completed')"
after=$(grep -oE '"id"[[:space:]]*:[[:space:]]*"[a-z]+-PRS-[0-9]+' "$ART" | wc -l | tr -d ' ')

# --- Validate THE FILE ABOUT TO BE COMMITTED, not the one the generator made. -
# The standing rule here: the artifact lags its generator. Re-check on disk.
tmpdata=$(mktemp) || fail "mktemp failed"
python3 "$EXTRACT" "$REPO/wiki" --carryforward "$CARRY" --out "$tmpdata" >/dev/null 2>&1 \
  || { rm -f "$tmpdata"; fail "extract failed during post-regen validation"; }
if ! python3 "$VALIDATOR" "$ART" --source-data "$tmpdata" >>"$LOG" 2>&1; then
  rm -f "$tmpdata"; fail "validator FAILED on $ART. Artifact is on disk but NOT committed."
fi
rm -f "$tmpdata"
log "validated OK: $before -> $after triplets"

# --- Nothing to publish? (regen is deterministic; same vault = same bytes) ----
if git diff --quiet HEAD -- "$ART"; then
  done_ok "$ART is byte-identical to HEAD; nothing to publish."
fi

if [ "$DRYRUN" -eq 1 ]; then
  done_ok "DRY RUN: would commit and push $ART ($before -> $after triplets). No git write performed."
fi

# --- Commit, waiting out a held index.lock. ----------------------------------
msg="Regen PRS connectome: ${before} -> ${after} triplets (validated, automated)"
committed=0
for attempt in 1 2 3 4 5 6; do
  if commit_err=$(git commit -q -m "$msg" -- "$ART" 2>&1); then
    committed=1; break
  fi
  case "$commit_err" in
    *index.lock*)
      log "git index locked by another process (attempt $attempt/6); waiting 15s"
      sleep 15 ;;
    *"nothing to commit"*)
      done_ok "nothing to commit (raced with another publisher)." ;;
    *)
      fail "git commit failed: $commit_err" ;;
  esac
done
[ "$committed" -eq 1 ] || fail \
  "git index still locked after 6 attempts (90s). Another process holds $REPO/.git/index.lock. NOT pushed."

# --- Verify the commit touched exactly the one file. -------------------------
changed=$(git show --name-only --pretty=format: HEAD | grep -v '^$' | sort)
if [ "$changed" != "$ART" ]; then
  fail "commit touched unexpected files -- NOT pushing. Committed: $(echo "$changed" | tr '\n' ' ')"
fi
log "commit scope OK: $changed"

# --- Push. Never force. ------------------------------------------------------
if ! git push origin "$DEPLOY_BRANCH" >>"$LOG" 2>&1; then
  fail "push rejected (likely non-fast-forward; origin moved). Commit is LOCAL. Run 'git pull --rebase' on the Mac, then re-run. NOT force-pushing."
fi

done_ok "PUBLISHED: ${before} -> ${after} triplets, pushed to origin/$DEPLOY_BRANCH."

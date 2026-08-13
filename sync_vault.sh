#!/usr/bin/env bash
# sync_vault.sh — Syncs Summa 2026 vault data into C2A2-wiki and pushes to GitHub Pages.
#
# Run manually:  bash sync_vault.sh
# Scheduled by:  ~/Library/LaunchAgents/com.tloughran.summa-vault-sync.plist  (daily 21:00)
#
# Efficiency: rsync --checksum copies only files whose content has changed.
# Cost: commits and pushes only when something actually changed.
#
# Pipeline (agent handoff):
#   Progress agent adds new Day-NNN transcript + synthesis to Summa 2026 vault
#   → this script rsyncs them into wiki/vault/
#   → build_index.py (canonical, in the Summa vault) rebuilds summa_index.json
#     from _index/Days.md + the Leonine/Supplement skeleton, then we copy it
#     forward into wiki/vault/refs/
#   → git commit + push makes them live on GitHub Pages

set -euo pipefail

SUMMA="$HOME/Documents/Claude/Projects/Summa 2026 in a Year/vault"
WIKI="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/vault"
REPO="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project"
BUILD_INDEX="$SUMMA/refs/build_index.py"   # canonical index builder (Days.md-aware, Supplement-aware)
LOG="$REPO/sync_vault.log"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }

# Fail LOUD, not into a logfile nobody reads. Writes a marker file AND fires a
# macOS notification. Rationale (2026-07-20): pushes had been rejected since
# 2026-05-11 — 24 failures — and the only signal was a line in sync_vault.log.
# Two weeks of vault content sat unpublished because nothing surfaced it.
FAIL_MARKER="$REPO/sync_vault.FAILED"
fail_loud() {
  log "SYNC FAILED — $1"
  printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1" > "$FAIL_MARKER"
  osascript -e "display notification \"$1\" with title \"Summa vault sync FAILED\"" 2>/dev/null || true
  exit 1
}

log "=== Summa vault sync started ==="

# ── 1. Sync transcript and synthesis files (content-checksummed) ─────────────
rsync -a --checksum --delete \
  "$SUMMA/transcripts/" "$WIKI/transcripts/" \
  2>>"$LOG"

rsync -a --checksum --delete \
  "$SUMMA/synthesis/"  "$WIKI/synthesis/" \
  2>>"$LOG"

log "rsync complete"

# ── 2. Build the canonical index (single source of truth) ────────────────────
# build_index.py is the ONE index builder: it parses _index/Days.md + the
# hardcoded Leonine/Supplement skeleton and scans the vault for availability
# (including Supplementum Q.1-99). reindex_vault.py is RETIRED — it lacked
# Supplement coverage and over-claimed availability, disagreeing with
# build_index and ping-ponging via the old wiki→summa back-copy. We build in
# the Summa vault (where Days.md lives), then copy FORWARD into wiki/ so the
# data direction is uniformly Summa → wiki.
log "Building canonical index (build_index.py)…"
python3 "$BUILD_INDEX" --vault "$SUMMA" 2>>"$LOG" | tee -a "$LOG"
cp "$SUMMA/refs/summa_index.json" "$WIKI/refs/summa_index.json"
cp "$SUMMA/refs/index_summary.md" "$WIKI/refs/index_summary.md"
log "Canonical index built in Summa, copied → wiki"

# ── 2. Commit and push only if git sees changes ──────────────────────────────
cd "$REPO"

# Wait out a HELD git lock; clear only a genuinely ABANDONED one.
#
# This block used to `rm -f` all three locks unconditionally, justified as: "safe to
# remove here: this script is the only scheduled writer of wiki/vault/, runs
# single-threaded." That is true about wiki/vault/ and FALSE about the lock —
# .git/index.lock is REPO-GLOBAL, and owning wiki/vault/ says nothing about who
# holds it. Sandboxed scheduled runs bind-mount this repo at /sessions/<name>/mnt/
# and reach this same .git; their transcripts carry 102 "Unable to create
# .../.git/index.lock: File exists" and 12 HEAD.lock collisions. Removing a lock a
# live git still holds kills that process mid-write, which strands its half-written
# .git/objects/**/tmp_obj_* — 535 accumulated 2026-07-31..08-13 with nothing
# reporting it (now watched by check_scheduler_health.py's git-debris verdict).
#
# The rm existed for a real reason too, and that reason is kept: a crashed daily-run
# left a 0-byte HEAD.lock that blocked this script for ~17h with no visible error
# (2026-07-20), and before that a held lock silently dropped the 2026-06-18 push. So
# BOTH properties have to hold — never steal a live lock, still clear a dead one.
#
# Held vs abandoned is decided by lsof, not by age alone: git holds the lock file
# OPEN from creation until it commits or rolls back, so a lock no process has open is
# one nobody is using. The age floor is belt-and-suspenders against a lock created in
# the instant between our two checks. Waiting rather than stealing is the pattern
# scripts/publish_metabolism.sh:122 already uses against this same contention (6x15s);
# that one is the more recent and more tested of the two, so this follows it.
#
# Bash 3.2 (launchd runs /bin/bash): no arrays here on purpose — `"${arr[@]}"` on an
# empty array is an unbound-variable error under `set -u` in 3.2.
GIT_LOCKS="$REPO/.git/index.lock
$REPO/.git/HEAD.lock
$REPO/.git/refs/heads/main.lock"

# Overridable so the failure paths can actually be driven by a test. A guard nobody
# has watched fail is not a guard, and 6x15s of real sleep makes a test nobody runs.
GIT_LOCK_ATTEMPTS="${GIT_LOCK_ATTEMPTS:-6}"
GIT_LOCK_WAIT_SECS="${GIT_LOCK_WAIT_SECS:-15}"
GIT_LOCK_STALE_AGE="${GIT_LOCK_STALE_AGE:-300}"

# Absolute path, because this script sets no PATH and launchd's default is not the
# shell's. lsof lives in /usr/sbin, which a Terminal run finds and a stripped
# environment might not.
LSOF="${LSOF:-/usr/sbin/lsof}"

# `|| true` is load-bearing twice over: lsof exits 1 when nothing holds the file, and
# `set -o pipefail` would otherwise propagate that through the pipe and `set -e` would
# kill the script — which is exactly how publish_metabolism died silently on 08-09.
#
# If lsof is missing we CANNOT tell held from abandoned, so we say "unknown" and the
# caller treats that as held. Returning empty would be the old bug restored by the
# back door: every lock would look abandoned and get stolen. An unusable detector must
# fail toward not-touching-anything.
lock_holder() {
  if [ ! -x "$LSOF" ]; then
    echo "unknown-no-lsof"
    return 0
  fi
  "$LSOF" -t -- "$1" 2>/dev/null | tr '\n' ' ' || true
}

lock_age() {
  local now mt
  now=$(date +%s)
  mt=$(stat -f %m "$1" 2>/dev/null || echo "$now")
  echo $(( now - mt ))
}

wait_for_git_locks() {
  local attempt lock present held ripe holder n
  attempt=1
  while [ "$attempt" -le "$GIT_LOCK_ATTEMPTS" ]; do
    present=""; held=""; ripe=1
    while IFS= read -r lock; do
      [ -n "$lock" ] || continue
      [ -e "$lock" ] || continue
      present="$present$lock
"
      holder=$(lock_holder "$lock")
      if [ -n "$holder" ]; then
        held="$held $(basename "$lock")(pid ${holder% })"
      elif [ "$(lock_age "$lock")" -lt "$GIT_LOCK_STALE_AGE" ]; then
        ripe=0
      fi
    done <<EOF
$GIT_LOCKS
EOF

    [ -z "$present" ] && return 0

    n=$(printf '%s' "$present" | grep -c . || true)
    if [ -n "$held" ]; then
      log "git lock HELD by a live process:$held — waiting ${GIT_LOCK_WAIT_SECS}s (attempt $attempt/$GIT_LOCK_ATTEMPTS)"
    elif [ "$ripe" -eq 1 ]; then
      # Nothing holds them and they are old enough to be certain. This is the
      # 17h-HEAD.lock case, and it is the ONLY case that may remove a lock.
      log "clearing $n ABANDONED git lock(s) — no process holds them, age >= ${GIT_LOCK_STALE_AGE}s:"
      while IFS= read -r lock; do
        [ -n "$lock" ] || continue
        log "  removed $(basename "$lock") (age $(lock_age "$lock")s)"
        rm -f "$lock"
      done <<EOF
$present
EOF
      return 0
    else
      log "git lock present with no holder but younger than ${GIT_LOCK_STALE_AGE}s — too soon to call it abandoned; waiting ${GIT_LOCK_WAIT_SECS}s (attempt $attempt/$GIT_LOCK_ATTEMPTS)"
    fi
    sleep "$GIT_LOCK_WAIT_SECS"
    attempt=$(( attempt + 1 ))
  done

  # Still locked after the full wait. Refusing is the point: committing here would
  # mean having stolen the lock, and stealing is what stranded the objects.
  held=""
  while IFS= read -r lock; do
    [ -n "$lock" ] || continue
    [ -e "$lock" ] && held="$held $(basename "$lock")(holder: $(lock_holder "$lock"))"
  done <<EOF
$GIT_LOCKS
EOF
  fail_loud "git lock still present after $(( GIT_LOCK_ATTEMPTS * GIT_LOCK_WAIT_SECS ))s:$held. Another git process is mid-write — NOT stealing the lock. Nothing committed, nothing pushed."
}

wait_for_git_locks

# Refuse to run unless the working tree is actually on main. This script commits
# to the CHECKED-OUT branch but pushes `origin main` — on a feature branch that
# silently strands vault commits where they will never publish (exactly what
# happened 2026-07-19). Guard added 2026-07-20 alongside branch-based dev.
BRANCH=$(git symbolic-ref --short HEAD 2>/dev/null || echo "DETACHED")
if [ "$BRANCH" != "main" ]; then
  fail_loud "working tree is on '$BRANCH', not main — refusing to commit vault changes onto a non-main branch. Check out main (or use a worktree for feature work) and re-run."
fi

if git diff --quiet HEAD -- wiki/vault/ 2>/dev/null && \
   git ls-files --others --exclude-standard wiki/vault/ | grep -q .; then
  : # new untracked files exist — fall through to commit
elif git diff --quiet HEAD -- wiki/vault/ 2>/dev/null; then
  log "No changes in vault/ — nothing to push."
  log "=== Done ==="
  exit 0
fi

# Count what changed for a useful commit message
CHANGED=$(git diff --name-only HEAD -- wiki/vault/ 2>/dev/null; \
          git ls-files --others --exclude-standard wiki/vault/ 2>/dev/null)
N=$(echo "$CHANGED" | grep -c . || true)

git add wiki/vault/

DATE=$(date '+%Y-%m-%d')
# Commit ONLY wiki/vault/ — never a bare `git commit` here. The working tree can
# carry unrelated pre-staged changes (e.g. the architecture/ pathway set); a bare
# commit would sweep all of them into this push. --only restricts the commit to the
# vault paths regardless of what else is staged. (Hardened 2026-05-19.)
git -c user.name="Tom Loughran" \
    -c user.email="thomas.loughran@gmail.com" \
    commit --only -m "Summa vault sync ${DATE} (${N} file(s) updated)" -- wiki/vault/

log "Committed ${N} change(s). Pushing…"

# Reconcile BEFORE pushing. origin/main advances independently of this Mac — the
# heartbeat GitHub Action commits data-only straight to main — so a local-only
# push is rejected as non-fast-forward. Without a pull that rejection was silent
# and cost two weeks of unpublished vault content (2026-07-06 → 07-19).
# Risk is bounded: fetch/rebase are read-then-replay, any conflict aborts cleanly
# and leaves the local commit intact, and we NEVER force-push.
# >>> RECONCILE-BLOCK (extracted verbatim by scripts/test_sync_vault_rebase.sh — keep both markers)
if ! git fetch origin main >>"$LOG" 2>&1; then
  fail_loud "git fetch failed (network or credentials) — local commit kept, nothing pushed"
fi

# --autostash added 2026-08-03. Without it `git pull --rebase` REFUSES OUTRIGHT whenever the
# working tree carries unstaged changes to tracked files ("cannot pull with rebase: You have
# unstaged changes"). This tree is dirty most nights from agent output, so that is the normal
# state, not an edge case — the 2026-07-23 run died exactly there, and every earlier success
# was luck. --autostash stashes those changes, rebases, then restores them.
PULL_OUT=$(mktemp "${TMPDIR:-/tmp}/sync_vault_pull.XXXXXX")
if git pull --rebase --autostash origin main >"$PULL_OUT" 2>&1; then
  cat "$PULL_OUT" >>"$LOG"
  rm -f "$PULL_OUT"
  # git EXITS 0 when the rebase succeeds but restoring the autostash conflicts — it prints
  # "Applying autostash resulted in conflicts" and returns success anyway (verified
  # 2026-08-03). That leaves conflict markers in tracked files and the changes stranded in
  # `git stash list`. Unpushed and unsaid, the next daily run would commit the markers.
  # An unmerged index is the sound test for it.
  if [ -n "$(git ls-files --unmerged)" ]; then
    fail_loud "rebase succeeded but restoring the working-tree changes conflicted — the tree now has unmerged files and the changes are in 'git stash list'. Nothing pushed. Resolve manually in $REPO"
  fi
else
  cat "$PULL_OUT" >>"$LOG"
  # Name what actually happened. The old code called EVERY failure here a conflict, so on
  # 2026-07-23 the marker file read "rebase onto origin/main conflicted" when no rebase had
  # even started. A wrong diagnosis in a marker file is worse than no marker.
  if [ -d "$REPO/.git/rebase-merge" ] || [ -d "$REPO/.git/rebase-apply" ]; then
    git rebase --abort >>"$LOG" 2>&1 || true
    rm -f "$PULL_OUT"
    fail_loud "rebase onto origin/main conflicted and was aborted — local commit kept, nothing pushed. Resolve manually in $REPO"
  else
    WHY=$(tr '\n' ' ' <"$PULL_OUT" | tr -d '"\\' | tail -c 200)
    rm -f "$PULL_OUT"
    fail_loud "git pull --rebase never started a rebase — local commit kept, nothing pushed. git said: $WHY"
  fi
fi
# <<< RECONCILE-BLOCK

if git push origin main >>"$LOG" 2>&1; then
  log "Push succeeded."
  rm -f "$FAIL_MARKER"
else
  fail_loud "push rejected even after rebase — NOT force-pushing. Run 'git push origin main' manually from $REPO"
fi

log "=== Done ==="

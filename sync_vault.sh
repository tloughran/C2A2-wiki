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

# Clear stale git locks before any git write. A crashed/interrupted git process
# (or a sandbox run that couldn't unlink) leaves .git/index.lock behind, which
# aborts the commit with "Unable to create index.lock: File exists" — exactly
# the failure that silently dropped the 2026-06-18 push. Safe to remove here:
# this script is the only scheduled writer of wiki/vault/, runs single-threaded.
rm -f "$REPO/.git/index.lock" "$REPO/.git/refs/heads/main.lock" 2>/dev/null || true

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

git push origin main >>"$LOG" 2>&1 && log "Push succeeded." || {
  log "Push FAILED — run 'git push origin main' manually from $REPO"
  exit 1
}

log "=== Done ==="

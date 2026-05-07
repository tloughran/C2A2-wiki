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
#   → reindex_vault.py scans frontmatter and marks new days available=true in summa_index.json
#   → git commit + push makes them live on GitHub Pages

set -euo pipefail

SUMMA="$HOME/Documents/Claude/Projects/Summa 2026 in a Year/vault"
WIKI="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/vault"
REPO="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project"
REINDEX="$REPO/scripts/reindex_vault.py"
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

# ── 2. Reindex: scan vault files → update summa_index.json availability ───────
# This is the agent handoff point: the progress pipeline adds new Day-NNN files;
# reindex_vault.py detects them via frontmatter and activates them in the index.
log "Running reindex_vault.py…"
python3 "$REINDEX" "$WIKI" 2>>"$LOG" | tee -a "$LOG"

# Also copy the updated index back to the source Summa vault for consistency
cp "$WIKI/refs/summa_index.json" "$SUMMA/refs/summa_index.json"
log "Index synced back to source vault"

# ── 2. Commit and push only if git sees changes ──────────────────────────────
cd "$REPO"

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
git -c user.name="Tom Loughran" \
    -c user.email="thomas.loughran@gmail.com" \
    commit -m "Summa vault sync ${DATE} (${N} file(s) updated)"

log "Committed ${N} change(s). Pushing…"

git push origin main >>"$LOG" 2>&1 && log "Push succeeded." || {
  log "Push FAILED — run 'git push origin main' manually from $REPO"
  exit 1
}

log "=== Done ==="

#!/usr/bin/env bash
# Checkpoint commit script — run once from Terminal on the Mac.
# Commits the current state of the repo on main, tags it as a known-good
# checkpoint, then branches to `narration-modular` for the rebuild.
#
# Usage:
#   cd ~/Documents/Claude/Projects/RC\ Karpathy\ Wiki\ Project
#   bash checkpoint-commit.sh
#
# This script is LOCAL ONLY — it does NOT push to GitHub.
# Push manually after confirming the remote is private.

set -e
cd "$(dirname "$0")"

echo "=== Current state ==="
git branch --show-current
echo "Dirty files: $(git status --short | wc -l)"
echo ""

# Clean stale git lock if present (harmless if missing)
rm -f .git/index.lock

# Stop tracking files that should now be ignored
git rm --cached -q .DS_Store 2>/dev/null || true
git rm --cached -q "wiki/.DS_Store" 2>/dev/null || true
git rm --cached -q "wiki/.obsidian/workspace.json" 2>/dev/null || true
git rm --cached -q "wiki/.obsidian/graph.json" 2>/dev/null || true

# Stage everything respecting the new .gitignore
git add -A

echo "=== Staged for commit ==="
echo "Files: $(git diff --cached --name-only | wc -l)"
git diff --cached --stat | tail -3
echo ""

# Commit
git commit -m "Narration visualization checkpoint + content expansion since 2026-04-08

- Added wiki_narration.html: D3 force-graph visualization of 314 files
  across 11 traditions, with date-indexed History tour, brightness slider,
  Play/Pause/Speed controls, and pluggable TTS (browser voice by default,
  OpenAI tts-1-hd when API key provided in settings)
- ~110 new inbox proposals processed through pending -> approved/denied
- 6 daily review HTML pages generated (2026-04-07 through 2026-04-16)
- Updated all 11 agent profiles; expanded traditions/, architecture/,
  flags/, decisions/
- Added .gitignore (macOS, Obsidian workspace, claude-mem nested repo,
  Python/Node build artifacts, secrets)

This is a known-good checkpoint. Next: refactor narration from single
HTML file into modular JS + JSON data + build step, on branch
narration-modular."

# Tag the checkpoint so we can always get back to this exact state
git tag -a v4-narration-checkpoint -m "Working single-file narration HTML — frozen before modular rebuild"

# Branch off for the modular rebuild
git checkout -b narration-modular

echo ""
echo "=== Done ==="
git log --oneline -3
echo ""
echo "Currently on branch: $(git branch --show-current)"
echo "Tag on main: v4-narration-checkpoint"
echo ""
echo "Nothing has been pushed to GitHub. Verify the remote is private"
echo "before pushing:"
echo "  git remote -v"
echo "  # (if private and you want to back up): git push origin main --tags"

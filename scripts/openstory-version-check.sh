#!/bin/bash
# OpenStory weekly upstream-version check (report only — never mutates the repo).
set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="$HOME/Documents/Non-Claude Projects/OpenStory"
REPORT_DIR="$HOME/Documents/Claude/Scheduled/openstory-version-check/reports"
mkdir -p "$REPORT_DIR"
STAMP="$(date +%Y-%m-%d_%H%M)"
REPORT="$REPORT_DIR/report-$STAMP.md"
LATEST="$REPORT_DIR/latest.md"

if [ ! -d "$REPO/.git" ]; then
  echo "# OpenStory check $STAMP" > "$LATEST"
  echo "ERROR: repo not found at $REPO" >> "$LATEST"
  cp "$LATEST" "$REPORT"
  echo "$(date '+%F %T') ERROR repo-not-found"
  exit 1
fi

cd "$REPO" || exit 1
git fetch origin --quiet 2>&1 || echo "WARN: git fetch reported an error (see above)"

CUR=$(git log -1 --format="%h %s (%ci)" HEAD 2>&1)
BEHIND=$(git rev-list --count HEAD..origin/master 2>/dev/null || echo "?")
NEW=$(git log HEAD..origin/master --oneline 2>/dev/null | head -30)
VER=$(grep '^version' rs/Cargo.toml 2>/dev/null | head -1)
DIRTY=$(git status --porcelain 2>/dev/null)

{
  echo "# OpenStory upstream check — $STAMP"
  echo
  echo "**Current commit:** $CUR"
  echo
  echo "**Behind origin/master:** $BEHIND commits"
  echo
  echo "**rs/Cargo.toml:** ${VER:-unknown}"
  echo
  if [ -n "$DIRTY" ]; then
    echo "**Local uncommitted / untracked changes (would affect a pull):**"
    echo '```'
    echo "$DIRTY"
    echo '```'
  else
    echo "**Working tree:** clean"
  fi
  echo
  if [ "$BEHIND" != "0" ] && [ "$BEHIND" != "?" ]; then
    echo "**New upstream commits (newest 30):**"
    echo '```'
    echo "$NEW"
    echo '```'
    echo
    echo "Suggested next step:"
    echo '```'
    echo "cd \"$REPO\" && git pull && just up-no-mongo"
    echo '```'
  else
    echo "Up to date with origin/master."
  fi
} > "$REPORT"
cp "$REPORT" "$LATEST"

# macOS notification when behind (best-effort; ignored if it fails)
if [ "$BEHIND" != "0" ] && [ "$BEHIND" != "?" ]; then
  /usr/bin/osascript -e "display notification \"$BEHIND commits behind master — see latest.md\" with title \"OpenStory version check\"" 2>/dev/null || true
fi

echo "$(date '+%F %T') OK behind=$BEHIND ver=${VER:-?}"

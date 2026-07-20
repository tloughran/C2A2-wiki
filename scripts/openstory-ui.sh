#!/usr/bin/env bash
# openstory-ui.sh — OpenStory Vite dashboard, supervised by launchd
# (com.tomloughran.openstory.ui, RunAtLoad + KeepAlive). Foreground via exec so
# launchd restarts it if it dies. The UI is optional for the wiki feed (that's the
# backend's job); this just keeps the dashboard at http://localhost:5173. 2026-06-25.
set -euo pipefail
export PATH="/opt/homebrew/bin:$HOME/.cargo/bin:$PATH"
cd "$HOME/Documents/Non-Claude Projects/OpenStory/ui"
exec npm run dev

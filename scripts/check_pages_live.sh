#!/bin/bash
# check_pages_live.sh -- launchd entry for scripts/check_pages_live.py.
# /bin/bash wrapper, never python3 directly: TCC grants ~/Documents per
# executable, and the bash road is the one known to work under launchd
# (see check_scheduled_commits.sh). Exit codes pass through unchanged:
# 0 OK/WARN | 3 FAIL verdict | 2 cannot reach GitHub | 1 script error.
set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] pages-live check"
python3 "$REPO/scripts/check_pages_live.py" "$@"

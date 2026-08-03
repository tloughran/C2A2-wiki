#!/bin/bash
# launchd wrapper for generate_weekly_review.py.
#
# Same TCC trap as scripts/check_scheduled_commits.sh -- read that file's header
# for the full explanation. Short version: macOS gates ~/Documents read access
# per-executable, /usr/bin/python3 does not hold it under launchd, and
# com.tloughran.summa-weekly-review pointed straight at it. Every run since at
# least 2026-07-19 died with
#
#   can't open file '.../scripts/generate_weekly_review.py': [Errno 1] Operation not permitted
#
# and weekly_review.log is nothing but that line repeated. /bin/bash holds the
# grant and TCC attributes a child to its responsible parent, so python3 started
# from here reads the file fine.
#
# The script is report-only: it writes an HTML page under wiki/review/ and
# neither commits, pushes, nor sends anything.
set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project"
cd "$REPO" || { echo "$(date '+%F %T') ERROR repo-not-found: $REPO"; exit 1; }

python3 scripts/generate_weekly_review.py
RC=$?

echo "$(date '+%F %T') generate_weekly_review exit=$RC"
exit $RC

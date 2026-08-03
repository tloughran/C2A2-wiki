#!/bin/bash
# launchd wrapper for check_scheduled_commits.py.
#
# Why this exists rather than pointing the plist straight at python3:
# macOS TCC gates read access to ~/Documents per-executable, and
# /usr/bin/python3 (the CommandLineTools shim) is not granted it under launchd.
# The plist's original ProgramArguments -- python3 + the .py path -- failed every
# scheduled run with
#
#   can't open file '.../scripts/check_scheduled_commits.py': [Errno 1] Operation not permitted
#
# and wrote nothing, silently, for two days. /bin/bash IS granted, and TCC
# attributes a child process to the responsible parent, so invoking python3 from
# a bash script reads the same files fine. Every other working launchd agent in
# this repo (openstory-*, metabolism-publish) already uses exactly this shape;
# this one was the exception, which is why it was the one that broke.
#
# Running the .py by hand from a Terminal shell does NOT exercise this path --
# the shell has its own grant. The only real test is `launchctl kickstart`.
set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project"
cd "$REPO" || { echo "$(date '+%F %T') ERROR repo-not-found: $REPO"; exit 1; }

python3 scripts/check_scheduled_commits.py --status-file scheduler/commit_check.md
RC=$?

echo "$(date '+%F %T') check_scheduled_commits exit=$RC"
exit $RC

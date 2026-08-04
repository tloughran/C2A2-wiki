#!/bin/bash
# launchd wrapper for the two daily-run assertions.
#
# Runs BOTH checks, because they answer different questions about the same run and
# both feed the 06:00 morning report:
#
#   check_scheduled_commits.py  -- did the run's output get committed?  (the aftermath)
#   check_daily_run_stall.py    -- did the run finish at all, and if not, which tool
#                                  was it left waiting on?  (39 of 110 runs did not)
#
# They share one launchd agent on purpose. Every silent-failure incident in this repo
# has been a launchd job that died with nothing said about it, so a second agent is a
# second surface for exactly that; one job, one log, two verdicts is fewer places to
# go quiet. Each writes its own status file so neither can overwrite the other's line.
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
RC_COMMIT=$?
echo "$(date '+%F %T') check_scheduled_commits exit=$RC_COMMIT"

# Deliberately not short-circuited on the line above: a run that committed nothing is
# usually a run that also never finished, and the stall verdict is the one that names
# the blocking tool. Skipping it on the first failure would suppress the diagnosis
# precisely when it is needed.
python3 scripts/check_daily_run_stall.py --status-file scheduler/run_stall.md
RC_STALL=$?
echo "$(date '+%F %T') check_daily_run_stall exit=$RC_STALL"

[ "$RC_COMMIT" -ne 0 ] && exit "$RC_COMMIT"
exit "$RC_STALL"

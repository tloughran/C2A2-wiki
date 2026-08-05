#!/bin/bash
# launchd wrapper for the daily scheduler work: one action, then three assertions.
#
#   commit_daily_run.sh         -- commit what the sandboxed run could not. THE ONLY
#                                  STEP HERE THAT WRITES. Never pushes.
#
#   check_scheduled_commits.py  -- did the run's output get committed?  (the aftermath)
#   check_daily_run_stall.py    -- did the run finish at all, and if not, which tool
#                                  was it left waiting on?  (39 of 110 runs did not)
#   check_scheduler_health.py   -- did every OTHER job fire at all, survive, and leave
#                                  a dated artifact?  The two above watch one task;
#                                  this one watches all 70 registry tasks and all 11
#                                  launchd agents. It has to live here rather than in
#                                  the 07:00 scheduler-health-check task, because the
#                                  registry is under ~/Library and the scheduled tasks
#                                  only ever mount ~/Documents -- the same reason
#                                  check_scheduled_commits.py is here.
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

# Runs FIRST, and it is the only step here that writes anything. The daily run
# finishes ~04:41 having done all its work and then reports "Phase 6 BLOCKED --
# sandbox cannot write .git objects. Must run on Mac." This is the Mac. Doing it
# before the assertions means check_scheduled_commits.py below sees today's commit
# rather than failing on a thing the sandbox is structurally unable to do; and if
# this step refuses, that check fails right afterwards and says so.
#
# It commits. It never pushes -- wiki content reaches GitHub only past a human.
bash scripts/commit_daily_run.sh
RC_DAILY=$?
echo "$(date '+%F %T') commit_daily_run exit=$RC_DAILY"

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

# --quiet, because this one sweeps 70 tasks and 11 agents; the OK lines would bury
# the two above in the shared log. The status file gets the same non-OK lines plus a
# counted summary, and the 07:00 scheduler-health-check task reads that.
python3 scripts/check_scheduler_health.py --quiet --status-file scheduler/scheduler_health.md
RC_HEALTH=$?
echo "$(date '+%F %T') check_scheduler_health exit=$RC_HEALTH"

# First nonzero wins the agent's exit code. Not short-circuited above: a run that
# committed nothing is usually a run that also never finished, and the later checks
# are the ones that name the cause. Skipping them on the first failure would
# suppress the diagnosis precisely when it is needed.
[ "$RC_DAILY" -ne 0 ] && exit "$RC_DAILY"
[ "$RC_COMMIT" -ne 0 ] && exit "$RC_COMMIT"
[ "$RC_STALL" -ne 0 ] && exit "$RC_STALL"
exit "$RC_HEALTH"

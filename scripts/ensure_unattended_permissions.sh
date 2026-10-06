#!/bin/bash
# launchd wrapper for ensure_unattended_permissions.py — see that file for what the
# job is and why it has to poll rather than run at a scheduled time.
#
# Why bash and not python3 in the plist: macOS TCC gates read access to ~/Documents
# per-executable. /usr/bin/python3 does not hold the grant under launchd, so it
# cannot even open a .py that lives in this repo — it fails with
#   can't open file '.../scripts/*.py': [Errno 1] Operation not permitted
# and writes nothing at all. /bin/bash holds it, and TCC attributes the child to the
# responsible parent. This is rule 1 in scripts/launchd/README.md; it has already
# killed two agents in this repo.
#
# Running the .py from a Terminal shell does NOT exercise this path — the shell has
# its own grant. The only real test is `launchctl kickstart`.
set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project"
cd "$REPO" || { echo "$(date '+%F %T') ERROR repo-not-found: $REPO"; exit 1; }

python3 scripts/ensure_unattended_permissions.py
RC=$?

# 75 (EX_TEMPFAIL) is the normal steady state, not a fault: the fields are missing
# and the Claude desktop app is up, so there was nothing safe to do. It is reported
# as 0 here so launchd's own failure accounting stays meaningful — a nonzero exit
# from this agent means the patcher actually broke. The panel, not this exit code,
# is what says the fields are missing: check_scheduler_health.py asserts them
# against the live registry and turns red regardless of what this job managed.
[ "$RC" -eq 75 ] && exit 0
exit "$RC"

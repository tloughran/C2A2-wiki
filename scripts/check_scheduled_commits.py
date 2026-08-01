#!/usr/bin/env python3
"""Assert that scheduled tasks which are supposed to commit actually committed.

Why this exists
---------------
On 2026-08-01 `c282-wiki-agent-daily-run` ran at 04:34 EDT, produced a full day of
wiki output, and committed nothing. Nothing said so. The output sat in the working
tree while `git log` showed the last daily run as 2026-07-31 -- and the run before
that had crashed at commit time, leaving stale `.git` locks that blocked every
write in the repo for 37 hours before a human happened to notice.

The task's own exit status is not reachable from here: these tasks live in the
Claude *desktop app* registry

    ~/Library/Application Support/Claude/<account>/<workspace>/scheduled-tasks.json

which records only `lastRunAt` -- no exit code, no log, no output path. So we do
not ask the runner whether it succeeded. We check the artifact it was supposed to
leave behind, which is the only evidence that cannot lie about itself. Same
principle as the OpenStory ingest watchdog: assert against the source, not against
a liveness signal. See memory `liveness-is-not-progress`.

Where it has to run
-------------------
On the Mac, not in a task sandbox. The registry lives under `~/Library`, and the
scheduled tasks only ever mount `~/Documents` -- so none of them can read it,
including `morning-system-health`, which is the thing that reports this. Hence
`--status-file`: this runs on the Mac via launchd, writes one line into the repo,
and the morning report reads that line the same way it already reads the janitor's
findings and the OpenStory refresh status.

Usage
-----
    python3 scripts/check_scheduled_commits.py            # check, exit 1 on failure
    python3 scripts/check_scheduled_commits.py --quiet    # only print failures
    python3 scripts/check_scheduled_commits.py --status-file scheduler/commit_check.md
"""

import argparse
import glob
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone

REGISTRY_GLOB = os.path.expanduser(
    "~/Library/Application Support/Claude/*/*/*/scheduled-tasks.json"
)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# task id -> what it must have committed, and how long after a run we allow.
#
# grace_hours is measured from lastRunAt, and must exceed the task's own runtime
# (the daily run takes ~5 min) plus any slack you want before it screams. It is
# NOT the schedule interval -- a daily task that ran 20h ago and never committed
# is already broken; waiting another 4h to say so helps nobody.
#
# 1h is also what lets this be useful at all: the daily run starts 04:30 and ends
# ~04:40, so the verdict is final by 05:40 and the 06:00 morning report can carry
# it the same morning rather than a day late.
CHECKS = [
    {
        "task_id": "c282-wiki-agent-daily-run",
        "grep": "^C2A2 daily run",
        "grace_hours": 1,
        "note": "taskId carries a c282/c2a2 typo baked in; do not rename",
    },
]


def load_registry_tasks():
    """Every scheduled task the desktop app knows about, across all accounts.

    Returns (tasks_by_id, registry_paths). A task id present in more than one
    account wins on most-recent lastRunAt -- two accounts genuinely can hold the
    same id, and the one that actually ran is the one we care about.
    """
    paths = sorted(glob.glob(REGISTRY_GLOB))
    by_id = {}
    for path in paths:
        try:
            with open(path) as fh:
                tasks = json.load(fh).get("scheduledTasks", [])
        except (OSError, ValueError) as exc:
            # A registry we cannot read is a failure, not a zero-task account.
            print(f"FAIL  cannot read registry {path}: {exc}", file=sys.stderr)
            raise SystemExit(2)
        for task in tasks:
            tid = task.get("id")
            if not tid:
                continue
            prior = by_id.get(tid)
            if prior is None or (task.get("lastRunAt") or "") > (prior.get("lastRunAt") or ""):
                by_id[tid] = task
    return by_id, paths


def parse_iso(stamp):
    """Registry stamps are ISO-8601 with a trailing Z."""
    return datetime.fromisoformat(stamp.replace("Z", "+00:00"))


def last_commit_at(pattern):
    """UTC time of the newest commit whose subject matches, or None."""
    out = subprocess.run(
        ["git", "-C", REPO, "log", "-1", "--format=%cI", f"--grep={pattern}", "--all"],
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        print(f"FAIL  git log failed: {out.stderr.strip()}", file=sys.stderr)
        raise SystemExit(2)
    stamp = out.stdout.strip()
    return parse_iso(stamp).astimezone(timezone.utc) if stamp else None


def check(spec, tasks, quiet):
    """Return (ok, one_line_verdict). The line is what the morning report reads."""
    tid = spec["task_id"]
    task = tasks.get(tid)

    def say(ok, line, detail=""):
        if not ok or not quiet:
            print(("OK    " if ok else "FAIL  ") + line + detail)
        return ok, ("OK   " if ok else "FAIL ") + line

    # Absent is a failure, not a pass. A task that vanished from the registry
    # stops producing output just as thoroughly as one that errors.
    if task is None:
        return say(False, f"{tid}: not in any registry — deleted, or the registry moved")

    if not task.get("enabled", False):
        return say(True, f"{tid}: disabled in the registry")

    if not task.get("lastRunAt"):
        return say(False, f"{tid}: enabled but has never run")

    ran = parse_iso(task["lastRunAt"]).astimezone(timezone.utc)
    now = datetime.now(timezone.utc)
    deadline = ran + timedelta(hours=spec["grace_hours"])

    # Still inside the grace window: the run may legitimately be mid-flight.
    if now < deadline:
        age = (now - ran).total_seconds() / 60
        return say(True, f"{tid}: ran {age:.0f}m ago, still within "
                         f"{spec['grace_hours']}h grace")

    committed = last_commit_at(spec["grep"])
    if committed is not None and committed >= ran - timedelta(minutes=10):
        return say(True, f"{tid}: ran {ran:%Y-%m-%d %H:%M}Z, committed "
                         f"{committed:%Y-%m-%d %H:%M}Z")

    seen = f"{committed:%Y-%m-%d %H:%M}Z" if committed else "never"
    return say(
        False,
        f"{tid}: ran {ran:%Y-%m-%d %H:%M}Z "
        f"({(now - ran).total_seconds() / 3600:.1f}h ago) and committed nothing; "
        f"newest commit matching {spec['grep']!r} is {seen}",
        detail=f"\n      the run's output is probably sitting uncommitted — check "
               f"`git -C {REPO} status`, and check .git/*.lock",
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true",
                    help="print only failures (for cron / morning-health)")
    ap.add_argument("--status-file", metavar="PATH",
                    help="append one timestamped line per check, repo-relative; "
                         "this is what morning-system-health reads")
    args = ap.parse_args()

    tasks, paths = load_registry_tasks()
    if not paths:
        print(f"FAIL  no registry matched {REGISTRY_GLOB}", file=sys.stderr)
        return 2

    if not args.quiet:
        print(f"{len(tasks)} task(s) across {len(paths)} registry file(s)")

    results = [check(spec, tasks, args.quiet) for spec in CHECKS]

    if args.status_file:
        path = args.status_file
        if not os.path.isabs(path):
            path = os.path.join(REPO, path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
        with open(path, "a") as fh:
            for _, line in results:
                fh.write(f"{stamp}  {line}\n")

    return 0 if all(ok for ok, _ in results) else 1


if __name__ == "__main__":
    sys.exit(main())

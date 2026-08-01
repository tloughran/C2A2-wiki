#!/usr/bin/env python3
"""Exercise every branch of check_scheduled_commits, especially the FAIL paths.

A guard that has never been watched failing is not a guard. The bug this whole
detector exists to catch was itself a silent pass, so the cases that matter most
here are the ones where `check()` must return False: task missing from the
registry, task never run, task ran and did not commit. If those quietly returned
True the detector would be decoration.

    python3 scripts/test_check_scheduled_commits.py
"""

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_scheduled_commits as mod  # noqa: E402

SPEC = {"task_id": "t", "grep": "^X", "grace_hours": 2}
FAILURES = []


def iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def expect(name, got, want):
    if got != want:
        FAILURES.append(f"{name}: expected {want}, got {got}")
        print(f"  FAIL {name}")
    else:
        print(f"  ok   {name}")


def run(tasks, commit_at):
    """Drive check() with a stubbed git, so no repo state can sway the result."""
    mod.last_commit_at = lambda pattern: commit_at
    return mod.check(SPEC, tasks, quiet=True)[0]


def main():
    now = datetime.now(timezone.utc)
    stale = now - timedelta(hours=14)   # ran, well past grace
    fresh = now - timedelta(minutes=5)  # ran, still inside grace

    print("cases that MUST fail:")
    # The 2026-08-01 incident itself: ran, grace expired, last commit is a day old.
    expect("ran but committed nothing",
           run({"t": {"enabled": True, "lastRunAt": iso(stale)}},
               stale - timedelta(days=1)),
           False)
    # A commit exists but predates this run -- a previous day's, not this one's.
    expect("commit older than the run",
           run({"t": {"enabled": True, "lastRunAt": iso(stale)}},
               stale - timedelta(minutes=30)),
           False)
    expect("no commit has ever matched",
           run({"t": {"enabled": True, "lastRunAt": iso(stale)}}, None),
           False)
    # Deletion must be loud. A vanished task produces no output either.
    expect("task absent from registry", run({}, None), False)
    expect("enabled but never ran",
           run({"t": {"enabled": True, "lastRunAt": None}}, None),
           False)

    print("cases that MUST pass:")
    expect("ran and committed",
           run({"t": {"enabled": True, "lastRunAt": iso(stale)}},
               stale + timedelta(minutes=6)),
           True)
    # Committing a few minutes BEFORE lastRunAt is normal: the registry stamps
    # the run's end, the commit happens mid-run. The 10-minute slack covers it.
    expect("committed just before the run stamp",
           run({"t": {"enabled": True, "lastRunAt": iso(stale)}},
               stale - timedelta(minutes=5)),
           True)
    expect("still inside the grace window",
           run({"t": {"enabled": True, "lastRunAt": iso(fresh)}}, None),
           True)
    expect("disabled is not a failure",
           run({"t": {"enabled": False, "lastRunAt": iso(stale)}}, None),
           True)

    if FAILURES:
        print(f"\n{len(FAILURES)} case(s) wrong:")
        for f in FAILURES:
            print("  " + f)
        return 1
    print("\nall cases correct")
    return 0


if __name__ == "__main__":
    sys.exit(main())

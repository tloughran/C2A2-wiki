#!/usr/bin/env python3
"""Drive every FAIL path of check_scheduler_health, plus the cron arithmetic.

A guard nobody has watched fail is not a guard. This detector exists because a
previous watchdog returned a clean verdict every morning while three jobs were
broken, so the cases that matter are the ones that must NOT come back OK:

  - a launchd agent with `runs = 0` (the metabolism-publish failure, verbatim)
  - a launchd agent that is in the repo but was never installed
  - an agent that is down after a nonzero exit
  - a task whose cron says it should have fired twice since it last did
  - an artifact whose own recorded generation date is days old while its owning
    task reports a run every morning (the metabolism-regen-daily failure)
  - an artifact that does not date itself at all, or has vanished
  - a cron expression we cannot parse (must fail loud, never match-everything)
  - a failure marker present in the repo (the sync_vault.FAILED that sat
    unread from 2026-08-23 21:01), including a malformed one, which must
    never read as healthy just because its first line did not parse

The cron cases are separate: previous_fires is the arithmetic the whole
did-it-fire verdict rests on, and a matcher that silently matched nothing would
turn every task into a pass.

    python3 scripts/test_check_scheduler_health.py
"""

import json
import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_scheduler_health as mod  # noqa: E402

FAILURES = []


def expect(name, got, want):
    if got != want:
        FAILURES.append(f"{name}: expected {want!r}, got {got!r}")
        print(f"  FAIL {name}\n         expected {want!r}\n         got      {got!r}")
    else:
        print(f"  ok   {name}")


def iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


# A fixed "now" so the cron cases cannot drift with the wall clock.
# 2026-08-04 is a Tuesday; 15:00 local. The Sunday before it is 08-02.
NOW_LOCAL = datetime(2026, 8, 4, 15, 0, tzinfo=timezone(timedelta(hours=-4)))
NOW_UTC = NOW_LOCAL.astimezone(timezone.utc)
# The Sunday-20:00 fire immediately before NOW_LOCAL. Used as the mtime of a log
# that proves a runs = 0 job did fire.
LOGGED = datetime(2026, 8, 2, 20, 0, tzinfo=timezone(timedelta(hours=-4)))


RUNS_ZERO = ("\tstate = not running\n\truns = 0\n"
             "\tlast exit code = (never exited)\n")


def task(**kw):
    base = {"id": "t", "enabled": True, "cronExpression": "30 4 * * *"}
    base.update(kw)
    return base


def artifact_file(tmp, payload):
    path = Path(tmp) / "data.json"
    path.write_text(json.dumps(payload))
    return {"owner": "owner", "path": str(path), "field": "_meta.generated",
            "max_age_hours": 25}


def main():
    print("cron arithmetic (the did-it-fire verdict rests on this):")
    # Daily 04:30 -- the two most recent fires before Monday 15:00 are today and
    # yesterday. If this drifted, every daily task would look overdue or immortal.
    expect("daily 04:30 previous two",
           mod.previous_fires("30 4 * * *", NOW_LOCAL, 2),
           [datetime(2026, 8, 4, 4, 30), datetime(2026, 8, 3, 4, 30)])
    # Weekly Sunday 03:00 -- yesterday and the Sunday before. Interval arithmetic
    # ("168h") gets this right by luck; a matcher gets it right by construction.
    expect("weekly Sunday 03:00 previous two",
           mod.previous_fires("30 3 * * 0", NOW_LOCAL, 2),
           [datetime(2026, 8, 2, 3, 30), datetime(2026, 7, 26, 3, 30)])
    # Step and list forms both appear in the live registry.
    expect("every 4h step form",
           mod.previous_fires("15 */4 * * *", NOW_LOCAL, 2),
           [datetime(2026, 8, 4, 12, 15), datetime(2026, 8, 4, 8, 15)])
    expect("comma list form",
           mod.previous_fires("15 2,6,10,14,18,22 * * *", NOW_LOCAL, 2),
           [datetime(2026, 8, 4, 14, 15), datetime(2026, 8, 4, 10, 15)])
    # Cron numbers Sunday 0 and 7; Python numbers it 6. Getting this wrong shifts
    # every weekly task by a day.
    expect("dow 7 is the same Sunday as dow 0",
           mod.previous_fires("0 3 * * 7", NOW_LOCAL, 1),
           mod.previous_fires("0 3 * * 0", NOW_LOCAL, 1))
    # Tue, Mon, then back over the weekend to Fri -- 08-01 and 08-02 must not match.
    expect("weekday range 1-5 skips the weekend",
           mod.previous_fires("0 9 * * 1-5", NOW_LOCAL, 3),
           [datetime(2026, 8, 4, 9, 0), datetime(2026, 8, 3, 9, 0),
            datetime(2026, 7, 31, 9, 0)])

    expect("next fire looks forward, not back",
           mod.next_fire("30 6 * * 0", NOW_LOCAL),
           datetime(2026, 8, 9, 6, 30))

    print("\nlaunchd calendar fields -> cron (absent field means every):")
    # com.c2a2.metabolism-publish's actual StartCalendarInterval.
    expect("Weekday/Hour/Minute",
           mod.plist_schedule({"StartCalendarInterval": {
               "Weekday": 0, "Hour": 6, "Minute": 30}}),
           ["30 6 * * 0"])
    expect("a list of intervals becomes a list of crons",
           mod.plist_schedule({"StartCalendarInterval": [
               {"Hour": 6, "Minute": 30}, {"Hour": 18, "Minute": 0}]}),
           ["30 6 * * *", "0 18 * * *"])
    # StartInterval / watch paths / KeepAlive-only: we cannot say when it is due,
    # and saying nothing is what keeps runs = 0 a failure rather than an excuse.
    expect("no calendar interval yields no cron",
           mod.plist_schedule({"StartInterval": 3600}), [])

    print("\nunparseable cron must fail loud, never match everything:")
    for bad in ["30 4 * *", "99 4 * * *", "30 4 * * MON", "*/0 4 * * *"]:
        try:
            mod.cron_matcher(bad)
            expect(f"rejects {bad!r}", "accepted", "ValueError")
        except ValueError:
            expect(f"rejects {bad!r}", "ValueError", "ValueError")
    expect("unparseable cron fails the task, not the run",
           mod.verdict_task(task(cronExpression="30 4 * *"), NOW_LOCAL)[0],
           mod.FAIL)

    print("\nregistry tasks that MUST fail:")
    # The shape we are watching for: fired daily, then stopped.
    expect("missed two daily fires",
           mod.verdict_task(task(lastRunAt=iso(NOW_UTC - timedelta(days=3))),
                            NOW_LOCAL)[0],
           mod.FAIL)
    expect("enabled on a cron but never ran",
           mod.verdict_task(task(lastRunAt=None), NOW_LOCAL)[0],
           mod.FAIL)
    expect("weekly task silent for three weeks",
           mod.verdict_task(task(cronExpression="30 3 * * 0",
                                 lastRunAt=iso(NOW_UTC - timedelta(days=21))),
                            NOW_LOCAL)[0],
           mod.FAIL)

    print("\nregistry tasks that MUST pass (or the report becomes noise):")
    expect("ran this morning",
           mod.verdict_task(task(lastRunAt=iso(NOW_UTC - timedelta(hours=11))),
                            NOW_LOCAL)[0],
           mod.OK)
    # One miss is a sleeping laptop at 04:30. Failing on it would make the daily
    # report cry wolf, and a report that always shows red is not read.
    expect("one missed fire is tolerated",
           mod.verdict_task(task(lastRunAt=iso(NOW_UTC - timedelta(hours=26))),
                            NOW_LOCAL)[0],
           mod.OK)
    expect("disabled task is not overdue",
           mod.verdict_task(task(enabled=False, lastRunAt=iso(
               NOW_UTC - timedelta(days=900))), NOW_LOCAL)[0],
           mod.OK)
    expect("one-time task that already fired warns, does not fail",
           mod.verdict_task({"id": "t", "enabled": True,
                             "lastRunAt": iso(NOW_UTC - timedelta(days=90))},
                            NOW_LOCAL)[0],
           mod.WARN)

    print("\nlaunchd agents that MUST fail:")
    expect("runs = 0 (never fired), no context to excuse it",
           mod.parse_launchctl("a", 0, RUNS_ZERO)[0],
           mod.FAIL)
    expect("plist in the repo but not installed",
           mod.parse_launchctl("a", 113, "Could not find service")[0],
           mod.FAIL)
    expect("down after a nonzero exit",
           mod.parse_launchctl("a", 0, "\tstate = not running\n\truns = 4\n"
                                       "\tlast exit code = 1\n")[0],
           mod.FAIL)
    expect("loaded but reports no runs field",
           mod.parse_launchctl("a", 0, "\tstate = not running\n")[0],
           mod.FAIL)
    # A job that HAS had a fire come round since it loaded and still shows runs = 0
    # is the real thing. Sunday 06:30, loaded three weeks ago.
    expect("runs = 0 with fires missed since load",
           mod.parse_launchctl("a", 0, RUNS_ZERO,
                               context={"crons": ["30 6 * * 0"],
                                        "reloaded_at": datetime(2026, 7, 13)},
                               now_local=NOW_LOCAL)[0],
           mod.FAIL)
    # No schedule we can read (StartInterval, watch paths, KeepAlive-only) means we
    # cannot say it is early, so runs = 0 stays a failure rather than an excuse.
    expect("runs = 0 with no readable schedule",
           mod.parse_launchctl("a", 0, RUNS_ZERO,
                               context={"crons": [], "reloaded_at": datetime(2026, 8, 3)},
                               now_local=NOW_LOCAL)[0],
           mod.FAIL)
    # The 2026-09-03 defect, and its falsifier. Three agents carried a never-fired
    # FAIL while their logs held clean fires; the checker asserted "no log exists"
    # without opening one. These four cases pin the fix in BOTH directions -- a
    # patch that simply stopped failing on runs = 0 would pass the first two and
    # fail these last two.
    with tempfile.TemporaryDirectory() as tmp:
        wrote = os.path.join(tmp, "ran.log")
        with open(wrote, "w") as fh:
            fh.write("2026-08-30 20:00:01 generate_weekly_review exit=0\n")
        os.utime(wrote, (LOGGED.timestamp(), LOGGED.timestamp()))
        empty = os.path.join(tmp, "empty.log")
        open(empty, "w").close()
        os.utime(empty, (LOGGED.timestamp(), LOGGED.timestamp()))

        # MUST FAIL: log path declared, but launchd only ever created the file.
        # An empty log is not evidence of a run.
        expect("runs = 0 with an EMPTY log is still never-fired",
               mod.parse_launchctl("a", 0, RUNS_ZERO,
                                   context={"crons": ["0 20 * * 0"],
                                            "reloaded_at": datetime(2026, 7, 13),
                                            "logs": [empty]},
                                   now_local=NOW_LOCAL)[0],
               mod.FAIL)
        # MUST FAIL: the declared log is not on disk at all.
        expect("runs = 0 with a missing log is still never-fired",
               mod.parse_launchctl("a", 0, RUNS_ZERO,
                                   context={"crons": ["0 20 * * 0"],
                                            "reloaded_at": datetime(2026, 7, 13),
                                            "logs": [os.path.join(tmp, "nope.log")]},
                                   now_local=NOW_LOCAL)[0],
               mod.FAIL)

        print("\nthe runs = 0 log evidence (2026-09-03 false-FAIL fix):")
        # MUST PASS: com.tloughran.summa-weekly-review's shape. Sunday 20:00,
        # loaded 07-13, log written on the 08-02 fire -- the most recent one before
        # NOW_LOCAL. The counter says 0; the log says it ran.
        expect("runs = 0 but the log was written on the last fire is OK",
               mod.parse_launchctl("a", 0, RUNS_ZERO,
                                   context={"crons": ["0 20 * * 0"],
                                            "reloaded_at": datetime(2026, 7, 13),
                                            "logs": [wrote]},
                                   now_local=NOW_LOCAL)[0],
               mod.OK)
        # MUST WARN, not pass: same log, but on a DAILY schedule the 08-03 20:00
        # fire came round after that write and left nothing. Proof of life is not
        # proof of the latest run.
        expect("runs = 0, log present but a later fire left no write, warns",
               mod.parse_launchctl("a", 0, RUNS_ZERO,
                                   context={"crons": ["0 20 * * *"],
                                            "reloaded_at": datetime(2026, 7, 13),
                                            "logs": [wrote]},
                                   now_local=NOW_LOCAL)[0],
               mod.WARN)

    print("\nlaunchd agents that MUST fail (continued):")
    # An assertion-agent's UNLISTED exit codes are still faults: 78 is the
    # macl-xattr trap, 2 is the check itself failing to run.
    label = next(iter(mod.VERDICT_EXITS))
    expect("verdict-agent exiting 78 is still a fault",
           mod.parse_launchctl(label, 0, "\tstate = not running\n\truns = 3\n"
                                         "\tlast exit code = 78\n")[0],
           mod.FAIL)

    print("\nlaunchd agents that MUST pass:")
    expect("ran and exited clean",
           mod.parse_launchctl("a", 0, "\tstate = not running\n\truns = 9\n"
                                       "\tlast exit code = 0\n")[0],
           mod.OK)
    # A KeepAlive daemon that is up now has usually exited nonzero on its way
    # here. Failing on that would put openstory permanently in the red.
    expect("running daemon with a nonzero last exit is a restart, not a fault",
           mod.parse_launchctl("a", 0, "\tstate = running\n\truns = 31\n"
                                       "\tlast exit code = 2\n")[0],
           mod.OK)
    # An agent that IS an assertion exits 1 to mean "the thing I check is broken".
    # Calling that an agent fault would leave this permanently red on exactly the
    # days the other watchdog is working.
    # com.c2a2.metabolism-publish, verbatim, on 2026-08-05: Sunday 06:30, reloaded
    # Monday 08-03 when the macl-xattr log fix landed. The last fire (08-02) predates
    # the reload, so runs = 0 is what a healthy job looks like here. Calling it broken
    # would report a fixed job as failing for six more days and teach the reader to
    # skip the line.
    expect("weekly job reloaded after its last fire is early, not broken",
           mod.parse_launchctl("a", 0, RUNS_ZERO,
                               context={"crons": ["30 6 * * 0"],
                                        "reloaded_at": datetime(2026, 8, 3, 13, 37)},
                               now_local=NOW_LOCAL)[0],
           mod.WARN)
    expect("assertion-agent exit 1 is a finding, not a fault",
           mod.parse_launchctl(next(iter(mod.VERDICT_EXITS)), 0,
                               "\tstate = not running\n\truns = 1\n"
                               "\tlast exit code = 1\n")[0],
           mod.WARN)

    print("\nartifacts that MUST fail:")
    with tempfile.TemporaryDirectory() as tmp:
        # metabolism-regen-daily, verbatim: task reported a run every morning,
        # the file said it was generated five days earlier.
        spec = artifact_file(tmp, {"_meta": {"generated": iso(
            NOW_UTC - timedelta(days=5))}})
        expect("artifact five days stale",
               mod.verdict_artifact(spec, NOW_UTC)[0], mod.FAIL)

        # An artifact with no self-recorded date cannot be checked at all, and
        # must say so rather than falling back to an mtime that git does not keep.
        spec = artifact_file(tmp, {"_meta": {"lanes": 33}})
        expect("artifact does not date itself",
               mod.verdict_artifact(spec, NOW_UTC)[0], mod.FAIL)

        spec = artifact_file(tmp, {"_meta": {"generated": "last Tuesday"}})
        expect("self-recorded date is not a timestamp",
               mod.verdict_artifact(spec, NOW_UTC)[0], mod.FAIL)

        (Path(tmp) / "broken.json").write_text("{not json")
        expect("artifact is unreadable",
               mod.verdict_artifact({"owner": "o", "path": str(Path(tmp) / "broken.json"),
                                     "field": "_meta.generated",
                                     "max_age_hours": 25}, NOW_UTC)[0],
               mod.FAIL)

        expect("artifact is missing",
               mod.verdict_artifact({"owner": "o", "path": str(Path(tmp) / "gone.json"),
                                     "field": "_meta.generated",
                                     "max_age_hours": 25}, NOW_UTC)[0],
               mod.FAIL)

        # A row may carry its own failure_means; the generic wording must still
        # apply to rows that do not, or adding one row rewrites another's message.
        spec = artifact_file(tmp, {"_meta": {"generated": iso(
            NOW_UTC - timedelta(days=5))}})
        spec["failure_means"] = "the source has stopped producing"
        code, line = mod.verdict_artifact(spec, NOW_UTC)
        expect("failure_means reaches the reported line",
               code == mod.FAIL and "the source has stopped producing" in line, True)
        spec.pop("failure_means")
        code, line = mod.verdict_artifact(spec, NOW_UTC)
        expect("rows without failure_means keep the generic wording",
               "may report a run and write nothing" in line, True)

        print("\nartifacts that MUST pass:")
        spec = artifact_file(tmp, {"_meta": {"generated": iso(
            NOW_UTC - timedelta(hours=8))}})
        expect("artifact generated this morning",
               mod.verdict_artifact(spec, NOW_UTC)[0], mod.OK)

    # Git debris. The previous accumulation (535 stranded tmp_obj files, 07-31..08-13)
    # could not be pinned on any job because nothing reported it and the evidence was
    # deleted before its mtimes were read. Every case below is therefore about what
    # must NOT come back OK -- and about the age floor, which is the only thing
    # separating abandoned debris from a healthy `git add` that is mid-flight.
    print("\ngit debris that must NOT come back OK:")
    with tempfile.TemporaryDirectory() as tmp:
        git_dir = Path(tmp) / ".git"
        (git_dir / "objects" / "ab").mkdir(parents=True)
        (git_dir / "refs" / "heads").mkdir(parents=True)

        def stamp(path, hours_old):
            path.write_text("x")
            when = (NOW_LOCAL - timedelta(hours=hours_old)).timestamp()
            os.utime(path, (when, when))
            return path

        old_obj = stamp(git_dir / "objects" / "ab" / "tmp_obj_aaaa", 30)
        expect("a stranded tmp_obj warns",
               mod.verdict_git_debris(str(git_dir), NOW_LOCAL)[0], mod.WARN)
        # The line is the whole deliverable: without the timestamps this check
        # reports a number nobody can act on.
        expect("the warning carries the debris timestamps",
               "2026-08-03 09:00" in mod.verdict_git_debris(str(git_dir), NOW_LOCAL)[1],
               True)

        stamp(git_dir / "objects" / "tmp_obj_bbbb", 2)
        expect("tmp_obj directly under objects/ is counted too",
               "2 stranded" in mod.verdict_git_debris(str(git_dir), NOW_LOCAL)[1], True)

        lock = stamp(git_dir / "index.lock", 9)
        expect("a stale index.lock fails, outranking the objects",
               mod.verdict_git_debris(str(git_dir), NOW_LOCAL)[0], mod.FAIL)
        expect("the failure still names the stranded objects",
               "stranded tmp_obj" in mod.verdict_git_debris(str(git_dir), NOW_LOCAL)[1],
               True)
        lock.unlink()

        stamp(git_dir / "refs" / "heads" / "main.lock", 9)
        expect("a stale ref lock under refs/ fails",
               mod.verdict_git_debris(str(git_dir), NOW_LOCAL)[0], mod.FAIL)
        (git_dir / "refs" / "heads" / "main.lock").unlink()

        expect("a git directory that is not there fails loudly, never passes",
               mod.verdict_git_debris(str(Path(tmp) / "absent"), NOW_LOCAL)[0], mod.FAIL)

        print("\ngit debris that MUST pass:")
        # A healthy `git add` writes tmp_obj files and renames them in milliseconds.
        # Without this floor the check fires on every concurrent run and stops
        # being read -- the exact fate of the watchdog this script replaced.
        old_obj.unlink()
        (git_dir / "objects" / "tmp_obj_bbbb").unlink()
        stamp(git_dir / "objects" / "ab" / "tmp_obj_live", 0)
        expect("a tmp_obj younger than the age floor is a live write, not debris",
               mod.verdict_git_debris(str(git_dir), NOW_LOCAL)[0], mod.OK)
        stamp(git_dir / "index.lock", 0)
        expect("a lock younger than the age floor is a live git, not a stale lock",
               mod.verdict_git_debris(str(git_dir), NOW_LOCAL)[0], mod.OK)

    expect("git_common_dir resolves this repo to a real directory",
           Path(mod.git_common_dir(mod.REPO) or "/nonexistent").is_dir(), True)
    # A worktree's .git is a FILE pointing elsewhere, and worktrees share one object
    # store -- so debris stranded by a run in any worktree lands in the primary
    # repo's .git. Assuming `repo/.git` were a directory would check the wrong path.
    expect("git_common_dir on a non-repo returns None, rather than a bad guess",
           mod.git_common_dir(tempfile.gettempdir()) in (None,)
           or not Path(mod.git_common_dir(tempfile.gettempdir())).is_dir(), True)

    # -- failure markers ---------------------------------------------------
    # The marker's whole job is to survive being ignored, so every path that
    # could quietly return OK is driven here. A marker that exists but cannot
    # be parsed is still a job saying it died.
    spec = {"owner": "sync", "path": "sync_vault.FAILED"}

    with tempfile.TemporaryDirectory() as tmp:
        level, line = mod.verdict_failure_marker(spec, repo=tmp)
        expect("no marker reads OK", level, mod.OK)
        expect("no-marker line says the run did not fail",
               "did not fail" in line, True)

    with tempfile.TemporaryDirectory() as tmp:
        marker = os.path.join(tmp, "sync_vault.FAILED")
        with open(marker, "w") as fh:
            fh.write("[2026-08-23 21:01:34] git lock still present after 90s\n")
        level, line = mod.verdict_failure_marker(spec, repo=tmp)
        expect("marker present is a FAIL", level, mod.FAIL)
        expect("marker line carries its own stamp, not an mtime",
               "2026-08-23 21:01:34" in line, True)
        expect("marker line carries the writer's message",
               "git lock still present" in line, True)

    with tempfile.TemporaryDirectory() as tmp:
        marker = os.path.join(tmp, "sync_vault.FAILED")
        with open(marker, "w") as fh:
            fh.write("something changed the format\n")
        level, line = mod.verdict_failure_marker(spec, repo=tmp)
        expect("unparsed marker still FAILs", level, mod.FAIL)
        expect("unparsed marker says so", "unparsed" in line, True)

    with tempfile.TemporaryDirectory() as tmp:
        open(os.path.join(tmp, "sync_vault.FAILED"), "w").close()
        level, _ = mod.verdict_failure_marker(spec, repo=tmp)
        expect("empty marker still FAILs", level, mod.FAIL)

    # The shipped roster must actually point at something a producer writes.
    expect("sync_vault.FAILED is on the shipped marker roster",
           any(s["path"] == "sync_vault.FAILED" for s in mod.FAILURE_MARKERS), True)

    print("\nthe live roster must be reachable (a check that sees nothing passes "
          "everything):")
    tasks, paths = mod.load_registry_tasks()
    expect("registry sees more than the calling session's one task",
           len(tasks) > 1, True)
    labels, plist_problems = mod.launchd_labels()
    expect("at least one launchd plist in the repo", len(labels) > 0, True)
    # Every calendar-scheduled agent must yield a cron, or not_yet_due() silently
    # loses its ability to tell "early" from "broken" for that job.
    expect("every roster entry carries a context",
           all(isinstance(e, tuple) and "crons" in e[1] for e in labels), True)
    # Every shipped plist must parse. Two did not when this was written, and the
    # roster silently shrinking is exactly how a job stops being watched.
    expect("every shipped plist parses", plist_problems, [])

    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILED")
        for line in FAILURES:
            print(f"  - {line}")
        return 1
    print("all assertions passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

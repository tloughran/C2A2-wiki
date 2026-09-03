#!/usr/bin/env python3
"""Assert that every scheduled job actually fired, and left a dated artifact.

Why this exists
---------------
Four failures in one week shared one shape: a job that reported nothing and was
believed. `com.c2a2.metabolism-publish` had `runs = 0` -- it had never fired, two
Sundays running, and wrote no log precisely because it never started, so "read the
log" found nothing and read as "not yet". `metabolism-regen-daily` reported a run
every morning while its data file sat five days old. A hand-built artifact with no
regen path counted zero for six weeks and every consumer believed the zero.

A watchdog for exactly this already existed -- `scheduler-health-check`, daily at
07:00 -- and caught none of them, because it was blind three ways:

1. It enumerated tasks with `mcp__scheduled-tasks__list_scheduled_tasks`, which
   returns only the *calling session's* registry: **1 task of the 70** on this
   machine. Its daily "all N enabled tasks healthy" was N=1. See memory
   `wiki-agents-run-on-openstory-not-claude-tasks`.
2. It knew nothing about launchd at all, so a `runs = 0` agent was never in scope.
3. Its output check compared file mtimes. Git does not preserve mtimes, so on a
   tracked file that check is blind by construction -- memory
   `mtime-freshness-unsound-for-git-files`. We read the date the artifact records
   about *itself* instead.

All three are code's job, not a model's (Rule 5). The skill now runs this and
reports what it says.

The three questions, and why they are all here
----------------------------------------------
    did it fire?        launchd `runs`, registry `lastRunAt` vs the cron
    did it survive?     launchd `last exit code`
    did it produce?     the artifact's own recorded generation date

They live in one script, behind one launchd agent, on purpose: every silent
failure in this repo has been a job that died with nothing said about it, so a
second agent is a second surface for exactly that. One job, one log, three
verdicts is fewer places to go quiet.

Usage
-----
    python3 scripts/check_scheduler_health.py
    python3 scripts/check_scheduler_health.py --quiet          # failures only
    python3 scripts/check_scheduler_health.py --status-file scheduler/scheduler_health.md

Exit 0 all-clear (WARNs included), 1 if anything FAILed, 2 if the check itself
could not run.
"""

import argparse
import glob
import json
import os
import plistlib
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGISTRY_GLOB = os.path.expanduser(
    "~/Library/Application Support/Claude/*/*/*/scheduled-tasks.json"
)

# The launchd roster is the repo's own plists, not whatever happens to be loaded.
# Taking the roster from ~/Library/LaunchAgents would make an agent that was never
# installed invisible -- which is one of the failure modes we are here to catch.
PLIST_DIR = os.path.join(REPO, "scripts", "launchd")

# A task that missed this many consecutive scheduled fires is broken. Two, not one:
# a single miss is a laptop that was asleep at 03:00, which is normal here and not
# worth waking anyone for. Two in a row is not a coincidence.
MISSED_FIRES_ALLOWED = 2

# Artifact assertions. `field` is a dotted path into the JSON; the value must be an
# ISO-8601 timestamp the *producer wrote about itself*. Never an mtime.
#
# max_age_hours is the schedule interval plus slack, so a single missed run is not
# a scream but two are.
# Some agents ARE assertions, and exit nonzero to mean "what I checked is broken",
# not "I am broken". Reading that as an agent fault would put this permanently red
# on exactly the days the other watchdog is doing its job, and a report that is
# always red stops being read. Their finding is already reported through their own
# status files; here it is a WARN pointing at those.
#
# Only the codes listed are treated as verdicts. Anything else -- 2 (the check
# itself could not run), 78 (EX_CONFIG, the macl-xattr trap) -- is still a FAIL.
VERDICT_EXITS = {
    "com.c2a2.scheduled-commit-check": {"1"},
}

ARTIFACTS = [
    {
        "owner": "metabolism-regen-daily",
        "path": "wiki/metabolism/metabolism_data.json",
        "field": "_meta.generated",
        "max_age_hours": 25,
        "note": "reported a run every day 07-30..08-04 while this stayed 5 days old",
    },
    {
        # The row above asks whether the FILE was rebuilt. This one asks whether
        # the DATA moved. They are independent, and during 2026-08-15..08-24 the
        # first was green every morning while the second had been frozen for
        # days: the regen ran on time, on a source that had stopped producing.
        # Nothing here could see that, because nothing here read the data.
        "owner": "openstory-ingest (data inside metabolism_data.json)",
        "path": "wiki/metabolism/metabolism_data.json",
        "field": "_meta.t_max_event",
        "max_age_hours": 48,
        "failure_means": (
            "the newest OpenStory EVENT in the snapshot is that old, so the source "
            "has stopped producing. Check the H-Drive mount and the ingest agents; "
            "regenerating the artifact cannot move this date"
        ),
        "note": "48h chosen from 3150 sessions: p99.9 inter-session gap is 39.9h, and "
                "the only two gaps over 48h since 2026-05-07 were both real outages",
    },
]

# Git debris left behind when a git process dies mid-write. Two kinds, one cause:
#
#   .git/objects/**/tmp_obj_*  -- a loose object begun and never renamed into place
#   .git/index.lock, HEAD.lock, refs/**/*.lock -- an index/ref lock never released
#
# 535 stranded tmp_obj files accumulated 2026-07-31..08-13 with nothing reporting
# it, and a stale index.lock is what made commit_daily_run.sh refuse outright on
# 2026-08-11 ("REFUSED: stale git lock present"). Both are invisible until someone
# goes looking, which is the failure mode this whole script exists to end.
#
# This is a repo-wide condition, not any one task's artifact, so it gets its own
# verdict rather than an ARTIFACTS row: it has no owning task and no self-dated
# JSON to read.
#
# mtime is sound here, unlike the artifact checks. These are local writes to a
# live tree that git itself makes and never commits -- there is no clone or
# checkout that could restamp them, and the file's age IS the fact in question.
#
# The age floor exists because a healthy `git add` creates tmp_obj files and
# renames them within milliseconds; flagging those would fire on every concurrent
# run. Anything still sitting an hour later was abandoned.
GIT_DEBRIS_MIN_AGE_HOURS = 1


def git_common_dir(repo):
    """The shared .git directory, resolved through worktrees.

    Worktrees share one object store, so a tmp_obj stranded by a run in any
    worktree lands in the primary repo's .git. Asking git rather than assuming
    `repo/.git` is a directory keeps this correct when run from a worktree,
    where .git is a file pointing elsewhere.
    """
    out = subprocess.run(
        ["git", "-C", repo, "rev-parse", "--git-common-dir"],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        return None
    path = out.stdout.strip()
    if not path:
        return None
    return path if os.path.isabs(path) else os.path.join(repo, path)


def scan_git_debris(git_dir, now_local, min_age_hours=GIT_DEBRIS_MIN_AGE_HOURS):
    """(stale_tmp_objects, stale_locks) as lists of (path, mtime), oldest first."""
    cutoff = now_local - timedelta(hours=min_age_hours)

    def aged(paths):
        found = []
        for path in paths:
            try:
                mtime = datetime.fromtimestamp(os.path.getmtime(path)).astimezone()
            except OSError:
                continue  # vanished mid-scan: a live git just finished with it
            if mtime <= cutoff:
                found.append((path, mtime))
        return sorted(found, key=lambda pair: pair[1])

    tmp = glob.glob(os.path.join(git_dir, "objects", "**", "tmp_obj_*"), recursive=True)
    locks = (glob.glob(os.path.join(git_dir, "*.lock"))
             + glob.glob(os.path.join(git_dir, "refs", "**", "*.lock"), recursive=True))
    return aged(tmp), aged(locks)


def verdict_git_debris(git_dir, now_local, min_age_hours=GIT_DEBRIS_MIN_AGE_HOURS):
    """FAIL on a stale lock, WARN on stranded objects, OK on a clean store.

    The lock outranks the objects on purpose. Stranded objects waste disk and
    point at a bug; a stale lock actively blocks the next commit, which is a
    thing that has already happened here.

    Both lines carry the oldest and newest timestamps. That is the whole point of
    the check: the previous accumulation could not be pinned on any job because
    the evidence was deleted before anyone read its mtimes. Whoever reads this
    next should be able to name the 05:45 slot, or rule it out.
    """
    if not git_dir or not os.path.isdir(git_dir):
        return (FAIL, f"git debris: no git directory at {git_dir!r} — cannot check")

    tmp, locks = scan_git_debris(git_dir, now_local, min_age_hours)

    def span(items):
        first, last = items[0][1], items[-1][1]
        if first == last:
            return f"at {first:%Y-%m-%d %H:%M}"
        return f"{first:%Y-%m-%d %H:%M} .. {last:%Y-%m-%d %H:%M}"

    if locks:
        names = ", ".join(sorted({os.path.basename(p) for p, _ in locks}))
        line = (f"git debris: {len(locks)} stale lock(s) ({names}), {span(locks)} — "
                f"this blocks the next commit; remove once no git process is live")
        if tmp:
            line += f"; also {len(tmp)} stranded tmp_obj, {span(tmp)}"
        return (FAIL, line)

    if tmp:
        return (WARN, f"git debris: {len(tmp)} stranded tmp_obj file(s), {span(tmp)} — "
                      f"a git process died mid-write; the newest mtime names the slot")

    return (OK, "git debris: no stale tmp_obj or lock files")


# --------------------------------------------------------- failure markers

# A file whose EXISTENCE is the report.
#
# sync_vault.sh writes sync_vault.FAILED on every failure path and rm -f's it
# on a clean run, so the file is present exactly when the last run died. That
# marker sat in the repo root from 21:01 on 2026-08-23 and nothing read it --
# the same defect that let 08-19..08-22 go unpublished.
#
# Every other check in this script is scoped to an artifact that a *running*
# job maintains, so a job that does not run produces nothing to be stale. A
# marker inverts that: the non-event is the subject.
#
# The timestamp is read from the line the writer stamps into the file, never
# from the mtime -- same rule as the artifact checks.
FAILURE_MARKERS = [
    {
        "owner": "com.tloughran.summa-vault-sync",
        "path": "sync_vault.FAILED",
        "note": "written by sync_vault.sh fail_loud(); removed on a clean run",
    },
    {
        "owner": "com.tomloughran.openstory.watchdog",
        "path": "openstory_precondition.FAILED",
        "note": "H-Drive unmounted; written by openstory-watchdog.sh's precondition "
                "gate, cleared when the volume returns. The gate itself is correct "
                "-- restarting into a dangling symlink cannot help -- but it only "
                "ever notified, and 270 notifications 2026-07-24..08-24 bought "
                "nine days of dead ingest",
    },
]

MARKER_STAMP = re.compile(r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s*(.*)")


def verdict_failure_marker(spec, repo=None):
    """FAIL while the marker exists, OK when it does not.

    Deliberately no age tolerance, unlike the artifact checks. A marker is not
    data that has gone stale and might still be fine; it is a job stating that
    it died, and it stays true until that job succeeds and clears it. Ageing it
    out would re-create the exact silence it exists to break.
    """
    repo = REPO if repo is None else repo
    rel = spec["path"]
    owner = spec["owner"]
    path = os.path.join(repo, rel)

    if not os.path.exists(path):
        return (OK, f"{owner}: no {rel} — last run did not fail")

    try:
        with open(path) as fh:
            first = fh.readline().strip()
    except OSError as exc:
        return (FAIL, f"{owner}: {rel} present but unreadable ({exc})")

    match = MARKER_STAMP.match(first)
    if match:
        return (FAIL, f"{owner}: FAILED at {match.group(1)} -- {match.group(2)}")
    return (FAIL, f"{owner}: {rel} present, first line unparsed: {first!r}")


# --------------------------------------------------------------------------- cron


def _expand(field, lo, hi):
    """One cron field -> the set of values it matches. Raises on anything unknown.

    Deliberately strict: a cron expression we cannot parse must not silently
    become "matches everything", which would turn every stale task into a pass.
    """
    values = set()
    for part in field.split(","):
        step = 1
        if "/" in part:
            part, _, raw_step = part.partition("/")
            step = int(raw_step)
            if step < 1:
                raise ValueError(f"bad step in {field!r}")
        if part == "*":
            start, end = lo, hi
        elif "-" in part.lstrip("-"):
            raw_start, _, raw_end = part.partition("-")
            start, end = int(raw_start), int(raw_end)
        else:
            start = end = int(part)
        if start < lo or end > hi or start > end:
            raise ValueError(f"out of range in {field!r}")
        values.update(range(start, end + 1, step))
    return values


def cron_matcher(expression):
    """Compile a 5-field cron into a predicate over naive local datetimes."""
    fields = expression.split()
    if len(fields) != 5:
        raise ValueError(f"expected 5 cron fields, got {len(fields)}: {expression!r}")
    minutes = _expand(fields[0], 0, 59)
    hours = _expand(fields[1], 0, 23)
    doms = _expand(fields[2], 1, 31)
    months = _expand(fields[3], 1, 12)
    # Cron accepts both 0 and 7 for Sunday; Python's weekday() calls Sunday 6.
    dows = {d % 7 for d in _expand(fields[4], 0, 7)}

    dom_restricted = fields[2] != "*"
    dow_restricted = fields[4] != "*"

    def matches(when):
        if when.minute not in minutes or when.hour not in hours:
            return False
        if when.month not in months:
            return False
        dom_ok = when.day in doms
        dow_ok = ((when.weekday() + 1) % 7) in dows
        # Standard cron: when BOTH day fields are restricted they are OR'd, not
        # AND'd. None of our expressions do this today, but getting it wrong
        # would make such a task look permanently overdue.
        if dom_restricted and dow_restricted:
            return dom_ok or dow_ok
        return dom_ok and dow_ok

    return matches


def next_fire(expression, now_local, horizon_days=400):
    """The next time this cron will fire, or None past the horizon.

    Used to say WHEN a job that has legitimately not run yet is due. A weekly job
    reloaded on a Monday has not failed by Wednesday; it has not been asked yet.
    """
    matches = cron_matcher(expression)
    cursor = now_local.replace(second=0, microsecond=0, tzinfo=None)
    for _ in range(horizon_days * 24 * 60):
        cursor += timedelta(minutes=1)
        if matches(cursor):
            return cursor
    return None


def previous_fires(expression, now_local, count, horizon_days=45):
    """The `count` most recent times this cron should have fired, newest first.

    Walks back a minute at a time. 45 days of minutes is 65k iterations, which is
    nothing, and it is exactly right for weekly and monthly crons where interval
    arithmetic starts guessing.

    Works in naive wall-clock time, because that is what cron itself schedules on.
    A DST shift inside the window can move a computed fire by an hour; against a
    threshold of two missed fires (a day at minimum) that is noise.
    """
    matches = cron_matcher(expression)
    cursor = now_local.replace(second=0, microsecond=0, tzinfo=None)
    found = []
    for _ in range(horizon_days * 24 * 60):
        cursor -= timedelta(minutes=1)
        if matches(cursor):
            found.append(cursor)
            if len(found) == count:
                break
    return found


# ------------------------------------------------------------------------ verdicts

OK, WARN, FAIL = "OK", "WARN", "FAIL"


def verdict_task(task, now_local):
    """Did this registry task fire when its cron said it should?"""
    tid = task.get("id", "<no id>")

    if not task.get("enabled", False):
        return OK, f"{tid}: disabled"

    cron = task.get("cronExpression")
    last = task.get("lastRunAt")

    if not cron:
        # One-time task. Enabled with no cron and already fired means it never
        # auto-disabled; enabled and never fired is a task waiting on a fireAt we
        # cannot see from here. Neither is broken enough to fail the run.
        if last:
            return WARN, f"{tid}: one-time task still enabled after running {last[:16]}Z"
        return WARN, f"{tid}: enabled, no cron, never run"

    try:
        fires = previous_fires(cron, now_local, MISSED_FIRES_ALLOWED)
    except ValueError as exc:
        return FAIL, f"{tid}: unparseable cron {cron!r} — {exc}"

    if not last:
        return FAIL, f"{tid}: enabled on {cron!r} and has never run"

    ran_local = parse_iso(last).astimezone(now_local.tzinfo)
    if not fires:
        return WARN, f"{tid}: {cron!r} has no fire in the last 45 days"

    oldest_allowed = fires[-1]
    if ran_local.replace(tzinfo=None) >= oldest_allowed:
        return OK, f"{tid}: ran {ran_local:%Y-%m-%d %H:%M}, on schedule for {cron!r}"

    missed = sum(1 for f in fires if ran_local.replace(tzinfo=None) < f)
    hours = (now_local.replace(tzinfo=None) - ran_local.replace(tzinfo=None)).total_seconds() / 3600
    return FAIL, (
        f"{tid}: last ran {ran_local:%Y-%m-%d %H:%M} ({hours:.0f}h ago), "
        f"missed {missed} scheduled fire(s) of {cron!r}"
    )


def plist_schedule(job):
    """A StartCalendarInterval dict (or list of them) as cron expressions.

    launchd's calendar fields are the same five cron fields under different names,
    with "absent" meaning "every". Anything else -- StartInterval, watch paths,
    KeepAlive-only -- returns [], which means "we cannot say when this is due".
    """
    entries = job.get("StartCalendarInterval")
    if entries is None:
        return []
    if isinstance(entries, dict):
        entries = [entries]
    crons = []
    for entry in entries:
        def field(name):
            value = entry.get(name)
            return "*" if value is None else str(value)
        crons.append(" ".join([field("Minute"), field("Hour"),
                               field("Day"), field("Month"), field("Weekday")]))
    return crons


def not_yet_due(context, now_local):
    """(True, next_fire) if no scheduled fire has come round since the job loaded.

    `runs = 0` on a weekly job reloaded four days ago is not the same fact as
    `runs = 0` on a job that has been sitting there for six Sundays, and calling
    both a failure trains the reader to ignore both. This is what tells them apart.

    `reloaded_at` is the plist's mtime, which is a PROXY: launchd does not report
    when a service was bootstrapped. Rewriting a plist is what forces the reload,
    so in practice the two coincide -- but a bootout/bootstrap with no file edit
    would not move it, and would make this say FAIL where WARN was right. The proxy
    errs toward reporting, which is the safe direction.
    """
    reloaded_at, crons = context.get("reloaded_at"), context.get("crons") or []
    if reloaded_at is None or not crons:
        return False, None
    upcoming = []
    for cron in crons:
        try:
            if previous_fires(cron, now_local, 1)[0] > reloaded_at:
                return False, None  # a fire HAS come round since load, and was missed
            upcoming.append(next_fire(cron, now_local))
        except (ValueError, IndexError):
            return False, None
    upcoming = [f for f in upcoming if f]
    return True, min(upcoming) if upcoming else None


def plist_logs(job):
    """The log paths a job declares in its own plist."""
    paths = []
    for key in ("StandardOutPath", "StandardErrorPath"):
        value = job.get(key)
        if value:
            paths.append(os.path.expanduser(value))
    return paths


def newest_log_write(context):
    """(path, mtime) of the most recent non-empty log this job owns, else (None, None).

    2026-09-03: `runs = 0` was reported for com.tloughran.summa-weekly-review,
    com.c2a2.metabolism-publish and com.tomloughran.openstory-version-check, and all
    three had logs showing clean fires on 08-16, 08-23, 08-30 and 08-31. launchd's
    counter is NOT a run record for a calendar job that completed and was unloaded
    from memory. Three of the six FAIL lines on that morning's panel were false, and
    the one real FAIL -- the H-Drive unmounted, stopping OpenStory ingest -- sat
    unactioned for seven days behind them.

    The lesson is narrower than "the counter is wrong": this function exists so the
    checker never again ASSERTS the absence of an artifact it did not try to open.
    An empty log is not evidence of a run -- launchd creates the file when it
    bootstraps the job, before anything writes to it -- so size 0 does not count.
    """
    newest = (None, None)
    for path in context.get("logs") or []:
        try:
            stat = os.stat(path)
        except OSError:
            continue
        if stat.st_size == 0:
            continue
        # Naive local, matching installed_plist's mtime and what previous_fires
        # returns -- this module compares those two directly (see not_yet_due).
        when = datetime.fromtimestamp(stat.st_mtime)
        if newest[1] is None or when > newest[1]:
            newest = (path, when)
    return newest


def parse_launchctl(label, returncode, text, context=None, now_local=None):
    """Turn `launchctl print` output into a verdict.

    Split out from the subprocess call so the failure paths -- never fired, died
    nonzero, not installed -- can be driven in a test without a real launchd.
    """
    context = context or {}
    if returncode != 0:
        return FAIL, f"{label}: not loaded in launchd (plist is in the repo but not installed)"

    def field(name):
        match = re.search(rf"^\s*{re.escape(name)} = (.*)$", text, re.M)
        return match.group(1).strip() if match else None

    runs = field("runs")
    state = field("state")
    exit_code = field("last exit code")

    if runs is None:
        return FAIL, f"{label}: loaded but `launchctl print` reported no `runs` field"

    if runs == "0":
        pending, due = not_yet_due(context, now_local or datetime.now().astimezone())
        if pending:
            when = f", first due {due:%Y-%m-%d %H:%M}" if due else ""
            return WARN, (
                f"{label}: runs = 0, but it was (re)loaded "
                f"{context['reloaded_at']:%Y-%m-%d} and no scheduled fire has come "
                f"round since{when} — not yet proven, not yet broken"
            )
        # Before calling it never-fired, open the log. See newest_log_write.
        log_path, log_at = newest_log_write(context)
        if log_at is not None:
            now = now_local or datetime.now().astimezone()
            missed = None
            for cron in context.get("crons") or []:
                try:
                    last_due = previous_fires(cron, now, 1)[0]
                except (ValueError, IndexError):
                    continue
                if last_due > log_at and (missed is None or last_due > missed):
                    missed = last_due
            if missed is not None:
                return WARN, (
                    f"{label}: runs = 0, but {os.path.basename(log_path)} was written "
                    f"{log_at:%Y-%m-%d %H:%M}, so it HAS fired — the fire due "
                    f"{missed:%Y-%m-%d %H:%M} left no write. Read the log, not the counter."
                )
            return OK, (
                f"{label}: runs = 0, but {os.path.basename(log_path)} was written "
                f"{log_at:%Y-%m-%d %H:%M} — it fired and finished; launchd's counter "
                f"does not survive the unload"
            )
        return FAIL, (
            f"{label}: loaded but has NEVER fired (runs = 0), at least one scheduled "
            f"fire has passed, and its log is absent or empty. It never started."
        )

    # A KeepAlive daemon that is up right now has usually exited nonzero at some
    # point on its way here; that is a restart, not a fault. Only a job that is
    # down AND exited nonzero is currently broken.
    if exit_code not in (None, "0", "(never exited)") and state != "running":
        if exit_code in VERDICT_EXITS.get(label, ()):
            return WARN, (
                f"{label}: exit {exit_code} — it fired and REPORTED A FINDING; "
                f"read its status file, not this line"
            )
        return FAIL, f"{label}: last exit code {exit_code} (runs = {runs}, state = {state})"

    return OK, f"{label}: runs = {runs}, state = {state}, last exit {exit_code}"


def verdict_artifact(spec, now_utc, repo=REPO):
    """Did the producer leave a dated artifact, and is that date recent?"""
    owner, rel = spec["owner"], spec["path"]
    path = rel if os.path.isabs(rel) else os.path.join(repo, rel)

    if not os.path.exists(path):
        return FAIL, f"{owner}: artifact {rel} does not exist"

    try:
        with open(path) as fh:
            data = json.load(fh)
    except (OSError, ValueError) as exc:
        return FAIL, f"{owner}: cannot read {rel}: {exc}"

    node = data
    for key in spec["field"].split("."):
        if not isinstance(node, dict) or key not in node:
            return FAIL, f"{owner}: {rel} has no {spec['field']} — it does not date itself"
        node = node[key]

    try:
        generated = parse_iso(str(node)).astimezone(timezone.utc)
    except ValueError:
        return FAIL, f"{owner}: {rel} {spec['field']} is not a timestamp: {node!r}"

    age_hours = (now_utc - generated).total_seconds() / 3600
    if age_hours > spec["max_age_hours"]:
        means = spec.get("failure_means", "the task may report a run and write nothing")
        return FAIL, (
            f"{owner}: {rel} {spec['field']} is {generated:%Y-%m-%d %H:%M}Z, "
            f"{age_hours / 24:.1f} days ago — {means}"
        )
    return OK, (f"{owner}: {rel} {spec['field']} = {generated:%Y-%m-%d %H:%M}Z "
                f"({age_hours:.0f}h ago)")


# -------------------------------------------------------------------------- inputs


def parse_iso(stamp):
    """Registry and artifact stamps are ISO-8601, with or without a trailing Z."""
    return datetime.fromisoformat(stamp.replace("Z", "+00:00"))


def load_registry_tasks():
    """Every scheduled task across every account registry on this machine.

    Reads the JSON directly rather than asking the MCP tool, which only ever
    returns the calling session's own registry -- 1 task of 70. That gap is the
    whole reason the previous watchdog saw nothing.
    """
    paths = sorted(glob.glob(REGISTRY_GLOB))
    by_id = {}
    for path in paths:
        try:
            with open(path) as fh:
                tasks = json.load(fh).get("scheduledTasks", [])
        except (OSError, ValueError) as exc:
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


def installed_plist(label):
    """mtime of the INSTALLED copy, as the reload proxy. See not_yet_due()."""
    path = os.path.expanduser(f"~/Library/LaunchAgents/{label}.plist")
    try:
        return datetime.fromtimestamp(os.stat(path).st_mtime)
    except OSError:
        return None


def launchd_labels():
    """(labels, problems) for every plist the repo ships, read from the plists.

    A plist we cannot parse becomes a FAIL verdict rather than an exception. Two
    of these were unparseable when this was written -- their XML comments contained
    a literal `--`, which the spec forbids. `plutil -lint` and launchd itself both
    accept it, so nothing had ever complained; any strict XML reader chokes. A
    watchdog that dies on the roster it is meant to check is worse than useless,
    so the unreadable file is reported and the rest of the roster still runs.
    """
    labels, problems = [], []
    for path in sorted(glob.glob(os.path.join(PLIST_DIR, "*.plist"))):
        try:
            with open(path, "rb") as fh:
                job = plistlib.load(fh)
        except Exception as exc:  # plistlib raises ExpatError, not ValueError
            problems.append((FAIL, f"{os.path.basename(path)}: unreadable plist: {exc}"))
            continue
        label = job.get("Label")
        if not label:
            problems.append((FAIL, f"{os.path.basename(path)}: plist has no Label key"))
            continue
        labels.append((label, {"crons": plist_schedule(job),
                               "reloaded_at": installed_plist(label),
                               "logs": plist_logs(job)}))
    return labels, problems


def launchctl_print(label):
    out = subprocess.run(
        ["launchctl", "print", f"gui/{os.getuid()}/{label}"],
        capture_output=True,
        text=True,
    )
    return out.returncode, out.stdout


# ---------------------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true",
                    help="print only WARN and FAIL lines (for cron / morning-health)")
    ap.add_argument("--status-file", metavar="PATH",
                    help="append one timestamped line per non-OK verdict, plus a "
                         "summary; this is what the morning report reads")
    args = ap.parse_args()

    now_utc = datetime.now(timezone.utc)
    now_local = now_utc.astimezone()

    results = []

    tasks, registry_paths = load_registry_tasks()
    if not registry_paths:
        print(f"FAIL  no registry matched {REGISTRY_GLOB}", file=sys.stderr)
        return 2
    for _, task in sorted(tasks.items()):
        results.append(verdict_task(task, now_local))

    labels, plist_problems = launchd_labels()
    if not labels and not plist_problems:
        print(f"FAIL  no plists found in {PLIST_DIR}", file=sys.stderr)
        return 2
    results.extend(plist_problems)
    for label, context in labels:
        results.append(parse_launchctl(label, *launchctl_print(label),
                                       context=context, now_local=now_local))

    for spec in ARTIFACTS:
        results.append(verdict_artifact(spec, now_utc))

    results.append(verdict_git_debris(git_common_dir(REPO), now_local))

    for spec in FAILURE_MARKERS:
        results.append(verdict_failure_marker(spec))

    counts = {OK: 0, WARN: 0, FAIL: 0}
    for level, line in results:
        counts[level] += 1
        if level != OK or not args.quiet:
            print(f"{level:<5} {line}")

    summary = (
        f"{len(tasks)} registry task(s) across {len(registry_paths)} file(s), "
        f"{len(labels)} launchd agent(s), {len(ARTIFACTS)} artifact(s), "
        f"1 git-debris check, {len(FAILURE_MARKERS)} failure marker(s): "
        f"{counts[OK]} OK, {counts[WARN]} WARN, {counts[FAIL]} FAIL"
    )
    print(summary)

    if args.status_file:
        path = args.status_file
        if not os.path.isabs(path):
            path = os.path.join(REPO, path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        stamp = now_utc.strftime("%Y-%m-%dT%H:%MZ")
        with open(path, "a") as fh:
            fh.write(f"{stamp}  {summary}\n")
            for level, line in results:
                if level != OK:
                    fh.write(f"{stamp}  {level:<5} {line}\n")

    return 1 if counts[FAIL] else 0


if __name__ == "__main__":
    sys.exit(main())

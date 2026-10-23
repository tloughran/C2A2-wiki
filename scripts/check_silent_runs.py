#!/usr/bin/env python3
"""Assert that every scheduled run that was DISPATCHED actually said something.

Why this exists
---------------
A scheduled task can be handed a session, open a transcript, and then produce no
assistant turn at all -- it dies in 0-2 seconds with a one-line transcript holding
only the dispatch message. Measured 2026-10-23 across 3,743 scheduled transcripts:
19 runs ended this way. Fourteen of them fell in two days, 2026-08-26 (3) and
2026-08-27 (11), and nobody noticed at the time -- `scheduler-health-check` was
itself one of the dead, which is the whole argument for this living under launchd.

Nothing could see it. The four questions asked about a scheduled run were:

    did it fire at all?      launchd `runs`, registry `lastRunAt` vs cron
                             -> check_scheduler_health.py
    did it finish?           transcript present but no `result` record
                             -> check_daily_run_stall.py
    did it produce output?   the artifact's own recorded generation date
                             -> ARTIFACTS in check_scheduler_health.py
    did it SAY ANYTHING?     nothing asked this

A silent run answers the first question "yes" (it fired, `lastRunAt` advanced) and
the third "no", with no stall to name and no error to read. It looks exactly like a
task whose turn has not come round yet.

The 24 fall in two clusters with DIFFERENT durations, which is why duration is not
the signal here:

    2026-08-27  14 runs, 8 tasks, died in 0-2s (median 1s), model claude-opus-5
    2026-10-15   5 runs, 5 tasks, duration not measurable from disk -- these use
                 the newer 8-hex run directories, which have no matching
                 local_<uuid>.json metadata, so createdAt/lastActivityAt are not
                 available. A prior investigation recorded these as reaped at ~615s
                 with `no_response` / `had_first_response: false`; those field names
                 appear nowhere in the session metadata schema reachable from here,
                 so that figure is neither confirmed nor contradicted by this script.
     (5 more)    no parseable start time at all, reported undated.

Both clusters contain `scheduler-health-check` itself, which is the argument for
this check living under launchd rather than in the 07:00 task.

This is NOT the stall check in different clothes
------------------------------------------------
A stall leaves a LONG transcript with no `result` record: the run worked for a
while and then sat holding an unanswered permission prompt (39 of 110 daily runs,
measured 2026-08-04). A silent run leaves ONE LINE and exits in about a second.
Opposite shapes, opposite remedies -- a stall means "approve this tool", a silent
run means the dispatch layer handed out a session it could not service.

Which is also why the signal is "no assistant turn", not "short run" and not "no
result record". A silent run has no result record either, so keying on that would
fire this row on all 39 known stalls and make two checks say the same wrong thing.

Design commitments, each guarding a way this could go wrong
-----------------------------------------------------------
A WINDOW, not all history. The 19 historical cases are known and settled. An alarm
that re-reports them every morning is wallpaper inside a week, and this repo has
already learned that a row which cries wolf stops being read (see the LAG_ARTIFACTS
comment in check_scheduler_health.py).

ONE occurrence is a FAIL, not a WARN. Base rate is 19 in 3,743 runs -- 0.5%. There
is no benign version of "produced nothing", so there is no threshold to tune and
nothing to average.

A CLUSTER gets its own row. Fourteen silent runs across eight tasks in two days is
one dispatch-layer fault, not fourteen task faults, and reporting it as fourteen
rows invites fourteen wrong investigations.

AN UNREADABLE SESSION TREE IS A FAIL. Silence read as health is the founding
mistake of this repo. A check that can see nothing passes everything, so finding
zero transcripts in the window is only OK if we can also show the tree was readable
and simply empty.

The glob covers BOTH session-directory schemes
----------------------------------------------
The desktop app writes run directories two ways, and the changeover is around
2026-09-15:

    .../<session>/local_<uuid>/audit.jsonl     4,033 runs, the older scheme
    .../<session>/<8-hex>/audit.jsonl            719 runs, the current one

The 8-hex directory name is NOT the `sessionId` from the session metadata, so a
lookup keyed on `sessionId` silently resolves nothing for every run since
mid-September. That cost me a 691-run phantom on 2026-10-23 before I caught it, and
check_daily_run_stall.py's `local_*/audit.jsonl` glob has the same blind spot --
it has been unable to see any run since the changeover. Attribution is therefore by
the transcript's own first line, never by directory name.

    python3 scripts/check_silent_runs.py
    python3 scripts/check_silent_runs.py --window-hours 26
    python3 scripts/check_silent_runs.py --status-file scheduler/silent_runs.md
    python3 scripts/check_silent_runs.py --all-history   # the census, not the alarm

Exit 0 all-clear, 1 if any silent run was found, 2 if the check could not run.
"""

import argparse
import glob
import json
import os
import sys
from datetime import datetime, timedelta, timezone

OK, WARN, FAIL = "OK", "WARN", "FAIL"

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Both schemes, in one glob each. Kept as a list rather than a brace pattern so the
# two can be counted apart in the summary -- if one scheme goes to zero that is
# itself worth seeing, since that is how the changeover blindsided the stall check.
SESSION_GLOBS = [
    os.path.expanduser("~/Library/Application Support/Claude"
                       "/local-agent-mode-sessions/*/*/local_*/audit.jsonl"),
    os.path.expanduser("~/Library/Application Support/Claude"
                       "/local-agent-mode-sessions/*/*/*/audit.jsonl"),
]

# 26h, matching the artifact rows in check_scheduler_health.py: one daily cycle plus
# slack, so a run that fired late is still inside the window the morning after.
DEFAULT_WINDOW_HOURS = 26

# Above this many silent runs in one window, report the cluster instead of the rows.
# Two is a coincidence; three in a day has only ever happened on 08-26/27, which was
# a single dispatch-layer fault.
CLUSTER_AT = 3


def discover_transcripts(globs=None):
    """Every scheduled-run transcript on this machine, de-duplicated.

    The two globs overlap (the second matches local_* dirs too), so the result is a
    set. Returned as a sorted list for stable output.
    """
    globs = SESSION_GLOBS if globs is None else globs
    found = set()
    for pattern in globs:
        found.update(glob.glob(pattern))
    return sorted(found)


def attribution(path):
    """(task_id, started_utc) from a transcript's first line, or None if not a task.

    Reads ONE line: there are thousands of these files. Mirrors
    check_daily_run_stall.attribution deliberately -- same first-line contract, so
    the two cannot disagree about which task a transcript belongs to.

    The task id is the SKILL.md's parent directory name, which is the registry's
    taskId. Taking it from the path rather than the `name=` attribute is deliberate:
    `name=` has been observed to disagree with the registry id (the c282/c2a2 typo
    is baked into the directory, and the directory is what the registry keys on).
    """
    try:
        with open(path, errors="replace") as fh:
            first = fh.readline()
    except OSError:
        return None
    if "<scheduled-task" not in first:
        return None
    try:
        rec = json.loads(first)
    except ValueError:
        return None
    content = (rec.get("message") or {}).get("content")
    if not isinstance(content, str) or 'file="' not in content:
        return None
    task_file = content.split('file="', 1)[1].split('"', 1)[0]
    task_id = os.path.basename(os.path.dirname(task_file)) or "<unknown>"
    started = rec.get("timestamp")
    return task_id, started


def scan_for_output(path):
    """(said_something, n_lines, n_assistant). Stops at the first assistant turn.

    "Said something" means an assistant message exists, NOT that a `result` record
    exists -- a run that spoke and then hung is a stall, which is a different check's
    verdict, and conflating them would make this row fire on all 39 known stalls.
    """
    n_lines = n_assistant = 0
    try:
        with open(path, errors="replace") as fh:
            for line in fh:
                n_lines += 1
                # Cheap substring reject before parsing: most lines are not messages.
                if '"assistant"' not in line:
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if (rec.get("message") or {}).get("role") == "assistant":
                    n_assistant += 1
                    break
    except OSError:
        return None, n_lines, 0
    return n_assistant > 0, n_lines, n_assistant


def parse_iso(stamp):
    if not stamp:
        return None
    try:
        return datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    except ValueError:
        return None


def collect(now_utc, window_hours, transcripts, all_history=False):
    """Partition scheduled runs in the window into spoke / silent / undatable.

    Split from main() so a test can drive it with a directory of hand-built
    transcripts and no real session tree.
    """
    cutoff = now_utc - timedelta(hours=window_hours)
    spoke, silent, undatable = [], [], []
    for path in transcripts:
        attr = attribution(path)
        if attr is None:
            continue
        task_id, started = attr
        when = parse_iso(started)
        if when is None:
            # A transcript with no parseable start cannot be placed in the window.
            # It is NOT dropped: the five April silent runs have no timestamp field,
            # and dropping undatable records is how a whole format generation goes
            # unwatched. It is reported separately instead of guessed at via mtime,
            # which git does not preserve (memory mtime-freshness-unsound-for-git).
            said, n_lines, _ = scan_for_output(path)
            if said is False:
                undatable.append((task_id, path, n_lines))
            continue
        if not all_history and when < cutoff:
            continue
        said, n_lines, _ = scan_for_output(path)
        if said is None:
            undatable.append((task_id, path, n_lines))
        elif said:
            spoke.append((task_id, when, path))
        else:
            silent.append((task_id, when, path, n_lines))
    silent.sort(key=lambda r: (r[1], r[0]))
    return spoke, silent, undatable


def verdicts(now_utc, window_hours, transcripts, readable_tree, all_history=False):
    """The verdict rows. Pure function of the inputs so it is testable."""
    results = []

    # Cardinal rule first: a check that sees nothing passes everything.
    if not readable_tree:
        results.append((FAIL, (
            "silent-run detector: could not read the session tree at "
            f"{SESSION_GLOBS[0].split('/local-agent')[0]} -- this check is BLIND, "
            "which is not the same as clean. Under launchd this is usually TCC: the "
            "agent must be /bin/bash + a wrapper, never python3 directly (see the "
            "header of check_scheduled_commits.sh)"
        )))
        return results

    spoke, silent, undatable = collect(now_utc, window_hours, transcripts,
                                       all_history)
    scope = "all history" if all_history else f"the last {window_hours}h"

    if len(silent) >= CLUSTER_AT:
        tasks = sorted({r[0] for r in silent})
        first, last = silent[0][1], silent[-1][1]
        results.append((FAIL, (
            f"silent-run CLUSTER: {len(silent)} silent run(s) across {len(tasks)} "
            f"task(s) in {scope}, {first:%Y-%m-%d %H:%M}Z..{last:%Y-%m-%d %H:%M}Z. "
            f"This is ONE dispatch-layer fault, not {len(silent)} task faults -- do "
            f"not open {len(silent)} investigations. Tasks: {', '.join(tasks)}"
        )))
    else:
        for task_id, when, path, n_lines in silent:
            results.append((FAIL, (
                f"silent-run {task_id}: dispatched {when:%Y-%m-%d %H:%M}Z and "
                f"produced NO assistant turn ({n_lines} line(s) in {path}). This is "
                f"not a stall -- a stall leaves a long transcript with no result "
                f"record. This run never answered at all, so there is no blocking "
                f"tool to approve; look at the dispatch layer"
            )))

    if undatable:
        tasks = sorted({r[0] for r in undatable})
        results.append((WARN, (
            f"silent-run detector: {len(undatable)} silent run(s) carry no parseable "
            f"start time and could not be placed in a window, so they are reported "
            f"without a date rather than dropped: {', '.join(tasks)}"
        )))

    if not silent:
        if spoke:
            results.append((OK, (
                f"silent-run detector: {len(spoke)} scheduled run(s) in {scope}, all "
                f"produced output"
            )))
        else:
            # Readable tree, genuinely no runs in the window. On a machine that was
            # asleep (2026-10-19..10-23) this is the truth, not a fault -- but it is
            # a WARN, because "no runs at all" is also what a dead dispatcher looks
            # like and this check cannot tell those apart. check_scheduler_health's
            # did-it-fire rows can.
            results.append((WARN, (
                f"silent-run detector: NO scheduled run at all in {scope}, across "
                f"{len(transcripts)} transcript(s) on disk. The tree is readable, so "
                f"this is not blindness -- but an idle dispatcher and a dead one look "
                f"alike from here. Check the did-it-fire rows in scheduler_health.md"
            )))
    return results


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--window-hours", type=float, default=DEFAULT_WINDOW_HOURS,
                    help=f"window to report on (default {DEFAULT_WINDOW_HOURS})")
    ap.add_argument("--all-history", action="store_true",
                    help="census over every run ever, not the alarm window")
    ap.add_argument("--quiet", action="store_true",
                    help="print only WARN and FAIL lines")
    ap.add_argument("--status-file", metavar="PATH",
                    help="append one timestamped line per non-OK verdict, plus a "
                         "summary; this is what the morning report reads")
    args = ap.parse_args(argv)

    now_utc = datetime.now(timezone.utc)
    transcripts = discover_transcripts()

    # Readable means: the root exists AND we found at least one transcript. A root
    # that exists but yields nothing is the TCC failure shape -- the directory stats
    # fine and every open() inside it is refused.
    root = SESSION_GLOBS[0].split("/local-agent")[0]
    readable_tree = os.path.isdir(root) and bool(transcripts)

    results = verdicts(now_utc, args.window_hours, transcripts, readable_tree,
                       args.all_history)

    counts = {OK: 0, WARN: 0, FAIL: 0}
    for level, line in results:
        counts[level] += 1
        if level != OK or not args.quiet:
            print(f"{level:<5} {line}")

    summary = (
        f"{len(transcripts)} transcript(s) on disk: "
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

    if not readable_tree:
        return 2
    return 1 if counts[FAIL] else 0


if __name__ == "__main__":
    sys.exit(main())

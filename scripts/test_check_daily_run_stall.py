#!/usr/bin/env python3
"""Exercise every branch of check_daily_run_stall, especially the FAIL paths.

A guard that has never been watched failing is not a guard, and this one guards a
failure mode whose whole character is silence: a run that hangs on a permission
prompt writes nothing further and looks, by every timestamp, like a short run that
simply ended. So the cases that matter most are the ones where `check()` must return
False -- above all "no result record, quiet past grace", which must both fail AND
name the blocking tool, since the blocker migrates between tools and naming it is
the only thing that makes the pattern visible.

Two parsing cases are here because they were real bugs, not hypotheticals:

  * `file="..."` is backslash-escaped inside the JSON line, so a substring test for
    `file="` against the RAW line never matches. The first version of the script did
    exactly that and reported "no transcript was found" for a run whose transcript
    was sitting right there -- a false FAIL that would have looked like a second,
    different fault.
  * The `result` record is the finish signal. If `scan_transcript` missed it, every
    completed run would be reported as a stall.

    python3 scripts/test_check_daily_run_stall.py
"""

import json
import shutil
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_daily_run_stall as mod  # noqa: E402

SKILL = "/Users/x/Documents/Claude/Scheduled/t/SKILL.md"
SPEC = {"task_id": "t", "grace_minutes": 45}
FAILURES = []


def iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def expect(name, got, want):
    if got != want:
        FAILURES.append(f"{name}: expected {want!r}, got {got!r}")
        print(f"  FAIL {name}")
    else:
        print(f"  ok   {name}")


def write_transcript(dirpath, started, records):
    """One synthetic audit.jsonl in the real on-disk shape.

    The first line is the scheduled-task preamble exactly as the desktop app writes
    it -- a JSON string whose embedded quotes are escaped. json.dumps reproduces that
    escaping, which is the point: this is what tripped the raw-substring match.
    """
    session = dirpath / "acct" / "space" / f"local_{started[:19].replace(':', '')}"
    session.mkdir(parents=True, exist_ok=True)
    path = session / "audit.jsonl"
    lines = [json.dumps({
        "type": "user",
        "timestamp": started,
        "message": {"role": "user",
                    "content": f'<scheduled-task name="t" file="{SKILL}">\nrun it\n'},
    })]
    lines += [json.dumps(r) for r in records]
    path.write_text("\n".join(lines) + "\n")
    return path


def tool_use(name, stamp):
    return {"type": "assistant", "timestamp": stamp,
            "message": {"role": "assistant",
                        "content": [{"type": "tool_use", "name": name}]}}


def perm(subtype, name):
    """A permission_* system record. These carry no `timestamp` on disk."""
    return {"type": "system", "subtype": subtype, "tool_name": name}


def run(tasks, transcript_dir, now):
    mod.SESSIONS_GLOB = str(transcript_dir / "*/*/local_*/audit.jsonl")
    return mod.check(SPEC, tasks, quiet=True, now=now)


def main():
    tmp = Path(tempfile.mkdtemp(prefix="stallcheck-"))
    try:
        now = datetime.now(timezone.utc)
        ran = now - timedelta(hours=10)
        task = {"enabled": True, "lastRunAt": iso(ran), "filePath": SKILL}

        empty = tmp / "empty"
        empty.mkdir()

        print("cases that MUST fail:")

        expect("task absent from registry",
               run({}, empty, now)[0], False)
        expect("enabled but never ran",
               run({"t": {"enabled": True, "lastRunAt": None, "filePath": SKILL}},
                   empty, now)[0], False)
        expect("registry entry has no filePath",
               run({"t": {"enabled": True, "lastRunAt": iso(ran)}}, empty, now)[0],
               False)
        expect("ran but no transcript exists",
               run({"t": task}, empty, now)[0], False)

        # The failure this check exists for: no result record, silent well past grace.
        stalled = tmp / "stalled"
        write_transcript(stalled, iso(ran),
                         [tool_use("mcp__workspace__bash", iso(ran + timedelta(seconds=55)))])
        ok, line = run({"t": task}, stalled, now)
        expect("stalled run fails", ok, False)
        # Naming the blocker is half the value -- it migrates between tools, so a
        # verdict that only said "stalled" would hide the pattern this exists to show.
        expect("stalled verdict names the blocking tool",
               "mcp__workspace__bash" in line, True)
        expect("stalled verdict reports how long it has been silent",
               "silent for" in line, True)

        # The real shape of every observed hang: the prompt lands on one block of a
        # multi-block turn and the turn keeps emitting. Reporting the trailing block
        # named the wrong tool on 08-04 and 08-06, and the 08-04 misreading is what
        # got mcp__workspace__bash held back from approval.
        held = tmp / "held"
        write_transcript(held, iso(ran), [
            tool_use("mcp__gmail__unlabel_message", iso(ran + timedelta(seconds=50))),
            perm("permission_request", "mcp__gmail__unlabel_message"),
            tool_use("TaskUpdate", iso(ran + timedelta(seconds=51))),
        ])
        ok, line = run({"t": task}, held, now)
        expect("multi-block turn still fails", ok, False)
        expect("verdict names the tool holding the prompt",
               "mcp__gmail__unlabel_message" in line, True)
        expect("verdict does not name the trailing tool_use",
               "TaskUpdate" in line, False)

        # A transcript from some other day is not evidence about the run that just
        # happened; treating it as such would report a stale success.
        old = tmp / "old"
        write_transcript(old, iso(ran - timedelta(days=1)),
                         [{"type": "result", "timestamp": iso(ran - timedelta(days=1))}])
        expect("newest transcript predates the run stamp",
               run({"t": task}, old, now)[0], False)

        print("cases that MUST pass:")

        done = tmp / "done"
        write_transcript(done, iso(ran),
                         [tool_use("Bash", iso(ran + timedelta(minutes=3))),
                          {"type": "result", "timestamp": iso(ran + timedelta(minutes=7))}])
        expect("completed run passes", run({"t": task}, done, now)[0], True)

        # Mid-flight: no result yet, but it wrote a record inside the grace window.
        live_ran = now - timedelta(minutes=5)
        live = tmp / "live"
        write_transcript(live, iso(live_ran),
                         [tool_use("Bash", iso(now - timedelta(minutes=2)))])
        expect("run still inside the grace window passes",
               run({"t": {"enabled": True, "lastRunAt": iso(live_ran),
                          "filePath": SKILL}}, live, now)[0], True)

        expect("disabled is not a failure",
               run({"t": {"enabled": False, "lastRunAt": iso(ran), "filePath": SKILL}},
                   empty, now)[0], True)

        print("parsing cases (each was a real bug):")

        # The escaped-quote bug. attribution() must recover the path from the JSON
        # string, not from a substring match on the raw line.
        path = write_transcript(tmp / "parse", iso(ran), [])
        raw = path.read_text().splitlines()[0]
        expect("file=\" is escaped in the raw line", 'file="' in raw, False)
        expect("attribution recovers the SKILL path anyway",
               mod.attribution(str(path)), (SKILL, iso(ran)))

        # A file that is not a scheduled-task transcript must be rejected, not
        # mis-attributed to whatever task we happen to be checking.
        stray = tmp / "parse" / "stray.jsonl"
        stray.write_text(json.dumps({"type": "user", "timestamp": iso(ran),
                                     "message": {"content": "hello"}}) + "\n")
        expect("non-task transcript is not attributed",
               mod.attribution(str(stray)), None)

        scanned = mod.scan_transcript(str(write_transcript(
            tmp / "parse2", iso(ran),
            [tool_use("Edit", iso(ran)),
             {"type": "result", "timestamp": iso(ran + timedelta(minutes=1))}])))
        expect("scan sees the result record", scanned["finished"], True)
        expect("scan falls back to the last tool_use when nothing prompted",
               scanned["blocked_tool"], "Edit")

        # An ANSWERED request is not a blocker. Every run, finished or not, carries
        # several of these; if they were not cleared, the first prompt of the morning
        # would be reported as the blocker for the rest of the day.
        answered = mod.scan_transcript(str(write_transcript(
            tmp / "parse3", iso(ran),
            [perm("permission_request", "mcp__gmail__search_threads"),
             perm("permission_response", "mcp__gmail__search_threads"),
             tool_use("Edit", iso(ran))])))
        expect("an answered request does not count as the blocker",
               answered["blocked_tool"], "Edit")

        auto = mod.scan_transcript(str(write_transcript(
            tmp / "parse4", iso(ran),
            [perm("permission_request", "mcp__gmail__create_draft"),
             perm("permission_auto_approved", "mcp__gmail__create_draft"),
             tool_use("Edit", iso(ran))])))
        expect("approvedPermissions auto-approval clears the request too",
               auto["blocked_tool"], "Edit")

        if FAILURES:
            print(f"\n{len(FAILURES)} case(s) wrong:")
            for f in FAILURES:
                print("  " + f)
            return 1
        print("\nall cases correct")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Drive every verdict path of check_silent_runs, against hand-built transcripts.

A guard nobody has watched fail is not a guard. The cases here are the ones that
must NOT come back OK, and each corresponds to a real way this detector could be
made useless:

  - a dispatched run with no assistant turn is a FAIL (the whole point)
  - a run that SPOKE and then hung is NOT this check's FAIL -- that is a stall, and
    firing on it would duplicate check_daily_run_stall and make both untrustworthy
  - a cluster collapses to ONE row, not N rows (08-27 was one fault, not fourteen)
  - history outside the window is NOT re-reported (an alarm that repeats is ignored)
  - an UNREADABLE session tree is a FAIL, never an OK (silence != health)
  - a readable-but-empty window is a WARN, not an OK and not a FAIL
  - a run with no parseable start is reported undated, never dropped
  - BOTH session-directory schemes are discovered (local_* and 8-hex)

That last one is not hypothetical: keying on sessionId instead of the transcript's
own first line made 719 real runs invisible on 2026-10-23, and the same blind spot
in check_daily_run_stall's local_*-only glob had been hiding every run since the
2026-09-15 changeover.

    python3 scripts/test_check_silent_runs.py
"""

import json
import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_silent_runs as mod  # noqa: E402

FAILURES = []
NOW = datetime(2026, 8, 27, 13, 0, tzinfo=timezone.utc)


def expect(name, got, want):
    if got != want:
        FAILURES.append(f"{name}: expected {want!r}, got {got!r}")
        print(f"  FAIL {name}\n         expected {want!r}\n         got      {got!r}")
    else:
        print(f"  ok   {name}")


def dispatch_line(task_id, when):
    """The first line of a real transcript, in the shape attribution() parses."""
    rec = {
        "type": "user",
        "timestamp": when.strftime("%Y-%m-%dT%H:%M:%S.000Z") if when else None,
        "message": {
            "role": "user",
            "content": (f'<scheduled-task name="{task_id}" '
                        f'file="/Users/tom/Documents/Claude/Scheduled/{task_id}'
                        f'/SKILL.md">\nThis is an automated run.'),
        },
    }
    if when is None:
        rec.pop("timestamp")
    return json.dumps(rec)


def assistant_line():
    return json.dumps({"type": "assistant",
                       "message": {"role": "assistant", "content": "working on it"}})


def tool_line():
    """A tool_use turn with no assistant role -- a stall's trailing shape."""
    return json.dumps({"type": "tool_use", "name": "Bash"})


def result_line():
    return json.dumps({"type": "result", "subtype": "success"})


def make_run(root, task_id, when, lines, scheme="local"):
    """Write one transcript under a session tree matching the real layout.

    scheme="local" -> <session>/local_<uuid>/audit.jsonl   (pre 2026-09-15)
    scheme="hex"   -> <session>/<8-hex>/audit.jsonl        (current)
    """
    n = len(list(Path(root).rglob("audit.jsonl")))
    name = f"local_{n:08d}-0000-0000-0000-000000000000" if scheme == "local" \
        else f"{n:08x}"
    d = Path(root) / "local-agent-mode-sessions" / "acct" / "sess" / name
    d.mkdir(parents=True, exist_ok=True)
    body = [dispatch_line(task_id, when)] + lines
    (d / "audit.jsonl").write_text("\n".join(body) + "\n")
    return str(d / "audit.jsonl")


def globs_for(root):
    base = os.path.join(root, "local-agent-mode-sessions", "*", "*")
    return [os.path.join(base, "local_*", "audit.jsonl"),
            os.path.join(base, "*", "audit.jsonl")]


def levels(results):
    return [lvl for lvl, _ in results]


def run(root, window=26, all_history=False, readable=True):
    tr = mod.discover_transcripts(globs_for(root))
    return mod.verdicts(NOW, window, tr, readable, all_history)


def main():
    print("a dispatched run that never spoke (the whole point):")
    with tempfile.TemporaryDirectory() as t:
        make_run(t, "summa-qc-sweep", NOW - timedelta(hours=1), [])
        r = run(t)
        expect("a silent run is a FAIL", levels(r), [mod.FAIL])
        expect("the row names the task", "summa-qc-sweep" in r[0][1], True)
        expect("the row says NO assistant turn",
               "NO assistant turn" in r[0][1], True)
        # The actionable half: a reader must not go hunting for a tool to approve.
        expect("the row distinguishes itself from a stall",
               "not a stall" in r[0][1], True)

    print("\na run that SPOKE and then hung is a STALL, not this check's business:")
    with tempfile.TemporaryDirectory() as t:
        # Long transcript, assistant turns, no result record -- textbook stall. If
        # this ever FAILs here, this detector has become a duplicate of
        # check_daily_run_stall and both become noise.
        make_run(t, "c282-wiki-agent-daily-run", NOW - timedelta(hours=1),
                 [assistant_line(), tool_line()] * 20)
        expect("a stall is NOT reported by this check", levels(run(t)), [mod.OK])

    print("\na finished run is clean:")
    with tempfile.TemporaryDirectory() as t:
        make_run(t, "summa-2026-daily-batch", NOW - timedelta(hours=2),
                 [assistant_line(), result_line()])
        r = run(t)
        expect("a healthy run is OK", levels(r), [mod.OK])
        expect("the OK row counts the runs it checked", "1 scheduled run" in r[0][1],
               True)

    print("\nthe 2026-08-27 cluster must collapse to ONE row, not fourteen:")
    with tempfile.TemporaryDirectory() as t:
        tasks = ["summa-qc-sweep", "summa-commentary-reviewer",
                 "summa-2026-nightly-verification", "c2a2-agent-stump-fredrickson",
                 "c282-wiki-agent-daily-run", "summa-2026-daily-batch",
                 "metabolism-regen-daily", "scheduler-health-check"]
        for i in range(14):
            make_run(t, tasks[i % len(tasks)], NOW - timedelta(hours=12 - i * 0.5), [])
        r = run(t)
        expect("fourteen silent runs give ONE verdict row", len(r), 1)
        expect("that row is a FAIL", r[0][0], mod.FAIL)
        expect("it is labelled a CLUSTER", "CLUSTER" in r[0][1], True)
        expect("it counts the runs", "14 silent run(s)" in r[0][1], True)
        # The reason the cluster row exists at all.
        expect("it says ONE fault, not N", "not 14 task faults" in r[0][1], True)

    print("\ntwo is not a cluster (a cluster row would hide which tasks):")
    with tempfile.TemporaryDirectory() as t:
        make_run(t, "summa-qc-sweep", NOW - timedelta(hours=3), [])
        make_run(t, "supabase-c2a2-keep-warm", NOW - timedelta(hours=2), [])
        r = run(t)
        expect("two silent runs are listed individually", len(r), 2)
        expect("both are FAILs", levels(r), [mod.FAIL, mod.FAIL])

    print("\nsettled history must NOT be re-reported every morning:")
    with tempfile.TemporaryDirectory() as t:
        # The real 08-27 cluster, seen from 2026-10-23. Re-alarming on it daily is
        # how a row stops being read.
        for i in range(14):
            make_run(t, "summa-qc-sweep", NOW - timedelta(days=57, hours=i), [])
        make_run(t, "morning-system-health", NOW - timedelta(hours=2),
                 [assistant_line(), result_line()])
        r = run(t, window=26)
        expect("old silent runs are outside the window", levels(r), [mod.OK])
        # ...but must still be findable on demand, or the census is lost.
        expect("--all-history still finds them",
               levels(run(t, all_history=True)), [mod.FAIL])

    print("\nblindness must never read as health:")
    with tempfile.TemporaryDirectory() as t:
        make_run(t, "summa-qc-sweep", NOW - timedelta(hours=1), [])
        r = run(t, readable=False)
        expect("an unreadable tree is a FAIL", levels(r), [mod.FAIL])
        expect("it says it is BLIND", "BLIND" in r[0][1], True)
        # The actual cause, every time it has happened here.
        expect("it names the TCC/bash cause", "TCC" in r[0][1], True)
        # And it must not also report the silent run it cannot be sure it saw.
        expect("a blind check reports nothing else", len(r), 1)

    print("\na readable but empty window is a WARN, not OK and not FAIL:")
    with tempfile.TemporaryDirectory() as t:
        # The 10-19..10-23 sleep: genuinely no runs. Not a fault -- but an idle
        # dispatcher and a dead one look identical from here, so it cannot be OK.
        make_run(t, "summa-qc-sweep", NOW - timedelta(days=40),
                 [assistant_line(), result_line()])
        r = run(t, window=26)
        expect("no runs in window is a WARN", levels(r), [mod.WARN])
        expect("it says the tree was readable", "not blindness" in r[0][1], True)

    print("\nundatable runs are reported, never dropped:")
    with tempfile.TemporaryDirectory() as t:
        # The five April silent runs carry no timestamp field. Dropping them is how
        # an entire format generation goes unwatched.
        make_run(t, "morning-project-status", None, [])
        make_run(t, "morning-system-health", NOW - timedelta(hours=1),
                 [assistant_line(), result_line()])
        r = run(t)
        expect("an undatable silent run is reported", mod.WARN in levels(r), True)
        warn = [l for lvl, l in r if lvl == mod.WARN][0]
        expect("it is named", "morning-project-status" in warn, True)
        expect("it says why it has no date", "no parseable start time" in warn, True)

    print("\nBOTH directory schemes must be discovered (719 runs were invisible):")
    with tempfile.TemporaryDirectory() as t:
        make_run(t, "summa-qc-sweep", NOW - timedelta(hours=2), [], scheme="local")
        make_run(t, "openstory-agents-telemetry-refresh", NOW - timedelta(hours=1),
                 [], scheme="hex")
        tr = mod.discover_transcripts(globs_for(t))
        expect("both schemes found, de-duplicated", len(tr), 2)
        r = run(t)
        expect("both are reported", len(r), 2)
        names = " ".join(l for _, l in r)
        expect("the 8-hex run is not skipped",
               "openstory-agents-telemetry-refresh" in names, True)
        # The regression that hid them: a local_*-only glob.
        only_local = [globs_for(t)[0]]
        expect("a local_*-only glob STILL misses the 8-hex run (this is the bug)",
               len(mod.discover_transcripts(only_local)), 1)

    print("\nattribution comes from the transcript, not the directory name:")
    with tempfile.TemporaryDirectory() as t:
        p = make_run(t, "c2a2-lit-search-pipeline", NOW - timedelta(hours=1), [],
                     scheme="hex")
        got = mod.attribution(p)
        expect("task id read from the SKILL.md path", got[0],
               "c2a2-lit-search-pipeline")
        # A non-task session must be ignored entirely, or every interactive Cowork
        # session becomes a scheduled-run verdict.
        d = Path(os.path.dirname(p))
        (d / "audit.jsonl").write_text(json.dumps(
            {"message": {"role": "user", "content": "hello, not a scheduled task"}})
            + "\n")
        expect("a non-scheduled session is not attributed", mod.attribution(p), None)
        expect("and contributes no verdict", levels(run(t)), [mod.WARN])

    print("\nthe live session tree must be reachable (this check's own premise):")
    tr = mod.discover_transcripts()
    expect("the real glob finds transcripts", len(tr) > 100, True)
    # Both schemes must be present in reality, not just in the fixtures.
    expect("real local_* runs exist", any("/local_" in p for p in tr), True)
    expect("real 8-hex runs exist", any("/local_" not in p for p in tr), True)
    attributed = [p for p in tr[:400] if mod.attribution(p)]
    expect("real transcripts attribute to tasks", len(attributed) > 0, True)

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

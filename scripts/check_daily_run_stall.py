#!/usr/bin/env python3
"""Assert that a scheduled run FINISHED, and name the tool it hung on if it did not.

Why this exists
---------------
Measured 2026-08-04 over all 110 `c282-wiki-agent-daily-run` transcripts: 39 never
reached the end. An unattended run that raises a tool-permission prompt at 04:35 has
nobody to answer it, and **nothing anywhere times it out** -- it hangs until the
permission stream closes, which in the worst observed case was 5.1 days later, when
the Mac went to sleep. The agent then receives a synthesized "the user doesn't want
to take this action right now" and stops mid-phase. See memory
`scheduled-runs-hang-on-permission-prompts`.

`check_scheduled_commits.py` is the sibling of this check and does not cover it. It
asks "did a commit land", which is the *aftermath*; it cannot say whether the run is
still sitting there holding a prompt, and it cannot say **which tool** blocked. That
last part is the actionable half: the blocker is not predictable from the call (every
recent one was a read-only command) and it migrates -- approving `create_draft` in
2026-05 stopped that tool stalling and the hang simply moved to the next un-approved
tool. Naming it each time is what makes the pattern visible.

How a stall is detected
-----------------------
The desktop app writes one `audit.jsonl` per scheduled run, under

    ~/Library/Application Support/Claude/local-agent-mode-sessions/*/*/local_*/

whose first line carries `<scheduled-task ... file="<the task's SKILL.md>">`, which is
how a transcript is attributed to a task. A run that reaches the end emits a record of
`"type": "result"`. Across those 110 transcripts that record is present in exactly the
71 that finished and absent from all 39 that did not.

Naming the blocker reads the app's own `permission_request` record, whose `tool_name`
field IS the tool holding the prompt; an unanswered one (no following
`permission_response` or `permission_auto_approved`) is the blocker. The trailing
`tool_use` block survives only as a fallback for a stall with no permission record at
all. It was the original signal and it is **wrong whenever a model turn emits several
tool_use blocks and the prompt lands on an early one** -- which is the normal case, not
a corner: on 2026-08-06 the run was held on a Gmail `unlabel_message` while the last
block in the turn was `TaskUpdate`, and on 2026-08-04 it was held on the same Gmail
call while the last block was `mcp__workspace__bash`. Both were reported as the wrong
tool for two days, and the 08-04 misreading is what put `mcp__workspace__bash` on the
do-not-approve list.

So: **no `result` record == did not finish.** Elapsed time is deliberately NOT the
signal -- a hung transcript stops being written the moment it hangs, so a 5-day stall
and a 51-second one look identical by duration. Duration is only used to decide
whether a run is still legitimately in flight (longest clean run observed: 535s).

Report-only, by design
----------------------
This does not terminate anything and does not touch `approvedPermissions`. Tom's call
2026-08-04: do not widen auto-approval for an agent that holds `git push` rights to a
public repo. The verdict goes to `scheduler/run_stall.md`, which `morning-system-health`
reads at 06:00.

`approvedPermissions`, on the task's own registry entry, is the ONLY allowlist these
runs honour -- it is what emits `permission_auto_approved`, and it is written by
answering a prompt with "always allow" in the app. A `permissions.allow` block in
`.claude/settings.json` does nothing here: the run's cwd is its own `outputs/`
directory under Application Support, so the project file is never discovered, and the
14 entries added to the global file on 2026-08-05 changed nothing -- on 08-06 all four
Gmail tools listed there prompted exactly as they had on 08-02 and 08-04.

Re-measured over 111 transcripts once the blocker was read from `permission_request`
instead of the trailing `tool_use`: 71 finished, 40 did not, and the blockers are Gmail
`unlabel_message` 14, `unlabel_thread` 5, `create_draft` 5 (all before it was approved
in 2026-05), `label_thread` 2 -- 26 of 40 -- then `allow_cowork_file_delete` 5,
`Bash`/`mcp__workspace__bash` 2 each, `TaskUpdate` 2, `move_file` and `start_process` 1
each.

Usage
-----
    python3 scripts/check_daily_run_stall.py
    python3 scripts/check_daily_run_stall.py --quiet
    python3 scripts/check_daily_run_stall.py --status-file scheduler/run_stall.md
"""

import argparse
import glob
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_scheduled_commits as commits  # noqa: E402  (registry loading, shared)

REPO = commits.REPO

SESSIONS_GLOB = os.path.expanduser(
    "~/Library/Application Support/Claude/local-agent-mode-sessions"
    "/*/*/local_*/audit.jsonl"
)

# grace_minutes must exceed the task's real runtime with room to spare. The longest
# clean daily run measured across 110 transcripts is 535s (~9 min); 45 min is five
# times that and still well inside the 75-minute gap between the 04:30 start and the
# 05:45 check, so a verdict at check time is never a guess about a live run.
CHECKS = [
    {
        "task_id": "c282-wiki-agent-daily-run",
        "grace_minutes": 45,
        "note": "taskId carries a c282/c2a2 typo baked in; do not rename",
    },
]


def attribution(path):
    """(task_file, started) from a transcript's first line, or None.

    Cheap on purpose: there are thousands of these files and only a hundred belong to
    any one task, so attribution reads one line and the full scan happens only for the
    handful that match.
    """
    try:
        with open(path, errors="replace") as fh:
            first = fh.readline()
    except OSError:
        return None
    # Cheap reject on the raw line. Only `<scheduled-task` can be matched here --
    # the quotes of `file="..."` are backslash-escaped inside the JSON string, so
    # that part is checked after decoding.
    if "<scheduled-task" not in first:
        return None
    try:
        rec = json.loads(first)
    except ValueError:
        return None
    content = (rec.get("message") or {}).get("content")
    if not isinstance(content, str) or 'file="' not in content:
        return None
    return content.split('file="', 1)[1].split('"', 1)[0], rec.get("timestamp")


def scan_transcript(path):
    """Did this run finish, when did it last write, and what was it waiting on."""
    last_ts = None
    finished = False
    last_tool = None
    pending_permission = None
    try:
        with open(path, errors="replace") as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if rec.get("type") == "result":
                    finished = True
                if rec.get("timestamp"):
                    last_ts = rec["timestamp"]
                # The transcript says outright which tool raised a prompt. A request
                # with no answer after it is the tool the run is sitting on; prompts
                # are serial, so the next answer of any kind clears the outstanding
                # one.
                subtype = rec.get("subtype")
                if subtype == "permission_request":
                    pending_permission = rec.get("tool_name")
                elif subtype in ("permission_response", "permission_auto_approved"):
                    pending_permission = None
                # Fallback only. A model turn can emit several tool_use blocks at
                # once, and the one that prompts need not be the last -- on
                # 2026-08-06 the prompt was on the first of three, so the trailing
                # block named TaskUpdate while the run was held on a Gmail call.
                content = (rec.get("message") or {}).get("content")
                if isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict) and block.get("type") == "tool_use":
                            last_tool = block.get("name")
    except OSError:
        return None
    return {"last_ts": last_ts, "finished": finished,
            "blocked_tool": pending_permission or last_tool}


def newest_transcript_for(task_file, sessions_glob):
    """The most recently started transcript attributed to this task, or None.

    `sessions_glob` is passed rather than defaulted so the module global is read at
    call time -- a default argument would freeze it at import and make the glob
    untestable.
    """
    best_path, best_started = None, None
    for path in glob.glob(sessions_glob):
        attr = attribution(path)
        if attr is None:
            continue
        found_file, started = attr
        if found_file != task_file or not started:
            continue
        if best_started is None or started > best_started:
            best_path, best_started = path, started
    if best_path is None:
        return None
    info = scan_transcript(best_path)
    if info is None:
        return None
    info.update(path=best_path, task_file=task_file, started=best_started)
    return info


def check(spec, tasks, quiet, now=None):
    """Return (ok, one_line_verdict). The line is what the morning report reads."""
    tid = spec["task_id"]
    task = tasks.get(tid)
    now = now or datetime.now(timezone.utc)

    def say(ok, line, detail=""):
        if not ok or not quiet:
            print(("OK    " if ok else "FAIL  ") + line + detail)
        return ok, ("OK   " if ok else "FAIL ") + line

    if task is None:
        return say(False, f"{tid}: not in any registry — deleted, or the registry moved")

    if not task.get("enabled", False):
        return say(True, f"{tid}: disabled in the registry")

    if not task.get("lastRunAt"):
        return say(False, f"{tid}: enabled but has never run")

    task_file = task.get("filePath")
    if not task_file:
        return say(False, f"{tid}: registry entry has no filePath — cannot find its transcript")

    ran = commits.parse_iso(task["lastRunAt"]).astimezone(timezone.utc)
    info = newest_transcript_for(task_file, SESSIONS_GLOB)

    # No transcript for a run the registry says happened is itself a failure: it means
    # either the run left no record or the transcript layout moved under us. Silence
    # here would read as health.
    if info is None:
        return say(False, f"{tid}: ran {ran:%Y-%m-%d %H:%M}Z but no transcript was found",
                   detail=f"\n      looked in {SESSIONS_GLOB}")

    started = commits.parse_iso(info["started"]).astimezone(timezone.utc)
    if abs((started - ran).total_seconds()) > 2 * 3600:
        return say(False,
                   f"{tid}: newest transcript starts {started:%Y-%m-%d %H:%M}Z but the "
                   f"registry's last run is {ran:%Y-%m-%d %H:%M}Z — no record of that run")

    if info["finished"]:
        return say(True, f"{tid}: run of {started:%Y-%m-%d %H:%M}Z completed")

    last_ts = commits.parse_iso(info["last_ts"]).astimezone(timezone.utc) if info["last_ts"] else started
    quiet_for = (now - last_ts).total_seconds() / 60

    if quiet_for < spec["grace_minutes"]:
        return say(True, f"{tid}: run of {started:%Y-%m-%d %H:%M}Z still in flight "
                         f"({quiet_for:.0f}m since its last record, "
                         f"{spec['grace_minutes']}m grace)")

    tool = info["blocked_tool"] or "unknown"
    return say(
        False,
        f"{tid}: run of {started:%Y-%m-%d %H:%M}Z never finished — silent for "
        f"{quiet_for / 60:.1f}h, blocked on {tool}",
        detail="\n      an unattended run holding a permission prompt hangs until the "
               "permission stream closes\n"
               f"      (worst observed: 5.1 days). Transcript: {info['path']}",
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true",
                    help="print only failures (for cron / morning-health)")
    ap.add_argument("--status-file", metavar="PATH",
                    help="append one timestamped line per check, repo-relative; "
                         "this is what morning-system-health reads")
    args = ap.parse_args()

    tasks, paths = commits.load_registry_tasks()
    if not paths:
        print(f"FAIL  no registry matched {commits.REGISTRY_GLOB}", file=sys.stderr)
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

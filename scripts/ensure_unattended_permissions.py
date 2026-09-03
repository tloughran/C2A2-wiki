#!/usr/bin/env python3
"""ensure_unattended_permissions.py — keep the unattended permission fields on the
scheduled tasks that need them, durably.

THE PROBLEM. `permissionMode: bypassPermissions` (plus `chromePermissionMode`) is
what stops c282-wiki-agent-daily-run from blocking forever on the first approval
prompt for a tool it has not pre-approved — 8 stalls in 30 days, worst hold 5.1
days, each on a different tool. The field lives ONLY in the desktop app's
scheduled-tasks.json; there is no SKILL.md frontmatter or per-task config that can
declare it, so the registry is the only place to put it.

WHY A HAND EDIT DOES NOT STICK. The app holds the task list in memory and writes
the whole file back out from that memory. An edit made while the app is running is
overwritten with no other symptom: the daily run commits its work BEFORE it blocks,
so lastRunAt stays current and every artifact check stays green. This is exactly
what happened on 2026-09-03: applied 12:49, gone by 16:28.

THE MECHANISM. Write only while the app is NOT running, and check often enough to
catch a window. Launched by com.c2a2.unattended-permissions at load and every 10
minutes: if the fields are already right it does nothing; if they are wrong and
Claude is up it defers and says so; if they are wrong and Claude is down it patches
and the app picks the file up on its next launch.

This does not replace the falsifier. check_scheduler_health.py asserts the fields
against the LIVE registry and turns the panel red when they are missing, whatever
this script did or did not manage to do. If the panel is red and this log says
DEFERRED for days, the answer is still: quit Claude, run this once, relaunch.

    python3 scripts/ensure_unattended_permissions.py [--dry-run] [--verbose]

Exit codes:  0 fields present   75 deferred (app running)   1 error
"""
import argparse
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys

REGISTRY_GLOB = os.path.expanduser(
    "~/Library/Application Support/Claude/local-agent-mode-sessions"
    "/*/*/scheduled-tasks.json")

LOG_PATH = os.path.expanduser("~/Library/Logs/c2a2-unattended-permissions.log")

# Tasks that must never wait for a human, and the fields that make that true.
# Keep in step with UNATTENDED_PERMISSION_TASKS in check_scheduler_health.py.
REQUIRED = {
    "c282-wiki-agent-daily-run": {
        "permissionMode": "bypassPermissions",
        "chromePermissionMode": "skip_all_permission_checks",
    },
}

EX_DEFERRED = 75


def log(msg):
    line = f"{datetime.datetime.now().astimezone().isoformat(timespec='seconds')}  {msg}"
    # Under launchd, stdout is redirected to LOG_PATH itself, so printing as well
    # would write every line twice. Interactive runs still want to see it.
    if sys.stdout.isatty():
        print(line)
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


APP_BUNDLE_MARKER = "Claude.app/Contents/"


def claude_is_running():
    """True if the Claude desktop app has any live process.

    Matches the app bundle path against the full argument list, so a `claude` CLI
    or a shell function of that name is not mistaken for the app that owns the
    registry. Helper processes count: they only exist while the app is up.

    NOT pgrep. On this machine `pgrep -f 'Claude.app/Contents/MacOS/Claude'`
    returns nothing while that exact process is in `ps`, and `pgrep -x Claude`
    misses it too. A false "not running" is the one answer that causes the damage
    this script exists to prevent, so the check reads `ps` directly, and any
    failure to determine the answer is treated as RUNNING.
    """
    try:
        r = subprocess.run(["ps", "-Ao", "args="],
                           capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return True
    if r.returncode != 0:
        return True
    return any(APP_BUNDLE_MARKER in line for line in r.stdout.splitlines())


def find_task(tasks, name):
    for t in tasks:
        if isinstance(t, dict) and t.get("filePath", "").rstrip("/").endswith(
                f"/{name}/SKILL.md"):
            return t
    return None


def missing_fields(task, wanted):
    return {k: v for k, v in wanted.items() if task.get(k) != v}


def registries():
    return sorted(glob.glob(REGISTRY_GLOB))


def survey():
    """Return [(path, task_name, task, missing_dict)] for every required task found."""
    found = []
    for path in registries():
        try:
            with open(path, encoding="utf-8") as f:
                doc = json.load(f)
        except (OSError, ValueError) as e:
            log(f"WARN  unreadable registry {path}: {e}")
            continue
        tasks = doc.get("scheduledTasks") or []
        for name, wanted in REQUIRED.items():
            t = find_task(tasks, name)
            if t is not None:
                found.append((path, name, t, missing_fields(t, wanted)))
    return found


def patch(path, dry_run=False):
    """Re-apply every required field in one registry. Aborts if the file changes
    underneath us, so a write racing the app's own write can never half-land."""
    before = os.stat(path).st_mtime_ns
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    changed = []
    for name, wanted in REQUIRED.items():
        t = find_task(doc.get("scheduledTasks") or [], name)
        if t is None:
            continue
        for k, v in missing_fields(t, wanted).items():
            t[k] = v
            changed.append(f"{name}.{k}={v}")
    if not changed:
        return []
    if dry_run:
        log(f"DRY-RUN would set: {', '.join(changed)}  in {path}")
        return changed

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(path, f"{path}.bak.{stamp}")
    tmp = f"{path}.tmp.{os.getpid()}"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2)
        f.write("\n")
    if os.stat(path).st_mtime_ns != before:
        os.unlink(tmp)
        raise RuntimeError("registry changed while patching — aborted, nothing written")
    os.replace(tmp, path)
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would change; write nothing")
    ap.add_argument("--verbose", action="store_true",
                    help="log even when there is nothing to do")
    args = ap.parse_args()

    found = survey()
    if not found:
        log("ERROR no registry contains any required task — check REGISTRY_GLOB "
            f"({REGISTRY_GLOB}) and the task names in REQUIRED")
        return 1

    stale = [(p, n, m) for p, n, _, m in found if m]
    if not stale:
        if args.verbose:
            log(f"OK    {len(found)} task(s) already carry their unattended fields")
        return 0

    detail = "; ".join(f"{n} missing {sorted(m)}" for _, n, m in stale)
    running = claude_is_running()
    if running and not args.dry_run:
        log(f"DEFER Claude is running; not writing. {detail}. "
            "Will retry on the next run, or quit Claude and run this once.")
        return EX_DEFERRED

    for path in sorted({p for p, _, _ in stale}):
        try:
            changed = patch(path, dry_run=args.dry_run)
        except (OSError, ValueError, RuntimeError) as e:
            log(f"ERROR patching {path}: {e}")
            return 1
        if changed and not args.dry_run:
            log(f"SET   {', '.join(changed)}  in {path}")

    if args.dry_run:
        return EX_DEFERRED if running else 0

    remaining = [n for _, n, _, m in survey() if m]
    if remaining:
        log(f"ERROR fields still missing after patch: {sorted(set(remaining))}")
        return 1
    log("OK    unattended fields re-applied; they take effect at the app's next launch")
    return 0


if __name__ == "__main__":
    sys.exit(main())

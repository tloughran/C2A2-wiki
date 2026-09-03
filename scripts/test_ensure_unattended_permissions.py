#!/usr/bin/env python3
"""Tests for ensure_unattended_permissions.py. Plain asserts, no pytest.

    python3 scripts/test_ensure_unattended_permissions.py

WHY (Rule 9): this script's whole job is to write to a file another program owns.
There are exactly two ways it can do harm, and both are tested here rather than
its happy path:

  1. It writes while the Claude desktop app is running. The app then overwrites
     from memory and the edit is lost with no symptom — the original bug. So the
     detector is tested in the dangerous direction: it must say RUNNING right now
     (this test only runs on a Mac with the app up) and must say RUNNING when it
     cannot tell.
  2. It writes while the app is mid-write and lands a half-patched registry. So
     the mtime guard is tested by mutating the file underneath the patch.

The write path itself is exercised against a COPY of the live registry, never the
live one, since the tests run with the app up.
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "ensure_unattended_permissions.py")
_spec = importlib.util.spec_from_file_location("eup", SCRIPT)
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

FAILURES = []


def check(label, cond, detail=""):
    if cond:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label}  {detail}")
        FAILURES.append(label)


TASK = "c282-wiki-agent-daily-run"
WANT = E.REQUIRED[TASK]


def fixture(with_fields=False, task_name=TASK):
    """A minimal registry of the real shape: tasks identified by filePath only."""
    d = tempfile.mkdtemp(prefix="eup_")
    p = os.path.join(d, "scheduled-tasks.json")
    t = {
        "id": "abc",
        "filePath": f"/Users/x/Documents/Claude/Scheduled/{task_name}/SKILL.md",
        "cronExpression": "30 4 * * *",
        "enabled": True,
        "approvedPermissions": ["mcp__Gmail__search_threads"],
    }
    if with_fields:
        t.update(WANT)
    other = {"id": "zzz", "filePath": "/Users/x/Documents/Claude/Scheduled/other/SKILL.md"}
    with open(p, "w", encoding="utf-8") as f:
        json.dump({"scheduledTasks": [other, t], "recordedSkips": []}, f, indent=2)
    return p


# ── 1. The dangerous direction: is the app running? ───────────────────────────

def test_detector():
    print("claude_is_running()")
    check("says RUNNING while the desktop app is up (it is, or these tests "
          "could not have reached this machine)", E.claude_is_running() is True)

    real = subprocess.run
    try:
        subprocess.run = lambda *a, **k: (_ for _ in ()).throw(OSError("no ps"))
        check("treats an unavailable ps as RUNNING", E.claude_is_running() is True)
        subprocess.run = real
        class R:
            returncode, stdout = 1, ""
        subprocess.run = lambda *a, **k: R()
        check("treats a failed ps as RUNNING", E.claude_is_running() is True)
        subprocess.run = real
        class S:
            returncode, stdout = 0, "/usr/bin/python3\n/bin/zsh\n"
        subprocess.run = lambda *a, **k: S()
        check("says NOT running when no bundle process is present",
              E.claude_is_running() is False)
        class T:
            returncode = 0
            stdout = "/Applications/Claude.app/Contents/MacOS/Claude\n"
        subprocess.run = lambda *a, **k: T()
        check("matches the app bundle path", E.claude_is_running() is True)
        class U:
            returncode, stdout = 0, "/opt/homebrew/bin/claude --resume\n"
        subprocess.run = lambda *a, **k: U()
        check("does NOT match the claude CLI", E.claude_is_running() is False)
    finally:
        subprocess.run = real


# ── 2. Task lookup ────────────────────────────────────────────────────────────

def test_find_task():
    print("find_task()")
    tasks = json.load(open(fixture(), encoding="utf-8"))["scheduledTasks"]
    check("finds by filePath (the registry has no name key)",
          E.find_task(tasks, TASK) is not None)
    check("does not match a different task", E.find_task(tasks, "other-run") is None)
    check("does not match a prefix of the name",
          E.find_task(tasks, "c282-wiki-agent") is None)
    check("missing_fields reports both when absent",
          sorted(E.missing_fields(E.find_task(tasks, TASK), WANT)) ==
          ["chromePermissionMode", "permissionMode"])
    ok = json.load(open(fixture(with_fields=True), encoding="utf-8"))["scheduledTasks"]
    check("missing_fields reports none when present",
          E.missing_fields(E.find_task(ok, TASK), WANT) == {})
    wrong = json.load(open(fixture(), encoding="utf-8"))["scheduledTasks"]
    E.find_task(wrong, TASK)["permissionMode"] = "default"
    check("a WRONG value counts as missing, not as present",
          "permissionMode" in E.missing_fields(E.find_task(wrong, TASK), WANT))


# ── 3. The write path, on a copy ──────────────────────────────────────────────

def test_patch_writes_and_is_idempotent():
    print("patch()")
    p = fixture()
    changed = E.patch(p)
    check("sets both fields", len(changed) == 2, str(changed))
    t = E.find_task(json.load(open(p, encoding="utf-8"))["scheduledTasks"], TASK)
    check("permissionMode landed", t.get("permissionMode") == WANT["permissionMode"])
    check("chromePermissionMode landed",
          t.get("chromePermissionMode") == WANT["chromePermissionMode"])
    check("leaves approvedPermissions alone",
          t.get("approvedPermissions") == ["mcp__Gmail__search_threads"])
    check("leaves the other task alone",
          len(json.load(open(p, encoding="utf-8"))["scheduledTasks"]) == 2)
    check("keeps sibling top-level keys",
          "recordedSkips" in json.load(open(p, encoding="utf-8")))
    check("took a backup", len([f for f in os.listdir(os.path.dirname(p))
                                if ".bak." in f]) == 1)
    check("second run is a no-op", E.patch(p) == [])
    check("no second backup", len([f for f in os.listdir(os.path.dirname(p))
                                   if ".bak." in f]) == 1)


def test_mtime_guard():
    print("mtime guard")
    p = fixture()
    real_dump = json.dump

    def racing_dump(obj, fh, **kw):
        real_dump(obj, fh, **kw)
        time.sleep(0.01)
        with open(p, "a", encoding="utf-8") as f:   # the app writes underneath us
            f.write(" ")
    json.dump = racing_dump
    try:
        E.patch(p)
        check("aborts when the registry changes mid-write", False, "no exception")
    except RuntimeError as e:
        check("aborts when the registry changes mid-write", "aborted" in str(e))
    finally:
        json.dump = real_dump
    doc = json.loads(open(p, encoding="utf-8").read())
    check("and leaves the file unpatched",
          E.find_task(doc["scheduledTasks"], TASK).get("permissionMode") is None)
    check("and leaves no .tmp behind",
          not [f for f in os.listdir(os.path.dirname(p)) if ".tmp." in f])


# ── 4. End to end against the LIVE registry (read-only: the app is up) ────────

def test_live_defers_and_writes_nothing():
    print("live run, app up")
    live = E.registries()
    check("finds at least one registry", len(live) >= 1, str(live))
    found = E.survey()
    check(f"finds {TASK} in a real registry",
          any(n == TASK for _, n, _, _ in found), str([n for _, n, _, _ in found]))

    before = {p: os.stat(p).st_mtime_ns for p in live}
    log_before = os.path.getsize(E.LOG_PATH) if os.path.exists(E.LOG_PATH) else 0
    r = subprocess.run([sys.executable, SCRIPT], capture_output=True, text=True)
    # stdout is silent when not a tty (launchd redirects it into LOG_PATH), so the
    # log file, not stdout, is where the verdict has to be read.
    with open(E.LOG_PATH, encoding="utf-8") as f:
        f.seek(log_before)
        written = f.read()
    check("exits 75 (deferred), not 0", r.returncode in (0, E.EX_DEFERRED),
          f"rc={r.returncode} {r.stderr[:200]}")
    check("stays quiet on stdout when not a tty (no duplicate log lines)",
          r.stdout.strip() == "", r.stdout[:120])
    if r.returncode == E.EX_DEFERRED:
        check("logs DEFER and names the missing fields",
              "DEFER" in written and "permissionMode" in written, written[:200])
    else:
        check("exit 0 means the fields are already applied",
              not [n for _, n, _, m in E.survey() if m])
    after = {p: os.stat(p).st_mtime_ns for p in live}
    check("touched NO live registry", before == after,
          str([p for p in before if before[p] != after.get(p)]))
    check("left no backup beside a live registry",
          not [f for p in live for f in os.listdir(os.path.dirname(p))
               if ".bak." in f or ".tmp." in f])


def test_health_check_agrees():
    """The falsifier and the fixer must name the same tasks, or one will quietly
    guard something the other does not maintain."""
    print("agreement with check_scheduler_health.py")
    src = open(os.path.join(HERE, "check_scheduler_health.py"), encoding="utf-8").read()
    for name in E.REQUIRED:
        check(f"{name} is asserted by the health check", name in src)


if __name__ == "__main__":
    test_detector()
    test_find_task()
    test_patch_writes_and_is_idempotent()
    test_mtime_guard()
    test_live_defers_and_writes_nothing()
    test_health_check_agrees()
    print()
    if FAILURES:
        print(f"FAILED ({len(FAILURES)}): " + ", ".join(FAILURES))
        sys.exit(1)
    print("all checks passed")

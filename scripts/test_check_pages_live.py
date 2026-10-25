#!/usr/bin/env python3
"""Tests for check_pages_live.py. Every case drives a real decision path and says
WHY that path matters; each asserts on the files the health checker reads.

Run:  python3 scripts/test_check_pages_live.py
"""
import importlib.util
import json
import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cpl", os.path.join(HERE, "check_pages_live.py"))
cpl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cpl)

NOW = datetime(2026, 10, 25, 20, 0, 0, tzinfo=timezone.utc)
PAGE = b"<html>explorer</html>"
results = []


def ts(hours_ago):
    return (NOW - timedelta(hours=hours_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


def run(n, status, conclusion=None, hours_ago=0.1, name=cpl.DEPLOY_WORKFLOW, recent=True):
    return {"id": n, "name": name, "run_number": n, "status": status, "conclusion": conclusion,
            "created_at": ts(hours_ago), "head_sha": "abcdef1234", "html_url": f"https://x/{n}",
            "_recent": recent}


def fake(runs, probe_hours_ago, live, main, fail_on=None):
    def get(url):
        if fail_on and fail_on in url:
            raise cpl.Unreachable(url + ": boom")
        if "/runs" in url:
            if "status=" in url:  # the API filters by status over ALL history
                st = url.split("status=")[1]
                return json.dumps({"workflow_runs": [r for r in runs if r["status"] == st]}).encode()
            return json.dumps({"workflow_runs": [r for r in runs if r["_recent"]]}).encode()
        if "/commits" in url:
            return json.dumps([{"commit": {"committer": {"date": ts(probe_hours_ago)}}}]).encode()
        if url.startswith(cpl.PAGES_BASE):
            return live
        if url.startswith(cpl.RAW_BASE):
            return main
        raise AssertionError(url)
    return get


def case(name, why, runs, probe_hours_ago, live, main, expect_exit, expect_verdict,
         marker_before=False, argv=(), fail_on=None):
    with tempfile.TemporaryDirectory() as repo:
        marker = os.path.join(repo, "pages_live.FAILED")
        if marker_before:
            with open(marker, "w") as fh:
                fh.write("[2026-10-24 05:40:00] old failure\n")
        code = cpl.main(list(argv), repo=repo, now=NOW,
                        get=fake(runs, probe_hours_ago, live, main, fail_on))
        state = os.path.join(repo, "scheduler", "pages_live.json")
        verdict = json.load(open(state))["verdict"] if os.path.exists(state) else None
        ok = code == expect_exit and verdict == expect_verdict
        if expect_verdict == "FAIL":
            ok = ok and os.path.exists(marker)
        elif expect_verdict in ("OK", "WARN"):
            ok = ok and not os.path.exists(marker)
        else:  # nothing written: state absent, marker exactly as it was
            ok = ok and os.path.exists(marker) == marker_before
        results.append(ok)
        print(("PASS" if ok else "FAIL") + f"  {name}\n      why: {why}"
              + ("" if ok else f"\n      got exit={code} verdict={verdict} marker={os.path.exists(marker)}"))


# 1. The 2026-10-25 incident itself: the probe page matched (explorer.html had not
#    changed since the jam began) while every deploy queued behind a waiting run.
case("stuck deploy run fails even when the probe page matches",
     "the real outage left explorer.html identical for weeks; only the queue showed it",
     [run(152, "pending", hours_ago=0.2), run(107, "waiting", hours_ago=19 * 24)],
     probe_hours_ago=27 * 24, live=PAGE, main=PAGE, expect_exit=3, expect_verdict="FAIL")

# 2. A normal push: deploy running, page not yet swapped. Must not cry wolf.
case("deploy in flight inside the grace window is WARN, not FAIL",
     "a report that is red after every push stops being read",
     [run(153, "in_progress", hours_ago=0.1), run(152, "completed", "success", 1)],
     probe_hours_ago=0.5, live=b"old", main=PAGE, expect_exit=0, expect_verdict="WARN")

# 3. Deploys 'succeed' or vanish, yet the page never changes.
case("live page still different hours after main changed it is FAIL",
     "whatever the cause, the public entry page is not what was reviewed and pushed",
     [run(152, "completed", "success", 6)],
     probe_hours_ago=5, live=b"old", main=PAGE, expect_exit=3, expect_verdict="FAIL")

# 4. A failed deploy is a fault; a cancelled one is ordinary supersession.
case("newest finished deploy that failed is FAIL",
     "a failing workflow publishes nothing, and the next push will fail the same way",
     [run(154, "completed", "failure", 1), run(153, "completed", "success", 30)],
     probe_hours_ago=40, live=PAGE, main=PAGE, expect_exit=3, expect_verdict="FAIL")
case("newest finished deploy that was cancelled is fine",
     "a newer push cancelling an older pending deploy is how the queue is meant to work",
     [run(155, "completed", "success", 0.5), run(154, "completed", "cancelled", 1)],
     probe_hours_ago=40, live=PAGE, main=PAGE, expect_exit=0, expect_verdict="OK")

# 5. Recovery must clear the marker, or the health report stays red forever.
case("healthy check removes an old failure marker",
     "a marker that outlives the fault turns the watchdog into noise",
     [run(156, "completed", "success", 3)],
     probe_hours_ago=40, live=PAGE, main=PAGE, expect_exit=0, expect_verdict="OK",
     marker_before=True)

# 6. Not being able to look is not a verdict about the site.
case("unreachable GitHub exits 2 and changes nothing",
     "a network blip must neither raise nor clear the alarm",
     [], probe_hours_ago=1, live=PAGE, main=PAGE, expect_exit=2, expect_verdict=None,
     marker_before=True, fail_on="tloughran.github.io")

# 7. Workflows other than Pages are ignored (heartbeat runs constantly).
case("a long-running non-Pages workflow is not a stuck deploy",
     "only the Pages queue decides what the public sees",
     [run(9, "in_progress", hours_ago=5, name="heartbeat-refresh"), run(156, "completed", "success", 3)],
     probe_hours_ago=40, live=PAGE, main=PAGE, expect_exit=0, expect_verdict="OK")

# 9. The real jam: the run holding the queue had scrolled out of the recent list,
#    and the newest pending deploy behind it was younger than STUCK_HOURS.
case("stuck run outside the recent-runs window is still found",
     "the 10-06 run was ~50 runs back; a recent-only query reads green on a jammed queue",
     [run(160, "pending", hours_ago=1.2), run(159, "completed", "cancelled", 3),
      run(107, "waiting", hours_ago=19 * 24, recent=False)],
     probe_hours_ago=27 * 24, live=PAGE, main=PAGE, expect_exit=3, expect_verdict="FAIL")

# 8. --dry-run is for a human looking; it must write nothing.
case("dry run reports but writes no state and no marker",
     "a manual look must not move the health checker's inputs",
     [run(107, "waiting", hours_ago=100)], probe_hours_ago=40, live=PAGE, main=PAGE,
     expect_exit=3, expect_verdict=None, argv=["--dry-run"])

print(f"\n{sum(results)}/{len(results)} passed")
sys.exit(0 if all(results) else 1)

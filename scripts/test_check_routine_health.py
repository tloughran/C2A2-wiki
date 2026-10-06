#!/usr/bin/env python3
"""test_check_routine_health.py -- drive every verdict of check_routine_health.py.

Each case is a shape that actually happened, or the one the tolerance exists
for. A watchdog nobody has watched go red is not a watchdog, so most cases
assert FAIL or WARN, and the OK cases exist to prove the tolerances do not
cry wolf on a laptop-asleep morning or an hourly routine anchored at :37.

  python3 scripts/test_check_routine_health.py
"""
import json
import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_routine_health as mod  # noqa: E402

FAILURES = []
# Monday 2026-10-05 15:00 Indianapolis (EDT, UTC-4) = 19:00Z.
NOW = datetime(2026, 10, 5, 19, 0, tzinfo=timezone.utc)
TZ = "CRON_TZ=America/Indianapolis "


def expect(name, got, want):
    if got != want:
        FAILURES.append(name)
        print(f"  FAIL {name}\n         expected {want!r}\n         got      {got!r}")
    else:
        print(f"  ok   {name}")


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def routine(cron, fired=None, status="SUCCEEDED", created="2026-09-01T00:00:00Z", **kw):
    t = {"name": "r", "enabled": True, "cron_expression": cron, "created_at": created}
    if fired:
        t["last_run"] = {"status": "ROUTINE_RUN_STATUS_" + status, "fired_at": iso(fired)}
    t.update(kw)
    return t


def level(t):
    return mod.verdict_routine(t, NOW)[0]


print("must FAIL:")
# A run that errored is red regardless of the clock.
expect("last run FAILED", level(routine(TZ + "30 4 * * *", NOW - timedelta(hours=10), "FAILED")), mod.FAIL)
# Daily 04:30 local; last fired three days ago -> two scheduled fires missed.
expect("daily routine missed two fires",
       level(routine(TZ + "30 4 * * *", NOW - timedelta(days=3))), mod.FAIL)
# Enabled for weeks, schedule says it should have run, it never has.
expect("enabled long ago, never fired", level(routine(TZ + "30 4 * * *")), mod.FAIL)
# Strictness: an unreadable zone must not turn into "matches everything".
expect("unknown time zone", level(routine("CRON_TZ=Mars/Olympus 30 4 * * *", NOW)), mod.FAIL)
expect("unparseable cron", level(routine(TZ + "61 4 * * *", NOW)), mod.FAIL)

print("must WARN:")
# 2026-10-05, verbatim: the dashboard built in 3 minutes, then waited ~6h on a
# publish approval. Its status said PENDING the whole time.
expect("run PENDING for six hours (approval wait)",
       level(routine("0 11 * * 1-5", NOW - timedelta(hours=6), "PENDING")), mod.WARN)

print("must stay OK (tolerances):")
expect("daily routine fired this morning",
       level(routine(TZ + "30 4 * * *", NOW - timedelta(hours=10, minutes=30))), mod.OK)
# One missed morning (laptop asleep, a transient) is allowed; two is a pattern.
expect("one missed fire is tolerated",
       level(routine(TZ + "30 4 * * *", NOW - timedelta(days=1, hours=10))), mod.OK)
# Hourly routines are anchored server-side to their creation minute: computed at
# :00, really at :37. Must not read as missed.
expect("hourly routine anchored at :37",
       level(routine("0 * * * *", NOW.replace(minute=0) - timedelta(minutes=23))), mod.OK)
expect("PENDING for one hour is just running",
       level(routine("0 11 * * 1-5", NOW - timedelta(hours=1), "PENDING")), mod.OK)
expect("created yesterday, not yet asked twice",
       level(routine(TZ + "0 3 * * 1", created=iso(NOW - timedelta(days=1)))), mod.OK)
expect("disabled routine", level(routine(TZ + "30 4 * * *", enabled=False)), mod.OK)
expect("one-shot routine", level({"name": "x", "enabled": True, "run_once_at": iso(NOW)}), mod.OK)
# Every routine on this account says America/Indianapolis, a legacy alias some tz
# databases omit. Without the fallback all 38 read FAIL (seen 2026-10-05).
expect("legacy zone America/Indianapolis resolves",
       str(mod.split_cron(TZ + "30 4 * * *")[0]).endswith("Indianapolis"), True)

print("snapshot loading:")
with tempfile.TemporaryDirectory() as tmp:
    one = {"data": [routine("0 11 * * 1-5", NOW)]}
    p = os.path.join(tmp, "one.json"); json.dump(one, open(p, "w"))
    expect("raw list_triggers result", len(mod.load_snapshot(p)), 1)
    p = os.path.join(tmp, "pages.json"); json.dump([one, one], open(p, "w"))
    expect("several saved pages are flattened", len(mod.load_snapshot(p)), 2)
    p = os.path.join(tmp, "empty.json"); json.dump({"data": []}, open(p, "w"))
    expect("empty snapshot exits 2, not a quiet pass", mod.main(["--snapshot", p]), 2)

print(f"\n{'ALL PASSED' if not FAILURES else str(len(FAILURES)) + ' FAILED'}")
sys.exit(1 if FAILURES else 0)

#!/usr/bin/env python3
"""Drive every branch of the metabolism monitor's ingest gate, and its exit code.

The gate that already existed (assert_fresh) is one-directional by construction:
it compares the live db's mtime against the snapshot's build time, and the
monitor rebuilds at the top of every run, so that difference can only exceed the
limit when the db is NEWER than the build. A dead source drives it negative. The
logbook has the failure verbatim, from the 2026-07-04/05 writer outage:

    snapshot lag behind db -37.94 h. Gate = 24h; PASS.

So the cases that matter here are the ones that must NOT come back OK:

  - no events at all for longer than the fail limit (an ingest outage)
  - events arriving while no session has STARTED (the mode that hid 2026-08:
    long-open sessions keep the event clock warm while capture is dead)
  - the old, negative-lag artifact reading, which must not rescue either
  - a snapshot with no t_max_event (pre-2026-08-24) -- must judge on starts and
    SAY it is doing that, never let a missing field read as a passing check
  - a snapshot with no timestamps at all -- unknown must not read as OK
  - the boundary either side of the fail limit, so the threshold is real
  - main() exiting 3 only AFTER the reports are on disk

    python3 scripts/test_metabolism_monitor.py
"""

import json
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import metabolism_monitor as mod  # noqa: E402

FAILURES = []


def expect(name, got, want):
    if got != want:
        FAILURES.append(f"{name}: expected {want!r}, got {got!r}")
        print(f"  FAIL {name}\n         expected {want!r}\n         got      {got!r}")
    else:
        print(f"  ok   {name}")


NOW = datetime(2026, 8, 24, 18, 0, tzinfo=timezone.utc)


def iso(hours_ago, base=NOW):
    return (base - timedelta(hours=hours_ago)).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def snap(event_h=None, start_h=None, omit_event=False, omit_both=False, base=NOW):
    """A minimal snapshot whose only interesting content is its two timestamps.

    Assertions that pass now=NOW into assess_ingest() keep the frozen base, so
    they read the same on any calendar day. Fixtures fed to main() -- which
    reads the real wall clock -- must pass base=datetime.now(timezone.utc), or
    they age into the wrong verdict the day after they are written.
    """
    meta = {"generated": iso(0, base), "db_mtime": iso(0, base), "lanes": 3,
            "total_runs": 10, "t_min": iso(3000, base)}
    if not omit_both:
        meta["t_max"] = iso(start_h, base)
        if not omit_event:
            meta["t_max_event"] = iso(event_h, base)
    return {"_meta": meta, "lanes": [], "yield_daily": []}


def level(**kw):
    return mod.assess_ingest(snap(**kw), now=NOW)["level"]


def main():
    print("assess_ingest -- the verdict")
    # Healthy: the live reading on the day this was written.
    expect("both fresh -> OK", level(event_h=0.2, start_h=1.7), "OK")

    # THE OUTAGE. 2026-08-19 07:07 -> 08-23 22:36 was a 111.5h hole.
    expect("no events for 111h -> FAIL", level(event_h=111.5, start_h=111.5), "FAIL")
    v = mod.assess_ingest(snap(event_h=111.5, start_h=111.5), now=NOW)
    expect("outage message says ingest, not artifact",
           "ingest outage, not a stale artifact" in v["message"], True)
    expect("outage message refuses to recommend a regen",
           "regenerating cannot fix it" in v["message"], True)

    # THE HIDING MODE: events keep flowing, session creation is dead. One number
    # cannot tell this from health, which is why both are carried.
    expect("events fresh, starts 111h stale -> FAIL", level(event_h=0.5, start_h=111.5), "FAIL")
    v = mod.assess_ingest(snap(event_h=0.5, start_h=111.5), now=NOW)
    expect("hiding-mode message names session capture",
           "Session capture looks dead" in v["message"], True)
    expect("hiding-mode message reports BOTH ages",
           "0.5h ago" in v["message"] and "111.5h" in v["message"], True)

    print("\nassess_ingest -- the threshold is real")
    expect("47h -> WARN, not FAIL", level(event_h=47.0, start_h=47.0), "WARN")
    expect("49h -> FAIL", level(event_h=49.0, start_h=49.0), "FAIL")
    expect("exactly at fail limit (48h) -> WARN", level(event_h=48.0, start_h=48.0), "WARN")
    expect("23h -> OK", level(event_h=23.0, start_h=23.0), "OK")
    expect("25h -> WARN", level(event_h=25.0, start_h=25.0), "WARN")
    # p99.9 of real inter-session gaps is 39.9h: a normal-but-quiet stretch must
    # warn and must not fail, or the gate gets ignored.
    expect("p99.9 gap (39.9h) -> WARN not FAIL", level(event_h=39.9, start_h=39.9), "WARN")

    print("\nassess_ingest -- missing data must never read as OK")
    expect("no t_max_event, starts stale -> FAIL",
           level(start_h=111.5, omit_event=True), "FAIL")
    v = mod.assess_ingest(snap(start_h=111.5, omit_event=True), now=NOW)
    expect("missing-field message admits what it could not check",
           "predates event-time tracking" in v["message"], True)
    expect("no t_max_event, starts fresh -> OK", level(start_h=1.0, omit_event=True), "OK")
    expect("no timestamps at all -> FAIL", level(omit_both=True), "FAIL")
    v = mod.assess_ingest(snap(omit_both=True), now=NOW)
    expect("unknown is stated as unknown", "Unknown is not OK" in v["message"], True)

    print("\nthe old artifact gate must not rescue any of it")
    # -37.94h is the real logbook reading from the 07-04/05 outage.
    stale = snap(event_h=111.5, start_h=111.5)
    with tempfile.NamedTemporaryFile("w", suffix=".db", delete=False) as fh:
        db = fh.name
    fresh = mod.assert_fresh({"_meta": {"generated": datetime.now(timezone.utc).isoformat()}}, db)
    expect("assert_fresh still passes a just-built snapshot", fresh["gate"], "artifact-only")
    expect("artifact gate labelled so it is not read as health",
           fresh["gate"] == "artifact-only" and mod.assess_ingest(stale, now=NOW)["level"], "FAIL")

    print("\nmain() -- exit code, and reports written BEFORE it")
    tmp = Path(tempfile.mkdtemp())
    mod.DATA_JSON = tmp / "metabolism_data.json"
    mod.MONITOR_DIR = tmp / "monitor"
    mod.STATE_PATH = mod.MONITOR_DIR / "state.json"
    mod.FINDINGS_MD = mod.MONITOR_DIR / "findings.md"
    mod.LOGBOOK_MD = mod.MONITOR_DIR / "logbook.md"
    real_now = datetime.now(timezone.utc)
    out = snap(event_h=111.5, start_h=111.5, base=real_now)
    out["_meta"]["generated"] = real_now.isoformat()
    out["lanes"] = [{"key": "k", "label": "k", "category": "agent", "runs": 1,
                     "rows": [{"t": iso(111.5, real_now), "in": 1, "out": 1, "cache_read": 0,
                               "cache_creation": 0, "thinking_tokens": 0}]}]
    mod.DATA_JSON.write_text(json.dumps(out))

    argv = sys.argv[:]
    sys.argv = ["metabolism_monitor.py", "--no-regen", "--db", db]
    try:
        code = 0
        try:
            mod.main()
        except SystemExit as exc:
            code = exc.code
    finally:
        sys.argv = argv
    expect("stale ingest exits 3", code, mod.EXIT_INGEST_STALE)
    expect("findings.md written despite the failure", mod.FINDINGS_MD.exists(), True)
    expect("logbook.md written despite the failure", mod.LOGBOOK_MD.exists(), True)
    expect("state.json written despite the failure", mod.STATE_PATH.exists(), True)
    body = mod.FINDINGS_MD.read_text()
    expect("findings leads with the ingest verdict",
           body.index("## Ingest liveness: FAIL") < body.index("## New since last week"), True)
    expect("findings says exit 3 is the monitor working",
           "not the monitor broken" in body, True)
    expect("state.json carries the verdict",
           json.loads(mod.STATE_PATH.read_text())["ingest"]["level"], "FAIL")

    # And the healthy path must exit 0, or every green day looks broken.
    ok = snap(event_h=0.2, start_h=1.7, base=datetime.now(timezone.utc))
    ok["_meta"]["generated"] = datetime.now(timezone.utc).isoformat()
    ok["lanes"] = out["lanes"]
    mod.DATA_JSON.write_text(json.dumps(ok))
    sys.argv = ["metabolism_monitor.py", "--no-regen", "--db", db]
    try:
        code = 0
        try:
            mod.main()
        except SystemExit as exc:
            code = exc.code
    finally:
        sys.argv = argv
    expect("healthy ingest exits 0", code, 0)

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

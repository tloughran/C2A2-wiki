#!/usr/bin/env python3
"""check_routine_health.py -- did every CLOUD routine fire, and did its run end?

Why this exists
---------------
Between 2026-09-16 and 09-28 about 32 scheduled tasks moved from the Mac's task
registry to cloud Routines. check_scheduler_health.py reads the Mac registry, so
from then on it could only say, 32 times a morning, "moved to a cloud scheduled
task; the Mac registry can no longer tell whether it fires". The run-stall check
failed daily for the same reason, and the morning status report counted 20
routines as "all succeeded" while one sat blocked on an approval prompt for six
hours. Nothing on the Mac can see a cloud run.

The cloud CAN see them: the Routines service records each routine's schedule and
its last run (status, fired_at, finished_at). This script judges that record.
It does not fetch it -- a launchd job on the Mac has no credentials for the
Routines service. The 07:00 `scheduler-health-check` routine fetches it (it holds
the connector), saves the raw listing to a file, runs this script on the file,
and only REPORTS the result. Same split as check_scheduler_health.py: the model
fetches and reports, code judges (CLAUDE.md Rule 5).

Verdicts, per enabled routine:
  FAIL  last run FAILED, or never fired though its schedule says it should have,
        or missed MISSED_FIRES_ALLOWED (2) scheduled fires in a row
  WARN  a run has been PENDING/RUNNING for over PENDING_WARN_HOURS -- the
        2026-10-01/10-05 dashboard shape: done in 3 minutes, then waiting hours
        on an approval nobody was there to give
  OK    otherwise

The cron tolerance is the Mac checker's, on purpose: one missed fire is a
transient; two is a pattern. Hourly routines are anchored server-side to their
creation minute, so a fire computed at :00 may really land at :37. Comparing
against the OLDER of the last two computed fires absorbs that.

Usage:
  python3 scripts/check_routine_health.py --snapshot scheduler/routines_snapshot.json
  python3 scripts/check_routine_health.py --snapshot ... --status-file scheduler/routine_health.md
Exit: 0 no FAIL, 1 at least one FAIL, 2 the snapshot is unreadable.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_scheduler_health as mac  # noqa: E402  (shared cron evaluator + verdict levels)

OK, WARN, FAIL = mac.OK, mac.WARN, mac.FAIL
PENDING_WARN_HOURS = 2
LEGACY_ZONES = {"America/Indianapolis": "America/Indiana/Indianapolis"}


def split_cron(expression):
    """'CRON_TZ=America/Indianapolis 46 6 * * 1' -> (ZoneInfo, '46 6 * * 1').

    Routines without the prefix are UTC, per the Routines service.
    """
    expression = expression.strip()
    zone = timezone.utc
    if expression.startswith("CRON_TZ="):
        head, _, expression = expression.partition(" ")
        name = head.split("=", 1)[1]
        try:
            zone = ZoneInfo(name)
        except Exception:
            # Every routine here says America/Indianapolis: a legacy alias the
            # Routines service and macOS accept, but which tz databases built
            # without the "backward" links (some Linux images) do not carry.
            # Unknown names still raise -- a zone we cannot read must not pass.
            zone = ZoneInfo(LEGACY_ZONES[name])
    return zone, expression.strip()


def parse_iso(stamp):
    return datetime.fromisoformat(stamp.replace("Z", "+00:00")) if stamp else None


def verdict_routine(trigger, now_utc):
    name = trigger.get("name") or trigger.get("id", "<unnamed>")
    if not trigger.get("enabled"):
        return OK, f"{name}: disabled{' (' + trigger['ended_reason'] + ')' if trigger.get('ended_reason') else ''}"

    last_run = trigger.get("last_run") or {}
    status = (last_run.get("status") or "").replace("ROUTINE_RUN_STATUS_", "")
    fired = parse_iso(last_run.get("fired_at") or trigger.get("last_fired_at"))

    # A run that ended badly is the loudest thing we can say, whatever the clock.
    if status == "FAILED":
        reason = (last_run.get("failure_reason") or "").replace("ROUTINE_RUN_FAILURE_REASON_", "")
        return FAIL, f"{name}: last run FAILED ({reason or 'no reason given'}) at {fired:%Y-%m-%d %H:%MZ}" if fired \
            else f"{name}: last run FAILED"

    if status in ("PENDING", "RUNNING") and fired:
        hours = (now_utc - fired).total_seconds() / 3600
        if hours > PENDING_WARN_HOURS:
            return WARN, (f"{name}: run fired {fired:%Y-%m-%d %H:%MZ} still {status} after {hours:.1f}h "
                          f"-- usually a prompt waiting for an approval nobody is there to give")

    cron = trigger.get("cron_expression")
    if not cron:
        # One-shot (run_once_at) and poke-only routines have no schedule to miss.
        return OK, f"{name}: no recurring schedule"

    try:
        zone, expr = split_cron(cron)
        now_local = now_utc.astimezone(zone)
        fires = mac.previous_fires(expr, now_local, mac.MISSED_FIRES_ALLOWED)
    except (ValueError, KeyError) as exc:
        return FAIL, f"{name}: cannot evaluate schedule {cron!r} -- {exc}"

    if not fires:
        return WARN, f"{name}: {cron!r} has no fire in the last 45 days"

    created = parse_iso(trigger.get("created_at"))
    oldest_allowed = fires[-1].replace(tzinfo=zone)
    if fired is None:
        # Not asked twice yet since it was created: not a miss, just new.
        if created and created > oldest_allowed:
            return OK, f"{name}: created {created:%Y-%m-%d}; not yet due twice"
        return FAIL, f"{name}: enabled on {cron!r} and has never fired"

    if fired >= oldest_allowed or (created and created > oldest_allowed):
        tail = f", last run {status}" if status else ""
        return OK, f"{name}: fired {fired:%Y-%m-%d %H:%MZ}, on schedule{tail}"

    missed = sum(1 for f in fires if fired < f.replace(tzinfo=zone))
    hours = (now_utc - fired).total_seconds() / 3600
    return FAIL, (f"{name}: last fired {fired:%Y-%m-%d %H:%MZ} ({hours:.0f}h ago), "
                  f"missed {missed} scheduled fire(s) of {cron!r}")


def load_snapshot(path):
    """Accept the raw list_triggers result ({"data": [...]}) or a bare list.

    Several pages saved together as a list of results are flattened too, so the
    routine can save every page without merging them by hand.
    """
    raw = json.load(open(path))
    pages = raw if isinstance(raw, list) and raw and isinstance(raw[0], dict) and "data" in raw[0] else [raw]
    triggers = []
    for page in pages:
        triggers.extend(page["data"] if isinstance(page, dict) else page)
    return triggers


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--snapshot", required=True, help="saved list_triggers JSON")
    ap.add_argument("--status-file", help="append a stamped block (summary + non-OK lines)")
    ap.add_argument("--quiet", action="store_true", help="print only WARN and FAIL lines")
    args = ap.parse_args(argv)

    try:
        triggers = load_snapshot(args.snapshot)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAIL  cannot read routine snapshot {args.snapshot}: {exc}", file=sys.stderr)
        return 2
    if not triggers:
        print(f"FAIL  routine snapshot {args.snapshot} lists no routines", file=sys.stderr)
        return 2

    now_utc = datetime.now(timezone.utc)
    results = [verdict_routine(t, now_utc) for t in triggers]
    counts = {lvl: sum(1 for l, _ in results if l == lvl) for lvl in (OK, WARN, FAIL)}
    for level, line in results:
        if not (args.quiet and level == OK):
            print(f"{level:<5} {line}")
    summary = (f"cloud routines: {len(results)} checked -- "
               f"{counts[OK]} OK / {counts[WARN]} WARN / {counts[FAIL]} FAIL")
    print(summary)

    if args.status_file:
        os.makedirs(os.path.dirname(os.path.abspath(args.status_file)), exist_ok=True)
        stamp = now_utc.strftime("%Y-%m-%dT%H:%MZ")
        with open(args.status_file, "a") as fh:
            fh.write(f"{stamp}  {summary}\n")
            for level, line in results:
                if level != OK:
                    fh.write(f"{stamp}  {level:<5} {line}\n")
    return 1 if counts[FAIL] else 0


if __name__ == "__main__":
    sys.exit(main())

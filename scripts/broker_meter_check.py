#!/usr/bin/env python3
"""Report the Pathway-00 broker's daily meters against their caps.

Why this exists
---------------
On 2026-07-29 the voice guide was dead all morning and nobody knew why. The
cause was a spent meter: realtime_session shared the `enrich` budget, 20 voice
starts cost 500c, and the broker returned 402 to every visitor for the rest of
the UTC day. It had already happened on 07-22 (511c, over cap) and nearly on
07-25 (482c) without anyone noticing, because nothing ever read the meter.

Deciding "is a counter near its cap" is arithmetic, not judgment (CLAUDE.md
Rule 5), so this is a script and not a prompt. Point the morning brief at it.

The caps are PARSED OUT OF the deployed broker source rather than restated
here, so this file cannot drift away from the thing it is checking. If the
source is missing the script says so and exits non-zero rather than quietly
comparing against a guess (Rule 12).

Usage
-----
    python3 scripts/broker_meter_check.py            # last 7 days, human report
    python3 scripts/broker_meter_check.py --days 30
    python3 scripts/broker_meter_check.py --json     # machine-readable

Exit codes: 0 clean · 1 today at/over WARN_FRACTION of a cap · 2 cannot check.
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

PROJECT_REF = "akhcocmgfwybdovqeovd"
API = f"https://api.supabase.com/v1/projects/{PROJECT_REF}/database/query"

# Same credential the authenticated `supabase` CLI uses. Never printed.
KEYCHAIN_SERVICE = "Supabase CLI"

BROKER_SRC = (
    Path(__file__).resolve().parent.parent
    / ".private/supabase/functions/cc-broker/index.ts"
)

WARN_FRACTION = 0.80

# (label, meter column, broker constant holding its cap)
METERS = [
    ("dataset enrich", "cost_cents", "GLOBAL_DAILY_CENTS_CAP"),
    ("web enrich", "web_cost_cents", "WEB_GLOBAL_DAILY_CENTS_CAP"),
    ("realtime voice", "rt_cost_cents", "RT_GLOBAL_DAILY_CENTS_CAP"),
]


def die(msg):
    print(f"broker-meter: CANNOT CHECK — {msg}", file=sys.stderr)
    sys.exit(2)


def read_caps():
    """Parse the cap constants out of the broker source.

    Restating them here would let this check pass while the real caps had
    moved, which is the failure mode it exists to prevent.
    """
    if not BROKER_SRC.exists():
        die(f"broker source not found at {BROKER_SRC}")
    src = BROKER_SRC.read_text()
    caps = {}
    for _, _, const in METERS:
        m = re.search(rf"^const\s+{const}\s*=\s*(\d+)\s*;", src, re.M)
        if not m:
            die(f"{const} not found in {BROKER_SRC.name} — did the broker change?")
        caps[const] = int(m.group(1))
    return caps


def token():
    try:
        out = subprocess.run(
            ["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
            capture_output=True, text=True, check=True,
        )
    except subprocess.CalledProcessError:
        die(f"no keychain item for service {KEYCHAIN_SERVICE!r}; run `supabase login`")
    t = out.stdout.strip()
    if not t:
        die("keychain returned an empty Supabase token")
    return t


def query(sql):
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": sql}).encode(),
        headers={
            "Authorization": f"Bearer {token()}",
            "Content-Type": "application/json",
            # Cloudflare fronts the management API and 403s (code 1010) on the
            # default Python-urllib agent. Identify ourselves properly.
            "User-Agent": "c2a2-broker-meter-check/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        die(f"management API returned {e.code}: {e.read()[:200].decode(errors='replace')}")
    except urllib.error.URLError as e:
        die(f"management API unreachable: {e.reason}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    caps = read_caps()
    rows = query(
        "select meter_date::text, asks, cost_cents, web_asks, web_cost_cents, "
        "rt_asks, rt_cost_cents from public.global_meter "
        f"where meter_date >= current_date - {int(args.days)} "
        "order by meter_date desc;"
    )
    if not isinstance(rows, list):
        die(f"unexpected API payload: {str(rows)[:200]}")

    today = rows[0]["meter_date"] if rows else None
    findings = []
    for row in rows:
        for label, col, const in METERS:
            cap, spent = caps[const], row.get(col) or 0
            if spent >= cap * WARN_FRACTION:
                findings.append({
                    "date": row["meter_date"],
                    "meter": label,
                    "spent_cents": spent,
                    "cap_cents": cap,
                    "pct": round(100 * spent / cap),
                    "capped_out": spent >= cap,
                    "is_today": row["meter_date"] == today,
                })

    if args.json:
        print(json.dumps({"caps": caps, "days": rows, "findings": findings}, indent=2))
    else:
        print(f"Broker daily meters — last {args.days} days (UTC days; cents)")
        print(f"{'date':<12}{'enrich':>14}{'web':>14}{'voice':>14}")
        for row in rows:
            def cell(col, const):
                spent, cap = row.get(col) or 0, caps[const]
                mark = "!" if spent >= cap else ("~" if spent >= cap * WARN_FRACTION else " ")
                return f"{spent}/{cap}{mark}"
            print(
                f"{row['meter_date']:<12}"
                f"{cell('cost_cents', 'GLOBAL_DAILY_CENTS_CAP'):>14}"
                f"{cell('web_cost_cents', 'WEB_GLOBAL_DAILY_CENTS_CAP'):>14}"
                f"{cell('rt_cost_cents', 'RT_GLOBAL_DAILY_CENTS_CAP'):>14}"
            )
        if findings:
            print("\nAt or near cap:")
            for f in findings:
                when = "TODAY" if f["is_today"] else f["date"]
                state = "CAPPED OUT" if f["capped_out"] else "near cap"
                print(f"  {when}: {f['meter']} {state} — {f['spent_cents']}/{f['cap_cents']}c ({f['pct']}%)")
            print(
                "\n  A capped meter means the broker returns 402 to every visitor for that\n"
                "  action until 00:00 UTC. Reset with:\n"
                "    update public.global_meter set <column> = 0 where meter_date = current_date;"
            )
        else:
            print("\nAll meters clear.")

    # Only today's state is actionable — a spent meter three days ago has
    # already reset and needs no alert.
    sys.exit(1 if any(f["is_today"] for f in findings) else 0)


if __name__ == "__main__":
    main()

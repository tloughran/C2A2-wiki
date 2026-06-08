#!/usr/bin/env python3
"""
sync_roster.py
--------------
Add the agents present in agent_map.json but missing from the agents_tab.html
AGENTS array, so the schedule animation covers the full 34-agent roster.

Surgical + idempotent: existing AGENTS entries are left untouched; only missing
taskIds are appended. Re-running is a no-op. Schedule fields (days/hour/minute)
are derived from each agent's cron. Agents that fire multiple times per day
(*/N or hour-lists) can't be fully represented by the single-hour animation
model -- they get a representative time and the cadence noted in the description.

Usage: python3 sync_roster.py [--map PATH] [--html PATH]
"""
import argparse
import json
import os
import re
import sys

HOME = os.path.expanduser("~")
VAULT = os.path.join(HOME, "Documents/Claude/Projects/RC Karpathy Wiki Project/wiki")
DEFAULT_MAP = os.path.join(VAULT, "agents/openstory/agent_map.json")
DEFAULT_HTML = os.path.join(VAULT, "agents_tab.html")

# canonical taskId -> spelling already used in the HTML roster (baked-in typo)
TYPO_DUP = {"c282-wiki-agent-daily-run": "c2a2-wiki-agent-daily-run"}

# concise, factual descriptions inferred from taskId/category (no fabricated detail)
DESCRIPTIONS = {
    "c2a2-wiki-janitor-weekly": "Weekly wiki janitor — housekeeping pass over the C2A2 vault (dead links, stale proposals, formatting).",
    "c2a2-sewing-agent-weekly": "Weekly 'sewing' agent — C2A2 pipeline stitching related wiki threads and proposals.",
    "c2a2-prs-connectome-weekly": "Weekly PRS connectome builder — C2A2 pipeline assembling the personal-realist-synthesis connectome.",
    "summa-qc-sweep": "Summa QC sweep — quality-control pass over the Summa 2026 workspace. Runs every 4 hours; highest-volume agent.",
    "summa-commentary-reviewer": "Summa commentary reviewer — reviews commentary entries in the Summa 2026 workspace. Runs every 4 hours.",
    "reviewer-review-weekly": "Weekly reviewer-review — meta-review of reviewer agent output.",
    "scheduler-health-check": "Daily scheduler health check — verifies scheduled tasks are firing as configured.",
    "supabase-c2a2-keep-warm": "Daily Supabase keep-warm — pings the C2A2 Supabase instance to prevent cold pause.",
    "connector-health-weekly": "Weekly connector health check — verifies MCP connectors are authenticated and reachable.",
    "weekly-claude-projects-backup": "Weekly backup of the ~/Documents/Claude projects tree.",
}


def parse_cron(cron):
    """Return (days[list 0=Sun..6=Sat], hour, minute, multi_per_day)."""
    p = cron.split()
    m, h, _dom, _mon, dow = (p + ["*"] * 5)[:5]
    minute = int(re.split(r"[,/]", m)[0]) if m != "*" else 0
    multi = False
    if h == "*" or h.startswith("*/"):
        hour, multi = 0, True
    elif "," in h:
        hour, multi = int(h.split(",")[0]), True
    else:
        hour = int(h)
    if dow == "*":
        days = list(range(7))
    else:
        days = []
        for tok in dow.split(","):
            if "-" in tok:
                a, b = tok.split("-")
                days += list(range(int(a), int(b) + 1))
            else:
                d = int(tok)
                days.append(0 if d == 7 else d)
        days = sorted(set(days))
    return days, hour, minute, multi


def pretty(task_id):
    return " ".join(w.upper() if w in ("c2a2", "prs", "qc") else w.capitalize()
                    for w in task_id.split("-"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", default=DEFAULT_MAP)
    ap.add_argument("--html", default=DEFAULT_HTML)
    args = ap.parse_args()

    agent_map = json.load(open(args.map))
    html = open(args.html).read()

    existing = set(re.findall(r"taskId:'([^']+)'", html))
    existing |= set(re.findall(r'taskId:"([^"]+)"', html))

    new_entries, new_friendly = [], []
    for a in agent_map["agents"]:
        tid = a["taskId"]
        if tid in existing or TYPO_DUP.get(tid) in existing:
            continue
        cron = a.get("cron", "")
        if not cron:
            print("  SKIP (no cron): %s" % tid)
            continue
        days, hour, minute, multi = parse_cron(cron)
        desc = DESCRIPTIONS.get(tid, "%s agent (%s)." % (a.get("category", ""), a.get("schedule", "")))
        cat = a.get("category", "project")
        thinkers = a.get("thinkers", [])
        entry = (
            "  {\n"
            "    taskId:%s,\n"
            "    description:%s,\n"
            "    schedule:%s,\n"
            "    category:%s, days:%s, hour:%d, minute:%d,\n"
            % (json.dumps(tid, ensure_ascii=False), json.dumps(desc, ensure_ascii=False),
               json.dumps(a.get("schedule", ""), ensure_ascii=False),
               json.dumps(cat), json.dumps(days), hour, minute)
        )
        if thinkers:
            entry += "    thinkers:%s,\n" % json.dumps(thinkers, ensure_ascii=False)
        entry += "    narration:%s,\n" % json.dumps(desc, ensure_ascii=False)
        entry += "    multiDaily:%s\n  }," % ("true" if multi else "false")
        new_entries.append(entry)
        new_friendly.append("  %s: %s," % (json.dumps(tid), json.dumps(pretty(tid))))

    if not new_entries:
        print("No missing agents — roster already complete.")
        return

    # insert via function-replacement so backslashes in the payload aren't
    # interpreted as regex group references
    agents_block = "\n".join(new_entries) + "\n"
    friendly_block = "\n".join(new_friendly) + "\n"
    html, n1 = re.subn(r"const AGENTS = \[\n",
                       lambda m: m.group(0) + agents_block, html, count=1)
    html, n2 = re.subn(r"const FRIENDLY_NAMES = \{\n",
                       lambda m: m.group(0) + friendly_block, html, count=1)
    if n1 != 1 or n2 != 1:
        sys.exit("ERROR: insertion anchor not found (AGENTS=%d, FRIENDLY=%d)" % (n1, n2))

    total = len(re.findall(r"taskId:['\"]", html))
    html = re.sub(r'(<div class="subtitle">Weekly Schedule · )\d+( Agents</div>)',
                  r"\g<1>%d\g<2>" % total, html)

    open(args.html, "w").write(html)
    print("Added %d agents (roster now %d):" % (len(new_entries), total))
    for e in new_entries:
        print("   +", re.search(r'taskId:"([^"]+)"', e).group(1))


if __name__ == "__main__":
    main()

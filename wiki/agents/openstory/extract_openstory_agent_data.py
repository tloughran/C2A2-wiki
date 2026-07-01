#!/usr/bin/env python3
"""
extract_openstory_agent_data.py
--------------------------------
Read the OpenStory SQLite store (read-only) and emit a per-agent telemetry
snapshot (agent_telemetry.json) into the C2A2 wiki vault. This is the data
foundation for the Agent Explorer subtabs (schedule viz, sociogram,
interrogative explorer) -- it decouples the tabs from whether serve is up.

Why a join layer: OpenStory truncates sessions.label to 50 chars, so the longer
thinker-pair taskIds lose their tails (e.g. "...mcgilchrist-kastr"). We resolve
each truncated label to its canonical taskId by unique prefix-match against
agent_map.json (the source of truth). See resolve_taskid().

Safe by construction: opens the DB read-only (mode=ro, no immutable -- immutable
breaks while serve is concurrently writing). Never writes to the DB.

Usage:
  python3 extract_openstory_agent_data.py [--db PATH] [--map PATH] [--out PATH]
Defaults target the real-machine layout.
"""

import argparse
import json
import os
import re
import sqlite3
import sys
import urllib.parse
from collections import defaultdict
from datetime import datetime

from openstory_db import (
    connect_ro,
    run_with_retry,
    is_excluded,
    EXCLUDED_PROJECT_SUBSTRINGS,
)

HOME = os.path.expanduser("~")
DEFAULT_DB = os.path.join(HOME, "Documents/Non-Claude Projects/OpenStory/data/open-story.db")
DEFAULT_VAULT = os.path.join(HOME, "Documents/Claude/Projects/RC Karpathy Wiki Project/wiki")
DEFAULT_MAP = os.path.join(DEFAULT_VAULT, "agents/openstory/agent_map.json")
DEFAULT_OUT = os.path.join(DEFAULT_VAULT, "agents/openstory/agent_telemetry.json")

TOOL_USE = "message.assistant.tool_use"


# DB access is via openstory_db.connect_ro_snapshot: the live WAL-mode db must be
# snapshotted before reading or quick_check trips on a mid-write inconsistency.


def label_fragment(label):
    """Extract the (possibly truncated) task name from a session label.
    Handles both name="slug" and the 50-char-truncated name="slug<EOL>."""
    if not label:
        return None
    m = re.search(r'name="([^"]*)', label)
    if not m:
        return None
    frag = m.group(1).strip()
    return frag or None


def build_resolver(canonical):
    """Return resolve(frag) -> (taskId | None, reason).
    Match rules, in order: exact; unique prefix (truncation); else unmatched."""
    canon_set = set(canonical)

    def resolve(frag):
        if frag is None:
            return None, "no_label"
        if frag in canon_set:
            return frag, "exact"
        prefixed = [t for t in canonical if t.startswith(frag)]
        if len(prefixed) == 1:
            return prefixed[0], "prefix"
        if len(prefixed) > 1:
            return None, "ambiguous:%s" % ",".join(prefixed)
        return None, "unmatched"

    return resolve


def dow(ts):
    """Day-of-week index 0=Mon..6=Sun from an ISO timestamp, or None."""
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).weekday()
    except ValueError:
        return None


def duration_s(first, last):
    try:
        a = datetime.fromisoformat(first.replace("Z", "+00:00"))
        b = datetime.fromisoformat(last.replace("Z", "+00:00"))
        d = (b - a).total_seconds()
        return d if d >= 0 else None
    except (ValueError, AttributeError):
        return None


def new_stat():
    return {
        "sessions": 0,
        "events": 0,
        "eval": 0,
        "apply": 0,
        "scope_open": 0,
        "scope_close": 0,
        "errors": 0,
        "delegations": 0,
        "tool_use": 0,
        "tool_use_named": 0,
        "thinking": 0,
        "prompts": 0,
        "duration_s_total": 0.0,
        "duration_sessions": 0,
        "first_seen": None,
        "last_seen": None,
        "by_dow": [0, 0, 0, 0, 0, 0, 0],
        "tools": defaultdict(int),
        "models": defaultdict(int),
        "session_ids": [],
    }


PATTERN_FIELD = {
    "eval_apply.eval": "eval",
    "eval_apply.apply": "apply",
    "eval_apply.scope_open": "scope_open",
    "eval_apply.scope_close": "scope_close",
    "error.recovery": "errors",
    "agent.delegation": "delegations",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--map", default=DEFAULT_MAP)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    with open(args.map) as f:
        agent_map = json.load(f)
    map_by_id = {a["taskId"]: a for a in agent_map["agents"]}
    canonical = list(map_by_id.keys())
    resolve = build_resolver(canonical)

    con = connect_ro(args.db)
    cur = con.cursor()

    # 1) sessions -> taskId
    sid_to_task = {}
    unmatched_frags = defaultdict(int)
    ambiguous_frags = defaultdict(int)
    discovered_frags = defaultdict(int)
    sessions = cur.execute(
        "SELECT id, label, event_count, first_event, last_event, project_name FROM sessions"
    ).fetchall()
    stats = defaultdict(new_stat)
    sess_meta = {}
    for sid, label, ecount, first, last, project_name in sessions:
        if is_excluded(label, project_name):
            # Cross-project session (e.g. BOSCO) — isolate, do not attribute.
            key = "(excluded)"
        else:
            frag = label_fragment(label)
            if frag is None:
                key = "(interactive)"
            else:
                task, reason = resolve(frag)
                if task:
                    key = task
                elif reason.startswith("ambiguous"):
                    ambiguous_frags[frag] += 1
                    key = "(unmatched)"
                else:
                    # Clean scheduled-task name with no roster entry: attribute it
                    # to its own name as a DISCOVERED agent rather than lumping it
                    # into "(unmatched)". New scheduled tasks then self-attribute,
                    # so agent_map stays an enrichment layer rather than a gate
                    # that silently drops every task not hand-updated for.
                    discovered_frags[frag] += 1
                    key = frag
        sid_to_task[sid] = key
        sess_meta[sid] = (ecount or 0, first, last)
        s = stats[key]
        s["sessions"] += 1
        s["session_ids"].append(sid)
        d = dow(first)
        if d is not None:
            s["by_dow"][d] += 1
        for ts in (first, last):
            if ts:
                if s["first_seen"] is None or ts < s["first_seen"]:
                    s["first_seen"] = ts
                if s["last_seen"] is None or ts > s["last_seen"]:
                    s["last_seen"] = ts
        dur = duration_s(first, last)
        if dur is not None:
            s["duration_s_total"] += dur
            s["duration_sessions"] += 1

    # 2) patterns by session,type
    for sid, ptype, n in cur.execute(
        "SELECT session_id, type, COUNT(*) FROM patterns GROUP BY session_id, type"
    ):
        key = sid_to_task.get(sid)
        if key is None:
            continue  # pattern for a session not in sessions table (shouldn't happen)
        field = PATTERN_FIELD.get(ptype)
        if field:
            stats[key][field] += n

    # 3) events by session,subtype (events totals + thinking/prompts)
    for sid, subtype, n in cur.execute(
        "SELECT session_id, subtype, COUNT(*) FROM events GROUP BY session_id, subtype"
    ):
        key = sid_to_task.get(sid)
        if key is None:
            continue
        s = stats[key]
        s["events"] += n
        if subtype == "message.assistant.thinking":
            s["thinking"] += n
        elif subtype == "message.user.prompt":
            s["prompts"] += n

    # 4) tool_use payloads -> per-agent tool + model frequency
    for sid, payload in cur.execute(
        "SELECT session_id, payload FROM events WHERE subtype = ?", (TOOL_USE,)
    ):
        key = sid_to_task.get(sid)
        if key is None:
            continue
        s = stats[key]
        s["tool_use"] += 1
        try:
            data = json.loads(payload).get("data", {})
        except (ValueError, TypeError):
            continue
        tool = data.get("tool")
        if tool:
            s["tools"][tool] += 1
            s["tool_use_named"] += 1
        model = data.get("model")
        if model:
            s["models"][model] += 1

    con.close()

    # 5) assemble output
    def finalize(s):
        out = dict(s)
        out.pop("session_ids", None)
        out["tools"] = dict(sorted(s["tools"].items(), key=lambda x: -x[1]))
        out["models"] = dict(sorted(s["models"].items(), key=lambda x: -x[1]))
        ea = s["eval"] + s["apply"]
        out["eval_apply_ratio"] = round(s["eval"] / s["apply"], 3) if s["apply"] else None
        out["eval_apply_total"] = ea
        out["avg_duration_min"] = (
            round(s["duration_s_total"] / s["duration_sessions"] / 60.0, 1)
            if s["duration_sessions"] else None
        )
        out["avg_events_per_session"] = (
            round(s["events"] / s["sessions"], 1) if s["sessions"] else 0
        )
        out["tool_coverage"] = (
            round(s["tool_use_named"] / s["tool_use"], 2) if s["tool_use"] else None
        )
        out.pop("duration_s_total", None)
        return out

    agents_out = {}
    for tid in canonical:
        s = stats.get(tid)
        m = map_by_id[tid]
        base = {
            "taskId": tid,
            "category": m.get("category"),
            "schedule": m.get("schedule"),
            "cron": m.get("cron"),
            "thinkers": m.get("thinkers", []),
            "constitutions": m.get("constitutions", []),
            "captured": s is not None,
        }
        if s:
            base.update(finalize(s))
        else:
            base.update({"sessions": 0, "events": 0, "eval": 0, "apply": 0,
                         "captured": False})
        agents_out[tid] = base

    reserved = set(canonical) | {"(interactive)", "(unmatched)", "(excluded)"}
    discovered_out = {}
    for key in sorted(stats):
        if key in reserved:
            continue
        d = finalize(stats[key])
        d.update({
            "taskId": key,
            "category": "discovered",
            "schedule": None,
            "cron": None,
            "thinkers": [],
            "constitutions": [],
            "captured": True,
            "discovered": True,
            "needs_curation": True,
        })
        discovered_out[key] = d

    buckets = {}
    for k in ("(interactive)", "(unmatched)", "(excluded)"):
        if k in stats:
            buckets[k] = finalize(stats[k])

    total_sessions = sum(s["sessions"] for s in stats.values())
    total_events = sum(s["events"] for s in stats.values())
    captured = sum(1 for a in agents_out.values() if a["captured"])

    out = {
        "_meta": {
            "generated": datetime.now().astimezone().isoformat(),
            "source": "openstory-db",
            "db_path": args.db,
            "db_mtime": datetime.fromtimestamp(os.path.getmtime(args.db)).isoformat(),
            "join": "sessions.label name=\"...\" -> roster taskId (exact/unique-prefix); clean non-roster scheduled names self-attribute as discovered agents; no-name sessions -> (interactive)",
            "caveats": {
                "avg_duration_min": "session run-span (last_event - first_event); reliable for single-run agents, inflated for long-lived/append sessions",
                "tool_coverage": "fraction of tool_use events exposing data.tool; older (pre-tool-field) sessions read 0 and yield sparse tool maps",
            },
            "roster_size": len(canonical),
            "roster_captured": captured,
            "discovered_count": len(discovered_out),
            "excluded_sessions": stats["(excluded)"]["sessions"] if "(excluded)" in stats else 0,
            "excluded_substrings": list(EXCLUDED_PROJECT_SUBSTRINGS),
            "total_sessions": total_sessions,
            "total_events": total_events,
            "discovered_agents": dict(discovered_frags),
            "unmatched_label_fragments": dict(unmatched_frags),
            "ambiguous_label_fragments": dict(ambiguous_frags),
        },
        "agents": agents_out,
        "discovered": discovered_out,
        "buckets": buckets,
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)

    print("Wrote %s" % args.out)
    print("  roster: %d/%d captured | sessions=%d events=%d"
          % (captured, len(canonical), total_sessions, total_events))
    if discovered_out:
        print("  discovered agents (self-attributed, need curation): %d distinct"
              % len(discovered_out))
    if "(excluded)" in stats:
        print("  excluded (cross-project, e.g. BOSCO): %d sessions isolated"
              % stats["(excluded)"]["sessions"])
    if unmatched_frags:
        print("  unmatched label fragments: %d distinct (see _meta)" % len(unmatched_frags))
    if ambiguous_frags:
        print("  AMBIGUOUS fragments (need attention): %s" % dict(ambiguous_frags))


if __name__ == "__main__":
    run_with_retry(main)

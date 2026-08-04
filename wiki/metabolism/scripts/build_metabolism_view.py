#!/usr/bin/env python3
"""
build_metabolism_view.py
------------------------
Prototype generator for the C2A2 "Agentic Metabolism" view (Pathway 29).

Reads the OpenStory SQLite store (read-only) and emits:
  - metabolism_data.json : per-session rows (timestamp, duration, events, tokens)
                           grouped by agent taskId, plus an (interactive) lane.
  - metabolism_view.html : self-contained, data inlined, double-clickable.

Reuses the label->taskId join discipline from extract_openstory_agent_data.py
(agent_map.json is the source of truth). Read-only by construction; never writes
the DB.

This is a PROTOTYPE built only from data that already exists. The "yield" axis
is deliberately present-but-disabled in the UI: it needs a usefulness definition
(Level-1 measurement framework) before it can be computed. That is the reserved
architectural space.

Usage:
  python3 build_metabolism_view.py [--db PATH] [--map PATH] [--outdir DIR]
"""

import argparse
import csv
import glob
import json
import os
import re
import sqlite3
import subprocess
import sys
import urllib.parse
from collections import defaultdict
from datetime import datetime

HOME = os.path.expanduser("~")
DEFAULT_DB = os.path.join(HOME, "Documents/Non-Claude Projects/OpenStory/data/open-story.db")
DEFAULT_MAP = os.path.join(HOME, "Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/agents/openstory/agent_map.json")

# How old the newest cross-tradition signal may get before compute_signal_yield
# says so out loud. 21 days: the sources behind it (pattern-detector findings,
# the cross-program index, approved review cards) are bursty, so a fortnight of
# quiet is normal and three weeks is not.
SIGNAL_STALE_WARN_DAYS = 21
# Filled in by compute_signal_yield; copied into _meta so the axis ships its own
# provenance rather than a bare, unreadable zero.
SIGNAL_SOURCE = {"status": "not_read"}


def connect_ro(db_path):
    if not os.path.exists(db_path):
        sys.exit("ERROR: DB not found: %s" % db_path)
    uri = "file:%s?mode=ro" % urllib.parse.quote(db_path)
    con = sqlite3.connect(uri, uri=True)
    res = con.execute("PRAGMA quick_check").fetchone()[0]
    if res != "ok":
        sys.exit("ERROR: DB failed quick_check: %s" % res)
    return con


def label_fragment(label):
    if not label:
        return None
    m = re.search(r'name="([^"]*)', label)
    if not m:
        return None
    frag = m.group(1).strip()
    return frag or None


def build_resolver(canonical):
    canon_set = set(canonical)

    def resolve(frag):
        if frag is None:
            return None
        if frag in canon_set:
            return frag
        prefixed = [t for t in canonical if t.startswith(frag)]
        if len(prefixed) == 1:
            return prefixed[0]
        return None

    return resolve


def duration_min(first, last):
    try:
        a = datetime.fromisoformat(first.replace("Z", "+00:00"))
        b = datetime.fromisoformat(last.replace("Z", "+00:00"))
        d = (b - a).total_seconds() / 60.0
        return round(d, 1) if d >= 0 else None
    except (ValueError, AttributeError):
        return None


def regen_prs_yield(repo, out_dir, prs_csv):
    """Refresh the WS2 PRS metric, then prove it is actually fresh. Fails loud.

    WHY (2026-07-29): this module used to just read whichever prs_yield_detail.csv
    happened to be checked in, and NOTHING regenerated it. The file was last
    written 2026-06-30, so the 85 triplets articulated on 07-01 (21) and 07-21 (64)
    were invisible: the Metabolism tab's PRS-articulated axis flatlined after
    2026-06-17 and read "no PRS triplets since mid-June" while production had in
    fact continued. Worse, the one bar that did show -- 144 on 06-30 -- was the
    Track A backlog clear, a first-seen batch rather than a production day, so the
    axis was not merely incomplete but actively misleading.

    DECISION-058 designates this CSV the single source of truth for both PRS axes
    AND the connectome, "so these axes and the connectome can never disagree".
    That holds only while something regenerates it. A single source that nothing
    refreshes is stale by construction, and 512-vs-427 is what disagreement looks
    like. House Rule 5 -- if code can answer, code answers -- so the regen happens
    here rather than in a manual step somebody has to remember. This is the same
    discipline stamp_assets.py applies to iframe asset versions, and for the same
    reason: forgetting the manual bump IS the repeatable error.

    prs_yield.py carries its own Rule 12 assertion (ids on disk but absent from git
    history abort the run), so a non-zero exit means a real inconsistency and must
    propagate, never be swallowed into silently-frozen axes.
    """
    script = os.path.join(repo, "wiki", "architecture", "metrics", "prs_yield.py")
    if not os.path.isfile(script):
        sys.exit("FAIL (Rule 12): %s missing; refusing to build PRS yield axes "
                 "from an unrefreshable snapshot." % script)
    try:
        r = subprocess.run([sys.executable, script, "--repo", repo,
                            "--out-dir", out_dir],
                           capture_output=True, text=True, timeout=600)
    except (OSError, subprocess.SubprocessError) as e:
        sys.exit("FAIL (Rule 12): could not run prs_yield.py: %s" % e)
    if r.returncode != 0:
        sys.exit("FAIL (Rule 12): prs_yield.py exited %d; PRS axes NOT built.\n%s"
                 % (r.returncode, (r.stderr or r.stdout or "").strip()))
    if not os.path.isfile(prs_csv):
        sys.exit("FAIL (Rule 12): prs_yield.py reported success but %s is absent."
                 % prs_csv)

    # Freshness, proven by CONTENT rather than by mtime.
    #
    # An mtime comparison was tried here first and is wrong: git does not preserve
    # mtimes, so any checkout stamps every tradition file with the checkout time.
    # A CSV can then be months out of date and still test "newer than its sources"
    # -- which is exactly the shape of the bug this guard exists to catch (the
    # 2026-06-30 CSV was newer on disk than the 07-21 triplets that it omitted).
    #
    # So compare the sets directly: every (tradition, PRS-NN) present on disk must
    # appear in the CSV. Deterministic, mtime-independent, and it fires on the real
    # failure -- a regen that "succeeded" while writing somewhere else leaves the
    # tracked CSV short, and 427-vs-510 is not a subtle difference.
    sources = sorted(glob.glob(os.path.join(repo, "wiki", "traditions",
                                            "*", "prs_triplets.md")))
    if not sources:
        sys.exit("FAIL (Rule 12): no wiki/traditions/*/prs_triplets.md found; "
                 "the PRS axes would be silently empty.")
    # Same marker prs_yield.py keys on: a line that is exactly "PRS-NN:".
    prs_line = re.compile(r"^PRS-(\d+):\s*$")
    on_disk = set()
    for path in sources:
        tradition = os.path.basename(os.path.dirname(path))
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                mm = prs_line.match(line)
                if mm:
                    on_disk.add((tradition, "PRS-%02d" % int(mm.group(1))))
    in_csv = set()
    with open(prs_csv, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            in_csv.add(((row.get("tradition") or "").strip(),
                        (row.get("prs_id") or "").strip()))
    absent = sorted(on_disk - in_csv)
    if absent:
        sys.exit("FAIL (Rule 12): %d triplet(s) present on disk but absent from "
                 "%s -- the PRS axes would undercount. First few: %s"
                 % (len(absent), prs_csv,
                    ", ".join("%s/%s" % t for t in absent[:8])))
    sys.stderr.write("PRS yield refreshed: %d rows, all %d on-disk triplets "
                     "accounted for\n" % (len(in_csv), len(on_disk)))


def compute_vault_yield(repo):
    """Per-day vault yield from git history (real, not a placeholder):
    wikilinks added/removed, .md files added, commit count, and new PRS ids
    first-seen per day (from the WS2 metric CSV). Read-only."""
    try:
        log = subprocess.run(
            ["git", "-C", repo, "log", "--reverse", "--pretty=%H|%ad",
             "--date=short", "--", "wiki/"],
            capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
    except (OSError, subprocess.SubprocessError):
        return None
    if not log:
        return None
    daily = defaultdict(lambda: {"links_added": 0, "links_removed": 0,
                                 "files_added": 0, "commits": 0,
                                 "prs_added": 0, "prs_articulated": 0,
                                 "signals": 0})
    for line in log:
        try:
            sha, date = line.split("|")
        except ValueError:
            continue
        d = daily[date]
        d["commits"] += 1
        diff = subprocess.run(
            ["git", "-C", repo, "show", sha, "--", "wiki/**/*.md", "wiki/*.md"],
            capture_output=True, text=True).stdout
        for ln in diff.splitlines():
            if ln[:4] in ("+++ ", "--- "):
                continue
            if ln.startswith("+"):
                d["links_added"] += ln.count("[[")
            elif ln.startswith("-"):
                d["links_removed"] += ln.count("[[")
        st = subprocess.run(
            ["git", "-C", repo, "show", "--name-status", "--pretty=",
             "--diff-filter=A", sha, "--", "wiki/"],
            capture_output=True, text=True).stdout
        d["files_added"] += sum(1 for x in st.splitlines() if x.strip().endswith(".md"))

    # PRS-triplet yield: two per-day series, both from the WS2 single source of
    # truth (architecture/metrics/prs_yield_detail.csv, produced by prs_yield.py),
    # so these axes and the connectome can never disagree (DECISION-058).
    #   prs_added       = git first-seen date (objective, but backfill-clustered)
    #   prs_articulated = self-reported Date Added (when the work was done)
    import csv
    prs_dir = os.path.join(repo, "wiki", "architecture", "metrics")
    prs_csv = os.path.join(prs_dir, "prs_yield_detail.csv")
    regen_prs_yield(repo, prs_dir, prs_csv)
    with open(prs_csv, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            seen = (row.get("first_seen_date") or "").strip()
            if seen:
                daily[seen]["prs_added"] += 1
            made = (row.get("date_added") or "").strip()
            if made:
                daily[made]["prs_articulated"] += 1

    # Cross-tradition signal yield: a signal-only day (no vault commit) gets its
    # own daily entry via the defaultdict, so it still draws a bar.
    for d, n in compute_signal_yield(
            os.path.join(repo, "wiki", "level2_signal_stream.html")).items():
        daily[d]["signals"] += n

    return [dict(date=k, **v) for k, v in sorted(daily.items())]


def compute_signal_yield(sig_html):
    """Per-day count of dated cross-tradition signals from the Interactions
    Level-2 stream -- the SIG array inlined in level2_signal_stream.html, the
    same dated dataset the Interactions tab shows (its upstream extract_signals.py
    is out-of-git, so this in-repo HTML is the canonical in-tree source). Distinct
    from the PRS-similarity connectome cross-edges, which are static/undated.
    Returns {date: count}; warns and returns empty if the source is unreadable.

    Also records what it found in SIGNAL_SOURCE, which main() copies into _meta.
    A frozen source and a genuinely quiet upstream both render as a flat zero on
    this axis, and for six weeks (2026-06-23 -> 2026-08-04) it WAS frozen: the
    stream was a hand-built 2026-06-28 artifact nobody rebuilt, hiding 192
    signals. The axis must therefore carry its own provenance, so a zero can be
    read as 'no signals' or 'stale source' without opening another file."""
    out = defaultdict(int)
    if not os.path.isfile(sig_html):
        SIGNAL_SOURCE["status"] = "missing"
        sys.stderr.write("WARN: %s missing; signals yield axis will be empty\n" % sig_html)
        return out
    try:
        shtml = open(sig_html, encoding="utf-8").read()
        j = shtml.index("const SIG = ") + len("const SIG = ")
        sig_arr, _ = json.JSONDecoder().raw_decode(shtml, j)
    except (ValueError, OSError) as e:
        SIGNAL_SOURCE["status"] = "unparseable"
        sys.stderr.write("WARN: could not parse signals from %s: %s\n" % (sig_html, e))
        return out
    for rec in sig_arr:
        d = (rec.get("date") or "").strip()
        if re.match(r"^\d{4}-\d{2}-\d{2}$", d):
            out[d] += 1

    SIGNAL_SOURCE.update(status="ok", records=len(sig_arr), dated=sum(out.values()),
                         latest=(max(out) if out else None))
    if out:
        stale = (datetime.now().date()
                 - datetime.strptime(max(out), "%Y-%m-%d").date()).days
        SIGNAL_SOURCE["stale_days"] = stale
        if stale > SIGNAL_STALE_WARN_DAYS:
            # Not fatal: the snapshot is still an accurate picture of a stale
            # source. Fatal would block every metabolism refresh on an unrelated
            # pipeline. Loud, and recorded in _meta, is the honest middle.
            sys.stderr.write(
                "WARN: cross-tradition signal source is %d days stale (newest %s). "
                "The yield_signals axis will read 0 for every day since. "
                "Rebuild it: bash scripts/regen_level2_signals.sh\n" % (stale, max(out)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--map", default=DEFAULT_MAP)
    ap.add_argument("--repo", default=os.path.join(HOME,
                    "Documents/Claude/Projects/RC Karpathy Wiki Project"),
                    help="git repo root containing the wiki/ vault (for yield series)")
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--from-json", default=None,
                    help="render HTML from an existing metabolism_data.json; skip DB/git "
                         "(view-layer changes only; no re-ingest)")
    args = ap.parse_args()

    if args.from_json:
        with open(args.from_json) as fj:
            data = json.load(fj)
        os.makedirs(args.outdir, exist_ok=True)
        html_path = os.path.join(args.outdir, "metabolism_view.html")
        with open(html_path, "w") as fh:
            fh.write(HTML_TEMPLATE.replace("/*__DATA__*/", json.dumps(data)))
        print("Wrote %s (rendered from %s)" % (html_path, args.from_json))
        return

    with open(args.map) as f:
        agent_map = json.load(f)
    map_by_id = {a["taskId"]: a for a in agent_map["agents"]}
    canonical = list(map_by_id.keys())
    resolve = build_resolver(canonical)

    con = connect_ro(args.db)
    cur = con.cursor()

    # 1) sessions -> lane key (agent taskId, or (interactive) for human-driven)
    sid_key = {}
    sess = {}
    for sid, label, ecount, first, last in cur.execute(
        "SELECT id, label, event_count, first_event, last_event FROM sessions"
    ):
        frag = label_fragment(label)
        key = resolve(frag) if frag else "(interactive)"
        if key is None:
            key = "(unmatched)"
        sid_key[sid] = key
        sess[sid] = {
            "first": first,
            "last": last,
            "events": ecount or 0,
            "in": 0, "out": 0, "cache_read": 0, "cache_creation": 0,
            "thinking_tokens": 0,
            "thinking_chars": 0, "thinking_blocks": 0,
        }

    # 2) token sums per session from assistant message payloads
    for sid, payload in cur.execute(
        "SELECT session_id, payload FROM events "
        "WHERE subtype LIKE 'message.assistant%' AND payload IS NOT NULL"
    ):
        s = sess.get(sid)
        if s is None:
            continue
        try:
            _d = json.loads(payload).get("data") or {}
            # OpenStory migrated its event-payload schema on 2026-04-07:
            # token_usage moved from data.token_usage to
            # data.agent_payload.token_usage. Read both so sessions on either
            # side of the migration are counted (pre-fix, everything after
            # 2026-04-06 read as zero tokens and the interactive lane vanished).
            u = _d.get("token_usage") or (_d.get("agent_payload") or {}).get("token_usage")
        except (ValueError, TypeError):
            continue
        if not u:
            continue
        s["in"] += u.get("input_tokens", 0) or 0
        s["out"] += u.get("output_tokens", 0) or 0
        s["cache_read"] += u.get("cache_read_input_tokens", 0) or 0
        s["cache_creation"] += u.get("cache_creation_input_tokens", 0) or 0

    # 3) thinking tokens (separate 'system.thinking_tokens' subtype).
    #    THINKING-TOKEN JOIN FIX (2026-06-22): these events carry the sentinel
    #    session_id "audit" in the events.session_id column; the REAL session id is
    #    nested at data.raw.session_id, and data.raw.estimated_tokens_delta is the
    #    per-event token estimate. The previous COUNT(*) GROUP BY session_id therefore
    #    dumped all ~41k events under the single "audit" key and read 0 in every real
    #    lane. We now sum estimated_tokens_delta keyed on the real nested session id,
    #    so thinking_tokens carries actual estimated thinking tokens (not an event count).
    for (payload,) in cur.execute(
        "SELECT payload FROM events "
        "WHERE subtype = 'system.thinking_tokens' AND payload IS NOT NULL"
    ):
        try:
            raw = (json.loads(payload).get("data") or {}).get("raw") or {}
            rsid = raw.get("session_id")
            delta = raw.get("estimated_tokens_delta") or 0
        except (ValueError, TypeError):
            continue
        s = sess.get(rsid)
        if s is not None:
            s["thinking_tokens"] += delta

    # 3b) thinking CONTENT from the 'message.assistant.thinking' subtype, captured
    #     CONTINUOUSLY (back to March, per lane from its first run) -- unlike the
    #     'system.thinking_tokens' accounting in (3), which is audit-emitted (sentinel
    #     session_id="audit") and exists only on a handful of June days. We record TWO
    #     things per thinking block (data.raw.message.content[type=="thinking"]):
    #       thinking_blocks = COUNT of reasoning blocks. This is the PRIMARY continuous,
    #         universal measure: every lane has it from its first run.
    #       thinking_chars  = length of the block's plaintext, when present. IMPORTANT
    #         (Phase-1 finding 2026-06-23): the plaintext is STRIPPED (empty string,
    #         signature only) for the large majority of agent runs -- many agentic lanes
    #         are 100% empty (redacted/encrypted thinking). So thinking_chars measures
    #         TEXT-RETENTION, not reasoning volume, and is kept for the tooltip only, not
    #         as the headline metric. Use thinking_blocks for the gap-free cadence of
    #         reasoning. See metabolism-monitor/logbook.md.
    for sid, payload in cur.execute(
        "SELECT session_id, payload FROM events "
        "WHERE subtype = 'message.assistant.thinking' AND payload IS NOT NULL"
    ):
        s = sess.get(sid)
        if s is None:
            continue
        try:
            raw = (json.loads(payload).get("data") or {}).get("raw") or {}
            content = ((raw.get("message") or {}).get("content")) or []
        except (ValueError, TypeError):
            continue
        for item in content:
            if isinstance(item, dict) and item.get("type") == "thinking":
                s["thinking_blocks"] += 1
                t = item.get("thinking")
                if isinstance(t, str):
                    s["thinking_chars"] += len(t)

    con.close()

    # 4) assemble per-lane rows. Keep only sessions with any token signal OR
    #    that belong to a real agent (so empty agents still show their cadence).
    lanes = defaultdict(list)
    for sid, s in sess.items():
        key = sid_key[sid]
        if key == "(unmatched)":
            continue
        has_tokens = (s["in"] or s["out"] or s["cache_read"] or s["cache_creation"])
        if not has_tokens and key == "(interactive)":
            continue  # interactive lane: only token-bearing runs, keeps it legible
        if not s["first"]:
            continue
        lanes[key].append({
            "sid": sid,
            "t": s["first"],
            "dur_min": duration_min(s["first"], s["last"]),
            "events": s["events"],
            "in": s["in"], "out": s["out"],
            "cache_read": s["cache_read"], "cache_creation": s["cache_creation"],
            "total": s["in"] + s["out"] + s["cache_read"] + s["cache_creation"],
            "thinking_tokens": s["thinking_tokens"],
            "thinking_chars": s["thinking_chars"],
            "thinking_blocks": s["thinking_blocks"],
        })

    # 5) lane metadata + ordering (by total output tokens desc)
    lane_meta = []
    all_t = []
    for key, rows in lanes.items():
        rows.sort(key=lambda r: r["t"])
        all_t.extend(r["t"] for r in rows)
        if key == "(interactive)":
            label = "Human-driven (interactive)"
            cat = "interactive"
            thinkers = []
        else:
            m = map_by_id.get(key, {})
            thinkers = m.get("thinkers", [])
            cat = m.get("category", "agent")
            label = (" + ".join(thinkers)) if thinkers else key
        # inter-run intervals (hours) between consecutive runs
        gaps = []
        for a, b in zip(rows, rows[1:]):
            try:
                ta = datetime.fromisoformat(a["t"].replace("Z", "+00:00"))
                tb = datetime.fromisoformat(b["t"].replace("Z", "+00:00"))
                gaps.append((tb - ta).total_seconds() / 3600.0)
            except ValueError:
                pass
        gaps.sort()
        median_gap = round(gaps[len(gaps) // 2], 1) if gaps else None
        lane_meta.append({
            "key": key, "label": label, "category": cat, "thinkers": thinkers,
            "schedule": map_by_id.get(key, {}).get("schedule"),
            "runs": len(rows),
            "out_total": sum(r["out"] for r in rows),
            "all_total": sum(r["total"] for r in rows),
            "median_gap_h": median_gap,
            "rows": rows,
        })
    lane_meta.sort(key=lambda L: L["out_total"], reverse=True)

    data = {
        "_meta": {
            "generated": datetime.now().astimezone().isoformat(),
            "source": "openstory-db",
            "db_path": args.db,
            "db_mtime": datetime.fromtimestamp(os.path.getmtime(args.db)).isoformat(),
            "lanes": len(lane_meta),
            "total_runs": sum(L["runs"] for L in lane_meta),
            "t_min": min(all_t) if all_t else None,
            "t_max": max(all_t) if all_t else None,
            "note": "Prototype. Token data summed from event payloads in open-story.db "
                    "(both pre/post 2026-04-07 token_usage paths). Thinking: the PRIMARY "
                    "metric is 'thinking steps (count)' = number of message.assistant.thinking "
                    "blocks, captured CONTINUOUSLY (every lane from its first run). Two other "
                    "thinking figures appear in the tooltip but are NOT good headline metrics: "
                    "'chars retained' = plaintext length, which is STRIPPED (signature-only, "
                    "empty) for the majority of agent runs, so it measures text-retention not "
                    "reasoning; 'audit-tok' = system.thinking_tokens estimated_tokens_delta, "
                    "audit-emitted and present only on a few June days. All bucketed by session "
                    "start like every other metric. Yield = wikilinks/files "
                    "added per day PLUS PRS-triplet "
                    "yield (first-seen and articulated series) from wiki/ git history and the "
                    "WS2 metric CSV (DECISION-058); PRS yield is LIVE, not 'still to come'. "
                    "Cross-tradition signals/day (yield_signals) are counted from the dated "
                    "Interactions Level-2 signal stream.",
        },
        "lanes": lane_meta,
        "yield_daily": compute_vault_yield(args.repo) or [],
    }
    # After the literal, not inside it: dict values evaluate in order, so _meta
    # is already built by the time compute_vault_yield -> compute_signal_yield
    # fills SIGNAL_SOURCE.
    data["_meta"]["signal_source"] = dict(SIGNAL_SOURCE)

    os.makedirs(args.outdir, exist_ok=True)
    json_path = os.path.join(args.outdir, "metabolism_data.json")
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)

    html_path = os.path.join(args.outdir, "metabolism_view.html")
    with open(html_path, "w") as f:
        f.write(HTML_TEMPLATE.replace("/*__DATA__*/", json.dumps(data)))

    print("Wrote %s" % json_path)
    print("Wrote %s" % html_path)
    print("  lanes=%d runs=%d range=%s..%s"
          % (len(lane_meta), data["_meta"]["total_runs"],
             data["_meta"]["t_min"], data["_meta"]["t_max"]))
    print("  signal source: %s" % data["_meta"]["signal_source"])


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>C2A2 Agentic Metabolism — prototype</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<style>
  :root { --bg:#0a0a0f; --panel:#14141c; --ink:#e8e8f0; --dim:#8a8aa0; --line:#2a2a38; --accent:#C9A84C; }
  html,body { margin:0; background:var(--bg); color:var(--ink);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; }
  header { padding:14px 20px; border-bottom:1px solid var(--line); }
  h1 { font-size:17px; margin:0 0 3px; font-weight:600; letter-spacing:.2px; }
  .sub { font-size:12px; color:var(--dim); }
  .bar { display:flex; gap:18px; align-items:center; flex-wrap:wrap;
    padding:10px 20px; border-bottom:1px solid var(--line); font-size:13px; }
  .bar label { color:var(--dim); margin-right:6px; }
  select { background:var(--panel); color:var(--ink); border:1px solid var(--line);
    border-radius:6px; padding:4px 8px; font-size:13px; }
  option:disabled { color:#555; }
  .note { font-size:12px; color:var(--accent); }
  #wrap { padding:8px 8px 30px; overflow-x:auto; }
  .lane-label { font-size:11px; fill:var(--ink); }
  .lane-meta { font-size:10px; fill:var(--dim); }
  .axis text { fill:var(--dim); font-size:10px; }
  .axis line, .axis path { stroke:var(--line); }
  .gridline { stroke:var(--line); stroke-opacity:.4; }
  .run { stroke:#0a0a0f; stroke-width:.5; cursor:pointer; }
  .run:hover { stroke:#fff; stroke-width:1.5; }
  #tip { position:fixed; pointer-events:none; background:#1c1c28; border:1px solid var(--line);
    border-radius:8px; padding:9px 11px; font-size:12px; line-height:1.5; max-width:300px;
    opacity:0; transition:opacity .08s; box-shadow:0 6px 24px rgba(0,0,0,.5); z-index:10; }
  #tip b { color:var(--accent); }
  .legend { display:flex; gap:14px; flex-wrap:wrap; padding:4px 20px 12px; font-size:11px; color:var(--dim); }
  .legend span { display:inline-flex; align-items:center; gap:5px; }
  .dot { width:10px; height:10px; border-radius:50%; display:inline-block; }
</style>
</head>
<body>
<header>
  <h1>C2A2 Agentic Metabolism <span style="color:var(--dim);font-weight:400">— prototype (Pathway 29)</span></h1>
  <div class="sub" id="meta"></div>
</header>
<div class="bar">
  <div><label>View</label>
    <select id="view">
      <option value="raster" selected>Raster (per-agent runs)</option>
      <option value="wave">Waveform (system pulse)</option>
      <option value="dual">Returned vs sent (tokens)</option>
    </select>
  </div>
  <div><label>Amplitude</label>
    <select id="metric">
      <option value="events" selected>Events (activity)</option>
      <option value="out">Output tokens (work produced)</option>
      <option value="total">Total tokens (in+out+cache)</option>
      <option value="cache_read">Cache-read tokens (recirculated)</option>
      <option value="thinking_blocks">Thinking steps (count ✦ continuous)</option>
      <option value="thinking_tokens">Thinking tokens (audit est. ✦ Jun+ only)</option>
      <option value="dur_min">Duration (min)</option>
      <option value="yield_files">Yield: files added/day ✦ headline</option>
      <option value="yield_links">Yield: wikilinks added/day ✦ live</option>
      <option value="yield_prs">Yield: PRS first-seen/day ✦ git</option>
      <option value="yield_prs_made">Yield: PRS articulated/day ✦ date-added</option>
      <option value="yield_signals">Yield: cross-tradition signals/day ✦ interactions</option>
    </select>
  </div>
  <div><label>Color</label>
    <select id="color">
      <option value="category">By category</option>
      <option value="cache_ratio">By cache-read share</option>
    </select>
  </div>
  <div id="logwrap"><label>Log Y</label><input type="checkbox" id="logy"></div>
  <div class="note" title="Yield is now computed from wiki/ git history.">
    ◆ Yield is a live axis (vault git): wikilinks, files &amp; PRS triplets/day. PRS first-seen = the git commit-day a PRS-NN id first appeared; PRS articulated = its self-reported Date Added (when the work was done). Both from the WS2 metric across traditions/*/prs_triplets.md (DECISION-058).
  </div>
</div>
<div class="legend" id="legend"></div>
<div id="wrap"><svg id="chart"></svg></div>
<div id="tip"></div>
<script>
const DATA = /*__DATA__*/;
const lanes = DATA.lanes;
const meta = DATA._meta;
const fmt = d3.format(",");
const _tmax = meta.t_max ? new Date(meta.t_max) : null;
const _ageDays = _tmax ? Math.floor((Date.now()-_tmax)/864e5) : null;
document.getElementById("meta").textContent =
  `${meta.lanes} lanes · ${fmt(meta.total_runs)} runs · `
  + `${(meta.t_min||"").slice(0,10)} → ${(meta.t_max||"").slice(0,10)} · `
  + `source: open-story.db (${(meta.db_mtime||"").slice(0,10)})`
  + (_ageDays!=null && _ageDays>1 ? ` · ⚠ snapshot ${_ageDays}d old — regen to extend right edge` : "");

const catColor = d3.scaleOrdinal()
  .domain(["c2a2-thinker","c2a2-master","c2a2-meta","c2a2-infra","interactive","agent"])
  .range(["#5A8EAF","#C9A84C","#8B6DAE","#4A8A7A","#C47A9A","#9A7A5A"]);

const tip = document.getElementById("tip");
const margin = {top:24, right:30, bottom:34, left:210};
const rowH = 30;

function renderRaster() {
  const metric = document.getElementById("metric").value;
  const colorBy = document.getElementById("color").value;

  const width = Math.max(900, (document.getElementById("wrap").clientWidth || 1000) - 20);
  const innerW = width - margin.left - margin.right;
  const innerH = lanes.length * rowH;
  const height = innerH + margin.top + margin.bottom;

  const svg = d3.select("#chart").attr("width", width).attr("height", height);
  svg.selectAll("*").remove();
  const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleTime()
    .domain([new Date(meta.t_min), new Date(meta.t_max)]).range([0, innerW]).nice();
  const y = d3.scaleBand()
    .domain(lanes.map(L => L.key)).range([0, innerH]).paddingInner(0.25);

  // amplitude radius scale (sqrt; robust to huge cache values)
  let maxAmp = 1;
  lanes.forEach(L => L.rows.forEach(r => { maxAmp = Math.max(maxAmp, +r[metric]||0); }));
  const r = d3.scaleSqrt().domain([0, maxAmp]).range([1.5, 14]);

  // gridlines
  g.append("g").attr("class","axis")
    .attr("transform", `translate(0,${innerH})`)
    .call(d3.axisBottom(x).ticks(8).tickFormat(d3.timeFormat("%b %d")));
  x.ticks(8).forEach(t => {
    g.append("line").attr("class","gridline")
      .attr("x1", x(t)).attr("x2", x(t)).attr("y1", 0).attr("y2", innerH);
  });

  // lane rows
  const lane = g.selectAll(".lane").data(lanes).join("g")
    .attr("transform", L => `translate(0,${y(L.key)})`);

  lane.append("text").attr("class","lane-label")
    .attr("x", -margin.left+6).attr("y", y.bandwidth()/2 - 2)
    .text(L => L.label.length>30 ? L.label.slice(0,29)+"…" : L.label);
  lane.append("text").attr("class","lane-meta")
    .attr("x", -margin.left+6).attr("y", y.bandwidth()/2 + 11)
    .text(L => `${L.runs} runs · ${L.schedule||"on-demand"}`
      + (L.median_gap_h!=null ? ` · ~${L.median_gap_h}h gap` : ""));

  lane.append("line").attr("class","gridline")
    .attr("x1",0).attr("x2",innerW)
    .attr("y1",y.bandwidth()/2).attr("y2",y.bandwidth()/2);

  const TOKEN_METRICS = ["out","total","cache_read","thinking_tokens","thinking_blocks"];
  const isTok = TOKEN_METRICS.includes(metric);
  lane.each(function(L) {
    d3.select(this).selectAll(".run").data(L.rows).join("circle")
      .attr("class","run")
      .attr("cx", d => x(new Date(d.t)))
      .attr("cy", y.bandwidth()/2)
      .attr("r", d => { const v=+d[metric]||0; return (isTok && v===0) ? 3 : r(v); })
      .attr("fill", d => {
        const v=+d[metric]||0;
        if (isTok && v===0) return "none";
        if (colorBy==="cache_ratio") {
          const tot = d.total||1; const sh = (d.cache_read||0)/tot;
          return d3.interpolateViridis(sh);
        }
        return catColor(L.category);
      })
      .attr("stroke", d => { const v=+d[metric]||0; return (isTok && v===0) ? catColor(L.category) : "#0a0a0f"; })
      .attr("stroke-dasharray", d => { const v=+d[metric]||0; return (isTok && v===0) ? "2,1.5" : "none"; })
      .attr("fill-opacity", 0.82)
      .on("mousemove", (ev,d) => {
        tip.style.opacity=1;
        tip.style.left=(ev.clientX+14)+"px"; tip.style.top=(ev.clientY+14)+"px";
        tip.innerHTML = `<b>${L.label}</b><br>${d.t.slice(0,16).replace("T"," ")}<br>`
          + `out <b>${fmt(d.out)}</b> · in ${fmt(d.in)}<br>`
          + `cache-read ${fmt(d.cache_read)} · create ${fmt(d.cache_creation)}<br>`
          + `thinking ${fmt(d.thinking_blocks)} steps · ${fmt(d.thinking_chars)} chars retained · ${fmt(d.thinking_tokens)} audit-tok<br>`
          + `events ${fmt(d.events)} · ${d.dur_min!=null?d.dur_min+" min":"dur n/a"}`;
      })
      .on("mouseleave", () => tip.style.opacity=0);
  });

  // legend
  const lg = document.getElementById("legend");
  if (colorBy==="category") {
    const cats = [...new Set(lanes.map(L=>L.category))];
    lg.innerHTML = cats.map(c =>
      `<span><i class="dot" style="background:${catColor(c)}"></i>${c}</span>`).join("");
  } else {
    lg.innerHTML = `<span>cache-read share: <i class="dot" style="background:${d3.interpolateViridis(0)}"></i> low `
      + `<i class="dot" style="background:${d3.interpolateViridis(.5)}"></i> `
      + `<i class="dot" style="background:${d3.interpolateViridis(1)}"></i> high</span>`
      + `<span style="margin-left:14px">circle size = amplitude metric</span>`;
  }
  if (isTok) {
    const zeroLanes = lanes.filter(L => !L.rows.some(r => (+r[metric]||0) > 0)).length;
    if (zeroLanes) lg.innerHTML += `<span style="margin-left:14px;color:var(--dim)">`
      + `○ ${zeroLanes} lanes: cadence only, no token payloads (instrumentation gap, not zero work)</span>`;
  }
}
const METRIC_LABEL = {events:"events", out:"output tokens", total:"total tokens",
  cache_read:"cache-read tokens", thinking_blocks:"thinking steps (count)",
  thinking_tokens:"thinking tokens (audit est., Jun+)",
  dur_min:"minutes", yield_links:"wikilinks added", yield_files:"files added",
  yield_prs:"PRS first-seen", yield_prs_made:"PRS articulated",
  yield_signals:"cross-tradition signals"};
const YIELD = DATA.yield_daily || [];

function interactiveHorizon() {
  const L = lanes.find(x => x.key === "(interactive)");
  if (!L || !L.rows.length) return null;
  return new Date(L.rows[L.rows.length-1].t);
}
function drawHorizon(g, x, innerH) {
  const hz = interactiveHorizon();
  if (!hz) return;
  g.append("line").attr("x1",x(hz)).attr("x2",x(hz)).attr("y1",0).attr("y2",innerH)
    .attr("stroke","#C47A9A").attr("stroke-width",1).attr("stroke-dasharray","4,3").attr("stroke-opacity",0.75);
  g.append("text").attr("x",x(hz)+4).attr("y",11).attr("fill","#C47A9A").style("font-size","10px")
    .text("interactive capture ends");
}

function frame() {
  const width = Math.max(900, (document.getElementById("wrap").clientWidth || 1000) - 20);
  const m = {top:24, right:30, bottom:34, left:64};
  const innerW = width - m.left - m.right, innerH = 460;
  const svg = d3.select("#chart").attr("width", width).attr("height", innerH+m.top+m.bottom);
  svg.selectAll("*").remove();
  const g = svg.append("g").attr("transform", `translate(${m.left},${m.top})`);
  return {g, innerW, innerH};
}
function axes(g, x, y, innerH, ylabel) {
  g.append("g").attr("class","axis").attr("transform",`translate(0,${innerH})`)
    .call(d3.axisBottom(x).ticks(10).tickFormat(d3.timeFormat("%b %d")));
  g.append("g").attr("class","axis").call(d3.axisLeft(y).ticks(6).tickFormat(d3.format("~s")));
  g.append("text").attr("transform","rotate(-90)").attr("x",-innerH/2).attr("y",-50)
    .attr("text-anchor","middle").attr("fill","var(--dim)").style("font-size","11px").text(ylabel);
}
function weekendBands(g, days, x, innerW, innerH) {
  days.forEach(d => { const wd = d.getUTCDay(); if (wd===0||wd===6) {
    g.append("rect").attr("x", x(d)).attr("y",0).attr("width", Math.max(1, innerW/days.length))
      .attr("height", innerH).attr("fill","#ffffff").attr("fill-opacity",0.03); }});
}
function dayAxis() {
  const day = d3.timeDay;
  const t0 = day.floor(new Date(meta.t_min)), t1 = day.ceil(new Date(meta.t_max));
  const days = day.range(t0, t1);
  return {day, t0, t1, days, idx:new Map(days.map((d,i)=>[+d,i]))};
}

function renderWave() {
  const metric = document.getElementById("metric").value;
  const logy = document.getElementById("logy").checked;
  const isYield = metric.startsWith("yield");
  const {g, innerW, innerH} = frame();
  const {day, t0, t1, days, idx} = dayAxis();
  const x = d3.scaleTime().domain([t0, t1]).range([0, innerW]);
  weekendBands(g, days, x, innerW, innerH);
  const lg = document.getElementById("legend");
  const ylabel = (METRIC_LABEL[metric]||metric) + " / day" + (logy?" (log)":"");

  if (isYield) {
    // yield as discrete day-bars: a bar = a real vault-commit day; an absent bar = no
    // commit that day (a true gap, NOT a zero). Fixes the trailing/interior "flat-zero"
    // valleys the area chart drew through sparse git history.
    const field = metric==="yield_files" ? "files_added"
                : metric==="yield_prs" ? "prs_added"
                : metric==="yield_prs_made" ? "prs_articulated"
                : metric==="yield_signals" ? "signals" : "links_added";
    const yUnit = metric==="yield_files" ? "files"
                : metric==="yield_prs" ? "PRS first-seen"
                : metric==="yield_prs_made" ? "PRS articulated"
                : metric==="yield_signals" ? "cross-tradition signals" : "wikilinks";
    const yColor = metric==="yield_prs" ? "#4A8A7A"
                : metric==="yield_prs_made" ? "#C47A9A"
                : metric==="yield_signals" ? "#5A8EAF" : "#C9A84C";
    const byday = new Map(YIELD.map(yy => [+day.floor(new Date(yy.date)), yy[field]||0]));
    const vals = days.map(d => ({date:d, v: byday.has(+d) ? byday.get(+d) : null}));
    const yMax = d3.max(vals, d => d.v||0) || 1;
    const y = d3.scaleLinear().domain([0, yMax]).nice().range([innerH,0]);
    const bw = Math.max(2, innerW/days.length*0.7);
    g.selectAll(".ybar").data(vals.filter(d => d.v!=null)).join("rect").attr("class","ybar")
      .attr("x", d => x(d.date)-bw/2).attr("y", d => y(d.v)).attr("width", bw)
      .attr("height", d => innerH-y(d.v)).attr("fill",yColor).attr("fill-opacity",0.72);
    axes(g, x, y, innerH, ylabel);
    if (metric==="yield_signals") {
      lg.innerHTML = `<span><i class="dot" style="background:${yColor}"></i>`
        + `${yUnit} per day (Interactions L2 stream)`
        + `</span><span style="margin-left:14px">a bar = a day with signals · gaps = no cross-tradition signal that day</span>`;
    } else {
      lg.innerHTML = `<span><i class="dot" style="background:${yColor}"></i>`
        + `${yUnit} added per commit-day (vault git)`
        + `</span><span style="margin-left:14px">a bar = a commit day · gaps = no vault commit (not zero)</span>`;
    }
  } else if (logy) {
    const rows = days.map(d => ({date:d, v:0}));
    lanes.forEach(L => L.rows.forEach(r => { const i=idx.get(+day.floor(new Date(r.t))); if(i!=null) rows[i].v += (+r[metric]||0); }));
    const yMax = d3.max(rows, d=>d.v) || 1;
    const y = d3.scaleLog().domain([1, Math.max(2,yMax)]).range([innerH,0]).clamp(true);
    const area = d3.area().x(d=>x(d.date)).y0(y(1)).y1(d=>y(Math.max(1,d.v))).curve(d3.curveMonotoneX);
    g.append("path").datum(rows).attr("d", area).attr("fill","#5A8EAF").attr("fill-opacity",0.45)
      .attr("stroke","#5A8EAF").attr("stroke-width",1.3);
    axes(g, x, y, innerH, ylabel);
    lg.innerHTML = `<span><i class="dot" style="background:#5A8EAF"></i>system total (${METRIC_LABEL[metric]||metric})</span>`
      + `<span style="margin-left:14px">faint bands = weekends</span>`;
  } else {
    const cats = [...new Set(lanes.map(L => L.category))];
    const rows = days.map(d => { const o={date:d}; cats.forEach(c=>o[c]=0); return o; });
    lanes.forEach(L => L.rows.forEach(r => { const i=idx.get(+day.floor(new Date(r.t))); if(i!=null) rows[i][L.category] += (+r[metric]||0); }));
    const series = d3.stack().keys(cats)(rows);
    const yMax = d3.max(rows, d => cats.reduce((s,c)=>s+d[c],0)) || 1;
    const y = d3.scaleLinear().domain([0,yMax]).nice().range([innerH,0]);
    const area = d3.area().x(d=>x(d.data.date)).y0(d=>y(d[0])).y1(d=>y(d[1])).curve(d3.curveMonotoneX);
    g.selectAll(".layer").data(series).join("path").attr("class","layer")
      .attr("d", area).attr("fill", s=>catColor(s.key)).attr("fill-opacity",0.78)
      .attr("stroke", s=>catColor(s.key)).attr("stroke-width",0.4);
    axes(g, x, y, innerH, ylabel + " (stacked by category)");
    lg.innerHTML = cats.map(c=>`<span><i class="dot" style="background:${catColor(c)}"></i>${c}</span>`).join("")
      + `<span style="margin-left:14px">faint bands = weekends</span>`;
  }
  // (Former "interactive capture ends" horizon removed 2026-06-17: it marked
  // the 2026-04-06 schema-migration gap, which the token-path fix now closes.)
}

function renderDual() {
  const logy = document.getElementById("logy").checked;
  const {g, innerW, innerH} = frame();
  const {day, t0, t1, days, idx} = dayAxis();
  const rows = days.map(d => ({date:d, sent:0, returned:0}));
  lanes.forEach(L => L.rows.forEach(r => { const i=idx.get(+day.floor(new Date(r.t)));
    if(i!=null){ rows[i].sent += (+r.in||0)+(+r.cache_read||0); rows[i].returned += (+r.out||0); }}));
  const x = d3.scaleTime().domain([t0,t1]).range([0,innerW]);
  weekendBands(g, days, x, innerW, innerH);
  const yMax = d3.max(rows, d=>Math.max(d.sent,d.returned)) || 1;
  const y = logy ? d3.scaleLog().domain([1,Math.max(2,yMax)]).range([innerH,0]).clamp(true)
                 : d3.scaleLinear().domain([0,yMax]).nice().range([innerH,0]);
  const base = logy ? 1 : 0;
  const mk = key => d3.line().x(d=>x(d.date)).y(d=>y(Math.max(base,d[key]))).curve(d3.curveMonotoneX);
  const series = [["sent","#A85D3A","tokens sent (input + cache-read)"],
                  ["returned","#4E8A5E","tokens returned (output)"]];
  series.forEach(([k,c]) => g.append("path").datum(rows).attr("fill","none")
    .attr("stroke",c).attr("stroke-width",1.6).attr("d", mk(k)));
  axes(g, x, y, innerH, "tokens / day" + (logy?" (log)":""));
  document.getElementById("legend").innerHTML = series.map(([k,c,l])=>
    `<span><i class="dot" style="background:${c}"></i>${l}</span>`).join("")
    + `<span style="margin-left:14px">faint bands = weekends</span>`;
}

function setControls(view) {
  document.getElementById("color").parentElement.style.display = (view==="raster") ? "" : "none";
  document.getElementById("logwrap").style.display = (view==="raster") ? "none" : "";
  const sel = document.getElementById("metric");
  sel.parentElement.style.display = (view==="dual") ? "none" : "";
  [...sel.options].forEach(o => { if (o.value.startsWith("yield")) o.disabled = (view!=="wave"); });
  if (view!=="wave" && sel.value.startsWith("yield")) sel.value = "events";
  // Log Y is inert for yield metrics — their commit-day bars use a fixed linear scale.
  // Grey out + disable the checkbox when it can't change anything (wave view + a yield metric).
  const logyChk = document.getElementById("logy");
  const logyInert = (view==="wave" && sel.value.startsWith("yield"));
  logyChk.disabled = logyInert;
  logyChk.title = logyInert ? "Log scale doesn't apply to per-commit-day yield bars" : "";
  document.getElementById("logwrap").style.opacity = logyInert ? "0.4" : "";
}

function render() {
  const view = document.getElementById("view").value;
  setControls(view);
  if (view==="wave") renderWave();
  else if (view==="dual") renderDual();
  else renderRaster();
}
["view","metric","color","logy"].forEach(id =>
  document.getElementById(id).addEventListener("change", render));
window.addEventListener("resize", render);
render();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()

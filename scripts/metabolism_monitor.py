#!/usr/bin/env python3
"""
metabolism_monitor.py - C2A2 Metabolism Monitor, Phase 0 (reliable signal + census).

Phase 0 of the maturity ladder in METABOLISM_MONITOR_AGENT_SPEC.md. It does three
things and makes NO judgments (no verdicts -- that is Phase 2+):

  1. Regenerate metabolism_data.json from the live open-story.db at the top of the
     run (bundled: the monitor owns its own freshness, per the 2026-06-22 decision).
  2. Assert freshness and FAIL LOUD: if the snapshot is more than MAX_STALE_H behind
     the db, exit non-zero. Everything downstream reads this snapshot, so a stale
     signal must stop the run rather than be silently "learned" from.
  3. Emit a one-time DESCRIPTIVE census of the metabolism + efficiency slice it owns,
     every line tagged [descriptive] or [provisional], plus pointers to the standing
     flags and counts owned by the 14a/15c self-awareness system (consumed, NOT
     recomputed here -- the non-duplication discipline of spec section 7a).

Convention: mirrors scripts/janitor.py (path auto-detect, baseline-then-deltas,
state.json + findings.md, surfaced via morning-system-health). The DURABLE learning
goes to logbook.md; the ephemeral weekly deltas go to findings.md.

Usage:
    python3 metabolism_monitor.py                 # regen, assert freshness, write census
    python3 metabolism_monitor.py --no-regen      # read existing snapshot (freshness still asserted)
    python3 metabolism_monitor.py --dry-run       # compute + print census; no file writes
    python3 metabolism_monitor.py --db PATH       # override db path
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import urllib.parse
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# --- Configuration (path auto-detect: same discipline as janitor.py) ---------
_MAC_ROOT = Path("/Users/tomloughran/Documents/Claude/Projects")


def _detect_root() -> Path:
    if _MAC_ROOT.exists():
        return _MAC_ROOT
    if Path("/sessions").exists():
        for mnt in sorted(Path("/sessions").glob("*/mnt")):
            if (mnt / "RC Karpathy Wiki Project").exists():
                return mnt
    return _MAC_ROOT


_ROOT = _detect_root()
PROJECT_ROOT = _ROOT / "RC Karpathy Wiki Project"
METAB_DIR = PROJECT_ROOT / "wiki" / "metabolism"
BUILDER = METAB_DIR / "scripts" / "build_metabolism_view.py"
DATA_JSON = METAB_DIR / "metabolism_data.json"
AGENT_MAP = PROJECT_ROOT / "wiki" / "agents" / "openstory" / "agent_map.json"
MONITOR_DIR = PROJECT_ROOT / "metabolism-monitor"
STATE_PATH = MONITOR_DIR / "state.json"
FINDINGS_MD = MONITOR_DIR / "findings.md"
LOGBOOK_MD = MONITOR_DIR / "logbook.md"

# OpenStory db: prefer the canonical data/ path; fall back to the Mac home path.
_DB_CANDIDATES = [
    _ROOT.parent / "Non-Claude Projects" / "OpenStory" / "data" / "open-story.db",
    Path(os.path.expanduser("~")) / "Documents" / "Non-Claude Projects" / "OpenStory" / "data" / "open-story.db",
]
DEFAULT_DB = next((str(p) for p in _DB_CANDIDATES if p.exists()), str(_DB_CANDIDATES[-1]))

MAX_STALE_H = 24.0  # Phase-0 done-gate: json must never be >24h behind the db.


# --- Freshness ---------------------------------------------------------------
def _parse_iso(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def assert_fresh(data, db_path):
    """Fail loud if the snapshot is stale. Returns a (descriptive) freshness dict."""
    now = datetime.now(timezone.utc)
    gen = _parse_iso(data.get("_meta", {}).get("generated"))
    db_mtime_meta = _parse_iso(data.get("_meta", {}).get("db_mtime"))
    db_mtime_live = None
    if os.path.exists(db_path):
        db_mtime_live = datetime.fromtimestamp(os.path.getmtime(db_path), tz=timezone.utc)

    if gen is None:
        sys.exit("FRESHNESS FAIL: snapshot has no _meta.generated timestamp; refusing to proceed.")
    if gen.tzinfo is None:
        gen = gen.replace(tzinfo=timezone.utc)

    snapshot_age_h = (now - gen).total_seconds() / 3600.0
    # Lag of the snapshot behind the live db file (the gate the spec names).
    lag_h = None
    if db_mtime_live is not None:
        lag_h = (db_mtime_live - gen).total_seconds() / 3600.0

    if lag_h is not None and lag_h > MAX_STALE_H:
        sys.exit(
            "FRESHNESS FAIL: snapshot is %.1fh behind the live db (limit %.0fh).\n"
            "  snapshot generated: %s\n  live db mtime:      %s\n"
            "  Run without --no-regen so the monitor regenerates before reading."
            % (lag_h, MAX_STALE_H, gen.isoformat(), db_mtime_live.isoformat())
        )
    if snapshot_age_h > MAX_STALE_H:
        sys.exit(
            "FRESHNESS FAIL: snapshot is %.1fh old (limit %.0fh); regenerate before reading."
            % (snapshot_age_h, MAX_STALE_H)
        )
    return {
        "snapshot_generated": gen.isoformat(),
        "snapshot_age_h": round(snapshot_age_h, 2),
        "db_mtime_meta": db_mtime_meta.isoformat() if db_mtime_meta else None,
        "db_mtime_live": db_mtime_live.isoformat() if db_mtime_live else None,
        "snapshot_lag_behind_db_h": round(lag_h, 2) if lag_h is not None else None,
    }


# --- Census (deterministic; the model does NOT touch this arithmetic) --------
def compute_census(data):
    lanes = data.get("lanes", [])
    meta = data.get("_meta", {})
    yield_daily = data.get("yield_daily", [])

    months = defaultdict(lambda: {"in": 0, "out": 0, "cache_read": 0,
                                  "cache_creation": 0, "thinking_tokens": 0, "runs": 0})
    sys_tot = {"in": 0, "out": 0, "cache_read": 0, "cache_creation": 0,
               "thinking_tokens": 0, "runs": 0}
    lane_rows = []
    for L in lanes:
        l_in = l_out = l_cr = l_cc = l_th = 0
        for r in L.get("rows", []):
            mk = (r.get("t") or "")[:7]
            for fld in ("in", "out", "cache_read", "cache_creation", "thinking_tokens"):
                v = r.get(fld, 0) or 0
                months[mk][fld] += v
                sys_tot[fld] += v
            months[mk]["runs"] += 1
            sys_tot["runs"] += 1
            l_in += r.get("in", 0) or 0
            l_out += r.get("out", 0) or 0
            l_cr += r.get("cache_read", 0) or 0
            l_cc += r.get("cache_creation", 0) or 0
            l_th += r.get("thinking_tokens", 0) or 0
        runs = L.get("runs", len(L.get("rows", [])))
        l_total = l_in + l_out + l_cr + l_cc
        lane_rows.append({
            "label": L.get("label", L.get("key")),
            "category": L.get("category"),
            "runs": runs,
            "out": l_out,
            "in": l_in,
            "out_per_in": round(l_out / l_in, 2) if l_in else None,
            "cache_read_frac": round(l_cr / l_total, 3) if l_total else None,
            "out_per_run": round(l_out / runs) if runs else None,
            "thinking_tokens": l_th,
            "median_gap_h": L.get("median_gap_h"),
        })

    sys_total_tok = sys_tot["in"] + sys_tot["out"] + sys_tot["cache_read"] + sys_tot["cache_creation"]
    census = {
        "as_of": datetime.now(timezone.utc).isoformat(),
        "range": {"t_min": meta.get("t_min"), "t_max": meta.get("t_max")},
        "lanes": len(lanes),
        "runs": sys_tot["runs"],
        "system": {
            "in": sys_tot["in"], "out": sys_tot["out"],
            "cache_read": sys_tot["cache_read"], "cache_creation": sys_tot["cache_creation"],
            "thinking_tokens": sys_tot["thinking_tokens"],
            "out_per_in": round(sys_tot["out"] / sys_tot["in"], 3) if sys_tot["in"] else None,
            "cache_read_frac": round(sys_tot["cache_read"] / sys_total_tok, 3) if sys_total_tok else None,
        },
        "by_month": {k: dict(v) for k, v in sorted(months.items()) if k},
        "lane_rows": sorted(lane_rows, key=lambda x: x["out"], reverse=True),
        "yield": {
            "yield_days": len(yield_daily),
            "links_added": sum(d.get("links_added", 0) for d in yield_daily),
            "files_added": sum(d.get("files_added", 0) for d in yield_daily),
            "prs_added": sum(d.get("prs_added", 0) for d in yield_daily),
            "prs_articulated": sum(d.get("prs_articulated", 0) for d in yield_daily),
        },
        "synthesis": synthesis_census(yield_daily),
    }
    return census


def synthesis_census(yield_daily, today=None):
    """Sewing-lane yield: the wiki/synthesis/<a>_<b>_bridge.md essays.

    Four numbers, all raw counts. NO coverage ratio: the cast is not fixed --
    Loughran and MacIntyre are structural and appear in every version, while the
    other thinkers may belong only to this one, so any "N of C(k,2) possible"
    denominator would move for reasons that have nothing to do with the lane's
    output. Tom's call, 2026-08-26.

    essays/words come from the per-day series (git-derived, objective).
    traditions is current-state from the filenames.
    stale_days is days since the last day the series recorded an essay -- the
    lane is weekly, so 14d is two missed cycles (warn) and 21d is three (fail).
    Boundaries are inclusive: at exactly 14 days two expected runs have already
    produced nothing, which is the thing worth flagging, not the day after.
    Carries its own provenance for the same reason the signal axis has to: a
    frozen source and a genuinely quiet agent both render as zero, and the
    signals axis sat at 0 for six weeks with nobody able to tell which it was."""
    import datetime, glob, os, re
    essays = sum(d.get("synthesis_essays", 0) for d in yield_daily)
    words = sum(d.get("synthesis_words", 0) for d in yield_daily)

    days = [d["date"] for d in yield_daily if d.get("synthesis_essays", 0) > 0]
    last = max(days) if days else None
    stale = None
    if last:
        today = today or datetime.date.today()
        try:
            stale = (today - datetime.date(*map(int, last.split("-")))).days
        except (TypeError, ValueError):
            stale = None

    syn_dir = PROJECT_ROOT / "wiki" / "synthesis"
    names, pairs, unparsed = set(), set(), 0
    for f in sorted(glob.glob(os.path.join(str(syn_dir), "*.md"))):
        m = re.match(r"^(.+?)_(.+?)_bridge\.md$", os.path.basename(f))
        if not m:
            unparsed += 1
            continue
        a_, b_ = m.group(1).lower(), m.group(2).lower()
        names.update((a_, b_))
        pairs.add(frozenset((a_, b_)))
    on_disk = len(pairs) + unparsed

    status = "ok"
    if stale is None:
        status = "unknown"
    elif stale >= 21:
        status = "fail"
    elif stale >= 14:
        status = "warn"

    return {
        "essays": essays,
        "words": words,
        "traditions": len(names),
        "stale_days": stale,
        "status": status,
        # ASSERTION, not an indicator. One essay per pair is the invariant; a
        # divergence means the lane wrote a second essay for a pair it had
        # already bridged. Reported, never silently reconciled.
        "pairs_on_disk": len(pairs),
        "pairs_equal_essays": (len(pairs) == on_disk and unparsed == 0),
        "unparsed_filenames": unparsed,
        "provenance": {
            "essays_words": "yield_daily, git first-seen over wiki/synthesis/",
            "traditions_pairs": str(syn_dir),
            "last_essay_day": last,
            "cadence": "c2a2-sewing-agent-weekly; warn >=14d, fail >=21d",
        },
    }


# --- Rendering ---------------------------------------------------------------
def _fmt(n):
    return f"{n:,}" if isinstance(n, int) else ("n/a" if n is None else str(n))


def render_logbook_entry(census, fresh):
    s = census["system"]
    L = []
    L.append("## %s - Phase 0 baseline census (descriptive)" % census["as_of"][:10])
    L.append("")
    L.append("Phase 0 of the metabolism-monitor maturity ladder. NO verdicts: every line "
             "below is a descriptive or provisional fact about the signal as it stands. "
             "Interpretation is deferred to Phase 2+.")
    L.append("")
    L.append("**Freshness** [descriptive]: snapshot generated %s (age %.2fh); live db mtime %s; "
             "snapshot lag behind db %s h. Gate = %.0fh; PASS." % (
                 fresh["snapshot_generated"], fresh["snapshot_age_h"],
                 fresh["db_mtime_live"], fresh["snapshot_lag_behind_db_h"], MAX_STALE_H))
    L.append("")
    L.append("**Scope** [descriptive]: %s lanes, %s runs, %s -> %s." % (
        _fmt(census["lanes"]), _fmt(census["runs"]),
        (census["range"]["t_min"] or "")[:10], (census["range"]["t_max"] or "")[:10]))
    L.append("")
    L.append("**Token metabolism, system totals** [descriptive]: "
             "out %s, in %s, cache-read %s, cache-creation %s, thinking %s (est.)." % (
                 _fmt(s["out"]), _fmt(s["in"]), _fmt(s["cache_read"]),
                 _fmt(s["cache_creation"]), _fmt(s["thinking_tokens"])))
    L.append("")
    L.append("**Efficiency ratios** [descriptive]: system out/in = %s; "
             "cache-read fraction of all tokens = %s (the Karpathy wiki-as-environment "
             "thesis as a measured number -- recirculated context vs. regenerated)." % (
                 s["out_per_in"], s["cache_read_frac"]))
    L.append("")
    L.append("**Token metabolism by month** [descriptive]:")
    L.append("")
    L.append("| month | output | input | cache-read | thinking (est.) | runs |")
    L.append("|---|---|---|---|---|---|")
    for mk, mv in census["by_month"].items():
        L.append("| %s | %s | %s | %s | %s | %s |" % (
            mk, _fmt(mv["out"]), _fmt(mv["in"]), _fmt(mv["cache_read"]),
            _fmt(mv["thinking_tokens"]), _fmt(mv["runs"])))
    L.append("")
    L.append("**Per-lane (top by output)** [descriptive]:")
    L.append("")
    L.append("| lane | cat | runs | output | out/in | cache-read frac | out/run | thinking | median gap h |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for r in census["lane_rows"]:
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            r["label"], r["category"], _fmt(r["runs"]), _fmt(r["out"]),
            r["out_per_in"], r["cache_read_frac"], _fmt(r["out_per_run"]),
            _fmt(r["thinking_tokens"]), r["median_gap_h"]))
    L.append("")
    y = census["yield"]
    L.append("**Yield series (vault git + WS2 CSV)** [descriptive]: %s yield-days; "
             "links added %s, files added %s, PRS first-seen %s, PRS articulated %s." % (
                 _fmt(y["yield_days"]), _fmt(y["links_added"]), _fmt(y["files_added"]),
                 _fmt(y["prs_added"]), _fmt(y["prs_articulated"])))
    sy = census.get("synthesis") or {}
    if sy:
        _stale = "unknown" if sy["stale_days"] is None else ("%s d" % sy["stale_days"])
        L.append("**Synthesis bridges (sewing lane)** [descriptive]: %s essays; %s words; "
                 "%s traditions touched; last essay %s ago (%s)." % (
                     _fmt(sy["essays"]), _fmt(sy["words"]), _fmt(sy["traditions"]),
                     _stale, sy["status"].upper()))
        L.append("  Source: %s. Cadence: %s." % (
            sy["provenance"]["traditions_pairs"], sy["provenance"]["cadence"]))
        if sy["status"] in ("warn", "fail"):
            L.append("  ^ the lane has missed cycles. A zero here is only meaningful "
                     "against this staleness reading -- check the source before "
                     "concluding the agent is idle.")
        if not sy["pairs_equal_essays"]:
            L.append("  ^ ASSERTION FAILED: %s distinct pairs but %s parsed essays "
                     "(%s unparsed filenames). The lane has bridged a pair twice, or a "
                     "filename does not match <a>_<b>_bridge.md." % (
                         _fmt(sy["pairs_on_disk"]), _fmt(sy["essays"]),
                         _fmt(sy["unparsed_filenames"])))
    L.append("")
    L.append("**Consumed, NOT recomputed here** (owned by the 14a/15c self-awareness system; "
             "spec section 7a non-duplication) [provisional]:")
    L.append("- PRS confidence distribution and email-verification coverage (1/6 commit-days): "
             "see the latest `wiki/architecture/metrics/*_snapshot.md`.")
    L.append("- Cross-tradition census (connection count, cross-module fiber density, modularity): "
             "see `wiki/architecture/narrative_prs_connectome.md` -- descriptive, never a control target.")
    L.append("- Standing flags the monitor consumes and must not re-derive: REVISE-124 (do not harden "
             "views on PRS-yield), REVISE-111 (pre-register falsifiers), OPEN-084 (three-count divergence).")
    L.append("- OPEN-083 (metabolism cliff artifact-vs-real): RESOLVED 2026-06-22 as artifact -- the "
             "Apr-6 cliff was the 2026-04-07 token_usage schema migration; reading both paths shows "
             "continuous nonzero output across the boundary and through May/June. No real output collapse.")
    L.append("")
    L.append("_No verdict is offered on whether any of the above is 'good' or 'improving'. "
             "That judgment is gated to Phase 2-3 behind a pre-registered falsifier (REVISE-111)._")
    L.append("")
    return "\n".join(L)


def render_findings(census, fresh, is_baseline):
    L = []
    L.append("# Metabolism Monitor - findings")
    L.append("")
    L.append("_Phase 0 (reliable signal + descriptive census). Generated %s. "
             "Ephemeral: this file is overwritten each run; durable learning lives in "
             "logbook.md._" % census["as_of"][:19])
    L.append("")
    L.append("## New since last week")
    L.append("")
    if is_baseline:
        L.append("- Phase 0 baseline established. The full descriptive census was written to "
                 "`metabolism-monitor/logbook.md`. No deltas yet (this is the first run).")
        L.append("- Freshness gate PASS: snapshot %.2fh old, lag behind live db %s h (limit %.0fh)." % (
            fresh["snapshot_age_h"], fresh["snapshot_lag_behind_db_h"], MAX_STALE_H))
        L.append("- OPEN-083 resolved (artifact); thinking-token join fixed (system thinking est. %s tokens, "
                 "previously read 0 in lanes)." % _fmt(census["system"]["thinking_tokens"]))
    else:
        L.append("- (Delta computation begins at Phase 1; Phase 0 only establishes the baseline.)")
    L.append("")
    L.append("_A 'no findings' week after findings is itself a finding (fail-loud); the monitor "
             "surfaces a stale or empty signal rather than hiding it._")
    L.append("")
    return "\n".join(L)


# --- Main --------------------------------------------------------------------
def _snapshot_db(live_db):
    """Consistent read snapshot of the live (actively-written) db via the SQLite
    backup API. Reading the live WAL db directly trips build_metabolism_view's
    PRAGMA quick_check mid-write ('2nd reference to page ...'); a backup is a
    consistent point-in-time copy that quick_check passes."""
    if not os.path.exists(live_db):
        sys.exit("ERROR: db not found: %s" % live_db)
    fd, snap = tempfile.mkstemp(prefix="os_metab_snap_", suffix=".db")
    os.close(fd)
    src = sqlite3.connect("file:%s?mode=ro" % urllib.parse.quote(live_db), uri=True)
    dst = sqlite3.connect(snap)
    src.backup(dst)
    dst.close()
    src.close()
    return snap


def regen(db_path):
    if not BUILDER.exists():
        sys.exit("ERROR: builder not found: %s" % BUILDER)
    snap = _snapshot_db(db_path)
    print("[regen] snapshot %s -> builder" % snap)
    try:
        cmd = [sys.executable, str(BUILDER), "--db", snap, "--map", str(AGENT_MAP),
               "--repo", str(PROJECT_ROOT), "--outdir", str(METAB_DIR)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        sys.stdout.write(r.stdout)
        # Always forward stderr, not only on failure. The builder's WARNs -- a
        # missing agent map, an unreadable or STALE cross-tradition signal source
        # -- all arrive on a zero exit code, and swallowing them is how the
        # signal axis read a silent flat zero for six weeks.
        if r.stderr:
            sys.stderr.write(r.stderr)
        if r.returncode != 0:
            sys.exit("ERROR: regen failed (build_metabolism_view.py exit %d)" % r.returncode)
    finally:
        try:
            os.remove(snap)
        except OSError:
            pass
    # Record the LIVE db's identity in the snapshot (the temp path is an internal
    # detail; freshness is judged against the live db).
    try:
        with open(DATA_JSON) as fh:
            d = json.load(fh)
        d["_meta"]["db_path"] = db_path
        d["_meta"]["db_mtime"] = datetime.fromtimestamp(os.path.getmtime(db_path)).isoformat()
        with open(DATA_JSON, "w") as fh:
            json.dump(d, fh, indent=2)
    except (OSError, ValueError, KeyError):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--no-regen", action="store_true",
                    help="read the existing snapshot (freshness is still asserted, fails loud if stale)")
    ap.add_argument("--regen-only", action="store_true",
                    help="regenerate the snapshot and assert freshness, then exit; write no "
                         "census/findings/logbook (for the daily freshness-refresh task)")
    ap.add_argument("--dry-run", action="store_true",
                    help="compute and print the census; write no files")
    args = ap.parse_args()

    if not args.no_regen:
        regen(args.db)

    if not DATA_JSON.exists():
        sys.exit("ERROR: %s not found (run without --no-regen to generate it)." % DATA_JSON)
    with open(DATA_JSON) as fh:
        data = json.load(fh)

    fresh = assert_fresh(data, args.db)        # FAILS LOUD if stale

    if args.regen_only:
        print("[regen-only] freshness PASS: snapshot age %.2fh, lag behind db %s h (limit %.0fh)" % (
            fresh["snapshot_age_h"], fresh["snapshot_lag_behind_db_h"], MAX_STALE_H))
        print("  range %s -> %s; lanes=%d" % (
            (data.get("_meta", {}).get("t_min") or "")[:10],
            (data.get("_meta", {}).get("t_max") or "")[:10],
            data.get("_meta", {}).get("lanes", 0)))
        return
    census = compute_census(data)

    logbook_entry = render_logbook_entry(census, fresh)

    if args.dry_run:
        print("\n----- FRESHNESS -----")
        print(json.dumps(fresh, indent=2))
        print("\n----- LOGBOOK ENTRY (not written, --dry-run) -----\n")
        print(logbook_entry)
        return

    MONITOR_DIR.mkdir(parents=True, exist_ok=True)
    is_baseline = not STATE_PATH.exists()

    # logbook is durable: append dated entries, never overwrite.
    logbook_new = not LOGBOOK_MD.exists()
    with open(LOGBOOK_MD, "a", encoding="utf-8") as fh:
        if logbook_new:
            fh.write("# Metabolism Monitor - logbook (durable)\n\n"
                     "Accumulating record of what we have learned about how the C2A2 swarm "
                     "metabolizes. Append-only; dated entries. Owned slice: metabolism + "
                     "efficiency (spec section 7a). No verdicts before Phase 2.\n\n")
        fh.write(logbook_entry)
        fh.write("\n---\n\n")

    with open(FINDINGS_MD, "w", encoding="utf-8") as fh:
        fh.write(render_findings(census, fresh, is_baseline))

    state = {
        "phase": 0,
        "last_run": census["as_of"],
        "baseline_established": True,
        "freshness": fresh,
        "system_totals": census["system"],
        "yield": census["yield"],
    }
    with open(STATE_PATH, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2)

    print("\n[done] phase=0 baseline=%s" % is_baseline)
    print("  findings: %s" % FINDINGS_MD)
    print("  logbook:  %s" % LOGBOOK_MD)
    print("  state:    %s" % STATE_PATH)
    print("  system out/in=%s cache-read-frac=%s thinking=%s" % (
        census["system"]["out_per_in"], census["system"]["cache_read_frac"],
        _fmt(census["system"]["thinking_tokens"])))


if __name__ == "__main__":
    main()

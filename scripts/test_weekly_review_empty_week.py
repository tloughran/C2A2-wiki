#!/usr/bin/env python3
"""Tests for generate_weekly_review.py's handling of a week with no completed days.
Plain asserts, no pytest dependency.

    python3 scripts/test_weekly_review_empty_week.py

WHY (Rule 9): for ten weeks the generator answered an empty week by reprinting the
last five completed days under the new week's label. W32-W35 all shipped days
286-307 and 42,781 words. Nothing failed, nothing was red, and the only way to see
it was to diff two reviews by hand. The intent encoded here is not "handle the
empty case" but "an empty week must never yield a file that looks like a fresh
review", and the two empty causes must be told apart:

    series over          -> exit 0, say so, write NOTHING
    days missing, series open -> exit 3, write NOTHING

The falsifier runs both directions: it fails if a refusal stops happening AND it
fails if a real week stops producing a review.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "gwr", os.path.join(HERE, "generate_weekly_review.py"))
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)

SCRIPT = os.path.join(HERE, "generate_weekly_review.py")
REPO = os.path.dirname(HERE)
FAILURES = []


def check(label, cond, detail=""):
    if cond:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label}  {detail}")
        FAILURES.append(label)


# ── Fixture vault ─────────────────────────────────────────────────────────────

HEADER = (
    "| Date | Day | Range | Cum | Pars | Mode | Status |\n"
    "|---|---|---|---|---|---|---|\n"
)
ROW = "| {date} | {dow} | {a}–{b} | {b} | Prima Pars (I) | agent batch | {status} |\n"


def make_vault(rows):
    """rows: list of (isodate, day_start, day_end, status_cell)."""
    d = tempfile.mkdtemp(prefix="wr_vault_")
    for sub in ("_index", "transcripts", "synthesis"):
        os.makedirs(os.path.join(d, sub))
    body = HEADER + "".join(
        ROW.format(date=r[0], dow="Mon", a=r[1], b=r[2], status=r[3]) for r in rows)
    with open(os.path.join(d, "_index", "Pace tracker.md"), "w", encoding="utf-8") as f:
        f.write("# Pace tracker\n\n" + body)
    with open(os.path.join(d, "_index", "QC log.md"), "w", encoding="utf-8") as f:
        f.write("| ts | day |\n|---|---|\n")
    return d


def run(vault, week, wiki_dir):
    return subprocess.run(
        [sys.executable, SCRIPT, "--week", week,
         "--summa-vault", vault, "--wiki-dir", wiki_dir],
        capture_output=True, text=True)


def reviews_in(wiki_dir):
    rd = os.path.join(wiki_dir, "review")
    return sorted(os.listdir(rd)) if os.path.isdir(rd) else []


# ── Unit: series_finale_row ───────────────────────────────────────────────────

def test_finale_detection():
    print("series_finale_row()")
    import datetime as dt
    rows = G.read_pace_tracker(make_vault([
        ("2026-06-22", 286, 290, "✅"),
        ("2026-06-26", 306, 307, "✅ SERIES COMPLETE — Day 307 is the finale"),
    ]))
    check("parses both rows", len(rows) == 2, f"got {len(rows)}")
    check("keeps the status cell",
          any("SERIES COMPLETE" in r["status"] for r in rows))
    check("finds the finale for a later week",
          (G.series_finale_row(rows, dt.date(2026, 8, 24)) or {}).get("day_end") == 307)
    check("no finale for a week before it",
          G.series_finale_row(rows, dt.date(2026, 6, 22)) is None)
    check("no finale when the marker is absent",
          G.series_finale_row(G.read_pace_tracker(make_vault([
              ("2026-06-22", 286, 290, "✅")])), dt.date(2026, 8, 24)) is None)
    check("an unfinished row cannot be the finale",
          G.series_finale_row(G.read_pace_tracker(make_vault([
              ("2026-06-26", 306, 307, "SERIES COMPLETE (planned)")])),
              dt.date(2026, 8, 24)) is None)


# ── End-to-end: the three outcomes ────────────────────────────────────────────

FULL = [
    ("2026-06-22", 286, 290, "✅"),
    ("2026-06-26", 306, 307, "✅ SERIES COMPLETE — Day 307 is the finale"),
]
OPEN_SERIES = [("2026-06-22", 286, 290, "✅")]


def test_live_week_still_works():
    """The other direction: a week that HAS days must still produce a review."""
    print("a week with completed days")
    vault = make_vault(FULL)
    wiki = tempfile.mkdtemp(prefix="wr_wiki_")
    r = run(vault, "2026-W26", wiki)          # 2026-06-22 .. 2026-06-28
    check("exit 0", r.returncode == 0, r.stderr.strip()[:200])
    check("writes exactly one review", reviews_in(wiki) == ["2026-W26_weekly_review.html"],
          str(reviews_in(wiki)))


def test_after_finale_is_quiet_and_writes_nothing():
    print("an empty week AFTER the series finale")
    vault = make_vault(FULL)
    wiki = tempfile.mkdtemp(prefix="wr_wiki_")
    r = run(vault, "2026-W35", wiki)
    check("exit 0 (not a failure)", r.returncode == 0, f"rc={r.returncode}")
    check("names the finale day", "Day 307" in r.stdout, r.stdout.strip()[:200])
    check("writes NO file", reviews_in(wiki) == [], str(reviews_in(wiki)))

    # The regression itself: two different empty weeks used to yield two files with
    # identical content. Now they yield none.
    r2 = run(vault, "2026-W34", wiki)
    check("a second empty week also writes nothing",
          r2.returncode == 0 and reviews_in(wiki) == [], str(reviews_in(wiki)))


def test_missing_days_without_finale_fails_loud():
    print("an empty week while the series is still OPEN")
    vault = make_vault(OPEN_SERIES)
    wiki = tempfile.mkdtemp(prefix="wr_wiki_")
    r = run(vault, "2026-W35", wiki)
    check("exit 3", r.returncode == 3, f"rc={r.returncode} {r.stderr.strip()[:200]}")
    check("says why on stderr", "no completed days" in r.stderr, r.stderr.strip()[:200])
    check("writes NO file", reviews_in(wiki) == [], str(reviews_in(wiki)))


def test_silent_fallback_is_gone():
    print("the old fallback")
    src = open(os.path.join(HERE, "generate_weekly_review.py"), encoding="utf-8").read()
    check("no 'last 5 completed days' reprint path",
          "Including last 5 completed days" not in src)


# ── Integration: the real vault, pinned ───────────────────────────────────────

def test_real_vault_current_week():
    """Pins the live state: the Summa series ended 2026-06-26 at Day 307, so the
    current week is an after-finale week. If a new series starts, this test fails
    and forces a conscious update rather than silently passing."""
    print("the real Summa vault, current week")
    vault = os.path.expanduser(
        "~/Documents/Claude/Projects/Summa 2026 in a Year/vault")
    if not os.path.isdir(vault):
        print("  skip (vault not present on this machine)")
        return
    wiki = tempfile.mkdtemp(prefix="wr_wiki_")
    r = subprocess.run(   # no --week: defaults to the current ISO week
        [sys.executable, SCRIPT, "--summa-vault", vault, "--wiki-dir", wiki],
        capture_output=True, text=True)
    check("exit 0", r.returncode == 0, f"rc={r.returncode} {r.stderr.strip()[:200]}")
    check("reports the series finished at Day 307",
          "Day 307" in r.stdout, r.stdout.strip()[:200])
    check("writes NO file into wiki/review", reviews_in(wiki) == [],
          str(reviews_in(wiki)))


if __name__ == "__main__":
    test_finale_detection()
    test_live_week_still_works()
    test_after_finale_is_quiet_and_writes_nothing()
    test_missing_days_without_finale_fails_loud()
    test_silent_fallback_is_gone()
    test_real_vault_current_week()
    print()
    if FAILURES:
        print(f"FAILED ({len(FAILURES)}): " + ", ".join(FAILURES))
        sys.exit(1)
    print("all checks passed")

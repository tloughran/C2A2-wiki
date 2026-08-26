"""Tests for the sewing-lane yield rows in metabolism_monitor.synthesis_census.

WHY these assertions and not the obvious ones: the obvious test is
"essays == 66, traditions == 14". That test is wrong. Those are facts about
the corpus on one day, and the corpus is supposed to grow -- a test that goes
red when the sewing agent does its job is worse than no test. What must hold
regardless of size is asserted here; what is merely true today is PRINTED so a
reader sees drift without the suite crying wolf.

Run: python3 scripts/test_synthesis_yield.py
"""
import datetime
import glob
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import metabolism_monitor as M  # noqa: E402

SYN = os.path.join(REPO, "wiki", "synthesis")


def test_git_extraction_matches_disk():
    """The per-day series counts an essay on the day git first saw it. However
    many essays exist, the series must account for exactly the files on disk --
    this is what catches a path-prefix or name-status parsing regression."""
    on_disk = len(glob.glob(os.path.join(SYN, "*.md")))
    shas = [l for l in subprocess.run(
        ["git", "-C", REPO, "log", "--reverse", "--pretty=%H", "--", "wiki/synthesis/"],
        capture_output=True, text=True).stdout.split() if l]
    counted = words = 0
    for sha in shas:
        st = subprocess.run(
            ["git", "-C", REPO, "show", "--name-status", "--pretty=", "--diff-filter=A",
             sha, "--", "wiki/"], capture_output=True, text=True).stdout
        counted += sum(1 for x in st.splitlines()
                       if x.strip().endswith(".md")
                       and x.split("\t")[-1].startswith("wiki/synthesis/"))
        diff = subprocess.run(["git", "-C", REPO, "show", sha, "--", "wiki/**/*.md",
                               "wiki/*.md"], capture_output=True, text=True).stdout
        cur = None
        for ln in diff.splitlines():
            if ln.startswith("+++ "):
                p = ln[4:].strip()
                cur = p[2:] if p.startswith("b/") else p
            elif ln.startswith("+") and cur and cur.startswith("wiki/synthesis/"):
                words += len(ln[1:].split())
    print("  essays on disk %d / counted from git %d; words counted %s"
          % (on_disk, counted, "{:,}".format(words)))
    assert counted == on_disk, "git-counted essays %d != %d on disk" % (counted, on_disk)
    assert words > 0, "word extraction returned zero -- diff attribution is broken"


def test_staleness_boundaries_are_inclusive():
    """The lane is weekly. At exactly 14 days TWO expected runs have produced
    nothing, and that is the moment worth flagging -- not the day after. This
    caught a real off-by-one (`> 14` let 14 days read as ok)."""
    series = [{"date": "2026-05-11", "synthesis_essays": 1, "synthesis_words": 800},
              {"date": "2026-08-12", "synthesis_essays": 2, "synthesis_words": 1600},
              {"date": "2026-08-20", "synthesis_essays": 0, "synthesis_words": 0}]
    for day, want in (("2026-08-19", "ok"), ("2026-08-26", "warn"),
                      ("2026-09-01", "warn"), ("2026-09-02", "fail")):
        c = M.synthesis_census(series, today=datetime.date(*map(int, day.split("-"))))
        assert c["status"] == want, "%s: %s != %s (%sd)" % (day, c["status"], want,
                                                            c["stale_days"])
        assert c["provenance"]["last_essay_day"] == "2026-08-12", \
            "a zero-essay day was mistaken for lane activity"
    print("  boundaries ok at 8d/14d/20d/21d")


def test_empty_series_is_unknown_never_ok():
    """A lane with no recorded output must never read healthy. This is the
    signals-axis lesson: it sat at 0 for six weeks and nothing said so."""
    c = M.synthesis_census([])
    assert c["status"] == "unknown", "empty series read as %s" % c["status"]
    assert c["stale_days"] is None


def test_one_essay_per_pair_invariant():
    """Every essay bridges a distinct pair. A divergence means the lane wrote a
    second essay for a pair it had already bridged, or a filename stopped
    matching <a>_<b>_bridge.md. Either is worth knowing; neither is fatal."""
    c = M.synthesis_census([])
    print("  pairs %d, traditions %d, unparsed %d"
          % (c["pairs_on_disk"], c["traditions"], c["unparsed_filenames"]))
    assert c["unparsed_filenames"] == 0, \
        "%d filenames do not match <a>_<b>_bridge.md" % c["unparsed_filenames"]
    assert c["pairs_equal_essays"], "one-essay-per-pair invariant broken"


if __name__ == "__main__":
    failed = 0
    for name, fn in sorted(globals().items()):
        if not name.startswith("test_"):
            continue
        try:
            print("%s ..." % name)
            fn()
        except AssertionError as e:
            failed += 1
            print("  FAIL: %s" % e)
    print("\n%s" % ("ALL PASSED" if not failed else "%d FAILED" % failed))
    sys.exit(1 if failed else 0)

#!/usr/bin/env python3
"""Unit + integration tests for the janitor's roster-drift check (fact_inventory
R5, Family 1). Plain asserts, no pytest dependency.

    python3 scripts/test_janitor_drift.py

Unit tests exercise the pure _roster_findings() core with synthetic rosters so
every branch is covered without fixture files. The final integration test runs
check_roster_drift() against the real repo and pins the current known state, so
a future roster change forces a conscious test update (Rule 9: encode intent).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import janitor as J  # noqa: E402


def checks(findings):
    return sorted(f.check for f in findings)


def by_check(findings, name):
    return [f for f in findings if f.check == name]


# A fully-aligned roster: three agents, all four surfaces agree, no alias.
BASE = dict(
    agents=["a", "b", "c"],
    friendly=["a", "b", "c"],
    roster_size=3,
    alias={},
    map_ids=["a", "b", "c"],
    allow={},
)


def run(**over):
    d = dict(BASE)
    d.update(over)
    return J._roster_findings(
        d["agents"], d["friendly"], d["roster_size"],
        d["alias"], d["map_ids"], d["allow"])


def test_aligned_roster_is_clean():
    assert checks(run()) == [], "an aligned roster should produce no findings"


def test_duplicate_taskid_warns():
    f = run(agents=["a", "a", "b", "c"])
    assert "roster_duplicate_taskid" in checks(f)
    assert by_check(f, "roster_duplicate_taskid")[0].severity == "warn"


def test_friendly_orphan_warns():
    f = run(friendly=["a", "b", "c", "ghost"])
    assert "roster_friendly_orphan" in checks(f)
    assert "agent:ghost" == by_check(f, "roster_friendly_orphan")[0].scope


def test_missing_friendly_name_is_ok():
    # an AGENT with no friendly name is fine — fname() falls back.
    f = run(friendly=["a", "b"])
    assert "roster_friendly_orphan" not in checks(f)


def test_roster_size_stale_warns():
    f = run(roster_size=99)
    assert "roster_size_stale" in checks(f)
    assert by_check(f, "roster_size_stale")[0].severity == "warn"


def test_roster_size_none_is_skipped():
    f = run(roster_size=None)
    assert "roster_size_stale" not in checks(f)


def test_map_agent_not_displayed_warns():
    f = run(map_ids=["a", "b", "c", "hidden"], roster_size=4)
    assert "roster_map_not_displayed" in checks(f)


def test_display_extra_is_info():
    f = run(agents=["a", "b", "c", "extra"])
    fe = by_check(f, "roster_display_extra")
    assert fe and fe[0].severity == "info"


def test_display_extra_suppressed_by_allowlist():
    allow = {"roster_display_only": [{"taskId": "extra"}]}
    f = run(agents=["a", "b", "c", "extra"], allow=allow)
    assert "roster_display_extra" not in checks(f), \
        "allowlisted display-only agent must be suppressed"


def test_alias_normalizes_both_directions():
    # display id 'disp' aliases to canonical 'canon'; the map holds 'canon'.
    f = run(agents=["a", "b", "c", "disp"],
            friendly=["a", "b", "c", "disp"],
            map_ids=["a", "b", "c", "canon"],
            roster_size=4,
            alias={"disp": "canon"})
    # canon IS displayed (via disp) -> no map_not_displayed;
    # disp DOES map into the roster (via canon) -> no display_extra.
    assert checks(f) == [], \
        "alias should reconcile disp<->canon in both directions: %r" % checks(f)


def test_allowlist_never_hides_a_real_map_gap():
    # a genuine map_not_displayed must still fire even with an allowlist present.
    allow = {"roster_display_only": [{"taskId": "whatever"}]}
    f = run(map_ids=["a", "b", "c", "hidden"], roster_size=4, allow=allow)
    assert "roster_map_not_displayed" in checks(f)


def test_integration_real_repo_state():
    """Pin the current real roster: fully clean. The three known display-only
    agents (watchdog, collaboration-history, korbyt-tasks) are allowlisted in
    drift_allowlist.json['roster_display_only']; every within-universe invariant
    holds. If this fails, the roster changed — reconcile agent_map.json /
    agents_tab.html or update the allowlist consciously (never silence a real
    warn just to green this test)."""
    f = J.check_roster_drift()
    assert f == [], "real roster drift detected: %r" % (
        [(x.severity, x.check, x.scope, x.detail) for x in f])


# ---- schedule-drift unit tests (fact_inventory Family 2 / R5) --------------
# Synthetic single-agent lists exercise the pure _schedule_findings() core so
# every parse/compare branch is covered without fixture files.

def sched(**over):
    a = dict(taskId="x", schedule="Mon 03:00", cron="0 3 * * 1")
    a.update(over)
    return J._schedule_findings([a])


def test_schedule_aligned_is_clean():
    assert sched() == [], "string time+weekday matching cron should be clean"


def test_schedule_time_drift_warns():
    f = sched(schedule="Mon 03:04", cron="0 3 * * 1")
    assert [x.check for x in f] == ["schedule_string_drift"]
    assert f[0].severity == "warn"
    assert "03:04 vs cron 03:00" in f[0].detail


def test_schedule_daily_string_vs_daily_cron():
    # 'daily HH:MM' vs a daily cron is time-comparable (the broad drift class).
    f = sched(schedule="daily 06:03", cron="0 6 * * *")
    assert len(f) == 1 and "06:03 vs cron 06:00" in f[0].detail


def test_schedule_weekday_drift_warns():
    # time matches, but the string names Mon while cron fires Tue (dow 2).
    f = sched(schedule="Mon 03:00", cron="0 3 * * 2")
    assert len(f) == 1 and "weekday Mon vs cron dow 2" in f[0].detail


def test_schedule_daily_string_skips_weekday_check():
    # 'daily' names no weekday, so only time is compared (here it matches).
    assert sched(schedule="daily 03:00", cron="0 3 * * 5") == []


def test_schedule_multi_time_cron_skipped():
    # '*/4' hour fires many times a day; a single display time is not comparable.
    assert sched(schedule="every 4h :15", cron="15 */4 * * *") == []


def test_schedule_listed_hour_cron_skipped():
    # a comma-list hour ('2,6,10,...') is likewise multi-time -> not comparable.
    assert sched(schedule="every 4h :15 (offset)",
                 cron="15 2,6,10,14,18,22 * * *") == []


def test_schedule_no_time_string_skipped():
    assert sched(schedule="manual", cron=None) == []
    assert sched(schedule="manual only", cron="0 3 * * 1") == []


def test_schedule_missing_fields_skipped():
    assert J._schedule_findings([{"taskId": "x"}]) == []


def test_schedule_mon_fri_time_only():
    # 'Mon-Fri' is a range: weekday isn't checked (cron dow '1-5' isn't single),
    # but the time still drifts and must surface.
    f = sched(schedule="Mon-Fri 09:10", cron="0 9 * * 1-5")
    assert len(f) == 1 and "09:10 vs cron 09:00" in f[0].detail
    assert "weekday" not in f[0].detail


def test_schedule_dow_seven_is_sunday():
    # cron dow 7 and 0 both mean Sunday; a 'Sun' string must reconcile with 7.
    assert sched(schedule="Sun 03:00", cron="0 3 * * 7") == []


def test_schedule_integration_real_repo():
    """Pin the current real state: CLEAN. The 30 formerly-drifted schedule strings
    were canonicalized to their cron minute in agent_map.json (2026-07-21, the
    follow-up to increment 3), so every comparable string now matches its cron and
    the check returns []. If this fails, a schedule string drifted from cron again
    (or a new agent landed with a stale string) — fix agent_map.json, never silence
    a real warn to green this test (Rule 9)."""
    f = J.check_schedule_drift()
    assert f == [], "real schedule drift detected: %r" % (
        [(x.severity, x.scope, x.detail) for x in f])


# ---- tab-description-coverage unit tests (fact_inventory Family 4 / R5) -----

def tdc(tabs, keys, exempt=frozenset()):
    return J._tab_desc_findings(tabs, keys, exempt)


def test_tab_all_covered_is_clean():
    tabs = [("a.html", "A"), ("b.html", "B")]
    assert tdc(tabs, {"a.html", "b.html"}) == []


def test_tab_missing_description_warns():
    f = tdc([("a.html", "A"), ("gap.html", "Gap")], {"a.html"})
    assert [x.check for x in f] == ["tab_missing_description"]
    assert f[0].severity == "warn" and f[0].scope == "tab:gap.html"


def test_tab_orphan_description_not_flagged():
    # a description key with no tab button (a sub-view) is NOT a finding.
    assert tdc([("a.html", "A")], {"a.html", "subview.html"}) == []


def test_tab_exempt_suppresses():
    f = tdc([("a.html", "A"), ("gap.html", "Gap")], {"a.html"}, {"gap.html"})
    assert f == [], "allowlisted tab must be suppressed"


def test_tab_duplicate_src_reported_once():
    # a view reachable from two buttons must yield a single finding.
    f = tdc([("gap.html", "Nav"), ("gap.html", "Footer")], set())
    assert len(f) == 1


def test_tab_exempt_never_hides_a_different_gap():
    f = tdc([("x.html", "X"), ("y.html", "Y")], set(), {"x.html"})
    assert [x.scope for x in f] == ["tab:y.html"]


def test_tab_integration_real_repo():
    """Pin the current real state: two live tabs — Start here (start_here.html) and
    Inter-Tradition Study (interT_study.html) — have no descriptions entry, so their
    "?" falls back to generic text. When help text is authored for them (a No-Blind-
    Push explorer.html edit) or they are exempted, this list shrinks and the test
    must be updated consciously (Rule 9)."""
    f = J.check_tab_description_coverage()
    assert all(x.check == "tab_missing_description" and x.severity == "warn"
               for x in f), "unexpected finding shape: %r" % [
                   (x.check, x.severity) for x in f]
    scopes = sorted(x.scope for x in f)
    assert scopes == ["tab:interT_study.html", "tab:start_here.html"], \
        "tab-description gaps changed: %r" % scopes


# ---- count-drift unit tests (fact_inventory Family 2 / R5) ------------------

def caf(text, pattern, real=155, name="curated", src="src.json", af="a.html"):
    return J._count_assertion_findings(name, real, src, af, text, pattern)


def test_count_match_is_clean():
    assert caf("we curated 155 things", r"curated (\d+)") == []


def test_count_drift_warns_with_line():
    f = caf("line1\nhas 156 curated items", r"(\d[\d,]*) curated")
    assert [x.check for x in f] == ["count_drift"]
    assert f[0].severity == "warn" and f[0].scope == "a.html:2"
    assert "asserts 156 but src.json has 155" in f[0].detail


def test_count_commas_stripped():
    # "1,006" must parse as 1006, not fail or read as 1.
    f = caf("the 1,006 curated set", r"(\d[\d,]*) curated", real=1006)
    assert f == [], "1,006 should equal real=1006 after comma strip"


def test_count_multiple_assertions_each_reported():
    f = caf("156 curated ... and 156 curated again", r"(\d[\d,]*) curated")
    assert len(f) == 2 and all(x.check == "count_drift" for x in f)


def test_count_stale_pattern_is_info():
    # a registered pattern that no longer matches surfaces (never silently drops).
    f = caf("no number here", r"(\d+) curated")
    assert [x.check for x in f] == ["count_assertion_stale"]
    assert f[0].severity == "info"


def test_count_specific_pattern_ignores_unrelated_numbers():
    # 'N curated' must not fire on '156 scanned pages' or '100 communities'.
    txt = "156 scanned pages; 100 communities; 155 curated communities"
    assert caf(txt, r"(\d[\d,]*) curated") == []


def test_real_count_json_list(tmp_path=None):
    import tempfile, os, json as _j
    d = tempfile.mkdtemp()
    p = os.path.join(d, "x.json")
    open(p, "w").write(_j.dumps([1, 2, 3]))
    # _real_count resolves relative to PROJECT_ROOT; pass an absolute-ish shim
    rel = os.path.relpath(p, J.PROJECT_ROOT)
    assert J._real_count({"file": rel, "kind": "json_len"}) == 3


def test_count_integration_real_repo():
    """Pin the current real state: the curated-community count is asserted as 156
    in three prose sites but curated_communities.json holds 155 (fact_inventory
    off-by-one). When reconciled — prose changed to 155, or a 156th community added
    — this shrinks and the test must be updated consciously (Rule 9)."""
    f = J.check_count_drift()
    drift = [x for x in f if x.check == "count_drift"]
    assert len(drift) == 3, "curated-community count drift changed: %r" % [
        (x.scope, x.detail) for x in drift]
    assert all("155" in x.detail for x in drift)
    assert not [x for x in f if x.check in (
        "count_source_unreadable", "count_assertion_unreadable",
        "count_assertion_stale")], "registry has an unreadable/stale entry: %r" % [
            (x.check, x.detail) for x in f]


def main():
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
            print("ok    ", t.__name__)
        except AssertionError as e:
            failed += 1
            print("FAIL  ", t.__name__, "--", e)
        except Exception as e:  # noqa: BLE001
            failed += 1
            print("ERROR ", t.__name__, "--", type(e).__name__, e)
    print("\n%d/%d passed" % (len(tests) - failed, len(tests)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

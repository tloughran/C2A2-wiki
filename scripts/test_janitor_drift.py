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

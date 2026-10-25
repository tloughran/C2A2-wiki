#!/usr/bin/env python3
"""check_pages_live.py -- is the PUBLIC site what is on GitHub?

WHY: every Pages deploy from 2026-10-06 to 2026-10-25 sat "pending" behind one
run that waited on an environment approval no setting required any more, until
the next push cancelled it. Nineteen days of pushes never reached the live site,
and every check here stayed green, because they all read origin -- none read
Pages. Found only because a tab was visibly missing (handoffs/explorer-tab-visibility.md).

THREE QUESTIONS, all deterministic (no model):
  1. Is a Pages deploy stuck?   any "Deploy static site to Pages" run still
                                queued/waiting/pending/in_progress after STUCK_HOURS.
  2. Did the last deploy fail?  newest COMPLETED deploy run concluded "failure".
                                ("cancelled" is normal: a newer push supersedes.)
  3. Is the entry page live?    the bytes of PROBE on Pages equal the bytes on
                                main, once main last touched PROBE more than
                                GRACE_HOURS ago. Inside the grace window a
                                difference is a deploy in flight: WARN, not FAIL.
                                Stateless: the anchor is the commit date main
                                records, never a stored "first seen" flag.

Robot pushes (heartbeat-refresh, via GITHUB_TOKEN) do NOT trigger a deploy, so
data files legitimately lag Pages until the next Mac push. That is why the probe
is explorer.html, which only human-reviewed pushes touch.

WRITES (all gitignored):
  scheduler/pages_live.json  -- checked_at (every fire), verdict, detail lines
  scheduler/pages_live.md    -- one line per fire
  pages_live.FAILED          -- repo root, present exactly while the verdict is
                                FAIL (first line "[stamp] reason"); removed on
                                OK/WARN. check_scheduler_health.py reads it.

EXIT: 0 OK or WARN | 3 FAIL (a VERDICT about the site, excused in
      check_scheduler_health.py VERDICT_EXITS) | 2 cannot reach GitHub | 1 script error

Usage:  python3 scripts/check_pages_live.py [--dry-run]
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER_REPO = "tloughran/C2A2-wiki"
PAGES_BASE = "https://tloughran.github.io/C2A2-wiki/"
RAW_BASE = "https://raw.githubusercontent.com/" + OWNER_REPO + "/main/"
API = "https://api.github.com/repos/" + OWNER_REPO
DEPLOY_WORKFLOW = "Deploy static site to Pages"
WORKFLOW_FILE = "pages.yml"
PROBE = "wiki/explorer.html"
STUCK_HOURS = 2.0
GRACE_HOURS = 2.0
UNFINISHED = ("queued", "waiting", "pending", "in_progress", "requested")

OK, WARN, FAIL = "OK", "WARN", "FAIL"


class Unreachable(Exception):
    """GitHub or Pages could not be read: the check did not run (exit 2)."""


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "c2a2-pages-live-check",
                                               "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read()
    except Exception as exc:  # URLError, HTTPError, timeout: all mean "could not look"
        raise Unreachable(f"{url}: {exc}")


def parse_ts(text):
    return datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def assess(now, runs, probe_commit_at, live_bytes, main_bytes):
    """Pure verdict from what was fetched -> (verdict, [detail lines])."""
    findings = []
    deploys = [r for r in runs if r.get("name") == DEPLOY_WORKFLOW]

    for r in deploys:
        if r.get("status") in UNFINISHED:
            age = (now - parse_ts(r["created_at"])).total_seconds() / 3600
            if age > STUCK_HOURS:
                findings.append((FAIL, f"deploy run #{r.get('run_number')} ({r['head_sha'][:8]}) "
                                       f"has been '{r['status']}' for {age:.1f}h -- it holds the "
                                       f"Pages queue; open {r.get('html_url')}"))

    done = [r for r in deploys if r.get("status") == "completed"]
    if done and done[0].get("conclusion") == "failure":
        r = done[0]
        findings.append((FAIL, f"newest finished deploy #{r.get('run_number')} "
                               f"({r['head_sha'][:8]}) FAILED: {r.get('html_url')}"))

    since = (now - probe_commit_at).total_seconds() / 3600
    if live_bytes == main_bytes:
        findings.append((OK, f"{PROBE} live == main ({len(main_bytes)} bytes)"))
    elif since <= GRACE_HOURS:
        findings.append((WARN, f"{PROBE} live != main, but main changed it {since:.1f}h ago "
                               f"(<= {GRACE_HOURS:g}h grace): a deploy may be in flight"))
    else:
        findings.append((FAIL, f"{PROBE} live != main ({len(live_bytes)} vs {len(main_bytes)} "
                               f"bytes) {since:.1f}h after main last changed it"))

    order = {OK: 0, WARN: 1, FAIL: 2}
    verdict = max((v for v, _ in findings), key=order.get)
    return verdict, [f"{v}: {d}" for v, d in findings]


def gather(get=fetch):
    # Recent Pages runs answer "did the last deploy fail". A stuck run is asked
    # for BY STATUS: in the 2026-10 jam the run holding the queue was three weeks
    # and ~50 runs old, far outside any recent-runs window, and the newest pending
    # run behind it was often under STUCK_HOURS old at check time.
    base = API + "/actions/workflows/" + WORKFLOW_FILE + "/runs?per_page=30"
    runs = json.loads(get(base))["workflow_runs"]
    seen = {r.get("id") for r in runs}
    for status in UNFINISHED:
        for r in json.loads(get(base + "&status=" + status))["workflow_runs"]:
            if r.get("id") not in seen:
                seen.add(r.get("id"))
                runs.append(r)
    commits = json.loads(get(API + "/commits?sha=main&per_page=1&path=" + PROBE))
    if not commits:
        raise Unreachable(f"no commit on main touches {PROBE}")
    probe_commit_at = parse_ts(commits[0]["commit"]["committer"]["date"])
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    live = get(PAGES_BASE + PROBE + "?check=" + stamp)
    main = get(RAW_BASE + PROBE)
    return runs, probe_commit_at, live, main


def write_outputs(repo, now, verdict, details):
    local = now.astimezone()
    stamp = local.strftime("%Y-%m-%d %H:%M:%S")
    sched = os.path.join(repo, "scheduler")
    os.makedirs(sched, exist_ok=True)
    with open(os.path.join(sched, "pages_live.json"), "w") as fh:
        json.dump({"checked_at": local.isoformat(timespec="seconds"),
                   "verdict": verdict, "detail": details}, fh, indent=2)
        fh.write("\n")
    worst = next((d for d in details if d.startswith(verdict)), details[-1])
    with open(os.path.join(sched, "pages_live.md"), "a") as fh:
        fh.write(f"{stamp} {verdict} -- {worst}\n")
    marker = os.path.join(repo, "pages_live.FAILED")
    if verdict == FAIL:
        with open(marker, "w") as fh:
            fh.write(f"[{stamp}] {worst}\n")
            for d in details:
                fh.write(d + "\n")
    elif os.path.exists(marker):
        os.remove(marker)


def main(argv, repo=REPO, get=fetch, now=None):
    dry = "--dry-run" in argv
    now = now or datetime.now(timezone.utc)
    try:
        runs, probe_at, live, main_bytes = gather(get)
    except Unreachable as exc:
        print(f"pages-live: cannot check -- {exc}")
        return 2
    verdict, details = assess(now, runs, probe_at, live, main_bytes)
    print(f"pages-live: {verdict}")
    for d in details:
        print("  " + d)
    if not dry:
        write_outputs(repo, now, verdict, details)
    return 3 if verdict == FAIL else 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as exc:  # a crash must not read as a verdict
        print(f"pages-live: script error: {exc!r}")
        sys.exit(1)

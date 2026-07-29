#!/usr/bin/env python3
"""openstory_ingest_lag.py -- THE single answer to "is OpenStory ingest keeping up?"

WHY THIS FILE EXISTS (2026-07-29)
---------------------------------
On 2026-07-27 the backend's kqueue watcher hit EMFILE partway through registering
the watch tree and stopped delivering events. Its HTTP thread kept answering
/health 200, so openstory-watchdog.sh -- which asked only "are you up?" -- saw a
healthy service for 53 hours while nothing was ingested. The daily refresh guard
DID notice (REFRESH_STATUS.md, 2026-07-29 FAIL), but it runs once a day and can
only refuse to refresh feeds; it cannot restart anything.

So the watchdog now checks ingest progress too. To keep that from becoming two
drifting opinions, both callers ask THIS script, and it is the only place the
question is answered.

WHY LAG, NOT AGE
----------------
Two wrong signals were considered and rejected:

  * .db file mtime -- in WAL mode the main DB file only changes on checkpoint, so
    it reads stale during perfectly healthy ingest; and a mere *reader* touches
    -shm/-wal, so it can read fresh when ingest is dead. Observed both ways on
    2026-07-29.
  * absolute frontier age -- false-positives every time nobody is running
    sessions. Six quiet hours is not a six-hour outage.

The honest question is whether ingest has fallen BEHIND THE DISK:

    lag = mtime(newest transcript in watch root) - MAX(sessions.last_event)

If nothing is being written, both ends sit still and lag stays flat -- healthy,
at any hour of the day. During the 2026-07-27 stall the disk kept moving while
the frontier did not, and lag grew to 53h. That is the signal.

Exit codes:  0 = within threshold, 1 = lagging, 2 = cannot determine (fail loud;
callers must treat 2 as "unknown", never as "fine").
"""

import argparse
import datetime as dt
import os
import sqlite3
import sys

DEFAULT_DB = os.path.expanduser(
    "~/Documents/Non-Claude Projects/OpenStory/data/open-story.db")
DEFAULT_WATCH = os.path.expanduser("~/openstory-watch")
# 30 min: comfortably above normal write-to-ingest latency (seconds), far below
# the hours-long stalls this exists to catch.
DEFAULT_MAX_LAG = 1800


def die(msg):
    sys.stderr.write("openstory_ingest_lag: %s\n" % msg)
    sys.exit(2)


def frontier_epoch(db):
    """Newest ingested event across all sessions, as epoch seconds."""
    if not os.path.isfile(db):
        die("DB not found: %s" % db)
    try:
        # Read-only URI so this can never block or corrupt a live writer.
        con = sqlite3.connect("file:%s?mode=ro" % db, uri=True, timeout=10)
        row = con.execute(
            "SELECT MAX(last_event), COUNT(*) FROM sessions").fetchone()
        con.close()
    except sqlite3.Error as e:
        die("DB read failed: %s" % e)
    newest, count = row if row else (None, 0)
    if not newest:
        die("no sessions rows -- cannot establish an ingest frontier")
    iso = newest.replace("Z", "+00:00")
    try:
        return dt.datetime.fromisoformat(iso).timestamp(), newest, count
    except ValueError:
        die("unparseable last_event: %r" % newest)


def newest_source(watch_root):
    """mtime of the most recently written transcript under watch_root.

    stat() (not lstat) on purpose: the watch root is a tree of symlinks created
    by openstory-bridge.sh, and what matters is when the real transcript was
    appended, not when the link was made. Broken links are skipped rather than
    fatal -- a dangling link is the bridge's problem, not an ingest stall.
    """
    if not os.path.isdir(watch_root):
        die("watch root not found: %s" % watch_root)
    newest, newest_path, n = 0.0, None, 0
    for root, _dirs, files in os.walk(watch_root):
        for f in files:
            if not f.endswith(".jsonl"):
                continue
            try:
                m = os.stat(os.path.join(root, f)).st_mtime
            except OSError:
                continue
            n += 1
            if m > newest:
                newest, newest_path = m, os.path.join(root, f)
    if not n:
        die("no .jsonl transcripts under %s -- bridge not running?" % watch_root)
    return newest, newest_path, n


def iso(epoch):
    return dt.datetime.fromtimestamp(epoch, dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--watch-root", default=DEFAULT_WATCH)
    ap.add_argument("--max-lag", type=int, default=DEFAULT_MAX_LAG,
                    help="seconds of lag tolerated before exit 1")
    ap.add_argument("--quiet", action="store_true",
                    help="print nothing on success (exit code only)")
    a = ap.parse_args()

    front, front_iso, sessions = frontier_epoch(a.db)
    src, src_path, files = newest_source(a.watch_root)

    # Negative lag means the frontier is ahead of the newest file mtime, which
    # happens routinely (the DB records the event; the file's mtime may lag a
    # buffered flush). Not a fault -- clamp.
    lag = max(0, int(src - front))
    stale = lag > a.max_lag

    line = ("lag=%ds frontier=%s newest_source=%s sessions=%d files=%d"
            % (lag, front_iso, iso(src), sessions, files))
    if stale:
        sys.stderr.write("STALE: %s (threshold %ds)\n  behind: %s\n"
                         % (line, a.max_lag, src_path))
        print(line)
        sys.exit(1)
    if not a.quiet:
        print(line)
    sys.exit(0)


if __name__ == "__main__":
    main()

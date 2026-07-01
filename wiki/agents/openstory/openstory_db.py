#!/usr/bin/env python3
"""
openstory_db.py -- shared, contention-tolerant read access to the live OpenStory DB.

Why this exists: open-story.db is WAL-mode and written continuously by the agent
runtime, and the C2A2 sandbox reaches it over a FUSE mount. Empirically (2026-06-26,
during a peak write/checkpoint burst):

  * Plain mode=ro full scans trip RELIABLY with "database disk image is malformed /
    Page <n> is never used" -- a write lands during the seconds-long scan and the
    WAL/shm can't be coordinated for our reader over the mount.
  * PRAGMA quick_check and the SQLite backup API (both whole-file scans) trip the same
    way. The prior daily refresh aborted every morning since 2026-06-08 precisely
    because its connect helper ran a quick_check guard. (Verified from the task's run
    transcript.)
  * An in-place immutable=1 read survives SHORT scans but still tears on a LONG one
    (the extractor holds the connection ~35 s, long enough to overlap a checkpoint
    that rewrites the main file).

So the only robust shape is to DECOUPLE the long read from the live writer: take a
dumb byte-copy of the main db file to LOCAL disk (off the FUSE mount), validate THAT
copy, and let the extractor do all its slow work against the static local file. The
copy omits the -wal sidecar, so the data is as of the last checkpoint (empirically
~minutes behind) -- the right trade for a daily snapshot. A copy torn by a checkpoint
is caught by the local quick_check and retried by run_with_retry.

House rules: regular strings only; fail loud (Rule 12) rather than emit garbage.
"""

import atexit
import os
import shutil
import sqlite3
import sys
import tempfile
import time
import urllib.parse


# --- Cross-project exclusions (ISOLATE NOW, REMOVE LATER) -------------------
# BOSCO is a SEPARATE project (Northern Uganda off-grid archive) whose sessions
# leak into the live OpenStory store but must NOT be mined into C2A2 telemetry.
# Matched by any text field (session label, project_name, scheduled-task name),
# case-insensitive substring. Single source of truth for both agent extractors.
# Provisional: when BOSCO sessions are purged from open-story.db, delete
# EXCLUDED_PROJECT_SUBSTRINGS + is_excluded and the two extractor call sites.
EXCLUDED_PROJECT_SUBSTRINGS = ("bosco",)


def is_excluded(*fields):
    """True if any provided text field matches an excluded cross-project
    substring (case-insensitive). Keeps BOSCO out of every C2A2 feed from one
    definition rather than a filter duplicated per extractor."""
    for f in fields:
        if f and any(sub in f.lower() for sub in EXCLUDED_PROJECT_SUBSTRINGS):
            return True
    return False


def _quiet_remove(path):
    try:
        os.remove(path)
    except OSError:
        pass


def connect_ro(live_db):
    """Return a read connection to a consistent LOCAL copy of the live db.

    Copies the main db file (only) to local temp, opens it immutable, and integrity-
    checks the local copy. A torn copy (a checkpoint rewrote pages during the byte
    copy) fails the local quick_check and is raised as DatabaseError so run_with_retry
    re-copies. The successful copy is cleaned up at interpreter exit."""
    if not os.path.exists(live_db):
        sys.exit("ERROR: DB not found: %s" % live_db)
    fd, local = tempfile.mkstemp(prefix="os_agent_local_", suffix=".db")
    os.close(fd)
    # Dumb byte copy: no SQLite consistency is assumed during the copy itself; the
    # bytes we get are validated locally next. Local disk is off the FUSE mount and
    # has no live writer, so the long extractor read that follows is stable.
    shutil.copyfile(live_db, local)
    con = sqlite3.connect("file:%s?immutable=1" % urllib.parse.quote(local), uri=True)
    res = con.execute("PRAGMA quick_check(1)").fetchone()[0]
    if res != "ok":
        con.close()
        _quiet_remove(local)
        raise sqlite3.DatabaseError(
            "local copy failed quick_check -- a checkpoint rewrote pages mid-copy "
            "(torn copy); retrying: %s" % res
        )
    atexit.register(_quiet_remove, local)
    return con


def run_with_retry(fn, tries=4, delay=3.0):
    """Run fn() and, on a transient sqlite DatabaseError (a torn copy / mid-write
    inconsistency), retry the whole call. fn MUST be idempotent -- both agent
    extractors are: they read into memory and write their output only after all reads
    succeed.

    After `tries` failures we fail loud: persistent failure against a quiet DB is
    genuine on-disk corruption (operator fix: sqlite3 db '.recover'), and the calling
    scheduled task must surface it rather than silently leave stale data."""
    last = None
    for i in range(tries):
        try:
            return fn()
        except sqlite3.DatabaseError as e:
            last = e
            sys.stderr.write(
                "[openstory_db] transient DB read error (attempt %d/%d): %s\n"
                % (i + 1, tries, e)
            )
            time.sleep(delay)
    sys.exit(
        "ERROR: open-story.db unreadable after %d attempts -- if a writer/checkpoint "
        "is active this is contention (re-run when quiet); if it persists against a "
        "quiet DB it is genuine corruption (sqlite3 db '.recover'): %s" % (tries, last)
    )

SEARCH-AGAINST-ASSUMPTION-1663:
  Date searched: 2026-09-24
  Original item: ASSUMPTION-1663
  Original statement: The large-db jobs cannot run in the sandbox (7.2 GB db vs 5.9 GB free).
    Proposed fixes: the SQLite backup API or `VACUUM INTO`, or running on the Mac. (Tested claim:
    the backup API or VACUUM INTO can produce a consistent read snapshot of a live 7+ GB WAL-mode
    db within bounded scratch space.)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1663
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted diagnosis and proposed mechanisms (db grew 7.14 → 7.2 GB in a day).
      15b: Searched for challenging literature (lane: SQLite backup / VACUUM INTO semantics; immutable=1 risk)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. SQLite project. "Online Backup API" (sqlite.org/c3ref/backup_finish.html). [Fetched; primary.]
       The source is read-locked only during each sqlite3_backup_step() call. If another connection
       or process modifies the source between steps, "the backup will be automatically restarted".
       On a live db with frequent writes, an incremental backup of 7+ GB may restart repeatedly and
       never finish. A single step(-1) avoids restarts only by holding the read for the whole copy.
       The destination is a full page-for-page copy, the same size as the source; it does not
       shrink. The page also names VACUUM INTO and sqlite3_rsync as the other "safe" ways to take a
       consistent backup. This CORROBORATES consistency, but only for the copy mechanisms.
    2. SQLite project. "Write-Ahead Logging" (sqlite.org/wal.html, updated 2026-08-25). [Fetched;
       primary.] A long read transaction stops the checkpointer from making progress. With
       overlapping readers, "the WAL file will grow without bound". A multi-minute snapshot read of
       7 GB (VACUUM INTO or step(-1)) pins the WAL, so the live db's -wal file grows on the host
       while the copy runs. Section 11 also documents a WAL-reset corruption bug in 3.7.0-3.51.2
       (fixed in 3.51.3) that is triggered by concurrent write/checkpoint from separate processes.
       That is the exact topology of a live db plus a snapshotting job.
    3. SQLite project. "URI Filenames" (sqlite.org/uri.html). [Seen in search results; wording from
       snippet, not fetched.] If a file marked immutable=1 changes anyway, SQLite "might return
       incorrect query results and/or SQLITE_CORRUPT errors". immutable=1 skips locking and change
       detection, so it is unsafe on a live WAL db and gives no consistency guarantee.
    4. SQLite VACUUM docs (legacy copy via system.data.sqlite.org mirror). [Fetched; this older
       version predates VACUUM INTO.] Plain VACUUM may need up to 2x the db size in free space. This
       applies to in-place VACUUM, not VACUUM INTO. Recorded here to prevent a mix-up between the two.

  Strength of challenge: Strong (on the "bounded scratch space" part); Weak (on consistency)

  Summary: The consistency half of the claim holds according to SQLite's own documentation.
  VACUUM INTO and the backup API are listed as safe ways to take a consistent copy (a single
  step(-1) or VACUUM INTO reads one snapshot). The "within bounded scratch space" half is
  challenged. Both mechanisms write a whole database to the destination. VACUUM INTO writes a
  compacted copy that is at most about the live size (minus free pages). The backup API writes a
  full-size copy. Neither can fit a 7.2 GB db into 5.9 GB unless free-page compaction happens to
  recover more than 1.3 GB, which is unknown. Neither changes the copy-whole pattern that
  PRESUMPTION-1081 flags. The live-db side has its own costs: WAL growth on the host while the
  snapshot read is held, repeated restarts for the incremental backup API, and the (now patched)
  multi-process WAL-reset bug. immutable=1 is explicitly unsafe here.

  Specific risks: The proposed fix is implemented and still fails on disk space. Or it "succeeds"
  by writing to a host path outside the sandbox scratch, which moves the problem. Or an
  incremental backup loops on restarts. An immutable=1 shortcut returns silently wrong reads.

  Mitigations available: Measure freelist_count × page_size to learn what VACUUM INTO would
  actually produce. Read in place, read-only, via a normal (non-immutable) connection inside one
  read transaction, if the sandbox can reach the file. Export only the needed tables or columns
  (ATTACH plus INSERT…SELECT, or sqlite3_rsync to a host-side replica). Run on the Mac. Check
  SQLite ≥ 3.51.3.

  Search scope: Moderate: 4 searches plus 3 primary-doc fetches (sqlite.org backup API, WAL page;
  legacy VACUUM page). The current lang_vacuum.html page and the uri.html page were not fetched
  (lang_vacuum was not in the provenance set; uri.html was seen in results only).

  Excluded results: DEV Community "Reproduce SQLite WAL Checkpoint Starvation…" post; loke.dev
  "20GB WAL File" blog; photostructure.com; oneuptime.com blog; GitHub grappa-irc issue #2287;
  GitHub better-sqlite3 docs; hoelz.ro and codejam.info blogs on immutable; Coddy/Bun/Scribd pages.
  Excluded as secondary or GitHub. The primary sqlite.org documents were used instead.

  Recommendation: CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1663
  Strongest counterargument: Both proposed mechanisms solve consistency, which was never the
    problem. The problem is space, and both write an entire database to the destination. VACUUM
    INTO's output is bounded by the live data size, not by the scratch size, and the backup API's
    output is full-size. With 7.2 GB live and 5.9 GB free, the fix only works if more than 18% of
    the file is free pages, and nobody has measured that. Meanwhile, the long snapshot read pins
    the WAL and grows the host-side -wal file. The incremental alternative restarts every time the
    live db is written.
  What would need to be true for C2A2 to be safe: A measured freelist showing that the VACUUM INTO
    output is under the scratch size with margin, re-measured as the db grows. Or the destination
    is on the host, not in the sandbox. Or the job reads in place and never copies.
  How to test: Run `PRAGMA page_count; PRAGMA freelist_count; PRAGMA page_size;` on the live db.
    Compute (page_count − freelist_count) × page_size and compare it to 5.9 GB.

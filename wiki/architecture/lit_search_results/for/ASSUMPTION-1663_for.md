SEARCH-FOR-ASSUMPTION-1663:
  Date searched: 2026-09-24
  Original item: ASSUMPTION-1663
  Original statement: The SQLite online backup API or `VACUUM INTO` can produce a consistent read
    snapshot of a live 7+ GB WAL-mode db within bounded scratch space.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-1663
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the stated assumption about SQLite snapshot mechanisms on a live database.
      15a: Searched for supporting literature (official sqlite.org documentation treated as primary)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. SQLite project, "SQLite Backup API" (sqlite.org/backup.html, last updated 2025-11-13; fetched).
       — States that completing the backup call sequence makes the destination a bit-wise identical
       copy of the source as of when copying began (a "snapshot"); incremental stepping means the
       source is read-locked only briefly; and "when the backup operation is completed the backup
       database contains a consistent and up-to-date snapshot." Lists VACUUM INTO as a more recent
       technique for copying a live database.
    2. SQLite project, "VACUUM" (lang_vacuum.html; text seen via search on sqlite.org requirement
       matrix and the System.Data.SQLite doc mirror, direct fetch blocked). — VACUUM INTO output "is a
       consistent snapshot of the original database"; cannot run inside a transaction; output may be
       incomplete if interrupted by power loss; fsync applied when synchronous is NORMAL/FULL.
    3. SQLite project, "URI Filenames In SQLite" (sqlite.org/uri.html; seen in search). — Documents
       that immutable=1 skips all locking and change detection and that if the file changes anyway,
       SQLite "might return incorrect query results and/or SQLITE_CORRUPT errors." Supports the
       lane's premise that immutable=1 is unsafe on a live db and that a sanctioned snapshot
       mechanism is the correct alternative.

  Strength of support: Moderate (Strong for the consistency half; None for the bounded-scratch half)

  Summary: Official documentation directly supports the consistency claim for both mechanisms: the
    backup API and VACUUM INTO are the project's sanctioned ways to take a transactionally consistent
    copy of a live database, including in WAL mode, and immutable=1 is explicitly unsafe on files
    that can change. No source addresses the "bounded scratch space" condition for a 7+ GB database;
    both mechanisms write a full-size (VACUUM INTO: compacted) copy, so scratch is bounded only by
    database size, not independent of it.

  Caveats: (a) The backup API page itself warns that writes from another process/connection force a
    restart, and "if the backup process is restarted frequently enough it may never run to
    completion" — relevant when a separate writer is active on a large db. (b) VACUUM INTO holds a read
    transaction for its duration; in WAL mode this can block checkpoint progress so the -wal file may
    grow during a long copy (inference from WAL semantics, not confirmed from a fetched page).
    (c) Scratch requirement scales with db size; "bounded" is true only in the trivial sense.

  Search scope: Preliminary — three searches plus one fetch of sqlite.org/backup.html. Direct fetch of
    sqlite.org/lang_vacuum.html was refused (URL not yet in provenance set); VACUUM INTO text relied
    on search snippets from sqlite.org pages.

  Excluded results: GitHub issue mgwedd/aletheia #58 ("snapshot the DB (VACUUM INTO) before sealing")
    — GitHub issue, echoes the claim. oneuptime.com blog posts ("How to Back Up a WAL-Mode SQLite
    Database Without Losing Data", 2026-09-08) — vendor blog whose title echoes the lane closely and
    is dated two weeks before this search; not used. sqlite.work (aggregator), Scribd, Coddy,
    PhotoStructure and oldmoe blogs — secondary; primary docs used instead.

  Recommendation: PARTIALLY-SUPPORTED

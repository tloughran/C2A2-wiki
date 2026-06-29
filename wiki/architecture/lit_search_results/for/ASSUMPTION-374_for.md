SEARCH-FOR-ASSUMPTION-374:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-374
  Original statement: "Copy-the-hot-WAL-DB-to-local-disk + validate-the-local-copy is the correct way to read a live 2 GB WAL SQLite DB over a FUSE mount from a second process"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-374
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from OpenStory fix session: read-the-DB strategy stated as copy-to-local-then-validate
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. SQLite documentation, "Appropriate Uses / How To Corrupt" and "Backup API". - SQLite explicitly warns against accessing a database over a network/FUSE filesystem because POSIX advisory locking is unreliable there; pulling the DB to local disk before reading avoids that hazard, which supports the COPY-TO-LOCAL half of the assumption.
    2. SQLite Online Backup API / VACUUM INTO documentation. - SQLite provides a blessed mechanism (sqlite3 .backup / VACUUM INTO) for taking a transactionally consistent snapshot of a live database from a second connection; this validates the GOAL of a consistent local copy.
    3. WAL-mode documentation. - In WAL mode readers do not block writers; a properly taken snapshot can be read concurrently with writes, supporting the feasibility of reading a hot DB.

  Strength of support: Moderate

  Summary: The strategy is partially well-grounded. Pulling a SQLite database off a FUSE/network mount to local disk before reading is exactly what SQLite's own guidance recommends, because advisory locking over FUSE is unreliable. WAL mode permits consistent snapshot reads without blocking the writer. The "validate the local copy" step (e.g., PRAGMA integrity_check) is a recognized safeguard. Support is contingent on the COPY being a consistent snapshot, not a naive byte copy (see caveats).

  Caveats: Support holds only if the copy is taken via the backup API / VACUUM INTO (or by copying main+ -wal+ -shm consistently), NOT via a plain cp during an active checkpoint. integrity_check validates structural integrity but not completeness/freshness, so "validate" is necessary-not-sufficient.

  Search scope: SQLite WAL semantics; backup API; FUSE/network-FS locking. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

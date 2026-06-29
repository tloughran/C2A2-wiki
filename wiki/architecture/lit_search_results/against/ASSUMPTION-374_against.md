SEARCH-AGAINST-ASSUMPTION-374:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-374
  Original statement: "Copy-the-hot-WAL-DB-to-local-disk + validate-the-local-copy is the correct way to read a live 2 GB WAL SQLite DB over a FUSE mount from a second process"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-374
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: copy-to-local-then-validate stated as the correct read method
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. SQLite "How To Corrupt An SQLite Database File" + WAL docs. - A naive byte copy of a hot WAL database (copying main .db without consistently capturing -wal/-shm, or mid-checkpoint) yields a torn/inconsistent file; the blessed method is the backup API / VACUUM INTO, not cp. The assumption is "correct" only if the copy method is the snapshot API.
    2. PRAGMA integrity_check semantics. - integrity_check verifies structural well-formedness, NOT completeness or freshness; a stale or torn-but-structurally-valid snapshot can PASS validation while missing committed data - so "validate the local copy" gives false assurance.
    3. SQLite locking over FUSE/network filesystems. - Locking is unreliable there; if the copy is performed with any locking/read transaction over the FUSE mount, it may itself observe an inconsistent state during a concurrent checkpoint.

  Strength of challenge: Moderate

  Summary: The strategy is correct in its broad shape (read off local disk, not over FUSE) but the stated form is under-specified in a way the literature flags as dangerous. "Copy" must mean a consistent-snapshot copy (backup API / VACUUM INTO), not a file cp, or torn copies are expected under write load. Worse, the "validate" step relies on integrity_check, which cannot detect a stale or incomplete snapshot - it tests structure, not completeness - so passing validation does not establish the copy is correct.

  Specific risks: A torn or stale local copy passes integrity_check and is treated as ground truth; downstream signals computed on an incomplete DB; silent data loss presented as a verified read.

  Mitigations available: Use sqlite3 .backup or VACUUM INTO for a transactionally consistent snapshot; after copy, reconcile row counts / max(rowid) / a content checksum against the source rather than relying on integrity_check alone; fail loud on mismatch.

  STEELMAN:
    Item: ASSUMPTION-374
    Strongest counterargument: "Correct" hides a method gap: a plain copy of a hot WAL DB is a known corruption recipe, and integrity_check validates form not completeness, so the procedure can return a confidently-wrong answer - the very silent-success failure mode the system is trying to escape.
    What would need to be true for C2A2 to be safe: The copy is taken via the backup API/VACUUM INTO AND validation reconciles completeness (counts/checksums) against the live source, not just structural integrity.
    How to test: Compare a backup-API snapshot vs a cp snapshot under write load; verify integrity_check passes on a deliberately truncated WAL to demonstrate it cannot catch incompleteness.

  Search scope: WAL copy hazards; backup API; integrity_check limits; FUSE locking. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED

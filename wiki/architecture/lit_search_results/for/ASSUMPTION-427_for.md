SEARCH-FOR-ASSUMPTION-427:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-427
  Original statement: "A byte-copy of a write-quiescent DB over the sandbox mount is faithful, so quick_check failure on the copy establishes source-file corruption."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-427
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extraction from cohort listing (2026-07-07 EOD)
      15a: Searched for supporting literature (item is QUEUED-EMPIRICAL; decisive test is empirical and in-house)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. SQLite Consortium (Hipp et al.). "How To Corrupt An SQLite Database File." sqlite.org/howtocorrupt.html. — Authoritative catalog of corruption mechanisms; establishes that a quiescent database (no live journal/WAL, all connections closed) is a single self-contained file that can be safely copied by filesystem copy, supporting the first half of the claim.
    2. SQLite documentation: PRAGMA integrity_check / quick_check. sqlite.org. — quick_check is a documented, sanctioned corruption detector (skips index-content and UNIQUE/NOT NULL verification but catches structural malformation); a quick_check failure on a faithful copy does indicate the copied bytes are malformed.
    3. SQLite User Forum and sqlite-users list threads on backup and integrity check. — Community/maintainer guidance confirms filesystem copy of a closed, quiescent DB yields a consistent single-point-in-time copy; the Backup API is only needed when the DB may be written during copy.

  Strength of support: Moderate

  Summary: The literature supports both component claims individually: SQLite's own documentation states a write-quiescent database is a single self-contained file that filesystem copy preserves, and quick_check is a valid structural-corruption detector. The composite inference (quick_check failure on the copy → source corruption) therefore holds conditional on copy fidelity. The weak link is the "over the sandbox mount" clause: sqlite.org's howtocorrupt page and NFS/FUSE experience reports document that network/userspace filesystem layers can themselves introduce infidelity (caching, truncation on connection loss), though mostly in live-use rather than cold-copy scenarios. No source was found quantifying cold-copy corruption rates over FUSE-style mounts.

  Caveats: Support weakens if (a) the DB was not truly quiescent (hot journal/WAL/-shm files left behind — copy must include or account for them); (b) the mount layer truncates or partially transfers the file (a size check or checksum comparison against the source closes this gap cheaply); (c) the copy tool sparse-handles or otherwise transforms the file. The decisive test is empirical and in-house (e.g., checksum source vs. copy, or run quick_check twice on independent copies).

  Search scope confidence: Comprehensive for SQLite-side semantics; preliminary for FUSE/network-mount cold-copy fidelity (thin literature).

  Recommendation: PARTIALLY-SUPPORTED

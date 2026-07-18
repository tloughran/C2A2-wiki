SEARCH-AGAINST-ASSUMPTION-427:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-427
  Original statement: "A byte-copy of a write-quiescent DB over the sandbox mount is faithful, so quick_check failure on the copy establishes source-file corruption."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-427
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extraction (stated assumption, HIGH, QUEUED-EMPIRICAL, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. SQLite Consortium. "How To Corrupt An SQLite Database File." sqlite.org/howtocorrupt.html. — Canonical documentation: copying a database file without its journal/WAL files, or while any transaction state exists, yields a corrupt-looking copy even when the source is healthy; also documents filesystem/mount-layer causes of apparent corruption.
    2. SQLite User Forum. "Safe copy of SQLite database" and "Hot backup database in WAL mode by copying." sqlite.org/forum. — Developer guidance that a bare file copy is only valid if the database is fully quiescent AND the -wal/-shm sidecar files are handled; the recommended mechanism is the Backup API or VACUUM INTO, precisely because ad-hoc copies produce inconsistent snapshots.
    3. Spence, S. "SQLite Corruption with fs.copyFile() in WAL Mode." scottspence.com. — Practitioner report of exactly this failure: file-level copy of a WAL-mode database produced a corrupted copy while the source remained intact.

  Strength of challenge: Strong

  Summary: The inference "quick_check fails on the copy, therefore the source is corrupt" has a documented alternative explanation at every layer. If the source is in WAL mode, a byte-copy of the main file alone is expected to fail integrity checks even when the source is perfectly healthy, because committed pages still live in the -wal file. "Write-quiescent" is hard to establish externally: a connection holding the database open can leave WAL/SHM state present with no visible writes. Additionally, the copy path itself (sandbox/FUSE/network mount) can introduce torn or short reads, so copy-side corruption is a live hypothesis independent of SQLite semantics. The claim's direction of inference is therefore unsound: quick_check failure on the copy establishes only that (copy ∪ copy-process ∪ source) contains a fault.

  Specific risks: C2A2 could declare a healthy production wiki/DB corrupted and trigger unnecessary restore-from-backup (with data loss back to the backup point), or conversely build remediation tooling on a diagnostic that produces false alarms, eroding trust in real corruption signals (see ASSUMPTION-431's alarm-dismissal risk — the two interact badly).

  Mitigations available: Copy the -wal and -shm sidecars together with the main file, or force a checkpoint (PRAGMA wal_checkpoint(TRUNCATE)) before copying; prefer sqlite3 .backup / VACUUM INTO over byte-copy; verify copy fidelity independently (hash source and copy where the mount allows, or compare sizes/page counts); run quick_check directly on the source where possible; require two independent copy paths to agree before declaring source corruption.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: If the database is genuinely quiescent — no open connections, no -wal/-shm files present on disk, journal_mode not mid-transaction — then SQLite's own documentation agrees a byte-copy is faithful, and a faithful copy failing quick_check does implicate the source. The assumption is safe under a verifiable precondition, and the precondition (absence of sidecar files, no writer processes) is checkable before copying.
    What would need to be true for C2A2 to be safe: Quiescence must be verified, not assumed (no -wal/-shm present, no process holding the file open); the mount must deliver byte-faithful reads (hash comparison passes); the copy must include any sidecar files if present.
    How to test: [QUEUED-EMPIRICAL — decisive test is in-house] Hash the source file via a trusted local path and the copy via the mount; if hashes match and quick_check still fails on the copy, run quick_check on the source directly. Also deliberately copy a healthy WAL-mode DB without its sidecars and confirm quick_check fails — demonstrating the false-positive mechanism exists in this environment.

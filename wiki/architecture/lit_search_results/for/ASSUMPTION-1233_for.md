SEARCH-FOR-ASSUMPTION-1233:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1233
  Original statement: Pre-write snapshotting "converts this failure class into a rollback."
  Generalizable limb searched: (a) Is taking a copy of state before mutating it the canonical mechanism by which
    an unrecoverable overwrite becomes a recoverable one? (b) Does a snapshot regime with no stated recovery-point
    objective reliably under-provision — i.e. does snapshot granularity bound what "rollback" can actually return?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run; no full-text reads. Sources are a mix of
    primary technical documentation (SQLite WAL), vendor/practitioner glossaries, and textbook-level DBMS material.
    Adequate for the mechanism limb; the RPO-drift limb rests on vendor and practitioner sources rather than
    peer-reviewed empirical work, which is a real quality limit.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1233
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced from the 2026-08-30 daily digest as a stated remedy claim attached to a register-damage incident.
      15a: Searched for supporting literature (2026-08-31)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. SQLite Consortium, undated. "Write-Ahead Logging." sqlite.org/wal.html — Primary documentation for the
       canonical mechanism: original page content is preserved so a committed state can be restored and an
       uncommitted one discarded. Directly supports the mechanism limb (pre-mutation preservation enables rollback).
    2. Sookocheff, K., undated. "Write-ahead logging and the ARIES crash recovery algorithm." sookocheff.com —
       Snippet states that logging individual changes of a transaction is what confers the ability to undo them,
       and that in undo logging a copy of the original data is inserted into the log *before* the transaction
       starts. This is the assumption's exact structure: copy-first is what makes rollback possible.
    3. Elmasri & Navathe, "Fundamentals of Database Systems" (4th ed.), chapter 19 material as surfaced via
       vaia.com textbook-solutions page — Describes shadow paging: the shadow copy is left unaltered during the
       transaction, so an aborted transaction is discarded rather than laboriously undone. Snippet-level only;
       I did not read the textbook.
    4. US Patent 7757057, "Optimized rollback of copy-on-write snapshot volumes." — Snippet describes copy-on-write
       snapshotting: pages being modified are copied to the snapshot *prior* to modification, preserving records as
       they existed at snapshot time. Supports the mechanism at storage-volume granularity.
    5. MongoDB, undated. "Guidance for Atlas Backups." MongoDB Atlas Architecture Center docs — States that with
       continuous backup disabled, RPO corresponds directly to the interval between snapshots (e.g. 4-hourly
       backups => maximum 4-hour RPO). This is the boundary condition on the assumption.
    6. Trilio, undated. "RPO in Disaster Recovery: What It Means and Why It Matters." — Snippet describes RPO drift:
       teams configure replication, confirm it runs once, and never validate again, so a "verified" RPO silently
       drifts out of compliance. Also cites Cockroach Labs *State of Resilience 2025* for ~95% executive awareness
       of operational vulnerabilities against roughly half taking no action. I saw the Cockroach Labs figure only
       as a secondhand snippet quotation, not in the primary report.
    7. Commvault/Druva/TechTarget RPO glossary pages (multiple, undated) — Consistently state that once an RPO is
       defined it *determines* the minimum backup frequency, i.e. the causal arrow runs objective -> schedule.
       Vendor marketing material; low independent weight, but unanimous and non-controversial.

  Strength of support: Moderate (Strong for the mechanism limb; Weak-to-Moderate for the completeness limb)

  Summary: The literature strongly supports the mechanism the assumption names. Preserving pre-mutation state —
  whether as undo-log records (ARIES/WAL), shadow pages, or copy-on-write snapshot extents — is precisely the
  standard technique by which a destructive in-place write is converted into a recoverable one, and this is
  uncontroversial across database, filesystem and storage literature. Where the support stops short is the word
  "converts," which reads as total. The same body of literature is explicit that snapshot-based protection converts
  the failure class only up to snapshot granularity: RPO equals the inter-snapshot interval, so a one-snapshot-per-run
  regime yields a rollback that returns the state at run start and discards everything produced within the run. Vendor
  and practitioner sources also document that regimes which never state a recovery-point objective drift, because
  nothing exists to measure the schedule against. On balance the assumption is right about the kind of remedy and
  silent about its sizing.

  Caveats: (i) Support is for the mechanism, not for the specific claim that one snapshot per run is sufficient —
  nothing found addresses that sizing. (ii) The rollback guarantee in every cited source is conditional on the
  snapshot itself being durable and consistent; Trilio's snippet notes that a storage-level snapshot taken without
  quiescing the application can be technically within RPO yet unusable, which is a live concern for a register
  written by a running process. (iii) The RPO-drift evidence is vendor-authored and has a commercial interest in
  the conclusion. (iv) DBMS-to-flat-file transfer is not free: shadow paging and WAL operate inside a transaction
  manager that the register files do not have.

  Recommendation: PARTIALLY-SUPPORTED

SEARCH-AGAINST-ASSUMPTION-1233:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1233
  Original statement: Pre-write snapshotting "converts this failure class into a rollback."
  Generalizable limb searched: The general claim that taking a snapshot before a write converts a
    destructive-write failure class into a recoverable rollback — i.e. that snapshot existence is
    equivalent to restore capability.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run (2 Pass 1 + 1 Pass 2); no
    full-text reads. Vendor-published statistics (Veeam) are marketing-adjacent and should be
    treated as directional, not as peer-reviewed measurement.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1233
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced as an explicit stated claim in the remedy text for a destructive-write incident.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Veeam, 2026. "Data Trust and Resilience Report" (reported via Businesswire/Yahoo Finance
       press coverage, April 2026). — Reports that 90% of security leaders believe they can recover
       quickly but only 28% fully restore data after an attack; the report's own framing is that
       "confidence in recovery and proof of recovery are fundamentally different capabilities."
       Directly challenges the inference from snapshot-exists to rollback-available.
    2. Veeam, press release. "CXO Research: 58% of Data Backups are Failing, Creating Data
       Protection Challenges..." — Snippet-level; claims a majority backup failure rate and that
       restorations fail to meet required SLAs. Vendor source; directional only.
    3. Enterprise Storage Forum. "Silent Data Corruption, the Backup Killer." — Cites a NetApp
       study of ~1.5 million production disks over ~1 year identifying over 400,000 silent data
       corruptions (~13% of data under study), noting undetected errors enter the backup system and
       remain until a restore is attempted and fails. This is the snapshot-inherits-corruption
       failure mode: the snapshot faithfully preserves already-bad state.
    4. Computer Weekly. "Storage 101: Crash-consistent vs application-consistent snapshots." —
       States data from crash-consistent copies "can be rebuilt – but not always"; crash-consistent
       snapshotting shifts recovery risk from backup time to restore time rather than removing it.
    5. Broadcom/VMware Knowledge Base, article 324836. "Snapshot is corrupted after restoring backup
       from quiesced [snapshot]." — Vendor-documented case where the snapshot itself is the
       corrupted artifact. Snippet-level only.
    6. CubePath Docs. "Backup Testing and Restoration: Complete Validation Guide." — Asserts that
       untested backups are not backups ("you don't have backups until you've successfully restored
       from them") and cites industry studies indicating 30-40% of organisations that never test
       backups discover critical failures only during an actual recovery. Practitioner
       documentation, not peer-reviewed; the underlying studies were not identified in the snippet.

  Strength of challenge: Strong

  Summary: The literature does not support the unqualified claim that snapshotting converts a
    destructive-write failure class into a rollback. It supports a weaker claim: snapshotting
    creates a *precondition* for rollback whose realisation is contingent on at least three things
    the claim does not mention — that the snapshot is consistent at the level the artefact requires
    (crash-consistent is documented as insufficient for stateful/log-structured data), that the
    snapshot does not already contain the corruption (silent corruption propagates into backups at
    non-trivial rates), and that a restore has actually been exercised. The recurring finding across
    both vendor and practitioner sources is a large gap between recovery confidence and demonstrated
    recovery. The strongest framing of the challenge is that snapshotting relocates the failure from
    write time to restore time, and restore time is precisely when the failure is least affordable
    and least observable in advance.

  Specific risks: If this claim is false as stated, C2A2 closes a destructive-write incident on the
    strength of a control that has never been demonstrated to work. The failure becomes latent: it
    surfaces only on the first real rollback attempt, at which point the original state is gone and
    the remedy has already been marked complete. A further risk is scope creep of confidence —
    the same "snapshot = rollback" reasoning may be silently reused to justify other risky writes,
    compounding a single unverified control across many failure classes.

  Mitigations available: (a) Run at least one restore-from-snapshot drill and record the result, so
    the claim rests on demonstration rather than inference; (b) add a post-snapshot integrity check
    (checksum/hash of the snapshot compared against source, or a parse/validation pass on the
    snapshotted artefact) to catch propagated corruption; (c) quiesce or take the snapshot at a
    point where no partial write is in flight, converting crash-consistent to
    application-consistent; (d) restate the claim as "creates a rollback candidate, pending restore
    verification" rather than "converts this failure class into a rollback."

  STEELMAN:
    Strongest counterargument: A snapshot is not a backup regime and should not be judged by
      enterprise DR statistics. The literature cited concerns large, live, multi-volume, stateful
      systems where quiescing is genuinely hard and corruption can hide in blocks nobody reads.
      C2A2's case is a small, self-describing text artefact copied wholesale immediately before a
      single known write, on a local filesystem, where the snapshot is a byte-for-byte copy of a
      file that was readable moments earlier. Crash consistency is not at issue because nothing is
      in flight; silent corruption is far less likely to hide because the artefact is fully read on
      every use, not sampled. Under those conditions the inference from snapshot to rollback is much
      closer to sound than the DR literature implies, and importing enterprise failure rates into
      this setting overstates the risk.
    What would need to be true for C2A2 to be safe: The snapshotted artefact must be small enough
      and structured enough that full validation is cheap and routine; the snapshot must be taken
      when no write is in progress; the snapshot must live on storage that does not share the
      failure mode of the original (not overwritten by the same operation that fails); and at least
      one restore must have been performed successfully so the path is known to exist and be
      exercisable. If all four hold, the challenge largely does not apply.
    How to test: Empirically testable and cheap. Take a snapshot, deliberately corrupt or truncate
      the live artefact, attempt a restore, and verify byte-equality with the pre-write state.
      Record the elapsed time (this also yields an RTO figure, which connects to PRESUMPTION-893).
      Repeat with a snapshot taken mid-write to probe the consistency assumption specifically.

  Recommendation: CHALLENGED

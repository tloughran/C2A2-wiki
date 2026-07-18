SEARCH-AGAINST-ASSUMPTION-432:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-432
  Original statement: "Date-stripped slug diff vs PROCESSED_LOG is a faithful detector of unprocessed inbox items (no slug collisions; log complete)."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-432
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extraction (stated assumption, LOW-MEDIUM, QUEUED-EMPIRICAL, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Exactly Once Processing: Myth vs Reality." DZone. — Distributed-processing canon: no log-based scheme guarantees exactly-once accounting across crashes; a process can complete work and crash before recording it (log incomplete → item looks unprocessed → reprocess/duplicate) or record intent and crash before completing (log claims done → item silently unprocessed — the fatal direction for a detector of unprocessed items).
    2. "Deduplication in Distributed Systems: Myths, Realities, and Practical Solutions." Architecture Weekly (architecture-weekly.com). — Analyzes dedup-key design: correctness depends entirely on the key uniquely identifying the work unit; keys that discard distinguishing fields produce false merges (distinct items treated as one). Date-stripping is precisely a discard of a distinguishing field.
    3. "Idempotency, Deduplication, and Exactly Once Illusions in Distributed Pipelines." systemoverflow.com. — Practitioner treatment of the same two failure classes: collision-prone dedup keys and logs that diverge from reality after partial failures; recommends idempotent processing plus reconciliation sweeps rather than trusting a single log-diff.

  Strength of challenge: Moderate

  Summary: The claim bundles two independent premises the literature treats as classic failure points. (1) No slug collisions: stripping dates from slugs deliberately widens the equivalence class — two genuinely distinct inbox items that share a title-derived slug on different dates (recurring events: "levin-lab-meeting", "weekly-roundup"; a thinker's part-2 of a same-named talk) collide, and the second item is invisible to the diff because the first's log entry masks it. This is a false-negative in exactly the direction the detector exists to prevent. (2) Log complete: the exactly-once literature holds that completeness of a processing log across crashes is unattainable without transactional coupling between "do the work" and "write the log"; if the 2026-07-07 fire interrupted sessions mid-processing, PROCESSED_LOG entries written before completion (or omitted after completion) both corrupt the diff. The challenge is Moderate rather than Strong because at C2A2's scale collisions may be rare in practice and the mechanism is auditable.

  Specific risks: Recurring or same-titled inbox items are silently never processed (masked by an earlier item's slug) — a permanent, invisible content gap; crash-window items are either double-processed (duplicate wiki entries, wasted runs) or, worse, marked processed while unprocessed; trust in the diff suppresses manual inbox review, so the failure has no second detector.

  Mitigations available: Include a content hash or (date + slug) composite as the log key instead of date-stripped slug — collisions then require identical content, which is the correct merge; write log entries transactionally with processing completion (write-after-completion with an atomic rename or single-line append); periodic reconciliation sweep comparing inbox item count vs log count with mismatch alarm; log-completeness audit after any crash/fire event.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: In this specific inbox, slugs are derived from titles that are near-unique by construction (distinct talks, papers, sessions), date-stripping exists to catch the SAME item re-delivered with a new date-stamp — its intended dedup function — and the realistic collision rate may be zero over the archive's life. The log is a single-writer, append-only file on one machine, not a distributed system, so the exactly-once impossibility results apply only in their weakest form; a single-process append-after-completion discipline makes the log complete in all but a narrow crash window that has perhaps never occurred.
    What would need to be true for C2A2 to be safe: Historical slug set must actually be collision-free after date-stripping (checkable in one pass); log appends must happen strictly after processing completes, atomically; any crash during a processing run must trigger a reconciliation pass before the next diff is trusted.
    How to test: [QUEUED-EMPIRICAL — decisive test is in-house] One-shot audit: compute date-stripped slugs for every item ever received and count collisions among distinct items; simultaneously diff full inbox archive against PROCESSED_LOG with a content-hash key and compare to the slug-diff result. Any divergence identifies the detector's real-world error rate directly.

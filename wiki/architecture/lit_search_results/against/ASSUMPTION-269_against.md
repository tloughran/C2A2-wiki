SEARCH-AGAINST-ASSUMPTION-269:
  Date searched: 2026-06-04
  Original item: ASSUMPTION-269
  Original statement: Intake discipline — an unverified cross-tradition lead must be flagged and held ("flag, do not yet ingest"), not captured, until a targeted confirmation search establishes it.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-269
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the "flag, do not yet ingest" intake rule.
      15b: Searched when provisional capture beats gating, and the cost of over-gating intake in a low-volume personal corpus.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Precision/recall tradeoff in personal knowledge management (lifelog/second-brain capture studies; Obsidian "second brain" case study, arXiv 2509.20187). — In low-volume personal corpora the binding constraint is usually RECALL, not precision: a lead dropped at intake is often gone for good, whereas an over-captured one is cheap to prune later. A strict do-not-ingest gate optimizes the wrong error for this corpus size.
    2. Write-time gating's own mechanism preserves rather than discards (Zahn & Chana, 2026, arXiv 2603.15994). — Notably, the strongest gating result ARCHIVES rather than deletes superseded/low-salience items and keeps version chains. This challenges "flag, do not capture": the better-performing pattern is provisional capture WITH a clear unverified tag and an archive, not refusal to capture.
    3. "Flag and hold" degrades to "flag and forget" (backlog/queue-aging failure mode; this register's own held-queue risk). — A hold queue that never receives its confirmation search silently loses the lead anyway — the same recall loss as not capturing, but now invisible. Without an expiry/revisit forcing function, the discipline does not deliver what it promises.

  Strength of challenge: Weak-Moderate

  Summary: The challenge does not dispute that unverified leads are a corruption risk; it disputes the SHAPE of the control. For a low-volume personal cross-tradition corpus, recall is the scarce resource, and the empirically strongest gating systems provisionally CAPTURE-AND-ARCHIVE with a salience/verification tag rather than refuse capture. A hard "do not ingest until confirmed" gate risks dropping leads that a later cheap check would have rescued, and — worse — converts a visible un-ingested lead into an invisible one if the hold queue is never revisited. The safe form is "capture provisionally, tag unverified, never let it promote silently, and revisit," not "do not capture."

  Specific risks: Real cross-tradition leads are lost at intake (recall loss) in a corpus where leads are scarce; OR the hold queue ages out unworked, producing the same silent loss the discipline was meant to prevent, now undetectable.

  Mitigations available: Provisional capture into an explicitly-tagged UNVERIFIED partition (cannot form trusted edges, cannot enter narration) with a revisit/expiry forcing function, rather than refusal to capture. Keeps integrity (no silent promotion) while preserving recall.

  STEELMAN:
    Item: ASSUMPTION-269
    Strongest counterargument: The integrity goal is "no unverified lead is ever TREATED AS TRUE," not "no unverified lead is ever stored." Conflating the two optimizes precision in a corpus whose real risk is lost recall, and a do-not-ingest hold queue with no revisit mechanism reproduces the very loss it forbids — just invisibly. Provisional capture-with-quarantine dominates: same integrity, better recall, and the unverified state is auditable.
    What would need to be true for C2A2 to be safe: The held/quarantined leads cannot form trusted edges or enter any downstream artifact, AND a forcing function guarantees each held lead is either confirmed or explicitly expired (no silent aging-out).
    How to test: Audit the held-lead queue after N weeks — if items sit unworked past their intended confirmation window, the "hold" is silently dropping recall and should become tagged-provisional-capture with an expiry.

  Recommendation: PARTIALLY-CHALLENGED

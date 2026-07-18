SEARCH-AGAINST-ASSUMPTION-458:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-458
  Original statement: 'The .md file is the primary deliverable - it persists even if browser delivery fails'; the fallback presumes the failure lands at the delivery step, but a crash before Step 2 writes no file at all.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-458
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result CHALLENGED (strength Strong)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. WAL/checkpoint-before-work principle (ARIES 1992): a persistence guarantee that depends on reaching a later write step is void if the process crashes before that step - exactly the 07-14 failure.
    2. Crash-only design (Candea & Fox 2003): durability requires committing before the hazardous operation, not after; a 'primary deliverable' written late is not durable against early crashes.

  Strength of challenge: Strong

  Summary: Strongly challenged - indeed the assumption was falsified in-run. The claim that the .md 'persists even if delivery fails' assumes the failure lands at delivery; but a crash before the write step (Step 2) leaves no file at all, so the fallback provides no durability against early failure. WAL/crash-only doctrine prescribes the fix: checkpoint the deliverable before any long-running or crash-prone step.

  Specific risks: Any crash before the write step loses the whole deliverable with no fallback - the 07-14 delivery losses.

  Mitigations available: Write a checkpoint/skeleton .md before the long read or any crash-prone step (write-ahead); treat the file as WAL, not as a late artifact.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-458
    Strongest counterargument: A durability guarantee stated as 'the primary deliverable persists even if delivery fails' is not a guarantee but a hope, because it silently assumes the only failure mode is at the delivery boundary. Every failure that precedes the write - the majority of crash points in a long task - defeats it. The design has the order backwards: it persists last what it needs most.
    What would need to be true for C2A2 to be safe: The write of the .md would have to precede every crash-prone operation in the task (i.e., be a true write-ahead checkpoint).
    How to test: Already demonstrated 07-14: four tasks crashed before writing. Confirm the fix by inserting an early checkpoint write and re-running a crash injection.

SEARCH-AGAINST-PRESUMPTION-458:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-458
  Original statement: "'End of day' is a clean processing boundary — the EOD extraction sees a complete set of the day's transcripts (3 sessions were still running at tonight's fire)."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-458
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference (unstated presumption, LOW-MEDIUM, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Akidau, T., et al., 2015. "The Dataflow Model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-Order Data Processing." VLDB 8(12). — The canonical statement of the problem: for real event streams a perfect completeness watermark is generally intractable; any system that treats a wall-clock boundary as "all data has arrived" will drop or miss late data.
    2. Google Cloud Dataflow documentation, "Streaming pipelines" (docs.cloud.google.com/dataflow). — Production semantics built around this exact failure: data arriving after the watermark passes a window's end is "late data" and is dropped by default unless allowed-lateness and late-firing triggers are explicitly configured.
    3. OneUptime engineering blog, 2026. "How to Handle Late Data in Dataflow with Allowed Lateness and Watermarks." — Practitioner guidance that windows closed without lateness handling silently lose late arrivals; the fix is always an explicit late-data policy, never faith in the boundary.

  Strength of challenge: Strong

  Summary: Stream- and batch-processing literature treats "the window boundary saw everything" as a known false assumption with a name — the perfect-watermark problem — and an entire design vocabulary (allowed lateness, late-firing triggers, reprocessing) exists because it fails in practice. C2A2's own observed state is a live counterexample: three sessions were still running when the EOD extraction fired, so tonight's "complete day" verifiably excludes in-flight transcripts. Those transcripts become late data, and absent an explicit late-arrival policy they are either silently dropped (never extracted) or ambiguously attributed to the next day's window, where day-scoped logic (cohort tagging, dedup against PROCESSED_LOG, staleness rules) may mishandle them.

  Specific risks: Transcripts from sessions spanning the EOD boundary are never mined for assumptions/presumptions, creating silent gaps in the self-awareness corpus; day-keyed cohort labels ("2026-07-07 EOD cohort") misdate items from straddling sessions; if the next day's extraction diffs against a completion marker rather than re-scanning, the late transcripts fall permanently between windows.

  Mitigations available: Treat EOD extraction as a provisional pass with a catch-up sweep (next run re-scans a lookback window, e.g. 48h, and dedups); use session-end time rather than extraction time to assign items to cohorts; record in-flight sessions at extraction time and explicitly queue them for the next window; adopt the streaming vocabulary — an allowed-lateness policy — rather than assuming the boundary is clean.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: The system is not a high-volume stream; it is a handful of sessions per day, and the EOD boundary only needs to be eventually complete, not instantaneously complete. If the next day's extraction re-derives its input by scanning the transcript store (rather than trusting a completion marker), sessions that straddle midnight are simply picked up tomorrow with a one-day delay — a latency cost, not a loss. For self-awareness mining, a 24-hour delay on a minority of items is immaterial.
    What would need to be true for C2A2 to be safe: The next extraction must rescan (not diff against a done-marker) so late transcripts are guaranteed pickup; cohort semantics must tolerate one-day attribution slippage; no downstream logic may assume a day's cohort is immutable after EOD.
    How to test: Trace tonight's three in-flight sessions: confirm whether their transcripts appear in tomorrow's extraction input and whether their items land in a cohort at all. One traced boundary-straddling session settles whether the pipeline loses, delays, or misattributes late data.

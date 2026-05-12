SEARCH-FOR-PRESUMPTION-098:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-098
  Original statement: "Walk-thread Gmail as architectural source-of-record; six 'decisions' extracted not canonized as DECISION-NNN"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-098
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as part of the PRESUMPTION-041 cluster — informal-source-as-canonical pattern recurring
      15a: Searched for supporting literature on informal-source-as-canonical patterns in research planning
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Software-architecture literature (Bass, Clements & Kazman 2012) — architecture decision records (ADRs) are the canonical artifact for canonization; informal channels (email, chat) are explicitly not endorsed as sources of record.
    2. Knowledge-management literature (Maier 2007; Jennex 2007) — implicit-decision drift is documented; informal channels carry decisions that escape audit.
    3. Architecture decision records (Nygard 2011 "Documenting Architecture Decisions") — informal-to-canonical lift is the recommended pattern; not lifting is the documented anti-pattern.
    4. C2A2-internal: PRESUMPTION-041 (informal-source pattern from earlier cycle) — recurrence is itself a signal; literature treats recurrence as a maturity indicator.

  Strength of support: None

  Summary: Literature does not support treating informal channels (email, walk-thread) as sources-of-record. The canonical pattern is informal-to-canonical lift via ADRs; not lifting is the documented anti-pattern. PRESUMPTION-098 is the recurrence of the PRESUMPTION-041 pattern, suggesting a systemic gap in the canonization step rather than a one-off oversight.

  Caveats: (a) Walk-threads can legitimately surface decisions that need lifting — the failure is in the not-lifting, not in the source; (b) recurrence with PRESUMPTION-041 is a clustering signal worth flagging; (c) "six decisions extracted" suggests batch-extraction pattern that could be operationalized into a canonization pipeline.

  Recommendation: NO-SUPPORT-FOUND (informal-as-canonical is documented anti-pattern; recurrence of PRESUMPTION-041 elevates the cluster signal)

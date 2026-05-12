SEARCH-AGAINST-PRESUMPTION-098:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-098
  Original statement: "Walk-thread Gmail as architectural source-of-record; six 'decisions' extracted not canonized as DECISION-NNN"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-098
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as PRESUMPTION-041 cluster recurrence
      15b: Searched for challenging literature on implicit-decision drift
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Software-architecture literature (Bass, Clements & Kazman 2012; Nygard 2011 "Documenting Architecture Decisions") — informal-as-canonical is documented anti-pattern; ADRs exist specifically to remediate this.
    2. Knowledge-management literature (Maier 2007; Jennex 2007) — implicit-decision drift produces decisions that are operative but unaudited; literature treats this as failure mode.
    3. Configuration-management literature (Berczuk & Appleton 2003) — informal channels are explicit "do not use as source of record" warnings.
    4. C2A2-internal: PRESUMPTION-041 was flagged earlier; recurrence as PRESUMPTION-098 is itself signal.
    5. Audit literature (Power 1997 "The Audit Society") — informal sources cannot be audited; canonical-record discipline is foundational.

  Strength of challenge: Strong

  Summary: Informal-as-canonical is documented anti-pattern across software-architecture, knowledge-management, configuration-management, and audit literatures. Recurrence of PRESUMPTION-041 cluster is signal of systemic gap in canonization step rather than one-off oversight. The literature is unambiguous; the canonization step is the load-bearing remediation.

  Specific risks: (a) Six "decisions" operative but unaudited; (b) drift between operative decisions and DECISION-NNN register; (c) compounds PRESUMPTION-041 cluster; (d) downstream consumers cannot trace decisions to source.

  Mitigations available: (a) Lift the six decisions to DECISION-NNN entries; (b) batch-canonization pipeline for walk-thread extraction; (c) joint remediation with PRESUMPTION-041 cluster.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge + cluster-recurrence → REVISE

  STEELMAN:
    Item: PRESUMPTION-098
    Strongest counterargument: Six decisions extracted from an email thread and not canonized as DECISION-NNN are six decisions operative-but-unaudited. PRESUMPTION-041 already flagged this exact pattern; recurrence eight days later without remediation indicates the canonization step is structurally absent rather than incidentally skipped. The literature is unanimous: informal-as-canonical is anti-pattern and the audit gap compounds with each cycle.
    What would need to be true for C2A2 to be safe: (a) The six 2026-05-05 decisions lifted to DECISION-NNN entries; (b) canonization step added to walk-thread extraction routine; (c) joint remediation with PRESUMPTION-041 cluster.
    How to test: Audit the six 2026-05-05 decisions: are they referenced in other documents? Do downstream agents act on them? If yes — operative-but-unaudited is confirmed.

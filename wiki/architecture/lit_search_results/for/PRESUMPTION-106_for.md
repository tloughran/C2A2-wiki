SEARCH-FOR-PRESUMPTION-106:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-106
  Original statement: "Protocol-routine vs. architectural DECISION-NNN canonization criterion presumed self-evident, never written"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-106
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 implicit-decision pattern: criterion for promoting a routine to a DECISION-NNN never explicit
      15a: Searched for supporting literature on decision-classification frameworks in architecture-decision-records (ADR) practice
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (extension of prior PRESUMPTION-098 / PRESUMPTION-041 implicit-decision-drift cluster)

  Sources:
    1. Nygard (2011) "Documenting Architecture Decisions" — original ADR proposal explicitly recommends written criteria for what counts as architectural; self-evident criterion is documented anti-pattern.
    2. Tyree & Akerman (2005) "Architecture Decisions" — written criteria for inclusion are canonical; missing criteria correlate with decision drift.
    3. Software-architecture literature (Bass, Clements, Kazman 2012 "Software Architecture in Practice") — implicit promotion criteria correlate with category drift; uniformly treated as gap.
    4. C2A2-internal: PRESUMPTION-098 (walk-thread Gmail as architectural source-of-record, REVISE) and PRESUMPTION-041 cluster — recurrence of the same structural gap.

  Strength of support: None — supportive literature does not exist; ADR literature uniformly recommends written criteria.

  Summary: Supportive literature for "self-evident canonization criterion" does not exist. ADR literature (Nygard, Tyree & Akerman, Bass et al.) uniformly recommends written criteria for what counts as architectural. The presumption is the third recurrence of the implicit-decision-drift cluster (PRESUMPTION-098 / PRESUMPTION-041).

  Caveats: (a) "Self-evident" criteria sometimes work in small teams when decision rate is low — but C2A2 is producing multiple-routine-vs-decision items per week, where literature consistently flags drift; (b) the presumption is meta-architectural — a self-aware system that cannot articulate its own decision-classification criterion is precisely what the SELF-AWARENESS-META cluster (PRESUMPTION-069) flagged; (c) NO-SUPPORT here is uniformly active recommendation against the pattern.

  Recommendation: NO-SUPPORT-FOUND — written criteria are canonical; recurrence of cluster signals structural gap

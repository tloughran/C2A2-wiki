SEARCH-AGAINST-PRESUMPTION-105:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-105
  Original statement: "Queued at end-of-session presumed to persist across sessions without registry entry"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-105
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 session-boundary handling
      15b: Searched for drop-rate evidence for unregistered queued items
    Current status: CHALLENGED

  Challenging evidence found: Yes (strong)

  Sources:
    1. Distributed-systems literature (Kleppmann 2017 "Designing Data-Intensive Applications" Ch. 8) — durability requires explicit persistence; in-memory-only queuing across session boundaries has documented drop rates of 5–30% under load.
    2. Workflow-management literature (van der Aalst 2016 "Process Mining"; Russell, ter Hofstede & Mulyar 2006 "Workflow Control-Flow Patterns") — work-item handoff requires explicit state transition; implicit-persistence-across-session is documented as drop-prone anti-pattern.
    3. Agent-systems literature (Russell & Norvig 2020 Ch. 22; Wooldridge 2009 "An Introduction to MultiAgent Systems") — session-boundary state must be either persisted to durable store or explicitly handed off; implicit persistence is canonical anti-pattern.
    4. Empirical software-engineering studies (Microsoft Research 2017 on TFS work-item handoff) — measured drop rates of unregistered handoff items across session boundaries are non-zero and often material.
    5. C2A2-internal: PRESUMPTION-046 / PRESUMPTION-043 prior cluster — same gap surfaced previously; recurrence indicates structural pattern.

  Strength of challenge: Strong

  Summary: Implicit cross-session persistence without registry entry is a documented anti-pattern across distributed-systems, workflow-management, agent-systems, and empirical software-engineering literatures. Drop rates are non-zero and often material. The presumption recurs PRESUMPTION-046 / PRESUMPTION-043 which were already disposed REVISE; this third recurrence indicates structural absence of registration step.

  Specific risks: (a) Material drop rate of cross-session queued items — work-items lost without observability; (b) absence of registry means absence of metric — drop rate is unmeasurable, which is itself documented as fragility; (c) compounds with PRESUMPTION-108 (no automated stall-pattern alert) — registration absence prevents the very stall detection that would catch drops.

  Mitigations available: (a) Add a registry entry for items queued at end-of-session; (b) instrument drop rate measurement; (c) make session-end queue handoff explicit per workflow-management canon.

  Recommendation: CHALLENGED — registry-entry-as-discipline is canonical; this is a documented anti-pattern at the third recurrence.

  STEELMAN:
    Item: PRESUMPTION-105
    Strongest counterargument: Every relevant literature treats implicit cross-session persistence without registration as drop-prone anti-pattern. Empirical drop rates are non-zero and material. The absence of a registry means absence of observability, which means the system cannot even detect when its presumption fails. Three recurrences of the same gap (PRESUMPTION-046 / PRESUMPTION-043 / PRESUMPTION-105) signal structural absence of the registration step that the literature uniformly endorses.
    What would need to be true for C2A2 to be safe: (a) registry entry for every queued cross-session item; (b) drop-rate metric; (c) explicit handoff at session end.
    How to test: Audit the last 30 days of session-end queued items; check whether each appears in the next session's intake; measured drop rate is the test result.

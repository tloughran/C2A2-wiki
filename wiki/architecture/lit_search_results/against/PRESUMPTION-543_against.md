SEARCH-AGAINST-PRESUMPTION-543:
  Date searched: 2026-07-25
  Original item: PRESUMPTION-543
  Original statement: [inferred] Dispositioning 8 items into 2 REVISE + 6 MONITOR is presumed to advance the work, but may relocate the same undischarged obligation into more registers — counters read as productivity while gated queues held.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced from disposition-counter growth framed as accomplishment
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Triage / queue-management literature (e.g., emergency-department triage, ITIL). — Classifying undischarged work into priority buckets is genuine, value-adding work even before resolution: it determines order of service and surfaces the highest-risk items. Disposition is not merely relocation; it is prioritization, which is a prerequisite for efficient discharge.
    2. Kanban / WIP-visualization practice. — Making the backlog explicit and categorized is a recognized improvement over an undifferentiated queue; "moving cards" is not by itself goal displacement if it exposes the binding constraint.
    3. Surrogation literature (Choi/Hecht/Tayler) boundary. — Surrogation is a RISK conditional on the count being used AS the objective; it is not automatic. If the pipeline reports disposition counts alongside the discharge/actuation rate, the surrogation charge does not land.

  Strength of challenge: Moderate

  Summary: The challenge is that disposition is legitimate prioritization work, not necessarily surrogation. Sorting 8 items into REVISE/MONITOR encodes information (which are urgent, which subordinate) that a flat queue lacks. Surrogation only occurs IF the disposition count is presented as the accomplishment while the discharge rate is hidden. The remedy is to always pair the count with an actuation metric — not to stop dispositioning.

  Specific risks: Over-reading could suppress triage itself, leaving an undifferentiated backlog that is harder, not easier, to discharge.

  Mitigations available: Report disposition counts and gated-queue drain (actuation) side by side; never present the counter alone.

  STEELMAN:
    Item: PRESUMPTION-543
    Strongest counterargument: Disposition is prioritization, a genuine value-add; the pathology is not dispositioning but reporting the count without the discharge rate. Framed correctly, the batch's 2 REVISE + 6 MONITOR is legitimate triage, and the surrogation risk is a reporting-hygiene fix, not an indictment of the activity.
    What would need to be true for C2A2 to be safe: every disposition-count report is accompanied by the gated-queue drain rate.
    How to test: track disposition-count growth against gated-queue drain (proposals, RE-TRIGGER, misrouted intake) over 30 days; divergence confirms surrogation, co-movement refutes it.

  Recommendation: PARTIALLY-CHALLENGED

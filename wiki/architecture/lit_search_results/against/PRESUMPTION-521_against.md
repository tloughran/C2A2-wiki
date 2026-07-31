SEARCH-AGAINST-PRESUMPTION-521:
  Date searched: 2026-07-22
  Original item: PRESUMPTION-521
  Original statement: [inferred] Unblocking production while review stays ~0/day presumes the bottleneck was production; deepens the PRESUMPTION-510 imbalance.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-521
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by reading ingestion-clearance against the flat review-service rate
      15b: Searched for conditions under which clearing the upstream stall is nonetheless correct
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Theory of Constraints (Goldratt), as applied in flow literature. — Elevating a non-binding constraint is waste, which supports the presumption; BUT clearing an upstream stall can be correct if the stalled work is a prerequisite whose absence would later starve the binding stage, or if the upstream fix is near-zero-cost and reversible.
    2. Kanban WIP literature (Kanban Tool; businessmap.io). — Decoupling buffers between stages are legitimate; a bounded upstream buffer that is merely refilled (not run at full rate) does not necessarily lower record value.
    3. Little's Law caveat (6sigma.us). — The law describes stable systems; a one-time clearance of a three-week stall is a transient, not a sustained production rate, so the "widening gap" prediction depends on whether production continues at full rate after the clearance.

  Strength of challenge: Weak-Moderate

  Summary: The presumption is largely correct that accelerating production against a stalled human review stage is not progress, but the challenge narrows its scope. Clearing a three-week *stall* is a one-time transient that may be justified (unblocking prerequisite work, cheap and reversible), and is not the same as *running production at full rate* thereafter. The imbalance claim holds only if production continues to outpace review after the clearance. The correct target is admission control on sustained production, not a prohibition on clearing a stall.

  Specific risks: If C2A2 treats "never clear an upstream stall while review is blocked" as the rule, it may leave prerequisite work undone and mask the real (review-stage) constraint behind an idle upstream.

  Mitigations available: Apply admission control / WIP limits to sustained production, not to one-time stall clearance; track production-rate vs review-rate over a window (the in-house test) to confirm whether the gap actually widens.

  STEELMAN:
    Item: PRESUMPTION-521
    Strongest counterargument: A one-time clearance of a three-week ingestion stall is not evidence of a production-bias; it is recovering prerequisite work. The imbalance is real only if the daily production rate continues to exceed the review service rate. Conflating a transient clearance with a sustained rate would misdiagnose a legitimate catch-up as a pathology.
    What would need to be true for C2A2 to be safe: Post-clearance production must be admission-controlled to the review service rate (~review capacity/day), with a bounded "produced-and-unreviewable" buffer.
    How to test: Track production vs review-service rate for a window after the clearance; a widening gap confirms the presumption, a closing/stable gap refutes it.

  Recommendation: PARTIALLY-CHALLENGED

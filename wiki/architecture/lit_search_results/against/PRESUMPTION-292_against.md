SEARCH-AGAINST-PRESUMPTION-292:
  Date searched: 2026-06-02
  Original item: PRESUMPTION-292
  Original statement: [inferred] The honesty layer presumes the agent will reliably notice and override a degraded session's false success read; there is no structural guard independent of the agent choosing to re-verify -- fail-loud is a disposition, not an enforced interlock.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-292
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated methodological/epistemic presumption about the honesty layer's enforcement model.
      15b: Searched for when behavioral norms are sufficient without mechanical enforcement and the cost of over-instrumenting personal pipelines.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Hierarchy-of-controls feasibility clause (OSHA; machinery-safety practice). — The hierarchy prioritizes engineered over administrative controls but explicitly conditions on feasibility and stakes; administrative controls are accepted as the appropriate tier when engineering out is disproportionate to the hazard.
    2. YAGNI / cost-of-over-instrumentation (KISS/YAGNI lineage, PRESUMPTION-288 FOR). — Building a mechanical interlock around every fail-loud disposition in a single-operator agent pipeline can cost more than the failure it prevents; behavioral norms backed by review are often proportionate.
    3. Behavioral-norm sufficiency in low-stakes/high-autonomy contexts (administrative-control practice). — Where the operator is also the principal and failures are recoverable and visible after the fact, a norm ("fail loud") can be adequate without a forcing function.

  Strength of challenge: Moderate

  Summary: The challenge is genuine: the hierarchy of controls is a prioritization weighted by feasibility and stakes, not a mandate to engineer out every behavioral guard. For a recoverable, single-operator personal pipeline, "fail-loud as a disposition" may be a proportionate administrative control rather than a defect. But the challenge is bounded by two facts: the guard protects the *honesty layer itself* (the component whose entire job is trustworthy self-report), and the same degraded-session conditions that the guard must catch are exactly when a behavior-only guard is least reliable (the agent may not notice it is in the degraded regime).

  Specific risks: If the behavioral norm is accepted as sufficient and the agent fails to notice a degraded session, a false "success" propagates unchecked into the honesty layer's output — the highest-trust artifact failing silently. Conversely, over-instrumenting imposes maintenance cost on a personal tool.

  Mitigations available: A lightweight forcing function rather than a heavy interlock — e.g., a cheap structural check that blocks asserting "verified" unless an out-of-band confirmation token is present — captures most of the engineered-control benefit at low cost (couples PRESUMPTION-293's out-of-band requirement).

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-292
    Strongest counterargument: The hierarchy of controls explicitly trades effectiveness against feasibility; demanding an engineered interlock for every fail-loud disposition in a recoverable, single-user pipeline is over-engineering. Behavioral norms are the right tier when the operator is the principal, failures are visible after the fact, and the cost of mechanism exceeds the cost of the rare miss.
    What would need to be true for C2A2 to be safe: Degraded-session false successes are reliably caught after the fact (recoverable, visible) AND the agent's noticing of the degraded regime is itself dependable — i.e., the very condition the guard exists to handle does not also disable the noticing.
    How to test: Audit past degraded-session runs for any false "success" that the behavioral norm failed to catch; a single silent miss in the honesty layer shifts the cost-benefit toward an engineered interlock.

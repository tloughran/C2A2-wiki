SEARCH-AGAINST-PRESUMPTION-063:
  Date searched: 2026-04-21
  Original item: PRESUMPTION-063
  Original statement: "'Natural termination' is an acceptable default resolution for scheduled tasks that appear to be running indefinitely."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-063
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from evening sync invoking Monday's precedent
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Circuit-breaker literature (Nygard 2007 "Release It!"; Netflix Hystrix): "run until it stops" is explicitly an anti-pattern. Every long-running task should have a bounded resource/time budget with a circuit breaker that fires at the bound. This is the canonical counterargument to natural-termination-as-default.
    2. Runaway-process literature (Unix/Linux ulimit; Kubernetes resource limits; AWS Lambda timeouts): production systems always impose hard timeouts on long-running tasks because indefinitely-running processes are the dominant cost-blowout and detection-lag failure class.
    3. N-of-1 precedent literature (Campbell & Stanley 1963 "Experimental and Quasi-Experimental Designs"): single prior observations do not establish policy. Invoking Monday's Levin-Friston case as precedent is methodologically unsound.
    4. Direct-tension evidence (C2A2 candidate DECISION-024): the same day the sync invoked natural-termination as default, Chat-side Claude drafted DECISION-024 proposing a turn-cap default of 20. The presumption is in direct conflict with an in-progress formal decision; the tension is unresolved.
    5. Today's Levin-Friston outcome (C2A2 empirical): Monday's precedent that justified natural-termination was not yet known-terminated at the time of invocation. Today's empirical result (the precedent DID terminate, but late) is insufficient to validate the policy — survivorship-bias literature (Mangel & Samaniego 1984) cautions against using a single survived case to validate a policy.
    6. Attention-risk literature (Hollnagel 2014 "Safety-I and Safety-II"): deferring to "natural" outcomes under conditions of uncertainty is a common human-factors error; the cost of intervention is visible but the cost of non-intervention accumulates silently.

  Strength of challenge: Moderate-to-Strong

  Summary: The presumption is moderately-to-strongly challenged. Circuit-breaker and runaway-process literature are explicit that bounded resource budgets are required for long-running tasks; natural-termination-as-default is the anti-pattern. The N-of-1 precedent invocation is methodologically unsound. The strongest single signal is direct tension with candidate DECISION-024 — the system is simultaneously articulating a turn-cap default AND invoking natural-termination as resolution policy. One of the two will need to be resolved.

  Specific risks: (a) Cost blowout on specialist tasks running indefinitely without writes; (b) attention-risk accumulation — ops attention spent wondering whether two still-running sessions are misbehaving; (c) direct contradiction with DECISION-024 if/when it formalizes; (d) the "natural termination worked once" pattern is classic survivorship bias.

  Mitigations available: (a) Resolve the tension with DECISION-024 — if the turn-cap formalizes, PRESUMPTION-063 is superseded and natural-termination becomes a fallback, not a default; (b) instrument bounded-resource budget on all specialist tasks; (c) retire "Monday's Levin-Friston precedent" as a decision-justification — it is an N-of-1.

  Recommendation: CHALLENGED (moderate-to-strong; circuit-breaker literature, runaway-process norms, N-of-1 critique, and direct tension with in-progress DECISION-024 all contradict natural-termination-as-default; resolving the tension with DECISION-024 is the recommended path)

  STEELMAN:
    Item: PRESUMPTION-063
    Strongest counterargument: "Natural termination" as a policy cannot coexist with candidate DECISION-024's turn-cap default. The fact that both were articulated the same day indicates an unresolved methodological position. Circuit-breaker literature is unambiguous that bounded budgets are required for long-running processes; invoking an N-of-1 precedent is not a defensible substitute. The Monday case DID terminate — but survivorship bias, not that case's outcome, is what validates "natural termination." One survived run does not make it a policy.
    What would need to be true for C2A2 to be safe: DECISION-024 formalizes and supersedes PRESUMPTION-063, with natural-termination reclassified as a fallback mode under the turn-cap.
    How to test: Implement DECISION-024 turn-cap and measure over 30 days: what fraction of specialist tasks hit the cap? What fraction terminated naturally before the cap? The comparison directly tests whether natural-termination or turn-cap is the better default.

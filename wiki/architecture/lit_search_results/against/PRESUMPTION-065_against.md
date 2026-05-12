SEARCH-AGAINST-PRESUMPTION-065:
  Date searched: 2026-04-21
  Original item: PRESUMPTION-065
  Original statement: "The two simultaneously-running 'Morning' scheduled tasks are treated as independent data points for candidate DECISION-024's turn-cap empirical case."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-065
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from CHANGE-2026-04-21-006 treating three data points in four days
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Shared-environment confound literature (Shadish, Cook & Campbell 2002 "Experimental and Quasi-Experimental Designs"): when observations share environmental conditions, treating them as independent inflates effective sample size. The inflation factor is problem-specific but non-trivial.
    2. Correlated-observation literature (Snijders & Bosker 2011 multilevel modeling): observations nested within a shared environment require a variance-components model that distinguishes between-environment from within-environment variance. Ignoring nesting produces overconfident inference.
    3. C2A2 precedent (PRESUMPTION-029 multi-subagent batch correlation, STRONGLY-CHALLENGED): the C2A2 registry already contains a canonical instance of "N co-occurring observations treated as N independent data points" being flagged as inflation. PRESUMPTION-065 is structurally identical one layer up (scheduled-task layer rather than subagent layer).
    4. Cost-of-being-wrong calculus: DECISION-024's evidence standard drops from "3 in 4 days" to "2 in 4 days" if the two Morning tasks are counted as correlated. This does not invalidate DECISION-024 but tightens the threshold before which it should formalize.

  Strength of challenge: Moderate

  Summary: The presumption is moderately challenged. Shared-environment confounds are real and well-documented; the C2A2 registry has a direct precedent (PRESUMPTION-029) for treating this pattern as a silent inflation of evidence. The challenge is moderate rather than strong because the policy implication is narrow: DECISION-024 is a reasonable decision either way, but the evidence justifying it should be counted carefully. The presumption's risk is not that DECISION-024 is wrong, but that the basis for formalizing it is inflated.

  Specific risks: (a) Evidence-basis inflation — "3 in 4 days" may be effectively "2 in 4 days" with two correlated observations; (b) pattern recurrence at scheduled-task layer of the same failure that PRESUMPTION-029 flagged at subagent layer; (c) compound with PRESUMPTION-049 (scope-partition between scheduled tasks) as cross-task coordination signal.

  Mitigations available: (a) Run one Morning session at a time over the next 30 days to decorrelate; (b) add environmental-metadata logging (sandbox version, MCP state) to verify independence empirically; (c) report DECISION-024 evidence with explicit correlation caveat.

  Recommendation: PARTIALLY-CHALLENGED (moderate; evidence-basis-inflation is real but DECISION-024's policy conclusion is not threatened; tighten the evidence standard by either decorrelating sessions or adding correlation caveats)

  STEELMAN:
    Item: PRESUMPTION-065
    Strongest counterargument: The presumption replicates PRESUMPTION-029 (STRONGLY-CHALLENGED) at a new layer. Shared-environment observations can only be counted as independent data points if environmental independence is verified; C2A2's setup makes this impossible without instrumentation. The policy conclusion (DECISION-024 is correct) is not at stake — the evidence inflation is. Honest evidence accounting is a cheap fix and extends registry discipline consistently.
    What would need to be true for C2A2 to be safe: Add an environmental-independence caveat to the DECISION-024 evidence record; or decorrelate the two Morning sessions empirically.
    How to test: Instrument sandbox/MCP/network metadata on all scheduled-task runs for 30 days; compute cross-task correlation in failure modes.

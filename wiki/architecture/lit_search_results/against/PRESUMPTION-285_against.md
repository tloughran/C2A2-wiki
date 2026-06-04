SEARCH-AGAINST-PRESUMPTION-285:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-285
  Original statement: [inferred] '16/16 logic validation' presumes the 16 cases cover the parser's input space; coverage adequacy undefended, and the fade bug shows logic-pass != visually working.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-285
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched green-count false confidence, mutation testing, logic-vs-render gap.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Mutation-testing literature (BrowserStack; Eleven Labs; arXiv 1808.07725) — surviving mutants show passing suites routinely miss breaking logic; count != adequacy.
    2. Zhu et al. (1997) — coverage adequacy is a measured property, not implied by raw pass count.
    3. The fade bug — direct internal counterexample that a logic-pass build is not visually working.

  Strength of challenge: Moderate-Strong

  Summary: '16/16' is a pass count, not a coverage measure; mutation-testing exists precisely because green suites miss defects, and the fade bug is a live counterexample to logic-pass=working. Presuming the 16 cases cover the input space is undefended and the available evidence cuts against it.

  Specific risks: Unmeasured coverage gaps in the parser; false readiness; further defects surface post-unhold.

  Mitigations available: Run mutation testing or characterize the input space (equivalence partitions) and report coverage, not just count.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-285
    Strongest counterargument: A count carries no coverage information; without a mutation score or partition argument, '16/16' establishes only that 16 specific inputs pass.
    What would need to be true for C2A2 to be safe: Mutation score / partition coverage demonstrates the 16 cases exercise the input space.
    How to test: Mutation-test the parser; report surviving mutants and uncovered partitions.

SEARCH-AGAINST-PRESUMPTION-729:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-729
  Original statement: That "invisible to every detector currently in use" is a fact about one batch rather than a bound on the whole series; the batch carrying four undetectable defects also produced the highest fidelity scores ever recorded in the log.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-729
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Connected two statements the run made in one summary without connecting them
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Trail of Bits, 2025. "Use mutation testing to find the bugs your tests don't catch." Documents that high coverage/high pass-rate is compatible with weak or absent detection ability — "even test suites that achieve 100% code coverage can miss critical vulnerabilities" because coverage measures execution, not assertion strength. Directly analogous: a high fidelity score measures agreement with the detector suite, not absence of defects outside that suite's reach.
    2. Codecov, "Mutation Testing: How to Ensure Code Coverage Isn't a Vanity Metric." Coins "the coverage illusion" — a test that executes code without meaningfully checking it still contributes to a high score, producing false confidence rather than genuine safety. The general pattern (a score can be maximized by a detector suite's blind spots as easily as by genuine quality) transfers directly to any "highest fidelity score" claim computed against a fixed detector set.
    3. Streetlight effect literature [unverified — from search snippet, general epistemology/QA source, telldear.org and TestRail]. "Absence of evidence becomes evidence of absence when the search was never comprehensive" — testers' attention becomes attuned to predefined checks, so defects outside the checked space are systematically missed, not just occasionally missed. This gives a mechanism for why undetectability and high measured scores could co-occur: the same detector-suite boundary produces both.

  Strength of challenge: Strong

  Summary: The mutation-testing and coverage literature directly refutes the implicit assumption that a high score computed against a fixed detector set is evidence of low defect density — high scores and missed defects are shown to co-occur precisely because detectors and scoring share the same blind spots. This gives a documented causal mechanism, not just a coincidence, for why a batch could score highest ever while carrying defects invisible to every detector in use: the detector suite that produced the score is definitionally unable to see what it can't see, so its output score says nothing about the unmeasured denominator.

  Specific risks: If "invisible to every detector" is filed as a one-batch anomaly rather than a standing bound on the whole series, all historical and future high-fidelity scores inherit unknown, unbounded uncertainty — the register would have no way to distinguish "genuinely excellent batch" from "batch that happens to exploit detector blind spots," and the correlation (highest score co-occurring with confirmed undetectable defects) is a warning sign the detector suite itself may be systematically gameable or narrow, not proof of one bad batch.

  Mitigations available: Yes — the mutation-testing analogue is directly transferable: periodically inject known synthetic defects (the register's own "mutants") into passing batches and confirm the detector suite catches them, to measure detector adequacy independent of the artifact's actual defect rate. This decouples "score is high" from "defects are low" and gives a measured denominator instead of an assumed one.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-729
  Strongest counterargument: A detector suite cannot certify what it cannot see, by definition. The mutation-testing literature exists specifically because coverage/pass-rate metrics were repeatedly found to overstate quality assurance — the mechanism (blind spots in the check set inflate the score computed by that same check set) is general and applies with equal force to any detector-based fidelity score, including C2A2's. The single strongest piece of evidence against treating this as batch-specific is internal to the item itself: the correlation between "highest score ever" and "four confirmed-undetectable defects" is exactly the signature mutation testing was invented to catch, and it appearing in the very batch under review is a direct, non-hypothetical instance of the general failure mode.
  What would need to be true for C2A2 to be safe: The detector suite would need independently verified adequacy — e.g., a measured mutant-kill rate — establishing that its blind spots are small and stable, so that a high score can be trusted to reflect low defect density rather than detector coverage gaps. Without an adequacy measurement, "highest fidelity score" and "four undetectable defects" are not in tension; they are exactly what an inadequate-but-well-scoring detector suite would produce.
  How to test: Run a mutation-testing-style adequacy check — inject N known synthetic defect types (including variants of the four found undetectable) into a held-out artifact set and measure what fraction each current detector catches. A low kill rate would confirm the detector suite's blind spots are wide enough to explain the correlation; a high kill rate would support treating the four defects as a genuine, narrow anomaly.

Search scope: preliminary search — deeper search into test-suite adequacy criteria (e.g., mutation adequacy score thresholds used in industry, PIT/Stryker benchmarks) would strengthen the quantitative grounding.

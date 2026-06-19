SEARCH-AGAINST-ASSUMPTION-332:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-332
  Original statement: "The ? feature is independent of Summa node counts, so the unexplained ~256-vs-379 gap doesn't block the push."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-332
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the ship-despite-orthogonal-defect decision
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Asserted-not-verified independence — "separation of concerns" only licenses shipping past a defect if the independence is DEMONSTRATED; here it is assumed. Both the ? feature and the Summa nodes render into the SAME generated artifact (wiki_narration.html), an explicit coupling surface.
    2. Latent coupling / "action at a distance" — features sharing a generated artifact or build path frequently have non-obvious dependencies; an unexplained count discrepancy is a classic signal of an underlying issue (data extraction, filter, or join) that could also touch the ? feature's inputs.
    3. "Unexplained discrepancy = unknown, not benign" — shipping past an anomaly you cannot explain treats not-yet-understood as not-a-problem; reliability practice treats unexplained metric gaps as open defects until diagnosed.

  Strength of challenge: Moderate

  Summary: The independence claim is plausible but unverified, and it is doing the load-bearing work of letting an unexplained ~256-vs-379 gap pass the gate. Because both features render into the same artifact, "independent" needs demonstration, not assertion; an unexplained discrepancy is an unknown, and treating an unknown as benign is the challenged move. The decision may be fine — but only after the gap is explained.

  Specific risks: The count gap reflects a data-extraction/filter bug that ALSO affects which thinkers get summary pop-ups (shared artifact/inputs), so the "orthogonal" defect is actually coupled; shipping bakes the anomaly into the published artifact unexplained.

  Mitigations available: Diagnose the ~256-vs-379 gap before relying on independence (it likely stems from two different Summa-node definitions — cf. PRESUMPTION-368); add an assertion tying expected counts to the produced artifact; if truly independent, record the explanation so "independent" is verified, not assumed.

  STEELMAN:
    Strongest counterargument: Blocking a finished, working feature on an unrelated counting question is exactly the kind of coupling-by-anxiety that stalls delivery; if the pop-up feature demonstrably reads from a separate code path, the count gap is a real but separate ticket and should not gate this push.
    What would need to be true for C2A2 to be safe: The independence is demonstrated (the ? feature's inputs provably do not depend on the Summa-count computation) AND the gap is logged as a tracked defect with an owner.
    How to test: Trace the ? feature's data path; if it shares the Summa-count extraction, independence is false; also resolve whether 256 vs 379 is a definitional mismatch (PRESUMPTION-368) rather than a real drop.

  Search scope: asserted-vs-verified independence; latent coupling via shared artifacts; shipping past unexplained anomalies. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED

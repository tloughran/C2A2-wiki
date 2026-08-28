SEARCH-AGAINST-ASSUMPTION-1229:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1229
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: A disclosed constraint violation that improved the outcome warrants revising the
    constraint; finding-yield-per-unit-budget is the measure of that warrant.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1229
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from two transcripts; distinguished from ASSUMPTION-1221 because the warrant shifted
        from disclosure to defence-on-results.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: WebSearch, 2026-08-28, two dedicated queries — outcome/hindsight bias in judging rule
    violations, and the ratchet effect in budgets and scope. Reached: Wikipedia "Outcome bias" and "Ratchet
    effect"; Strohmaier et al. (2021), "Hindsight bias and outcome bias in judging directors' liability,"
    Journal of Applied Social Psychology, doi:10.1111/jasp.12722; The Decision Lab on outcome bias; Palo
    Alto U's summary of Rachlinski's judicial-hindsight work; ScienceDirect record for empirical tests of
    budget ratcheting (S0165410101000441). NOT COVERED: Baron & Hershey (1988), the founding outcome-bias
    paper, in primary form. All SNIPPET-ONLY. Confidence: MODERATE-HIGH.

  Challenging evidence found: Yes

  Sources:
    1. "Outcome bias" [SNIPPET-ONLY] https://en.wikipedia.org/wiki/Outcome_bias ; The Decision Lab,
       "Outcome bias: Why we blame bad results, not bad reasoning" [SNIPPET-ONLY]
       https://thedecisionlab.com/biases/outcome-bias — Outcome bias is the error of evaluating a decision's
       quality by its known result; the same behaviour draws more or less condemnation purely as a function
       of how it turned out. ASSUMPTION-1229 performs this operation in the favourable direction.
    2. Strohmaier, S. et al. (2021), "Hindsight bias and outcome bias in judging directors' liability and
       the role of free will beliefs," Journal of Applied Social Psychology, doi:10.1111/jasp.12722
       [SNIPPET-ONLY] — Demonstrates the bias surviving in expert populations (judges, psychiatrists) on
       negligence and liability judgments, i.e. it is not defeated by professional training or by care.
    3. "Ratchet effect" [SNIPPET-ONLY] https://en.wikipedia.org/wiki/Ratchet_effect ; empirical tests of
       budget ratcheting, ScienceDirect S0165410101000441 [SNIPPET-ONLY; authors unverified] —
       Names the structural consequence: once a limit moves in the permissive direction it is very hard to
       move back, and the phenomenon is explicitly related to scope, mission and feature creep.
    4. FasterCapital, "Cost Creep and the Ratchet Effect" [SNIPPET-ONLY] — Cost creep is described as
       insidious precisely because each individual increase is locally justified.

  Strength of challenge: Strong

  Summary: The inference the item makes has a name in two literatures and in both it is classified as an
    error. A constraint was breached; the breach produced findings; the findings are then offered as the
    warrant for revising the constraint. That is outcome bias in its textbook form — the decision to breach
    is being scored on its realised result rather than on the reasoning available beforehand — and the
    expert-population evidence says care and disclosure do not immunise against it. The structural
    consequence is worse than the epistemic one: a limit that can be raised by exceeding it profitably can
    only move one way, and the ratchet literature is unanimous that recovery is much harder than escalation.
    The measurement limb survives — yield-per-unit-effort is a real quantity — but it does not rescue the
    inference, because the measurement was made *after* the breach and only on the breaching runs.

  Specific risks: (a) The budget stops being a constraint and becomes a formality, at which point the
    estate loses its only signal that a run is expensive. (b) Every future overrun acquires the same defence,
    since a longer run will almost always find more. (c) This item and ASSUMPTION-1221 and PRESUMPTION-892
    together constitute a documented drift, not three separate incidents.

  Mitigations available: Yes. Derive the budget prospectively from measured yield-per-unit-cost across a
    sample of runs including compliant ones, and revise it on that basis rather than on the record of
    breaches. Attach an expiry to any revision. Record the pre-breach expectation so the post-hoc comparison
    has a baseline that is not itself contaminated.

  STEELMAN:
    Item: ASSUMPTION-1229
    Strongest counterargument: Outcome bias is an error when the outcome was determined by chance, and that
      is not obviously the case here. If longer runs find more defects *reliably and repeatably* — 28 for 28
      — then the relationship is not luck, it is a measured dose-response, and refusing to update the limit
      on it would be a different error: preserving a number because it is a number. A constraint that is
      never revisited in the light of evidence is not a control, it is a ritual.
    What would need to be true for C2A2 to be safe: the yield-per-unit-cost relationship would need to be
      measured across the whole range, including runs that stayed inside the budget, so the comparison is a
      curve rather than an anecdote about the high end.
    How to test: for the last 30 runs, plot findings against tokens consumed. If yield per token is flat or
      rising at the top of the range, the limit is too low and the revision is earned. If it falls, the
      overruns bought less per token than the compliant portion and the defence collapses.

  Recommendation: CHALLENGED

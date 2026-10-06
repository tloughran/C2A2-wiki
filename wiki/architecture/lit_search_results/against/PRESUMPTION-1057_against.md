SEARCH-AGAINST-PRESUMPTION-1057:
  Date searched: 2026-09-21
  Original item: PRESUMPTION-1057
  Original statement: The 223-day lag is a discovery-channel failure, not a coverage failure; pair
    enumeration may not address it.

  **Execution note:** 15a and 15b were executed by a single scheduled process on 2026-09-21. Query sets
  were framed separately and the FOR files were written before any AGAINST query was issued, but the
  two-process independence the spec assumes was NOT achieved. Weight the strength ratings accordingly.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-1057
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Noted the gap between a channel-shaped diagnosis and a coverage-shaped remedy.
      15b: Searched for evidence that coverage-shaped remedies do fix channel-shaped lags.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Hirt, J. et al. 2023, citation-tracking scoping review, *Research Synthesis Methods*
       DOI:10.1002/jrsm.1635; and reference-based search-strategy literature (ResearchGate 336570058).
       — The challenge to the dichotomy: in systematic-review practice, adding an enumeration-shaped
       channel is exactly how channel bias is corrected. Coverage and channel are not the alternatives
       14b's framing makes them; a second enumerative channel *is* a channel intervention.
    2. "Rethinking Literature Search Evaluation," arXiv:2605.29234. — Reports order-of-magnitude recall
       gains from systematic bibliography expansion. If a mechanical enumeration can move recall that
       far, "coverage-shaped remedies don't fix channel problems" is too strong as a general claim.
    3. Seed-based retrieval comparison, arXiv:2403.09295. — Shows channels are complementary rather
       than substitutable: the practical answer is usually *both*, not a choice between them.

  Strength of challenge: Moderate

  Summary: The diagnosis is probably right and the dichotomy is probably wrong. Evidence that discovery
    is channel-dominated does not entail that an enumerative remedy fails — in the nearest studied
    domain, enumerative remedies are the standard correction for channel bias, and they work. The
    defensible version of 1057 is narrower and stronger: *this particular* enumeration (91 thinker
    pairs) may be indexed on the wrong axis for a corpus whose channel is venues. That is a claim about
    the choice of enumeration key, not about enumeration.

  Specific risks: If 1057 is read as "don't build the sweep," the estate may decline a cheap recall gain
    on the strength of a framing distinction. If it is read as "build it on the wrong key," it saves
    2,184 queries. The two readings recommend opposite actions, which is reason to disposition it
    carefully rather than quickly.

  Mitigations available: Stop treating 1561 and 1057 as competing claims and run the single experiment
    that scores both: the pre-registered back-test, with the added instruction to record the venue of
    each recovered event. If recovered events cluster in few venues, 1057 wins on the narrow reading and
    the sweep should be re-keyed to venues. If they scatter, 1561 wins and the sweep should be built.

  STEELMAN:
    Item: PRESUMPTION-1057
    Strongest counterargument: The item's real contribution is not the channel/coverage distinction but
      the observation that a remedy was specified without a test of the diagnosis it answers. That
      observation holds regardless of which way the back-test comes out, and it is the third item in
      this intake to name an instrument that has been specified and not run. The dichotomy it is
      wrapped in is weaker than the observation it carries.
    What would need to be true for C2A2 to be safe: that the back-test runs before the sweep is built.
      It is in hand, it is pre-registered, and it is hours of work.
    How to test: as above; one experiment scores 1561 and 1057 together.

  Recommendation: PARTIALLY-CHALLENGED

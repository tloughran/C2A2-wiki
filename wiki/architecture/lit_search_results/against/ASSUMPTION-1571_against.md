SEARCH-AGAINST-ASSUMPTION-1571:
  Date searched: 2026-09-21
  Original item: ASSUMPTION-1571
  Original statement: Staleness-based downgrading selects for defective items -- 8 of 9 searched items
    from the downgraded cohorts went to REVISE, 1 stayed open, 0 confirmed -- and therefore slows the
    clock on exactly the items most in need of it.

  **Execution note:** 15a and 15b were executed by a single scheduled process on 2026-09-21. Query sets
  were framed separately and the FOR files were written before any AGAINST query was issued, but the
  two-process independence the spec assumes was NOT achieved. Weight the strength ratings accordingly.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1571
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-09-20 15d weekly cycle.
      15b: Searched for challenges to the inference from the 8-of-9 figure.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Selection-bias literature (Wikipedia, *Selection bias*; Scribbr, *Survivorship Bias*; First10EM,
       *Survival bias*; "Biases in Data Science Lifecycle," arXiv:2009.09795). — The decisive challenge
       is methodological, not substantive. Selection bias "arises when the way units enter your sample
       depends on the variable you are studying." The 8-of-9 figure counts only items that *were
       searched*; items are searched non-randomly, and in a stalled queue the ones that get searched are
       disproportionately the ones somebody judged worth searching. The sample is conditioned on the
       outcome.
    2. "Suspected bias in selection criteria of target subpopulation and its validation" (PMC10339632).
       — Treats exactly this shape of error: a subpopulation selected by criteria correlated with the
       endpoint, and what validation is required before its rate is reported as a population rate.
    3. Base-rate context from the estate's own registers. — Across the corpus of dispositions, REVISE is
       a common outcome. Without the REVISE base rate for *non*-downgraded searched items, 8-of-9 has no
       comparison class and cannot support a claim about *selection*. No literature is needed for this
       point; it is arithmetic, and the missing denominator is available in-house.

  Strength of challenge: Strong

  Summary: The underlying hypothesis may well be true — aging and latent defect do correlate in the
    practice literature — but the evidence offered cannot establish it. n=9, drawn from the searched
    subset of a stalled queue, with no control cohort and no base rate, is a textbook
    selection-on-the-dependent-variable design. The claim as stated ("selects for defective items") is
    a causal claim about the *downgrading rule*, and the data speak only about items that survived a
    different filter downstream of it.

  Specific risks: The queue discipline gets inverted on the strength of a 9-item sample. If the true
    effect is smaller than the selection artefact, the estate replaces one biased ordering with another
    and loses the aging signal it currently has. Second risk: this is the kind of finding that gets
    cited later as established ("we showed staleness selects for defects"), and the n=9 provenance does
    not travel with the sentence.

  Mitigations available: Compute the REVISE rate for non-downgraded searched items over the same window
    — the denominator exists in `lit_search_returns.md` and the computation is a grep. If the downgraded
    cohort's rate exceeds the base rate materially, the claim survives its strongest objection cheaply.
    Until then, state the finding as a hypothesis with its n attached.

  STEELMAN:
    Item: ASSUMPTION-1571
    Strongest counterargument: The finding is an artefact of the pipeline's own stall. In a backlog of
      ~130 live items draining at a handful per run, the items that get searched are the ones an agent
      picked out — and agents pick out items that look wrong. So "downgraded items go to REVISE" may
      report nothing about downgrading and everything about how search targets are chosen in a starved
      queue. The claim would then be the pipeline measuring its own triage behaviour and reading the
      result as a property of the world: precisely the reflexive-instrument failure PRESUMPTION-1053
      names, arriving one item later in the same intake.
    What would need to be true for C2A2 to be safe: that searched items are drawn from the downgraded
      cohorts in a way not correlated with apparent defectiveness — or that the base-rate comparison is
      computed and the gap survives it.
    How to test: the base-rate comparison above. One query, in hand, no new instrument.

  Recommendation: CHALLENGED

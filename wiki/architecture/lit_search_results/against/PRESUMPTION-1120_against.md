SEARCH-AGAINST-PRESUMPTION-1120:
  Date searched: 2026-10-11
  Original item: PRESUMPTION-1120
  Original statement: [inferred] Each proposal-writing job presumes its own evidential threshold is
    the house threshold. The wiki daily run declined to propose from unverifiable content. The
    Wolfram agent proposed from segment titles and left the check to the reviewer. Question: should
    all proposal-writing agents share one explicit evidential threshold, and where should
    unverifiable-but-relevant items go?
  Under test: the implied remedy, one shared explicit threshold, and the fallback of deferring
    verification to the reviewer. I searched for evidence that uniform thresholds harm
    heterogeneous tasks, and that deferring verification to a human reviewer fails.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1120
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-10): Inferred from the different proposal behaviour of the wiki daily run and the
        Wolfram agent that each job treats its own threshold as the house standard. Queued with the
        shared-threshold question.
      15b (2026-10-11): Searched for challenging literature. 3 searches: GRADE context-specific
        certainty thresholds; Cartwright & Hardie's critique of single evidence hierarchies;
        automation bias and rubber-stamping by human reviewers. 1 fetch attempted: PMC6542664 (GRADE)
        FAILED (reCAPTCHA wall, no content). Not retried, per the 1-fetch limit.
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. No successful fetch; all sources are snippet or search-summary grade.
  Search scope: preliminary (3 searches, 1 failed fetch). Broader search recommended.

  Challenging evidence found: Partial
  Strength of challenge: Moderate against "one uniform threshold". Moderate in favour of the
    presumption's concern, against the Wolfram-style "defer to reviewer" fallback.

  Sources:
    1. GRADE Working Group: GRADE Guidance 32 / 2021 contextualisation paper, and GRADE Guidance 41
       (2025) "Certainty Ratings: Thresholds Rather Than Categories of Contextualization." [snippet]
       GRADE redefined certainty as certainty that the true effect lies on one side of a chosen
       threshold. Users must choose and state the threshold, which depends on the decision context.
       Guidance 41 drops the contextualisation categories but keeps that "considering context in
       choosing thresholds remains worthwhile". Bearing: the leading evidence framework has an
       explicit and uniform method, but deliberately leaves the threshold value to the decision.
       That challenges "one shared threshold" for proposal agents with different stakes, such as a
       tradition-wiki addition versus an architecture change.
    2. Cartwright N & Hardie J. 2012. "Evidence-Based Policy: A Practical Guide to Doing It Better."
       OUP. [snippet: publisher blurbs and THE review] Rankings of evidence quality say how reliable a
       study is, not whether its result applies here. Over-reliance on a single standard (RCTs) "can
       at times discourage decision-makers from exercising their own discretion and judgement".
       Bearing: a single evidential bar can be met by evidence that is still irrelevant to the target
       question, and it can block relevant evidence that falls short of the bar.
    3. Automation-bias literature: Skitka, Mosier & Burdick 1999 (IJHCS) and the Cologne
       mammography study 2023 (Radiology). [snippet, secondary summaries] With an automated aid,
       participants missed 41% of unflagged critical events, against 3% without the aid (Skitka).
       When the AI gave wrong suggestions, inexperienced radiologists' accuracy fell from about 80%
       to under 20%. A governance commentary notes that agreement rates alone cannot tell rubber-
       stamping from correct confirmation. Bearing: this cuts against the Wolfram pattern (propose
       from titles, let the reviewer check). Reviewers tend to accept proposals as framed, so a
       deferred check often does not happen.

  Summary: The literature splits the presumption's implied remedy. It supports making thresholds
    explicit and stated: GRADE requires it. It challenges making them uniform. GRADE and Cartwright
    both hold that the right evidential bar depends on the decision and the context of use, so one
    house threshold would be too strict for low-stakes wiki proposals or too loose for architectural
    ones. On where unverifiable items go, the automation-bias literature is a strong warning against
    routing them to the reviewer as ordinary proposals. Reviewers under-verify AI-framed items.
    "Deferring the check to the reviewer" in practice means no check.

  Specific risks: (a) One threshold either suppresses useful low-stakes proposals or lets through
    under-evidenced high-stakes ones. (b) Unverifiable items mixed into normal proposals get
    rubber-stamped. (c) A separate holding queue for unverifiable items becomes a write-only backlog
    (compare PRESUMPTION-1121).

  Mitigations available: Use one shared method with stake-tiered thresholds (stated per proposal
    class). Each proposal carries an explicit evidence-grade label (verified / snippet / title-only).
    Unverifiable items go to a separate "verification-needed" lane with an expiry date, not into the
    normal reviewer queue.

  STEELMAN:
    Item: PRESUMPTION-1120
    Strongest counterargument: A single house threshold is the evidence-hierarchy mistake in a new
      setting. The major evidence framework (GRADE) settled on an explicit method with thresholds
      chosen per decision, because the cost of error differs across decisions. Proposal agents in
      C2A2 range from tradition-wiki additions to architecture changes. One bar for all of them will
      be wrong for most of them. Meanwhile the obvious place for unverifiable items, the human
      reviewer, is documented to under-verify AI-framed suggestions. So the actual inconsistency
      between agents may matter less than its two candidate fixes.
    What would need to be true for C2A2 to be safe: Thresholds are explicit and tiered by stake.
      Every proposal states the grade of evidence it rests on. Unverifiable items are labelled and
      quarantined, not passed to the reviewer as routine.
    How to test: Seed several title-only proposals, clearly or subtly marked, into the reviewer queue
      and measure the acceptance rate against verified proposals. Compare the error rates of
      accepted proposals under the uniform and tiered regimes.

  Boundary conditions identified:
    - The automation-bias findings are from human operators under time pressure. Tom's review
      conditions (asynchronous, accumulating backlog) plausibly make this worse, but that was not
      tested.
    - GRADE concerns clinical and policy evidence. The transfer to agent proposal-writing is by
      analogy.

  Recommendation: PARTIALLY-CHALLENGED

  SYSTEMIC-RISK-FLAG: see PRESUMPTION-1121_against.md.

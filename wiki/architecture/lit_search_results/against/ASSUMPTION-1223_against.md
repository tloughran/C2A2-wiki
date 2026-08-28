SEARCH-AGAINST-ASSUMPTION-1223:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1223
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High)
  Original statement: A keyword-triggered escalation filter can invert — systematically holding the
    highest-value items — because item value and the trigger token co-occur. Precision reported as 1-of-17.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1223
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim; the 1-of-17 precision figure carried as stated, not independently recounted.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Search scope: WebSearch, 2026-08-28, one dedicated query on the unreliability of small-sample classifier
    precision estimates. Reached: arXiv 2606.26422 (uncertainty in classifier performance, incl. LLM
    settings); arXiv 1906.04119 (prevalence CIs under prior shift); Raschka's ML confidence-interval notes;
    PMC7959610 on classifier uncertainty. NOT COVERED: any literature defending keyword triage on its
    merits, which would have been the other half of a fair challenge and which I did not find. All
    SNIPPET-ONLY. Confidence: MODERATE-HIGH on the statistical limb, LOW elsewhere.

  Challenging evidence found: Yes — against the item's evidential basis, not against its direction

  Sources:
    1. Anon. (2026), "Estimating Uncertainty in Classifier Performance with Applications to Large Language
       Models and Nested Data" (arXiv:2606.26422) [SNIPPET-ONLY; authors unverified] —
       Precision and recall are point estimates subject to sampling variation; uncertainty is routinely
       estimated by methods inappropriate for small labelled sets, and the default Wald interval and basic
       percentile bootstrap are the *least* accurate, "with coverage sometimes far below the nominal 95%."
    2. Anon., "Confidence intervals for class prevalences under prior probability shift" (arXiv:1906.04119)
       [SNIPPET-ONLY; authors unverified] — CLT-based intervals become unstable at small test sample size
       and small positive-class prevalence, and low power strongly biases prevalence estimates. Both
       conditions hold at n=17 with one positive.
    3. Sebastian Raschka, "ML Classifier Confidence Intervals" [SNIPPET-ONLY]
       https://sebastianraschka.com/blog/2022/confidence-intervals-for-ml.html ; PMC7959610, "Classifier
       uncertainty: evidence, potential impact, and probabilistic treatment" [SNIPPET-ONLY] —
       Recommend Wilson score intervals for small n, and note that reporting metrics as precise numbers
       irrespective of sample size makes every derived quantity falsely definite.

  Strength of challenge: Moderate-Strong (evidential limb); None found (mechanism limb)

  Summary: The challenge lands on the number rather than the worry. "1 of 17" is a point estimate with one
    positive event; a Wilson interval on that runs roughly from the low single digits to the mid-twenties in
    percent, which is consistent with a filter that is badly miscalibrated and also with one that is merely
    unlucky. Reporting it bare — as the queue entry notes was done, uncounted — is the specific practice the
    sources warn produces false definiteness. Separately, and this is the more important gap: no evidence
    was found either way for the item's distinctive mechanism, that item *value* and the trigger token
    co-occur. That is an empirical claim about this corpus, it has never been measured here, and it is what
    would make the filter inverted rather than simply imprecise.

  Specific risks: If the estate acts on "the filter inverts" when what it has is "the filter fired 17 times
    and was right once," it will redesign a classifier on a statistic that cannot support the redesign, and
    the redesign's improvement will be unmeasurable against the same noisy baseline. The converse risk is
    live too: dismissing the figure as small-n could retire a real inversion.

  Mitigations available: Recount with a Wilson interval and report the interval, not the ratio. Then run the
    one query that settles the mechanism: for the items the filter held, was their value higher or lower
    than the base rate? That is a two-column comparison, not a research project.

  STEELMAN:
    Item: ASSUMPTION-1223
    Strongest counterargument: In escalation settings the asymmetry is severe — a missed high-value item
      costs far more than an over-attended benign one — so waiting for a statistically comfortable sample
      before acting is itself a decision with a cost, and at n=17 with 16 misses the posterior on "this
      filter is fine" is already thin. Demanding a Wilson interval before touching a filter that appears to
      be holding the wrong things is a precision standard the estate does not apply to changes it likes.
    What would need to be true for C2A2 to be safe: the trigger token would have to be uncorrelated with
      item value, so the 16 misses are ordinary imprecision distributed evenly across the value range.
    How to test: rank the 17 triggered items by value and compare to the unfiltered population. Correlation
      present → inversion. Correlation absent → imprecision, and a threshold change suffices.

  Recommendation: PARTIALLY-CHALLENGED

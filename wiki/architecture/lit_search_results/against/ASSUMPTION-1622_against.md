SEARCH-AGAINST-ASSUMPTION-1622:
  Date searched: 2026-09-23
  Original item: ASSUMPTION-1622
  Original statement: A count reported "for continuity" under an unresolved definitional gap
    propagates the gap into every downstream ratio.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1622
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Compared four PRS totals from three sessions against a source count.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (the core mechanism, that a definitional gap in a
      count carries into quantities built from it, is not contradicted; the universal
      "every downstream ratio" is challenged by documented boundary conditions under which
      ratios are invariant to, or only weakly affected by, the definitional error)

  Challenging evidence found: Partial

  Sources:
    1. "Addressing bias due to measurement error of an outcome with unknown sensitivity in
       database epidemiologic studies. A contribution from the ConcePTION project." American
       Journal of Epidemiology (advance article; also PMC12409137). Addresses outcome counts
       whose definition captures an unknown fraction of true cases. It relies on the standard
       epidemiological result that when outcome misclassification is nondifferential and
       specificity is perfect, the risk ratio is unbiased even though every count is wrong.
       A definitional gap that affects numerator and comparator the same way drops out of the
       ratio. Direct boundary condition on "every downstream ratio."
    2. "Nondifferential disease misclassification may bias incidence risk ratios away from the
       null." (PubMed 16488359), plus "Misconceptions About the Direction of Bias From
       Nondifferential Misclassification" (PubMed 35231925). Together these show that the
       effect of a definitional error on a ratio depends on its structure: sometimes none,
       sometimes toward the null, sometimes away from it. That weakens the claim as a general
       rule but also shows the gap cannot be assumed harmless. Two-edged.
    3. Bartlett, R. & Partnoy, F. (2020). "The Ratio Problem." (NYU Law working paper). Argues
       that error in a ratio's numerator and error in its denominator behave very differently,
       so what the gap does downstream depends on where the count sits in the ratio, not only
       on whether the gap exists.
    4. "Surveillance bias in the assessment of the size of COVID-19 epidemic waves: a case
       study." Public Health (ScienceDirect, 2024). Case-count indicators, whose definition
       depended on testing regime, overestimated wave-size ratios compared with seroprevalence,
       hospitalisation and deaths. This CORROBORATES the claim: a definitional or detection gap
       in a count did propagate into ratios built on it.
    5. [unverified — from background knowledge] National statistical offices routinely
       publish series across a definition change with "break in series" flags and bridged or
       back-cast estimates, so that ratios within one definitional regime stay valid. This is
       a governance pattern in which continuity reporting does not contaminate every ratio.

  Strength of challenge: Moderate (against the universal quantifier); Weak-to-None (against
    the core mechanism)

  Summary: The epidemiological measurement-error literature is the main challenge. A count
  can be wrong in absolute terms while ratios built from it stay unbiased, specifically when
  the definitional error is nondifferential across the compared groups and one-sided (perfect
  specificity, imperfect sensitivity). So "every downstream ratio" overstates the case. Whether
  the gap reaches a ratio depends on whether numerator and denominator are measured under the
  same definition, and on whether the gap affects sensitivity or specificity. The same
  literature warns that the direction and size of the bias are hard to predict in general
  (exceptions to the "toward the null" rule are well catalogued), and the COVID wave-ratio
  case study is a documented example of propagation. On balance the claim holds as a default
  risk but not as a universal law.

  Specific risks: If C2A2 treats the claim as universal, it may throw away or quarantine
  ratios that are valid, such as within-session comparisons made under one consistent PRS
  definition. It may also miss the more dangerous case the literature points to: ratios that
  mix counts from different definitional regimes, where the bias is differential and can go
  either way.

  Mitigations available: Tag every count with the definition version used. Compute ratios
  only between counts that share a version, or flag a "break in series." Where the gap is
  known to be one-sided (undercount only), say so, because ratio invariance may then apply.

  Search scope: Preliminary — 3 searches (surveillance case-definition change and trends;
  nondifferential misclassification and ratio measures; ratio bias cancellation). No
  literature found that deals specifically with metric governance in software or agent
  pipelines. Broader search in data-quality and metric-governance venues recommended.

  Excluded results: aqrab.ai "Surveillance Bias" blog (no author or venue); unrelated patents
  and physics papers returned by the ratio-bias query.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1622
  Strongest counterargument: A definitional gap is a systematic error, not random noise, and
    systematic errors shared by numerator and denominator cancel in ratios. If every PRS total
    across the three sessions was counted under the same unresolved definition, then ratios
    and trends between those totals may be fully valid even though no single total is. The
    measurement-error literature has formal conditions for this: nondifferential error with
    perfect specificity leaves the risk ratio unbiased. Reporting a count "for continuity" is
    exactly what keeps the definition constant, which is the precondition for cancellation.
    On this view, continuity reporting protects ratios rather than contaminating them. The
    danger comes from changing the definition midstream, not from keeping an imperfect one.
  What would need to be true for C2A2 to be safe: (a) All counts entering a given ratio use
    the same operational definition. (b) The gap errs in one direction only (for example,
    systematic undercount with no false inclusions). (c) The gap's effect does not differ
    across the sessions or agents being compared. If any of these fails, the original claim's
    warning applies in full.
  How to test: Re-count one session's PRS total under each candidate definition. Recompute
  the downstream ratios under each. If the ratios stay stable while the absolute totals move,
  the cancellation boundary condition holds. If the ratios move, the propagation claim is
  confirmed for this pipeline.

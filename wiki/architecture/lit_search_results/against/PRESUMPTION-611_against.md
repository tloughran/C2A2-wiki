SEARCH-AGAINST-PRESUMPTION-611:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-611
  Original statement: [as queued] The census presumes a quantity that cannot be computed automatically should not be estimated; but reporting a bounded interval with its method stated is more honest than refusal. The register has no representation for "between X and Y," so the choice presents as a binary between false precision and silence. 209 partials are enumerated; only the classification is missing.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-611
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the census's refusal and its sole stated justification
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Tamer, E., "Partial Identification in Econometrics" (Annual Review of Economics / Harvard working paper); Manski worst-case bounds documentation (GJRM `mb`; MetricGate Manski bounds). — The field's own standard caution: no-assumptions bounds are OFTEN UNINFORMATIVELY WIDE, containing the truth but too wide to settle the question. An interval that spans most of [0,1] is not more informative than a refusal; it is a refusal with a number attached, and it is harder to argue with.
    2. Horowitz & Manski; Lee bounds literature. — Narrowing requires additional assumptions (monotonicity, selection restrictions) that must themselves be credible and stated. In C2A2's case, the obstruction is that two automated attempts could not classify — i.e. the classification RULE is unsettled. Bounds do not repair an unsettled definition; they propagate it into the interval's endpoints.
    3. Small-sample and prior-sensitivity literature (arXiv 2010.06110; small-sample bias adjustment). — Where estimates depend on the analyst's stated assumptions, small-sample results regress toward those assumptions. A hand-sampled defect fraction over 209 items, classified by the same agent that wrote the classification rule, is a self-classification with no inter-rater check — the register has already flagged self-certification as a live concern (PRESUMPTION-565 / MONITOR-489 lineage).
    4. Register-internal, reported per PREMISE-120: REVISE-254 (2026-07-31) ruled that a three-state intake convention must be gated on a MEASURED partition fraction with a pre-registered threshold, and cited Dubois & Prade to the effect that ignorance is a meta-evaluation rather than a truth value. Minting an interval TYPE now, to hold a number produced by the very classification that is unsettled, is the same move REVISE-254 declined eight days earlier.

  Strength of challenge: Moderate-to-Strong

  Summary: The item's methodological premise — that non-identification does not license silence — is correct and standard. The challenge is that the item's case is not a partial-identification case. Partial identification addresses a parameter that is not pinned down by the data under weak assumptions; here the parameter is not pinned down because the CLASSIFIER is unsettled, which two automated attempts demonstrated. Bounds constructed over an unsettled classification inherit the unsettlement in their endpoints and, per the field's own caution, are likely to be uninformatively wide — a number that cannot discriminate but that reads as a measurement. The strongest version of the census's refusal is therefore not squeamishness about numbers but a judgment that the defect DEFINITION is the missing object, and that publishing an interval would let the definitional gap be forgotten behind a figure. There is also a governance objection: the register ruled eight days ago (REVISE-254) that a new intake representation must be gated on measurement, and this item proposes a new representation to hold an unmeasured quantity.

  Specific risks: An interval published over an unsettled classification becomes the anchor for later work; subsequent readers cite the endpoints and not the caveat, which is the exact propagation failure PRESUMPTION-615 documents in the same intake. Second risk: the hand sample would be classified by the same agent whose rule failed twice, giving a self-certified number with no independent check.

  Mitigations available: Yes, and they are cheap: settle the compliant-vs-defective DEFINITION first and write it down; then draw the stratified sample; require a second, independently instructed classifier on a subsample and report agreement; report the interval only with the definition and the agreement rate attached. If the worst-case bound turns out to span more than, say, half the unit interval, report it as uninformative rather than as a finding.

  STEELMAN:
    Item: PRESUMPTION-611
    Strongest counterargument: The census's refusal may be the more rigorous act, not the less. Two automated classification attempts failed, which is evidence that "defective" is not yet operationally defined — and an interval estimated over an undefined predicate is not partial identification, it is precision applied to a question nobody has finished asking. The partial-identification literature agrees, on its own terms: worst-case bounds are frequently uninformatively wide, and narrowing them requires credible extra assumptions, which here would have to be assumptions about the very classification that could not be automated. Meanwhile the number, once written, will outlive its caveats — this register documented that mechanism in the same intake. And the register's own most recent ruling, REVISE-254, declined to mint a new intake representation without a measured basis and a pre-registered threshold; PRESUMPTION-611 asks for exactly such a representation on exactly the grounds that ruling rejected. Refusing to publish a number one cannot defend is a recognised professional standard, not an absence of one.
    What would need to be true for C2A2 to be safe: the defect definition is written before any estimate; the sample is classified with an independent second reader and agreement reported; the interval is pre-registered as informative only if narrower than a stated width; the register's interval type, if minted, is gated per REVISE-254.
    How to test: Draw a stratified sample of ~40 of the 209 partials, have two independently instructed classifiers rate them, and report (a) Cohen's kappa and (b) the resulting bound. If kappa is low, the item is refuted — the obstruction was definitional, not representational. If kappa is high, the item is vindicated and the refusal was overcautious. Denominator 40 of 209, corpus-scoped; decidable now and it discriminates the two readings.

  Recommendation: PARTIALLY-CHALLENGED

SEARCH-FOR-PRESUMPTION-604:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-604
  Original statement: The underpowered-self-measurement flag is treated as a property of three badly-named quantities, remediable by REVISE-257's feasibility clause. This presumes single-digit denominators are a drafting artifact rather than a structural consequence of the system's granularity. Runs are daily; batches have been 13, 8, 4, 3; incidents are counted per run. ANY per-batch or per-incident proportion is single-digit by construction. The only route to a two-digit denominator is pooling across days, and nothing in the register pools. REVISE-257 cannot be satisfied without a pooling convention that does not exist.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-604
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the structural reading of 15b's own 2026-07-31 SYSTEMIC-RISK-FLAG
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Kim et al., 2026. "Sequential Event Rate Monitoring." Statistics in Medicine (doi 10.1002/sim.70359). — States that the number of accrued EVENTS, not the number of looks, is what determines power in event-driven monitoring, and that monitoring cadence must be designed against the accrual rate. Supports the item's central claim: power is a property of the accrual design (here, the daily cadence), not of how the quantity is worded.
    2. Lakens, D. "Sequential Analysis," in Improving Your Statistical Inferences (lakens.github.io). — Sequential designs accumulate information across looks under a pre-specified spending function; power at any single look is lower than a fixed design's, and the compensation comes from accumulation. Supplies the named mechanism the item says the register lacks: information is pooled ACROSS periods by design, not within one.
    3. "E-values for Adaptive Clinical Trials: Anytime-Valid Monitoring in Practice" (arXiv 2602.06379). — Anytime-valid / e-value methods permit continuous monitoring with evidence accumulating across arbitrarily many looks without alpha inflation. This is a concrete, currently-standard pooling convention available to a daily-cadence system, so the item's "no route exists" reading is supported only for the register AS BUILT, not in principle.
    4. Small-n sequential (snSMART) literature, e.g. Bayesian group-sequential snSMART designs. — Where per-period n is irreducibly small, the field's standard response is to change the design (borrow across periods/arms, Bayesian pooling) rather than to reword the estimand. Supports the item's implication that REVISE-257's clause, as written, asks a drafting-level fix for a design-level problem.

  Strength of support: Strong

  Summary: The statistical literature supports the item's diagnosis directly. Power in a monitoring system is a function of accrual — events per unit time times observation window — and is therefore fixed by cadence and batch size, not by how a settling quantity is phrased. A daily run producing single-digit batches yields single-digit per-run denominators by construction, exactly as the item states. The literature also confirms the item's implied prescription: the discipline's answer to irreducibly small per-period n is a pooling or accumulation convention (group-sequential spending functions, anytime-valid e-values, Bayesian borrowing), all of which are explicit design objects that must be specified in advance. Since the register scopes every settling quantity to a run or a cohort and specifies no such convention, REVISE-257's "named route to a larger denominator" is unsatisfiable as written — not because no route can exist, but because none has been built.

  Caveats: (1) The item's strong form ("the only route is pooling across days") is supported; its strongest form ("no route could exist") is NOT — the literature supplies several. 15a reports this as narrowing, not as refutation. (2) All primary sources are from clinical-trial monitoring; transfer to an operational self-audit pipeline is analogical, and the trial setting has a pre-registered protocol that C2A2's daily runs do not. (3) The item's own settling quantity — a distribution of achievable denominators across the register, partitioned by scope — is computable from internal data and was not computed by this search; the literature cannot settle it. (4) Search scope: sequential monitoring, small-n design, anytime-valid inference. NOT searched: rare-event reliability estimation, which bears on the incident-count case.

  Recommendation: SUPPORTED

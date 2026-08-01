SEARCH-AGAINST-PRESUMPTION-604:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-604
  Original statement: [as queued] Single-digit denominators are a structural consequence of daily cadence and batch size, not an item-drafting fault; ANY per-batch or per-incident proportion is single-digit by construction; the only route to a two-digit denominator is pooling, which the register does not do; therefore REVISE-257 is unsatisfiable as written.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-604
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the structural reading of 15b's own 07-31 SYSTEMIC-RISK-FLAG
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Exact inference for rare events and small samples — e.g. "Exact Inference for Random Effects Meta-Analyses for Small, Sparse Data" (PMC12456449); exact GLMM/conditional likelihood approaches. — Valid inference at small n is available without pooling; the discrete-data exact methods give correct coverage where asymptotic methods fail. This refutes the strongest reading of the item, that single-digit denominators make a quantity undecidable. They make intervals wide, which is a different and reportable condition.
    2. Bayesian small-sample literature (arXiv 2010.06110, noninformative priors; PMC8543928, additional-evidence decision making). — Bayesian methods yield valid inference irrespective of study count. But the same sources supply the caution: estimates are HIGHLY sensitive to prior specification at small n and can perform worse than frequentist asymptotics. So the escape route exists but is not free.
    3. Meta-analysis-with-few-studies literature (arXiv 1807.09037; PMC10503457 on heterogeneity with two studies). — Pooling — the item's named "only route" — is itself unreliable when the units pooled are few or heterogeneous: coverage is compromised or intervals become inconclusively wide. A pooling convention adopted to satisfy REVISE-257 would not obviously produce better-grounded numbers, only larger denominators.
    4. Small-sample bias / regression-to-prior findings ("Small-Sample Bias Adjustment"): in heterogeneous or minority-dominated subgroups, pooled Bayesian estimators regress small cells toward the prior mean, amplifying bias for rare combinations. Directly relevant: the register's interesting cases are the rare ones.
    5. Counterexample to the item's universal quantifier, from the queue itself: PRESUMPTION-611's own settling quantity has denominator 209, and PRESUMPTION-602's is corpus-scoped. Both are register items whose denominators are not single-digit. The claim "ANY per-batch or per-incident proportion is single-digit" is true but vacuous — the quantifier that matters is over settling quantities, and there it is false.

  Strength of challenge: Strong

  Summary: The item's causal diagnosis — cadence determines achievable per-run n — is not in dispute. What is challenged is the two inferences drawn from it. First, that the register has no route to two-digit denominators: this is false on the register's own contents, since corpus- and cohort-scoped quantities exist (209 partials in PRESUMPTION-611, the full artifact corpus in PRESUMPTION-602) and were minted on the same day. The constraint therefore bites on item-drafters who choose per-run estimands, which is closer to the drafting-fault reading the item is arguing against than the item allows. Second, that pooling is the answer: the meta-analytic literature on few and heterogeneous studies reports that pooling across a small number of dissimilar units degrades coverage and shrinks rare cells toward the prior — so a pooling convention adopted to satisfy REVISE-257 could manufacture larger denominators without manufacturing more information. The literature's actual prescription at small n is exact or explicitly Bayesian inference with wide, honestly reported intervals — which is a drafting and reporting change, not a cadence change.

  Specific risks: If C2A2 accepts the item as stated, it concludes REVISE-257 is unsatisfiable and either voids the feasibility clause or builds a pooling convention. Voiding it removes the only current brake on underpowered self-measurement. Building a naive pooling convention across heterogeneous daily runs risks exactly the Simpson-type aggregation error the meta-analysis literature warns about, and would produce two-digit denominators that look satisfying and are not.

  Mitigations available: Yes: (a) require the estimand's SCOPE (run / cohort / corpus) to be declared alongside the settling quantity, which makes the achievable denominator visible at drafting time; (b) permit wide intervals with exact small-sample methods rather than requiring a large denominator; (c) if pooling is introduced, require a stated homogeneity condition for the pooled units.

  STEELMAN:
    Item: PRESUMPTION-604
    Strongest counterargument: The item generalises from three items to a structural law and gets the quantifier wrong. It is trivially true that a proportion whose denominator is one run's batch is single-digit when batches are single-digit — but that is a statement about the estimands the drafters chose, not about the system's granularity, and the same day's intake contains counterexamples with denominators of 209 and of the whole corpus. The system is not prevented from asking corpus-scoped questions; it has simply been asking run-scoped ones. Worse, the remedy the item points toward is the one the statistical literature is most cautious about: pooling few, heterogeneous units degrades coverage and biases exactly the rare cells the register exists to catch. The discipline's answer to irreducibly small n is not a bigger denominator obtained by aggregation — it is exact inference with an honestly wide interval, and a willingness to say the interval is uninformative. REVISE-257 is satisfiable as written; what it demands is that drafters pick a scope where a denominator exists.
    What would need to be true for C2A2 to be safe: settling quantities must carry a declared scope; the feasibility clause must be read as requiring a route, and corpus/cohort scoping counts as one; no pooling convention is adopted without a stated homogeneity condition.
    How to test: The item's own settling quantity, computed: take every settling quantity currently in the register, partition by scope (run / cohort / corpus), and report the achievable-denominator distribution per partition. If the corpus partition is non-empty and its denominators are two-digit or larger, the item's "no route exists" claim is refuted and the drafting-fault reading survives. Register-scoped, denominator in the hundreds.

  Recommendation: PARTIALLY-CHALLENGED

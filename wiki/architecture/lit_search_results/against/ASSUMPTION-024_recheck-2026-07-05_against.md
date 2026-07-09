SEARCH-AGAINST-ASSUMPTION-024-RECHECK:
  Date searched: 2026-07-06
  Original item: ASSUMPTION-024 / PREMISE-004 (monthly incorporated-premise re-check; validated 2026-04-15)
  Original statement: "Convergence of independent lines of evidence (triangulation/overdetermination) is a legitimate confirmatory strategy (Wimsatt 1981)."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a,15b → 15c (INCORPORATED) → 15d re-check → 15b
    Original item: ASSUMPTION-024 / PREMISE-004
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted stated methodological premise that triangulation of independent evidence lines is legitimately confirmatory (Wimsatt 1981)
      15b: Re-checked for NEW challenging literature since validation date 2026-04-15
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (the principle stands; new and recent literature attacks the independence premise as applied in AI-assisted pipelines like C2A2)

  Sources:
    1. Kim, E. et al., 2025. "Correlated Errors in Large Language Models." ICML 2025 (arXiv:2506.07962). — Empirical finding that LLMs err together: on one leaderboard, models agree 60% of the time when both err, and larger/more accurate models have highly correlated errors even across distinct architectures and providers. Any C2A2 "independent lines" produced by multiple model runs or agents share failure modes and are not probabilistically independent.
    2. "CARE: Confounder-Aware Aggregation for Reliable LLM Evaluation." arXiv:2603.00039 (March 2026). — New near/after the validation window: LLM judges share latent confounders (verbosity, stylistic preference, training artifacts) so majority-vote/averaging aggregation provides little gain or amplifies systematic mistakes — a direct formal analogue of pseudo-robust triangulation.
    3. "Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection." arXiv:2602.08003 (Feb 2026). — Under uniform pairwise correlation, adding more models does not drive error to zero but converges to a floor; convergence of many correlated "lines" is bounded evidence, not accumulating evidence.
    4. Schupbach, J. / Stegenga, J. line: "Robustness, Discordance, and Relevance" (Philosophy of Science) and Stegenga & Menon, "Robustness and Independent Evidence." — Standing philosophical critique: ontic independence is not sufficient for robustness arguments; failure of independence produces illusory (pseudo-)robustness, and real multi-technique evidence is often discordant rather than concordant.
    5. Houkes, Šešelja & Vaesen, "Robustness analysis" (PhilSci-Archive 22010). — Recent survey of robustness-analysis critiques: models are rarely independent in the way robustness arguments require; robust theorems cannot by themselves specify mechanisms.
    6. Orzack, S. & Sober, E., 1993 (background), and Odenbaugh/Alexandrova critiques of robustness in modeling. — The classic objection line the newer work extends: concordance among models sharing core assumptions confirms the shared assumptions' consequences, not the world.

  Strength of challenge: Moderate

  Summary: No new literature overturns Wimsatt's principle itself — triangulation over genuinely independent determinations remains a legitimate confirmatory strategy, and the philosophical debate about its scope predates the validation. What has changed since 2026-04-15 is the applied picture for AI-assisted pipelines: the ICML 2025 correlated-errors result and the early-2026 aggregation papers (CARE; information-theoretic ensemble selection) establish empirically that multiple LLM-generated analyses are correlated evidence streams — sharing training data, architectures, and stylistic confounders — and that aggregating them yields an error floor, not convergence to truth. For C2A2, whose "independent lines of evidence" are frequently produced by sibling agents of the same model family reading overlapping corpora, the independence premise of PREMISE-004 is exactly the part the new literature undermines. The philosophy-of-science critique (pseudo-robustness, discordance) supplies the framework: concordance among dependent detectors confirms the shared dependence, not the hypothesis.

  Specific risks: C2A2 may score claims as strongly confirmed because multiple agent analyses converge, when the convergence reflects shared model priors and shared source contamination (e.g., all agents read the same wiki notes); the 15a/15b for-against pattern itself is only as independent as the underlying model; overdetermination language in the wiki could systematically overstate epistemic warrant for cross-tradition claims.

  Mitigations available: Diversify determination types, not just runs — pair LLM analysis with non-LLM checks (textual quotation verification, human judgment, quantitative measures) so lines differ in mechanism; when multiple agents are used, use different model families and document shared inputs; treat intra-family agent agreement as one line of evidence, not N; adopt discordance-reporting (record when lines disagree rather than only when they converge); cap the confirmatory weight assigned to converging LLM outputs per the ensemble error-floor results.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-024 / PREMISE-004
  Strongest counterargument: Wimsatt's warrant flows entirely through independence, and the 2025–2026 empirical record shows that the kind of evidence lines C2A2 actually aggregates — analyses by LLM agents — are demonstrably non-independent even across providers: models agree in error at rates far above chance, and correlated ensembles converge to an error floor no amount of additional agreement can breach. Triangulation in C2A2 therefore risks being a single instrument reading taken N times and reported as N instruments: the convergence is real, but it measures the shared prior, not the claim. Since PREMISE-004 is incorporated (load-bearing for the wiki's confirmation methodology), an unexamined independence assumption propagates inflated confidence system-wide.
  What would need to be true for C2A2 to be safe: Convergence is only counted as triangulation when the lines differ in mechanism (LLM analysis vs. direct quotation vs. human check vs. quantitative measure), and same-family agent agreement is explicitly weighted as one line.
  How to test: Take a set of claims where multiple C2A2 agents converged; rerun one line with a different model family and one non-LLM check; measure how often convergence survives. Separately, seed a deliberately false but plausible claim and test whether sibling agents converge on it — convergence on the seeded error quantifies the pseudo-robustness rate.

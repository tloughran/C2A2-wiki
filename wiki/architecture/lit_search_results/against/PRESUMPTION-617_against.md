SEARCH-AGAINST-PRESUMPTION-617:
  Date searched: 2026-08-02
  Original item: PRESUMPTION-617
  Original statement: That a result produced under an acknowledged and disclosed protocol deviation carries the same evidential status as one produced under protocol; that disclosure alone discharges the deviation.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-617
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced an unstated assumption that declaring a deviation restores the status of the result, rather than merely making the deviation visible.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Torka, A.-K. et al., 2025. "Going off script: Exploring the reporting of preregistration deviations in Industrial and Organizational Psychology and their relationship with questionable research practices." Journal of Occupational and Organizational Psychology. — 72% of preregistered studies deviated at least once and 68% had at least one *undisclosed* deviation; deviations are analysed in explicit relation to questionable research practices, i.e. the deviation is treated as a bias-bearing event in its own right, not a bookkeeping entry.
    2. Willroth, E.C. & Atherton, O.E., 2024. "Best Laid Plans: A Guide to Reporting Preregistration Deviations." Advances in Methods and Practices in Psychological Science 7(1). — Sets out that disclosure is necessary but not sufficient: deviations must be reported with timing (before/after seeing data), rationale, and accompanying sensitivity or robustness analyses. Bias risk is a function of *when* the deviation occurred, which disclosure records but does not remove.
    3. Claesen, A. et al., 2021. "Comparing dream to reality: an assessment of adherence of the first generation of preregistered studies." Royal Society Open Science (PMC8548785). — Effectively all examined preregistered studies deviated, and most deviations were undisclosed; establishes that the disclosure norm is weakly enforced in practice, so a system that treats disclosure as sufficient inherits an empirically low compliance base rate.
    4. Registered report on EEG/ERP preregistration practices, 2025. Cortex (ScienceDirect S0010945225000577). — Mean adherence to preregistration 60%; only 16% of published studies fully adhered or disclosed all deviations; z-curve analysis indicated selective reporting was still present in the published preregistered literature. Disclosure regimes did not eliminate the bias they were designed to prevent.
    5. "Practical Guidelines for Standardised Resolution of Important Protocol Deviations in Clinical Trials Conducted in Sub-Saharan Africa," 2024 (PMC11043146), with FDA draft guidance on protocol deviations. — Under ICH/GCP, important protocol deviations are those that "might significantly affect the completeness, accuracy, and/or reliability of the study data"; serious deviations "deemed to invalidate the data collected" lead to *exclusion of data from analysis*. Documentation of a deviation is a mandatory obligation, and is explicitly not a remedy for its effect on data status.
    6. Replicability-Index analyses and "Eleven years of student replication projects provide evidence on the correlates of replicability in psychology," 2023 (PMC10645069). — Replication success was 72-82% when the same authors replicated versus 58-60% when all authors differed. Non-independent verification produces materially inflated success rates; a result verified by the same agent that produced it is not equivalent in status to one verified independently, however transparently the arrangement is declared.

  Strength of challenge: Strong

  Summary: Across both the preregistration literature and the regulatory trials literature, disclosure is treated as a reporting obligation that makes a deviation assessable — not as an operation that restores the deviating result to protocol status. GCP goes further and specifies that important deviations can invalidate data and trigger exclusion from analysis regardless of how well documented they are. The empirical picture is worse than the normative one: adherence is around 60%, full disclosure around 16%, and selective reporting is still detectable in published preregistered work. Separately, the replication data show that non-independent verification inflates apparent success by roughly 14-22 percentage points, so a disclosed self-verification is a measurably weaker result, not an equivalent one carrying a footnote.

  Specific risks: Deviated results enter the corpus at full weight and are cited downstream by items that do not carry the deviation flag forward, so the discount is lost at the first hop. Because disclosure is cheap, it becomes the dominant strategy: the system learns that any deviation is permissible provided it is announced, and the protocol degrades into a default that is routinely overridden. A verification performed by the producing agent and disclosed as such gets counted as verification in aggregate coverage statistics, inflating the system's estimate of its own evidential base.

  Mitigations available: (a) Two-tier status — deviated results carry a distinct type that propagates to anything derived from them, not a prose note; (b) classify deviations as important/non-important on the ICH criterion (does it affect completeness, accuracy or reliability of the result) and exclude important-deviation results from load-bearing claims; (c) record deviation *timing* (before or after the result was seen) since that is the bias-determining variable; (d) require a sensitivity analysis — what would the result have been under protocol; (e) never count non-independent verification toward a verification quota.

  Search scope: Comprehensive for preregistration deviation reporting and for ICH/GCP protocol-deviation handling. Moderate for the status of non-independent verification — the replication-by-same-author figures are solid but were located through secondary summaries; direct retrieval of the underlying replication datasets recommended before quoting the exact percentages.

  STEELMAN:
    Strongest counterargument: The alternative to disclosed deviation is undisclosed deviation, and the literature's own numbers show that is what actually happens 68% of the time. A disclosed deviation is strictly more informative than a silent one, and the entire preregistration reform rests on the claim that transparency plus reader judgement outperforms rigid adherence. Rigid protocol enforcement in a research system with genuine uncertainty produces either paralysis or concealment. Moreover the ICH framework itself distinguishes important from non-important deviations and "tends to be inclusive" — most deviations do not invalidate anything, and treating them all as status-reducing would discard sound results and create a strong incentive to under-report.
    What would need to be true for the system to be safe: (i) the deviation is non-important on the completeness/accuracy/reliability criterion; (ii) it was decided before the result was observed; (iii) the disclosure is machine-readable and propagates to derived artifacts; (iv) an independent party, not the producer, judges the deviation's materiality.
    How to test: Sample results in the corpus carrying disclosed deviations. For each, check whether the deviation flag survives one and two hops of downstream citation, and whether an independent re-run under protocol reproduces the result. The propagation-survival rate and the under-protocol reproduction rate together give the size of the status inflation.

  Recommendation: CHALLENGED

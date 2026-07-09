SEARCH-AGAINST-PRESUMPTION-452:
  Date searched: 2026-07-07
  Original item: PRESUMPTION-452
  Original statement: "[inferred] Subset (9-page) + aggregate (<2%) resolver agreement establishes census-wide delta validity."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-452
    Item type: PRESUMPTION (unstated — surfaced by inference), Priority LOW
    Transform at each step:
      14b: Inferred from the 2026-07-06 autonomous-Monday EOD sources (sewing bootstrap verification report validating the weekly census agent against the bootstrap protocol via a 9-page spot check plus <2% aggregate difference)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Simpson, E. H., 1951. "The Interpretation of Interaction in Contingency Tables." Journal of the Royal Statistical Society B, 13(2), 238-241; with the canonical empirical case Bickel, P. J., Hammel, E. A. & O'Connell, J. W., 1975, "Sex Bias in Graduate Admissions: Data from Berkeley," Science, 187(4175), 398-404. — Aggregate agreement can coexist with, and mask, systematic stratum-level disagreement; two resolvers can match to <2% overall while disagreeing sharply on specific strata (e.g., orphans vs connected pages) with the errors cancelling in the total.
    2. Bland, J. M. & Altman, D. G., 1986. "Statistical methods for assessing agreement between two methods of clinical measurement." The Lancet, 327(8476), 307-310. — Agreement between methods must be assessed via paired per-item differences and limits of agreement, not overall totals or correlations; an aggregate <2% difference is precisely the kind of summary statistic Bland & Altman showed to be inadequate evidence of method agreement.
    3. Christensen, H. S. et al., 2022. "A descriptive study of sample sizes used in agreement studies published in the PubMed repository." BMC Medical Research Methodology, 22:242. — Median sample sizes in published agreement studies are ~65-71 items; small samples yield wide confidence intervals around agreement estimates. A 9-page validation subset is roughly an order of magnitude below field norms, making its agreement estimate statistically weak (with 9/9 concordance, the exact binomial 95% lower bound on per-page agreement is only ~66-70%).
    4. Lachenbruch, P. A. (and successors), sample-size work for kappa and agreement (e.g., Sim, J. & Wright, C. C., 2005, "The Kappa Statistic in Reliability Studies," Physical Therapy, 85(3), 257-268). — Chance-corrected agreement statistics are unstable at small n and sensitive to category prevalence; with a skewed page population (many connected, few problematic), a small convenience subset will be dominated by easy cases.
    5. Alsallakh, B. et al. / ML evaluation literature on slice-based validation (e.g., Sagadeeva, S. & Boehm, M., 2021, "SliceLine: Fast, Linear-Algebra-based Slice Finding for ML Model Debugging," SIGMOD). — Modern model-validation practice explicitly rejects aggregate-only validation because models (and resolvers) fail on slices; discovering the disagreeing subpopulation requires stratified or slice-finding evaluation, not a global delta.

  Strength of challenge: Strong

  Summary: The statistics of agreement offer little support for inferring census-wide delta validity from a 9-page subset plus a <2% aggregate difference. Simpson's-paradox literature shows aggregate concordance can mask offsetting stratum-level disagreements — the failure mode most relevant here, since link-resolution differences would plausibly concentrate in exactly the strata the census exists to count (orphans, edge-case wikilinks, embeds, aliases). Bland & Altman established that method agreement must be shown on paired per-item differences, not totals. Sample-size research puts published agreement studies at a median of ~65-71 items, so n=9 yields agreement estimates with confidence intervals too wide to certify anything "census-wide" (a perfect 9/9 result is still consistent with ~30% of pages disagreeing). If the 9 pages were chosen conveniently rather than by stratified sampling, selection bias compounds the problem. The <2% aggregate bound does constrain gross total-count divergence, which is why the challenge is not total — but validity of stratum-level deltas (the orphan/sparse/connected transitions) is unestablished.

  Specific risks: Resolver disagreements concentrated in a small stratum — e.g., pages with unusual link syntax, or the orphan boundary itself — could shift dozens of pages between orphan/sparse/connected categories while total counts move <2%. C2A2 would then report spurious week-over-week "synthesis health" transitions (or miss real ones) while believing its instrument validated. Downstream decisions (which pages to sew, whether synthesis is working) inherit the error.

  Mitigations available: Stratified validation sampling (draw pages from each census category, oversampling boundary/edge-syntax cases); report per-stratum agreement, not just aggregate; compute and record the confidence interval on the subset agreement rate; increase validation n toward field norms (~50-70 pages) once, then spot-check thereafter; log the page-level paired differences (a Bland-Altman-style table) whenever both resolvers run.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-452
    Strongest counterargument: A <2% aggregate delta plus 9 concordant pages is consistent with large offsetting stratum-level errors (Simpson's paradox) and, on its own, statistically certifies per-page agreement no better than roughly 70% at the 95% level. Agreement-study norms require an order of magnitude more items and per-item paired analysis (Bland & Altman) before declaring two instruments interchangeable. If the 9 pages were not randomly and stratifiedly sampled — and validation subsets rarely are — the estimate is further biased toward easy, well-formed pages, precisely the ones least likely to expose resolver differences.
    What would need to be true for C2A2 to be safe: Resolver differences would need to be homogeneous across page types (no error concentration in strata), the 9 pages would need to have been sampled to include the difficult strata (orphans, unusual link syntax, embeds), and the downstream use of the census would need to depend only on aggregate counts, not on stratum transitions — none of which is currently evidenced.
    How to test: Run both resolvers over the full census once (or a stratified 60-80 page sample), compute per-stratum agreement and the distribution of page-level deltas; specifically check agreement on the orphan/sparse boundary pages. If per-stratum agreement holds at high n, the presumption is retroactively validated cheaply.

  Search scope confidence: High for the statistical core (Simpson/aggregation, Bland-Altman, agreement sample sizes are settled literature); moderate for the software-specific slice-validation framing, which is younger but consistent.

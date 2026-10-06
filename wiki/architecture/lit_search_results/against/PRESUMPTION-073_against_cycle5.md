SEARCH-AGAINST-PRESUMPTION-073:
  Date searched: 2026-09-04
  Original item: PRESUMPTION-073 (MONITOR-068), priority MEDIUM-HIGH
  Original statement: "Adding two traditions brings N=11->13 without affecting N-dependent
    properties (cross-program density, statistical power for r)."
  Cycle: monthly re-check cycle 5 (15d re-trigger of 2026-07-05)

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15b (cycle 5)]
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Inferred from the expansion decision proceeding without a recalibration step for the
           cross-tradition metric r or the density measure.
      15b: Searched for challenging literature (cycle 5 re-check).
    Current status: CHALLENGED

  Queries run this cycle:
    1. "network density metrics not comparable across networks of different size finite size effects small networks"
    2. "dyadic data non-independence inflated Type I error correlation test all pairs QAP permutation Mantel"
    3. "effective sample size N(N-1)/2 pairs not independent network autocorrelation degrees of freedom overstated"
    4. "measurement invariance adding items to a scale changes construct test equating recalibration required"
    5. "adding nodes changes network metrics bias sampled networks node selection non-random effect on density clustering"
    6. "at what sample size do correlations stabilize Schonbrodt Perugini corridor of stability"
    7. "multiple comparisons all pairwise correlations family-wise error rate grows quadratically number of variables"
    8. "graph density normalization does not remove size dependence comparing networks different number of nodes bias"
    9. "number of agents multi-agent debate non-monotonic performance scaling adding agents changes dynamics 2026"

  Challenging evidence found: Yes

  Sources:
    1. van Wijk, B.C.M., Stam, C.J. & Daffertshofer, A. 2010. "Comparing Brain Networks of Different
       Size and Connectivity Density Using Graph Theory." PLoS ONE 5(10): e13701,
       doi 10.1371/journal.pone.0013701. [VERIFIED BY 15c 2026-09-04 - authors, venue, volume,
       DOI and PMID 21060892 all confirmed.] - The central challenge to the density half. Graph
       measures are influenced by N and mean degree k, and direct comparisons between empirical
       networks with different N and/or k "can yield spurious results." Normalising by the range of
       obtainable values DIMINISHES but does not eliminate N-sensitivity. 15c note: the abstract is
       blunter than this paraphrase - "none of the investigated methods allows for a reliable and
       fully unbiased comparison."
    2. Smith, K. & Escudero, J. 2020. "Normalised degree variance." Applied Network Science
       (s41109-020-00273-3; arXiv:1803.03057). - Specific "normalised" graph statistics retain a
       density dependence; normalisation is not a general cure for size/density comparability.
    3. Dekker, D., Krackhardt, D. & Snijders, T.A.B. "Sensitivity of MRQAP tests to collinearity and
       autocorrelation conditions" (Radboud repository); Kovacevic et al., "Structure matters:
       Assessing the statistical significance of network topologies," PMC11446434. - Standard
       parametric tests on dyadic data with moderate structural autocorrelation can produce Type I
       error rates "exceeding 50%." Because r is computed over all N(N-1)/2 pairs sharing common
       endpoints, the pairs are non-independent by construction, and the MAGNITUDE of the inflation
       changes with N - so the presumption of invariance fails even for the error rate.
    4. Farine, D.R. & Carter, G.G. bioRxiv 2021.06.04.447124, "Common Permutation Methods in Animal
       Social Network Analysis Do Not Control for Non-independence." - Stronger form: even the
       standard permutation remedies can fail. Removes the easy fix.
    5. Afyouni, S., Smith, S.M. & Nichols, T.E. 2019. "Effective degrees of freedom of the Pearson's
       correlation coefficient under autocorrelation." NeuroImage (PMC6693558). - The xDF correction
       "varies substantially over node pairs"; available EDF estimators make restrictive assumptions
       that, unmet, produce "biased inferences that lead to distorted topological descriptions."
       Directly contradicts the assumption that information content scales with raw pair count.
    6. Schonbrodt, F.D. & Perugini, M. 2013. "At what sample size do correlations stabilize?"
       Journal of Research in Personality 47(5):609-612, doi 10.1016/j.jrp.2013.05.009. - Point of
       stability is ~250 observations, ~400-450 for small-to-moderate true r within a +/-.10
       corridor. If the independent unit for r is the tradition (N=11 vs 13), C2A2 is one to two
       orders of magnitude below stability at BOTH values. The claim "N-dependent properties are
       unaffected" is true only in the sense that both values are unusably small - which is not the
       reassuring reading. [15b flagged a 2013/2016 discrepancy in a GitHub repo description; the
       DOI and JRP volume support 2013 and 15b did not guess.]
    7. Family-wise error literature (FWER references; Springer s00180-022-01214-7). - c = k(k-1)/2
       grows quadratically: 55 -> 78 comparisons is a 41.8% increase in multiplicity burden. Under
       independence, FWER at alpha=.05 goes from 1-.95^55 ~ 0.94 to 1-.95^78 ~ 0.982; under
       Bonferroni the per-test alpha tightens from .00091 to .00064, a 30% loss of per-test power.
       Either way the N-dependent inferential properties demonstrably change. (The independence
       assumption behind this arithmetic itself fails for overlapping pairs.)
    8. Non-random node-addition / sampling-bias literature: NBER WP 25270, "Non-Randomly Sampled
       Networks: Biases and Corrections"; npj Systems Biology and Applications s41540-025-00526-w,
       "Assessing the impact of sampling bias on node centralities"; Smith & Moody, "Network
       sampling coverage II." - WHICH nodes are added matters. Global metrics like density are
       comparatively robust while local metrics are not; non-random node selection can produce
       "stronger community-like structure than original networks." C2A2's two new traditions were
       chosen for substantive reasons, not sampled - a selection effect, not sampling noise, whose
       direction is set by the selection rationale.
    9. arXiv:2601.23219, "MonoScale: Scaling Multi-Agent System with Monotonic Improvement" (ICML
       2026 poster); arXiv:2512.08296, "Towards a Science of Scaling Agent Systems." - The existence
       of a paper whose contribution is MAKING multi-agent scaling monotonic is itself evidence that
       adding agents does not by default leave system properties unchanged. Improvement is monotonic
       on static ensemble-style tasks but non-monotonic on interactive ones, where "coordination
       overhead scales with interaction depth" and "errors cascade rather than cancel."
   10. Measurement-invariance literature (Springer s13428-021-01690-7, "Scale length does matter";
       PMC6563622 on continuous item-pool calibration and equating). - Fit statistics used to judge
       whether an instrument measures the same construct depend on scale length, and extending an
       item pool has an established equating/calibration procedure precisely BECAUSE extension is
       not assumed to be property-preserving. The presumption that C2A2 can extend its instrument
       from 11 to 13 without any recalibration step is contrary to standard practice in every field
       that has thought about instrument extension.

  NEW SINCE LAST CYCLE: Little that is new - and 15b states this is the honest finding. The
    load-bearing challenges (van Wijk 2010, Krackhardt/MRQAP, Schonbrodt & Perugini 2013, FWER
    arithmetic) are long-established and would have been available at any prior cycle. That three
    earlier cycles logged "no new sources" is consistent with the literature being stable, but the
    correct conclusion is that THE CHALLENGE WAS ALWAYS THERE, not that there is no challenge.
    Genuinely post-April: arXiv:2601.23219 only. Query 9 was run specifically to establish this.

  Strength of challenge: Strong

  Summary: The presumption fails on at least four independent grounds. First, graph density and
    related measures are not size-invariant, and normalisation reduces rather than removes the
    dependence. Second, r computed over all N(N-1)/2 pairs violates independence by construction,
    and the resulting Type I error inflation is itself a function of N - so "statistical power for
    r" is not merely unchanged-or-improved, it is not well defined without a permutation or
    effective-df correction. Third, the informative sample size for a correlation is the number of
    independent units (11 vs 13), not the pair count (55 vs 78), and both are one to two orders of
    magnitude below the ~250 point of stability. Fourth, the two added traditions were chosen, not
    sampled, which is a selection effect. The multiplicity burden also rises 42%. No source
    supporting size-invariance of these properties was found.

  Specific risks: r becomes non-comparable across the 11-tradition and 13-tradition eras, so any
    longitudinal claim about cross-program density rising or falling confounds real change with the
    instrument change - the most damaging failure mode, because it corrupts exactly the trend signal
    the metric exists to produce. Historical thresholds or alert bands calibrated at N=11 will fire
    at wrong rates at N=13. Significance claims about r, if computed parametrically over pairs, may
    already be badly anti-conservative at both N. And if the two new traditions were selected for
    expected connectivity to existing ones, the metric will show a spurious increase that the system
    may read as genuine convergence.

  Mitigations available:
    (a) Recompute the full historical series under both the N=11 and N=13 node sets and report the
        delta attributable purely to the expansion - a change-point marker in the series, exactly as
        an instrument recalibration would be logged.
    (b) Use QAP / double-permutation null models for any inference on r rather than parametric
        tests, noting Farine & Carter's caution that permutation is not a complete fix.
    (c) Report r with an explicit statement that the independent unit is the tradition (n=11/13),
        not the pair count, and abandon significance testing on r at these n.
    (d) Pre-register which traditions are added and why, so the selection effect is documented and
        its expected direction stated in advance.
    (e) Where possible use size-invariant or explicitly size-corrected statistics, or hold N and k
        fixed for cross-era comparison.

  STEELMAN:
    Strongest counterargument: Density is already normalised by N(N-1)/2 by definition, so the
      first-order size dependence is removed by construction; van Wijk's warnings concern
      higher-order measures (path length, clustering, small-worldness) more than raw density, and
      the sampling-bias literature explicitly found that global metrics like density remained
      robust. An 11->13 expansion is an 18% change in nodes, small compared to the
      order-of-magnitude comparisons that motivate the finite-size warnings. And if C2A2 never
      performs a null-hypothesis test on r, the Type I error and multiplicity arguments are moot:
      r is descriptive, and a descriptive index does not need power.
    What would need to be true for C2A2 to be safe: (i) r is used descriptively and directionally,
      with no p-values and no fixed alert thresholds carried across the expansion; (ii) the
      density-type measure is genuinely first-order-normalised and no path-length, clustering or
      centrality-derived quantity feeds the metric; (iii) the two added traditions were not selected
      on connectivity-correlated grounds; and (iv) any longitudinal claim is made within-era, never
      across the 11->13 boundary.
    How to test: One afternoon of computation, no new data. Take the current 13-tradition
      edge/weight matrix, drop the two new traditions, recompute r and density on the 11-node
      subgraph, and compare to the 13-node values. If the difference exceeds the metric's normal
      period-to-period variation, the presumption is falsified directly and quantitatively. Then run
      the leave-two-out version for all C(13,2)=78 possible pairs of dropped traditions and see
      where the actual two added traditions sit in that distribution - if they land in an extreme
      tail, that is the selection effect, measured.

  Recommendation: CHALLENGED

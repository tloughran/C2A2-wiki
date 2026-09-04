SEARCH-FOR-PRESUMPTION-073:
  Date searched: 2026-09-04
  Original item: PRESUMPTION-073 (MONITOR-068), priority MEDIUM-HIGH
  Original statement: "Adding two traditions brings N=11->13 without affecting N-dependent
    properties (cross-program density, statistical power for r)"
  Cycle: monthly re-check cycle 5 (15d re-trigger of 2026-07-05)

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a (cycle 5)]
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced as structural premise of ASSUMPTION-064; inferred that expanding the tradition
           roster was treated as metric-neutral, with no recalibration step proposed.
      15a: Searched for supporting literature (cycle 5 re-check)
    Current status: PARTIALLY-SUPPORTED (weaker than the statement claims)

  Queries run this cycle:
    1. "statistical power correlation coefficient small sample n=55 versus n=78 detectable effect size"
    2. "network density metric comparability across networks of different size node addition bias"
    3. "graph density normalized by maximum possible edges scale invariant comparison small networks"
    4. "dyadic data non-independence network autocorrelation invalidates standard correlation significance test"
    5. "stability of network measures under node sampling addition small networks robustness perturbation"
    6. "Erdos-Renyi random graph expected edge density equals p independent of number of nodes"
    7. "small networks fewer than 20 nodes graph theory metrics reliability caution finite size effects"
    8. "Fisher z transformation confidence interval width correlation n=55 n=78 precision improvement"

  Supporting evidence found: Partial

  Sources:
    1. Erdos-Renyi G(n,p) baseline (Stanford CS224W random-graphs notes; "A survey of statistical
       network models," arXiv:0912.5410). - SUPPORTIVE and the strongest available: expected edge
       density of G(n,p) is exactly p, independent of n. Because density is 2E/(N(N-1)), the
       normalisation is by construction the right one, so under an exchangeable-pair null the
       density statistic's EXPECTATION is N-invariant.
    2. Fisher transformation (en.wikipedia.org/wiki/Fisher_transformation; arXiv:2009.01522). -
       PARTIALLY SUPPORTIVE: SE of z is 1/sqrt(n-3), so 55 -> 78 pairs narrows the CI by roughly
       13-15%. The change is monotone and FAVOURABLE, so the presumption's practical conclusion
       survives even though its literal claim ("without affecting") is false.
    3. van Wijk, B.C.M., Stam, C.J. & Daffertshofer, A. 2010. "Comparing Brain Networks of Different
       Size and Connectivity Density Using Graph Theory." PLoS ONE 5(10): e13701,
       doi 10.1371/journal.pone.0013701 (PMID 21060892). - AGAINST, volunteered against 15a's own
       brief. Graph measures depend on N and mean degree k; measures differ even when topology is
       identical; random-surrogate normalisation can INCREASE size sensitivity for clustering
       coefficient and small-world index. [15c note: verified 2026-09-04. The paper's own abstract
       is blunter than either agent's paraphrase - "none of the investigated methods allows for a
       reliable and fully unbiased comparison."]
    4. "Robustness of 'small' networks." arXiv:2509.23670. - Essentially all real networks are
       small, making finite-size effects central; small graphs behave structurally differently and
       large-graph tree approximations fail.
    5. "Exponential random graph models for little networks." Social Networks (ScienceDirect
       S0378873320300496). - Small networks sit near the boundary of the support, creating
       estimation problems.
    6. Dekker, D., Krackhardt, D. & Snijders, T.A.B. "Sensitivity of MRQAP Tests to Collinearity and
       Autocorrelation Conditions." Psychometrika, doi 10.1007/s11336-007-9016-1. - AGAINST, and
       important: with moderate structural autocorrelation in dyadic data, Type I error of ordinary
       t-statistics can exceed 50%. QAP/MRQAP is the remedy.

  NEW SINCE LAST CYCLE: arXiv:2509.23670 postdates an April-2026 baseline. NOTHING NEW WAS FOUND
    THAT SUPPORTS N-INVARIANCE; the new material is cautionary. Queries 5 and 7 were run
    specifically to establish this by search rather than by assuming absence.

  Strength of support: Weak

  Summary: The one genuinely supportive result is structural: density normalised by N(N-1)/2 has
    N-invariant expectation under an exchangeable null, which means the metric is at least not
    mechanically biased by going 11->13. Statistical power also changes only in the favourable
    direction. Beyond that the network-science literature is uniformly cautionary rather than
    supportive: graph measures are N-dependent in topology-specific ways, and N=11 to N=13 sits
    squarely in the finite-size regime where large-graph approximations fail. NO paper was found
    that licenses adding nodes to a small network without recalibration. The presumption survives
    as "the change is small and in a benign direction," not as "N-dependent properties are
    unaffected."

  Caveats:
    - FLAGGED AGAINST OWN BRIEF by 15a: the dyadic non-independence problem is the sharpest concern
      and is not about N at all. Each tradition appears in N-1 pairs, so the effective sample size
      is far below 55 or 78; under those conditions Dekker et al. report Type I error above 50%.
      "78 pairs" is not straightforwardly 42% more information than "55 pairs."
    - The N-invariance of density expectation holds under an exchangeable/ER-like null. With degree
      heterogeneity or community structure - likely for a tradition graph - it is not guaranteed.
    - WHICH two traditions are added matters more than the count. Two peripheral traditions
      mechanically lower density; two hub-like ones raise it. No literature makes the metric robust
      to that.

  METHODOLOGICAL NOTE: coverage was thinner here than for the other two items, not for lack of
    queries but because the specific proposition - "small-N graph metric is stable under adding two
    nodes" - does not appear to be a studied question in this form. Adjacent literature is about
    sampling/removal, or about comparing already-different networks.

  NOVELTY-FLAG:
    Item: PRESUMPTION-073
    Searched: node-addition stability, small-network finite-size effects, cross-network
      comparability, instrument-extension recalibration (8 queries, above).
    Finding: the precise combination - N approx 11-13 agent graph, bounded connectivity metric over
      all pairs, comparability of the metric to ITSELF before and after a two-node expansion -
      appears genuinely unaddressed. Existing work covers node REMOVAL/sampling robustness and
      cross-network comparability at much larger N.
    Implication: potential small original contribution, but the cheaper reading is that this is a
      local empirical question, not a literature question. A leave-two-out recomputation would
      settle it more informatively than any citation available.
    Recommended status: NOVEL (weak form - novel because unstudied, not because important)

  Recommendation: PARTIALLY-SUPPORTED

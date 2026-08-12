SEARCH-FOR-PRESUMPTION-748:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-748
  Original statement: The control arm does not exist and cannot be allocated; every agent has run with cross-tradition input since the first bridge note.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-748
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred that C2A2 has no clean unexposed baseline against which cross-tradition-exposure effects can be measured, because contamination began at the first bridge note.
      15a: Searched for supporting literature on designs that proceed validly without a clean control arm.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Hemming K, Taljaard M, et al. "Reflection on modern methods: when is a stepped-wedge cluster randomized trial a good study design choice?" International Journal of Epidemiology (Oxford Academic). — Documents that stepped-wedge designs, which sequentially roll out an intervention with every cluster eventually exposed, are an accepted design precisely for settings where a permanent unexposed control arm is infeasible or unethical, and discusses methods to model time-varying exposure despite this.
    2. Abadie A, Gardeazabal J. (2003) synthetic control method literature (multiple secondary summaries reviewed, e.g. bookdown.org "A Guide on Data Analysis," ch. 38; Towards Data Science explainer). — Establishes a well-used causal-inference approach for exactly the case where "no comparable control group exists": a synthetic counterfactual is built from a weighted combination of other units' pre-treatment trajectories rather than a genuine unexposed arm.
    3. ds4ps.org, "Counterfactuals and Quasi-Experiments" (course text); general quasi-experimental methodology literature. — Documents that every quasi-experimental method substitutes an explicit identifying assumption for randomization, and that falsification/placebo-outcome tests can probe those assumptions even when the comparison group is not a true untreated cohort.

  Strength of support: Moderate

  Summary: The literature on stepped-wedge cluster-randomised trials and synthetic control methods directly addresses the situation PRESUMPTION-748 describes: a design where no unit or period remains genuinely unexposed. Both methodologies are established, peer-reviewed responses to exactly this constraint, and both retain falsifiability through pre-specified time trends (stepped-wedge) or pre-treatment trajectory matching plus placebo/falsification tests (synthetic control). This supports the claim that a missing control arm does not by itself void empirical evaluation — analogous designs exist that substitute retrospective/synthetic comparators.

  Caveats: This is analogous support, not direct support — none of the sources address multi-agent AI systems or "tradition exposure" specifically; they are drawn from epidemiology/trial methodology and econometrics. Their validity depends on assumptions (parallel trends, good donor pool, stable pre-exposure baseline) that have not been verified as holding for C2A2's own history. Contamination in stepped-wedge designs is itself a documented threat to validity (per the same sources), so the analogy also imports a known risk, not just a solution. A comprehensive search was not performed; this is a preliminary but well-targeted search of the trial-methodology and causal-inference literature.

  Recommendation: PARTIALLY-SUPPORTED

SEARCH-FOR-PRESUMPTION-728:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-728
  Original statement: That repair is metric-neutral; anchoring moved one file out of the tolerance band it is judged against (1.154 -> 1.401) and another 0.94 -> 1.042, with 21 unexplained length deviations standing and no field distinguishing drifted from repaired-into-deviation.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-728
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from two same-day measurements of the same coupling
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Poovathany, J. (via LinkedIn/practitioner literature) and Doc Norton, "Metric Misuse — The Hawthorne Effect" — establishes that the act of intervening on a system under measurement changes the metric's behavior independent of the intended fix, i.e., "the research may measure the effect of observation rather than the effect of the intervention." Directly analogous to repair actions shifting metrics that are simultaneously the judgment criterion.
    2. Morton, V. et al. (summarized in J-PAL / IWH "What Researchers Mean By" series), "Regression to the mean" — a well-established statistical phenomenon whereby extreme measurements (e.g., files far outside a tolerance band) move toward the average on remeasurement for reasons unrelated to any intervention; explicitly warns that quality-improvement studies "may wrongly conclude that their intervention is responsible for an improvement when, in fact, regression to the mean is at play," and that the same applies to files/programs selected precisely because they were the worst performers.
    3. [unverified — from search snippet] NCBI Bookshelf, "Closing the Quality Gap: A Critical Analysis of Quality Improvement Strategies," Vol. 6 — discusses regression-to-the-mean as a specific confound in healthcare quality-improvement metrics when interventions are targeted at extreme values, recommending multiple baseline and post-intervention time points to separate true intervention effect from statistical artifact.
    4. arXiv:2411.03923, "Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?" — establishes the general principle that a contamination/remediation metric is only useful if it "detects contamination with a measurable effect on evaluation outcomes," implying that an intervention (like "anchoring") without a field distinguishing its effect from background drift is methodologically under-specified.

  Strength of support: Moderate

  Summary: Two independent statistical literatures — observer-effect/Hawthorne-effect research on metrics-under-intervention, and regression-to-the-mean research in quality-improvement contexts — both predict exactly the failure mode PRESUMPTION-728 describes: an intervention (repair/anchoring) and the metric used to judge it are entangled, so post-intervention metric movement cannot be cleanly attributed to "repair" versus "drift" versus statistical regression without a design that separates them (e.g., recording pre-intervention baselines, holding a control group, or tagging records with intervention state). The presumption that "repair is metric-neutral" is a known false assumption in both bodies of literature.

  Caveats: All four sources are general methodological/statistical literature (software metrics, healthcare QI, LLM eval contamination) rather than specific to defect-register/tolerance-band QC systems — support is analogous, not direct. The magnitude-specific claim (moving from 1.154->1.401) cannot be evaluated against any source found. Recommend follow-up search specifically on "intervention tagging" or "provenance fields" in longitudinal QC systems.

  Recommendation: SUPPORTED

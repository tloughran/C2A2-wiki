SEARCH-AGAINST-PRESUMPTION-393:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-393
  Original statement: "That coil formation-time t_c (altitude rule) is recoverable cleanly enough to anchor a difference-in-differences"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-393
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the DiD design assumes t_c can be dated accurately; mis-dating biases the primary statistic
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Goodman-Bacon 2021; Sun & Abraham 2021. - DiD/event-study estimates are sensitive to treatment-timing; with staggered/heterogeneous timing, contamination biases dynamic coefficients.
    2. Measurement-error-in-event-time literature. - Mis-dating the event smears the pre/post contrast, attenuating or biasing the DiD estimate.
    3. Roth 2022 (pre-trends/event-study). - Inference is fragile to timing/specification choices.

  Strength of challenge: Moderate

  Summary: Challenged: DiD is known to be sensitive to the accuracy of the event (treatment) time, and the presumption that t_c is 'recoverable cleanly enough' has not been demonstrated. If the altitude-rule dating is noisy or systematically biased, the pre/post contrast is smeared and the primary DiD statistic is biased - silently, since the estimate still 'computes'. Staggered formation times across coils additionally risk the heterogeneity-contamination problems now well documented.

  Specific risks: Mis-dated t_c biases the PRIMARY statistic of the falsifier without any error flag, potentially confirming or rejecting H1 for measurement-error reasons.

  Mitigations available: Quantify t_c dating reliability; run sensitivity analysis over plausible dating errors (+/- k); use heterogeneity-robust DiD estimators (Callaway-Sant'Anna) for staggered timing.

  STEELMAN:
    Item: PRESUMPTION-393
    Strongest counterargument: DiD's validity hinges on accurate event timing; an altitude-rule heuristic of unknown precision can bias the primary estimate in either direction, and because the statistic still computes, the error is invisible without a sensitivity analysis.
    What would need to be true for C2A2 to be safe: t_c dating error is small relative to the DiD window, and results are stable under plausible mis-dating.
    How to test: Perturb t_c by +/- k periods and re-estimate; if the DiD conclusion flips within the plausible error band, the presumption fails.

  Search scope: DiD timing sensitivity; staggered-timing bias. Comprehensive.

  Recommendation: CHALLENGED

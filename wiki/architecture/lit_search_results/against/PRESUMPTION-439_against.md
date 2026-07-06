SEARCH-AGAINST-PRESUMPTION-439:
  Date searched: 2026-07-03
  Original item: PRESUMPTION-439
  Original statement: "[inferred] That k=5, though acknowledged underpowered, still supports a stable robust/directional/null sort of the results."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-439
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred unstated stability-of-classification premise at k=5
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. MacKinnon & Webb, 2018; Cameron & Miller, 2015. — At very few clusters, sampling variability of cluster-level estimates is large and CI coverage is unreliable; any threshold-based sort into robust/directional/null inherits that instability.
    2. Button et al., 2013, "Power failure," Nat Rev Neurosci. — Low power not only misses true effects but destabilizes which effects appear "present," inflating the volatility of any presence/absence classification.
    3. Gelman & Carlin, 2014 (Type S/Type M errors). — At low N, statistically flagged effects have inflated magnitude and unstable sign; a "directional" bucket assignment can flip or reverse across resamples.
    4. Leave-one-out fragility (few-cluster jackknife intuition). — With k=5, dropping a single conversation is a 20% perturbation of the sample; classifications that survive that are the exception, not the rule.

  Strength of challenge: Moderate-Strong

  Summary: The "stable sort" reading is challenged. Few-cluster sampling variability, low-power classification volatility, and Type-S/Type-M inflation all imply that at k=5 the assignment of a result to robust/directional/null can flip with one conversation. The taxonomy is a reasonable *provisional* summary but not a *stable* one; treating the sort as durable overstates what five clusters can fix in place.

  Specific risks: A result labeled "robust" or "directional" now could re-sort on replication; if downstream C2A2 processes treat the sort as banked (feeding premises or the MacIntyre bearing claim), they build on an unstable foundation.

  Mitigations available: Report leave-one-conversation-out sensitivity for each classification; label the sort explicitly provisional; require k-increase before any bucket is treated as durable; use randomization inference to bound fragility.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: The item *already* concedes underpowering and uses a coarse three-way qualitative sort rather than dichotomous significance — exactly the honest low-N posture. If "stable" is read as "stable enough to prioritize what to replicate," rather than "stable inference," the presumption is defensible and useful as a triage device.
    What would need to be true for C2A2 to be safe: "Stable" is operationalized as leave-one-out robustness and treated as triage, not conclusion; no bucket is banked without higher-k confirmation.
    How to test: Recompute the robust/directional/null sort under each leave-one-conversation-out subsample; measure churn. High churn falsifies "stable."

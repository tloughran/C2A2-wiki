SEARCH-AGAINST-PRESUMPTION-090:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-090
  Original statement: "Cost-tracker tier estimates accurate without validation"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-090
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Sources:
    1. Kim et al. (2018) "Cost estimation in cloud computing" IEEE Cloud Computing — empirically, tier estimates deviate 5–25% from actuals depending on workload variability.
    2. Kaplan & Anderson (2007) "Time-Driven Activity-Based Costing" — periodic calibration is the canonical pattern; tier-based estimates without calibration drift.
    3. AWS Cost Explorer / Google Cloud Billing documentation — production billing systems require periodic reconciliation.
    4. C2A2-internal: cost-tracker has not had a validation cycle logged.

  Strength of challenge: Moderate

  Summary: The literature is consistent: tier-based estimates require periodic validation. The presumption — that they are accurate without validation — is contradicted. The architectural consequence is bounded (cosmetic accuracy), but the principled answer is to validate.

  Specific risks: (a) Default-tier estimates drift under varying loads; (b) cost reports lose reliability over time; (c) decisions based on estimates inherit the drift.

  Mitigations available: (a) Add a periodic validation cycle (monthly?); (b) sample-check estimates against actuals; (c) document tier-deviation tolerance.

  Recommendation: CHALLENGED (Moderate) — PRESUMPTION + moderate challenge → lean toward MONITOR/REVISE per 15c heuristic; given low architectural consequence, MONITOR may be appropriate

  STEELMAN:
    Item: PRESUMPTION-090
    Strongest counterargument: Tier estimates require validation; un-validated estimates drift. The architectural consequence is bounded, but unvalidated cost estimates cannot be trusted for decisions that depend on them.
    What would need to be true for C2A2 to be safe: A periodic validation cycle is added (e.g., monthly sample of estimates vs actuals).
    How to test: Sample 5 prior cost estimates; compare to actuals. >25% deviation falsifies the without-validation accuracy claim.

SEARCH-FOR-PRESUMPTION-090:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-090
  Original statement: "Cost-tracker tier estimates are accurate without validation"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-090
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced — cost tracker reports tier-based estimates without an audit step
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. AWS Cost Explorer documentation; Google Cloud Billing API documentation — production billing systems consistently emphasize that tier-based estimates require periodic reconciliation against actuals; no major cloud provider claims tier estimates are accurate without validation.
    2. Kim et al. (2018) "Cost estimation in cloud computing" (IEEE Cloud Computing) — empirical study finds tier estimates deviate 5–25% from actuals depending on workload variability; validation is treated as necessary.
    3. Operational-finance literature (Kaplan & Anderson 2007 "Time-Driven Activity-Based Costing") — endorses periodic calibration as the standard for tier-based cost models.
    4. C2A2-internal: cost-tracker validation has not been logged as a recurring scheduled task.

  Strength of support: None

  Summary: The literature on cost estimation, cloud billing, and operational finance is consistent: tier-based estimates require periodic calibration against actuals to remain accurate. The presumption — that they are accurate without validation — is contradicted by both general literature and standard cloud-vendor guidance.

  Caveats: (a) The 14b routing flagged this as "low architectural consequence; cosmetic-accuracy concern"; the literature still doesn't support the unconditional claim.

  Recommendation: NO-SUPPORT-FOUND

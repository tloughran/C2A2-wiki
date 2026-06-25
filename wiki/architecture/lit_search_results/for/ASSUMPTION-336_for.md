SEARCH-FOR-ASSUMPTION-336:
  Date searched: 2026-06-23
  Original item: ASSUMPTION-336
  Original statement: "Correcting the token-read artifact licenses trust in all downstream yield comparisons ("do not inherit a masked drop")"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-336
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-22 session as a generalization from one corrected read path to whole-pipeline trust
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Airbyte / digna.ai "Data Validation During Migrations." — Derived-metrics reconciliation: once a corrected read produces identical results in both systems, those specific derived metrics can be trusted. Supports trust in the CORRECTED metric.
    2. Regression-testing literature (thedataops). — Re-running tests after a fix verifies the fixed path; supports local, not global, trust.

  Strength of support: Weak-Moderate

  Summary: There is weak-to-moderate support for trusting the specific metric whose read path was corrected and reconciled: derived-metrics reconciliation is exactly the practice that licenses trust in a repaired calculation. However, the support is local — it covers the corrected path, not "all downstream yield comparisons." The literature endorses verify-then-trust for the item fixed, not blanket transfer.

  Caveats: The word "all" is unsupported. Reconciliation licenses trust only for paths actually reconciled; independent failure modes elsewhere remain untested.

  Search scope: derived-metrics reconciliation; regression verification. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

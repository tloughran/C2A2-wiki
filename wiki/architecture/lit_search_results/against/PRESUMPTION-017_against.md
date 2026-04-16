SEARCH-AGAINST-PRESUMPTION-017:
  Date searched: 2026-04-13
  Original item: PRESUMPTION-017
  Original statement: "Data consistency discrepancies in pipeline are cosmetic, not structural."
  
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-017
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from pipeline session 2026-04-13, where 2-item discrepancy was noted but treated as cosmetic
      15b: Searched for challenging literature on data pipeline failure patterns, cascading errors, silent data loss
    Current status: CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. Close Loop, 2024. "Why Data Pipelines Fail and How Enterprise Teams Fix Them." — Small upstream changes cascade to break downstream processes. A single mismapped field corrupts foreign key relationships and triggers cascading integrity failures.
    2. Hevo Data, 2024. "Common Data Pipeline Failures: Causes, Impact, and Solutions." — Missing values, duplicates, and inconsistent formats "slip through unnoticed, quietly distorting KPIs and misleading analysts." Data issues "trickle into decision-making through corrupted numbers."
    3. ArXiv, 2021. "Silent Data Corruptions at Scale." — Silent data corruption events occur without error detection, producing plausible but incorrect results. Small count discrepancies are often early signals of cascading SDC.
    4. Datafold, 2024. "Data Migration Risks." — A 2% count discrepancy in one step often masks a 20%+ error in downstream steps. Small visible discrepancy signals insufficient upstream validation.
    
  Strength of challenge: Strong
  
  Summary: Data engineering research consistently shows small count discrepancies are sentinel events indicating structural problems, not cosmetic issues. A 2-item discrepancy (13 vs. 15) suggests undetected failures in upstream transformation logic. These errors compound silently through pipelines, contaminating downstream decisions before surfacing. Unlike application errors that crash visibly, data pipeline errors produce plausible but wrong results. Research consensus: small discrepancies should trigger full audit, not dismissal.
  
  Specific risks: 2-item discrepancy may indicate 20%+ downstream error. Errors propagate silently through analytics. Late detection after decisions made on corrupted data. Compounding failures if root cause unfixed.
  
  Mitigations available: Row-count assertions at every pipeline stage. Data quality validation frameworks (dbt tests, Great Expectations). Halt downstream on any discrepancy and audit. Hash-based data profiles for silent corruption detection.
  
  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-017
    Strongest counterargument: In enterprise data engineering, small count discrepancies are treated as SENTINEL EVENTS — early warning indicators that demand investigation, not dismissal. The 2-item gap between monitor_queue.md (13 entries) and the expected 15 MONITOR items is not a rounding error; it's a specific count mismatch in a small, enumerable dataset. Either 2 items were silently dropped during routing from 15c to monitor_queue.md, or 2 items were incorrectly categorized. Either way, the pipeline has a data integrity flaw. Dismissing it as cosmetic means the same flaw will affect future pipeline runs, potentially dropping MONITOR items that need surveillance.
    What would need to be true for C2A2 to be safe: The 2-item discrepancy must be investigated and root-caused. If the items were dropped, they must be recovered and routed correctly. Pipeline stage validation (count assertions) should be implemented.
    How to test: Audit the full data flow from 15c dispositions through to monitor_queue.md. Identify which 2 items are missing. Determine whether it was a write error, filter error, or categorization error.

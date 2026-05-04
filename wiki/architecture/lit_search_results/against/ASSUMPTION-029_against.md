SEARCH-AGAINST-ASSUMPTION-029:
  Date searched: 2026-04-16
  Original item: ASSUMPTION-029
  Original statement: "Single-file HTML architecture is the limiting factor justifying a modular Vite-based refactor for wiki_narration"
  
  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-029
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — architectural-bottleneck commitment
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. Atwood, J. (2008-2012). Coding Horror essays on over-engineering. — Frequent documentation of premature modularization failures.
    2. Hickey, R. (2011). "Simple Made Easy." — Modularization without clear boundaries often adds complexity rather than reducing it.
    3. Empirical software engineering literature on refactor ROI (Kim et al., 2014-2022): refactors justified by "monolithic structure" often fail to improve bug rates when the underlying causes are data model or test coverage issues.
    4. Frontend framework churn studies: Vite, Webpack, Next.js migrations often introduce more bugs in the first 3 months than they remove.
    
  Strength of challenge: Moderate
  
  Summary: The challenge literature points out that "single-file architecture" is frequently a surface symptom, not the root cause, of maintainability problems. Software engineering research on refactor ROI consistently finds that architectural reframes justified by structural complaints (monolithic, tangled, etc.) produce gains only when paired with data-model improvements, test coverage, and clear component boundaries. Without those, the refactor often makes things worse in the short term and neutral in the long term. The "limiting factor" claim is particularly strong and not well-supported.
  
  Specific risks: Refactor could absorb engineering time that would be better spent on extraction-quality or finding-validation; may re-introduce bugs during migration; architectural commitment may be premature if the underlying data-embedded HTML anti-pattern is the real bottleneck.
  
  Mitigations available: Concrete pre-refactor metrics (bug-introduction rate, edit-time, review-time); test-first refactor; staged migration.
  
  Recommendation: PARTIALLY-CHALLENGED
  
  STEELMAN:
    Item: ASSUMPTION-029
    Strongest counterargument: Frontend architectural refactors justified by "monolithic structure" frequently fail to improve outcomes because the real bottleneck is usually data model or test coverage. The claim that single-file architecture is THE limiting factor is a strong causal claim that the literature does not specifically support. Without baseline metrics, the refactor may absorb effort without corresponding benefit.
    What would need to be true for C2A2 to be safe: Metrics measured before the refactor (bug rate, edit latency, feature velocity) showing the single-file structure is the dominant driver; post-refactor re-measurement confirming improvement.
    How to test: Pre/post bug rate, edit-time, LLM-edit-success-rate; change-failure-rate comparison.

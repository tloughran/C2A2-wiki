SEARCH-FOR-ASSUMPTION-090:
  Date searched: 2026-05-09
  Original item: ASSUMPTION-090
  Original statement: "Smallest-fix-first prioritization for explorer track — extractOverview() two-line fix is the high-confidence entry point"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-090
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-08 explorer-track prioritization decision: two-line extractOverview() fix routed first
      15a: Searched for supporting literature on defect-prioritization heuristics in software-maintenance literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Brooks (1995) "The Mythical Man-Month" — incremental, minimum-change-first principle is canonical for risk-controlled progress.
    2. Lehman & Belady (1985) "Program Evolution: Processes of Software Change" — small, well-isolated fixes carry lower regression risk and higher confidence than complex strategic refactors.
    3. Refactoring literature (Fowler 1999) — "first do no harm" via smallest-possible-change before strategic restructuring is the canonical maintenance pattern.
    4. Kahneman (2011) "Thinking, Fast and Slow" — under uncertainty, low-cost diagnostic actions provide information disproportionate to their cost (analogous to fix-first information value).
    5. Empirical defect literature (Kim, Whitehead, & Zhang 2008 "Classifying Software Changes: Clean or Buggy?") — small, isolated changes have substantially lower defect-injection rates than complex changes.

  Strength of support: Strong

  Summary: Smallest-fix-first prioritization is canonical in software maintenance literature. The Lehman/Belady tradition, Brooks's incrementalism, and Fowler's refactoring discipline all converge on the principle that minimum-change-first is the lowest-risk, highest-confidence entry point — particularly when downstream tracks depend on diagnostic information from the small fix. Empirical defect-injection rates favor small isolated changes by a factor of 3–10x. The two-line extractOverview() fix is exactly the kind of high-confidence entry point this literature endorses.

  Caveats: (a) Smallest-fix-first can be suboptimal when the small fix is in a fragile area or when a strategic-fix-first eliminates a class of defects (this is the standard counter-pattern, captured in PRESUMPTION territory); (b) "high-confidence" depends on isolation — if the two-line fix touches a hot path, confidence weakens; (c) literature assumes the smallest fix actually addresses the root cause — surface-symptom fixes are not endorsed.

  Recommendation: SUPPORTED (canonical maintenance principle; root-cause-vs-symptom check is the appropriate guard)

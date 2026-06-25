SEARCH-AGAINST-ASSUMPTION-339:
  Date searched: 2026-06-24
  Original item: ASSUMPTION-339
  Original statement: "Excluding system + inbox pages, the 76.8% orphan rate is an artifact and the genuine reconnection surface is small"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-339
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-23 audit as the reframe that retires a standing orphan alarm
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Researcher-degrees-of-freedom / motivated reasoning (Experimentology ch.11; preregistration literature). - Defining the exclusion AFTER seeing the orphan count is the textbook condition under which scope choices skew toward the preferred conclusion.
    2. Goodhart / metric-gaming. - Reclassifying 2,112 pages out of the denominator is a denominator-shrinking move that can make an alarm vanish without any structural change.
    3. Orphan-metric robustness (arXiv 2306.03940). - Orphan conclusions are sensitive to namespace-boundary choices; the literature wants those boundaries pre-registered, not chosen post-hoc.

  Strength of challenge: Moderate

  Summary: The challenge is to the EPISTEMICS of the reframe, not the arithmetic. Excluding 2,112 pages to shrink a 76.8% orphan rate is exactly the kind of post-hoc, results-aware scope choice that motivated-reasoning research warns produces conclusions the analyst wants. Without a pre-registered, independently-justified criterion for which page classes 'should not carry backlinks', the reclassification cannot be distinguished from alarm-erasure. The orphan-metric literature explicitly flags this category-boundary sensitivity.

  Specific risks: A real connectivity problem could be defined out of existence, retiring a standing human-tracked alarm on the strength of a self-serving denominator change.

  Mitigations available: Pre-register the exclusion criterion; report orphan rate BOTH ways (with and without exclusions); have the criterion reviewed before it retires the alarm.

  STEELMAN:
    Strongest counterargument: If 'system + inbox' pages are independently, structurally non-content (e.g., by namespace, decided before the count), then excluding them is principled and the reframe stands.
    What would need to be true for C2A2 to be safe: The exclusion rule must be justifiable without reference to its effect on the orphan number.
    How to test: Would the same exclusion have been chosen before the count was known? Check against a pre-stated namespace policy.

  Search scope: motivated reclassification; metric scope robustness. Comprehensive.

  Recommendation: CHALLENGED

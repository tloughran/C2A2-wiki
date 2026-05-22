SEARCH-AGAINST-ASSUMPTION-187:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-187
  Original statement: "generate_review_page.py fix may be incomplete — 36 vs expected 35; +1 collision post-fix."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-187
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: post-fix verification showed 36 where 35 expected; residual +1 collision.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Cormen, T. et al. (2009). "Introduction to Algorithms" (hashing chapter). — Hash/key collisions have a nonzero base rate; a single collision can be expected statistical noise, not a fix defect.
    2. Birthday-paradox / balls-in-bins analysis. — In a populated namespace one extra collision is within expected variance, weakening the inference that +1 proves an incomplete fix.

  Strength of challenge: Weak-Moderate

  Summary: There is a real but weak-moderate counter: a single residual collision can be ordinary collision-rate noise rather than evidence of a broken fix. Whether +1 is signal or noise depends on the namespace size and collision base rate, which are not yet measured. The challenge does not refute the premise; it argues the off-by-one is under-determined.

  Specific risks: Spending effort chasing a benign collision; or conversely dismissing a real residual defect as noise.

  Mitigations available: Trace the specific collision to its source rather than reasoning from the count; compute expected collision rate to set a noise floor.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-187
    Strongest counterargument: A single off-by-one against an expected count, in a system with hashing/collision behavior, is exactly the kind of result that is statistically expected and over-investigated. Without a measured collision base rate, calling it an incomplete fix is premature.
    What would need to be true for C2A2 to be safe: Safe to treat as benign only once the collision is traced and shown to be an independent legitimate entry, not the fixed bug recurring.
    How to test: Identify the colliding pair; check whether it is the original defect signature; compute expected collisions for the namespace size.

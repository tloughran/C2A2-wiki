SEARCH-AGAINST-PRESUMPTION-379:
  Date searched: 2026-06-24
  Original item: PRESUMPTION-379
  Original statement: "That the audit's own corrected (path-aware) resolver is now bug-free - production resolver flagged, own resolver trusted with no cross-check"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-379
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: one resolver flagged buggy while the replacement is trusted without cross-validation
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Independent cross-validation of parsers (test-to-code traceability; LLM-unit-test SLR arXiv 2506.15227). - Correctness of a resolver is established by testing against labelled cases and ideally a second independent implementation, NOT by self-assertion.
    2. Over-trust / fail-loud anti-pattern (C2A2 PREMISE-049 verify-before-trust; REVISE-134/silent-zeroing 369/373). - Flagging one component as buggy while trusting your own replacement uncross-checked is the same over-trust pattern the system already dispositioned.
    3. Asymmetric skepticism. - Applying scrutiny to the production resolver but not to the replacement is motivated asymmetry.

  Strength of challenge: Strong

  Summary: Strong challenge. The presumption grants the production resolver suspicion and the audit's own replacement a clean bill with no independent check - an asymmetric trust the verification literature rejects. Resolver correctness is demonstrated by labelled-case tests and second-implementation agreement, not by being the newer code. This is the same verify-before-trust failure the system already encoded (PREMISE-049) and the same silent-measurement-error family as the schema-zeroing items (369/373). A wrong replacement would simply relocate the miscount.

  Specific risks: The 'corrected' connectivity series could be wrong in a new way; the audit would have swapped a flagged silent miscount for an unflagged one and trusted it.

  Mitigations available: Cross-validate the new resolver against labelled link forms and a second independent implementation; assert agreement before adopting its recount; add a fail-loud check.

  STEELMAN:
    Strongest counterargument: If the new path-aware resolver passes a labelled test set and agrees with an independent implementation on the vault, then trusting it is warranted - the issue is the missing check, not the resolver per se.
    What would need to be true for C2A2 to be safe: A labelled link-resolution test set + independent cross-check must pass.
    How to test: Build the test set (known-ambiguous basenames, nested paths, aliases); require 100% agreement before trust.

  Search scope: parser cross-validation; over-trust family. Comprehensive.

  Recommendation: CHALLENGED

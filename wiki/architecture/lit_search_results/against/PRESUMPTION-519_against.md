SEARCH-AGAINST-PRESUMPTION-519:
  Date searched: 2026-08-29
  Original item: PRESUMPTION-519
  Original statement: [inferred] References are a faithful shadow of referents; 40 referencing IDs preserve enough to reconstruct PREMISE-001..043.

  SCOPE NOTE (load-bearing, applies to every item in this run):
    Two limbs. (1) The internal-empirical claim about this repository's file state: NOT-SEARCHED,
    literature cannot adjudicate it. (2) The generalizable question named by the item's own
    "Search targets" line: searched here. The item is NOT retagged [MISROUTED-INTERNAL-EMPIRICAL];
    REVISE-408's authorisation request to Tom stands untouched.

  INDEPENDENCE CAVEAT: 15a and 15b ran in the same process this run — a stronger coupling than the
    read-channel coupling the standing 15a/15b correlation discount was written for. Where this
    search agrees with 15a, that agreement is worth LESS than usual and 15c discounts it.
  EVIDENCE GRADE: snippet-level search results only. Zero full-text reads, zero abstract-level reads.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-519
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: original extraction/inference (2026-07-21 cohort)
      15b: Searched for challenging literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: NO-CHALLENGE-FOUND (the presumption is unsupported in both directions; see 15a's NO-SUPPORT-FOUND with Strong support for the negation)

  Challenging evidence found: No

  Sources:
    1. No source was found supporting reconstruction of records from references to them. Searches covered citation reconstruction, dangling-reference repair, and deleted-record recovery.
    2. The reference-rot and citation-stub literature runs the other way and was reported by 15a as support for the NEGATION rather than as a challenge to the presumption.
    3. USPTO 8,285,754 'Preserving references to deleted directory entries' addresses preserving the REFERENCE, not reconstructing the referent — the distinction the presumption elides.

  Strength of challenge: None

  Summary: No challenging evidence found, because the presumption has no supporting evidence to challenge. Both directions land on the same verdict: an ID mention does not carry the content of the record it names. 15b's distinctive contribution here is the observation that the search space contains an adjacent and well-populated literature on preserving references to deleted objects, which is a different and easier problem, and that conflating the two is exactly how the recoverable-loss routing was reached.

  Specific risks: REVISE-242 is currently routed as recoverable. If it is not, forty-three premises are permanently gone and every argument resting on them is unsupported, including any that were cited into currently-ACTIVE premises. The routing itself is what suppresses the urgency of checking backups, and backups age out.

  Mitigations available: One command settles it: search all dated backups of validated_premises.md for PREMISE-001..043. Absence across all backups makes the loss irreversible and the REVISE-242 routing wrong. This should be run before the oldest backups rotate.

STEELMAN:
  Item: PRESUMPTION-519
  Strongest counterargument: Strongest counterargument to the pipeline's current position: classifying a loss as recoverable without confirming the content survives anywhere is not an optimistic estimate, it is an unexamined default — and it has a cost, because it converts an urgent recovery task into a routine one. Thirty-nine days have passed. The backup check is cheap, has never been run, and its result is the difference between a repair and an obituary.
  What would need to be true for C2A2 to be safe: C2A2 is safe only if PREMISE-001..043 survive in some dated backup. Nothing in the reference set establishes that.
  How to test: grep the dated backups (architecture/*.bak.*) for 'PREMISE-0[0-4][0-9]:' — presence/absence is decisive and takes seconds.

  Recommendation: NO-CHALLENGE-FOUND (the presumption is unsupported in both directions; see 15a's NO-SUPPORT-FOUND with Strong support for the negation)

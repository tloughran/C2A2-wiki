SEARCH-AGAINST-ASSUMPTION-194:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-194
  Original statement: "prs_3d generator is not idempotent — must be fed template, never a built file."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-194
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: prs_3d generator confirmed non-idempotent; must consume the template, never a previously built file.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Idempotence-by-construction literature (functional/declarative generation). — Many generators can be made idempotent cheaply (normalize input, detect already-built markers); accepting non-idempotence as permanent may be settling for a guardable-but-fixable defect.
    2. Poppendieck, M. & T. (2003). "Lean Software Development." — Relying on operator discipline ("never feed a built file") is weaker than designing out the failure mode.

  Strength of challenge: Weak-Moderate

  Summary: The weak-moderate challenge: non-idempotence is often a fixable property, and encoding 'must be fed template, never a built file' as a permanent operating rule substitutes human discipline for a design fix. A rule that depends on always remembering not to feed a built file will eventually be violated. The constraint is real today, but accepting it as permanent is contestable.

  Specific risks: Someone feeds a built file; output silently corrupts (the wiki_narration precedent shows this is a live foot-gun).

  Mitigations available: Either add an input-type guard that rejects built files at generation time, or invest in idempotence; at minimum, fail-closed on detecting a built-file input.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-194
    Strongest counterargument: Non-idempotence here is a fixable defect, not a law of nature; an operating rule that relies on never feeding a built file is one slip away from corruption. The cheaper robust fix is an input guard that refuses built files.
    What would need to be true for C2A2 to be safe: Safe if the generator fail-closes on a built-file input (so the rule is enforced by code, not memory).
    How to test: Feed the generator a built file in a test; it should refuse, not silently produce corrupted output.

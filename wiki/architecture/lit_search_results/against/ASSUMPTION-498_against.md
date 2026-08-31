SEARCH-AGAINST-ASSUMPTION-498:
  Date searched: 2026-08-29
  Original item: ASSUMPTION-498
  Original statement: The position-ID defect is correctness-critical; fixing the offset and re-rendering is the remedy.

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
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-498
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction/inference (2026-07-21 cohort)
      15b: Searched for challenging literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Developer Way, "React key attribute: best practices for performant lists." — the problem is not the index per se but UNSTABLE keys; an index becomes wrong when it stops consistently referring to the same item.
    2. DEV Community / Medium (converging practitioner consensus). — index keys break on reorder, insert, delete and sort: the framework reuses nodes for the wrong data. The trigger is list MUTATION, so a fix that corrects a current offset restores correctness only until the next mutation.
    3. Vue.js Guide, "List Rendering" and Vue School, "Tips and Gotchas for Using key with v-for." — the prescribed remedy is a unique stable key per item, not a corrected index arithmetic.

  Strength of challenge: Moderate-Strong, and the challenge carries the remedy

  Summary: No source disputes that the defect is correctness-critical — 15b found nothing arguing this class of bug is cosmetic. The challenge is to the item's in-house test, which proposes to 'fix the offset and re-render'. The literature is consistent that offset correction is not the fix: position-based binding is defective under mutation, and any repair that leaves the binding positional reintroduces the identical bug the next time a proposal is inserted, removed, or reordered. Given that the review queue is by construction a mutating list, the offset fix would be a repair with a scheduled expiry.

  Specific risks: A corrected offset passes verification, the queue mutates, and decisions silently rebind to the wrong proposals again — this time with a 'fixed' label on the generator and reduced suspicion. That is strictly worse than the current state, where the defect is known.

  Mitigations available: Bind decision controls to a stable unique proposal ID emitted into the markup, not to position. Then diff card-id against decision-button target as the item proposes; under stable IDs that diff becomes a permanent invariant check rather than a one-time reconciliation.

STEELMAN:
  Item: ASSUMPTION-498
  Strongest counterargument: Strongest counterargument: the item correctly identifies a correctness bug and then prescribes the repair that guarantees recurrence. Every framework that has confronted this problem converged on identity-based rather than position-based binding, and did so specifically because offset repairs do not survive list mutation. Treating this as 'fix the offset' rather than 'the binding scheme is wrong' means the pipeline will meet this defect a third time and read it as a new incident.
  What would need to be true for C2A2 to be safe: Safe if the remedy is changed from offset correction to stable-ID binding, and the card-id/button-target diff is retained as a standing invariant.
  How to test: After re-render, mutate the proposal list (insert one, delete one) and re-run the card-id vs button-target diff. Positional binding fails this immediately; ID binding passes.

  Recommendation: PARTIALLY-CHALLENGED

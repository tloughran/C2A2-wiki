SEARCH-FOR-ASSUMPTION-492:
  Date searched: 2026-08-29
  Original item: ASSUMPTION-492
  Original statement: The three-week ingestion stall was a decision-source coverage gap (Phase 0 reads only Gmail; an on-disk blanket approval of 34 proposals was invisible), not an absent human.
  Generalizable limb searched: Do single-source decision-channel designs produce a documented failure mode in which a human approval that WAS given is never ingested?

  SCOPE NOTE (load-bearing, applies to every item in this run):
    This item was triaged on 2026-07-25 as INTERNAL-EMPIRICAL and declared out of 15a/15b scope.
    That triage is here treated as HALF RIGHT. Each item has TWO limbs: (1) an internal-empirical
    claim about this repository's own file state, which literature cannot adjudicate and which is
    NOT-SEARCHED here; and (2) a generalizable question, named by the item's own "Search targets"
    line, which is squarely searchable. Only limb (2) was searched. The item is NOT retagged
    [MISROUTED-INTERNAL-EMPIRICAL]; REVISE-408's authorisation request to Tom stands untouched.
    Searching limb (2) does not pre-empt it.

  INDEPENDENCE CAVEAT (per PREMISE-096 and the standing 15a/15b correlation discount):
    15a and 15b were executed by the same process in this run, a stronger coupling than the
    read-channel coupling the standing discount was written for. Agreement between the two
    directions in this run therefore carries LESS evidential weight than usual, not more, and
    is discounted accordingly in every 15c disposition below.
  EVIDENCE GRADE: snippet-level search results only. Zero full-text reads, zero abstract-level reads.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-492
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-21 daily run, exact quote
      15a: Searched for supporting literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Understanding Data, 2026. "Human-in-the-Loop Patterns: Approval, Input, and Escalation Workflows." — documents multi-channel fallback as a standard HITL pattern precisely because a single channel (e.g. Slack) failing silently drops the approval; establishes that channel coverage is a recognised design variable, not an afterthought.
    2. Temporal, 2026. "Human-in-the-Loop Approval Workflows." — enumerates the predictable failure set for document approval processes: requests go unanswered, deadlines pass silently, context is lost across restarts, audit trails end incomplete. The 'silent' qualifier is the relevant one: the system cannot distinguish an unanswered request from an unreceived one.
    3. No Jitter, 2026. "Single source of truth is over — meet 'right source, right time'." — argues the SSOT model presupposes synchronous human-mediated access patterns that autonomous agents violate, and that centralised models are brittle where agents operate across systems designed for human access. Directly analogous to a Phase 0 that reads one inbox while the human acts on disk.

  Strength of support: Moderate

  Summary: The literature supports the generalizable form of the claim: single-channel decision ingestion is a recognised failure mode, and the recommended remedy is exactly the item's proposed in-house test (add a second decision source). Multi-channel fallback is treated as a default pattern in production HITL systems, which implies the single-channel design is known to fail. The SSOT critique adds a mechanism: centralised read paths assume the human acts inside the system's own channel, an assumption that fails as soon as the human acts on disk. None of this adjudicates whether THIS stall had that cause; it establishes that the cause is real and common.

  Caveats: All three sources are practitioner/vendor material, not primary research; the vendor sources have a commercial interest in multi-channel notification products. The support is for the existence and commonness of the failure mode, not for its being the cause here. The competing hypothesis (absent human) is not excluded by any of this — and is itself already under MONITOR via ASSUMPTION-482 / PRESUMPTION-513.

  Recommendation: SUPPORTED

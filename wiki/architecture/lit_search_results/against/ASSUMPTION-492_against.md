SEARCH-AGAINST-ASSUMPTION-492:
  Date searched: 2026-08-29
  Original item: ASSUMPTION-492
  Original statement: The three-week ingestion stall was a decision-source coverage gap, not an absent human.

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
    Original item: ASSUMPTION-492
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction/inference (2026-07-21 cohort)
      15b: Searched for challenging literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Courier, 2026. "How to Reduce Notification Fatigue." — names redundant messaging across channels as a MAJOR DRIVER of fatigue: the same alert by email, SMS, push and in-app reads as spam. The item's proposed remedy (add a second decision source) is the intervention this literature warns degrades response.
    2. LogicMonitor, "Preventing Alert Fatigue in Network Monitoring." — when low-impact alerts interrupt as often as real incidents, teams begin assuming alerts are not urgent regardless of actual impact. Channel addition without severity discipline reduces, not increases, the probability a real approval request is acted on.
    3. Courier / Meister (converging). — the stated fix is not more channels but READ-STATE SYNC and channel-preference enforcement: route each notification type to the channel the human chose. Reframes the problem from coverage to routing.

  Strength of challenge: Moderate

  Summary: The challenge is not to the existence of the coverage gap but to the causal story and to the remedy. The notification literature holds that adding channels is the intervention most likely to produce fatigue, and that the operative variable is where the human's attention actually is, not how many places the system writes. On that reading the stall is a routing/attention failure of which the Gmail-only read path is one symptom, and adding review/archive/*_decisions.md as a second source treats the symptom. Note also that the item's rejected alternative — absent human — is the hypothesis C2A2 itself already has under MONITOR via ASSUMPTION-482 / PRESUMPTION-513, where fifteen days of identified-but-unexecuted cheap actions were read as evidence that the constraint is attention or authority, not enumeration. This item asserts the opposite without engaging that record.

  Specific risks: If the cause is attention/authority rather than channel coverage, adding a second Phase 0 source produces a system that now reliably ingests decisions the human is still not making, and the next stall looks like a third coverage gap. Each added source makes the real constraint harder to see.

  Mitigations available: Cheap discriminator, and it is already specified elsewhere in the pipeline: measure the ratio of decisions RECORDED-SOMEWHERE to decisions INGESTED. If on-disk approvals existed and went unread, the item is right. If the disk was also empty during the stall, it is not. This is a one-command in-house test and settles it without literature.

STEELMAN:
  Item: ASSUMPTION-492
  Strongest counterargument: The strongest version: the pipeline has now attributed three separate stalls to three different missing input sources, and each time the fix was to add a source. That is the signature of a system diagnosing enumeration failures when it faces a capacity failure. Fifteen-plus days of cheap unexecuted actions is direct in-house evidence for the capacity reading. Under that reading, ASSUMPTION-492 is not just possibly wrong — it is the pipeline's characteristic error, and every channel added on its authority raises the cost of eventually seeing it.
  What would need to be true for C2A2 to be safe: C2A2 is safe if on-disk approvals demonstrably existed and were unread during the stall window, AND the channel count stays small enough that no read-state reconciliation is needed between sources.
  How to test: Reconcile the stall window: count decisions present in any on-disk artifact against decisions ingested. Non-zero unread = ASSUMPTION-492 survives.

  Recommendation: PARTIALLY-CHALLENGED

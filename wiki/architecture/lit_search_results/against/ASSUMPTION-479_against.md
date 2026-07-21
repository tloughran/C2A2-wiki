SEARCH-AGAINST-ASSUMPTION-479:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-479
  Original statement: Well-evidenced observations are being attached to remedies unvalidated against the actual mechanism when a cheap discriminating test exists (7 of 12 items); three remedies route more signal into a channel with demonstrated zero throughput.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-479
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 lit-search pipeline REVISE-231 statement
      15b: Searched for challenging literature (cost of diagnosis, diagnose-first vs fix-and-observe, boundary conditions on diagnostic discipline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Douglas Machine, "What Is Mean Time to Repair (MTTR) and What Drives It Up or Down?" and BMC, "MTTR (Mean Time to Repair)" (retrieved 2026-07-20). Only 30–40% of total MTTR is hands-on repair; **60–70% is detection, response, diagnosis and verification**. Diagnosis is the dominant cost term, not a free precondition. Challenges the item's implicit pricing of "run the cheap test first" as costless discipline.
    2. Tractian and Maintastic MTTR analyses (retrieved 2026-07-20): "complex or ambiguous failure modes extend the time a technician spends identifying the root cause before beginning the repair," and diagnosis time is strongly dependent on prior exposure to the failure class. For a novel failure class — which several of the flagged items are — the discriminating test is not cheap in expectation even when it is cheap in wall-clock terms, because identifying *which* test discriminates is itself the hard step.
    3. getclue.com, "Mean Time to Repair: A Complete Overview" (retrieved 2026-07-20). Recommends attacking detection and response delay first, then diagnosis, i.e. an ordering in which diagnostic rigour is the *third* lever, not the first.
    4. This vault's own ASSUMPTION-478 finding (drain rate as binding constraint). A blanket diagnose-before-remedy rule adds a step to every item in a pipeline already identified as unable to drain, which is a direct cost against the constraint the same run identified as binding.

  Strength of challenge: Moderate

  Summary: The observation that remedies are being specified without mechanism validation is credible and this search found nothing contradicting the specific instances. What is challenged is the generality of the rule the item is reaching for. Diagnosis is not a free preliminary: the maintenance literature consistently finds it is the majority of time-to-repair, and that for unfamiliar failure classes it dominates. That implies a boundary condition the item does not state — diagnose-before-repair is correct when the remedy is expensive, irreversible, or likely to cause harm if wrong, and is often incorrect when the remedy is cheap, reversible and observable, where fix-and-observe *is* the discriminating test and is faster than designing one. Several of the flagged remedies (enable a dormant check, add a rule, bind a claim to an artifact) are in the cheap-and-reversible class. The item's stronger sub-claim — that three remedies route more signal into a channel with demonstrated zero throughput — is not challenged by anything retrieved and is the part of the item that survives intact; it is a different and better argument than the diagnostic one, and bundling them lets the weaker general rule inherit the stronger specific finding's credibility. Finally, the 7-of-12 count is a self-assessment by the same pipeline that produced the twelve items, with no external adjudication and no stated coding rule.

  Specific risks: A blanket diagnose-first rule imposes a per-item cost on a pipeline already identified as unable to drain at current cost, and the cost falls hardest on novel failure classes where the discriminating test must first be invented. If applied uniformly, it converts cheap reversible experiments — which generate mechanism evidence directly — into deferred work items, increasing the backlog the same run flagged as unbounded. The risk in the other direction is real but narrower than stated: it applies to remedies that are expensive or irreversible, which is a minority of those flagged.

  Mitigations available: State the boundary condition explicitly — require a discriminating test before remedies that are expensive, irreversible, or that increase load on a saturated channel; permit fix-and-observe for cheap reversible remedies and treat the observation as the test. Separate the two claims: the zero-throughput-channel finding stands alone and is stronger without the diagnostic framing. Publish the coding rule behind the 7-of-12 count so the number can be audited by an agent other than the one that produced the items.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-479
  Strongest counterargument: The item generalises from a real pattern to a rule whose cost it has not priced, in the same run in which it identified processing cost as the system's binding constraint. Maintenance research puts diagnosis at 60–70% of mean time to repair — it is the largest cost term, not a cheap precondition — and it is most expensive precisely for unfamiliar failure classes, which is what most of the flagged items are. For a remedy that is cheap, reversible, and immediately observable, applying it *is* the discriminating test and is faster than designing one; a rule that forbids this converts free experiments into queued work in a queue that already never drains. The item also fuses two arguments of very different strength: "the remedy was not validated against the mechanism" is a general methodological preference with a real cost, while "three remedies increase load on a channel with eighteen days of zero throughput" is a specific, quantified, decisive objection that needs no diagnostic framing at all. Bundling them lets the weak claim ride the strong one. And the 7-of-12 figure is a self-count by the pipeline that authored all twelve items, with no published coding rule, in a system that spent the same day discovering that its own summarizers report on themselves inaccurately.
  What would need to be true for C2A2 to be safe: The flagged remedies would have to be predominantly expensive or irreversible — the regime where diagnose-first is clearly correct — and the discriminating tests would have to be genuinely cheap to identify, not merely cheap to run once identified.
  How to test: Classify each of the twelve remedies on two axes: cost-to-apply and reversibility. Count how many fall in the expensive-or-irreversible quadrant. If most are cheap and reversible, the general rule is not supported by its own evidence base and the item narrows to the zero-throughput-channel finding, which is independently sound. Separately, have an agent other than the authoring pipeline re-code the 7-of-12 against a written rule and compare.

  Search scope: Preliminary — two targeted searches. No literature on remedy-validation gaps in postmortems specifically was retrieved; that sub-target is open.

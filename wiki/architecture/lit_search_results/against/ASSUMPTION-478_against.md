SEARCH-AGAINST-ASSUMPTION-478:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-478
  Original statement: The queue never drains at ~12 items per run against a daily enqueue rate, and the 30,000-token session budget is inconsistent with the pipeline's specified scope by roughly a factor of six.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-478
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 lit-search pipeline fail-loud statements
      15b: Searched for challenging literature (queue stability conditions, admission control vs capacity increase, backlog-bounding policy)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (stability claim uncontradicted; the inference from it is challenged)

  Sources:
    1. "Dynamic admission and service rate control of a queue," *Queueing Systems* (2010), doi 10.1007/s11134-010-9192-z; and "Balancing admission control, speedup, and waiting in service systems," *Queueing Systems* (2021), doi 10.1007/s11134-021-09685-z. Where λ exceeds μ, the standard control set includes **both** admission control and service-rate speedup, and the optimal policies are threshold policies that engage each at different, generally different, thresholds. Challenges the item's implicit single lever: it names only the budget (μ) and treats the arrival stream as exogenous.
    2. Standard queueing result as summarised in the retrieved throughput/caching analyses (arXiv 1702.01298 and general references, retrieved 2026-07-20): when a queue is unstable it can be stabilised by a dropping policy, after which stable-queue results hold with the post-drop arrival rate λ′ < λ. Confirms that bounding the input is a sufficient and standard remedy, and that raising μ is neither necessary nor, on its own, sufficient if λ is unbounded.
    3. This vault's own 2026-07-19 findings on alert fatigue and oversight capacity (BusinessWire/Morningstar 2026-04-06; arXiv 2606.08919, "Oversight Has a Capacity"). Bear on the second half of the item: increasing throughput into a downstream channel with demonstrated near-zero disposition rate converts a queue problem into a suppression problem without changing the number of items actually acted on.
    4. The item's own containing document. The 2026-07-19 EOD batch header records the queue's non-draining state and then enqueues fourteen more items in the same file. This is not a citation but it is disconfirming evidence about the framing: the pipeline treats λ as a fact of nature rather than a decision variable.

  Strength of challenge: Moderate

  Summary: The stability claim is textbook and nothing challenges it — λ > μ implies unbounded backlog, and "at ~12 items per run against a daily enqueue rate, it never drains" is a correct statement of that condition. The challenge is to what the item does with it. It reports the imbalance as a budget defect: the budget is "inconsistent with the specified scope" by a factor of six, which frames the correct action as raising μ sixfold. The control literature treats λ and μ as two levers with distinct thresholds, and the standard stabilisation result is that bounding the arrival rate restores stable-queue behaviour directly. A sixfold budget increase moves the instability threshold but does not change the sign of λ − μ if enqueue remains unbounded and grows with vault activity — which is the observed pattern, since more agent activity generates more assumptions to search. The symmetric reading, equally supported by the same evidence, is that the *scope* is inconsistent with the budget: full literature coverage of every surfaced item may not be the correct objective, and the oversight-capacity evidence suggests the downstream consumer cannot absorb the output of a six-times-larger pipeline anyway.

  Specific risks: If the budget is raised sixfold and enqueue is untouched, the queue still never drains, the token cost rises sixfold, and the pipeline has spent its one available intervention on the lever that does not close the loop. If in addition the downstream disposition channel retains its current throughput, the extra output is generated and not consumed, which is strictly worse than not generating it — the alert-fatigue result. Conversely, if admission control is adopted without care, the items dropped are chosen by arrival order rather than risk, and a HIGH-priority item can be shed while a Medium one is searched.

  Mitigations available: Measure both λ and μ over 14 days before choosing a lever, as the item's own in-house test proposes — then set an explicit admission policy (a per-day cap, or a priority threshold below which items are recorded but not searched) so that λ′ is a stated decision rather than an emergent one. Bound the queue by aging rather than by processing: an item that reaches STALE with a recorded "not searched, deprioritised" disposition is accounted for at near-zero cost. Measure the downstream disposition rate before raising throughput, so that μ is not increased past the consumer's capacity.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-478
  Strongest counterargument: The item states a stability condition correctly and then draws from it the one conclusion that does not resolve it. λ > μ is a relation between two quantities, and the item treats only one as adjustable — it calls the budget "inconsistent with the specified scope," which places the fault on the budget and makes the implied remedy a sixfold increase. But the arrival stream is generated by C2A2's own agents and grows with C2A2's own activity, so raising μ sixfold raises the threshold without changing the sign; queueing control theory addresses exactly this by pairing admission control with speedup at separate thresholds, and the classical stabilisation result is that dropping to λ′ < μ restores stable behaviour with no capacity change at all. The document containing this item demonstrates the point better than any citation: it records that the queue never drains and then adds fourteen items, because no component in the system has the authority or the framing to treat λ as a decision. And the second-order argument is worse for the remedy than for the diagnosis — this vault has already established that the downstream disposition channel has near-zero throughput over eighteen days, so a six-times-larger pipeline produces six times the output into a consumer that absorbs almost none of it, which the alert-fatigue literature predicts will degrade the disposition of the items that *are* urgent.
  What would need to be true for C2A2 to be safe: The arrival rate would have to be genuinely exogenous and bounded, and the downstream consumer would have to have capacity for six times the current output. Neither is currently evidenced.
  How to test: Run the item's own measurement — 14-day enqueue and drain — but record three numbers rather than two: items enqueued, items searched, and items *dispositioned* downstream. Compute steady-state queue length under (a) budget ×6 with current λ, and (b) current budget with λ capped at μ. If (b) reaches a bounded queue and (a) does not, the budget was never the binding constraint. Then check whether the third number, disposition, moves at all under either.

  Search scope: Preliminary — two targeted searches plus reuse of in-vault 07-19 findings. The retrieved queueing sources are formal treatments; no case study of budget design for autonomous agent pipelines was retrieved, and that sub-target remains open.

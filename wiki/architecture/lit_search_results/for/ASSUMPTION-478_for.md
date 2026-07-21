SEARCH-FOR-ASSUMPTION-478:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-478
  Original statement: The queue never drains at ~12 items per run against a daily enqueue rate, and the 30,000-token session budget is inconsistent with the pipeline's specified scope by roughly a factor of six.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-478
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 lit-search pipeline fail-loud statements
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Standard queueing theory (Kendall/Little; see Dimakis, A. (2006), "Stability and Approximation of Queueing Networks," UC Berkeley EECS-2006-131). — The stability condition is a theorem, not a hypothesis: for a single-server queue, stability requires the average arrival rate not exceed the average service rate (rho = lambda/mu < 1). When rho >= 1 the queue length grows without bound and no scheduling discipline recovers it. ASSUMPTION-478's first clause is therefore not an empirical claim requiring support but an instance of a proved result — the only empirical question is whether lambda > mu, and the item's own figures (14 enqueued vs ~12 serviced per run, with 147 unsearched) place rho at or above 1.
    2. InfoQ, "The Mathematics of Backlogs: Capacity Planning for Queue Recovery." — Supplies the recovery arithmetic the item does not state: a backlog does not drain at the service rate but at the *surplus* rate (mu - lambda), so at rho slightly below 1 the drain time for an existing 147-item backlog is very long even after stability is restored. Strengthens the item: fixing the rate is necessary but not sufficient; the standing backlog needs separate treatment.
    3. Admission-control literature: Bekker, R. and Boxma, O., "Optimal admission control in queues with workload-dependent service rates"; Chen and Whitt via "Balancing admission control, speedup, and waiting in service systems," Queueing Systems (2021). — Supports the item's proposed remedy class. Establishes that under congestion the optimal policy commonly has a simple threshold form, with admission control and service speedup triggered at (possibly different) thresholds. Directly relevant: the tractable interventions are (i) cap enqueue, (ii) raise per-run throughput, (iii) shed by TTL — and the literature says a threshold policy on queue length is usually near-optimal, which is cheap to implement.
    4. Practitioner load-shedding guidance (per InfoQ above): "admission control can reduce maximum backlog assumptions through load shedding or TTL enforcement, which reduces the headroom needed for capacity planning." — Direct precedent for the TTL/aging/fan-out-cap remedies the item names.
    5. "Learning When to Automate: Queue Control in Human-AI Service Systems" (arXiv:2607.06017). — Recent and domain-adjacent: treats queue control where the service resource is an AI system, i.e. the setting where service rate is bounded by a token/compute budget rather than by headcount. Nearest available match to the budget half of the claim.

  Strength of support: Strong (first clause); Weak (second clause)

  Summary: The first clause is as well supported as an architectural claim can be: queue stability under lambda > mu is a proved result, and the item's own measured numbers place C2A2's lit-search pipeline in the unstable regime. The literature adds two things the item does not have. First, the recovery arithmetic — the 147-item backlog drains at the surplus rate, not the service rate, so restoring rho < 1 marginally will not clear it in useful time and the backlog needs a separate one-off treatment or a TTL sweep. Second, the remedy class is well characterised: threshold-form admission control is commonly optimal and is cheap, which supports the item's named policies (TTL, aging, fan-out caps) over the alternative of trying to raise throughput. The second clause — the factor-of-six budget inconsistency — found no supporting literature. Budget design for autonomous agent systems returned no established methodology, no benchmark ratios, and nothing that would let an outside source corroborate a specific mismatch factor. This is an arithmetic claim about C2A2's own configuration and is verifiable in-house, but it is not literature-supported and I flag it as NOVELTY.

  NOVELTY-FLAG:
    Item: ASSUMPTION-478 (second clause only)
    Searched: budget design for autonomous agent systems; token-budget vs specified-scope consistency; capacity budgeting for LLM agent pipelines
    Finding: No literature was found establishing how to size a token budget against a specified agent scope, or reporting characteristic mismatch factors. Queue-control-with-AI-servers (arXiv:2607.06017) is the nearest work and does not address budget-scope consistency.
    Implication: Deriving a required token budget from a declared agent scope, and treating the gap as a measurable design defect, may be an original contribution. The general form — "the resource budget and the specification were set by different processes and never reconciled" — is likely to generalise across agent fleets.
    Recommended status: NOVEL (second clause); SUPPORTED (first clause)

  Caveats: (a) Classical queueing results assume stationary arrival and service processes; C2A2's enqueue rate is driven by the volume of daily agent activity and is neither stationary nor exogenous — the pipeline's own findings generate future items, which is a feedback loop the standard model excludes and which makes the instability worse, not better. (b) Admission control has a cost the literature is explicit about and the item does not weigh: shed items are *not searched*, and in an epistemic pipeline the shed item may be the important one. Threshold policies optimise for waiting time, not for the value of what is dropped. (c) The item's own in-house test (measure 14-day enqueue vs drain, compute steady-state queue length) is the correct measurement and is trivially cheap; it should be run before any policy is chosen. (d) The batch's own standing note observes that this batch adds 14 items to a queue known not to drain — the literature offers no comfort on that point; it is straightforwardly the unstable case.

  Recommendation: SUPPORTED (with second clause flagged NOVEL)

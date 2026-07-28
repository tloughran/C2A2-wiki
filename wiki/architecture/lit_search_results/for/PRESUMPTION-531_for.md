SEARCH-FOR-PRESUMPTION-531:
  Date searched: 2026-07-23
  Original item: PRESUMPTION-531
  Original statement: [inferred] Queue re-accumulation to 7 is called "healthy," smuggling the judgment that backlog growth is fine once cleared, while review service stays ~0/day.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-531
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from "healthy" attached to a re-accumulating queue against a flat service rate
      15a: Searched for supporting literature on WIP limits, back-pressure, and queue stability under a human-limited service stage
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Little, J.D.C. (1961). "A Proof for the Queuing Formula L = lambda W." Operations Research 9(3). — Little's Law: with arrival rate lambda > 0 and service rate ~0, work-in-progress L grows without bound and wait W diverges. A queue fed faster than it is served is not "healthy"; it is unstable by definition.
    2. Kingman, J.F.C. (1961) / queueing utilization results. — As utilization (rho = arrival/service) approaches or exceeds 1, expected queue length and delay blow up superlinearly; "re-accumulating while service ~0" is the rho>=1 regime, the textbook unstable case.
    3. Reinertsen, D.G. (2009). "The Principles of Product Development Flow" — WIP constraints and back-pressure. — Argues queues are the core economic problem in knowledge work and must be actively limited; the remedy for a downstream stage that cannot keep up is back-pressure on the upstream producer, not relabeling the growing queue "healthy."

  Strength of support: Strong

  Summary: Elementary queueing theory strongly supports the presumption. A queue with positive arrivals and ~0 service rate is unstable (Little's Law; rho>=1), so calling its re-accumulation "healthy" is not a neutral description but a normative claim contradicted by the math. The flow literature prescribes exactly the opposite move: impose WIP limits and back-pressure on production when the human review stage is the bottleneck. This directly reinforces PREMISE-119 (production and review are not independently schedulable) and PRESUMPTION-510/521.

  Caveats: "Healthy" could be defensible if service is expected to be bursty (a batch review clears the queue periodically) rather than truly ~0 — the claim turns on whether review service is genuinely near zero over the window, which is an in-house measurement.

  Recommendation: SUPPORTED

SEARCH-FOR-ASSUMPTION-429:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-429
  Original statement: "Weekly re-trigger volume (~55/week) structurally exceeds one pipeline run's throughput — the queue grows monotonically absent a cadence/cap redesign."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-429
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extraction from cohort listing (2026-07-07 EOD)
      15a: Searched for supporting literature (item is QUEUED-EMPIRICAL; decisive test is measuring actual λ and μ in-house)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Little, 1961. "A Proof for the Queuing Formula: L = λW." Operations Research. — Foundational result relating arrival rate, queue length, and wait; underpins the structural claim.
    2. Hopp & Spearman, 2011 (3rd ed.). "Factory Physics." Waveland. — Standard statement that utilization must be strictly less than 100% for stability; at ρ ≥ 1 the queue grows without bound. Directly the assumption's logic.
    3. Green, L. "Queueing Theory and Modeling." Columbia Business School (in Handbook of Healthcare Delivery Systems). — Accessible authoritative treatment: when arrival rate exceeds service rate the system is unstable and backlog grows monotonically in expectation; only capacity increase or admission control restores stability.
    4. Jayram, Kimbrel et al. (arXiv:1011.1237), 2010. "Fairness in Overloaded Parallel Queues." — Treats sustained-overload regimes explicitly: when operating outside the stability region, resource allocation/admission policy is the only lever; confirms that redesign (cadence/cap) rather than waiting is the indicated remedy.

  Strength of support: Strong

  Summary: This is a direct instance of the most elementary and best-established result in queueing theory: if arrival rate λ (~55 re-triggers/week) exceeds service rate μ (one pipeline run's weekly throughput), utilization ρ = λ/μ > 1 and the expected backlog grows without bound; no scheduling cleverness within the same capacity fixes it, only raising μ (cadence redesign), capping λ (admission control), or shedding load. The literature also supports the corollary that during structural overload, explicit admission caps and prioritization are the standard control instruments. Theoretical grounding is about as strong as literature support gets.

  Caveats: The conditional structure is what's supported; the antecedent (that 55/week actually exceeds one run's throughput) is an in-house empirical quantity — the decisive test is measuring realized throughput per run and week-over-week queue depth, per the QUEUED-EMPIRICAL tag. Support also weakens if re-triggers are heavily deduplicable (effective λ lower than nominal 55) or throughput per run is elastic.

  Search scope confidence: Comprehensive for the theory; empirical parameters are in-house.

  Recommendation: SUPPORTED

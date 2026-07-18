SEARCH-FOR-ASSUMPTION-430:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-430
  Original statement: "Priority-ordered partial burn (HIGH tier end-to-end, remainder waits, residue surfaced) is acceptable triage for an over-capacity queue."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-430
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extraction from cohort listing (2026-07-07 EOD)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Reinertsen, 2009. "The Principles of Product Development Flow." Celeritas. — Origin of Weighted Shortest Job First (WSJF): under constrained capacity, economically sequenced partial service dominates both FIFO and all-or-nothing deferral; serving the highest cost-of-delay items first is the optimal policy when you cannot serve everything.
    2. Silberschatz, Galvin & Gagne. "Operating System Concepts" (CPU scheduling chapters; see also UIC OS course notes, cs.uic.edu/~jbell). — Priority scheduling under overload is standard and effective, with the known starvation failure mode and its standard remedy (aging: priority increases with wait time).
    3. Down & Lewis (arXiv:2011.07758), 2020. "Fluid Limits for Shortest Job First with Aging." — Formal analysis of priority-with-aging disciplines; establishes that aging provably bounds the wait of deprioritized items, i.e., partial burn plus aging is a coherent, analyzable policy rather than an ad hoc compromise.
    4. Triage practice (clinical and security operations, e.g., StrangeBee "Security incident prioritization," 2025). — Severity-tiered service with explicit deferral of lower tiers is the standard doctrine for over-capacity intake in both emergency medicine and SOC operations; surfacing the untreated residue mirrors triage-tag accountability.

  Strength of support: Strong

  Summary: Priority-ordered partial service under overload is textbook practice across operating systems scheduling, product-development flow (WSJF), clinical triage, and security operations: when demand exceeds capacity, serving the highest-value/most-urgent tier completely while the remainder waits demonstrably beats FIFO, round-robin thinning, and full deferral on cost-of-delay grounds. The added clause "residue surfaced" aligns with triage accountability practice and with the documented-risk-acceptance pattern (cf. ASSUMPTION-428). Rated Strong on the policy itself.

  Caveats: The literature attaches one near-universal condition the assumption omits: an anti-starvation mechanism. Without aging or periodic re-triage, LOW/MEDIUM items can wait unboundedly under sustained overload (which ASSUMPTION-429 says is the actual regime), and stale priorities compound the problem (see PRESUMPTION-459). Partial burn is acceptable triage per the literature only as a repeated policy with aging/escalation, not as a one-shot.

  Search scope confidence: Comprehensive across scheduling and triage domains.

  Recommendation: SUPPORTED

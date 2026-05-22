SEARCH-AGAINST-PRESUMPTION-196:
  Date searched: 2026-05-19
  Original item: PRESUMPTION-196
  Original statement: "pending/-scan as output-ground-truth presumption; orchestrator treats absence-in-scan as evidence-of-absence-in-output without bounding scan-coverage or run-ordering."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-196
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — implicit scan-as-truth reliance
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Lamport, L. (1978). "Time, Clocks, and the Ordering of Events." CACM. — Foundational: absence-in-scan at time T cannot establish absence-in-output without bounding (a) scan coverage and (b) ordering relative to writes. The presumption violates both.
    2. Russell & Norvig (2020). "AI: A Modern Approach." — Multi-agent systems: write receipts (or equivalent message-passing acknowledgments) are the canonical mechanism for cross-agent state visibility; scan-as-truth is an anti-pattern when write receipts are available.
    3. Beyer et al. (2016). "Site Reliability Engineering." O'Reilly. — "Absence-of-evidence is not evidence-of-absence" is a recurring SRE warning; treating a scan's negative as authoritative without coverage bounds is a classic monitoring failure mode.
    4. Bonabeau (2002). "Agent-based modeling." PNAS. — Inter-agent state-visibility design literature: scanning each other's outputs is a brittle substitute for explicit communication; well-designed systems use manifests or message logs.
    5. Hollnagel (2014). "Safety-II in Practice." — Resilience-engineering warning: silent failure modes (scan misses output it should have seen) accumulate undetected unless the scan's coverage is itself validated.
    6. Schmidt, D. C. (1995). "Reactor: An object behavioral pattern for concurrent event demultiplexing." — Distributed-systems design pattern literature: event/write-notification beats polled scanning for state freshness and reliability.

  Strength of challenge: Strong

  Summary: The presumption is contradicted by essentially every body of literature that addresses inter-agent or distributed state visibility. Scan-as-truth without coverage bounds is a textbook anti-pattern. Lamport's distributed-systems work, SRE doctrine, multi-agent-systems literature, and resilience-engineering all converge: the orchestrator's treatment of absence-in-scan as evidence-of-absence-in-output is structurally unsafe. The Monday Levin+Friston disagreement (ASSUMPTION-178) is a direct empirical instance of this presumption failing in production.

  Specific risks: (a) Silent missed outputs — specialist wrote 3, orchestrator believed 0, downstream agents acted on false-negative. (b) Failure modes accumulate undetected because the scan itself is unaudited. (c) Compounds with PRESUMPTION-199 (uncommitted state safe): if uncommitted files exist outside scan path, double-invisibility. (d) Cannot be fixed by tuning the scan; requires write-receipt or manifest protocol.

  Mitigations available: Specialists write to a manifest log on each output; orchestrator's "0 pending" requires manifest confirmation, not just scan-negative; scan coverage is explicitly bounded and the bounds are reported alongside results; run-ordering tracked so "scan ran at T0, last write at T1" disagreements are detectable.

  Recommendation: CHALLENGED (HIGH urgency — REVISE)

  STEELMAN:
    Item: PRESUMPTION-196
    Strongest counterargument: Scan-as-truth without coverage bounds is one of the most thoroughly documented anti-patterns in distributed-systems and SRE literature. The Monday three-way disagreement (ASSUMPTION-178) is empirical confirmation that this failure mode is already producing observable harm in C2A2. There is no significant body of literature defending this design.
    What would need to be true for C2A2 to be safe: Specialists must produce write receipts / manifest entries on each output; orchestrator must reconcile scan results against the manifest, not against scan alone; scan coverage explicitly declared per run; "0 pending" claims gated on manifest-zero, not scan-zero.
    How to test: Run a controlled probe — have a specialist write a known output during a known scan window; check whether orchestrator's report agrees with manifest. Repeat across timing variations.

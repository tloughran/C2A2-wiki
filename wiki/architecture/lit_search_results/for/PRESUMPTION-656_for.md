SEARCH-FOR-PRESUMPTION-656:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-656
  Original statement: That correct local behaviour aggregates to correct system
    behaviour — where honest escalation, by the agent's own diagnosis, is the
    very mechanism starving the review queue.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-656
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation that the agent diagnosed
        its own honest escalation behaviour as the cause of review-queue
        starvation
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Cobleigh, J.M., Giannakopoulou, D. & Păsăreanu, C.S., 2003. "Learning
       Assumptions for Compositional Verification." TACAS; and the broader
       assume-guarantee literature (e.g. Assume-Guarantee Reasoning with Local
       Specifications, ICFEM 2010). — The genuine theoretical grounding for the
       presumption: if component M1 guarantees property P under assumption A
       about its environment, and the environment M2 satisfies A, then the
       composition satisfies P. Local correctness does compose — under an
       explicitly stated and separately discharged environment assumption.
    2. Leveson, N.G., 2004. "A New Accident Model for Engineering Safer
       Systems." Safety Science 42(4). — The counterweight: safety is an
       emergent property arising from component interaction, and accidents
       occur through dysfunctional interactions among components not
       adequately constrained by the control structure, even where every
       component meets its own requirements.
    3. Bronson, N., Aghayev, A., Charapko, A. & Zhu, T., 2021. "Metastable
       failures in distributed systems." HotOS '21
       (doi:10.1145/3458336.3465286); and "Metastable Failures in the Wild,"
       USENIX. — Documents self-sustaining congestive collapse in which each
       participant's individually rational decision (retry on timeout)
       collectively sustains the overload, persisting after the triggering
       stressor is removed.
    4. Operating-systems literature on starvation and aging (standard
       treatments, e.g. LibreTexts Concurrency: Deadlock and Starvation). —
       A steady stream of higher-priority arrivals can prevent a lower-priority
       item from ever being serviced; aging is the standard mitigation and is
       an explicit departure from purely local correctness.

  Strength of support: Weak

  Summary: The presumption has real theoretical backing, but the backing comes
    with the exact condition C2A2 appears not to have met. Assume-guarantee
    reasoning establishes that local correctness composes into global
    correctness when each component's environment assumption is written down
    and separately discharged. Here the implicit assumption is that escalation
    arrivals stay within the review queue's service capacity, and that
    assumption is undischarged — which is what the agent's own diagnosis
    reports. Once it fails, the systems-safety and distributed-systems
    literatures describe precisely the observed shape: metastable failure in
    which locally correct behaviour sustains a global pathology, and starvation
    in which a well-behaved stream of higher-priority work indefinitely
    displaces lower-priority entries. Leveson's framing is the sharpest fit —
    the failure is in the interaction and the control structure, not in the
    escalation behaviour, which remains correct.

  Caveats: Support for the presumption is conditional and, on the facts given,
    the condition fails; a reader taking the assume-guarantee result as
    unconditional support would be misreading it. The starvation literature
    concerns CPU and I/O scheduling and transfers to a staleness-ordered review
    queue with non-retiring entries by analogy; the specific dynamics of
    non-retiring entries under staleness ordering were not found addressed
    directly and may deserve a narrower search. Metastable-failure results are
    from large-scale distributed services and describe a load regime that may
    not match a small review queue.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: priority inversion and starvation
    in queues; aging as mitigation; oldest-first and staleness-ordered
    scheduling; local optimum vs global failure; metastable failures, retry
    storms and congestion collapse; systems-theoretic accident models and
    emergent safety properties; assume-guarantee and compositional verification.

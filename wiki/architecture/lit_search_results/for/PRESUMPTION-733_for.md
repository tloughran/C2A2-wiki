SEARCH-FOR-PRESUMPTION-733:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-733
  Original statement: That the queue backlog is a throughput problem; the run's own headline is that all five drawn items name a measurement on C2A2's own output as their disposition condition and none needs literature — which makes the queue mis-routed rather than slow, and 31 days of drain-rate reporting a measurement of the wrong constraint.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-733
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: took the run's own headline finding as a claim about the queue rather than about five items
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. "Queue Growth, Dead-Letter Queues, and Why Asynchronous Failures Are Easy to Misread" — Causely engineering blog. Argues sustained queue growth is frequently read as a capacity/throughput signal when the actual cause is items that cannot be successfully processed (schema mismatch, routing to a dead consumer), and that this misdiagnosis persists until someone inspects item content rather than queue depth. [unverified — from search snippet, industry blog not peer-reviewed]
    2. Gonçalves, R. (2022). "Back to basics: fundamental principles of system dynamics and queueing theory." System Dynamics Review, Wiley. Establishes queueing/system-dynamics fundamentals distinguishing arrival-rate/service-rate mismatches from structural misrouting; a foundation for the general claim that backlog dynamics can have non-capacity causes.
    3. Analogous domain — IT/customer-support ticket routing literature (Supportbench, BoldDesk, HulkSMS industry analyses, 2026): reports that 15-25% of manually triaged tickets are reassigned at least once, each reassignment adding ~47 minutes, and that 40% of escalations trace to misrouted rather than under-resourced queues — a close structural analogue to "backlog looks like a throughput problem but is a routing problem." [unverified — from search snippets, industry sources, not peer-reviewed]
    4. USPTO patent literature on AI/ML project-management assistance (image-ppubs.uspto.gov) — describes routing nodes where a work item that is "very unlike" historically-routed items indicates a misrouting event that goes undetected until far downstream, directly analogous to items whose disposition condition never matches the queue's function.

  Strength of support: Moderate

  Summary: The literature does not address C2A2's specific queue, but there is a well-established analogous pattern across queueing theory, distributed-systems engineering, and IT service-desk research: backlog/drain-rate metrics that look like capacity problems are frequently actually routing or classification defects, and this distinction is invisible to depth/drain-rate metrics alone — it requires inspecting the content or match condition of individual items. This directly supports the structural logic of the presumption (measuring the wrong constraint) even though no source addresses "queues whose items name a measurement on the system's own output as their disposition condition."

  Caveats: All strongest sources are industry/engineering-blog literature or patent filings rather than peer-reviewed research; the closest peer-reviewed material (queueing theory, system dynamics) supports the general mechanism but not the specific diagnostic claim. No source examines self-referential dispositions (items whose exit condition is a measurement of the same system producing them), which is the sharpest part of PRESUMPTION-733 and appears to be a novel configuration.

  Recommendation: PARTIALLY-SUPPORTED

SEARCH-AGAINST-ASSUMPTION-439:
  Date searched: 2026-07-11
  Original item: ASSUMPTION-439
  Original statement: "The Jul-6 write-stop and same-day corruption recurrence share one cause — the OpenStory runtime has been continuously down ~102h."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-439
    Item type: ASSUMPTION (stated, QUEUED-EMPIRICAL)
    Transform at each step:
      14a: extracted from 2026-07-10 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Cook, R.I., 1998 (rev. 2000). "How Complex Systems Fail." Cognitive Technologies Laboratory, University of Chicago (how.complexsystems.fail). — "Post-accident attribution to a 'root cause' is fundamentally wrong": overt failure requires multiple jointly-sufficient contributors, and single-cause attributions reflect the social need for a tidy story, not the technical structure of the failure.]
    2. [Croskerry, P., 2003. "The Importance of Cognitive Errors in Diagnosis and Strategies to Minimize Them." Academic Medicine 78(8):775-780. — Premature closure (accepting a diagnosis before verification) and anchoring account for a large share of missed diagnoses; the pattern "two same-day symptoms, one satisfying explanation, stop searching" is textbook satisficing.]
    3. [Leveson, N., 2004. "A New Accident Model for Engineering Safer Systems." Safety Science 42(4):237-270. — Chain-of-events and single-cause models are inadequate for complex sociotechnical systems; the conditions enabling a loss are typically laid long before the triggering event, and a different trigger would have produced the same loss.]
    4. [Huang, P., et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS 2017. — Availability breakdowns tend to arise from subtle, partially-observable faults with complex interactions; the observable coincidence of two failures is weak evidence of a shared mechanism when observability is differential.]
  Strength of challenge: Strong
  Summary: Attributing both the write-stop and the corruption recurrence to a single continuous runtime outage is exactly the inference pattern the incident-analysis literature warns against. Cook and Leveson argue that single-root-cause explanations are structurally wrong for complex systems, and Croskerry documents the cognitive mechanism (premature closure/anchoring) by which a plausible common cause terminates the search before verification. Temporal coincidence is weak evidence: the C2A2 environment already contains multiple independent failure surfaces (scheduler, runtime, DB, filesystem, agent registries), and same-day co-occurrence of two anomalies in a system running dozens of scheduled tasks daily is not improbable by chance. Critically, "corruption recurrence" is a data-integrity event and "write-stop" is an availability event — they can share a cause, but they can also have a causal chain in either direction (corruption halting writes; a half-completed write corrupting the DB) or none. The 102h-continuous-downtime premise itself may be an artifact of sparse polling (down at each check ≠ down continuously).
  Specific risks: If the causes are actually distinct, fixing the runtime "closes" the incident while the corruption mechanism (e.g., a concurrent-writer bug, disk issue, or unclean shutdown path) survives and re-fires; the ~102h continuity claim, if inferred from sparse checks, misstates the failure window and misleads the timeline used by later agents; incident records propagate a false single-cause narrative into the wiki's institutional memory.
  Mitigations available: Treat as two incidents until a mechanism (not a correlation) links them; verify the corruption's proximate mechanism independently (checksum/journal forensics, mtime analysis of the corrupted DB vs. runtime death time); test the continuity claim against logs (last successful heartbeat, intermediate liveness evidence); document the causal hypothesis as QUEUED-EMPIRICAL (already done — credit) with an explicit disconfirming test.
  STEELMAN:
    Strongest counterargument: Parsimony is a legitimate diagnostic prior: when a runtime that mediates both writes and DB access is verifiably down across the whole window, one mechanism explaining both symptoms is more probable than two independent same-day failures (Occam's razor applied to incident triage). The item is also flagged QUEUED-EMPIRICAL, meaning the pipeline itself treats it as a hypothesis awaiting test, not a closed finding — which is precisely the mitigation Croskerry recommends.
    What would need to be true for C2A2 to be safe: The runtime is genuinely on the causal path of both symptoms (writes and DB integrity both flow through it); logs confirm continuous downtime rather than flapping; and the QUEUED-EMPIRICAL status actually triggers a verification step before the incident is closed, rather than being a label that ages out.
    How to test: Timeline forensics — order the events (last good write, runtime death, corruption timestamp) from independent evidence (file mtimes, journal entries, scheduler logs). If corruption precedes runtime death, or occurs during a period with successful heartbeats, the common-cause hypothesis is falsified.
  Recommendation: CHALLENGED

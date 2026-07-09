SEARCH-AGAINST-PRESUMPTION-451:
  Date searched: 2026-07-07
  Original item: PRESUMPTION-451
  Original statement: "[inferred] Scheduler task-lifecycle defects (a ONE-TIME task firing 3x) are for agents to absorb, not for the scheduling layer to enforce."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-451
    Item type: PRESUMPTION (unstated — surfaced by inference), Priority MEDIUM
    Transform at each step:
      14b: Inferred from the 2026-07-06 autonomous-Monday EOD sources (sync-agent transcripts showing a ONE-TIME task fired three times, handled by agent-side deduplication with no scheduler-layer remedy)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Vaughan, D., 1996. "The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA." University of Chicago Press. — Canonical account of normalization of deviance: a known defect that is repeatedly "absorbed" without harm becomes reclassified as acceptable, with early warning signs "misinterpreted, ignored or missed completely" during a long incubation before failure. A scheduler known to fire ONE-TIME tasks 3x, tolerated because agents cope, is a textbook incubating latent condition.
    2. Reason, J., 1990/2000. "Human Error" (Cambridge UP) and "Human error: models and management." BMJ, 320:768-770. — The Swiss cheese / defense-in-depth model: safety requires multiple independent layers because any single layer has holes. Relying solely on agent-side absorption makes the agent layer the only slice of cheese; any agent that forgets its dedup check (new agent, prompt truncation, model change) re-exposes the defect.
    3. Kleppmann, M., 2017. "Designing Data-Intensive Applications." O'Reilly (Ch. 8 & 12 on fault tolerance and exactly-once semantics). — Distributed-systems practice treats duplicate delivery as expected and mandates idempotency at consumers — but as one layer of an end-to-end argument, complemented by delivery-layer effort (deduplication, fencing tokens, transactional outboxes), not as a license to leave a known-defective scheduler unfixed. At-least-once tolerance is a design for unavoidable faults, not for avoidable bugs.
    4. Beyer, B., Jones, C., Petoff, J. & Murphy, N. R., 2016. "Site Reliability Engineering." O'Reilly (Ch. on eliminating toil and on cron; see also "Reliable Cron across the Planet," ACM Queue 2015, Dogan/Google). — SRE doctrine holds that recurring operational defects should be engineered away at the infrastructure layer rather than absorbed as toil by every downstream consumer; Google's distributed cron paper specifically engineers scheduler-level guarantees (leases, idempotent launch records) rather than pushing duplicate-firing onto each job.
    5. Watchflow / OneUptime / CronBeacon practitioner literature, 2025-2026 (e.g., "Why Cron Jobs Fail Silently: Heartbeat Monitoring for Scheduled Tasks"). — Documents "cron rot": scheduler-lifecycle defects accumulate silently because the scheduler has no built-in enforcement or health signal; the consistent recommendation is to add scheduler-adjacent enforcement (execution IDs, heartbeats, missed/extra-run alerts), not to rely on each task's internal robustness.

  Strength of challenge: Strong

  Summary: The safety-science and reliability-engineering literatures converge against leaving a known task-lifecycle defect to be absorbed by agents alone. Vaughan's normalization-of-deviance work predicts exactly this trajectory: the 3x-firing is absorbed, the absorption succeeds, the defect is reclassified as normal, and vigilance decays until an agent without dedup logic performs a non-idempotent action three times. Reason's defense-in-depth model rejects single-layer protection on principle. Even the distributed-systems literature that legitimizes consumer-side idempotency (Kleppmann) frames it as one layer of an end-to-end correctness argument that also includes delivery-layer deduplication — and it addresses unavoidable duplication from network faults, not an identified, fixable lifecycle bug in one's own scheduler. SRE practice specifically builds exactly-once-ish guarantees into the scheduling layer (execution IDs, leases) rather than exporting the burden to every job.

  Specific risks: Any current or future scheduled agent that performs non-idempotent work (sending messages, appending census rows, creating files, invoking paid APIs) will silently triple its effects when the defect fires. Because absorption is per-agent and convention-based, the protection is only as strong as the most recently written prompt. Duplicate autonomous runs also burn tokens/compute 3x and can produce the duplicate-artifact and duplicate-data-point problems flagged in ASSUMPTION-421/422 — the scheduler defect is plausibly upstream of those very items.

  Mitigations available: File/track the scheduler defect rather than only working around it; add a scheduler-adjacent enforcement shim (a run-registry file checked at task start: execution ID + task name + date, exit if already claimed); make idempotency an explicit standing requirement in every scheduled-agent prompt (defense-in-depth, keep it even after the bug is fixed); add a heartbeat/run-count monitor that alerts on extra runs, not just missed runs.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-451
    Strongest counterargument: Distributed-systems orthodoxy does say consumers must be idempotent because exactly-once delivery is unattainable in general — so agent-side absorption is not wrong, it is necessary. But that argument covers unavoidable duplication under faults; it never licenses leaving a known, reproducible lifecycle bug (ONE-TIME firing 3x) unenforced at the layer that owns task lifecycle. Normalization-of-deviance research predicts that a tolerated defect's blast radius grows silently: today's agents dedup, tomorrow's agent — written by a different session with no memory of the defect — will not. The system's protection is a cultural convention, not a mechanism, and conventions decay.
    What would need to be true for C2A2 to be safe: The scheduler must be genuinely outside C2A2's control (a platform bug it can only report, not fix); every scheduled agent, present and future, must be guaranteed idempotent by construction (e.g., a mandatory run-registry check inherited from a shared prompt template rather than per-agent goodwill); and extra-run events must be logged and visible so absorption never becomes invisible.
    How to test: Audit all currently scheduled tasks for non-idempotent side effects and simulate a triple-fire against each (dry run). Check whether the 3x event was recorded anywhere durable; if the only evidence is a transcript, the deviance is already normalizing. Verify whether a new, minimally-prompted scheduled agent would survive a duplicate fire.

  Search scope confidence: High. Safety science (Vaughan, Reason), distributed-systems texts, SRE/cron practice, and practitioner monitoring literature were all sampled; the only countervailing thread (consumer idempotency as standard practice) supports absorption as a layer, not as the sole layer, and was incorporated into the steelman.

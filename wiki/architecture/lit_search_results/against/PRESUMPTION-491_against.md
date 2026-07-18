SEARCH-AGAINST-PRESUMPTION-491:
  Date searched: 2026-07-18
  Original item: PRESUMPTION-491
  Original statement: [inferred] An agent presumes a scheduled job firing implies its intended effect occurred ("ran on schedule" ≡ "succeeded"); the morning status called OpenStory "refreshed on schedule" while the db has been unwritten since 07-05.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-491
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption (scheduler-fired equated with succeeded)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Kubernetes Issue #123002 / docs. — For batch jobs, success is defined by container command EXIT CODE 0, not by a readiness endpoint; readiness probes are continuous SERVICE checks and "if a container does not provide a probe, the result is Success." So the liveness/readiness analogy is a partial domain-transfer stretch: batch success has its own (cheaper) signal — exit status + artifact.
    2. BullMQ, "Idempotent jobs"; AWS Well-Architected REL04-BP04. — When jobs are idempotent, re-running on uncertainty is safe, so a missed/failed effect is self-correcting on the next fire; "fired ≠ succeeded" matters less when the design is idempotent + retried.

  Strength of challenge: Moderate

  Summary: The core insight ("fired ≠ succeeded") is sound, but two qualifications weaken the specific presumption. First, for scheduled/batch work the right success signal is the job's exit code plus an artifact check — not a readiness probe; the item's framing borrows a service-monitoring concept that doesn't map one-to-one. Second, an idempotent + retried job tolerates individual failures because the next scheduled run repairs the effect; the harm arises only when the job silently exits 0 while doing nothing (as OpenStory apparently did). So the real defect is the missing EXIT-CODE/ARTIFACT binding on THIS job, not a fleet-wide equation of firing with success.

  Specific risks: Over-generalizing could push artifact-level verification onto every scheduled task (cost, complexity) when targeted exit-code + freshness checks on state-mutating jobs would suffice.

  Mitigations available: Make state-mutating scheduled jobs (a) fail non-zero on no-op, (b) emit an artifact marker (rows written / mtime), (c) have the status reader assert the marker's freshness before claiming "refreshed."

  STEELMAN:
    Strongest counterargument: The presumption is correct in spirit but the fix is narrower and cheaper than a readiness-probe analogy implies: bind each state-mutating job's success to a post-condition assertion (did the db advance?). Idempotent retries already cover transient failures; only silent no-op-exit-0 needs catching.
    What would need to be true for "fired ⇒ succeeded" to be tolerable: The job must be idempotent, retried, and fail LOUD (non-zero) on no-op, so a fired-but-failed run is self-healing and visible.
    How to test: Force the OpenStory writer to no-op and confirm it exits non-zero and the morning status refuses to say "refreshed"; if it still claims success, the binding is missing.

  Recommendation: PARTIALLY-CHALLENGED

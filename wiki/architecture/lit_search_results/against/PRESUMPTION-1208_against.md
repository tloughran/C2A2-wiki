SEARCH-AGAINST-PRESUMPTION-1208:
  Date searched: 2026-11-03
  Original item: PRESUMPTION-1208
  Original statement: Each copy of a duplicated task presumes its own outcome is the task's outcome. The local lit pipeline reported 'didn't run today' and 'anything queued is still waiting' without reading the lock log.
  Claim tested (literature lane): challenges to the claim that replica-local reporting is a defect: cases where local reporting is adequate or correct, where the shared record is itself unreliable, and where a global view costs more than it returns. The in-house limb is NOT 15a/15b scope and was not run.
  Search scope: PRELIMINARY. 3 web searches, 1 fetch. Google SRE book ch. 24 was fetched (summary only). Fencing/lock sources are title-only. Not reached: Kleppmann's essay text, Chandra-Toueg, Lamport on clocks, any LLM-agent scheduler source. Broader search recommended.
  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15b
    Original item: PRESUMPTION-1208
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: inferred from the local pipeline's 'did not run' report contradicted by the other copy's lock-log record
      15b: Searched for challenging literature (preliminary; 3 searches, 1 fetch)
    Current status: PARTIALLY-CHALLENGED
  Challenging evidence found: Partial
  Sources:
    1. Beyer, B., Jones, C., Petoff, J., Murphy, N.R. (eds.), 2016, Site Reliability Engineering, ch. 24 "Distributed Periodic Scheduling with Cron." https://sre.google/sre-book/distributed-periodic-scheduling/ [fetched; summary read, not full text] - in Google's cron only the leader replica launches jobs and modifies shared state; followers replicate a quorum-written launch record. Challenge to the framing: where a design names one acting copy, "the other copy did not run" is the intended state, and a follower's local report is correct for its role. The remedy is a shared, quorum-agreed record per launch (job plus scheduled time), not each copy checking the other ad hoc. The chapter also states a general preference for skipping a launch over risking a double launch, so "did not run" can be a deliberate outcome.
    2. hackernoon.com, "distributed locks are more dangerous than they look" https://hackernoon.com/distributed-locks-are-more-dangerous-than-they-look [title only; secondary] and system-design.space "distributed locks leases fencing" https://system-design.space/en/chapter/distributed-locks-leases-fencing/ [title only] - the lock-fencing literature (Kleppmann's essay is the usual primary; not retrieved) holds that a lock record alone does not prove who acted: a holder can pause or lose its lease and still act. Challenges the presumption's remedy (read the lock log) as sufficient authority.
    3. sVIRGO, arXiv 2602.02438 https://arxiv.org/pdf/2602.02438 and USPTO US6574744 "uniform global view of the system status of a distributed computer network" https://patents.google.com/patent/US6574744 [titles only] - surfaced on the coordination cost of maintaining a global status view. Relevance unverified; included as the only cost-side hits.
  Strength of challenge: Weak
  Summary: Nothing found says replica-local reporting is acceptable when a replica asserts a claim about the whole task. The challenge is narrower: where the design makes one copy authoritative, a local report is correct for its scope; the shared record must itself be authoritative (quorum or fencing) rather than a log that any copy can read; and skipping can be intended. The presumption survives as a scoping defect (an unqualified claim), not as a refuted premise.
  Specific risks: If the lock log is not authoritative, reading it before reporting replaces one unchecked claim with another; two copies could still disagree about who ran. If the remedy is applied to every report, cost and latency rise for little gain on low-stakes status lines.
  Mitigations available: Scope the report to the copy ("this copy did not run; lock log shows X"); key each launch by job plus scheduled time as in the SRE chapter; treat the lock log as evidence with a stated reader and timestamp, not as ground truth.

STEELMAN:
  Item: PRESUMPTION-1208
  Strongest counterargument: In a replicated scheduler the system's correctness depends on a single agreed record per launch, written by whichever copy acts, with quorum or fencing so that a stale holder cannot claim the run. Local reports from non-acting copies are noise by design, and a fix that merely tells each copy to read a lock log leaves the real hazard in place, because a log written by a copy that has since paused or lost its lease can mislead. A report that says "did not run" may also be the correct and preferred outcome, since skipping beats double launch.
  What would need to be true for C2A2 to be safe: the lock log is written atomically with a launch identifier (job plus scheduled time) and a holder identity; a copy that reports "did not run" cites the record it read and its time; only one copy is meant to act on a given item.
  How to test: for 10-26..11-02, list each day's lock-log lines against each copy's own report; count days where a copy's claim was contradicted by a log entry written by the other copy, and days where the log itself was ambiguous (two LOCKED lines with no RELEASED).

SYSTEMIC-RISK check: Not flagged. A loose resemblance to PRESUMPTION-1207 (conclusions asserted without consulting an available record) exists, but the evidence for a shared literature-backed vulnerability is title-only on both items.

  Recommendation: PARTIALLY-CHALLENGED

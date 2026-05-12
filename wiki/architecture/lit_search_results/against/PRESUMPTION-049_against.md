SEARCH-AGAINST-PRESUMPTION-049:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-049
  Original statement: "Wiki daily run and Levin+Friston specialist run are scope-partitioned without coordination contract"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-049
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as observed parallel-pipeline state without cross-task coordination
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Distributed-systems coordination literature (Lamport 1978 clocks; Gray & Reuter 1992 transactions; Kleppmann 2017): parallel tasks that *write* to a shared data store require an explicit coordination contract or a write-exclusion mechanism — "scope-partition by convention" is known to drift silently and produce race conditions.
    2. Observed empirical drift — duplicate Levin production in the review queue: this is direct evidence that the partition has already failed. Literature explicitly names "by-convention partitions" as the origin of this class of failure.
    3. CAP-theorem and consistency-model literature (Brewer 2000; Vogels 2009): idempotency-by-convention requires that the outputs are actually idempotent; the duplicate-Levin artifact suggests that the write path is not idempotent at the object level.
    4. Production-system failure reports (Google SRE book ch. 14; Jepsen analyses of distributed-db race conditions): the "everything was fine until a schedule overlap" failure mode is common and specifically cited as a reason to adopt explicit coordination contracts.
    5. Paired PRESUMPTION-054 (specialist convergence without turn-cap): without a cost-cap on the specialist, the specialist's runtime can overlap with the next daily-wiki run, which the partition-by-schedule explicitly does not account for. The two presumptions compound.

  Strength of challenge: Moderate

  Summary: The presumption is challenged on both *pattern* and *instance* grounds. At the pattern level, scope-partition-by-convention is a named failure mode in distributed-systems literature — the canonical remediation is either an explicit write-exclusion mechanism or an idempotent merge protocol. At the instance level, the duplicate-Levin artifact is direct empirical evidence the partition has already failed. The presumption's "without coordination contract" clause converts from "permissible" to "implicated" once the drift is observable.

  Specific risks: (a) Duplicate-production noise in the review queue (observed); (b) silent Friston coverage gap if specialist scope fails to match daily-wiki scope; (c) schedule overlap if specialist convergence is unbounded (compounds with PRESUMPTION-054); (d) invisible-to-the-pipeline state: neither task knows the other ran.

  Mitigations available:
    - Add an explicit coordination-contract document: who is responsible for which thinker-slots, at what cadence, with what handoff.
    - Write-exclusion via per-thinker lock-file or per-day lease; idempotent merge for dedup.
    - Cross-task state ping: each task emits a "ran at T with scope X" marker that the other reads before starting.
    - Enforce per-thinker uniqueness in the review queue.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-049
    Strongest counterargument: "Without coordination contract" is a named failure mode, not a design choice. The duplicate-Levin-in-review-queue signal is the exact empirical evidence the distributed-systems literature predicts for by-convention partitions under schedule overlap. The system has the evidence that the partition failed; the presumption now retrospectively labels the failure as an unstated design choice. Absent an explicit contract, the partition can be expected to drift further as specialist cadence increases or thinker-slots grow.
    What would need to be true for C2A2 to be safe: Explicit coordination contract (written down, not emergent), idempotent merge at the review-queue layer, and a detection mechanism for partition drift.
    How to test: Audit the review queue for duplicate items over the next 4 weeks; measure the per-thinker duplicate rate; observe whether daily-wiki runs complete before specialist runs start.

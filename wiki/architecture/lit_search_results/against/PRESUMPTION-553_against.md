SEARCH-AGAINST-PRESUMPTION-553:
  Date searched: 2026-07-27
  Original item: PRESUMPTION-553
  Original statement: [inferred] The 15d re-trigger machinery presumes re-triggering keeps items live for a downstream consumer, but consumption has been zero for 18 days and the ~174-item backlog grew; re-triggering feeds a queue with drain rate zero.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-553
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from a re-trigger loop feeding a queue with zero consumption for 18 days
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Log/stream vs work-queue distinction (event-sourcing and append-only log literature, e.g., Kleppmann, Designing Data-Intensive Applications, ch. on logs). — An append-only log is DESIGNED to grow unboundedly and is not pathological; "consumption rate zero" is only a failure if the blocks are work-in-progress rather than a durable record. If the RE-TRIGGER blocks function partly as an audit trail, the queueing-instability framing miscategorizes them.
    2. Deliberate deferral / priority scheduling (real-time scheduling; the monitor cohort's explicit monthly/low-priority downgrade). — Many backlog items are LOW-PRIORITY monitors intentionally deferred to a monthly cadence; a growing count of intentionally-deferred items is a policy choice, not starvation of due work. The 15d records show due-date bookkeeping is being maintained.
    3. Re-triggering does produce effects (the escalation machinery). — Re-triggers are not inert: MONITOR-420's auto-escalate trigger FIRED and starvation/priority-staleness triggers are keyed off the standing blocks. So re-triggering demonstrably "keeps items live" in the specific sense of driving escalation, even with zero evidence-pass consumption.

  Strength of challenge: Moderate

  Summary: The queueing-theory verdict is sound for work-in-progress but is conditioned by what the re-trigger blocks ARE. If they double as a durable audit log or are intentionally-deferred low-priority monitors, unbounded growth is not per se harmful; and re-triggering is not fully inert since it drives the escalation triggers. The challenge does not deny the backlog is a problem — it denies that "re-trigger = broken because drain is zero" is the whole story; the harm is specifically the read/context cost and the aging of genuinely-due items, not accumulation as such.

  Specific risks: If the presumption is over-read as "stop re-triggering," the system loses its escalation and due-date bookkeeping while the real fix (a consumer / bound) is still absent - worse than the status quo.

  Mitigations available: Split an operational working-set from an archived log (bounded queue + durable record); impose a WIP limit AND assign/point a consumer at the oldest cohort (the standing BACKLOG-FLAG remedy) rather than disabling re-triggering.

  STEELMAN:
    Item: PRESUMPTION-553
    Strongest counterargument: Zero evidence-pass consumption is real, but the re-trigger loop still performs escalation and due-date accounting, and an append-only record is entitled to grow. The problem is the ABSENT CONSUMER downstream, not the re-trigger producer; fixing the producer (stop re-queuing) would remove a working safety function while leaving the actual gap.
    What would need to be true for C2A2 to be safe: an operational/archive split with a bounded working-set, and a consumer pointed at the oldest cohort (or an explicit re-scoping of the 15d cadence to observed throughput).
    How to test: in-house - measure arrival vs consumption over 2026-07-08..07-26 from monitor_queue.md (already effectively done: 110 -> 147 -> ~174, consumption 0), and measure the per-run read/context cost the backlog imposes.

  Recommendation: PARTIALLY-CHALLENGED

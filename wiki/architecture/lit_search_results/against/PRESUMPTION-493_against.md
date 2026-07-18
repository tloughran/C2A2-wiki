SEARCH-AGAINST-PRESUMPTION-493:
  Date searched: 2026-07-18
  Original item: PRESUMPTION-493
  Original statement: [inferred] The fail-loud discipline presumes an attending listener within bounded time; on day 12 of no attended session, loud surfacings accumulate unactioned (17-day review gap, 27 proposals, staged-not-pushed writes) — "surfaced loudly" ≡ "unaddressed." Generalizes P-487 beyond No-Blind-Push.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-493
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from day-12 accumulation of unactioned loud surfacings
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Temporal, "Reliable data processing: Queues and Workflows"; RabbitMQ "Reliability Guide." — Durable/persistent queues write items to disk and survive crashes/restarts; a durably-surfaced item is DEFERRED, not lost. This challenges "surfaced loudly ≡ unaddressed": if surfacings persist idempotently, a returning listener processes them without loss.
    2. AWS Well-Architected REL04-BP04 (idempotency); DEV "Idempotency ... Beyond Retry Safely." — When accumulated work is idempotent and durable, batch catch-up on the listener's return is safe; accumulation ≠ failure unless the underlying state is being lost.
    3. incident.io, "Escalation policy best practices." — Escalation presupposes an available target; where the sole listener is unavailable there may be "nowhere to escalate," so escalation is not a universal remedy — bounding the CLAIM that escalation always fixes this.

  Strength of challenge: Weak-Moderate

  Summary: The presumption conflates two cases that should be separated. Where surfacings are DURABLE and their referents idempotent (e.g., proposals, review notes), accumulation is deferral, not loss — a returning listener can drain them, so "unaddressed" overstates the harm. The genuinely damaging case is narrow: where deferral causes irreversible loss (the staged-not-pushed WRITES, which risk never persisting — the durability path, already flagged REVISE-220/222). So the real risk is not "fail-loud is useless without a listener" in general, but specifically "fail-loud over a NON-DURABLE referent equals silent failure." The queue-without-consumer concern is valid; the blanket equation is too strong.

  Specific risks: Treating all accumulated surfacings as equally lost could trigger drastic auto-action (autonomous pushes) where safe deferral suffices, reintroducing the very No-Blind-Push risk P-487 guards.

  Mitigations available: Classify surfacings by referent durability; only items whose referent decays (unpushed writes, frozen dbs, expiring tokens) need time-bounded auto-escalation/fallback; durable-referent items can safely wait for the listener.

  STEELMAN:
    Strongest counterargument: "Surfaced ≡ unaddressed" is only true where the surfacing's referent is perishable. A durable, idempotent backlog is a feature (nothing is lost); the failure is confined to perishable referents. The design fix is not "assume no listener" but "make surfacings durable and escalate only the perishable ones."
    What would need to be true for the presumption to be low-risk: Every surfacing must be durably stored, and only decay-prone referents wired to a time-bounded fallback (alternate channel or bounded autonomous action).
    How to test: Inventory current surfacings; mark which have perishable referents; confirm those (and only those) have an escalation/fallback path. If perishable items lack one, the risk is real but bounded to that subset.

  Recommendation: PARTIALLY-CHALLENGED

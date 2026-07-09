SEARCH-FOR-PRESUMPTION-451:
  Date searched: 2026-07-07
  Original item: PRESUMPTION-451
  Original statement: "[inferred] Scheduler task-lifecycle defects (a ONE-TIME task firing 3x) are for agents to absorb, not for the scheduling layer to enforce."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-451
    Item type: PRESUMPTION (unstated — surfaced by inference); Priority MEDIUM
    Transform at each step:
      14b: Inferred from the 2026-07-06 autonomous-Monday EOD sources (sync-agent transcripts / bootstrap verification report showing a nominally one-time task firing three times with no scheduler-side guard)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Richardson (microservices.io), "Pattern: Idempotent Consumer." — Canonical statement that "it's usually a good idea to use a message broker that guarantees at-least-once delivery," with the accepted consequence that "the consumer can be invoked repeatedly for the same message"; the recommended remedy is a consumer-side idempotency key, i.e., the CONSUMER (agent) absorbs the duplicate. Directly supports placing dedup responsibility at the consumer.
    2. Jovanović, "Idempotent Consumer — Handling Duplicate Messages." — Argues it is "much simpler and more common to settle for at-least-once semantics and just de-duplicate on the consumer side" rather than pursue true exactly-once delivery at the delivery layer, supporting the design choice to have agents handle redelivery.
    3. Kafka at-least-once guidance (OneUptime, "How to Implement Kafka Consumers with At-Least-Once Semantics," 2026). — Standard industry position that exactly-once at the delivery/scheduling layer is expensive and often impractical; idempotent consumers are the pragmatic norm.
    4. "The Cron Job That Silently Drains $100K Monthly" (Medium, Sohail). — Documents that scheduled-task lifecycle defects (zombie/duplicate/overlapping runs) are a widespread, silently-compounding reality, supporting the descriptive premise that such defects routinely reach and must be handled downstream of the scheduler.

  Strength of support: Moderate

  Summary: Distributed-systems literature strongly supports one half of the presumption: at-least-once delivery is the pragmatic default, exactly-once at the delivery layer is costly/often infeasible, and the dominant, textbook remedy is to make the CONSUMER idempotent — i.e., the agent absorbs duplicates. In that sense, "duplicates are for consumers to handle" is a mainstream, well-grounded engineering stance. The cron-rot literature further confirms that lifecycle defects (a one-time task firing multiple times) do occur and do surface downstream. The support is only partial, however, because the same literature frames consumer-side idempotency as a DELIBERATE, engineered contract (idempotency keys, dedup tables), not as a license for the scheduling layer to ship uncorrected lifecycle bugs — the claim conflates "consumers should be idempotent" with "the scheduler need not fix a ONE-TIME violation."

  Caveats: A ONE-TIME task firing 3x is arguably not at-least-once redelivery of the SAME logical message but a scheduler lifecycle DEFECT (wrong number of distinct fires); idempotent-consumer theory addresses redelivery of identical messages and may not fully license ignoring a correctness bug in fire-count semantics. Best practice pairs consumer idempotency WITH scheduler-side guarantees (dedup windows, single-execution locks), so "absorb, not enforce" is only half the recommended defense-in-depth. Sources are messaging/streaming systems; transfer to a Claude-agent scheduler is analogical.

  Recommendation: PARTIALLY-SUPPORTED

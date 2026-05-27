SEARCH-AGAINST-ASSUMPTION-225:
  Date searched: 2026-05-27
  Original item: ASSUMPTION-225
  Original statement: A 34-file / ~90-PRS-triplet / 12-tradition ingestion is too large and error-prone to execute unattended at the tail of the daily cycle; it belongs in a focused, ideally attended session.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-225
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on attended-vs-unattended bulk ops.
    Current status: PARTIALLY-CHALLENGED (Weak-Moderate)

  Sources:
    1. Continuous-deployment literature (Humble & Farley 2010) — fully automated, unattended deployment of LARGE changes is routine in mature pipelines IF idempotency, rollback, and observability are engineered. Manual attention is not the only protective layer.
    2. Bain & Company / DORA reports (Forsgren et al. 2018 "Accelerate") — high-performing teams ship larger, more frequent automated changes; attended-only design is associated with LOWER reliability.
    3. Parasuraman & Manzey (2010) "Complacency and bias in human use of automation" — attended supervision of unfamiliar large batches is itself error-prone; human attention is not the silver bullet the assumption implies.
    4. Counter-evidence: the 2026-05-26 attended session WAS attended but PRS-extraction was DEFERRED to a further attended session — attended-only design doesn't automatically deliver throughput.

  Strength of challenge: Weak-Moderate

  Summary: The literature does not support "attended is always safer." Mature automated pipelines run large batches reliably IF preconditions (idempotency, rollback, observability) are engineered. The challenge is that the assumption skips over WHICH preconditions the C2A2 pipeline lacks; the right remedy may be engineering the preconditions, not requiring attention.

  Specific risks: (a) Defer-to-attended becomes deferral-as-bottleneck-relabel (PRESUMPTION-248); (b) attended supervision of unfamiliar 12-domain batches is itself error-prone (complacency / vigilance decrement); (c) the assumption may foreclose investment in pipeline engineering.

  Mitigations available: (a) Engineer idempotency + rollback + observability so unattended is safer; (b) make the attended session genuinely attended (active checking, not passive presence); (c) compromise: attended-canary + unattended-rest with explicit gates.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate)

  STEELMAN:
    Item: ASSUMPTION-225
    Strongest counterargument: The assumption frames attended supervision as the safety layer, but the safety actually comes from idempotency + rollback + observability — engineering work that has not been done. Requiring attention substitutes a scarce, unreliable resource (human attention) for a reliable, scalable one (engineering). If the gate stays dark, the supposed safety is fictional.
    What would need to be true for C2A2 to be safe: Either engineer the preconditions (then unattended is fine), OR guarantee attended availability via SLA + cadence.
    How to test: Run the 12-tradition ingest with a documented rollback plan + spot-check + automated post-condition validation. Measure error rate against attended baseline. If error rates are comparable or lower, attended-only is over-conservative.

SEARCH-AGAINST-ASSUMPTION-335:
  Date searched: 2026-06-23
  Original item: ASSUMPTION-335
  Original statement: "The post-Apr-6 "token cliff" was a 2026-04-07 schema-migration read-path artifact (data.token_usage -> data.agent_payload.token_usage zeroing reads), not an output collapse; both-paths read recovers continuous, growing output"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-335
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a GROUNDED claim (verified via C2A2 live-db probe); queued for failure-class / operational context, not to establish the fact
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: No (the fact is grounded; only a weak boundary note)

  Sources:
    1. (No literature challenges the grounded fact.) Weak boundary note: migration-testing literature cautions that a single recovered read path does not by itself prove NO other field was affected — relevant to 373/336, not to the artifact reading of the cliff itself.

  Strength of challenge: Weak

  Summary: No challenge to the grounded claim: the both-paths probe directly demonstrates the artifact, and the literature corroborates the failure class rather than disputing it. The only adjacent caution is that confirming one read path is not a whole-pipeline clean bill — but that targets the durability (373) and over-trust (336) presumptions, not the artifact interpretation of the cliff. As an explanation of the post-Apr-6 cliff, the claim stands unchallenged.

  Specific risks: Minimal for the fact itself; the residual risk lives in the generalizations 336 (trust all downstream) and 373 (fix is durable).

  Mitigations available: Keep the artifact finding scoped to the token-read path; route durability/whole-pipeline trust to 373/336 with canary assertions.

  STEELMAN:
    Strongest counterargument: Even a grounded probe is a point-in-time read; one could argue the "cliff" had multiple causes and the read-path artifact merely masked a real (smaller) output change.
    What would need to be true for C2A2 to be safe: A both-paths reconciliation across the full window (not a single timestamp) must show continuous growth — which the probe reports — for the pure-artifact reading to hold.
    How to test: Reconcile derived output metrics across both schemas for the entire post-Apr-6 window; identical continuous series => pure artifact.

  Search scope: boundary/whole-pipeline caution only; fact unchallenged. Comprehensive.

  Recommendation: NO-CHALLENGE-FOUND

SEARCH-FOR-ASSUMPTION-335:
  Date searched: 2026-06-23
  Original item: ASSUMPTION-335
  Original statement: "The post-Apr-6 "token cliff" was a 2026-04-07 schema-migration read-path artifact (data.token_usage -> data.agent_payload.token_usage zeroing reads), not an output collapse; both-paths read recovers continuous, growing output"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-335
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a GROUNDED claim (verified via C2A2 live-db probe); queued for failure-class / operational context, not to establish the fact
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Branch Boston, "Schema Evolution Strategies: Handling Data Structure Changes Without Breaking Pipelines." — Documents the exact failure: a moved/renamed field silently zeros downstream reads while the underlying data is intact.
    2. Functionize / Airbyte data-migration-testing guides. — Silent data corruption from type/path mismatches after migration is a recognized class; data "appears valid but reads incorrect values."
    3. C2A2-internal live-db probe (06-22). — both-paths read (data.token_usage OR data.agent_payload.token_usage) recovers a continuous, growing series, empirically confirming the artifact reading.

  Strength of support: Moderate-Strong

  Summary: The claim is both empirically grounded (the live-db probe recovers continuous output under a both-paths read) and squarely matches a documented failure class: a schema migration that relocates a field silently zeroes reads while data remain intact. The supporting literature confirms this is a common, well-characterized "silent read-path" artifact, not an exotic interpretation. Support is strong for the artifact reading over the output-collapse reading.

  Caveats: Literature value here is operational (recurrence-guard design), since the fact itself is already grounded. Support for the FACT does not extend to PRESUMPTION-373's separate claim that the both-paths fix is durable/complete.

  Search scope: schema-evolution silent-zeroing; data-migration silent corruption. Comprehensive; fact already grounded.

  Recommendation: SUPPORTED

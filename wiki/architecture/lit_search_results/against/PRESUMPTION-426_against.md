SEARCH-AGAINST-PRESUMPTION-426:
  Date searched: 2026-07-01
  Original item: PRESUMPTION-426
  Original statement: "[inferred] That an exact count-match (+144) proves content correctness — presumes no compensating (drop-plus-wrong-add) errors."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-426
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption from the +144 count-match verification
      15b: Searched for challenging literature (genuine web search 2026-07-01)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Integrate.io / SDET-QA ETL validation — a matching row count is passed even when content diverges; count validation is explicitly a necessary-not-sufficient check and is blind to offsetting errors (a dropped record plus a wrongly-added record net to the same count).
    2. Microsoft SQL replication validation — checksum/count can report success despite structural/logical differences; aggregate equality does not entail element-wise correctness.
    3. Accounting/verification analogue — "compensating errors" is a named failure class precisely because equal totals routinely hide two errors that cancel.

  Strength of challenge: Strong

  Summary: An exact +144 is fully consistent with, e.g., 2 correct-adds dropped and 2 wrong-adds inserted — the count is identical, the content is wrong. Compensating/offsetting errors are a named, well-documented failure mode that aggregate counts cannot detect. The presumption's implicit "count proves content" is directly false.

  Specific risks: Wrong or misattributed cards enter the connectome undetected because the headline number matched; the error is invisible precisely because it balanced.

  Mitigations available: Verify identity, not just cardinality — check that the specific expected proposal_ids are present (set difference, not count difference), plus a content spot-check. This is the same fix as A-394.

  STEELMAN:
    Item: PRESUMPTION-426
    Strongest counterargument: If the ingest is append-only with a monotonic, gap-checked id sequence, an exact +144 combined with an id-range check is much stronger than a bare count and approaches proof for the "no silent drop" property — so count-match is not worthless, it is just incomplete without the id check.
    What would need to be true for C2A2 to be safe: Verification keys on the SET of expected proposal_ids (per A-396), not on the count.
    How to test: Compute expected_ids minus present_ids and present_ids minus expected_ids; both empty is the real check.

  SYSTEMIC-RISK: member of the "structural-proxy / measurement-validity" cluster (with A-394, P-430) — see AGAINST-431 systemic note.

  Recommendation: CHALLENGED (Strong — count-match cannot detect compensating errors; identity-level check required)

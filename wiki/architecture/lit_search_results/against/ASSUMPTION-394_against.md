SEARCH-AGAINST-ASSUMPTION-394:
  Date searched: 2026-07-01
  Original item: ASSUMPTION-394
  Original statement: "A clean connectome regen (288->432, +144, node --check + count-match + content-population green) is sufficient verification of ingestion correctness."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-394
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-30 verification step
      15b: Searched for challenging literature (genuine web search 2026-07-01)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Microsoft SQL replication validation docs — row-count/checksum validation has documented blind spots (column filters, offset/logical-structure differences) and can pass despite real divergence; structural equality is not content equality.
    2. Integrate.io "Data Validation in ETL" — structural checks must be paired with SEMANTIC validation (business-rule, referential-integrity, range checks); count+parse+populate does not verify that the RIGHT content populated the RIGHT records.
    3. Gartner/ShiftAsia defect-escape — a "green build" masks defects when the check suite is not aligned to the fault classes that matter; structural green != correct.

  Strength of challenge: Strong

  Summary: The word "sufficient" is directly contradicted by the ETL/validation literature. Count-match + parse-validity + non-null population are necessary first-line checks but are known to be insufficient: they cannot detect semantic errors (wrong content in a well-formed record) or compensating errors (a drop cancelling a wrong add, which yields an exact count-match — PRESUMPTION-426). This is a classic false-green.

  Specific risks: Ingested claim cards that are structurally valid but semantically wrong (misattributed tradition, wrong PRS linkage, duplicated-but-renamed content) pass every gate and enter the connectome and downstream premise register uncorrected.

  Mitigations available: Add a content-level check — sampled semantic spot-check, referential-integrity check (proposal_id linkage), and a duplicate/near-duplicate scan — on top of the structural gate.

  STEELMAN:
    Item: ASSUMPTION-394
    Strongest counterargument: If ingestion is a pure structural transform (copy card -> node) with no semantic transformation, then structural checks plus the upstream attended review (A-393) may jointly approach sufficiency — the human already vetted content, so the regen only needs to confirm nothing was dropped/mangled.
    What would need to be true for C2A2 to be safe: The attended pass must actually have vetted every card's content AND the regen must be a lossless structural copy — then "structural green" inherits the human's content verification.
    How to test: On a sample, compare rendered connectome nodes against source cards for content fidelity, not just presence.

  Recommendation: CHALLENGED (Strong — structural green is necessary but not sufficient; "sufficient" is a false-green claim)

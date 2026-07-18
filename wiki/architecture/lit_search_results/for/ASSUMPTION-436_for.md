SEARCH-FOR-ASSUMPTION-436:
  Date searched: 2026-07-10
  Original item: ASSUMPTION-436
  Original statement: "proposal_id frontmatter presence is the correct validity criterion for pending proposals (17 filenames → 16 valid)."
  QUEUED-EMPIRICAL: literature clause only searched; in-house empirical test out of scope for 15a.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-436
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-09 EOD cohort
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. item.com Ontology, current. "Schema Validation: Enforce Data Structure Integrity & Consistency." — Describes required-field detection as a standard validity gate: scanning every record to confirm mandatory attributes are present and flagging records that lack them, before they enter downstream processing. Directly parallels treating proposal_id presence as the validity criterion at read time.
    2. Dagster, 2024–2025. "How to Enforce Data Quality at Every Stage of Your Data Pipeline." dagster.io. — Ingestion-stage validation guidance: completeness checks on mandatory fields determine whether a record is admitted as valid; records failing required-field checks are quarantined rather than counted, matching the 17-filenames-to-16-valid filtering move.
    3. OneUptime, 2026. "How to Build Data Validation." oneuptime.com. — Recent engineering guidance that ingestion validation should catch malformed records before they enter the system, with required/mandatory-field presence listed among the first-line validity criteria in schema-on-read pipelines.
    4. Medium (Dagogo), 2023. "Data Integrity in a Data Pipeline: Best Practices (DIM)." — Missing-data checks that "identify missing or null values in mandatory fields and flag incomplete records" are canonical; presence of the identifying key field is the archetypal mandatory field because downstream joins/dedup depend on it.

  Strength of support: Moderate

  Summary: The data-engineering literature squarely supports required-field presence as a legitimate, standard validity criterion in schema-on-read pipelines: records missing a mandatory field — especially a unique identifier — are conventionally classified as invalid or quarantined at ingest, and counts of "valid records" conventionally exclude them. The specific move made here (17 files by filename, 16 valid by presence of the proposal_id key) is an instance of exactly this pattern, and using the identifier field as the gate is especially well supported because identifiers underpin deduplication, referencing, and lifecycle tracking of proposals. Syntactic presence checks are the accepted first tier of validity, ahead of semantic checks.

  Caveats: The literature supports presence-of-required-field as *a* correct and standard criterion, not as the *complete* one: best practice layers semantic validation (is the proposal_id well-formed, unique, and does it reference a real proposal?) on top of presence, and recommends quarantining and triaging failed records rather than silently discounting them — a file missing proposal_id may be a recoverable authoring error rather than a non-proposal. Whether presence alone correctly classifies this specific 17th file is the queued empirical question, which literature cannot settle.

  Search scope confidence: comprehensive for ingest-validation practice; no literature found on frontmatter validation in agent-maintained markdown stores specifically

  Recommendation: PARTIALLY-SUPPORTED

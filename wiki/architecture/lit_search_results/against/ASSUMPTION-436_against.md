SEARCH-AGAINST-ASSUMPTION-436:
  Date searched: 2026-07-10
  Original item: ASSUMPTION-436
  Original statement: "proposal_id frontmatter presence is the correct validity criterion for pending proposals (17 filenames → 16 valid)."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-436
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-09 EOD cohort
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. [OneUptime, 2026. "How to Build Data Validation" (data pipeline validation guide). — Core best practice: records failing schema validation must not be silently dropped; they should be routed to a dead-letter queue for investigation, because a validation failure is a signal about the producer, not proof the record is worthless.]
    2. [DEV Community (137foundry). "The Real Cost of Silent Data Pipeline Failures." — Field-level checks that quietly exclude records are a canonical silent-failure mode; the excluded record often turns out to be a real, wanted record whose producer had a formatting bug.]
    3. [DEV Community (ramavala). "The Hidden Enemy of Data Pipelines: BigQuery Schema Evolution Failures." — Documents how single-field/schema mismatches (renamed field, missing key, ignoreUnknownValues=true) cause meaningful data to be silently lost while the pipeline reports success; presence-of-one-field is a brittle proxy that breaks under schema drift.]
    4. [Anomaly Armor blog. "Data Pipeline Monitoring: How to Stop Silent Failures Before They Hit Production." — Recommends completeness monitoring (expected vs received record counts) precisely because filter-style validity checks convert producer bugs into invisible data loss; a 17→16 filter without investigating the 1 is the pattern warned against.]
    5. [Unstructured.io. "Common Data Ingestion Challenges and How to Handle Them." — Malformed-but-meaningful records are common in document ingestion; the recommended handling is quarantine-and-repair, not exclusion, since malformation usually indicates a fixable producer defect.]

  Strength of challenge: Moderate

  Summary: The data-quality literature does not object to using a required field as a schema check; it objects to using it as a terminal validity verdict. Single-field presence is a weak proxy for validity in both directions: a file can carry a proposal_id yet be semantically broken (duplicate ID, wrong type, empty body), and a file lacking proposal_id can be a fully meaningful proposal whose author-agent had a frontmatter bug — the most likely cause of exactly one outlier among 17. Best practice is to treat validation failures as dead-letter items to be inspected and repaired, with the count discrepancy (17 vs 16) surfaced as a producer-defect signal. Silently reclassifying the 17th file as invalid risks losing a real proposal and masking a bug in whatever agent wrote it.

  Specific risks: A legitimate proposal is silently dropped from the pending queue (work lost, author-agent's intent discarded), and the upstream bug that produced a frontmatter-less proposal file goes undiagnosed and recurs; over time the "valid = has proposal_id" rule trains the system to discard evidence of its own defects.

  Mitigations available: Quarantine rather than discard — move the non-conforming file to a dead-letter location and log it for review; inspect the 17th file's content to determine whether it is a real proposal (and if so, repair the frontmatter and file a bug against the producing agent); validate more than one field (ID present, ID unique, ID format, non-empty body); emit an alert whenever filename-count and valid-count diverge.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: "Has proposal_id" tests conformance to a serialization convention, not validity of the proposal. In ingest-pipeline practice the single malformed record among many well-formed ones is the classic signature of a producer bug, and the professionally mandated response is quarantine, inspection, and repair — not reclassification as invalid. A criterion that lets the system silently shed inconvenient records will, under schema drift, shed arbitrarily many of them while reporting success.
    What would need to be true for C2A2 to be safe: The 17th file must actually be non-proposal content (e.g., a template, README, or aborted write) rather than a malformed proposal; and the frontmatter convention must be enforced at write time by all producing agents, so absence of proposal_id genuinely entails non-proposal.
    How to test: Open the 17th file and read it — if it contains proposal-like content, the criterion misfired; also audit producing agents' write paths to confirm frontmatter is always emitted. This is the queued in-house empirical test.

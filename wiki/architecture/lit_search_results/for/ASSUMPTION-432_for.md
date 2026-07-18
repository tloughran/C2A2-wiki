SEARCH-FOR-ASSUMPTION-432:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-432
  Original statement: "Date-stripped slug diff vs PROCESSED_LOG is a faithful detector of unprocessed inbox items (no slug collisions; log complete)."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-432
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extraction from cohort listing (2026-07-07 EOD)
      15a: Searched for supporting literature (item is QUEUED-EMPIRICAL; decisive test is a collision audit of actual slugs)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Airbyte, 2025. "Understanding Idempotency: A Key to Reliable and Scalable Data Pipelines." airbyte.com. — Establishes deterministic unique identifiers per record, checked against a processed set, as the cornerstone pattern for detecting already-processed vs. unprocessed items; the slug-vs-log diff is a direct instance.
    2. Streamkap, 2025. "Idempotency in Streaming Pipelines: Exactly-Once Without the Headaches." — Documents idempotency-at-the-sink via key comparison as the standard practical route to exactly-once-effective processing over at-least-once delivery; supports the architecture's soundness.
    3. SystemOverflow. "Idempotency, Deduplication, and Exactly Once Illusions in Distributed Pipelines." — Details key-design requirements (deterministic, collision-resistant keys; complete durable processed-log) and names the two failure modes the assumption itself flags: key collisions (false dedup → silently skipped items) and log incompleteness (false novelty → reprocessing).

  Strength of support: Moderate

  Summary: The set-difference of deterministic item keys against a durable processed log is the canonical, widely documented mechanism for detecting unprocessed items in ingest pipelines; the assumption's architecture is squarely within best practice, and the literature confirms the mechanism is faithful exactly under the two stated conditions (key uniqueness, log completeness). The specific key-design choice — stripping dates from slugs — is a lossy normalization, and the dedup literature explicitly identifies lossy key normalization as the primary false-positive mode: two distinct items differing only in date (e.g., recurring sessions with the same title) would collide and the newer one would be silently treated as processed. No source quantifies collision rates for this naming scheme; that is in-house.

  Caveats: Support weakens with (a) recurring same-titled items where the date was the distinguishing field (most likely real collision source); (b) any non-atomic append to PROCESSED_LOG (crash between process and log → missed-item is impossible but double-process possible; reversed order gives silent skip); (c) slug generation changes over time breaking determinism. Per QUEUED-EMPIRICAL, the decisive test is an audit for duplicate date-stripped slugs in the historical corpus.

  Search scope confidence: Comprehensive for idempotency/dedup design patterns; no quantitative false-positive-rate studies for slug-style keys found.

  Recommendation: PARTIALLY-SUPPORTED

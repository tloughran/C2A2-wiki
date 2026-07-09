SEARCH-AGAINST-ASSUMPTION-421:
  Date searched: 2026-07-07
  Original item: ASSUMPTION-421
  Original statement: "Re-running a completed baseline protocol duplicates artifacts; a structurally identical 3,000-line file two runs later is clutter, not measurement."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-421
    Item type: ASSUMPTION (stated), Priority LOW
    Transform at each step:
      14a: Extracted from the 2026-07-06 autonomous-Monday EOD sources (sewing bootstrap verification report comparing weekly census agent vs older bootstrap census protocol)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Simons, D. J., 2014. "The Value of Direct Replication." Perspectives on Psychological Science, 9(1), 76-80. — Argues that direct replication is "the only way to verify the reliability of an effect"; obtaining the same result with the same procedure is not redundant but is precisely how reliability is established. An identical outcome IS the measurement, contradicting the "clutter, not measurement" framing.
    2. Open Science Collaboration, 2015. "Estimating the Reproducibility of Psychological Science." Science, 349(6251). — The replication crisis demonstrated the cost of treating repeated runs of "completed" protocols as low-value; only ~36-47% of replications reproduced original findings, showing that "completed baseline" results cannot be assumed stable without re-measurement.
    3. Measurement System Analysis (MSA) literature; e.g., AIAG MSA Reference Manual, 4th ed., 2010 (summarized in "Stability of a Measurement System," Six Sigma DSI). — Stability of a measurement system can only be assessed by repeatedly measuring the same reference over time and plotting on control charts; the "identical" repeated measurement is the raw material of drift detection, not clutter. A run that returns the same 3,000 lines is a stability data point.
    4. Peels, R. & Bouter, L. (and related work, e.g., "Exact replication: Foundation of science or game of chance?" PLOS Biology / PMC6456162, 2019). — Notes there is no such thing as truly exact replication (dates, contexts, tool versions differ); a "structurally identical" file two runs later is actually a distinct observation under slightly different conditions, and its similarity is informative.
    5. Research data management / data integrity norms (e.g., GxP/ALCOA+ audit-trail guidance; RMIT Research Integrity RDM guide, 2024). — RDM norms favor retaining raw outputs with provenance so history can be reconstructed; deleting or suppressing repeated raw artifacts as "clutter" runs against retention and audit-trail standards.

  Strength of challenge: Moderate

  Summary: The replication and measurement-system literature challenges the core framing that an identical repeated result is "clutter, not measurement." In replication science, obtaining the same result under the same protocol is the definitive evidence of reliability, and the replication crisis showed how dangerous it is to assume a completed baseline remains valid. In industrial measurement-system analysis, repeatedly measuring a stable reference over time is the only way to detect instrument drift — the near-identical repeat run is exactly what a stability control chart consumes. Research-data-management norms further weigh toward retaining repeated raw artifacts with provenance. The challenge is only moderate, however, because the claim has a defensible practical core: an unintentionally re-fired protocol (vs a designed replication) producing a same-week duplicate does create curation burden, and the literature's remedy is to log the confirmation compactly, not necessarily to keep every 3,000-line artifact in place.

  Specific risks: If C2A2 treats identical re-runs as pure clutter and deletes/suppresses them, it loses (a) its only native drift-detection signal for the census instrument, (b) evidence of protocol stability across agent/tool versions, and (c) audit-trail provenance for later disputes about when the vault's connectivity actually changed. A silent divergence between "structurally identical" and "actually identical" could be discarded unexamined.

  Mitigations available: Diff the re-run against the original before discarding; record a compact "stability confirmation" note (checksum, date, delta=0) even if the full artifact is archived rather than kept inline; treat unintended re-runs as free replication data; adopt an RDM-style retention policy (archive, don't delete) with provenance metadata.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-421
    Strongest counterargument: In metrology and replication science, the statement "identical result = clutter" is backwards: an identical result from a repeated protocol is the highest-value confirmation available — it is the stability measurement itself. The replication crisis (OSC 2015) showed that fields which assumed completed baselines were settled paid dearly; Simons (2014) argues repetition with the same procedure is the only route to verified reliability. Moreover, no repetition is truly exact — the second run occurred under a different vault state, agent version, and date — so its structural identity is an empirical finding, not a duplication artifact. Discarding it destroys the drift-detection baseline and violates raw-data retention norms.
    What would need to be true for C2A2 to be safe: The re-run must be verifiably byte-comparable to the original (a recorded diff/checksum showing delta=0), the confirmation must be logged somewhere durable before the artifact is treated as clutter, and the census instrument must have some other stability check (e.g., the weekly agent itself) covering drift detection.
    How to test: Diff the two 3,000-line files programmatically; if truly identical, record the checksum-match as a stability data point and archive one copy. Periodically (e.g., quarterly) deliberately re-run the bootstrap protocol and compare — if it ever diverges from the weekly agent's picture, the "clutter" assumption was masking instrument drift.

  Search scope confidence: Moderate-high. Replication-value, MSA-stability, and RDM-retention literatures were all sampled; no literature was found that affirmatively endorses discarding repeated measurements as clutter, though practical data-curation guidance on deduplication exists and partially supports the claim's operational intent.

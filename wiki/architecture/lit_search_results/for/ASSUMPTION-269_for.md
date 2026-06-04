SEARCH-FOR-ASSUMPTION-269:
  Date searched: 2026-06-04
  Original item: ASSUMPTION-269
  Original statement: Intake discipline — an unverified cross-tradition lead must be flagged and held ("flag, do not yet ingest"), not captured, until a targeted confirmation search establishes it.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-269
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated intake rule "flag, do not yet ingest" for unverified cross-tradition leads.
      15a: Searched citation/lead verification before ingest, provenance discipline in automated KB construction, and write-time gating.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. CheckIfExist / CiteAudit (arXiv 2602.15871, 2602.23452, 2026). "Detecting Citation Hallucinations" / "Verifying Scientific References in the LLM Era." — LLM-era reference fabrication is a documented integrity risk: plausible-looking citations that correspond to no real publication. Verifying a lead against scholarly databases BEFORE trusting it is the recommended control — exactly "confirm before ingest."
    2. Zahn & Chana, 2026. "Selective Memory for Artificial Intelligence: Write-Time Gating with Hierarchical Archiving." arXiv 2603.15994. — Write-time gating that filters incoming knowledge objects by a composite salience/reliability score achieves ~100% accuracy vs ~13% for ungated stores under real LLM evaluation. Direct empirical support that filtering AT CAPTURE beats ingest-everything for KB integrity.
    3. Provenance/metadata-for-reproducibility practice (citation-verification pipelines; KB provenance tracking). — Tracking source identifiers, timestamps, and verification state so any item can be traced to a confirmed source is standard; "flag, do not yet ingest" is the operational front-end of that provenance discipline. Reinforces this register's existing verify-the-effect / provenance family.

  Strength of support: Strong

  Summary: The "flag, do not yet ingest" rule is strongly grounded. The LLM-era citation-hallucination literature establishes that unverified leads are a real corruption vector for automated knowledge bases, and write-time gating shows empirically that filtering at the point of capture dramatically outperforms ingest-everything. Provenance discipline reinforces holding an item in an explicit unverified state until a confirmation search promotes it. For a cross-tradition corpus where a fabricated lead could create a spurious bridge between thinkers, the discipline is the proportionate, well-supported standard.

  Caveats: The literature supports gating, not indefinite holding — the held-but-unverified queue must actually receive its confirmation search, or recall is lost silently (see 15b). Support is for "verify before trust," not for "hold and forget."

  Recommendation: SUPPORTED

SEARCH-FOR-PRESUMPTION-1141:
  Date searched: 2026-10-15
  Original item: PRESUMPTION-1141
  Original statement: "Outputs can be validated without recorded process (workflow) lineage. Literature question: what do data-provenance and workflow-lineage literatures (W3C PROV; scientific-workflow provenance) say about validating outputs without lineage?"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1141
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-14 transcripts.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Search scope: PRELIMINARY — broader search recommended. Titles/URLs only; no full text read; items marked UNVERIFIED come from background knowledge.

  Sources:
    1. Groth, Moreau et al., 2005. "Provenance-based validation of e-Science experiments." ISWC 2005 / J. Web Semantics. — Title and URL only seen. Lineage-based validation is the literature's default; it is the contrast case, not support. UNVERIFIED beyond title.
    2. Moreau & Missier (eds.), 2013. W3C PROV-DM. — UNVERIFIED (background). Provenance is optional descriptive record; PROV does not mandate lineage for validity.
    3. Davidson & Freire, 2008. "Provenance and scientific workflows: challenges and opportunities." SIGMOD. — UNVERIFIED. Lineage needed for reproducibility/error attribution; output checks can detect but not attribute errors.

  Strength of support: Weak

  Summary: No source found affirmatively claiming output-only validation suffices. Support is indirect: provenance is an enhancement, and artifact-intrinsic checks (schema, semantic, content, replication) are standard practice. Output-only validation is plausible when outputs are self-verifying (independent oracle, constraints, replication) and weak when correctness depends on how the output was derived.

  Caveats: Provenance literature is advocacy for lineage, so biased against the presumption. Preliminary search: 2 WebSearch calls, titles/URLs only, no full text; most claims from background knowledge.

  Recommendation: PARTIALLY-SUPPORTED

NOVELTY-FLAG: none (literature exists; no direct study of the specific use).

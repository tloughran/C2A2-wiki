SEARCH-FOR-ASSUMPTION-099:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-099
  Original statement: "DECISION-027 candidate scope can be extended to cover external-tool-review layer — specialist self-attribution + external-LLM prioritization adoption are presumed same epistemic-weight protocol"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-099
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD DECISION-027 candidate scope-extension question
      15a: Searched for review-aggregation framework taxonomies that distinguish source-types
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Higgins et al. (2019) "Cochrane Handbook for Systematic Reviews of Interventions" — review-aggregation frameworks distinguish source-types (primary research, secondary review, expert opinion) but apply a unified weighting protocol; scope unification across source-types is canonical when adjudication tier is articulated.
    2. GRADE Working Group (2008) "Rating quality of evidence and strength of recommendations" — single epistemic-weight protocol covers heterogeneous sources via documented tier classification; supports scope unification with explicit tier articulation.
    3. ADR (Architecture Decision Records) literature (Nygard 2011) — single ADR can govern multiple instances of the same decision class when class-coherence is documented; supports unification when source-types share class.
    4. Ross et al. (2010) "Distinguishing systematic and survey reviews" — separate adjudication tiers for distinct source-types is also canonical when the source-types differ in failure-mode rather than weighting.
    5. C2A2-internal: PRESUMPTION-074 (specialist self-attribution) and PRESUMPTION-115 (external-LLM prioritization) both fall in the "one source treated as primary signal without adjudication" pattern; substrate-coupling supports unified scope.

  Strength of support: Moderate (Partial)

  Summary: Scope unification across source-types is canonical when (a) source-types share the same failure-mode (here: "primary signal without adjudication"), (b) the unified protocol explicitly articulates tier classification, and (c) source-type-specific adjudication can be added as a sub-tier rather than a separate decision. The Cochrane / GRADE / ADR literatures all support this pattern. The PARTIAL classification reflects that source-type-specific failure modes (specialist confirmation bias vs. external-LLM training-data overlap) may warrant per-source-type adjudication sub-tiers within the unified scope.

  Caveats: (a) Unification is canonical only when failure-modes are sufficiently similar; if specialist self-attribution and external-LLM prioritization fail in different ways, separate ADRs are preferred; (b) PRESUMPTION-118 captures the asymmetric-reversibility risk — unifying-then-splitting is documented as more costly than starting split; (c) scope unification at decision-time foregrounds substrate; scope unification post-hoc risks rationalizing distinct decisions as "the same".

  Recommendation: PARTIALLY-SUPPORTED (substrate-coupling is real but failure-mode differentiation should be assessed before unifying; per PRESUMPTION-118, asymmetric-reversibility analysis is the canonical guard)

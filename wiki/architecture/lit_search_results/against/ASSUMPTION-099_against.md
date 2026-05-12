SEARCH-AGAINST-ASSUMPTION-099:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-099
  Original statement: "DECISION-027 candidate scope can be extended to cover external-tool-review layer — specialist self-attribution + external-LLM prioritization adoption are presumed same epistemic-weight protocol"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-099
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD DECISION-027 scope-extension question
      15b: Searched for counter-evidence on unified vs. per-source-type adjudication tiers
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Moderate

  Sources:
    1. LLM-evaluation literature (Ribeiro et al. 2020; Bowman & Dahl 2021) — failure modes for specialist self-attribution (confirmation bias in own-output evaluation) differ structurally from failure modes for external-LLM prioritization (training-data overlap, prompt-sensitivity); per-source-type adjudication is preferred.
    2. AMSTAR-2 (Shea et al. 2017) — review-aggregation frameworks distinguish source-types when failure modes differ; unifying scope across heterogeneous failure modes is documented anti-pattern.
    3. ADR literature (Nygard 2011) — retroactive ADR splitting is more expensive than starting split; PRESUMPTION-118 captures the asymmetric-reversibility risk.
    4. Brown et al. (1998) "AntiPatterns" — premature unification of distinct decision surfaces is documented anti-pattern; "scope-extension creep" risk.
    5. C2A2-internal: PRESUMPTION-074 (specialist self-attribution) and PRESUMPTION-115 (external-LLM prioritization) were REVISE'd separately because they surface in different operational contexts (within-system specialist vs. cross-system external review); failure-mode differentiation may justify per-source-type adjudication.

  Strength of challenge: Moderate

  Summary: Per-source-type adjudication is preferred when failure modes differ structurally. Specialist self-attribution and external-LLM prioritization fail in different ways (confirmation bias vs. training-data overlap), suggesting the unified-scope approach risks aggregating decisions that need distinct guards. PRESUMPTION-118's asymmetric-reversibility concern compounds the challenge — unifying-then-splitting is more costly than starting split.

  Specific risks: (a) Unified scope hides per-source-type failure-mode differences; (b) asymmetric-reversibility — split is the cheap initial state; (c) scope-extension creep — once DECISION-027 is unified, additional source-types (human reviewer, regulator, etc.) get pulled in without re-analysis.

  Mitigations available: (a) Document failure-mode differentiation explicitly; (b) start split (DECISION-027 + DECISION-028) and merge if substrate-coupling proves dominant; (c) bound scope explicitly with re-analysis trigger if extension is contemplated.

  Recommendation: PARTIALLY-CHALLENGED (substrate-coupling supports unification; failure-mode differentiation favors split; asymmetric-reversibility analysis is the canonical guard before commitment)

  STEELMAN:
    Item: ASSUMPTION-099
    Strongest counterargument: Specialist self-attribution and external-LLM prioritization fail in different ways. Specialist self-attribution fails by confirmation bias in own-output evaluation; external-LLM prioritization fails by training-data overlap and prompt-sensitivity. The two require distinct guards: specialist self-attribution needs independent adjudication tier; external-LLM prioritization needs cross-LLM divergence test. Unifying scope hides this differentiation. Asymmetric-reversibility analysis (PRESUMPTION-118) shows that split is the cheap initial state — start split and merge later if substrate-coupling proves dominant; starting unified and splitting later is more expensive due to downstream coupling that accumulates while the unified ADR is in force.
    What would need to be true for C2A2 to be safe: (a) Failure-mode differentiation explicitly documented; (b) asymmetric-reversibility analysis completed; (c) substrate-coupling at the implementation level (not meta-level) verified before unification.
    How to test: Specify the guards each ADR scope would need; check whether they overlap at the implementation level or only at the meta-level; if meta-level only, split is preferred.

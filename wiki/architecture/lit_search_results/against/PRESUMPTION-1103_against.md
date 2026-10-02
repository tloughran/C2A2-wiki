SEARCH-AGAINST-PRESUMPTION-1103:
  Date searched: 2026-10-02
  Original item: PRESUMPTION-1103
  Original statement: A natural-language work item handed between agents has one determinate test target, so different agents reading it will test the same claim.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1103
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-10-01 lit-pipeline conflict.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Beyond Accuracy: LLM Variability in Evidence Screening for Software Engineering SLRs", 2026. arXiv:2604.27006. https://arxiv.org/pdf/2604.27006 [fetched] — same criteria applied by different LLMs give different decisions; Gwet AC2 0.55–1.0 across 5 identical reruns at temperature 0; accuracy gaps of 22 and 47 pp across models.
    2. "Can We Hide Machines in the Crowd?" 2025. arXiv:2510.06658 [search-snippet] — LLM vs human annotator equivalence.
    3. "Repair or Resample? Failure Debugging in LLM Multi-Agent Systems", 2026. arXiv:2608.25920 [search-snippet] — loosely relevant.

  Strength of challenge: Moderate

  Summary: Different LLM readers, and the same one rerun, do not reliably reach the same decision on the same written criterion, so a determinate target cannot be assumed. Humans show the same inter-rater problem (classic construct validity). Support is by analogy from annotation and screening reliability; no paper on agent-to-agent work-item handoff was found.

  STEELMAN: Natural-language specs are underdetermined. Agents differ in model, context and sampling, so the claim tested diverges silently. Agreement as low as 0.55 on identical inputs shows divergence even without differing interpretation. Without a checkable operationalization (explicit claim, pass/fail predicate, echo-back of the interpreted claim), 'same claim tested' is unverified, and agreement on a pass/fail outcome can mask different targets.

  Caveats: Evidence is from screening/annotation, not handoff; a well-written item may be near-determinate and the 0.55 floor may come from weak models.

  Search scope: preliminary search — broader search recommended (no software-requirements-ambiguity literature searched); web-only; independent of 15a — 15a results were not read by the 15b searcher.

  Recommendation: PARTIALLY-CHALLENGED

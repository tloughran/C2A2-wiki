SEARCH-FOR-PRESUMPTION-1072:
  Date searched: 2026-09-23
  Original item: PRESUMPTION-1072
  Original statement: Parallel same-model agents with separate contexts show error correlation comparable
    to a single agent when prompt wording and tools are shared.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1072
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Inferred by checking the fix claim against the premise register.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Kim, E. et al., 2025. "Correlated Errors in Large Language Models." ICML 2025 (PMLR v267;
       arXiv 2506.07962). — Across >350 LLMs, models agree ~60% of the time when both err; shared
       provider and architecture raise correlation, and more accurate models are more correlated even
       across providers. If distinct models are this correlated, instances of the same model are
       expected to be more so.
    2. Ji, Y., 2026. "More Debate, Same Evidence: Structural Limits of Homogeneous Multi-Agent
       Groundedness Judges." arXiv 2608.00243 (preprint, single author; title/author confirmed by
       fetch). — Reports that homogeneous panels sharing a model and evidence pool can shift a decision
       boundary without acquiring independent evidence; frames homogeneous debate as structurally
       limited. Close fit; preprint, not peer-reviewed.
    3. "Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry,"
       arXiv 2607.01661 (preprint; authors not checked). — Reports that when agents share identical
       information, deliberation fails to improve collective accuracy and multi-agent methods with
       homogeneous input do not outperform a single CoT agent. Directly supports "comparable to a
       single agent."
    4. "The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent
       Debate," arXiv 2605.00914 (preprint; abstract not fetched — [unverified beyond search snippet]).
       — Title indicates homogeneous debate does not beat an isolated single agent.
    5. Supporting-by-contrast: search summaries of heterogeneous-debate work (e.g. "Understanding Agent
       Scaling in LLM-Based Multi-Agent Systems via Diversity," arXiv 2602.03794) report that
       homogeneous agents produce highly correlated outputs and that gains appear only when prompts
       or models are diversified.

  Strength of support: Moderate-to-Strong

  Summary: A peer-reviewed large-scale study (Kim et al., ICML 2025) establishes high error correlation
    even across different LLMs, with shared architecture/provider as a driver, which predicts even
    higher correlation among same-model instances. A cluster of 2026 preprints on homogeneous
    multi-agent debate converges on the same finding: with shared model, prompts and evidence, extra
    agents add little beyond a single agent, and diversity of prompts/models/evidence is what breaks
    the correlation. The presumption is consistent with the direction of current literature.

  Caveats: "Comparable to a single agent" is stronger than most findings, which show diminished but
    sometimes non-zero benefit (cf. Du et al. 2024; Wang et al. 2023 self-consistency gains — reported
    in ASSUMPTION-1624_for.md). Most supporting sources are recent arXiv preprints not yet peer
    reviewed. Tasks studied are QA/verification with fixed answers; open-ended web search with
    stochastic retrieval may add diversity these studies do not capture.

  Search scope: Preliminary — two searches (correlated LLM errors; homogeneous multi-agent debate),
    plus one fetch to confirm source 2.

  Excluded results: GitHub "AkihikoWatanabe/paper_notes #2145" (repo mirror). Source 2's phrasing
    ("share a model, evidence pool") is close to the claim's framing; retained after confirming it is a
    real arXiv posting with a named author, but weight it accordingly.

  Recommendation: SUPPORTED

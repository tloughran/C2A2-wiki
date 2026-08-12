SEARCH-FOR-ASSUMPTION-814:
  Date searched: 2026-08-10
  Original item: ASSUMPTION-814
  Original statement: Object-level, and about C2A2 itself: "the 2026 multi-agent-debate literature reports that homogeneous, unguided debate can underperform a single self-correcting agent — C2A2's exact configuration."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-814
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted a literature return that bears on C2A2's own architecture rather than on a tradition's content
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate" (arXiv:2605.00914, 2026). Title and abstract directly match the assumption's claim: compares isolated self-correction against peer debate and a stochastic-noise control across high-difficulty benchmarks and reports that isolated self-correction outperforms unguided, homogeneous multi-agent debate. This is effectively a direct hit on the assumption as stated. [unverified — from search snippet only; full text not read]
    2. "When and Why Does Multi-Agent Debate Fail and Does It Really Underperform?" (arXiv:2510.20963v2, 2025-2026). Documents multiple MAD failure modes (context limitations, inter-agent misalignment, majority-driven convergence, performance degradation across rounds) and finds MAD does not consistently outperform single-agent baselines — corroborates the underperformance claim from an independent research group.
    3. Multi-LLM-Agents Debate — Performance, Efficiency, and Scaling Challenges (ICLR 2025 Blogposts). Reports that current MAD methods "fail to consistently outperform simpler single-agent strategies, even with increased computational resources," and that MAD significantly underperforms simple self-consistency/majority voting at equivalent inference budget (e.g., self-consistency 88.2% vs. MAD 83.0% on GSM8K with 9 total responses).
    4. "Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate" (arXiv, 2509.05396v1, 2025). Identifies sycophantic conformity, contextual fragility, and consensus collapse as specific mechanisms by which homogeneous peer debate destroys correct answers — a mechanistic account of why homogeneity (same model, same weaknesses) is a moderating variable, consistent with the assumption's framing that C2A2 is homogeneous and unguided.
    5. "Adaptive Heterogeneous Multi-Agent Debate for Enhanced Educational and Factual Reasoning" (Journal of King Saud University CIS / Springer, 2025) and ARMOR-MAD (arXiv:2606.13197, 2026). Both report that introducing heterogeneity and adaptive routing recovers 4-6%+ accuracy gains over standard (homogeneous) MAD — supporting the assumption's implicit claim that heterogeneity/guidance are the moderating conditions absent in C2A2's "exact configuration."

  Strength of support: Strong

  Summary: This is one of the more directly confirmed items searched: multiple independent 2025-2026 papers, including one (arXiv:2605.00914) whose title nearly restates the assumption verbatim, converge on the finding that homogeneous, unguided multi-agent debate underperforms single-agent self-correction and simple self-consistency baselines at matched compute. A separate cluster of papers (heterogeneous/adaptive-routing MAD variants) supports the assumption's implied corollary that heterogeneity and guidance are the specific moderators that would change this outcome — meaning C2A2's homogeneous, unguided configuration sits squarely in the underperforming regime the literature describes.

  Caveats: Findings were surfaced from search snippets and titles/abstracts, not full-text verification — the arXiv:2605.00914 citation in particular should be checked against the actual paper before being treated as confirmed rather than "unverified — from search snippet." The 2026 papers are recent preprints without established replication track records; several use different benchmarks (GSM8K, factual QA, data-cleaning tasks) so cross-task generalization to C2A2's specific task domain is not established. One 2026 paper ("When Helping Hurts... Multi-Agent Debate for Data Cleaning," arXiv:2606.02866) found debate's effect can reverse sign by task type (helps error detection, hurts generation) — this is a caveat/moderator not fully captured by the blanket "underperforms" framing in ASSUMPTION-814's own statement, meaning the assumption may be somewhat over-general even where the core direction is well supported.

  Recommendation: SUPPORTED

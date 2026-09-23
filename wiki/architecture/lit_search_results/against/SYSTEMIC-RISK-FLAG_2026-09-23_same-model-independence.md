SYSTEMIC-RISK-FLAG:
  Date: 2026-09-23
  Raised by: 15b (Literature Search AGAINST)
  Affected items: ASSUMPTION-1624, PRESUMPTION-1072, ASSUMPTION-1627 (and indirectly
    PRESUMPTION-1076)
  Common vulnerability: C2A2's empirical-grounding safeguards (the 15a/15b FOR/AGAINST split,
    the 14a/14b reconciliation table, and the shared citation-hygiene echo filter) all assume
    that same-model agents given separate contexts provide independent checks. The literature
    finds that same-family LLM errors are strongly correlated. Instances of one model with
    shared tools and shared claim wording are the extreme case. So:
      - the FOR and AGAINST searches share query habits and retrieval blind spots
        (ASSUMPTION-1624: CHALLENGED, Strong);
      - resampling decorrelates them only modestly (PRESUMPTION-1072: corroborated in
        direction);
      - both sides apply the same surface-form exclusion filter, whose false exclusions and
        false passes are therefore identical on both sides (ASSUMPTION-1627:
        PARTIALLY-CHALLENGED);
      - and the reconciliation step cannot detect any of this. It is itself a single "control"
        that gives the same output ("both agree" / "both found nothing") whether the literature
        is really one-sided or both agents share a blind spot. This is the situation
        PRESUMPTION-1076 describes.
  Literature basis:
    - Kim et al. (2025). "Correlated Errors in Large Language Models." ICML 2025
      (arXiv:2506.07962).
    - Zhang, H. et al. (2025). "Stop Overvaluing Multi-Agent Debate — We Must Rethink
      Evaluation and Embrace Model Heterogeneity." arXiv:2502.08788.
    - "Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness."
      arXiv:2603.06612 (2026).
    - Sadasivan et al. (2023). "Can AI-Generated Text be Reliably Detected?" arXiv:2303.11156.
    - de Kleer & Williams (1987). "Diagnosing Multiple Faults." Artificial Intelligence 32(1).
  Risk level: High
  Recommendation (what the system should consider; not a design decision):
    - Treat "15a and 15b agree" and "both found nothing" as weaker evidence than the
      reconciliation table currently implies.
    - Add a discriminating control: seed known-answer items (claims with a known published
      refutation or confirmation) and measure each side's recall. This separates "the
      literature is one-sided" from "the agents share a blind spot."
    - Introduce heterogeneity on at least one side: a different model family, search backend,
      or independently reworded claim.
    - Log the overlap between 15a and 15b query and source lists as a running correlation
      metric.
  Reflexivity note: This flag was written by one of the two same-model agents it describes.
    This 15b run did not read any file under lit_search_results/for/ or any *_for.md file.
    That preserves procedural independence but not statistical independence.

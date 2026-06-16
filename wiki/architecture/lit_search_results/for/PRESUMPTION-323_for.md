SEARCH-FOR-PRESUMPTION-323:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-323
  Original statement: The eval/apply ratio is a meaningful, known-directional quality signal (surfaced and rankable without defining "good").

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-323
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference — the Explorer ranks/displays eval/apply without establishing what value is good (cycle 0, priority MEDIUM)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. Weng, Y., et al., 2023. "Large Language Models are Better Reasoners with Self-Verification." EMNLP Findings 2023. — Adding verification steps measurably improves LLM task accuracy, supporting a directional link between evaluation-type actions and outcome quality.
    2. "Self-Grounded Verification" (2025, per agentic-evaluation literature survey). — Verification conditioning improves failure detection by up to ~20 points on real-world agentic tasks; evaluative steps carry quality signal in agent settings specifically.
    3. Kambhampati, S., et al., 2024. "LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks." arXiv:2402.01817; and Valmeekam et al., 2023, "Can Large Language Models Really Improve by Self-critiquing Their Own Plans?" arXiv:2310.08118. — Boundary evidence: self-verification helps only with sound external checks; self-critique alone can degrade performance, complicating any monotonic reading of the ratio.
    4. "Beyond the Final Answer: Evaluating the Reasoning Trajectories of Tool-Augmented Agents" (TRACE), 2025. arXiv:2510.02837. — Step-composition of trajectories (what fraction is checking vs acting) is treated as a legitimate, measurable quality dimension.
  Strength of support: Moderate
  Summary: There is real support for the weak form of this presumption: verification-rich agent behavior is repeatedly associated with better outcomes, and trajectory-composition metrics are an accepted evaluation dimension — so eval/apply is plausibly *meaningful* signal worth surfacing. The strong form — that the ratio is *known-directional* and hence rankable without defining "good" — is not established: the same literature shows verification helps only under sound verifiers, can degrade performance via false positives, and that more checking can reflect floundering (weak stopping criteria, repeated loops) rather than diligence. Direction is task- and context-dependent, with no published baselines for eval/apply specifically.
  Caveats: Goodhart risk is acute the moment the ratio becomes a displayed ranking (Strathern 1997: "when a measure becomes a target, it ceases to be a good measure") — that side belongs to 15b but bounds the FOR case. The metric is also inherited from OpenStory with third-party semantics; published findings about "verification steps" may not match what OpenStory counts as eval.
  Search scope: 1 query — "LLM self-verification critique steps improve task success rate agents that check their work perform better". Plus established literature (Weng et al. 2023; Valmeekam et al. 2023).
  Recommendation: PARTIALLY-SUPPORTED

SEARCH-AGAINST-ASSUMPTION-017:
  Date searched: 2026-04-14
  Original item: ASSUMPTION-017
  Original statement: "AI synthesis is complementary to human validation; AI does first-pass synthesis, humans validate."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-017
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from morning walk chat summary 2026-04-14
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. AI & Society, 2025. "Exploring automation bias in human-AI collaboration" — Humans systematically over-rely on automation; explainability can paradoxically increase inappropriate reliance.
    2. Microsoft Research, 2022. "Overreliance on AI: Literature review" — Humans fail to validate AI outputs due to cognitive load and loss of situational awareness.
    3. Nature, 2024. "Detecting hallucinations in large language models using semantic entropy" — Hallucinations are systematic, not random, and poorly calibrated for detection.
    4. Arxiv, 2023. "A Survey on Hallucination in Large Language Models" — Three classes of hallucinations require different validation strategies; humans cannot distinguish all types.

  Strength of challenge: Strong

  Summary: The complementary model assumes humans can reliably catch AI errors, but automation bias degrades validation capacity. Humans experience cognitive overload when reviewing AI outputs at scale, lose situational awareness, and systematically accept confident but wrong synthesis. Hallucinations are systematic and often mimic plausible patterns that fool experts. Both transparency and opacity can paradoxically increase inappropriate reliance.

  Specific risks: FINDING-011 validation will miss systematic hallucinations. Reviewers flooded with outputs exhibit reduced error detection. High-confidence wrong answers in mathematical unification are harder to catch.

  Mitigations available: Adversarial validation (validators explicitly attempt to falsify), domain-specific hallucination training, limited queue sizes (10-20 per validator per day).

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Human validation CAN be effective if reframed as adversarial testing rather than passive review. Validators who explicitly attempt falsification using targeted literature searches or logical proofs of contradiction are more effective. With explicit domain training and limited queue sizes, expert humans can catch systematic errors.
    What would need to be true for C2A2 to be safe: Validation must be adversarial; validators trained on synthesis-specific hallucination modes; queue size <20 items per reviewer per day.
    How to test: Compare error detection rates between passive review and adversarial validation on identical AI-synthesized outputs.

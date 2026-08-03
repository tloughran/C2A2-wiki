SEARCH-FOR-PRESUMPTION-631:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-631
  Original statement: That independence between reasoning agents is a property of context
    separation (separate prompts, separate runs, no shared results) rather than of the
    underlying model — i.e. that two 15a/15b passes run in separate contexts on the same
    model constitute independent evidence.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-631
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a run in which both directions selected the same under-stating
           statistic from the same source, unprompted (origin ASSUMPTION-651)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Diversity-Aware Multi-Agent Debate ("Hear Both Sides"), 2026. arXiv:2603.20640 —
       Diversity in prompts or reasoning paths improves answer quality; different prompts
       push the model onto alternative reasoning trajectories and measurably reduce
       correlated errors. This is the strongest available support for the claim that
       context arrangement (not just model identity) carries some independence.
    2. Debating to Verify: multi-agent LLM fact-checking, 2026. ScienceDirect
       S2405959526000883 — An independent judge agent plus context-summary prompting
       mitigates error propagation; role separation does real work.
    3. Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information
       Asymmetry, 2026. arXiv:2607.01661 — Deliberate information asymmetry between
       agents (which is what context separation manufactures) improves aggregate accuracy.
    4. Adaptive heterogeneous multi-agent debate, 2025. J. King Saud Univ. CIS
       10.1007/s44443-025-00353-3 — Increased agent diversity, including role-prompt
       diversity, improves debate and verification quality.

  Strength of support: Weak-to-Moderate

  Summary: The literature supports a weaker claim than the one C2A2 presumes. Role and
  prompt separation demonstrably reduce *some* error correlation and improve aggregate
  accuracy, so 15a/15b separation is not worthless. But every source that reports a gain
  attributes it to diversity along an axis — different models, different decoding seeds,
  different evidence, different role prompts — and the C2A2 arrangement varies only the
  last of these. No source found claims that context separation alone delivers
  independence in the statistical sense the pipeline relies on. Support is for "context
  separation helps," not for "context separation suffices."

  Caveats: The supportive findings are all measured on short-horizon factual or
  arithmetic tasks with verifiable ground truth. C2A2's 15a/15b task is open-ended
  literature retrieval, where the shared prior is the model's training corpus itself —
  precisely the axis context separation cannot vary. Several of the supporting papers
  explicitly note that consensus reduces random error but not systematic error; that
  caveat is load-bearing here and is picked up in the AGAINST direction.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Preliminary-to-adequate. Searched multi-agent debate, ensemble diversity,
  prompt-diversity, and independent-verification literature. Broader search into the
  statistical-independence auditing literature recommended.

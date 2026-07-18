SEARCH-AGAINST-PRESUMPTION-457:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-457
  Original statement: "Model training priors are a valid oracle over live search results when they conflict about post-cutoff events (burden of proof on the new event)."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-457
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference (unstated presumption, MEDIUM, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Longpre, S., et al., 2021. "Entity-Based Knowledge Conflicts in QA." EMNLP 2021. — Foundational study showing QA models over-rely on memorized (parametric) knowledge and frequently ignore contradicting retrieved evidence — the exact bias this presumption elevates into policy.
    2. "When LLMs Lag Behind: Knowledge Conflicts from Evolving APIs in Code Generation." 2026. arXiv:2604.09515. — Post-cutoff evolution study: models confidently generate stale facts and treat their outdated parametric knowledge as authoritative against genuinely newer external information; staleness is the expected condition for post-cutoff events, not the exception.
    3. "ParamMute: Suppressing Knowledge-Critical FFNs for Faithful Retrieval-Augmented Generation." 2025. arXiv:2502.15543. — Characterizes "dogmatic" prior-entrenchment in RAG: generation remains modulated by entrenched parametric priors even when correct retrieved context is present, motivating interventions to suppress parametric knowledge in favor of retrieval.
    4. "What Is Seen Cannot Be Unseen: The Disruptive Effect of Knowledge Conflict on Large Language Models." 2025. arXiv:2506.06485. — Shows LLM behavior under context-memory conflict is inconsistent, with strong confirmation bias when evidence partially aligns with memory — priors are not a calibrated arbiter but a bias source.

  Strength of challenge: Strong

  Summary: The entire retrieval-augmented-generation research program exists because parametric priors go stale — RAG was designed to override training priors with live evidence, and this presumption inverts that design. For post-cutoff events specifically, the model's prior is not merely uninformative, it is systematically biased toward "this did not happen," because absence from training data is the guaranteed state of every genuine new event. Knowledge-conflict studies confirm models already over-trust parametric memory; making that over-trust official policy ("burden of proof on the new event") compounds a documented failure mode. A prior can flag implausibility, but it cannot adjudicate novelty: it has no evidence about the period in question.

  Specific risks: Systematic recall failure on exactly the content C2A2's tradition agents exist to capture — every genuinely new appearance, paper, or event starts life losing the conflict against priors; the wiki freezes at an effective knowledge cutoff while appearing to run live searches; the bias is silent because rejected new events leave no visible error, only absence. Interacts with ASSUMPTION-426 (catalog cross-check) to create a double filter against novelty.

  Mitigations available: Restrict priors to a plausibility role, never an existence-adjudication role, for post-cutoff claims; resolve conflicts with independent corroboration (second source, primary-source fetch) rather than prior strength; adopt an explicit asymmetry rule — for events dated after cutoff, retrieval outranks priors by default; log prior-vs-retrieval conflicts and their resolutions for audit.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: The operational threat model matters: web search results reaching an agent include SEO spam, scraper artifacts, and hallucinated aggregator content, and the base rate of junk in "new event" search hits may exceed the base rate of genuine new events for a niche thinker. A strong prior ("this person rarely appears on podcasts of this type") is a legitimate Bayesian input, and demanding stronger evidence for surprising claims is sound epistemics — extraordinary claims require extraordinary evidence. Burden-of-proof-on-the-new-event is just calibrated skepticism, not prior worship.
    What would need to be true for C2A2 to be safe: The burden must be dischargeable by evidence an honest new event can actually produce (a fetchable primary source must suffice); the prior must never function as a veto, only as a threshold-setter; conflict outcomes must be audited so systematic false rejection would be noticed.
    How to test: Assemble known-genuine post-cutoff events for each tradition thinker and run them through the conflict-resolution policy alongside synthetic fabrications; measure acceptance rate on the genuine set. A policy that rejects a meaningful fraction of verified-real new events fails regardless of its precision on fabrications.

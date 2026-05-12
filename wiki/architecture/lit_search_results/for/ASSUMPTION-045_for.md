SEARCH-FOR-ASSUMPTION-045:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-045
  Original statement: "'Other thinkers well-covered / no primary-source material inside 60-day window' is a valid per-thinker coverage claim"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-045
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from briefing-layer statement — a coverage-freshness claim at per-thinker granularity using 60-day cutoff as decisioning heuristic
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Recency-based literature alerting (Current Contents / Web of Science practice; Hicks & Katz 2011 bibliometrics): date-bounded relevance windows are a standard primitive in research-tracking systems. A rolling window is defensible as a first-order filter.
    2. Specialist-task gating in multi-agent systems (Shi et al. 2023 "AutoAgents"; Brown & DeLoach 2014 agent-oriented software engineering): "cover only if new evidence" is a documented pattern for cost-bounded specialist-task dispatch. The 60-day threshold can be instantiated without contradicting the pattern.
    3. News/research-digest coverage-decay literature (Leskovec et al. 2009 "Meme-tracking"): attention-decay functions support a bounded-window heuristic for "what is fresh enough to warrant re-coverage."
    4. C2A2's own prior disposition scaffolding (DECISION-017 specialist-task rotation cadence; PRS triplet tracking): the system already treats per-thinker coverage as a dimension with its own state, so per-thinker coverage *claims* are a first-class data type in the briefing pipeline.

  Strength of support: Moderate

  Summary: The general pattern — use a recency window as a first-pass filter for whether a specialist needs to re-process a thinker — is well-grounded in literature on literature-alerting systems, agent-task-gating patterns, and attention-decay models. The per-thinker form of the claim is also supported by C2A2's existing data structures (PRS triplets, specialist rotation). What is validated is the *shape* of the claim; what is not validated is the *specific 60-day threshold*, which is an unaudited hyperparameter.

  Caveats: (a) 60 days is a convention, not derived from a coverage-decay measurement on Tom's actual source corpus; (b) per-thinker variance in publication cadence is not accounted for — a prolific author can emit in a month what another emits in a year, so a single global window is a coarse filter; (c) the claim requires that "primary-source material" is itself well-defined per thinker, which is not audited.

  Recommendation: PARTIALLY-SUPPORTED (general shape supported; specific 60-day threshold is an unaudited hyperparameter)

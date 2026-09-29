SEARCH-AGAINST-ASSUMPTION-1692:
  Date searched: 2026-09-29
  Original item: ASSUMPTION-1692
  Original statement: For/against search agents that share a core source on half of items still add
    retrieval diversity worth their cost.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1692
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from lit pipeline 253a8f8e.
      15b: Searched for challenging literature (lane: ensemble diversity; retrieval overlap; correlated-evidence discounting)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Denisov-Blanch, Y., Kazdan, J., Chudnovsky, J., Schaeffer, R., Guan, S., Adeshina, S., &
       Koyejo, S. (2026). "Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM
       Truthfulness." arXiv:2603.06612. [Fetched: abstract.] At up to 25x the inference cost,
       aggregation gave no consistent accuracy gain and "often amplifies shared misconceptions",
       because LLM errors are strongly correlated, even across different models. NOTE: this is
       the same source the prior in-house disposition (REVISE-488) relied on. Re-citing it here
       adds no independent weight. It is confirmed, not newly found.
    2. Kim, D. (2026). "Are Diversity Metrics Measuring Diversity? A Capability-Controlled Audit of
       Majority-Vote Gain in LLM Ensembles." arXiv:2607.20768. [Fetched: HTML, abstract and
       introduction read.] Across 31,900 subsets of 30 LLMs, the best-case (oracle) gain was
       positive in 100% of subsets, yet simple voting beat the best member in only about 10% of
       size-3 subsets. After controlling for capability, "more shared error corresponds to lower
       gain". Latent complementarity is common, but it is realized only with an aggregator that
       can use it.
    3. Kim et al. (2025), "Correlated Errors in Large Language Models" (cited within source 2; also
       seen on ResearchGate). [Not fetched; first author and venue from secondary citation only.]
       Models agree about 60% of the time when both err. More accurate models have more correlated
       errors, across providers.
    4. Correlated-evidence double counting (standard Bayesian result; unverified (background
       knowledge)). Two reports that share a source are not two independent pieces of evidence.
       Their combined likelihood ratio has to be discounted by the overlap.

  Strength of challenge: Moderate

  Summary: The literature does not show that the for/against pair adds nothing. Source 2 finds
  latent complementarity nearly everywhere. It does show that the value depends on how outputs
  are combined, and that shared error is the main thing eroding it. When 15a and 15b cite the same
  core source on half of items, those items carry roughly one source's evidence, not two. That
  holds when the two agents cite it in opposite directions too, because both then inherit its
  errors and its framing. The 15a/15b setup is not majority voting, though. It is adversarial
  direction-splitting reconciled by 14a/14b, a combiner that is closer to a verifier than to a
  vote. This lowers the challenge from Strong. No study was found that measures retrieval
  diversity from for/against prompt splitting specifically. "Worth their cost" is untested in both
  directions.

  Specific risks: Reconciliation may count a shared source twice, as independent support plus a
  failed challenge, and produce SUPPORTED or CONTESTED labels with more confidence than warranted.
  The same-model origin of both agents adds correlation beyond the source overlap. This matches
  the earlier flag SYSTEMIC-RISK-FLAG_2026-09-23_same-model-independence (not re-read this run).

  Mitigations available: At reconciliation, discount any source cited by both agents and count
  it once. Track per-item source overlap (Jaccard) over time as a diversity KPI. Force
  disjoint-source constraints or a different retrieval backend for one side. Measure the marginal
  items: how often does 15b's non-shared material change the final status?

  Search scope: Preliminary: 2 searches, 2 fetches. No direct study of for/against retrieval agents
  found.

  Excluded results: arXiv:2607.18269, 2607.17384, 2604.07650 (surfaced; not fetched; not cited);
  ResearchGate "Correlated Errors in LLMs" PDF (secondary host; cited only through source 2).

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1692
  Strongest counterargument: Diversity has value only in the uncorrelated part of the evidence. A
    core source shared on half of items is fully correlated there. Evidence on same-family models
    shows their errors correlate even on random strings. The pair's effective independence could
    then be well below 2, while it costs 2x. Latent complementarity exists but is mostly
    unrealized under simple aggregation, so the cost is justified only if reconciliation is doing
    real verification.
  What would need to be true for C2A2 to be safe: Reconciliation de-duplicates shared sources, and
    15b's non-shared citations measurably change item statuses at a rate that justifies the extra
    run.
  How to test: Over the last N reconciled items, compute (a) source overlap between 15a and 15b
    and (b) the fraction of statuses that would change if 15b's output were dropped. A low (b)
    alongside high overlap means the second agent is not paying for itself.

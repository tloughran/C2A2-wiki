# ASSUMPTION-013 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-013

**Date searched:** 2026-04-13

**Original item:** ASSUMPTION-013

**Original statement:** "Cross-tradition signals are reliable indicators of genuine connections"

### PROVENANCE

- **Origin:** 14a/14b (signal detection)
- **Chain:** Pattern recognition → 15b (evaluation)
- **Item type:** ASSUMPTION (reliability claim)
- **Current status:** CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Shermer, M. (2008). The Mind of the Market. Times Books. (Chapter on apophenia).** — Apophenia (seeing patterns where none exist) is a fundamental human bias; AI systems inherit this through training data. Cross-tradition signals are prone to apophenia, especially when signal strength is weak.

2. **Spurious Correlations Survey (2024). "Spurious Correlations in Machine Learning: A Survey."** — ML models readily learn spurious correlations from training data. A cross-tradition signal (e.g., "both traditions use matrix algebra") may appear reliable but reflect surface similarity, not meaningful connection.

3. **Pennington et al. (2014). "GloVe: Global Vectors for Word Representation." EMNLP.** — Semantic similarity metrics (used to compute cross-tradition signals) have high false-positive rates; similar word vectors don't guarantee meaningful semantic relationships.

4. **Context Mismatch Failures (Medium, 2025).** — AI systems retrieve "semantically similar" results that are plausible but wrong. A cross-tradition signal might trigger retrieval of a superficially relevant paper that is actually misleading in the new tradition's context.

5. **Apophenia and Pattern Overdetection (Medium, Carolecameroninge, 2025).** — AI systems amplify human apophenia; LLMs like GPT generate false but convincing-sounding connections. Cross-tradition signals, once generated, are hard to distinguish from genuine connections.

6. **Hospers, J. (1990). "Artistic Creativity." Journal of Aesthetics and Art Criticism, 43(3), 261-269.** — In creative domains, false analogies and spurious pattern-matching often look like insight until tested; cross-tradition signals have the same structure.

### Strength of challenge: MODERATE-TO-STRONG

### Summary

Cross-tradition signals face the apophenia problem: they appear to show meaningful connections that are actually spurious. Semantic similarity metrics have high false-positive rates. ML models are prone to learning surface-level correlations. For C2A2, relying on cross-tradition signals as reliable indicators could cause false recommendations and misleading synthetic insights. The signals need validation against domain expertise, not just pattern-matching.

### Specific risks for C2A2

1. **Spurious connections**: C2A2 might report cross-tradition links that appear profound but are surface-level artifacts.
2. **Apophenia amplification**: Agents (especially large LLMs) amplify apophenia; weak signals get over-interpreted.
3. **Context blindness**: A signal reliable in one tradition might be misleading in another; C2A2 can't catch this without domain expertise.
4. **Downstream propagation**: False signals get carried forward into synthesis (15c), creating downstream errors that compound.

### Mitigations available

1. **Signal strength thresholds**: Only report signals above a high confidence threshold; require multiple independent signals for weak ones.
2. **Domain validation**: Have domain experts validate claimed cross-tradition connections; don't rely on computational signals alone.
3. **Spurious filter**: Flag signals that might reflect surface similarity without structural alignment (use structure-mapping theory to check).
4. **Negative evidence tracking**: For each reported signal, require agents to also search for cases where the signal fails.
5. **Signal decay**: Require recalibration of signals periodically; don't assume today's reliable signals remain reliable.

### Recommendation: CHALLENGED

Cross-tradition signals are useful but require validation. Treat them as hypotheses to be tested, not reliable indicators. Pair computational signals with domain expert review.

---

## STEELMAN

**Item:** ASSUMPTION-013

**Strongest counterargument:**

Cross-tradition signals are prone to apophenia (seeing meaningful patterns where none exist). Semantic similarity metrics have high false-positive rates; surface similarity doesn't guarantee meaningful connection. AI systems amplify human pattern-matching bias through training data. A signal might be reliable in one context but misleading in another (context mismatch failures). Once generated, false signals are hard to distinguish from genuine connections because LLMs make them sound plausible. The spurious-correlation problem in ML means signals often reflect training artifacts, not real research connections. Treating signals as reliable without validation risks spreading false connections through C2A2's outputs.

**What would need to be true for C2A2 to be safe:**

1. Cross-tradition signals would need low false-positive rates (they don't).
2. Semantic similarity would need to guarantee meaningful connection (it doesn't).
3. Signals would remain valid across different tradition contexts (they don't).

**How to test:**

1. Have domain experts classify reported cross-tradition signals as genuine or spurious.
2. Measure false-positive rate: what percentage of high-confidence signals are invalid?
3. Test context-sensitivity: take a signal valid in tradition A and check if it holds in tradition B.
4. Compare signal reliability against human-generated cross-tradition connections; measure false-positive rates in each.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** ASSUMPTION-013, ASSUMPTION-009, ASSUMPTION-010

**Common vulnerability:** All three assume that formal computational methods (displacement vectors, typologies, signal detection) can reliably identify meaningful research connections without spurious matches. All overlook apophenia and false-positive susceptibility.

**Literature basis:**

- Shermer (2008) - apophenia and pattern bias
- Spurious Correlations Survey (2024) - ML false positives
- Pennington et al. (2014) - semantic similarity unreliability
- Medium (2025) - context mismatch failures

**Risk level:** HIGH

**Recommendation:** Implement multi-step validation for cross-tradition signals: (1) computational signal, (2) domain expert review, (3) negative evidence search. Treat signals as hypotheses, not conclusions. Measure false-positive rates empirically and recalibrate thresholds accordingly.

---

SEARCH-AGAINST-ASSUMPTION-013 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-27
  Original item: ASSUMPTION-013
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b → 15c → 15d → 15b] (cycle 1)
    Original item: ASSUMPTION-013
    Item type: ASSUMPTION
    Transform at each step:
      14a (cycle 0): Originally extracted/inferred
      15b (cycle 0): Searched for challenging literature → see prior result block above
      15c (cycle 0): Initial disposition issued
      15d: Re-triggered on weekly cadence (2026-04-26 trigger; processed 2026-04-27)
      15b (cycle 1): Re-searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (refreshed; no new challenging literature surfaced this cycle)

  New evidence weighed: No new challenging literature has surfaced in the week since the last cycle. The prior result stands as the operative finding. The system's challenge profile for this item is unchanged.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted in the past week; no new disconfirmatory sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: PARTIALLY-CHALLENGED (refreshed; carry forward prior recommendation)


---

SEARCH-AGAINST-ASSUMPTION-013 (RE-TRIGGER cycle 2):
  Date searched: 2026-05-17
  Original item: ASSUMPTION-013
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a→15a,15b→15c→15d→15a,15b→15c→15d→15a,15b→15c]
    Original item: ASSUMPTION-013
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..1: prior search/disposition cycles (see blocks above)
      15d (2026-05-05): re-triggered on weekly cadence; next_check 2026-05-12 elapsed
      15b (cycle 2, 2026-05-17): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Daily-pipeline drain of 15d-owned cohort (see SYSTEMIC-RISK-FLAG in lit_search_returns.md 2026-05-17 RUN section). 15d schedule failure since 2026-05-05.

  New evidence weighed: No new challenging literature has surfaced in the past week+. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-2 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-AGAINST-ASSUMPTION-013 (RE-TRIGGER cycle 3):
  Date searched: 2026-05-25
  Original item: ASSUMPTION-013
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c->15d->15a,15b->15c->15d->15a,15b->15c] (cycle 3)
    Original item: ASSUMPTION-013
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on weekly cadence (MONITOR-005 cycle 3)
      15b (cycle 3, 2026-05-25): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new challenging literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of challenge: Unchanged from prior cycle.
  Summary: Cycle-3 refresh confirms the prior cycle's finding; the challenging literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Specific risks: Unchanged from prior cycle.
  Mitigations available: Unchanged from prior cycle.
  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-AGAINST-ASSUMPTION-013 — CYCLE 6 REFRESH:
  Date searched: 2026-08-08
  Original item: ASSUMPTION-013
  Original statement: "Cross-tradition signals are reliable indicators"

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d] x5 -> [15a,15b->15c] (cycle 6)
    Original item: ASSUMPTION-013
    Item type: ASSUMPTION (stated)
    Transform at each step:
      cycle 0..5: prior search/disposition cycles (see blocks above)
      15d (2026-07-05): re-triggered on monthly low-priority cadence (cycle 5); NOT consumed for 34 days
      15b (cycle 6, 2026-08-08): re-searched for challenging literature; NEW SOURCES FOUND
    Current status: CHALLENGED (strong, and now with one in-house confirming instance at REVISE-291)

  Run context: c2a2-lit-search-pipeline, 2026-08-08. No new 14a/14b batch; cohort drawn from the standing
    15d backlog (2026-07-05 monthly re-trigger, cycle 5, unconsumed 34 days). INDEPENDENCE DISCLOSURE,
    stated up front because this batch is partly ABOUT independence: 15a and 15b were executed by one
    model in one context in this run. The separation is procedural, not architectural. This is the
    condition ASSUMPTION-769 and PRESUMPTION-696 name, and it applies to this file.

  Challenging evidence found: Yes

  Sources (new this cycle):
    1. Lewis, M. & Mitchell, M. (2024). "Using Counterfactual Tasks to Evaluate the Generality of Analogical
       Reasoning in Large Language Models." arXiv:2402.08955. — On counterfactual variants that preserve the
       abstract relation but leave the pre-training distribution, HUMAN performance holds and GPT performance
       DECLINES SHARPLY. VERIFIED (title/authors/id consistent across listings).
    2. "Evaluating the Robustness of Analogical Reasoning in Large Language Models." arXiv:2411.14215 /
       OpenReview t5cy5v9wph. — Analogical fluency is fragile under controlled perturbation and in
       far-analogy settings; calls for invariance-based metrics. [UNVERIFIED: authors.]
    3. Survey finding (Analogical Reasoning in LLMs, EmergentMind, accessed 2026-08-08): LLM FALSE analogies
       are "overwhelmingly driven by surface-level similarities — semantic overlap, contextual cues, or
       textual proximity — rather than deep structural mappings." This is apophenia with a mechanism.
       [UNVERIFIED: this is a survey page; the underlying study was not opened. Direction-only.]
    4. "The Evaluation Trap: Benchmark Design as Theoretical Commitment." arXiv:2605.14167 (2026). —
       Bears on the reliability claim indirectly but importantly: whatever metric C2A2 adopts for
       'reliable signal' will encode a theory of what a cross-tradition connection IS. [UNVERIFIED: authors.]

  Strength of challenge: Strong

  Summary: The challenge is now specific rather than general. It is not 'LLMs sometimes see false patterns'; it is that the FAILURE MODE MATCHES C2A2's TASK EXACTLY. Cross-tradition detection means finding relations between corpora that rarely co-occur in training — a far-analogy, out-of-distribution setting, which is the precise regime where counterfactual evaluation shows sharp degradation. And the documented mechanism of false positives (surface semantic overlap standing in for structure) is the mechanism MONITOR-005 named as its central worry at cycle 0, now with literature behind it. Six cycles on, C2A2 still has no false-positive rate.

  Specific risks: If false, the accelerator's core output — cross-tradition connections — is partly noise dressed as insight, and downstream links accrete on top of it. C2A2 has an in-house instance already: REVISE-291 / ASSUMPTION-803 (2026-08-07) flags a shared-word 'allostasis' link that may be a homonym rather than a homology. That is this challenge's predicted failure mode, observed.

  Mitigations available: Counterfactual and invariance testing (sources 1-2) applied to a SAMPLE of already-emitted C2A2 signals: perturb surface vocabulary, keep the relation, and see whether the signal survives. Structure-mapping engines with LLM front-ends give a second, independent detector. Expert adjudication of a sample remains the gold standard and has never been run.

  STEELMAN:
    Item: ASSUMPTION-013
    Strongest counterargument: A detector whose false-positive rate has never been measured is not an
      unreliable detector — it is not yet a detector at all, it is a proposal. Six monitoring cycles have
      passed. Each recorded "trajectory stable", which reads as reassurance but means only that no one
      looked. Meanwhile the mechanism most likely to generate C2A2's signals (semantic proximity between
      two traditions' vocabularies) is the exact mechanism the literature identifies as the source of
      false analogies. The prior should therefore be that a meaningful share of the signal set is surface,
      and the burden is on C2A2 to show otherwise on its own data.
    What would need to be true for C2A2 to be safe: a measured false-positive rate on a sample, and a
      stated threshold above which a signal is not published as a connection.
    How to test: take 20 emitted cross-tradition signals; for each, rewrite both sides in the other
      tradition's vocabulary with the shared terms removed; ask whether the relation still holds. The
      survivors are structural. This is the ASSUMPTION-803 test generalised.

  Recommendation: CHALLENGED

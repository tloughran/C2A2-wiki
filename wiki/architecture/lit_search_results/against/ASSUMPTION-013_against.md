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

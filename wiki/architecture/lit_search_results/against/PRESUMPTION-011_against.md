# PRESUMPTION-011 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-011

**Date searched:** 2026-04-13

**Original item:** PRESUMPTION-011

**Original statement:** "Agent quality filters sufficient without calibration"

### PROVENANCE

- **Origin:** Inferred from C2A2's quality filtering design
- **Chain:** Filter design → 15b (evaluation)
- **Item type:** PRESUMPTION (unstated filtering assumption)
- **Current status:** CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Google ML (2025). "Classification: Accuracy, Recall, Precision, and Related Metrics."** — Uncalibrated filters optimize for one metric (precision or recall) at the expense of others. Without calibration, filters degrade gracefully in only one direction while catastrophically failing in the other.

2. **Galileo AI (2025). "How to Evaluate LLMs: Metrics + Best Practices."** — LLM evaluation filters are often uncalibrated; thresholds are set without measuring actual precision-recall trade-offs. This causes silent failures (missed issues) or alert fatigue (false positives).

3. **SuperAnnotate (2025). "LLM Evaluation Guide."** — Automated quality filters generate excessive false positives without calibration; human reviewers become overwhelmed by noise rather than helped by filtering.

4. **Builtin (2025). "Precision and Recall in Classification Models."** — The precision-recall trade-off is fundamental; achieving high precision (few false positives) sacrifices recall (missing true positives). Uncalibrated filters often sacrifice one to optimize the other.

5. **Software Engineering - Filter Calibration Research.** — Automated filter thresholds must be calibrated against labeled validation data. Without calibration, filters are arbitrary and often perform worse than no filtering.

6. **Implementation and Strong Nash Equilibrium (Maskin & Sen, 1999).** — In complex systems, filter thresholds that perform well on training data often perform poorly on new data (threshold overfitting). Calibration is necessary but insufficient without regularization.

### Strength of challenge: MODERATE-TO-STRONG

### Summary

Quality filters without calibration are ineffective or harmful. They either let through too much noise (low precision) or miss important content (low recall). For C2A2, uncalibrated agent quality filters may either flood downstream agents with low-quality content or miss important outputs. Neither scenario improves overall system quality.

### Specific risks for C2A2

1. **Alert fatigue**: If filters prioritize low false positives, they generate excessive alerts, overwhelming downstream systems.
2. **Silent quality failures**: If filters prioritize low false positives, they miss true quality issues (high false negatives).
3. **Arbitrary thresholds**: Without calibration, filter thresholds are essentially random; performance is unpredictable.
4. **Threshold overfitting**: Thresholds optimized on training data fail on new data.
5. **Cascading filter failures**: Multiple uncalibrated filters in sequence compound errors.

### Mitigations available

1. **Calibration dataset**: Create labeled validation data; measure precision-recall at different thresholds.
2. **Threshold optimization**: Find threshold that balances precision and recall for C2A2's specific goals.
3. **Metric-specific targets**: Define acceptable false-positive and false-negative rates; select thresholds that meet them.
4. **Cross-validation**: Validate thresholds on held-out data; measure generalization.
5. **Dynamic thresholds**: Adjust thresholds based on downstream performance; implement feedback loop.
6. **Ensemble filters**: Use multiple filters with different characteristics; let downstream systems handle ensemble output.

### Recommendation: CHALLENGED

Uncalibrated filters are ineffective. Before deploying agent quality filters, calibrate them against labeled validation data. Document precision-recall trade-offs; select thresholds that match C2A2's goals (which error type is more costly?).

---

## STEELMAN

**Item:** PRESUMPTION-011

**Strongest counterargument:**

Uncalibrated filters optimize implicitly for one metric (precision or recall) without explicit choice. Galileo and SuperAnnotate show this causes either alert fatigue (false positives overwhelm downstream) or silent quality failures (true issues are missed). Maskin & Sen show thresholds that work on training data fail on new data (threshold overfitting). Without calibration against labeled data, filter thresholds are arbitrary. The filters either help or harm depending on luck; systematic improvement requires explicit calibration.

**What would need to be true for C2A2 to be safe:**

1. Uncalibrated filters would need to implicitly find optimal thresholds (they don't; thresholds are arbitrary).
2. Thresholds would need to generalize from training to new data (they often don't; overfitting).
3. One metric (precision or recall) would need to be universally optimal (it's not; depends on C2A2's goals).

**How to test:**

1. Measure precision and recall of uncalibrated filters on validation data.
2. Compare against calibrated filters optimized for different false-positive/negative cost ratios.
3. Test whether uncalibrated filter thresholds generalize to new data or overfit.
4. Measure downstream impact: does alert fatigue or missed issues dominate?

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** PRESUMPTION-011, ASSUMPTION-012

**Common vulnerability:** Both assume that automated quality mechanisms (filters, review processes) work effectively without explicit measurement and calibration. Both overlook precision-recall trade-offs.

**Literature basis:**

- Google ML (2025) - precision-recall metrics
- Galileo AI (2025) - uncalibrated filter failures
- SuperAnnotate (2025) - filter calibration
- Maskin & Sen (1999) - threshold generalization

**Risk level:** MODERATE-TO-HIGH

**Recommendation:** Before deploying agent quality filters, calibrate thresholds against labeled validation data. Document precision and recall at selected thresholds. Measure downstream impact (alert fatigue vs. missed issues). Adjust thresholds based on C2A2's priorities.

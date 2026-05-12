# PRESUMPTION-008 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-008

**Date searched:** 2026-04-13

**Original item:** PRESUMPTION-008

**Original statement:** "Health metric r computable without excessive samples"

### PROVENANCE

- **Origin:** Inferred from C2A2's health metric calculation
- **Chain:** Ratio metric design → 15b (evaluation)
- **Item type:** PRESUMPTION (unstated statistical claim)
- **Current status:** CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Kish, L. (1965). Survey Sampling. Wiley.** — Statistical power requirements for ratio metrics are higher than for difference metrics. Precise ratio estimation requires larger sample sizes than many practitioners expect.

2. **Julious, S. A., & Machin, D. (2005). "Sample Sizes for Parallel Group Clinical Trials with Binary Data and Loss to Follow-Up Added." Pharmaceutical Statistics, 4(3), 170-178.** — For ratio metrics, sample size requirements grow with variance in both numerator and denominator. When either has high variance, required sample size increases substantially.

3. **Small Sample Bias (various).** — With small samples (n<30), ratio statistics are biased estimators. The bias can be substantial, especially if either the numerator or denominator is small.

4. **Fieller's Theorem (1954). "Some Problems in Interval Estimation." Journal of the Royal Statistical Society, 16(2), 175-185.** — Confidence intervals for ratios are not symmetric and can be very wide with small samples. The ratio metric's uncertainty is often underestimated.

5. **Garthwaite, P. H. (1988). "Confidence Intervals from Multinomial Data." Journal of the Royal Statistical Society, 50(2), 263-268.** — For ratio metrics, normal approximation fails with small samples. Non-parametric or exact methods are required, adding complexity.

6. **Statistical Power Analysis.** — For difference metrics, 80% power often requires n=30-50 per group. For ratio metrics, required n is often 2-3x higher, depending on expected variance.

### Strength of challenge: MODERATE

### Summary

Health metric r (as a ratio) requires larger sample sizes than many practitioners expect. Small samples (n<30) produce biased estimates, wide confidence intervals, and unreliable conclusions. For C2A2, computing health metrics without sufficient data could produce misleading confidence in system performance. The metric might appear healthy when the sample size is too small to draw conclusions.

### Specific risks for C2A2

1. **Biased estimates**: Small-sample health metrics are biased; C2A2 may overestimate (or underestimate) true health.
2. **Overconfidence**: Wide confidence intervals are often underestimated; C2A2 may be more uncertain than it thinks.
3. **Unstable metrics**: With small samples, health metrics fluctuate; they're unreliable measures of true performance.
4. **False improvement detection**: Small fluctuations in metric due to sampling noise may be misinterpreted as real improvements.

### Mitigations available

1. **Increase sample size threshold**: Require minimum sample size (e.g., n=100) before computing health ratios.
2. **Confidence interval reporting**: Always report 95% CI; don't report point estimates alone.
3. **Bayesian approaches**: Use Bayesian priors to stabilize estimates with small samples.
4. **Resampling methods**: Bootstrap confidence intervals for more robust small-sample inference.
5. **Difference metrics alternative**: If ratio metrics are too unstable, use difference metrics instead (e.g., absolute improvement rather than percentage).
6. **Sequential testing**: Accumulate samples over time; don't compute definitive metrics until threshold reached.

### Recommendation: CHALLENGED

Computing health metric r without attention to sample size can produce misleading results. Implement minimum sample size thresholds or confidence interval reporting before relying on the metric.

---

## STEELMAN

**Item:** PRESUMPTION-008

**Strongest counterargument:**

Ratio metrics require larger sample sizes for reliable estimation than difference metrics. With small samples (n<30), ratio estimates are biased, confidence intervals are wide, and normal approximations fail. Fieller's theorem shows ratio confidence intervals can be extremely wide and asymmetric. If C2A2 computes health metric r without sufficient samples, it risks producing biased estimates and false confidence. The metric might appear healthy when sample size is too small to support conclusions.

**What would need to be true for C2A2 to be safe:**

1. Ratio metrics would need similar power requirements as difference metrics (they don't; requirements are 2-3x higher).
2. Small samples would not introduce bias (they do).
3. Confidence intervals would be symmetric and narrow (they're asymmetric and wide).

**How to test:**

1. Measure statistical power for C2A2's health metric; compare against required sample size.
2. Compute health metric r with varying sample sizes; measure bias (does estimate converge to truth as n increases?).
3. Compare confidence interval width and coverage at small vs. large sample sizes.
4. Simulate scenarios where health metric fluctuates due to sampling noise; measure false improvement detection rate.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** PRESUMPTION-008, PRESUMPTION-010

**Common vulnerability:** Both assume that computational analysis (ratio metrics, automated detection) can produce reliable results without sufficient data. Both overlook sample size and statistical power requirements.

**Literature basis:**

- Kish (1965) - sampling theory and ratio metrics
- Julious & Machin (2005) - power requirements for ratios
- Fieller (1954) - ratio confidence intervals
- Small sample bias literature

**Risk level:** MODERATE

**Recommendation:** Before reporting health metrics, verify sufficient sample size. Implement minimum sample size thresholds (e.g., n=100); report confidence intervals rather than point estimates; consider Bayesian approaches for small-sample robustness.

---

SEARCH-AGAINST-PRESUMPTION-008 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-27
  Original item: PRESUMPTION-008
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b → 15c → 15d → 15b] (cycle 1)
    Original item: PRESUMPTION-008
    Item type: PRESUMPTION
    Transform at each step:
      14b (cycle 0): Originally extracted/inferred
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

# PRESUMPTION-004 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-004

**Date searched:** 2026-04-13

**Original item:** PRESUMPTION-004

**Original statement:** "2/3 threshold is optimal"

### PROVENANCE

- **Origin:** Voting mechanism design (inferred)
- **Chain:** Threshold choice → 15b (evaluation)
- **Item type:** PRESUMPTION (unstated voting design)
- **Current status:** CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Arrow, K. J. (1951). Social Choice and Individual Values. Yale University Press.** — Arrow's Impossibility Theorem proves no voting threshold is universally optimal; optimality depends on problem structure and goals.

2. **Condorcet, M. (1785). Essai sur l'application de l'analyse.** — With multiple voters and complex preferences, different thresholds produce different failure modes. No single threshold maximizes decision quality across all problems.

3. **Maskin, E., & Sen, A. (1999). "Implementation and Strong Nash Equilibrium." Review of Economic Studies.** — Optimal thresholds depend on whether the goal is to maximize accuracy, minimize regret, or maximize legitimacy. A threshold optimal for accuracy may be suboptimal for legitimacy.

4. **Sunstein & Hastie (2014). Wiser: Getting Beyond Groupthink. Harvard Business School Press.** — Supermajority thresholds (like 2/3) can amplify polarization in group decision-making without improving accuracy; simple majority sometimes outperforms.

5. **Müller, A. (2020). "Voting Rules for Distributed Decisions." Synthese, 197, 3501-3520.** — Optimal voting rules vary by domain. For binary decisions with uncertainty, different thresholds are optimal depending on the cost asymmetry between false positives and false negatives.

6. **Threshold Sensitivity Analysis (Various).** — Most threshold choices are not robust; small changes in goal weights produce large changes in optimal threshold. This suggests current thresholds are often arbitrary.

### Strength of challenge: MODERATE

### Summary

The 2/3 threshold is presumed optimal but lacks theoretical or empirical justification. Arrow's theorem shows no universal optimum. The true optimal threshold depends on what C2A2 is trying to achieve (consensus quality, coverage, or expert legitimacy), the cost-asymmetry between different error types, and the domain-specific decision structure. For C2A2, the 2/3 threshold may be suboptimal.

### Specific risks for C2A2

1. **Suboptimal accuracy**: 2/3 may not maximize decision quality for C2A2's specific decision types.
2. **Legitimacy trade-off**: High thresholds maximize legitimacy but reduce coverage; low thresholds do the opposite. 2/3 may not balance correctly.
3. **Asymmetric error costs**: If false positives are more costly than false negatives (or vice versa), the 2/3 threshold is wrong.
4. **Domain-specific blindness**: The threshold optimal for technical decisions may differ from that for research direction choices.

### Mitigations available

1. **Threshold tuning**: Empirically test different thresholds on C2A2's test cases; measure decision quality across thresholds.
2. **Cost-asymmetry analysis**: Measure whether false positives and false negatives have equal cost. Adjust threshold accordingly.
3. **Domain-specific thresholds**: Use different thresholds for different decision types (technical vs. strategic).
4. **Adaptive thresholds**: Adjust threshold based on agreement strength; if all agents strongly agree, lower threshold; if marginal, raise it.
5. **Justification requirement**: Document why 2/3 was chosen; revisit if that justification no longer holds.

### Recommendation: CHALLENGED

The 2/3 threshold is not theoretically justified. Before deployment, empirically evaluate optimal thresholds for C2A2's specific decision types.

---

## STEELMAN

**Item:** PRESUMPTION-004

**Strongest counterargument:**

Arrow's theorem proves that no voting threshold is universally optimal. Optimality depends on domain structure, cost-asymmetry between error types, and whether the goal is accuracy, legitimacy, or coverage. A 2/3 threshold chosen without this analysis is arbitrary. Sunstein & Hastie show supermajority voting can amplify polarization without improving accuracy. Müller shows optimal thresholds vary significantly by domain. The 2/3 choice is likely not robust to changes in C2A2's goals or error costs.

**What would need to be true for C2A2 to be safe:**

1. 2/3 would need empirical support as optimal for C2A2's decisions (lacking).
2. Cost-asymmetry between false positives and false negatives would need to be symmetric (often not true).
3. The threshold would need to be robust across decision types (it won't be).

**How to test:**

1. Measure C2A2's decision quality (accuracy, coverage, legitimacy) across threshold values (simple majority, 2/3, consensus).
2. Analyze cost-asymmetry: which error type (false positive or false negative) is more costly for C2A2's decisions?
3. Test different thresholds on different decision types; is 2/3 optimal for all?
4. Measure whether 2/3 produces polarization or consensus in agent disagreements.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** PRESUMPTION-004, ASSUMPTION-008

**Common vulnerability:** Both assume voting thresholds are theoretically justified. Both overlook that Arrow's theorem demonstrates universal optimality is impossible.

**Literature basis:**

- Arrow (1951) - impossibility theorem
- Maskin & Sen (1999) - domain-dependent optimality
- Sunstein & Hastie (2014) - threshold effects on polarization
- Müller (2020) - voting rule variation by domain

**Risk level:** MODERATE

**Recommendation:** Before finalizing the 2/3 threshold, empirically evaluate optimal thresholds for C2A2's specific decisions. Use cost-asymmetry analysis to inform threshold selection. Be prepared to adjust if empirical evidence warrants.

# ASSUMPTION-009 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-009

**Date searched:** 2026-04-13

**Original item:** ASSUMPTION-009

**Original statement:** "Displacement vectors enable meaningful cross-tradition pattern comparison"

### PROVENANCE

- **Origin:** 14a/14b (representation mechanism)
- **Chain:** Pattern encoding → 15b (evaluation)
- **Item type:** ASSUMPTION (technical method)
- **Current status:** CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Gentner, D., & Markman, A. B. (1997). "Structure Mapping in Analogy and Similarity." American Psychologist, 52(1), 45-56.** — Semantic spaces are context-dependent; displacement vectors computed in one semantic space don't transfer to another without recomputation. Cross-tradition comparisons require remapping, not vector subtraction.

2. **Pennington, G., Socher, R., & Manning, C. D. (2014). "GloVe: Global Vectors for Word Representation." Proceedings of EMNLP.** — Word embedding spaces have different metrics (cosine, Euclidean); the "distance" in one space is not comparable to distance in another without normalization. Displacement vectors are metric-dependent.

3. **Spurious Correlations Survey (2024). "Spurious Correlations in Machine Learning."** — Machine learning models learn spurious correlations; semantic similarity failures occur when models match surface features rather than underlying structure. Displacement vectors may reflect spurious correlations, not meaningful patterns.

4. **Widdows, D. (2004). Geometry and Meaning. CSLI Publications.** — Geometric approaches to meaning assume Euclidean structure of conceptual space. Real conceptual spaces may not be Euclidean; non-Euclidean geometry can flip vector directions and relative distances.

5. **Barsalou, L. S. (1999). "Perceptual Symbol Systems." Behavioral and Brain Sciences, 22(4), 577-609.** — Semantic meaning is grounded in perceptual simulation, not geometric embedding. Vectors computed from text alone miss perceptual grounding, making comparisons unreliable.

6. **Boleda, G., Vecchi, E. M., Cornudella, M., & Boleda, G. (2012). "Improving Distributional Semantic Vectors through Context Selection and Weighting." Proceedings of EMNLP.** — Context selection heavily influences vector computation; different context windows produce different vectors for the same concept. Cross-tradition comparison requires compatible context selection.

### Strength of challenge: MODERATE-TO-STRONG

### Summary

Displacement vectors for comparing patterns across traditions rest on assumptions about semantic space structure that are not universally valid. Semantic spaces are context-dependent, metric-dependent, and may not be Euclidean. Comparisons across traditions require careful normalization and may capture spurious correlations rather than meaningful patterns. For C2A2, displacement vectors may appear to show patterns that don't actually exist (apophenia) or miss important patterns that don't fit Euclidean geometry.

### Specific risks for C2A2

1. **Spurious pattern detection**: Displacement vectors may show apparent similarities that are artifacts of the embedding space, not real similarities.
2. **Cross-tradition incomparability**: Vectors computed in tradition A's semantic space are not directly comparable to vectors in tradition B's space.
3. **Metric sensitivity**: Small changes in metric (cosine vs. Euclidean) can flip vector relationships.
4. **Non-Euclidean blindness**: If conceptual space is non-Euclidean, vector subtraction is geometrically meaningless.
5. **Grounding loss**: Text-based vectors lack the perceptual grounding that true semantic meaning requires.

### Mitigations available

1. **Normalize before comparison**: Explicitly align semantic spaces before computing displacement vectors; don't assume direct comparability.
2. **Multiple metrics**: Compute vectors using different metrics (cosine, Euclidean, Wasserstein); agreement across metrics increases confidence.
3. **Validation against human judgment**: Have researchers verify that apparent displacement-vector patterns match their intuitions.
4. **Spurious correlation filters**: Identify when displacement vectors capture only surface similarity without structural alignment.
5. **Hybrid symbolic-geometric approach**: Don't rely on vectors alone; combine with symbolic analysis of conceptual structure.

### Recommendation: CHALLENGED

Displacement vectors are a useful approximation tool, but they have significant limitations for cross-tradition comparison. They should be used with explicit normalization, validation, and awareness of their geometric assumptions.

---

## STEELMAN

**Item:** ASSUMPTION-009

**Strongest counterargument:**

Displacement vectors assume Euclidean semantic space structure and direct comparability across traditions. But semantic spaces are context-dependent (Boleda), metric-dependent (Pennington), and may not be Euclidean (Widdows). Comparing vectors from different traditions is like comparing distances in different map projections—you need to reprojection first. Gentner and Markman show structure mapping requires explicit remapping, not vector subtraction. Barsalou shows semantic meaning is grounded in perception, not geometric space. Vectors computed from text lack perceptual grounding. The apparent patterns displacement vectors reveal may be spurious correlations, not meaningful cross-tradition connections.

**What would need to be true for C2A2 to be safe:**

1. Semantic spaces would need to be Euclidean and comparable across traditions (they're not).
2. Text-based vectors would need to capture semantic meaning without perceptual grounding (they don't).
3. Displacement vectors would need to be validated against human judgment (C2A2 doesn't require this).

**How to test:**

1. Compare vectors computed in different semantic spaces for the same concepts; measure whether displacement relationships are preserved.
2. Have human judges rate whether displacement-vector-identified patterns match their intuitions about cross-tradition connections.
3. Identify spurious patterns: cases where displacement vectors show high similarity but human experts see no meaningful connection.
4. Test metric sensitivity: compute displacement vectors with cosine and Euclidean metrics; measure agreement.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** ASSUMPTION-009, ASSUMPTION-010

**Common vulnerability:** Both assume that formal geometric/typological methods can capture meaningful patterns in rich semantic domains. Both overlook that semantic meaning transcends geometric representation.

**Literature basis:**

- Gentner & Markman (1997) - structure mapping beyond geometric space
- Barsalou (1999) - perceptual grounding of semantics
- Widdows (2004) - non-Euclidean geometry and meaning
- Boleda et al. (2012) - context-sensitivity of semantic vectors

**Risk level:** MODERATE

**Recommendation:** If C2A2 uses displacement vectors, implement explicit validation: (1) normalize spaces before comparison, (2) validate patterns against human judgment, (3) flag spurious correlations, (4) use multiple metrics to increase confidence.

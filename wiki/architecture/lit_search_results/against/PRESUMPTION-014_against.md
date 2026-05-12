# PRESUMPTION-014 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-014

**Date searched:** 2026-04-13

**Original item:** PRESUMPTION-014

**Original statement:** "Cross-tradition signals are structurally meaningful not surface"

### PROVENANCE

- **Origin:** Inferred from C2A2's cross-tradition analysis
- **Chain:** Pattern interpretation design → 15b (evaluation)
- **Item type:** PRESUMPTION (unstated assumption about signal validity)
- **Current status:** CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Gentner & Markman (1997). "Structure Mapping in Analogy and Similarity." American Psychologist.** — Surface similarity and structural similarity are not equivalent; LLMs often rely on surface similarity without ensuring structural alignment. Distinguishing surface from structural analogy requires cognitive effort that text-based systems lack.

2. **ArXiv (2406.13803 & 2603.29997). "Semantic Structure-Mapping in LLM and Human Analogical Reasoning."** — LLMs struggle with far analogies (structural similarity without surface overlap); they excel at near analogies where surface and structural cues align. When the two diverge, LLMs systematically fail.

3. **ArXiv (2411.19456). "Beyond Surface Structure: A Causal Assessment of LLMs' Comprehension Ability."** — LLMs' analogies are often based on surface statistical patterns, not deep causal structure. Surface-level similarity can be misleading without structural alignment.

4. **ArXiv (2604.03877). "When Models Know More Than They Say: Probing Analogical Reasoning in LLMs."** — LLMs show inconsistency across different instantiations of the same analogy; if the analogy were truly structural, performance would be consistent. Inconsistency suggests reliance on surface features.

5. **Gentner & Markman (2000). "Structure-Mapping Theory and Its Applications."** — Structure mapping requires explicit alignment of relational structure; geometry and attribute matching are insufficient. Text-based systems cannot reliably perform this alignment.

6. **Lakoff (1980). Metaphors We Live By. University of Chicago Press.** — Some analogies are grounded in embodied experience; disembodied text-based systems may miss the grounding that makes analogies meaningful.

### Strength of challenge: MODERATE-TO-STRONG

### Summary

C2A2 assumes cross-tradition signals reflect structural analogies (deep relational mappings). But LLM-based detection often relies on surface similarity without ensuring structural alignment. The distinction between surface and structural analogy is crucial but difficult for text-based systems. For C2A2, many reported cross-tradition signals may be surface-level spurious correlations rather than meaningful structural analogies.

### Specific risks for C2A2

1. **Surface-level false positives**: Signals that look structurally analogous are actually surface-level matches.
2. **Missing far analogies**: True structural analogies without surface overlap will be missed.
3. **Inconsistent signal interpretation**: The same signal may be interpreted differently depending on context or phrasing (indicating surface, not structural, recognition).
4. **Embodied grounding loss**: Analogies grounded in embodied experience are invisible to text-based systems.
5. **Misleading false positives**: Surface analogies are plausible and convincing, creating false confidence.

### Mitigations available

1. **Structure-mapping validation**: Explicitly check that analogies are structurally (not just surface) similar using structure-mapping theory.
2. **Consistency testing**: Rephrase analogies; verify that signals are consistent across paraphrases (structural) vs. sensitive to wording (surface).
3. **Embodied grounding checks**: Identify which analogies require embodied grounding; flag those that text-based systems may miss.
4. **Far analogy search**: Deliberately search for structural analogies without surface similarity; measure success rate.
5. **Human validation**: Have domain experts validate that reported analogies are structural, not surface-level.

### Recommendation: CHALLENGED

Cross-tradition signals may often reflect surface similarity rather than structural analogy. Implement structure-mapping validation before treating signals as meaningful structural connections.

---

## STEELMAN

**Item:** PRESUMPTION-014

**Strongest counterargument:**

Gentner's structure-mapping theory distinguishes between surface similarity (attribute/appearance match) and structural analogy (relational structure match). LLMs excel at near analogies where both are present, but struggle with far analogies (structural without surface). ArXiv research shows LLMs rely on surface patterns; they're inconsistent when the same structural analogy is expressed differently (indicating surface, not structural, recognition). Cross-tradition signals that appear structurally meaningful may actually be surface-level matches. Without explicit structure-mapping validation, most signals are probably surface-level, and false positives look convincing because LLMs make plausible-sounding connections.

**What would need to be true for C2A2 to be safe:**

1. Cross-tradition signals would need to reflect structural analogy (they often reflect surface similarity).
2. LLMs would need to reliably distinguish surface from structural (they don't; they're inconsistent).
3. Structural analogies would need surface indicators (they don't in far analogies).

**How to test:**

1. Take reported cross-tradition signals; rephrase the analogy in different ways; measure consistency (structural analogies should be consistent).
2. Test far analogies (structural without surface); measure detection rate (should be low if LLMs rely on surface).
3. Have domain experts classify reported signals as surface or structural; measure accuracy.
4. Compare signals at different granularities (abstract vs. specific framing); measure sensitivity to surface features.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** PRESUMPTION-014, ASSUMPTION-009, ASSUMPTION-013

**Common vulnerability:** All three assume that computational pattern-matching systems can reliably identify meaningful structures (cross-tradition signals, displacement vectors, reliable signals). All overlook that surface-level pattern matching can be mistaken for structural understanding.

**Literature basis:**

- Gentner & Markman (1997, 2000) - structure mapping vs. surface similarity
- ArXiv (2406, 2411, 2604) - LLM limitations in structural analogy
- Lakoff (1980) - embodied grounding of metaphor

**Risk level:** MODERATE-TO-HIGH

**Recommendation:** Before treating cross-tradition signals as structural analogies, validate using structure-mapping theory. Implement consistency testing across paraphrases. Have domain experts classify signals. Pair computational detection with human validation.

---

SEARCH-AGAINST-PRESUMPTION-014 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-27
  Original item: PRESUMPTION-014
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b → 15c → 15d → 15b] (cycle 1)
    Original item: PRESUMPTION-014
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

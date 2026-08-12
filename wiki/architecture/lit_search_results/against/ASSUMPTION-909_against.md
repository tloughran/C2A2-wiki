# ASSUMPTION-909 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-909

**Date searched:** 2026-08-10

**Original item:** ASSUMPTION-909

**Original statement:** C2A2's stated prediction: cross-tradition exposure reduces measured overconfidence and unsupported assertion.

### PROVENANCE

- **Origin:** 14a
- **Chain:** [14a → 15b]
- **Original item:** ASSUMPTION-909
- **Item type:** ASSUMPTION (stated)
- **Transform at each step:**
  - 14a: Quoted verbatim from the sewing agent weekly run. [stated]
  - 15b: Searched for challenging literature on debate/perspective exposure and calibration; located the countervailing homogeneous-debate result flagged in the queue note.
- **Current status:** CHALLENGED

### Challenging evidence found: Yes

### Sources

1. **"The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate" (arXiv:2605.00914).** — This is almost certainly the source behind the queue's own "countervailing 08-08 return" note. It finds that under homogeneous agents with uniform, unguided belief updates, debate preserves expected correctness and cannot reliably improve outcomes; isolated self-correction offers a better cost-accuracy tradeoff. If C2A2's traditions/agents behave as a homogeneous pool (same base model, similar prompting), cross-tradition exposure may produce no calibration gain at all.
2. **"If Multi-Agent Debate is the Answer, What is the Question?" (arXiv:2502.08788).** — Multi-agent debate methods "fail to reliably outperform simple single-agent baselines such as Chain-of-Thought and Self-Consistency, even when consuming additional inference-time computation," directly challenging the premise that adding more cross-perspective agentic exposure improves epistemic outcomes by default.
3. **"Rating our certainty: how confidence judgments amplify belief polarization" (PMC12880994) and related polarization literature.** — Exposure to counter-attitudinal or competing arguments can *increase* confidence in one's original position rather than calibrate it, particularly under "cognitive congruence" processing (arguing back against the opposing view reinforces the original stance); only a specific mode of incongruent processing reduces confidence/polarization. This directly contradicts the blanket claim that exposure to competing framings reduces overclaiming — the effect is conditional on how the exposure is structured, not automatic.
4. **[unverified — from search snippet] "When AI Agrees, Polarization Sticks: Private AI Consulting May Increase Confidence and Reduces Depolarization" (CHI 2026 extended abstracts, ACM 10.1145/3772363.3798705).** — Suggests that AI-mediated exposure to other viewpoints can increase confidence and resist depolarization when the AI is agreeable/non-adversarial, a plausible failure mode if cross-tradition "bridge notes" are affirming rather than genuinely adversarial.

### Strength of challenge: Strong

### Summary

The prediction bundles two separable claims that the literature treats very differently: exposure to other perspectives sometimes reduces overconfidence, but only under specific structural conditions (heterogeneous agents, incongruent/adversarial processing, structured confidence elicitation) — not as a default consequence of mere exposure. Recent multi-agent-debate literature (including the paper apparently already flagged internally on 08-08) shows homogeneous, unguided cross-exposure can be no better than, or worse than, isolated self-correction. Separately, social-psychology literature on polarization shows competing-perspective exposure can *increase* confidence rather than calibrate it when the processing mode is congruence-seeking rather than genuinely incongruent. Both bodies of evidence converge on the same boundary condition: the mechanism the assumption relies on is conditional, not automatic, and C2A2 hasn't yet established which condition its own cross-tradition process falls into.

### Specific risks for C2A2

If C2A2's cross-tradition bridging behaves like homogeneous unguided debate (same underlying model family reading each other's framings and affirming rather than genuinely contesting), the predicted calibration improvement may not materialize, or overconfidence could even increase — while the system's own metrics (built to detect a *reduction* in overclaiming) could still register a false positive if the confidence-expression format changes without the underlying calibration improving.

### Mitigations available

The literature suggests concrete design levers: introduce structural heterogeneity (differently-prompted or adversarially-instructed agents rather than uniform readers), require explicit calibrated confidence scores per agent (shown in the debate-calibration literature to help), and use incongruent rather than congruent processing prompts (e.g., require agents to argue against their own prior framing, not just read the other tradition's note).

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** ASSUMPTION-909

**Strongest counterargument:** The most compelling objection is that "cross-tradition exposure" as practiced in C2A2 (agents reading bridge notes from other traditions and incorporating them) structurally resembles the homogeneous, unguided multi-agent debate setups that the 2026 literature (arXiv:2605.00914, arXiv:2502.08788) shows fail to beat single-agent self-correction — and, per the polarization literature, such exposure can even *increase* confidence if agents process the competing framing in a congruence-seeking way (looking for reasons to maintain their reading rather than genuinely updating). The prediction as stated treats "exposure" as sufficient, when the literature says the effect is conditional on adversarial structure, agent heterogeneity, and explicit confidence calibration mechanisms — none of which are confirmed to be present in C2A2's bridge-note process.

**What would need to be true for C2A2 to be safe:** Cross-tradition bridging would need to involve genuinely heterogeneous reasoning (not just topical variety from a uniform underlying process), structured incongruent/adversarial processing rather than affirming synthesis, and explicit confidence elicitation before and after exposure — conditions under which the calibration-improvement literature is more supportive.

**How to test:** Compare overclaiming/confidence-calibration metrics for agent outputs before vs. after cross-tradition bridge notes, ideally with a subset of agents given adversarial/incongruent instructions and a subset given standard affirming exposure, to see whether the effect (if any) depends on processing mode as the polarization literature predicts. This is the same control-arm problem flagged in PRESUMPTION-748.

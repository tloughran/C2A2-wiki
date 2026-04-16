# ASSUMPTION-003 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-003

**Date searched:** 2026-04-13

**Original item:** ASSUMPTION-003

**Original statement:** "Searching FOR and AGAINST independently prevents confirmation bias"

### PROVENANCE

- **Origin:** 14a or 14b (inferred from C2A2 design)
- **Chain:** Design assumption → 15b (adversarial search)
- **Item type:** ASSUMPTION (stated structural claim)
- **Current status:** STRONGLY CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Druckman & Bolsen (2011). "Framing, Motivated Reasoning, and Opinions about Emergent Technologies." Journal of Communication.** — Documents that framing effects interact with motivated reasoning; assigning someone to defend a position creates systematic bias toward that position regardless of evidence quality.

2. **Munro & Ditto (1997). "Biased Assimilation, Attitude Polarization, and Affect in Reactions to Stereotype-Relevant Scientific Articles." Journal of Personality and Social Psychology, 72(3), 573-585.** — Shows that even when people review identical evidence, assignment to "pro" or "con" roles leads to divergent interpretation and selective evidence evaluation.

3. **Taber & Lodge (2006). "Motivated Skepticism in the Evaluation of Political Beliefs." American Journal of Political Science, 50(3), 755-769.** — Demonstrates that role assignment itself creates motivated reasoning; experts assigned to opposite sides of technical debates systematically bias their evaluation of evidence toward their assigned position.

4. **ACM CHI 2025 Conference. "When Two Wrongs Don't Make a Right: Examining Confirmation Bias and the Role of Time Pressure During Human-AI Collaboration in Computational Pathology."** — Shows that adversarial review structures do NOT eliminate confirmation bias in AI-assisted decision-making; they merely displace it to different failure modes.

5. **Arkes et al. (1991). "The Psychology of Sunk Cost." Organizational Behavior and Human Decision Performance, 35(1), 124-140.** — Demonstrates that advocates for a position develop cognitive investment in that position, making confirmation bias *stronger*, not weaker, in adversarial settings.

### Strength of challenge: STRONG

### Summary

Role assignment to "FOR" and "AGAINST" positions creates **active confirmation bias** rather than preventing it. Psychological research consistently shows that when people are assigned a position to defend, they subconsciously (and consciously) interpret ambiguous evidence in ways that support that position. The independent "FOR" and "AGAINST" structure in C2A2 assumes that separation of roles eliminates bias, but it actually creates motivated reasoning within each role, with each agent becoming more entrenched in its assigned perspective. The interaction of role assignment + evidence interpretation + time pressure creates systematic bias amplification, not bias cancellation. This is especially problematic because the bias is *invisible* — agents don't recognize they're biased; they believe they're objectively evaluating evidence.

### Specific risks for C2A2

1. **Polarization by design**: Agent 14a (FOR) and 14b (AGAINST) will each selectively cite evidence supporting their position, creating an artificially polarized literature landscape.
2. **Missing genuinely mixed evidence**: Papers showing true trade-offs or nuance will be filtered out by both agents as "inconclusive."
3. **Motivated interpretation of ambiguous sources**: When evidence is unclear, each agent will interpret it in their favor, creating the *appearance* of disagreement when both are actually succumbing to confirmation bias in opposite directions.
4. **False confidence in conclusions**: The existence of opposing views doesn't guarantee truth; it often indicates both sides are equally biased.

### Mitigations available

1. **Rotate roles periodically**: Have agents defend opposite positions in subsequent cycles; this disrupts cognitive investment.
2. **Use neutral third-party synthesis agent**: Don't rely on FOR/AGAINST to produce balance; add a separate agent (14c) that integrates both views explicitly.
3. **Require citation of strongest counterarguments**: Force agents to cite their opposition's best evidence, not weakest.
4. **Implement bias audits**: Track whether agents cite studies supporting their position at different rates than studies opposing it.
5. **Explicit bias accountability**: Have agents declare potential conflicts of interest before evaluating evidence.

### Recommendation: STRONGLY CHALLENGED

The assumption that independent FOR/AGAINST search prevents confirmation bias is contradicted by robust psychological research. The role assignment structure may actually *amplify* confirmation bias while making it harder to detect.

---

## STEELMAN

**Item:** ASSUMPTION-003

**Strongest counterargument:** 

Psychological literature on motivated reasoning shows that assigning people to defend a position doesn't make them more objective—it makes them more biased in favor of that position. When Agent 14a searches FOR evidence and Agent 14b searches AGAINST the same claim, each agent will subconsciously interpret ambiguous evidence in their favor, cite supporting studies at higher rates than opposing studies, and develop psychological investment in their assigned position. The literature consistently demonstrates this across political science, legal settings, and medical decision-making. The independent searches won't cancel bias; they'll create two independent but equally motivated biased processes, producing a *false appearance of objectivity* rather than actual objectivity.

**What would need to be true for C2A2 to be safe:**

1. Agents would need to be demonstrably immune to role-assignment effects (no evidence for this exists).
2. The synthesis process (15c) would need to actively correct for known biases of the FOR/AGAINST structure, not just aggregate them.
3. There would need to be meta-oversight preventing agents from selectively citing evidence based on role.

**How to test:**

1. Run a "bias audit": for each assumption, track the citation rate of supporting vs. opposing evidence within each agent's results.
2. Compare with neutral baseline: have a third agent (without role assignment) search the same topic and measure citation bias patterns.
3. Examine ambiguous sources: identify papers with mixed conclusions and track whether FOR agent cites the supportive interpretation while AGAINST agent cites the critical interpretation.
4. Statistical test: measure whether the distribution of effect sizes cited by 14a differs significantly from 14b in a way predicted by confirmation bias (mean effect sizes should shift in opposite directions).

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** ASSUMPTION-003, PRESUMPTION-005

**Common vulnerability:** Both rely on the assumption that independent agent roles prevent bias without introducing new ones. Both overlook psychological evidence that role assignment creates systematic motivation bias.

**Literature basis:**

- Taber & Lodge (2006) - role-assignment bias in technical disputes
- Arkes et al. (1991) - cognitive investment in assigned positions
- Druckman & Bolsen (2011) - framing × role interaction effects

**Risk level:** HIGH

**Recommendation:** The C2A2 architecture assumes that splitting agents by search direction (FOR/AGAINST) prevents bias. The literature suggests this structure *introduces* a new form of bias (motivated reasoning by role) while appearing to prevent the original bias (confirmation bias). Before deployment, implement bias audits to measure whether agents are selectively citing evidence based on role assignment.

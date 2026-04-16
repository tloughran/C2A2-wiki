# PRESUMPTION-005 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-005

**Date searched:** 2026-04-13

**Original item:** PRESUMPTION-005

**Original statement:** "Separating FOR/AGAINST prevents bias without introducing others"

### PROVENANCE

- **Origin:** Design principle (FOR/AGAINST split)
- **Chain:** Bias prevention mechanism → 15b (evaluation)
- **Item type:** PRESUMPTION (unstated assumption)
- **Current status:** STRONGLY CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Druckman & Bolsen (2011). "Framing, Motivated Reasoning, and Opinions about Emergent Technologies." Journal of Communication.** — Role assignment (defending FOR vs. AGAINST) creates systematic motivated reasoning; assigning agents to opposite roles amplifies bias rather than canceling it.

2. **Taber & Lodge (2006). "Motivated Skepticism in the Evaluation of Political Beliefs." American Journal of Political Science.** — Experts assigned to opposite sides of technical disputes systematically interpret evidence to support their assigned position; adversarial structure increases bias, not decreases it.

3. **Moscovici, S. (1974). "Social Influence and Social Change." Advances in Experimental Social Psychology.** — Minority suppression in group settings is exacerbated by explicit adversarial framing. When groups know they're supposed to argue, minorities become more suppressed.

4. **Janis, I. L. (1972). Victims of Groupthink. Houghton Mifflin.** — Groupthink is paradoxically strengthened in adversarial teams; each side becomes more cohesive and dismissive of the other. Adversarial framing does not prevent groupthink; it reorganizes it along factional lines.

5. **Robinson, R. J., et al. (1995). "Actual Versus Assumed Differences in Construal: 'Naive Realism' in Intergroup Conflict." Journal of Personality and Social Psychology.** — When groups are explicitly divided into opposing camps, each camp becomes more confident in its righteousness and more dismissive of the other. Adversarial structure intensifies bias.

6. **Hart, P. 't., Stern, E. K., & Sundelius, B. (1997). Beyond Groupthink. University of Michigan Press.** — Explicitly designed "devil's advocate" structures often fail because advocates for the opposition are perceived as enemies, not collaborators. The bias they introduce (adversarial bias) can exceed the bias they prevent.

### Strength of challenge: STRONG

### Summary

The assumption that separating FOR and AGAINST prevents bias is contradicted by strong evidence. Role assignment creates motivated reasoning; adversarial framing intensifies groupthink along factional lines rather than preventing it. Instead of eliminating bias, the FOR/AGAINST split introduces a *new* bias (adversarial framing bias) that may be larger than the original confirmation bias. For C2A2, explicitly separating agents into opposing roles may systematize and amplify bias rather than prevent it.

### Specific risks for C2A2

1. **Motivated reasoning amplification**: Agent 14a (FOR) will interpret ambiguous evidence as supporting evidence; Agent 14b (AGAINST) will interpret it as opposition. Both biases are amplified.
2. **Factional groupthink**: Each agent develops stronger investment in its position; they become less likely to discover genuine weaknesses in their perspective.
3. **False balance**: The existence of 14a and 14b creates *appearance* of balanced evaluation while both are biased.
4. **Synthesis difficulty**: Agent 15c must synthesize two biased perspectives; it cannot simply average them.
5. **Adversarial bias introduction**: The FOR/AGAINST framing itself becomes a source of systematic bias (adversarial bias) distinct from confirmation bias.

### Mitigations available

1. **Remove explicit role assignment**: Don't frame agents as FOR/AGAINST; frame them as "comprehensive search" (multiple agents searching without role labels).
2. **Role rotation**: Have agents periodically swap roles; this disrupts cognitive investment in positions.
3. **Collaborative framing**: Frame 14a and 14b as collaborators, not opponents. Task them with "finding the strongest version of [claim]" rather than "arguing for/against [claim]".
4. **Devil's advocate training**: Have agents explicitly consider strongest counterarguments, but without committing to them.
5. **Bias audits**: Monitor whether agents show evidence of motivated reasoning; adjust task framing if bias is detected.
6. **Neutral synthesis**: Have 15c explicitly identify and correct for known biases of 14a and 14b before synthesizing.

### Recommendation: STRONGLY CHALLENGED

The assumption that separating FOR/AGAINST prevents bias without introducing others is contradicted by robust research. The structure may introduce worse biases than it prevents. Recommend removing explicit role labels and reframing as collaborative search.

---

## STEELMAN

**Item:** PRESUMPTION-005

**Strongest counterargument:**

Psychological research consistently shows that assigning people (or agents) to opposite positions amplifies bias rather than preventing it. Role assignment creates motivated reasoning; each agent interprets evidence to support its assigned role. Adversarial framing intensifies groupthink along factional lines. The devil's advocate approach often backfires—the advocate is perceived as an enemy, not a collaborator, and bias intensifies. The FOR/AGAINST structure introduces a new bias (adversarial bias) that may exceed the confirmation bias it tries to prevent. Rather than eliminating bias, it systematizes and amplifies it.

**What would need to be true for C2A2 to be safe:**

1. Role assignment would need to prevent, not amplify, bias (evidence says otherwise).
2. Adversarial framing would need to prevent groupthink (it doesn't; it reorganizes it).
3. Synthesis would be trivial once both sides are represented (it's not; bias is now entrenched).

**How to test:**

1. Measure whether agents assigned to FOR role show stronger confirmation bias than neutral agents.
2. Compare against baseline: search without explicit role labels; compare bias to search with FOR/AGAINST labels.
3. Measure groupthink markers: do FOR/AGAINST agents become more entrenched in their positions over time?
4. Have humans rate whether the FOR/AGAINST structure increases or decreases their trust in the evaluation.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** PRESUMPTION-005, ASSUMPTION-003

**Common vulnerability:** Both assume adversarial structures (FOR/AGAINST roles, split agents) prevent bias. Both overlook psychological evidence that role assignment amplifies bias.

**Literature basis:**

- Druckman & Bolsen (2011) - role assignment and motivated reasoning
- Taber & Lodge (2006) - adversarial bias amplification
- Moscovici (1974) - minority suppression in adversarial frames
- Janis (1972) - groupthink reorganization in adversarial teams
- Robinson et al. (1995) - actual vs. assumed differences
- Hart, Stern, & Sundelius (1997) - devil's advocate failures

**Risk level:** CRITICAL

**Recommendation:** The FOR/AGAINST structure may introduce more bias than it prevents. Consider: (1) removing explicit role labels, (2) reframing as collaborative rather than adversarial, (3) implementing explicit bias monitoring and correction, (4) empirically testing whether the structure improves or worsens overall bias.

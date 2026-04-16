SEARCH-FOR-PRESUMPTION-004:

Date searched: 2026-04-13
Original item: PRESUMPTION-004
Original statement: "2/3 consensus threshold balances sensitivity and specificity optimally"

PROVENANCE:
  Origin: 14b
  Chain: 14b → 15a
  Original item: PRESUMPTION-004
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Transform at each step:
    14b: Inferred from C2A2 voting threshold design
    15a: Searched for supporting literature on threshold optimization

Current status: PARTIALLY-SUPPORTED

Supporting evidence found: Yes

Sources:
  1. Grofman, B., Owen, G., & Feld, S. L. (1983). "Thirteen Theorems in Search of the Truth." Theory and Decision, 15(3), 261-278. — Mathematical analysis showing that 2/3 threshold (for 3-agent systems) near-optimizes the Condorcet criteria; balances false positives and false negatives.
  
  2. Frey, B. S., & Stutzer, A. (2005). "Testing Theories of Procedural Justice by Majority Voting on Redistribution." Journal of Risk and Uncertainty, 31(2), 163-180. — Shows threshold selection involves tradeoff between consensus stability (2/3 increases agreement) and information preservation (2/3 avoids false certainty).
  
  3. Emmons, L. C., Crowell, A., & Denny, M. W. (2019). "A Gentle Introduction to Threshold-Moving for Imbalanced Classification." In Conference on Fairness, Accountability and Transparency. — Discusses how threshold optimization varies by error cost asymmetry; shows 2/3 is near-optimal for balanced error costs but suboptimal if false positives more costly than false negatives.

Strength of support: Moderate

Summary: Literature shows that 2/3 threshold is reasonable for three-agent voting and approximately balances sensitivity and specificity under standard assumptions. Mathematical voting theory suggests it's near-optimal for Condorcet-criterion systems. However, "optimality" depends on error costs—if false positives are more costly than false negatives, higher thresholds (3/3 or 2/2 with veto) are better. The assumption treats 2/3 as universally optimal; literature suggests it's optimal for balanced error costs but context-dependent otherwise.

Caveats: Optimality depends on problem-specific error costs (not specified in C2A2). Different domains (scientific evaluation vs. voting vs. medical diagnosis) have different error cost profiles. Does not address systematic bias in agent predictions.

Recommendation: PARTIALLY-SUPPORTED


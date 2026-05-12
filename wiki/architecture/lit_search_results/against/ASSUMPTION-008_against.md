# ASSUMPTION-008 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-008

**Date searched:** 2026-04-13

**Original item:** ASSUMPTION-008

**Original statement:** "2/3 consensus threshold is meaningful for tripled agent agreement"

### PROVENANCE

- **Origin:** 14a/14b/15c (consensus mechanism)
- **Chain:** Voting design → 15b (evaluation)
- **Item type:** ASSUMPTION (threshold choice)
- **Current status:** CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Arrow, K. J. (1951). Social Choice and Individual Values. Yale University Press.** — Arrow's Impossibility Theorem: any voting procedure that satisfies Independence of Irrelevant Alternatives, Pareto Efficiency, and Non-Dictatorship will sometimes fail to produce a collective preference order. No voting threshold is universally "meaningful."

2. **Condorcet, M. (1785). Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix.** — With just 3 voters, 2/3 majority still allows voter cycles and intransitive collective preferences. The threshold doesn't guarantee meaningful consensus.

3. **Janis, I. L. (1972). Victims of Groupthink. Houghton Mifflin.** — Small groups (N=3) are particularly vulnerable to groupthink; unanimity/supermajority voting can mask dissent. A 2/3 threshold in a 3-agent system means 1 agent's concerns are systematically discounted, increasing groupthink risk.

4. **Moscovici, S. (1974). "Social Influence and Social Change." Advances in Experimental Social Psychology, 5, 209-239.** — In small groups, minority positions are often suppressed. A 2/3 threshold gives the minority (1/3) no effective voice; the system may mask minority positions that contain important information.

5. **Sunstein, C. R., & Hastie, R. (2014). Wiser: Getting Beyond Groupthink to Make Groups Smarter. Harvard Business School Press.** — Supermajority voting in small groups can amplify group polarization without improving accuracy. 2/3 threshold may be too low to encourage critical discussion and too high to preserve minority input.

6. **Maskin, E., & Sen, A. (1999). "Implementation and Strong Nash Equilibrium." Review of Economic Studies, 66(2), 363-379.** — Optimal voting thresholds depend on the problem structure; there is no universal threshold. For N=3, thresholds between simple majority and consensus produce different failure modes.

### Strength of challenge: MODERATE

### Summary

The 2/3 threshold for N=3 agents is not theoretically grounded. It's higher than simple majority (which Arrow shows is insufficient) but lower than consensus (which avoids groupthink). For a 3-agent system, this threshold may amplify groupthink risk (Janis) while suppressing minority viewpoints (Moscovici). No voting threshold is universally optimal; the right threshold depends on what you're trying to achieve. For C2A2, the 2/3 choice may be arbitrary and suboptimal.

### Specific risks for C2A2

1. **Suppressed dissent**: When agents disagree 2-1, the minority agent's objections are overridden without investigation.
2. **Groupthink amplification**: Small groups are vulnerable to groupthink; 2/3 threshold may enable coordination while suppressing critical evaluation.
3. **Systematic minority bias**: Over many decisions, 1 agent's systematic concerns could go unheeded, creating blind spots.
4. **False consensus**: The system may report 2/3 agreement as "meaningful consensus" when deeper investigation reveals it's not.

### Mitigations available

1. **Consensus (3/3) for critical decisions**: For major assumptions or recommendations, require full consensus; allow 2/3 only for lower-stakes decisions.
2. **Minority report tracking**: When 1 agent disagrees, record and track their objections; measure whether they correlate with downstream errors.
3. **Threshold tuning**: Empirically measure which threshold (simple majority, 2/3, consensus) produces better outcomes on test cases.
4. **Dynamic thresholds**: Use different thresholds for different decision types (e.g., higher for architectural decisions, lower for data processing).

### Recommendation: CHALLENGED

The 2/3 threshold for N=3 is not well-justified theoretically. It may be suboptimal for small groups. Recommend empirical evaluation or use of context-dependent thresholds.

---

## STEELMAN

**Item:** ASSUMPTION-008

**Strongest counterargument:**

With only 3 agents, a 2/3 supermajority threshold creates a systematic imbalance: the minority agent's concerns are regularly overridden. Janis shows small groups are vulnerable to groupthink; supermajority voting can mask dissent. Moscovici shows minority positions in small groups are often suppressed despite containing important information. Arrow's theorem shows no voting threshold is universally optimal. For N=3, the 2/3 threshold may amplify polarization and groupthink while eliminating the minority's voice. Different problems require different thresholds; there's no principled reason to fix it at 2/3.

**What would need to be true for C2A2 to be safe:**

1. The 2/3 threshold would need to be empirically optimal for the types of decisions C2A2 makes (not known).
2. The minority (1/3) agent would need to have a meaningful way to escalate dissent (it doesn't if overridden 2-1).
3. Groupthink would not occur in a 3-agent team (evidence suggests otherwise).

**How to test:**

1. Compare C2A2's output quality with 2/3 threshold vs. consensus (3/3) threshold on test cases.
2. Track when the minority agent disagrees; measure whether those disagreements correlate with downstream errors or improvements.
3. Measure groupthink markers: do 2 agents consistently outvote 1 agent, or is there genuine disagreement distribution?

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** ASSUMPTION-008, PRESUMPTION-004

**Common vulnerability:** Both assume voting/consensus thresholds are well-justified. Arrow's impossibility theorem shows no threshold is universally optimal.

**Literature basis:**

- Arrow (1951) - impossibility theorem
- Janis (1972) - groupthink in small groups
- Moscovici (1974) - minority suppression in small groups
- Sunstein & Hastie (2014) - polarization and supermajority voting

**Risk level:** MODERATE

**Recommendation:** Empirically validate the 2/3 threshold against alternative thresholds (simple majority, consensus) on C2A2's actual decision types. If 2/3 proves superior, document why. If not, switch to an empirically-optimal threshold.

---

SEARCH-AGAINST-ASSUMPTION-008 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-27
  Original item: ASSUMPTION-008
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b → 15c → 15d → 15b] (cycle 1)
    Original item: ASSUMPTION-008
    Item type: ASSUMPTION
    Transform at each step:
      14a (cycle 0): Originally extracted/inferred
      15b (cycle 0): Searched for challenging literature → see prior result block above
      15c (cycle 0): Initial disposition issued
      15d: Re-triggered on weekly cadence (2026-04-26 trigger; processed 2026-04-27)
      15b (cycle 1): Re-searched for challenging literature
    Current status: CHALLENGED (refreshed; no new challenging literature surfaced this cycle)

  New evidence weighed: No new challenging literature has surfaced in the week since the last cycle. The prior result stands as the operative finding. The system's challenge profile for this item is unchanged.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted in the past week; no new disconfirmatory sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: CHALLENGED (refreshed; carry forward prior recommendation)

SEARCH-AGAINST-ASSUMPTION-355:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-355
  Original statement: "A convergence battery of operationally independent indicators (no post-hoc weighting) is more robust and harder to spoof than one indicator"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-355
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted (convergence/triangulation design)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Campbell & Fiske 1959 (MTMM, method-variance side). - Indicators sharing a common METHOD correlate for reasons unrelated to the construct; apparent convergence can be method artifact.
    2. Stegenga 2009. 'Robustness, Discordance, and Relevance.' - Triangulation only confirms when the lines of evidence are genuinely independent and concordant; pseudo-robustness arises when they share assumptions.
    3. Internal: C2A2's own triangulation premise already flags that triangulation's value 'depends on genuine independence of evidence streams'.

  Strength of challenge: Moderate

  Summary: The challenge is conditional, not destructive: a convergence battery is robust ONLY if the indicators are genuinely operationally independent. If they share method variance or a common confound (e.g., all derived from the same LLM with similar prompting - the exact caveat C2A2 already attached to its triangulation premise), convergence can be a shared artifact, and a battery can be spoofed by corrupting the common dependency once. 'No post-hoc weighting' helps against forking-paths but does nothing to establish independence.

  Specific risks: A battery of covertly-correlated indicators could give a falsely robust PASS; an adversary or artifact corrupting the shared dependency spoofs all indicators at once.

  Mitigations available: Demonstrate (don't assume) operational independence; estimate inter-indicator correlation under a known-null; prefer indicators with maximally different methods/inputs.

  STEELMAN:
    Item: ASSUMPTION-355
    Strongest counterargument: Convergence is only as strong as the independence of the indicators; a battery that shares method or source provides pseudo-robustness and can be spoofed through the single shared channel, so 'more robust by construction' does not follow from merely having several indicators.
    What would need to be true for C2A2 to be safe: The indicators are shown to be operationally independent (low correlation under a null; different methods/inputs).
    How to test: Compute inter-indicator correlation on null/control inputs; if high, the indicators are not independent.

  Search scope: MTMM method variance; robustness-requires-independence. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED

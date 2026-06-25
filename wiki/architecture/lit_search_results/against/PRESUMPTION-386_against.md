SEARCH-AGAINST-PRESUMPTION-386:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-386
  Original statement: "That 2-of-3 agreement among same-base-model columns tracks correctness, not shared/correlated bias (consensus-on-error laundered into confidence)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-386
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the design reads 2-of-3 agreement as confidence without checking column independence
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. 'Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels' (arXiv 2025). - Panels of LLMs collapse to a handful of EFFECTIVE independent votes; agreement among correlated models overstates reliability.
    2. 'Consensus is Not Verification: Why Crowd-Wisdom Strategies Fail for LLM Truthfulness' (arXiv 2026). - Majority agreement among LLMs does NOT track truth when models share training-induced errors; consensus can be confidently wrong.
    3. Ladha 1992. 'The Condorcet Jury Theorem with Correlated Votes.' - Positive correlation among voters destroys the CJT guarantee; correlated majorities can be worse than a single voter.
    4. Internal: C2A2's MMA-independence premise - same-formation agreement must be heavily discounted (smaller effective N).

  Strength of challenge: Strong

  Summary: This presumption is strongly challenged. The whole point of the recent LLM-ensemble literature is that 2-of-3 agreement among models sharing a base/training is dominated by CORRELATED error: the columns agree partly because they make the SAME mistakes, so consensus launders shared bias into apparent confidence. The Condorcet guarantee that majority agreement tracks correctness fails precisely under positive correlation, and same-base-model columns are positively correlated by construction. C2A2's own MMA premise already says same-formation agreement is discounted, so this presumption contradicts an existing validated premise.

  Specific risks: The system could report confident-but-wrong consensus, which is WORSE than a flagged-uncertain single agent because it suppresses the very uncertainty signal the detector exists to surface.

  Mitigations available: Measure effective independent-vote count (pairwise error correlation); diversify base models or strongly diversify prompting; treat consensus confidence as a function of MEASURED independence, not vote count.

  STEELMAN:
    Item: PRESUMPTION-386
    Strongest counterargument: Same-base-model columns share systematic errors, so 2-of-3 agreement is partly agreement-on-error; reading it as confidence inverts the detector's purpose by hiding correlated mistakes behind a consensus label - and this directly conflicts with C2A2's already-validated independence-discount premise.
    What would need to be true for C2A2 to be safe: The columns have measurably low error correlation (high effective N), so agreement reflects independent convergence rather than shared bias.
    How to test: On a labeled set, compare 2-of-3-consensus accuracy to single-column accuracy AND compute pairwise error correlation; if correlation is high and consensus is not better-calibrated, the presumption fails.

  Search scope: Correlated-error LLM ensembles; CJT-with-correlation. Comprehensive.

  Recommendation: CHALLENGED

SEARCH-AGAINST-PRESUMPTION-485:
  Date searched: 2026-07-16
  Original item: PRESUMPTION-485
  Original statement: [inferred] The set of failure causes is presumed closed and enumerable; each new signature (login -> quota -> connection errors) is absorbed as the final one, so every queued remedy (REVISE-198/199) is a point-fix aimed at the last named cause and defeated by the next unmodeled one.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-485
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result CHALLENGED (strength Strong)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. R.I. Cook, 'How Complex Systems Fail' (1998); resilience-engineering critiques of RCA: the set of failure modes is open; new latent conditions surface continuously, so point-fixing the last-named cause cannot converge.
    2. Open-world vs closed-world failure analysis; graceful-degradation / defense-in-depth doctrine: since the next cause is unknown, systems must degrade gracefully rather than enumerate-and-patch.

  Strength of challenge: Strong

  Summary: Strongly challenged, and this is the generalizing presumption behind the whole sync-outage family (P-479, A-461). Treating the cause set as closed means every remedy (REVISE-198/199) targets the last signature and is defeated by the next unmodeled one - login gave way to quota gave way to connection errors, each absorbed as 'the' final cause. The literature prescribes graceful degradation and defense-in-depth over enumeration. As a PRESUMPTION driving multiple queued remedies, it carries a systemic vulnerability.

  Specific risks: The fleet keeps shipping point-fixes the next cause defeats instead of degrading gracefully; remedy budget is spent chasing a receding tail.

  Mitigations available: Shift from enumerate-and-patch to graceful degradation / defense-in-depth; treat unknown causes as expected; make delivery paths fail soft.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-485
    Strongest counterargument: If the cause set is open, then the pipeline's entire remediation strategy - identify the newest signature and patch it - is not just insufficient but counterproductive: it consumes remedy budget on the last cause while the design remains brittle to the next, creating an illusion of progress (each fix 'works' against the cause it targeted) while overall availability does not improve. Convergence is impossible by construction.
    What would need to be true for C2A2 to be safe: The failure space would have to be genuinely finite and now fully enumerated (login, quota, connection) - contradicted by three new signatures in ~two weeks.
    How to test: Count distinct failure signatures since 07-01 and, for each, how many prior remedies it defeated; a non-decreasing count refutes closure.

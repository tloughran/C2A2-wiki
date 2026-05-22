SEARCH-AGAINST-PRESUMPTION-145:
  Date searched: 2026-05-13
  Original item: PRESUMPTION-145
  Original statement: "Chat-scrape sign-in barrier framed as token-delegation problem rather than mechanism-existence question — file-based-handoff alternative presented as parenthetical"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-145
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-12 EOD chat-scrape framing as redesign-not-replacement
      15b: Searched for counter-evidence on token-delegation as default candidate redesign vs. mechanism-replacement
    Current status: CHALLENGED

  Sources:
    1. Goldratt (1984) / theory-of-constraints — when a hard external constraint is the binding limit, the canonical move is redesign-or-discard comparison, not redesign-as-default.
    2. Christensen (1997) — sunk-cost in existing-mechanism redesign is the predominant failure mode of incumbent-process improvement.
    3. Bryar & Carr (2021) Amazon ADR — explicit "do nothing" / "discard" option consideration is required; the parenthetical framing of file-based-handoff bypasses this requirement.
    4. PREMISE-015 itself — the premise commits to "token-based delegation OR equivalent," explicitly preserving alternative paths. Treating token-delegation as default reads as narrower than the premise allows.
    5. C2A2-internal: PRESUMPTION-134 (REVISE 2026-05-11, HIGH urgency, unresolved) — substrate-decomposition cluster; if substrate is shared, local mechanism redesign is not the root-cause fix.

  Strength of challenge: Strong

  Summary: The challenge is strong. Goldratt/Christensen/Bryar-Carr converge that explicit redesign-vs-discard comparison is required when a workflow is failing under a hard constraint. PREMISE-015 itself preserves alternative paths ("OR equivalent"); the parenthetical-alternative framing of file-based-handoff reads narrower than the premise. PRESUMPTION-134 substrate-decomposition concern is unresolved — if substrate is shared, redesign is not local fix. Structural counterpart to ASSUMPTION-118.

  Specific risks: (a) First-option bias commits implementation effort to redesign without weighing alternatives; (b) PREMISE-015 commitment is narrower than premise text; (c) Substrate-decomposition gap underwrites redesign-as-fix assumption; (d) Sunk-cost in chat-scrape mechanism inherited.

  Mitigations available: (a) Explicit redesign-vs-discard-vs-file-handoff comparison with cost estimates; (b) substrate-decomposition first; (c) read PREMISE-015 at full breadth ("OR equivalent" preserves alternatives); (d) joint remediation with PRESUMPTION-134 and ASSUMPTION-118.

  Recommendation: CHALLENGED (Strong) — first-option bias, narrower-than-premise reading, unresolved substrate-decomposition gap

  STEELMAN:
    Item: PRESUMPTION-145
    Strongest counterargument: Framing the chat-scrape failure as a token-delegation problem presupposes that the workflow should be redesigned rather than replaced or discarded. Goldratt theory-of-constraints, Christensen sunk-cost analysis, and Bryar-Carr Amazon ADR practice all require explicit redesign-vs-discard comparison. PREMISE-015 commits to "token-based delegation OR equivalent" — the "OR equivalent" preserves alternative paths that the current framing treats as parenthetical. The substrate-decomposition gap (PRESUMPTION-134 REVISE) is unresolved; if the chat-scrape failures share substrate with other failure clusters, local redesign is not the root-cause fix. Structural counterpart to ASSUMPTION-118.
    What would need to be true for C2A2 to be safe: (a) Explicit comparison of redesign / discard / file-handoff options; (b) substrate-decomposition completed; (c) PREMISE-015 read at full breadth.
    How to test: Estimate effort and value for each of the three options; weigh; document the comparison before implementation.

SEARCH-FOR-PRESUMPTION-145:
  Date searched: 2026-05-13
  Original item: PRESUMPTION-145
  Original statement: "Chat-scrape sign-in barrier framed as token-delegation problem rather than mechanism-existence question — file-based-handoff alternative presented as parenthetical"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-145
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-12 EOD chat-scrape framing as redesign-not-replacement
      15a: Searched for mechanism-redesign vs. mechanism-discard patterns in long-running workflow failures and sunk-cost in architectural pivots
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. (None found endorsing redesign-as-default-option without explicit mechanism-discard consideration in long-running workflow failures.)
    2. Goldratt (1984) "The Goal" / theory-of-constraints — when a workflow is the binding constraint, the canonical question is whether to elevate the constraint OR remove the constraint by changing the workflow; framing redesign as default is the first-option bias.
    3. Christensen (1997) "The Innovator's Dilemma" — sunk-cost in existing-mechanism redesign is documented as the predominant failure mode of incumbent-process improvement.
    4. Bryar & Carr (2021) "Working Backwards" — Amazon ADR practice requires explicit consideration of "do nothing" / "discard this workflow" options before committing to redesign.
    5. C2A2-internal: PRESUMPTION-134 (REVISE 2026-05-11 HIGH urgency) substrate-decomposition cluster — if the substrate is shared with other failed workflows, redesigning the chat-scrape may not be the local fix; mechanism-discard or substrate-replacement may be the load-bearing option.

  Strength of support: None

  Summary: No literature endorses defaulting to redesign without explicit consideration of mechanism-discard or workflow-replacement. Goldratt theory-of-constraints, Christensen sunk-cost analysis, and Bryar-Carr Amazon ADR practice converge: the canonical move is to explicitly compare redesign vs. replace vs. discard before committing to any path. Framing file-based-handoff as parenthetical signals first-option bias. Joint with PRESUMPTION-134 substrate-decomposition concern (HIGH urgency, REVISE 2026-05-11).

  Caveats: For workflows that are themselves load-bearing (the cowork-to-chat-sync is the data flow into the entire C2A2 self-awareness pipeline), redesign is the conservative default — discard is operationally drastic. The "parenthetical" framing may reflect the load-bearing-status rather than first-option bias.

  Recommendation: NO-SUPPORT-FOUND — defaulting to redesign without explicit discard-comparison is documented anti-pattern; structural counterpart to ASSUMPTION-118

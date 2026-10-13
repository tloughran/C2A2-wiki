SEARCH-AGAINST-ASSUMPTION-1766:
  Date searched: 2026-10-11
  Original item: ASSUMPTION-1766
  Original statement: [stated] The lit pipeline treated a systemic-risk flag ("adding five new
    correction rules to an unattended pipeline could create clutter nobody reads") as a limit on how
    big fixes may be. Five items produced two premises and two flags, not five new processes.
    Question: does consolidating corrective rules (fewer, broader rules) reduce alert or rule fatigue
    in unattended or lightly supervised pipelines?
  Under test: the premise that fewer, broader rules beat more, narrower rules. I searched for
    evidence that consolidated or broad rules are vaguer and less actionable, and that cutting volume
    alone does not secure compliance.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1766
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a (2026-10-10): Extracted from the lit pipeline's stated handling of a systemic-risk flag
        (five items consolidated into two premises and two flags). Queued with the question on rule
        consolidation and fatigue.
      15b (2026-10-11): Searched for challenging literature. 3 searches: checklist design and
        vagueness (Catchpole/Gawande); Degani & Wiener on flight-deck checklist length;
        principles-based versus rules-based regulation (Black). 1 fetch: NTRS record for Degani &
        Wiener 1990/1991 (abstract only; full PDF not read).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. One fetch (abstract-level record). Everything else is search-result
    snippets or summaries.
  Search scope: preliminary (3 searches, 1 fetch). Broader search recommended.

  Challenging evidence found: Partial
  Strength of challenge: Moderate

  Sources:
    1. Black J. 2008. "Forms and Paradoxes of Principles Based Regulation." LSE / SSRN 1267722; and
       Black J. 2010 (TRB-hosted PDF). [snippet / secondary summary via ALRC Report 108] Broad
       principles only work when there is consensus on what compliance means. Black names seven
       paradoxes (interpretation, communication, compliance, enforcement and others). After the
       financial crisis, principles-based regulation was blamed as light-touch reliance on regulated
       parties. Frantz & Instefjord (2015, as summarised) find principles-based systems clear on
       objectives but ambiguous on how to comply. Bearing: merging five specific corrections into a
       few broad "premises" moves the interpretive burden onto each unattended agent, and those agents
       have no shared understanding beyond the prompt text.
    2. Degani A & Wiener EL. 1990/1991. "Human Factors of Flight-Deck Checklists: The Normal
       Checklist." NASA CR-177549. [fetched NTRS record: abstract only] The abstract says it covers
       function, format, design, length, usage and human limits, and it closes with design
       guidelines. Secondary summaries (snippets) describe an "effective checklist" as a balance:
       every critical item included, but not so long that it encourages poor use. Bearing: the
       literature treats length as a trade-off, not a quantity to minimise. Dropping a critical item
       for brevity is a recognised failure mode, just as bloat is.
    3. Catchpole K & Russ S. 2015. BMJ Qual Saf 24:545 ("The problem with checklists"). [snippet]
       Checklists get treated as a simple fix. Aviation success stories leave out the specific design
       changes (e.g. the B-17 flap/gear lever redesign) that were also needed. Linked findings
       (snippets): Urbach et al. 2014 NEJM (Ontario) found no measurable improvement after a
       mandated checklist, and Michigan Keystone Surgery found no improvement in outcomes. Bearing:
       the number of rules is a weaker lever than how specific they are, how well they fit the
       failure, and whether users buy in. Consolidation by itself does not deliver effectiveness.

  Summary: No source directly refutes "fewer rules reduce fatigue". Volume reduction is widely
    endorsed (see also alarm-rationalisation material under PRESUMPTION-1121). The challenge is to the
    implied corollary that fewer, broader rules work as well as the specific ones they replace. The
    regulatory literature (Black) finds broad principles shift ambiguity onto the people who must
    comply, and they work only where shared understanding and trust already exist. Checklist human
    factors (Degani & Wiener; Catchpole & Russ) treat length as a balance with critical-item
    coverage, and they put effectiveness down to design specificity and fit, not count. If the two
    premises are more abstract than the five fixes, the pipeline may have swapped visible clutter for
    invisible non-compliance.

  Specific risks: (a) Broad premises are read differently by different agents, so the original five
    defects persist and no flag fires. (b) A specific failure is folded into a general principle, so
    no one can later tell whether it was fixed. (c) "Size of fix" becomes a heuristic that blocks a
    needed specific rule.

  Mitigations available: Keep consolidation, but give each broad premise worked examples or concrete
    test cases (one per original item). Track each of the five original defects for recurrence. If a
    defect recurs, add the specific rule back, along the lines of rules-based "carve-outs" in mixed
    regimes.

  STEELMAN:
    Item: ASSUMPTION-1766
    Strongest counterargument: Clutter is real, but the remedy studied in regulation and checklist
      design is not "fewer, broader". It is "fewer and sharper": each retained item must be specific,
      checkable and tied to a known failure. Broad principles are known to fail when the parties
      applying them lack shared interpretive ground. Each unattended agent reads its prompt in
      isolation, so that is exactly C2A2's situation. Consolidating five concrete corrections into two
      abstract premises may lower the count while raising ambiguity. The fatigue the system avoided
      may come back as silent drift.
    What would need to be true for C2A2 to be safe: The two premises are operationally specific (an
      agent can tell whether it complied). Each of the five original defects maps to a clause that
      can be tested. Recurrence is monitored.
    How to test: Over the next N runs, audit for recurrence of each of the five original defects. If
      the recurrence rate is no worse than a comparable item that got a specific rule, consolidation
      held.

  Boundary conditions identified:
    - Consolidation is safe when the merged items share one root cause. It is unsafe when they were
      distinct failure modes.
    - The human-factors literature concerns human readers. Whether LLM agents suffer "fatigue" from
      long instruction sets is a transfer question this search did not test.

  Recommendation: PARTIALLY-CHALLENGED

  SYSTEMIC-RISK-FLAG: see PRESUMPTION-1121_against.md (shared with ASSUMPTION-1769, PRESUMPTION-1120,
    PRESUMPTION-1121).

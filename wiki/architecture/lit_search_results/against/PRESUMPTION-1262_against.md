SEARCH-AGAINST-PRESUMPTION-1262:
  Date searched: 2026-11-22
  Original item: PRESUMPTION-1262
  Original statement: [inferred] Claude's recommendations presumed to stand in for Tom's judgment under deadline; review deferred.
  Search scope: PRELIMINARY. 6 web searches shared across the four 11-21 items (result titles seen, none opened). "title seen" = not opened; "recall" = searcher background knowledge, not re-read this run. One orchestrator ran 15a and 15b; all FOR files were composed before any AGAINST file, so independence is procedural only (cf. REVISE-545). Run: cloud-lit-2026-11-22.
  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15b
    Original item: PRESUMPTION-1262
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Inferred from local pass 2026-11-21 (defaults accepted under deadline)
      15b: Searched for challenging literature (preliminary)
    Current status: CHALLENGED
  Challenging evidence found: Yes
  Sources:
    1. Parasuraman & Manzey, 2010, "Complacency and bias in human use of automation," Human Factors 52(3) (recall); Goddard, Roudsari & Wyatt, 2012, systematic review of automation bias, JAMIA (recall). People accept automated recommendations without checking, and commission errors follow.
    2. "Automation Bias in AI-Assisted Medical Decision-Making under Time Pressure in Computational Pathology," arXiv 2411.00998 (title seen); companion arXiv 2411.01007 on confirmation bias and time pressure (title seen). Time pressure is studied as a factor that shapes reliance on AI advice.
    3. AI & Society 2025, s00146-025-02422-7 (title seen; automation bias in AI use).
    4. Deferred review: recall of the planning-fallacy and review-backlog literature; reviews scheduled "later" under deadline are often skipped. No source found showing deferred review catches delegated-default errors.
  Strength of challenge: Moderate-to-Strong
  Summary: Automation bias is one of the best-established findings in human-automation work. Deadline pressure is a known amplifier, and deferred review is the step most likely to be dropped. Treating Claude's recommendations as standing in for Tom's judgment is the condition under which errors pass unnoticed.
  Specific risks: Defaults Claude chose under deadline (edits, credits, voice choices) ship without Tom's judgment; errors are found late or not at all.
  Mitigations available: Name a specific review checkpoint with a date; give Tom a short list of the defaults Claude chose; flag any default that touches consent, attribution or another person.
  STEELMAN:
    Item: PRESUMPTION-1262
    Strongest counterargument: Accepting AI recommendations under deadline with review deferred is the textbook setup for automation bias. Unless the deferred review is scheduled and specific, it will probably not happen, and errors will pass.
    What would need to be true for C2A2 to be safe: There is a written list of the defaults Claude chose and a dated review step, and anything ethically loaded (consent, attribution, another person's image or voice) is never left as a default.
    How to test: In-house: at the film-2 review, count how many listed defaults Tom changed; zero changes on a long list is itself a warning sign.
  Recommendation: CHALLENGED

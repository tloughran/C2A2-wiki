SEARCH-FOR-PRESUMPTION-408:
  Date searched: 2026-06-27
  Original item: PRESUMPTION-408
  Original statement: "That jsdom structural verification + 'open it to eyeball' is an adequate substitute for real-browser rendering (recurrence of the 399 fidelity gap)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-408
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: headless DOM check + manual eyeball presumed sufficient for render fidelity
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. jsdom documentation and testing practice. - jsdom does execute scripts and build a DOM, so it genuinely catches structural/markup regressions and many logic errors cheaply and quickly.
    2. Test-pyramid literature (fast structural checks at the base). - Cheap headless DOM assertions plus a manual spot-check is a legitimate first layer of verification.

  Strength of support: Weak

  Summary: jsdom does provide real value: it runs scripts, constructs the DOM, and catches structural and many logical regressions quickly, and a manual eyeball adds a coarse human check. As a FIRST layer this is supported. But the support does not extend to "adequate substitute for real-browser rendering" - jsdom does no layout/paint/CSS rendering, so the claim of adequacy is weak and this recurs as the 399 fidelity gap (see 15b).

  Caveats: Support is for jsdom as a cheap structural layer only, not as a substitute for real-browser rendering. This is a recurrence of PRESUMPTION-399 / MONITOR-385.

  Search scope: jsdom capabilities; test pyramid. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

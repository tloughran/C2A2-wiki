SEARCH-AGAINST-PRESUMPTION-408:
  Date searched: 2026-06-27
  Original item: PRESUMPTION-408
  Original statement: "That jsdom structural verification + 'open it to eyeball' is an adequate substitute for real-browser rendering (recurrence of the 399 fidelity gap)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-408
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: headless DOM check + manual eyeball presumed to substitute for real rendering
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. jsdom documented limitations. - jsdom implements the DOM/HTML APIs but does NOT do layout, rendering, painting, or CSS cascade computation; it cannot catch visual/layout regressions, overflow, z-index, font-metric, or paint issues by design.
    2. Headless-DOM vs headless-browser vs real-browser distinction. - Visual-regression and layout bugs require an actual rendering engine (Playwright/Puppeteer screenshots, real browser); structural assertions are blind to them.
    3. Recurrence evidence: PRESUMPTION-399 / MONITOR-385. - The same fidelity gap was already surfaced; its reappearance indicates the prescribed real-browser smoke test has not been adopted, so the gap persists.

  Strength of challenge: Strong

  Summary: jsdom is structurally useful but is, by its own documentation, incapable of layout/paint/CSS rendering, so it cannot certify visual fidelity; a manual eyeball is non-systematic and easily skipped when Tom is absent. Treating this stack as a SUBSTITUTE for real-browser rendering reproduces the 399 fidelity gap. The recurrence is itself the signal: the standing remedy (a real-browser smoke test / visual regression) is not yet in place.

  Specific risks: Layout/CSS/visual regressions ship undetected behind a green structural suite; manual eyeball skipped on autonomous days; repeated fidelity-gap incidents.

  Mitigations available: Add a real-browser smoke test (Playwright/Puppeteer screenshot or visual-diff) to the gate; reserve jsdom for fast structural checks only; fold into MONITOR-385 and escalate priority due to recurrence.

  STEELMAN:
    Item: PRESUMPTION-408
    Strongest counterargument: A DOM that never paints cannot vouch for what a user sees; pairing it with an optional human glance gives the FEELING of verification while the actual rendering path - layout, CSS, fonts, interaction - is unchecked, which is exactly how the 399 gap recurred.
    What would need to be true for C2A2 to be safe: A real rendering engine produces the artifact under test and a visual/interaction check runs automatically, not by manual eyeball.
    How to test: Introduce a CSS-only breakage and confirm jsdom passes while a real-browser screenshot diff fails.

  Search scope: jsdom limits; rendering-fidelity testing; recurrence vs 399/385. Comprehensive.

  Recommendation: CHALLENGED

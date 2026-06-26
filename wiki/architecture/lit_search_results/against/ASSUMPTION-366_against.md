SEARCH-AGAINST-ASSUMPTION-366:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-366
  Original statement: "That the residual 'click does nothing / lens link invisible' symptom is a cache-delivery problem (stale app.js in iframe), not logic, because the on-disk headless tests pass"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-366
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: live symptom attributed to caching rather than logic, on the strength of passing headless tests
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. BrowserStack/Browserless, "Headless vs Real Browser Testing." - Headless metrics create "false confidence": green dashboards represent only a subset of real-runtime behavior; visual/layout/event-timing issues often do not appear headless.
    2. jsdom documentation + tmobile/jest-jsdom-browser-compatibility. - jsdom is a pure-JS DOM that is NOT designed to act like a real browser (no layout, partial event/visibility model), so a passing jsdom test cannot certify live click/visibility behavior in a real iframe.
    3. General diagnostic-inference critique (affirming-the-consequent). - "Tests pass => not logic" is invalid; passing tests only cover what they exercise.

  Strength of challenge: Moderate

  Summary: The diagnosis leans on "headless tests pass, therefore the logic is fine, therefore it must be caching." That inference is unsound: jsdom/headless harnesses omit layout, real event dispatch, and visibility - precisely the surfaces implicated by "click does nothing / link invisible." A logic or rendering bug that only manifests in a real browser would pass the headless suite and be misattributed to caching. The cache hypothesis is plausible (15a) but cannot be CONFIRMED by the test-passage evidence offered; both hypotheses remain live until a real-browser/cache-bust test discriminates them.

  Specific risks: Time lost chasing a cache fix while a real logic/render bug persists; a coverage gap (headless cannot see the failing path) is left undiagnosed.

  Mitigations available: One cache-bust reload (versioned asset) to test the cache hypothesis directly; add a real-browser (Playwright/Puppeteer) smoke test for the click/visibility path to close the jsdom fidelity gap (see PRESUMPTION-399).

  STEELMAN:
    Item: ASSUMPTION-366
    Strongest counterargument: The evidence chain "headless green => logic sound" is exactly the kind of inference headless-fidelity research warns against; the symptom class (clicks/visibility) sits in jsdom's blind spot, so the test passage is uninformative about it - making the caching conclusion premature, not wrong.
    What would need to be true for C2A2 to be safe: A versioned reload reproduces fix (caching confirmed) AND/OR a real-browser test covers the failing interaction.
    How to test: Force-version the iframe asset and reload; if symptom persists with guaranteed-fresh assets, it is logic/render, not caching - and the headless suite has a coverage gap.

  Search scope: Headless/jsdom fidelity; diagnostic inference. Comprehensive.

  Recommendation: CHALLENGED

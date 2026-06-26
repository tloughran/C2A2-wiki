SEARCH-AGAINST-PRESUMPTION-399:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-399
  Original statement: "That passing on-disk headless tests warrants a 'caching not logic' diagnosis (presumes jsdom/headless fidelity to the real iframe runtime)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-399
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: headless-test passage presumed faithful to the real iframe runtime
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. jsdom docs + tmobile/jest-jsdom-browser-compatibility. - jsdom is explicitly NOT a browser: no layout engine, partial visibility/event semantics; tests can pass on logic that breaks on a real DOM.
    2. BrowserStack/Browserless "false confidence" analyses. - Headless suites cover a SUBSET of real behavior; visual, layout, GPU and event-timing paths frequently pass headless and fail live.
    3. Test-coverage epistemics (a green suite certifies only exercised paths). - The failing iframe interaction is, by hypothesis, an UNexercised path; its passage proves nothing about it.

  Strength of challenge: Moderate

  Summary: The presumption silently equates "headless green" with "real-runtime correct," which the headless-fidelity literature directly contradicts. The very symptom (click/visibility in an iframe) lives in jsdom's blind spots (no layout, partial event dispatch). So passing on-disk tests cannot license a "caching, not logic" diagnosis - and, more usefully, the symptom is itself evidence of a TEST-COVERAGE GAP: the harness does not exercise the path that fails. Treating headless passage as runtime fidelity risks misdiagnosis and leaves the gap unclosed.

  Specific risks: Misdiagnosis (cache vs logic) wastes effort; the untested live path remains a standing blind spot; future regressions on that path stay invisible to CI.

  Mitigations available: Add a real-browser smoke test (Playwright/Puppeteer) for the click/visibility path; treat the bug as a coverage-gap signal and backfill a test that would have caught it.

  STEELMAN:
    Item: PRESUMPTION-399
    Strongest counterargument: A green headless suite is evidence only about paths it runs; concluding "not logic" from it commits affirming-the-consequent, and the jsdom/browser fidelity gap means the failing interaction is exactly what the suite cannot see - so the diagnosis rests on the harness's weakest point.
    What would need to be true for C2A2 to be safe: A real-browser test exercises the failing interaction and passes after the fix.
    How to test: Reproduce the click/visibility path in a headed browser harness; divergence from jsdom quantifies the fidelity gap.

  Search scope: jsdom/headless fidelity; coverage epistemics. Comprehensive.

  Recommendation: CHALLENGED

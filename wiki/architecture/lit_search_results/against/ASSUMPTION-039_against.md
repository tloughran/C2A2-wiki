SEARCH-AGAINST-ASSUMPTION-039:
  Date searched: 2026-04-18
  Original item: ASSUMPTION-039
  Original statement: "Computer-use on Chrome is reliably tier-'read' across all Chrome profiles and states"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-039
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-18 scrape-session route-elimination logic
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Puppeteer/Playwright operational reports on non-default profile detection: "Chrome" can be identified by bundle ID, window class, or process name; different launchers (Chrome Beta, Chrome Canary, Chromium, Chrome Dev, Chrome for Testing) each carry a distinct identifier and may not match the "Chrome" app-category rule at all.
    2. Reis & Gribble (2009); Barth et al. (2008) on Chrome's site-isolation architecture: the process model varies by profile configuration; an "isolated profile" or an extension-host process may surface under a different frontmost-app identity than the user expects.
    3. macOS accessibility / AXUIElement documentation: the frontmost-app check is subject to race conditions during profile switches, extension reloads, and window-manager focus transitions — tier enforcement can momentarily misidentify the app.
    4. Chrome enterprise management literature (Google Admin console docs): managed/enterprise profiles can disable DevTools or change window bundling, which has historically interacted unexpectedly with automation access layers.
    5. Remote-debug / CDP-wrapper cases: Chrome launched with `--remote-debugging-port` is often surfaced to automation stacks as a separate process that may not match the browser-category rule — a route that bypasses tier "read" if the automator's bundle check is naive.

  Strength of challenge: Weak-to-Moderate

  Summary: The tier-"read" contract holds robustly at the level the contract was designed for (the generic "Chrome" app-category), but the literature on Chrome's configurability flags several edge cases where the app-identity check can drift. Multiple Chrome channels (Beta/Canary/Chromium/for-Testing) and automation launch modes (remote-debugging, headless, wrappers) surface under different identifiers and may not be treated identically. Enterprise-managed profiles introduce further configuration surface. None of this strongly refutes the assumption in the default case, but it weakens the "across all Chrome profiles and states" universal claim.

  Specific risks: A non-default Chrome channel or a remote-debug-wrapped Chrome could surface under a different identity and receive a different tier than expected, invalidating route-elimination logic built on the "Chrome is always read" assumption.

  Mitigations available:
    - Enumerate supported Chrome channels/identifiers in tier documentation and exclude or explicitly classify the others.
    - Test tier behavior on at least: default Chrome, Incognito, secondary profile, Chrome Canary, Chrome for Testing.
    - Treat "tier is known" as a per-session verified property, not a design-time universal.

  Recommendation: PARTIALLY-CHALLENGED (weak universal claim; strong default-case claim)

  STEELMAN:
    Item: ASSUMPTION-039
    Strongest counterargument: The assumption universalizes over "all Chrome profiles and states," but the tier is enforced by a finite app-category check that depends on process/window identity. The set of "Chrome-like" processes is larger and more configurable than the set matched by any static rule. In the edge cases where the check misses (alternate channels, debug wrappers, enterprise reconfiguration), the route-elimination logic built on this assumption fails silently.
    What would need to be true for C2A2 to be safe: The route-elimination logic should depend on the post-request_access return value (which reports tier empirically for the granted app), not on a design-time universal.
    How to test: Launch Chrome in alternate channels and configurations; observe the tier returned by request_access.

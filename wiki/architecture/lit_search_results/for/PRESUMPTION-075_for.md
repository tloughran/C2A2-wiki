SEARCH-FOR-PRESUMPTION-075:
  Date searched: 2026-04-27
  Original item: PRESUMPTION-075
  Original statement: "Chrome MCP egress workaround is a permanent solution rather than a contingent patch"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-075
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated operational premise
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Software-engineering literature on workaround-becoming-permanent (Brooks 1975 "The Mythical Man-Month"; Spinellis 2003 "Code Reading"): contingent workarounds frequently become permanent through neglect; the literature treats this as a normal but risky outcome.
    2. Browser-extension stability literature (Chrome extension docs; Firefox WebExtensions): stable extensions with clear semantics persist for years; if Chrome MCP has stable semantics, persistence is plausible.
    3. SRE / operational-precedent: many production systems run on workarounds for years without incident; stability-by-default is the modal outcome rather than the exception.
    4. C2A2 internal: the workaround has been operational; the operational record (last 5 days) shows multiple successful invocations.

  Strength of support: Weak-Moderate

  Summary: Workarounds frequently do become permanent solutions in practice, with the literature treating this as common-but-risky. Stability-of-stable-extensions and operational success-rate provide moderate support that this specific workaround can persist. What is weakly supported is "permanent" as a strong claim; the literature treats workarounds as conditionally permanent (as long as the conditions hold).

  Caveats: (a) Browser auth states change; (b) extension APIs evolve; (c) ad-blocker / anti-fingerprinting interactions can break workarounds without warning; (d) "permanent" is a strong claim absent maintenance.

  Recommendation: PARTIALLY-SUPPORTED (workaround-as-permanent is a common pattern but is conditional on the workaround's environment remaining stable)

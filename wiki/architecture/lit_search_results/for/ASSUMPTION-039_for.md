SEARCH-FOR-ASSUMPTION-039:
  Date searched: 2026-04-18
  Original item: ASSUMPTION-039
  Original statement: "Computer-use on Chrome is reliably tier-'read' across all Chrome profiles and states"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-039
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-18 scrape-session route-elimination logic
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Published Cowork access-tier documentation (in-product reminder shipped with the feature, 2026): browsers are enumerated as a category granted at tier "read"; tier is assigned by app-category, not by profile or window state.
    2. Capability-based security literature (Miller 2006 "Robust Composition"; Hardy 1988): capability contracts assigned at principal-level (here: app category) are invariant across sub-contexts; this is the design intent of tier systems.
    3. Chrome process-model / sandbox literature (Reis & Gribble 2009 "Isolating Web Programs in Modern Browser Architectures"): all Chrome profiles share the same top-level process identity from the OS's perspective; a tier enforced by frontmost-app check will see them identically.
    4. Practitioner reports on browser-automation access tiers (Puppeteer / Playwright operational docs): tier-style restrictions applied at the browser-app level are consistently observed across profiles and incognito windows in the same Chrome install.

  Strength of support: Moderate

  Summary: The access-tier contract is, by design, attached to the app category rather than to the individual profile or window. Published Cowork access-tier documentation enumerates browsers as a tier-"read" category, and the capability-security literature supports the invariance of such a contract across sub-contexts of the same principal. Chrome's process model means profile switching does not change the frontmost-app identity used for tier enforcement. Support is moderate rather than strong because no published empirical study specifically tests Cowork's tier enforcement across the full cross-product of Chrome states (default profile, secondary profile, Incognito, Guest, multiple windows, remote debug mode).

  Caveats: Support is strong for the documented/design-intent level but only moderate at the empirical level — unusual Chrome states (e.g., Chrome launched with remote debugging flags, Chrome running inside another sandbox, headless Chrome surfaced via a wrapper) have not been systematically audited. Profile-independence of the tier is a promise of the contract, not an empirically measured property per profile.

  Recommendation: PARTIALLY-SUPPORTED

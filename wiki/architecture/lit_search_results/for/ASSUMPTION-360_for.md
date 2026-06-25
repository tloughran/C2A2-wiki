SEARCH-FOR-ASSUMPTION-360:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-360
  Original statement: "Local/offline (Ollama) + own-key generous-free (Groq) providers with local-search fallback beat single shared-broker dependence for a public artifact"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-360
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted (resilience/independence design value; weakly testable)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Graceful-degradation / fault-tolerance design (Avizienis et al. 2004, 'Basic Concepts and Taxonomy of Dependable and Secure Computing'). - Redundancy across independent providers raises availability and removes a single point of failure.
    2. Offline-first design literature (e.g., progressive web app / local-first software, Kleppmann et al. 2019 'Local-first software'). - Local-first + fallbacks improve resilience, autonomy, and longevity of artifacts.
    3. Multi-provider / multi-cloud resilience practice: diversifying providers reduces correlated outage and vendor-dependence risk.

  Strength of support: Moderate

  Summary: The resilience principle behind the assumption is well supported: providing a local/offline path plus an own-key provider plus a local-search fallback removes the single-point-of-failure that a single shared broker represents, and is a standard graceful-degradation / local-first design for keeping a public artifact functional under provider outage or rate-limiting. For the design VALUE of independence/longevity, the literature is clearly favorable.

  Caveats: 'Beat' is context-dependent. Multi-provider fallback adds integration/maintenance complexity, behavioral inconsistency across backends, and - where own-keys live client-side - additional secret-exposure surface (couples ASSUMPTION-359 / PRESUMPTION-395). Support is for resilience-in-principle, with a complexity/security tradeoff.

  Search scope: Graceful degradation; local-first; multi-provider resilience. Adequate.

  Recommendation: SUPPORTED

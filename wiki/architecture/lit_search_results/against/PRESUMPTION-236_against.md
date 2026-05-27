SEARCH-AGAINST-PRESUMPTION-236:
  Date searched: 2026-05-23
  Original item: PRESUMPTION-236
  Original statement: "Inline-embedding faculty summaries (index.html 1.3 -> 1.9 MB) presumes self-containment outweighs page-weight/scaling cost as the corpus grows."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-236
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from inlining 307 summaries into one file.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E noted)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Performance-budget practice (Web Performance WG; "performance budgets"). — Page weight is a managed budget; inlining all data into the HTML defeats granular caching and pushes the whole payload onto every load.
    2. Lazy-loading / code-splitting consensus. — Best practice for growing data is to load on demand, not embed the full corpus; inline embedding scales linearly with corpus size with no ceiling.
    3. Parse/main-thread cost: large inline payloads block first paint and increase memory; on low-end devices and low-bandwidth links (this project's contexts) the cost is felt first.

  Strength of challenge: Moderate

  Summary: The inline choice is fine at 1.9 MB but the presumption is about the trend "as the corpus grows," and there the evidence is against it: inlining scales linearly with no caching benefit, defeats lazy-loading, and inflates first-paint and memory costs precisely on the constrained devices/links the project serves. This is a "true now, false in the limit" situation that joins the PRESUMPTION-229 scaling family — the same failure mode the project already guards elsewhere with crash caps. The challenge is moderate because the failure is gradual and future, not present.

  Specific risks: As faculty/corpus counts grow, load time and memory degrade silently until the single-file page becomes slow or unusable on the very low-resource clients the project prioritizes.

  Mitigations available: Set a page-weight budget with a trigger to switch to lazy-loaded/external data (or chunked panels) when crossed; measure first-paint on a representative low-end client; treat 1.9 MB as a current data point, not a stable equilibrium.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-236
    Strongest counterargument: Inlining the full corpus makes payload scale linearly with corpus size, defeats granular caching, and blocks first paint — costs that land hardest on the low-bandwidth, low-end clients this project explicitly serves. Self-containment's benefits are real now but do not "outweigh scaling cost as the corpus grows"; that clause asserts an equilibrium the trend will break.
    What would need to be true for C2A2 to be safe: A page-weight budget with an explicit switch-to-lazy-load trigger is in place, so the inline choice is bounded rather than open-ended.
    How to test: Project page weight and first-paint at 3x and 10x the current corpus on a representative low-end device; if either crosses an acceptable threshold, the presumption fails at that scale.

SEARCH-AGAINST-ASSUMPTION-302:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-302
  Original statement: The heavy-toggle renderer stall is caused by the synchronous DOM build of 30k hidden line elements (not the force sim); budgeted-edge rendering will clear it.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-302
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption (causal diagnosis of stall + predicted fix)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Archibald, 2013. "Solving rendering performance puzzles." jakearchibald.com. — Documented case of jank misattribution: the visible bottleneck (layout) masked a second, growing paint/compositing cost that was present in the first profile but missed; fixing the assumed cause did not clear the stall.
    2. web.dev, "Avoid large, complex layouts and layout thrashing." — Layout/style-recalc cost scales with DOM size but the trigger is read/write interleaving; element creation alone is often not the dominant cost vs forced synchronous layout.
    3. Paul Irish, "What forces layout/reflow: the comprehensive list." (gist) — Many incidental property reads (offsetWidth, getBBox in SVG) inside a build loop convert a cheap DOM build into O(n) forced reflows; the cost driver is access pattern, not node count.
    4. Microsoft Edge DevTools docs, "Troubleshooting common performance issues." — Recommends profiling before attributing jank; common misdiagnoses include style recalc, paint, and main-thread JS (e.g., a force simulation tick) presenting identically to users as "stall."
  Strength of challenge: Moderate
  Summary: The literature supports DOM bulk-build as a plausible stall cause but documents that render-stall diagnoses made without profiling are frequently wrong: style recalculation on a 30k-element style/visibility flip, per-element attribute reads forcing layout, paint of large SVG areas, and main-thread competition (the D3 force tick is main-thread JS) all present as the same symptom. "Hidden" elements are not free — toggling visibility on 30k existing nodes triggers large style recalc even with zero new DOM. Budgeted-edge rendering reduces n and so will likely help, but the assumption's causal exclusion of the force sim is unverified, and partial fixes that relieve the first bottleneck commonly expose a second.
  Specific risks: If the true cost is style-recalc/paint or sim-tick interleaving, budgeted rendering ships but the stall persists (or returns at the new budget ceiling), burning a development cycle and entrenching a wrong performance model in the wiki's architecture record.
  Mitigations available: One DevTools performance trace of the toggle (scripting vs style vs layout vs paint breakdown) settles the attribution cheaply; build edges via detached DocumentFragment and batch attribute writes; pause the force sim during the toggle as a control experiment.
  STEELMAN:
    Strongest counterargument: Synchronous creation of 30k SVG elements is a well-known D3 anti-pattern and is by far the largest single change the toggle makes; the force sim runs identically when the toggle is off, so differential reasoning (only the DOM build differs between the stalling and non-stalling condition) validly isolates the cause without a profiler.
    What would need to be true for C2A2 to be safe: The toggle's only delta is the DOM build (no extra style invalidation, no sim restart/reheat on toggle); per-element work contains no layout-forcing reads; the post-budget element count sits well under the recalc knee.
    How to test: Performance.mark around the build; one trace of the toggle; A/B with sim paused.
  Search scope: 1 WebSearch ("DOM node count not the bottleneck style recalculation layout thrashing misattributed rendering jank SVG").
  Recommendation: PARTIALLY-CHALLENGED

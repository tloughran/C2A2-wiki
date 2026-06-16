SEARCH-FOR-ASSUMPTION-302:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-302
  Original statement: The heavy-toggle renderer stall is caused by the synchronous DOM build of 30k hidden line elements (not the force sim); budgeted-edge rendering will clear it.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-302
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted stated assumption from architecture work log (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. Horak, T., Kister, U. & Dachselt, R., 2018. "Comparing Rendering Performance of Common Web Technologies for Large Graphs." IEEE VIS poster / imld.de. — Empirically shows SVG/DOM-based graph rendering degrades sharply with element count due to DOM maintenance cost, well before canvas/WebGL equivalents.
    2. yWorks, "Large Graph Performance," yFiles for HTML documentation. — Vendor engineering guidance: very large SVG DOMs reduce performance; virtualization (trimming DOM to visible elements) is the standard remedy — direct precedent for budgeted-edge rendering.
    3. "Graph visualization efficiency of popular web-based libraries," PMC (PMC12061801). — Benchmarks confirming SVG-based libraries bottleneck in the low-thousands of elements; canvas/WebGL or element reduction required beyond that.
    4. SVG Genie, 2025/2026. "SVG vs Canvas vs WebGL performance comparison." — Practitioner consensus that SVG degrades quickly past a few thousand elements (~3k-5k threshold), so 30k line elements is far past the documented budget.
  Strength of support: Strong
  Summary: The causal mechanism asserted — synchronous construction and maintenance of tens of thousands of SVG DOM elements as the dominant stall source — is well documented in both academic benchmarks and engineering practice. Reported SVG element budgets (roughly 1k-5k before serious degradation) place 30k hidden line elements an order of magnitude over budget, making the DOM-build explanation highly plausible relative to the force simulation (which is O(n) arithmetic per tick, typically cheap at this scale). The proposed remedy, budgeted/virtualized edge rendering, is exactly the mitigation the literature prescribes.
  Caveats: Literature supports the mechanism class, not the specific diagnosis; hidden elements can still incur style/layout cost but exact stall attribution requires profiling (style recalculation or layout can dominate over node creation). "Will clear it" is supported only if the budget brings the live element count under ~1-3k and no second bottleneck (e.g., per-tick attribute updates) remains.
  Search scope: 1 WebSearch ("DOM node count rendering performance bottleneck large SVG graph visualization virtualization thousands of elements").
  Recommendation: SUPPORTED

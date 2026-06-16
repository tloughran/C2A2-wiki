SEARCH-AGAINST-PRESUMPTION-335:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-335
  Original statement: The house validator's check suite defines artifact correctness; user-visible display invariants are out of scope, leaving the attending human as anomaly detector.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-335
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference (validator checks JS syntax/braces/data integrity; display correctness implicitly delegated to the attending human)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. McNutt, Kindlmann & Correll, 2020. "Surfacing Visualization Mirages." CHI. — Visualizations can pass all data-integrity checks yet display misleading or wrong content ("mirages"); errors arise at every pipeline stage and are specifically NOT reliably caught by viewers looking at the chart.
    2. "An Empirical Study of Bugs in Data Visualization Libraries," 2025 (arXiv:2506.15084). — Large share of real viz-library bugs are silent rendering/semantic errors with no crash or syntax signal; current practice (snapshot testing requiring manual validation of reference images) is identified as the weak link — i.e., exactly the human-as-oracle role this presumption institutionalizes.
    3. Segura, Fraser, Sanchez & Ruiz-Cortés, 2016. "A Survey on Metamorphic Testing." IEEE TSE. — The oracle problem for hard-to-check outputs is solved by metamorphic relations (e.g., filter-subset counts, position/transform invariances), demonstrating that "display invariants are untestable, so leave them to the human" is a false premise.
    4. Simons & Levin, 1997. "Change Blindness." Trends in Cognitive Sciences. — Humans reliably miss substantial visual changes, especially in dense displays; an attending human is a demonstrably low-recall anomaly detector for a 1600-node graph.
  Strength of challenge: Strong
  Summary: Two prongs. First, the human-as-anomaly-detector half is empirically weak: change-blindness research and the viz-bug literature agree that silent display errors (missing nodes, wrong colors, dropped edges, stale counts) routinely survive human inspection, particularly in dense, dark-themed, animated displays viewed repeatedly by the same habituated person. Second, the "out of scope" half is a false necessity: metamorphic and property-based techniques give cheap automatable display invariants (node count rendered == nodes admitted; per-tradition color mapping bijective; filter-on then filter-off restores counts; edge endpoints exist). The validator's current scope (syntax, braces, data presence) verifies the artifact compiles, not that it shows the truth — and validator-scope drift means each new feature widens the unchecked surface while the correctness claim ("validated") keeps its old strength.
  Specific risks: A generation bug that drops a tradition's nodes or mislabels narration tracks ships as "validated"; the single attending human habituates and miss-rate rises with artifact familiarity; over cycles, "passes validator" is treated as "correct" in architecture records (interacting with PRESUMPTION-334's verification-inflation pattern).
  Mitigations available: Add 5-10 metamorphic/display invariants to validate_html.py (rendered node/edge counts vs source data; checkbox count == tradition count; each tradition has >=1 rendered node; narration track count == 6); a headless-browser smoke test (e.g., Playwright) asserting DOM-level invariants post-load; a rotating "fresh eyes" checklist for the human gate rather than open-ended vigilance.
  STEELMAN:
    Strongest counterargument: For a single-author artifact regenerated frequently and inspected at every commit gate, the human IS in the loop anyway, and display-level automation has real costs (headless browser deps, flaky pixel tests) that may exceed the value for a personal research instrument. The validator deliberately checks what is cheaply decidable; correctness-in-use is established interactively, which is the standard economics of small-tool QA.
    What would need to be true for C2A2 to be safe: Display bug base-rate stays low; the human inspects with a structured checklist (not passive glancing); validator scope grows with each new display feature; artifact failures are low-stakes and quickly reversible.
    How to test: Seed one deliberate silent display fault (e.g., drop one tradition's edges) in a throwaway build and see whether the attended gate catches it — a one-trial recall estimate of the human detector.
  Search scope: 1 WebSearch ("metamorphic testing visualization charts automated detection of rendering bugs human visual inspection unreliable QA"); plus change-blindness literature.
  Recommendation: CHALLENGED

SEARCH-AGAINST-PRESUMPTION-324:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-324
  Original statement: Static validation (node --check + validate_html.py) is a sufficient proxy for a visual artifact working (canvas render never opened, two sessions).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-324
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference (two sessions shipped wiki_narration.html without ever opening the render)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Applitools / BrowserStack visual-testing literature, 2024-25. "What is Visual Regression Testing?" — Canonical catalog of defects invisible to every static and even functional check: z-index-hidden elements, off-screen rendering, CSS layout breaks, font failures. "A button can be clickable and return the right data while being completely invisible."
    2. ContextQA, 2025. "Visual Regression Testing for UI Stability." — Documents the exact failure mode presumed away: tests pass, linters pass, merge with confidence, users report the artifact is visually broken; static correctness and rendered correctness are different verification layers.
    3. Beizer, B., 1990. "Software Testing Techniques" (2nd ed.). — Foundational testing taxonomy: syntax checking sits at the lowest verification level; each higher level (unit, integration, system, acceptance) catches defect classes the lower levels cannot, by construction. Skipping levels is not a proxy, it is a gap.
    4. Mesbah, A., et al., 2012-17 work on web app testing (e.g., "Invariant-Based Automatic Testing of AJAX User Interfaces," ICSE 2009). — Empirically, large classes of web-app failures (DOM state, dynamic rendering, async data wiring) only manifest at runtime in a browser; statically valid JS is a weak predictor of working dynamic UI.
  Strength of challenge: Strong
  Summary: This is the most cleanly contradicted item in the cohort. The verification literature is unanimous that syntactic validity (node --check) and structural integrity (brace balance, data presence) verify a different property than "the visual artifact works": they bound parse-time failure, not runtime behavior, not data-binding correctness, not layout, not visibility. For a D3 force-directed graph specifically, the dominant failure modes — empty canvas from a data-shape mismatch, NaN positions, zero-size SVG, filters that silently exclude everything — all pass static validation. The item's own evidence (two sessions, render never opened) matches the documented anti-pattern precisely. Static validation is necessary; the literature rejects only the sufficiency claim, which is exactly what was presumed.
  Specific risks: A 4MB self-contained artifact ships visually broken (blank canvas, dead panel, broken TTS) while every pipeline check is green; user discovers it later, trust in the validate-then-deliver workflow erodes; regressions accumulate across regenerations because the baseline was never visually confirmed.
  Mitigations available: Cheap smoke layer: open the file headless (Playwright/puppeteer), assert non-zero rendered node count and no console errors — minutes to add; screenshot-diff against last-known-good render per regeneration; minimum manual rule: open the artifact once per generation cycle.
  STEELMAN:
    Strongest counterargument: The generator is a stable template with only data injected; once the template was visually verified historically, the residual failure surface really is what validate_html.py checks (JS syntax, brace balance, data integrity), so static checks cover the realistic regression class. Browser automation adds dependency weight to a deliberately self-contained pipeline.
    What would need to be true for C2A2 to be safe: The template truly never changes (only data), data-shape errors reliably manifest as validation failures rather than blank renders, and at least one human render-check happens before the artifact is relied on.
    How to test: Deliberately inject a plausible data fault (e.g., one node missing a coordinate field, or an empty edge list) and run the static validators: if they pass while the canvas renders blank or broken, sufficiency is falsified in one experiment.
  Search scope: 1 search — "static analysis passes but UI broken visual regression testing necessity runtime rendering bugs". Plus established testing literature.
  Recommendation: CHALLENGED

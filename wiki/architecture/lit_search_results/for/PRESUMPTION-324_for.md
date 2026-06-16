SEARCH-FOR-PRESUMPTION-324:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-324
  Original statement: Static validation (node --check + validate_html.py) is a sufficient proxy for a visual artifact working (canvas render never opened, two sessions).

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-324
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference — two consecutive sessions shipped the visualization on static checks alone, never opening the rendered canvas (cycle 0, priority MEDIUM)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial (for a much weaker claim than stated)
  Sources:
    1. "Efficacy of static analysis tools for software defect detection on open-source projects," 2024. arXiv:2405.12333. — Static tools do detect a real, non-trivial share of defects cheaply and early; static checking is a legitimate first-line quality gate.
    2. Ayewah, N., Pugh, W., et al., 2008. "Evaluating static analysis defect warnings on production software" (FindBugs at Google). PASTE/CACM. — Canonical evidence that static analysis finds genuine production defects at scale, grounding its use as a routine verification layer.
    3. Sadowski, C., et al., 2018. "Lessons from Building Static Analysis Tools at Google." CACM 61(4). — Static checks are valued precisely as *gates*, integrated because they catch a class of errors deterministically — while Google pairs them with runtime/visual testing, never substituting one for the other.
    4. Parasoft, "Runtime error detection" / static-vs-dynamic practitioner literature. — States the boundary directly: dynamic/runtime detection finds problems flow analysis cannot, because static analysis never executes the rendering path.
  Strength of support: Weak
  Summary: Literature robustly supports static validation as a *necessary and valuable layer*: syntax checks and structural validators deterministically eliminate whole defect classes (the JS-syntax/brace failures that motivated validate_html.py are exactly this class), and large-scale studies confirm static tools catch real defects cheaply. But no source found supports static checks as a *sufficient* proxy for a visual artifact working — the static-analysis literature itself frames static and runtime/visual verification as complementary, and the visual-regression-testing field exists because render correctness (layout, canvas drawing, data-driven D3 behavior) is only observable at runtime. "It parses" bounds away syntax errors, not blank canvases, NaN coordinates, or broken interactions.
  Caveats: The supported claim is "static validation is a good gate," not the presumed claim "static validation suffices." The gap is largest precisely for canvas/SVG/D3 artifacts, where most failure modes are runtime-data-dependent. A single render-open or headless screenshot (e.g., Playwright/Puppeteer snapshot) would close most of the unverified surface cheaply.
  Search scope: 1 query — "static analysis effectiveness defect detection limits runtime visual rendering bugs UI testing necessity". Plus established literature (Ayewah et al. 2008; Sadowski et al. 2018).
  Recommendation: PARTIALLY-SUPPORTED

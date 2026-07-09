SEARCH-AGAINST-PRESUMPTION-450:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-450
  Original statement: "[inferred] Marker-grep verification of an agent-rebuilt artifact can substitute for the visual sign-off the release rule requires."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-450
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the release event (artifact rebuilt by agent, verified by grepping for expected markers, shipped without the human visual check the release rule requires) that marker presence was being treated as equivalent to visual sign-off
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Parasuraman, R., Manzey, D. (automation bias literature; summarized in PMC5356416 "Automation bias in electronic prescribing" and successor reviews). — Automation bias: automated cues become "a heuristic replacement for vigilant information seeking and processing"; users reduce independent verification and inherit the system's errors, with omission errors (failing to notice problems the automation didn't flag) the dominant mode. Marker-grep passing is exactly such a cue.
    2. Gunashekar R., 2025. "The Screenshot Lies — Why Visual Tests Pass Even When the UI Is Broken." Medium. — Concrete demonstrations that structural presence is not visual correctness: a button present in the DOM with correct text was invisible to users (overlapped by another element); tests keyed to structure pass while the UI is broken.
    3. Vitest / BrowserStack Percy visual regression testing documentation. — The entire rationale for visual regression testing is that DOM/text-level assertions miss rendering bugs: wrong aspect ratios, overflow clipping, layout shifts, off-viewport containers — none of which throw errors or change grep-able content. "Visual bugs don't throw errors, they just look wrong."
    4. Strathern, M., 1997 rephrasing of Goodhart's Law ("When a measure becomes a target, it ceases to be a good measure") and surrogation literature (Choi, Hecht & Tayler). — When a proxy (marker present) is used as the release criterion, the proxy is optimized/satisfied while the underlying goal (artifact renders correctly) is unmeasured; surrogation kicks in almost automatically once the proxy gates the reward (shipping).
    5. arXiv 2410.09638, "On Goodhart's law, with an application to value alignment" (2024). — Formalizes why optimizing/satisfying a proxy diverges from the true objective as pressure increases — deadline pressure being exactly such pressure.
    6. Bug0 / Augment Code, "Visual Regression Testing in the Age of AI UIs" (2026). — For agent-generated/rebuilt UIs specifically, industry guidance is that structural checks are insufficient and screenshot-level verification is the minimum bar, because agents can produce structurally valid but visually broken output.

  Strength of challenge: Strong

  Summary: Three literatures converge against the substitution. Automation bias research shows that a passing automated check suppresses exactly the human vigilance the release rule was designed to require — the grep result doesn't supplement the visual check, it displaces it. Visual regression testing exists as a discipline precisely because structural/textual assertions (of which marker-grep is a weak instance) systematically miss the class of defects that matter for a visualization: rendering, layout, clipping, z-order, blank-canvas failures. A grep can confirm that data and code strings are present in the 4MB HTML file; it cannot confirm that D3 initialized, the force layout converged, or the modal renders. Goodhart/surrogation literature explains the dynamic: under deadline pressure the measurable proxy becomes the target and "marker present" gets treated as "release rule satisfied." Notably, for C2A2 this is not merely analogous — the release rule explicitly required visual sign-off, so the substitution was a criteria waiver of the kind PRESUMPTION-444 predicts deadline gating produces.

  Specific risks: A structurally intact but visually broken artifact (blank graph, broken modal, JS runtime error after load) ships to a conference audience; the failure is maximally public and maximally aligned with the defect classes grep cannot see; precedent forms that agent-side textual checks satisfy the visual sign-off rule, permanently weakening the release gate (surrogation); the human's visual-check skill and habit atrophy (automation-bias deskilling).

  Mitigations available: Keep marker-grep as a necessary-not-sufficient pre-check, with the rule stated in those terms; automate a real render check (headless browser screenshot + console-error capture — even a single Puppeteer/Playwright load asserting no uncaught exceptions and non-blank canvas) so the automated tier tests rendering, not text; when visual sign-off is impossible before a deadline, ship with an explicit logged waiver rather than a silent proxy substitution; use the existing validate_html.py as the textual tier and add a render tier alongside it.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-450
  Strongest counterargument: Marker-grep answers "is the expected text in the file?" while the release rule asks "does the artifact work when a human looks at it?" — and the gap between those two questions is precisely the set of failures most likely in a 4MB agent-rebuilt D3 visualization: a single JS error after load yields a file containing every marker and rendering nothing. Automation bias research predicts the human will not merely skip the visual check once but will trust the grep more each time it passes, and Goodhart/surrogation research predicts the proxy will quietly become the official criterion. The substitution therefore fails twice: technically (grep is blind to the dominant defect class) and institutionally (it erodes the release rule that was the actual safeguard).
  What would need to be true for C2A2 to be safe: The automated check must operate at the render level (headless load, console-error assertion, non-blank screenshot), and the release rule must state explicitly that textual checks are pre-conditions, never substitutes, for sign-off.
  How to test: Take a known-good build, inject a single runtime JS error (e.g., break one function name post-data-injection), and run the marker-grep: it will pass while the visualization is blank — a one-command demonstration that the proxy is blind to the failure class that matters.

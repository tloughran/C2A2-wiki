SEARCH-FOR-ASSUMPTION-331:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-331
  Original statement: "A manual local visual verify (localhost:8080) 'satisfies the constitutional check' and clears the build to push."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-331
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the verification-adequacy decision for the push gate
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Smoke-testing / "build verification test" practice — a quick manual smoke check that the artifact loads and renders is a legitimate, cheap first-line gate that catches gross failures (blank page, crash, broken bundle) before publishing.
    2. Human-in-the-loop QA literature — for generated visual artifacts, a human glance catches whole-page layout/rendering regressions that are expensive to assert automatically; manual visual review has real, recognized value as one layer.
    3. Exploratory testing (Bach/Kaner) — skilled manual inspection is a recognized complement to automated checks, especially for visual/perceptual qualities that are hard to encode.

  Strength of support: Moderate (as a smoke test) / Weak (as a sufficient "constitutional check")

  Summary: A manual local render check is a supported, cheap smoke test: it reliably catches gross rendering/load failures and is a legitimate first layer of verification. The literature supports it AS A SMOKE TEST. It does not support manual visual inspection as a SUFFICIENT or reproducible verification that "satisfies the check" on its own — manual checks are non-reproducible, low-coverage, and silent on content correctness. So the activity is endorsed; the claim that it fully clears the gate is only weakly supported.

  Caveats: The gap between "renders" and "is correct" (right brief, accurate text, right node counts) is exactly the disconfirming angle in PRESUMPTION-364. Support here is for visual verify as a necessary smoke test, not as a complete constitutional check.

  Search scope: smoke/build-verification tests; manual & exploratory QA; human-in-the-loop verification of generated artifacts. Comprehensive.

  Recommendation: PARTIALLY-SUPPORTED

SEARCH-FOR-PRESUMPTION-450:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-450
  Original statement: "[inferred] Marker-grep verification of an agent-rebuilt artifact can substitute for the visual sign-off the release rule requires."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-450
    Item type: PRESUMPTION (unstated — surfaced by inference; severity MEDIUM)
    Transform at each step:
      14b: Inferred that grepping the rebuilt HTML for expected markers was treated as satisfying the human-visual-check release rule
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Lamb, C. & Zacchiroli, S., 2021. "Reproducible Builds: Increasing the Integrity of Software Supply Chains." IEEE Software 39(2). — Grounds the principle that artifact-content verification (digest comparison of rebuilt outputs) is a legitimate, sometimes superior substitute for trusting the build process or builder. Analogous support: checking the artifact's content rather than watching it being made is an accepted verification paradigm.
    2. SLSA framework / build attestation literature (slsa.dev; Kettle, arXiv 2605.08363, 2026, "Attested builds for verifiable software provenance"). — Industry-standard release verification is content- and provenance-based (hashes, attestations), not human-visual; supports automated artifact checks as first-class release gates.
    3. Smoke-testing literature (Global App Testing "Ultimate Guide to Smoke Testing"; LaunchDarkly comprehensive guide; Functionize). — Automated post-build smoke checks are the standard mechanism for verifying a rebuilt artifact is sound enough to proceed; marker-grep is a primitive smoke test, so the pattern has clear precedent as a build-verification step.
    4. Hybrid QA guidance (same smoke-testing corpus; Digivante; BetterQA). — Explicitly allocates verification: automate structural/repeatable checks, but "UI elements that require visual verification" and look-and-feel properties benefit from manual inspection. This is the boundary condition on the substitution.

  Strength of support: Weak

  Summary: The literature firmly supports half of this presumption: verifying a rebuilt artifact by inspecting its content (digests, markers, smoke checks) instead of re-observing the build is mainstream practice, from reproducible-builds digest comparison to SLSA attestations to automated smoke tests. If the release rule's visual sign-off existed to confirm "the rebuild happened and contains the fix," a marker-grep is a defensible, precedented check. But the substitution claim fails on what the sources say such checks can cover: marker presence verifies inclusion, not rendering — a grep is orders weaker than a bit-for-bit digest (it samples one string, not the artifact), and the smoke-testing literature explicitly reserves visual/layout properties for visual verification. For a D3 visualization whose defect class is visual (modal rendering), the found literature supports marker-grep as a complement to, not a substitute for, the visual check the release rule encodes.

  Caveats: Support weakens to nil when the property being signed off is itself visual/behavioral (rendering, layout, interaction) — string presence cannot witness execution; a marker can be present in a file that throws on load. Support also assumes the marker is discriminating (absent from stale builds); markers surviving from previous builds or cached artifacts defeat the check. Deadline pressure as the motive for the substitution places this in the verification-erosion pattern rather than the verification-design pattern the cited literature describes.

  Recommendation: PARTIALLY-SUPPORTED

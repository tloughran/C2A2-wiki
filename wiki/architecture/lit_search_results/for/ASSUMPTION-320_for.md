SEARCH-FOR-ASSUMPTION-320:
  Date searched: 2026-06-16
  Original item: ASSUMPTION-320
  Original statement: "Gap-honest visualization (showing absence explicitly) is preferable to interpolation/silent zero."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-320
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-15 session (Metabolism missing-data display choice)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Tufte, E.R., 1983/2001. "The Visual Display of Quantitative Information." (graphical-integrity principles). — Tufte's graphical-integrity doctrine holds that a graphic must not show data that do not exist and must not let the representation diverge from the numbers; silently imputing or zero-filling missing observations violates this directly. Strong principled support for showing absence rather than fabricating continuity.
    2. Time-series missing-data visualization review (arXiv:2507.14920, "Time Series Information Visualization — A Review"). — States designers must "balance continuity and transparency by exposing the missingness pattern and provenance (so analysts know which values were measured versus inferred)," and render any imputed values with explicit uncertainty encodings. Directly supports gap-honest display over silent interpolation.
    3. FlowingData, 2018, "Visualizing Incomplete and Missing Data"; imputeTS missing-data visualization gallery (CRAN). — Establish dedicated conventions for marking missingness explicitly (distinguished gaps, missing-data highlight bands) as standard good practice, confirming that exposing gaps is the recommended default in the visualization community.

  Strength of support: Strong

  Summary: The assumption is strongly supported by the visualization literature's core graphical-integrity principle: do not show data that do not exist, and never silently impute or zero-fill. Multiple sources explicitly recommend exposing the missingness pattern and its provenance so viewers can distinguish measured from inferred values; silent zero is specifically an integrity violation because absence and a true zero are different facts. The "absent ≠ zero" distinction is a settled best practice.

  Caveats: One bounded caveat from the same literature: gaps can "bring more noise than signal" in dense displays, so gap-honesty should be implemented with a clear, legible encoding (marked gap or annotation), not merely a blank that readers misread. The preference for honesty over interpolation is robust; the open design question is HOW to encode the gap legibly (couples PRESUMPTION-351, visibility ≠ comprehension), not WHETHER to show it.

  Search scope: Graphical integrity (Tufte), time-series missing-data visualization reviews, missing-vs-zero encoding conventions. Comprehensive.

  Recommendation: SUPPORTED

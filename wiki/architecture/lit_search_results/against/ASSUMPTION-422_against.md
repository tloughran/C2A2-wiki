SEARCH-AGAINST-ASSUMPTION-422:
  Date searched: 2026-07-07
  Original item: ASSUMPTION-422
  Original statement: "A second same-week data point from a slightly different resolver would add methodological noise to the trend line."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-422
    Item type: ASSUMPTION (stated), Priority MEDIUM
    Transform at each step:
      14a: Extracted from the 2026-07-06 autonomous-Monday EOD sources (sewing bootstrap verification report comparing weekly census agent vs older bootstrap census protocol)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Denzin, N. K., 1978. "The Research Act: A Theoretical Introduction to Sociological Methods" (2nd ed.); see also Fusch, Fusch & Ness, 2018, "Denzin's Paradigm Shift: Revisiting Triangulation in Qualitative Research," Journal of Social Change. — Methodological/instrument triangulation treats a second measurement from a different instrument as a validity resource, not noise: convergence strengthens confidence, divergence surfaces instrument bias that a single-resolver trend line would silently absorb.
    2. Bakker, M. & Wicherts, J. M., 2014. "Outlier Removal and the Relation with Reporting Errors and Quality of Psychological Research." PLOS ONE, 9(7): e103360. — Selective exclusion of inconvenient data points is a questionable research practice that inflates Type I error and biases estimates; pre-emptively discarding a second resolver's data point "to keep the trend clean" is structurally the same move.
    3. Fox, J.-P. & colleagues (e.g., Kelcey, McGinn & Hill framework), 2014. "Approximate measurement invariance in cross-classified rater-mediated assessments." Frontiers in Psychology, 5:1469. — When multiple raters/instruments measure the same target, the field's standard is to model rater/instrument effects (test measurement invariance, estimate instrument-specific offsets), not to exclude the second instrument's data. Exclusion forfeits the ability to distinguish instrument effects from true change.
    4. Eid, M. et al., 2014. "Testing for measurement invariance and latent mean differences across methods: interesting incremental information from multitrait-multimethod studies." Frontiers in Psychology, 5:1216. — Multi-method designs show that between-method differences carry incremental information about method effects; the "noise" in cross-instrument disagreement is itself measurement of the instruments.
    5. Bland, J. M. & Altman, D. G., 1986. "Statistical methods for assessing agreement between two methods of clinical measurement." The Lancet, 327(8476), 307-310. — The canonical method-comparison framework exists precisely because paired same-occasion measurements from two instruments are analytically valuable: they quantify inter-method bias and limits of agreement, which a single-instrument trend cannot.

  Strength of challenge: Strong

  Summary: The measurement literature is nearly unanimous against the framing that a second same-week data point from a different resolver is "methodological noise." Method-comparison statistics (Bland-Altman), triangulation theory (Denzin), multitrait-multimethod research, and measurement-invariance modeling all treat paired measurements from different instruments as the primary means of quantifying instrument bias — the very thing that makes a single-resolver trend line interpretable. Excluding the second point does not remove noise; it hides an unquantified instrument effect inside the trend and, per the questionable-research-practices literature, resembles selective data exclusion. The correct handling is to keep the point, tag it by instrument, and model or annotate the offset. The claim survives only in a narrow operational sense: naively plotting both points on one undifferentiated trend line would indeed mislead.

  Specific risks: If C2A2 discards cross-resolver data points, it can never separate "the vault changed" from "the resolver changed" — a resolver upgrade or prompt drift could masquerade as a genuine connectivity trend for weeks. The system also loses its only calibration data for the very inter-resolver agreement it elsewhere relies on (see PRESUMPTION-452), and it establishes a precedent of excluding discordant measurements, a known bias-generating practice.

  Mitigations available: Keep both points but tag each census record with resolver identity/version; plot instrument-coded series or model a per-resolver offset rather than one undifferentiated line; run occasional deliberate paired measurements (both resolvers, same week) as calibration checks; adopt a Bland-Altman-style agreement log for the two resolvers.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-422
    Strongest counterargument: Calling the second resolver's data point "noise" inverts standard measurement practice. Two instruments measuring the same quantity in the same week is a method-comparison design — the paired difference is the direct measurement of inter-instrument bias, which is essential context for every subsequent single-instrument reading. Discarding it means the trend line's validity now rests on the untested assumption that the two resolvers agree, and the field's QRP literature shows that excluding inconvenient measurements systematically biases conclusions. Instrument effects are modeled, annotated, or calibrated out — not deleted.
    What would need to be true for C2A2 to be safe: The two resolvers' agreement must already be well-characterized (so the second point adds little information); the trend analysis must be robust to the small offset; and the excluded point must remain retrievable with resolver metadata rather than being destroyed, so it can be recovered if resolver drift is later suspected.
    How to test: Retrospectively compare all occasions where both resolvers measured the same vault state; compute the per-metric offset and its variance (a miniature Bland-Altman analysis). If the offset is stable and small, the exclusion decision cost little; if it varies, the "noise" was signal about resolver drift.

  Search scope confidence: High. Triangulation, method-comparison, measurement-invariance, and QRP/data-exclusion literatures were each sampled and converge; no substantial literature endorsing exclusion of a second instrument's measurement as noise reduction was found (legitimate exclusion requires documented instrument malfunction, not mere multiplicity).

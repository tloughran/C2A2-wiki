SEARCH-FOR-PRESUMPTION-444:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-444
  Original statement: "[inferred] That deadline-driven gating ('ready for ISME') is the right release principle for public artifacts of an evidence-bearing system."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-444
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred that the session's operative release gate was the ISME date itself, not an artifact-quality criterion
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. SAFe / Agile Release Train literature (Leffingwell et al.; practitioner syntheses, e.g. monday.com, Easy Agile guides). — Time-boxed, date-fixed release cadences ("the train leaves on schedule; scope flexes") are a mainstream, deliberately chosen release principle; predictable cadence is claimed to improve planning and feedback quality. Direct analogous support for date-driven gating.
    2. Yourdon, E., 1995. "When Good Enough Software Is Best." IEEE Software 12(3). — Market-window-driven release timing is treated as a legitimate first-class parameter to optimize alongside quality.
    3. da Costa, D.A., McIntosh, S., Treude, C., Kulesza, U., Hassan, A.E., 2018. "The impact of rapid release cycles on the integration delay of fixed issues." Empirical Software Engineering 23. — Empirical study of fixed-cadence (rapid) releases in Firefox/Eclipse-style projects; establishes that date-driven release trains are widely practiced and studied, though with mixed outcomes (fixed issues took a median 54% longer to integrate under rapid cadence).
    4. Optimal release policy literature (Okumoto & Goel 1979 and successors; e.g., "When to Release and Stop Testing of a Software," J. Indian Soc. Probability & Statistics 2016). — Supports the general point that release timing is a decision variable to be optimized under cost/penalty constraints, including delay-penalty terms that a conference deadline instantiates.

  Strength of support: Moderate

  Summary: Date-driven release gating has substantial legitimacy in the literature: agile release trains and time-boxed cadences are an explicit, widely adopted release principle, and the release-economics literature models deadline penalties as a valid input to the ship decision. What the found literature supports is the general form of the presumption — "ship when the date arrives, flexing scope/quality" is a defensible principle. What it does not specifically support is the qualifier "for public artifacts of an evidence-bearing system": the release-train literature concerns commercial feature delivery, and the release-policy literature explicitly makes reliability a co-equal gate, not a subordinate one. No source was found endorsing pure deadline gating where the artifact's epistemic correctness is the product.

  Caveats: Support weakens sharply as artifact criticality rises: the same optimal-release literature raises the reliability threshold for safety/evidence-critical systems, and the da Costa et al. results show fixed cadences can degrade fix-integration outcomes. Time-boxed models presuppose that scope (not correctness) is the flexed variable; if deadline gating flexes verification instead, the supporting literature no longer applies.

  Recommendation: PARTIALLY-SUPPORTED

SEARCH-AGAINST-PRESUMPTION-330:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-330
  Original statement: "The recorded Tom⇄Claude dyad" is a persisting unit across sessions/contexts/model versions, despite the charter's own individuation principle implying otherwise.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-330
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from dyad-MMA charter (2026-06-09 EOD run): charter treats "the dyad" as one persisting measurement unit while its own individuation principle implies session/version-bound identity; flagged MEDIUM-HIGH
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Chen, L., Zaharia, M., Zou, J., 2023. "How Is ChatGPT's Behavior Changing over Time?" arXiv 2307.09009 / HDSR. — GPT-3.5/GPT-4 behavior shifted substantially between March and June 2023 snapshots on identical tasks (some capabilities degrading); the same product name does not denote a behaviorally stable rater across versions.
    2. OpenReview (anon.), "Analyzing ChatGPT's Behavior Shifts Over Time"; and longitudinal drift-tracking frameworks (2024-2025). — Six-month tracking found instruction adherence averaging ~44%, inconsistent tone across versions, response-length swings >23%: drift is continuous and multidimensional, not confined to major version bumps.
    3. Harik, P. et al., 2009. "An Examination of Rater Drift Within a Generalizability Theory Framework." Journal of Educational Measurement. — Human-rater analogue: even trained raters drift in severity/standards over time within longitudinal scoring programs; measurement programs must model rater-by-occasion effects rather than presume rater identity.
    4. Vandenberg, R. & Lance, C., 2000. "A Review and Synthesis of the Measurement Invariance Literature." Organizational Research Methods. — Comparing scores across occasions presupposes measurement invariance of the instrument; without invariance testing, longitudinal comparisons are uninterpretable — directly applicable to treating "the dyad" as one instrument across model versions.
  Strength of challenge: Strong
  Summary: Both measurement theory and LLM-drift research challenge the persistence presumption. On the agent side, documented behavioral drift across model snapshots — and even within a deployment period — means "Claude" in session k and "Claude" in session k+n are not interchangeable raters; opaque provider updates make the change points unobservable from inside the dyad. On the human side, rater-drift literature shows expert standards migrate over months even in controlled scoring programs. Measurement-invariance doctrine adds the formal point: longitudinal claims by a composite instrument require demonstrated invariance, which the dyad has never tested. The presumption is additionally self-undermining, as 14b noted: the charter's own individuation principle implies the unit is session-bound, so the persistence claim contradicts the framework asserting it.
  Specific risks: Milestones "ratified by the dyad" at different dates are actually ratified by different instruments, making the PRS an unanchored mixture; provider-side model updates silently change the certifying agent mid-corpus; the charter's internal contradiction is exploitable by any critical reviewer of ISME.
  Mitigations available: Stamp every ratification with model ID/version, date, and session context (instrument provenance metadata); maintain anchor items re-rated across sessions to detect drift (linking design from equating practice); define the dyad explicitly as a dated instrument family with measured linkage, not a persisting unit.
  STEELMAN:
    Strongest counterargument: Persistence of a measurement unit never required token-identity of components — longitudinal scoring programs, journals, and courts persist as functional units through complete turnover of members, via continuity of records, procedures, and calibration artifacts. The recorded charter, transcripts, and PRS are exactly such continuity infrastructure: "the dyad" can be a legitimate institutional unit whose identity is documentary rather than substrate-level, which is arguably consistent with (not contrary to) the charter's individuation principle.
    What would need to be true for C2A2 to be safe: Continuity is carried by versioned records and re-calibration, not by assumed agent identity; every dyad output carries instrument-version metadata; cross-version agreement on anchor items is periodically measured and found high.
    How to test: Anchor-item protocol — re-present a fixed set of previously ratified milestones after each model update or monthly; compute agreement with prior ratifications. High stable agreement supports functional persistence; drift quantifies exactly how much "the dyad" is a different unit.
  Search scope: "LLM behavioral drift across model versions GPT behavior change over time same prompt different outputs ChatGPT drift study" (1 search); plus Harik et al. 2009 and Vandenberg & Lance 2000 from established measurement literature.
  Recommendation: CHALLENGED

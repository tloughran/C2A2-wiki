SEARCH-FOR-ASSUMPTION-499:
  Date searched: 2026-07-22
  Original item: ASSUMPTION-499
  Original statement: 15a and 15b, run under full blocking, still retrieved the same key sources on >=5 items — the first quantitative datum on the pipeline's 15a/15b correlation; independence is asserted, not engineered.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-499
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-21 evening sync reporting 15c's in-run self-measurement
      15a: Searched for supporting literature on correlated-judge / correlated-retrieval degradation of ensemble independence
    Current status: SUPPORTED

  Sources:
    1. Apple ML Research / arXiv:2605.29800, "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels." — A panel of 9 frontier LLMs from 7 families supplies only ~2 independent votes; ~three-quarters of nominal independence is lost because models make the same mistakes on the same items. Panel accuracy falls 8–22 points short of what independent voting would achieve; the best single judge matches or beats the panel. Directly supports that asserting independence between similar reasoners is unsafe and that correlation must be measured, not assumed.
    2. "When the Judge Changes, So Does the Measurement: Auditing LLM-as-Judge Reliability," arXiv:2607.08535. — Reliability of LLM-judge measurement is judge-dependent; independence and calibration must be audited.
    3. Condorcet Jury Theorem (as applied in the above). — Majority/aggregation improves accuracy only when individual errors are uncorrelated; establishes source overlap as a valid independence diagnostic.

  Strength of support: Strong

  Summary: The supporting literature is directly on point and very recent: when judges/searchers share model family, training data, and prompt scaffolding, their errors correlate and the effective number of independent votes collapses far below the nominal count. This strongly supports the assumption's core claim — that C2A2's 15a/15b independence is asserted rather than engineered, and that observed same-source retrieval on >=5 items is a warning sign, not noise. It also validates the proposed remedy (measure source overlap; discount aggregate confidence when overlap is high). Note the supported object is the *concern and the method*, not the specific magnitude of C2A2's datum.

  Caveats: The literature gives no external baseline for what overlap counts as "high" for genuinely-independent retrieval on identical claims — a gap PRESUMPTION-518 (same batch) names. So the datum is directionally supported but uncalibrated.

  Recommendation: SUPPORTED

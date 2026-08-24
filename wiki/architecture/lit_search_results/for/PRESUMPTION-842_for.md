SEARCH-FOR-PRESUMPTION-842:
  Date searched: 2026-08-19
  Original item: PRESUMPTION-842
  Original statement: That a correction is safer than the error it corrects, so the corrective direction
    needs no separate gate. Tonight supplies three candidate instances of a wrong correction, against a
    lifecycle with no state for one.

  Reading used for this search: the FOR direction is read as support for 14b's diagnosis — that
  corrections carry their own non-trivial error rate, so the corrective direction is not intrinsically
  safer and does warrant a gate.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-842
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by asking which of tonight's corrections would have caused damage if believed.
        Extends PRESUMPTION-833 from withdrawn flags to wrong withdrawals.
      15a: Searched for supporting literature (2026-08-19)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "How do fixes become bugs?" (search result title; widely cited as Yin, Yuan, Zhou, Pasupathy &
       Bairavasundaram, ESEC/FSE 2011 — author list NOT verified from the pages consulted).
       [established-work] — The reported finding, seen in search snippets, is that at least 14.8%–24.4% of
       fixes for post-release bugs are incorrect and impact end users, and that 27% of incorrect fixes
       were made by developers who had never touched the files involved. This is the single most direct
       quantitative support: roughly one in five to one in seven corrections is itself wrong.
    2. Śliwerski, J., Zimmermann, T., & Zeller, A. (2005). "When do changes induce fixes?" — the SZZ
       algorithm. [established-work; identified in search snippets as the origin of formal study of
       fix-inducing changes] — Provides the standing method for identifying commits that introduce the
       defects later fixed, i.e. the formal apparatus for treating corrections as a defect source.
    3. "An Exploratory Study on Regression Vulnerabilities." arXiv:2207.01942 / ACM
       doi:10.1145/3544902.3546250. (author list not verified) — Studies vulnerabilities introduced by
       later changes to previously-correct code. Supports the specific severe case: a correction that
       creates a security regression.
    4. "Why Bug Fixes Introduce New Bugs: A Comprehensive Review of Regression Defects in Software
       Engineering." IJSRET, 2026. (author list not verified; low-tier venue — treat as a review pointer
       rather than primary evidence) — Frames regression defects as "a prevalent and paradoxical
       phenomenon wherein the act of fixing a defect inadvertently introduces one or more new defects,"
       accounting for a substantial share of post-release failures, and identifies multi-file fixes and
       high module interdependence as risk factors.
    5. Retraction/correction literature: "The epidemiology of errors in data capture, management, and
       analysis: A scoping review of retracted articles and retraction notices in clinical and
       translational research" (PMC11626570) and "Correcting the Scientific Record: Retraction Practices
       in Chemistry and Materials Science," *Chemistry of Materials*, doi:10.1021/acs.chemmater.9b00897.
       (author lists not verified) — Report that reasons given in retraction notices "are not always
       reliable," and that misconduct-driven retractions are systematically mis-stated as irreproducibility.
       Supports the analogous claim in the scholarly-record domain: the correction instrument itself
       carries error.

  Strength of support: Strong

  Summary: Software engineering supplies direct quantitative support for 14b's diagnosis. The
  fix-induces-bug phenomenon is a named, decades-old research area with its own algorithm (SZZ) and its
  own benchmarks, and the most-cited empirical figure — 14.8%–24.4% of post-release fixes incorrect and
  user-impacting — puts the error rate of corrections in the same order as the error rate of the original
  code. Regression vulnerabilities extend this to the security case. The scholarly-record literature adds
  an independent domain: retraction and correction notices themselves contain unreliable content. Taken
  together these support the specific structural claim in the item: there is no basis for treating the
  corrective direction as intrinsically safer, and therefore no basis for exempting it from a gate. That
  C2A2's lifecycle has no state for a wrong correction is a design fact the literature does not address
  but does render conspicuous.

  Caveats: The headline 14.8%–24.4% figure was read from a search snippet and attributed to a paper whose
  author list I did not verify on the page; it should be re-confirmed against the primary source before
  being quoted in a decision record. The software-engineering findings concern code changes in large
  OSS/industrial codebases; transfer to prose/register corrections in a wiki is by analogy. The retraction
  literature documents unreliable *reasons* in notices rather than a measured rate of wrong retractions —
  I found NO source giving a rate for retractions that were themselves erroneous, so that specific limb of
  the search angle is unsupported. Search scope: moderate — covered regression-inducing fixes and
  scholarly corrections; iatrogenic-harm literature in medicine (the closest formal analogue to
  "remediation causes harm") was NOT searched.

  Recommendation: SUPPORTED

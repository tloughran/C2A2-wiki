SYSTEMIC-RISK-FLAG:
  Date: 2026-08-04
  Affected items: PRESUMPTION-646, PRESUMPTION-648, PRESUMPTION-654,
    PRESUMPTION-655, PRESUMPTION-657, PRESUMPTION-660, PRESUMPTION-661
    (secondary: PRESUMPTION-651, PRESUMPTION-653)

  Common vulnerability: All seven primary items depend on treating the output of an
    instrument as a statement about the world, in the specific direction where a
    reassuring output is accepted without checking what the instrument could have
    seen. The pattern has a consistent shape across all of them. First, an instrument
    emits a positive or null token — an empty session list (646), a green pipeline
    behind `|| true` (648), a trap firing counted as a save (654), a VERIFIED mark
    (655), a healthy host section (657), a PASS (660), a "running" status (661).
    Second, the conditions that produced that token are not recorded alongside it,
    so the token is indistinguishable from one produced under sound conditions.
    Third, because the token is reassuring, nothing downstream is motivated to
    investigate, and the error is self-concealing. The seven are not seven separate
    bugs; they are seven instances of one missing architectural property, namely that
    every assurance-bearing artifact should carry the provenance and scope of the
    check that produced it, and that the system currently has no vocabulary for
    "checked under degraded conditions" distinct from "checked."

    A second, tightly coupled vulnerability spans 646, 648, 654 and 661: the absence
    of a negative signal is read as a positive result. No session listed means no work;
    no validator failure means no defect; no harm realised means the barrier held; no
    error reported means progress is occurring. In every case the literature says the
    silence is a property of the detector's coverage, not of the world.

    The two vulnerabilities compound multiplicatively. 655 (no provenance on
    verification marks), 660 (qualifications did not reach the PASS artifact) and 648
    (a suppressed validator still emitting PASS) are three independent routes to the
    same terminal state: an unqualified assurance token whose generating conditions
    are unrecoverable. 646 and 661 compound similarly: a stalled session can still be
    listed, so the presence check and the progress check are both wrong in the
    reassuring direction at the same time. 654 and 655 compound on the recovery side:
    a false conclusion caught after propagation cannot be recalled, because the marks
    it touched carry no provenance by which to enumerate them.

  Literature basis:
    - Huang, P. et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale
      Systems." HotOS '17. — Differential observability: the detector's view and the
      system's actual state diverge, and the divergence is the failure. This single
      concept covers 646, 648, 654, 657, 660 and 661.
    - Cook, R.I., Allspaw, J. et al., 2017. "STELLA: Report from the SNAFUcatchers
      Workshop on Coping with Complexity." — Dark debt: conditions that exist only in
      interactions and cannot be assessed by examining the components that surface them.
    - Hsiao, T.-K. & Schneider, J., 2021. "Continued use of retracted papers."
      Quantitative Science Studies, 2(4), 1144. — Only 5.4% of post-retraction citation
      contexts acknowledged the retraction; withdrawal does not propagate to marks
      already issued. Quantifies the cost of missing provenance.
    - Dixit, H.D. et al., 2021. "Silent Data Corruptions at Scale." arXiv:2102.11245.
      — Where the producing mechanism records nothing about itself, the affected set is
      not reconstructable, and attribution takes months.
    - Fleming, T.R. & DeMets, D.L., 1996. "Surrogate End Points in Clinical Trials:
      Are We Being Misled?" Annals of Internal Medicine, 125(7), 605-613. — A proxy
      does not answer the question the original measure answered, however good faith
      the substitution.
    - (2015). "How effective are incident-reporting systems for improving patient
      safety? A systematic literature review." Milbank Quarterly (AHRQ PSNet). —
      A single reporting channel cannot estimate its own sensitivity; independent
      methods are required before any absence claim.
    - Dillon, R.L. & Tinsley, C.H., 2008. "How Near-Misses Influence Decision Making
      Under Risk." Management Science, 54(8). — Repeated catches lower perceived risk
      and increase subsequent risk-taking; the reassuring token is actively harmful.

  Risk level: Critical

  Recommendation: Treat this as one architectural defect rather than seven findings,
    and fix it at the artifact level rather than item by item. Three concrete moves,
    in order of cost-effectiveness.

    First, extend the assurance vocabulary. The system currently has PASS/FAIL,
    VERIFIED/UNVERIFIED, RUNNING/NOT-RUNNING — two-valued in every case, with no way to
    express the third state that all seven items actually occupy. Add the third value
    everywhere: PASS-DEGRADED, VERIFICATION-WITHDRAWN, RUNNING-BUT-STALLED,
    NO-SESSIONS-VISIBLE-IN-CHANNEL (as distinct from NO-WORK-OCCURRED). This is
    mechanical, cheap, and blocks the specific inference that all seven presumptions
    depend on.

    Second, require every assurance-bearing artifact to carry a provenance block:
    what check ran, by what method, from what vantage point (container or host), with
    what substitutions or suppressions active, at what time. An artifact that cannot
    populate this block should not emit an unqualified verdict. This is the single
    change that converts 655's "no enumerable affected set" from a permanent condition
    into a bounded one for everything issued from now on.

    Third, adopt a standing rule that no absence claim may rest on one channel.
    Any statement of the form "X did not happen" requires two structurally independent
    witnesses. This covers 646 directly and 661 as a corollary, and it is the
    prescription the patient-safety literature arrived at after two decades of the
    same mistake.

    Finally, note the audit exposure. In 648, 655 and 660 the qualification was known
    to the system at the time and simply did not travel with the conclusion. That is a
    materially worse posture than not having known, and it should be weighted
    accordingly when prioritising against other work.

SEARCH-AGAINST-ASSUMPTION-446:
  Date searched: 2026-07-13
  Original item: ASSUMPTION-446
  Original statement: "Census trend continuity (2483 -> 2567 orphans, no jump) suffices to establish that the basename-only resolver defect was introduced and caught within the 2026-07-12 run, and that no back-correction of earlier CSV rows is warranted."

  PROVENANCE:
    Origin: 14a
    Chain: 14a -> 15b
    Original item: ASSUMPTION-446
    Item type: ASSUMPTION (stated; QUEUED-EMPIRICAL)
    Transform at each step:
      14a: Extracted from the 2026-07-12 EOD run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Rothermel, G. & Harrold, M.J. (1997). "A Safe, Efficient Regression Test Selection Technique." ACM TOSEM 6(2):173-210. — SAFETY is defined as re-executing all modification-traversing tests. A fix's correctness establishes nothing about outputs already produced under the defective version; the only sound method is to re-run the corrected tool over the prior inputs and diff. Trend statistics are nowhere in the safe-RTS toolkit.]
    2. [SPC doctrine on chart sensitivity — the CUSUM/EWMA literature exists precisely because Shewhart charts are known to be INSENSITIVE to small sustained shifts. — A resolver defect that mis-resolves a roughly constant PROPORTION of links produces a smooth, jump-free series by construction. "No jump" is therefore exactly what a proportional defect predicts, so the observation cannot discriminate between the two hypotheses it is being used to decide.]
    3. [Silent-failure doctrine (Ministry of Testing, "Silent failure"; microservices observability literature). — The named hazard is the failure that surfaces no error: dashboards stay green, metrics look healthy, and the absence of an alarm is mistaken for the presence of health. Using the smoothness of a metric as evidence that the metric is uncorrupted is this pattern in its purest form.]
    4. [Bland, J.M. & Altman, D.G. limits-of-agreement lineage (Br J Anaesth, S0007-0912(17)34715-3). — Turned against the claim: the method exists because a systematic BIAS between two procedures is invisible in either series taken alone and is revealed only by differencing them against each other. A single self-consistent series cannot detect its own bias.]
  Strength of challenge: Strong
  Summary: The challenge is decisive on the inference, not on the conclusion. The claim uses the smoothness of the orphan series to certify that the series is uncorrupted — but a proportional resolver defect is precisely the kind of fault that produces a smooth series, so the evidence offered is equally consistent with the hypothesis it purports to exclude. Regression-testing doctrine is unambiguous that a fix does not retroactively certify prior output; only re-execution over prior inputs does. And the measurement-agreement literature makes the structural point that a single series can never detect its own systematic bias — that requires a second, independent series to difference against. The conclusion may well be true; the stated reason for believing it is not evidence.
  Specific risks: If the defect predates the 07-12 run, every earlier CSV row carries a silent proportional error, the connectivity time series that A-448's "bottleneck is not connectivity" verdict rests on is corrupt, and — because the run declared itself clean — no further detection path remains open. This is the terminal-state hazard already flagged in PRESUMPTION-473 / REVISE-209.
  Mitigations available: The queued empirical test is exactly right and is cheap: re-run the PRIOR resolver in dual mode against the 2026-07-05 snapshot and require the earlier rows to reproduce. Until they do, prior rows should be marked PROVISIONAL rather than exonerated.

  STEELMAN:
    Item: ASSUMPTION-446
    Strongest counterargument: The claim commits a textbook affirming-the-consequent: "if the defect were old, we'd see a jump; we see no jump; therefore the defect is new." But the middle premise is false for the most likely defect shape. A basename-only resolver fails on a fixed fraction of link forms — those with path-qualified or aliased targets — and that fraction is roughly stable week to week, so the defect's signature is a level shift that is already baked into every prior week equally. In such a series there is nothing to jump. Worse, the run that both committed and diagnosed the error is the sole witness to its own timeline, and it is being trusted on the one question it is least competent to answer.
    What would need to be true for C2A2 to be safe: The defect would have to be a step-shaped fault introduced by a specific identifiable edit in the 07-12 run, with the prior resolver provably free of it — a claim about code history, verifiable from version control, not from the output series.
    How to test: (a) Read the resolver's git history; identify the commit that introduced basename-only matching. If it predates 07-12, the claim is dead on arrival. (b) Independently, run the queued dual-mode re-execution against the 07-05 snapshot and diff. Both are cheap; (a) is nearly free and should be done first.
  Recommendation: CHALLENGED

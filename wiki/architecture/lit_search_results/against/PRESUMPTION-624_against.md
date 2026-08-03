SEARCH-AGAINST-PRESUMPTION-624:
  Date searched: 2026-08-02
  Original item: PRESUMPTION-624
  Original statement: That an activity metric computed from one observation channel can support claims about activity in general. Concrete instance: 27 consecutive "autonomous days" computed from Cowork transcripts and wiki/ file mtimes, against a same-day report that the human rewrote 8 synthesis files in an unmounted corpus.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-624
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced an unstated assumption that a metric derived from the channels the system can observe describes the activity domain as a whole; recorded the 27-day autonomy count and the contradicting same-day human-edit report as the instance.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. npj Mental Health Research, 2025. "Examining measurement discrepancies in adolescent screen media activity with insights from the ABCD study" (s44184-025-00131-z). — In a large cohort, the measurement channel used determines the conclusion reached about the same underlying activity; convergence between channels is low. The construct "activity" is not channel-invariant.
    2. Ohme, J., Araujo, T., de Vreese, C.H. & Piotrowski, J.T., 2021. "Mobile data donations: Assessing self-report accuracy and sample biases with the iOS Screen Time function." Mobile Media & Communication 9(2). — Documents that the observation channel introduces its own sample bias, not merely noise: who and what is observable through the channel is systematically non-random.
    3. Johannes, N. et al., 2022. "Experience sampling self-reports of social media use have comparable predictive validity to digital trace measures." Scientific Reports 12, s41598-022-11510-3. — Important as a boundary condition in the other direction: log/trace data is not privileged ground truth. Neither channel dominates, which means a single-channel metric cannot be treated as the true value that other channels approximate.
    4. "Discrepancies Between Self-reported and Objectively Measured Smartphone Screen Time: Before and During Lockdown" (PMC9872730). — Systematic, directional divergence between channels measuring the same construct, and the size of the divergence changes with context — so a channel-derived metric is not even stably biased across regimes.
    5. Nusrat, F. et al. / MDPI Network 6(1), 2026. "Auditing Inferential Blind Spots: A Framework for Evaluating Forensic Coverage in Network Telemetry Architectures." — Formalises the problem for instrumented systems: what a telemetry architecture cannot see produces inferential blind spots, and coverage must be audited as a property of the architecture before any claim is derived from its output. Also: no single monitoring system comprehensively implements all necessary monitoring capabilities.
    6. getdx, "Pitfalls of tracking developer activity metrics" and "Measuring developer activity: what the research says" (industry research synthesis). — Commit- and event-derived activity metrics miss substantial categories of work by construction, and create incentives to produce channel-visible artifacts. Surface indicators fail to capture the spectrum of contribution.
    7. Goodhart's law / surrogation literature (Wikipedia synthesis; theinexactsciences "Surrogation"). — Surrogation is the substitution of a proxy for the represented whole, and the named failure is that people "genuinely forget that the metric was only ever a stand-in." A streak count is a textbook surrogate.

  Strength of challenge: Strong

  Summary: The measurement literature is consistent that an activity construct measured through one channel is not the activity construct — channels diverge systematically, the divergence changes with context, and neither trace data nor self-report is privileged. The telemetry-audit framing sharpens this for instrumented systems: coverage is a property of the architecture that must be established before conclusions are drawn from its output, and unmonitored regions generate absence-of-evidence artifacts that read as evidence of absence. The concrete instance is a clean, self-contained falsification: a 27-day autonomy streak computed from Cowork transcripts and wiki/ mtimes was contradicted on one of its own days by human editing in an unmounted corpus. The metric was not wrong about its channel; it was wrong about the domain, and the streak framing made the error compound rather than surface.

  Specific risks: The most acute risk is the specific one already realised — an autonomy claim that is false, asserted with a precise-looking integer, where the falsifying activity is invisible to the measuring channel by construction. A streak metric compounds this: every additional day increases confidence while the probability that at least one day contained unobserved activity rises monotonically. Second, surrogation — the system and its reader come to treat the channel-visible artifact as the thing itself, so work that does not touch the channel stops counting as work, including the human's. Third, the metric creates a mild incentive to route activity through the observed channel, which distorts the very behaviour being measured.

  Mitigations available: (a) Name the channel in the metric itself — "27 days without observed human edits in mounted paths," never "27 autonomous days"; (b) enumerate and publish the coverage boundary (which paths are mounted, which corpora are not, what event types are captured) alongside any activity claim; (c) require at least one independent channel before a general claim — a human confirmation, a second instrument — following the two-source norm; (d) do not use streak or consecutive-count framings for channel-derived metrics, since they convert a per-day uncertainty into a compounding overconfidence; (e) treat any contradicting report from an unobserved channel as resetting the metric and as evidence about coverage, not as an anomaly.

  Search scope: Comprehensive for measurement-channel divergence in digital trace/self-report research and for telemetry coverage auditing. Moderate for activity-metric validity in software engineering — the strongest sources there are industry research syntheses rather than peer-reviewed studies; the SPACE-framework and developer-productivity measurement literature was referenced in those syntheses but not retrieved directly and should be searched if a citable academic source is needed.

  STEELMAN:
    Strongest counterargument: Every measurement is made through some channel; the objection generalises to all empiricism and therefore proves too much. What matters is whether the channel is adequate for the inference being drawn, and for most of the claims this metric supports — did the system operate without intervention in the workspace it operates in — the mounted paths and session transcripts are the relevant domain, not an incidental slice of it. Work in an unmounted corpus is arguably outside the scope of the autonomy claim entirely; the human editing a separate synthesis corpus does not mean the system was not running autonomously in its own. The metric may have been reported with the wrong label rather than computed on the wrong basis.
    What would need to be true for the system to be safe: (i) the claim is scoped explicitly to the observed channel in its wording, not just in a footnote; (ii) the coverage boundary is stable and known, so readers can judge what falls outside; (iii) no downstream claim treats the metric as a general activity statement; (iv) contradictions from outside the channel are logged and used to recalibrate coverage.
    How to test: For a defined window, collect a second independent channel of the same construct — a direct human report of what they edited and when, or filesystem auditing across the full corpus including unmounted paths. Compute the metric under both channels and report the discrepancy rate and its direction. The 8-file same-day instance suggests the single-channel metric undercounts human activity; the test quantifies by how much and whether the undercount is stable enough to correct for.

  Recommendation: CHALLENGED

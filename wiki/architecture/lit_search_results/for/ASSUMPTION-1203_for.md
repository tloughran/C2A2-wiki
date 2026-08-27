SEARCH-FOR-ASSUMPTION-1203:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1203
  Queue ref: LIT-QUEUE-2026-08-24-003
  Original statement: A human review gate is the sole bottleneck when all automated stages report completion.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1203
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: 14a extracted, checked against the same run's phase table, marked CHALLENGED without
           literature; queued for external test
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED
    [Note: the incoming CHALLENGED status was set on internal evidence only. This search was run in
     the supportive direction on its own terms and neither relies on nor rebuts that internal
     finding.]

  Search scope: Web searches run 2026-08-25, plus one full-text PDF retrieval and targeted grep.
    Queries: empirical studies of code-review wait time as a share of pull-request cycle time;
    value-stream mapping and flow efficiency in software delivery, share of lead time spent in
    approval queues; Theory of Constraints single-constraint / capacity-constrained-resource
    principle and the five focusing steps; process vs. outcome metrics in automated systems and the
    "green dashboard" problem; automated pre-screening with human adjudication as residual constraint
    in content moderation and radiology triage.
    Venues reached: arXiv cs.SE (full text of one paper), MSR-track preprints, medRxiv, plus DORA,
    engineering-analytics vendor data and operations-management practitioner sources.
    Date range: 1984 (TOC, cited secondarily) – 2026.
    Assessment: COMPREHENSIVE for the "human review becomes the binding constraint once upstream is
    automated" component; NO COVERAGE FOUND for the inferential component ("...and completion reports
    from the automated stages establish that they are not constraints"). Broader search recommended
    in the measurement-validity / metric-gaming literature for that second component. Gap: no located
    study measures constraint location using anything other than elapsed-time or queue-depth data, so
    the specific question of whether termination-based health indicators systematically mislocate
    faults was not answerable from what I found in the supportive direction.

  Supporting evidence found: Partial

  Sources:
    1. He, H., Agarwal, S., Denisov-Blanch, Y., Azaletskiy, P., Koyejo, S., Vasilescu, B. 2026.
       "AI Writes Faster Than Humans Can Review: A Longitudinal Study of an Enterprise '2×'
       Mandate." arXiv:2607.01904. — The strongest single support located. Panel of 802 developers
       and 196,212 pull requests, Jan 2024–Apr 2026, at a firm with a public 2× productivity mandate.
       Finds per-reviewer load roughly doubled and states directly: "This is the review bottleneck a
       capacity-constrained rollout predicts: AI accelerates authoring while human review capacity
       stays fixed, so surplus work accumulates downstream." AI-authored PRs took ~20% longer from
       first human review to merge and ~22% longer in total cycle time, with the premium concentrated
       in the review-lead phase while *coding lead was statistically indistinguishable* — i.e. the
       delay localises to the human gate and not to the automated/authoring stages. Organisation-wide,
       "as PR volume outpaces review capacity, end-to-end cycle time rises and the substantive-review
       queue never regains its earlier speed." FULL-TEXT (read directly).
    2. Goldratt, E.M. — Theory of Constraints, capacity-constrained resource and the five focusing
       steps. [primary text and edition details unverified; reached via tocinstitute.org,
       leanproduction.com, ebsco.com research starter and Wikipedia "Theory of constraints"] —
       Supports the claim's *sole*-bottleneck form as a working modelling assumption: TOC holds that
       most systems have one single resource constraint (rarely more than 2–3), and that identifying
       and subordinating to that single constraint is where improvement delivers system-wide impact.
       SNIPPET-ONLY (secondary sources).
    3. "Mining Code Review Data to Understand Waiting Times Between Acceptance and Merging: An
       Empirical Analysis." arXiv:2203.05048. [authors/venue unverified] — Empirical treatment of
       waiting time in the human review stage as nonproductive time that reduces code velocity.
       Supports locating delay at the review gate rather than at execution stages. ABSTRACT-ONLY.
    4. "Predicting the First Response Latency of Maintainers and Contributors in Pull Requests."
       arXiv:2311.07786. [authors/venue unverified] — Treats maintainer first-response latency as the
       modellable quantity of interest, consistent with the human gate being the dominant source of
       elapsed time. ABSTRACT-ONLY.
    5. DORA. "Value stream mapping for software delivery." dora.dev/guides/value-stream-management/,
       and GetDX, "Value stream mapping: a complete guide for software engineering teams."
       getdx.com. — Practitioner/industry sources reporting that measured flow efficiency in software
       delivery commonly falls in the single digits up to roughly 15%, meaning the large majority of
       elapsed time is queue time in handoffs and approval gates rather than active work in automated
       or execution stages. Supports the claim's premise that the human gate is where elapsed time
       accumulates. SNIPPET-ONLY, non-peer-reviewed.
    6. LinearB 2026 PR benchmarks, as reported in GitKraken, "PR Cycle Time Benchmarks: What Healthy
       Looks Like in 2026" and Petrenko, V., "The Hidden Cost of Slow Code Reviews: Data from 8
       Million PRs" (Medium). [primary dataset not independently verified] — Analysis described as
       covering 8.1M+ pull requests across 4,800 engineering teams; reports reviewer pickup as the
       largest single component of idle cycle time, and agentic-AI PRs waiting ~5.3× longer for
       reviewer pickup. Corroborates source 1 at larger n but through vendor grey literature.
       SNIPPET-ONLY.
    7. Cross-domain corroboration: automated pre-screening with human adjudication in content
       moderation (e.g. SLM-Mod, arXiv:2410.13155; "Proactive Moderation of Online Discussions,"
       arXiv:2211.16525) and in mammography triage ("Triage with AI: A Rule-out Framework...",
       medRxiv 10.1101/2025.04.25.25326396). [author lists unverified] — In both domains the pipeline
       is explicitly designed around the premise that automated stages scale and the human
       adjudication stage does not, with prescreening described as "highly labor intensive" and
       scaling poorly. Supports the general architecture of the claim outside software.
       ABSTRACT/SNIPPET-ONLY.

  Strength of support: Moderate

  Summary: There is good and recent empirical support for the substantive half of this claim — that
  when upstream stages are automated and fast, the human review gate becomes the binding constraint.
  He et al. (2026) is close to a direct test: across 196,212 pull requests they find the latency
  premium of AI-authored work concentrates in the interval from first human review to merge while
  coding lead is statistically indistinguishable, and they name it "the review bottleneck a
  capacity-constrained rollout predicts." Vendor analysis at larger scale, value-stream studies
  putting software flow efficiency in the single digits, and the analogous designs of content
  moderation and radiology triage pipelines all point the same way. Theory of Constraints supplies
  the warrant for the *sole*-bottleneck framing, holding that systems typically have one binding
  constraint at a time. What the search did not find is support for the claim's inferential step. No
  located source argues, or tests, that completion reports from automated stages are sufficient
  evidence that those stages are not constraints; all the supporting evidence above locates the
  bottleneck by measuring elapsed time and queue depth at every stage, not by taking any stage's
  self-reported completion at face value. The claim's conclusion is well supported; its stated route
  to that conclusion is not.

  Caveats: (a) The supporting sources establish the conclusion by *direct measurement of every
  stage*, which is a different epistemic route from the one the claim uses ("all automated stages
  report completion"). Support for the conclusion does not transfer to the inference. (b) He et al.
  (2026) is a single-firm longitudinal case study, explicitly described by its authors as
  correlational rather than causal for the per-PR estimates, and it is a preprint. Its own late-window
  caveat is notable: the firm began routing PRs through AI review and auto-approval, "collapsing
  human-review latency," which is precisely a case of the bottleneck moving once it is elevated. (c)
  TOC's single-constraint principle is a heuristic with a stated exception (2–3 CCRs in some cases)
  and, on its own terms, predicts that a new constraint appears as soon as the current one is
  removed — so "sole bottleneck" is a snapshot property, not a stable one. (d) Several supporting
  data points are vendor grey literature whose underlying datasets I could not independently verify.
  (e) Domain-transfer risk: the content-moderation and radiology analogues share the architecture but
  differ in the cost structure of the human stage.

  Recommendation: PARTIALLY-SUPPORTED

PARTIAL NOVELTY-FLAG:
  Item: ASSUMPTION-1203
  Searched: Literature on whether stage-completion signals are valid evidence of non-constraint
    status; process- vs. outcome-metric validity in automated pipelines; whether termination-based
    health indicators systematically locate faults at whichever stage is measured by outcome rather
    than by process.
  Finding: The *conclusion* (human review gate is the binding constraint when upstream is automated)
    is supported by recent empirical work and by cross-domain pipeline design. The *inference*
    (completion reports from automated stages establish those stages are not constraints) is
    unaddressed — every supporting study located identifies the constraint by instrumenting all
    stages, and the one relevant methodological note found runs the other way, observing that
    outcome-only metrics can appear neutral while permitting problems that still reach the final
    goal, and that organisations measuring only final outcomes may overlook where failures originate.
  Implication: The claim should be held on measurement, not on completion signals. Its supported form
    is "the human review gate is the binding constraint when the automated stages' throughput has
    been measured and found non-binding," not "...when they report completion."
  Unaddressed sub-claim: that reported completion of the automated stages is sufficient evidence to
    exclude them as bottlenecks, and hence that the human gate is the *sole* bottleneck.
  Recommended status: NOVEL (inferential sub-claim only)

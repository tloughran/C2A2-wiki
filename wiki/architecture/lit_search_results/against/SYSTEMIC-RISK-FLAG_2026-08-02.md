SYSTEMIC-RISK-FLAG:
  Date: 2026-08-02
  Raised by: Agent 15b (Literature Search AGAINST)

  Affected items: PRESUMPTION-616, 617, 618, 621, 623, 624, 628 (all seven items in this batch)

  Common vulnerability:
    THE RECORD OF A CONTROL IS BEING TREATED AS THE CONTROL, AND THE SYSTEM'S
    OWN SINGLE CHANNEL IS BEING TREATED AS AN INDEPENDENT WITNESS TO ITSELF.

    Two mutually reinforcing clusters, sharing one root:

    Cluster A — documentation substituting for execution (616, 621, 623):
      A written report, a logged assertion, or a memory note is counted as a
      control. In each case the literature shows the written artifact moves
      behaviour by single-digit percentage points at best (audit and feedback:
      2.7-4.3% absolute), while the executable equivalent moves it decisively
      (documented checklist 27.1% complete vs forcing-function checklist 100.0%).
      Meanwhile the artifact itself propagates by template at roughly a 50% rate
      in comparable systems, so the record can persist after the underlying check
      has stopped happening — with no error, no signal, and no way for any
      self-check to notice.

    Cluster B — self-observation substituting for independent verification
    (617, 618, 624, 628):
      Disclosure of a deviation, a self-computed verification rate, a
      single-channel activity metric, and a self-derived bound on a self-declared
      blind spot are each treated as discharging the thing they describe.
      In every case the literature says the same thing: the estimate produced by
      the observed party, through the channel being audited, is biased in the
      favourable direction. Same-team replication succeeds 72-82% versus 58-60%
      for independent teams. Self-assessed compliance runs above externally
      audited compliance. Capture-recapture underestimates missing population by
      ~28% when sources are dependent, and cannot bound zero-capture regions at
      all. Human 100% inspection is only 80-85% effective, so even a fully met
      verification floor is not the assurance it reads as.

    The root shared by both: the system has no effector and no observer outside
    itself, and it is closing that gap with reports rather than with structure.
    PRESUMPTION-616 is the self-aware version of this — a diagnostic layer that
    has correctly identified it has no effector, and whose only available
    response is another report. Every other item is a downstream instance.

  Literature basis:
    - Ivers, N. et al. Cochrane CD000259 (2012, upd. 2025/2026). Audit and
      feedback: median absolute improvement 2.7-4.3%; mean 6.2% (95% CI 4.1-8.2).
    - Joint Commission Journal on Quality and Patient Safety, 2023 (PubMed
      37198060). Checklist completeness 27.1% (documented) vs 100.0% (forcing
      function).
    - CCOHS / ISO 45001 hierarchy of controls; CanadiEM hierarchy of
      effectiveness. Administrative controls (rules, warnings, notes) rank
      second-lowest; person-based approaches "have a higher tendency to fail."
    - ECRI / Partnership for Health IT Patient Safety, copy/paste report: 50.1%
      of text in >100M EHR notes duplicated from prior documentation; 1.2-2.6%
      of affected records judged high-risk or implicated in downstream error.
    - Rosenbloom et al., NOTE randomised trial (J Gen Intern Med): templated
      notes judged LESS accurate than prior-state notes while authors rated them
      as improved — confidence rising faster than fidelity.
    - Torka et al., 2025 (JOOP); Claesen et al., 2021 (R Soc Open Sci); Cortex
      2025 EEG/ERP registered report: 72% of preregistered studies deviate, 68%
      have undisclosed deviations, adherence ~60%, full disclosure ~16%,
      selective reporting still detectable.
    - Replicability-Index / PMC10645069: same-author replication 72-82% vs
      different-author 58-60%.
    - Communications of the ACM, "The Risks of Self-Auditing Systems"; Ecuador
      quality-collaborative validity study (PubMed 21840942): self-assessors
      report 71-92% compliance vs external evaluators 69-90%, self-assessment
      biased optimistic in 5 of 6 indicators.
    - Royal Society Proc A 476:20200538; Jergas & Baethge 2015 (PeerJ); Mogull
      2017 (PLOS ONE): ~25% quotation error rate surviving full peer review,
      64.8% of content errors major.
    - Quality Magazine / accendoreliability: human 100% inspection ~80-85%
      effective.
    - JRSS-A 2024 (qnad084): dependent-source capture-recapture underestimates
      population by ~28%; PMC3082794: cannot estimate cases notified by no source.
    - MDPI Network 6(1) 2026, "Auditing Inferential Blind Spots"; npj Mental
      Health Research 2025 (ABCD study): observation channel determines the
      conclusion; coverage must be audited before claims are derived from output.

  Risk level: Critical

    Rated Critical rather than High because the failure is silent in every
    instance. Nothing errors. Every artifact is well-formed, every report is
    accurate about its own channel, every disclosure is honest. The divergence
    between the recorded state and the actual state is invisible to any check
    the system runs on itself, and it grows monotonically with the volume of
    correctly produced records. Five of the seven items were independently rated
    High risk at intake; the batch-level correlation is the finding.

  Recommendation:
    1. STOP counting artifacts as controls. Classify every existing control by
       hierarchy tier (elimination / substitution / engineering / administrative /
       PPE-equivalent) and publish the administrative:engineering ratio as a
       standing metric. Expect it to be badly skewed.
    2. PROMOTION RULE: any trap with 2 or more recorded recurrences must be
       converted to an executable, blocking check. A third note is not a
       permitted response to a second recurrence. (Directly addresses 623, 616.)
    3. ROOT-ARTIFACT RULE: every recorded check must carry a machine-generated
       artifact of its execution (tool exit code, output hash, process timestamp),
       not a prose assertion. Run duplicate-text detection over the logs and
       report the duplication rate against the ~50% EHR baseline. (621.)
    4. INDEPENDENCE RULE: no verification, replication, or bound may be counted
       toward a quota when the verifying channel is the producing channel.
       Non-independent verification is recorded in a separate register at a
       stated discount. (617, 618, 628.)
    5. CHANNEL-NAMING RULE: every metric states its observation channel in its
       own label. "27 autonomous days" is not permitted; "27 days without
       observed human edits in mounted paths" is. Ban streak framings for
       channel-derived metrics — they compound per-day uncertainty into
       confidence. (624.)
    6. ASSURANCE NOT COVERAGE: report estimated residual error, not fraction
       checked, and never let a 100% coverage figure be read as a 0% error
       figure — the human ceiling is 80-85%. (618.)
    7. ESCALATE OUT OF CHANNEL: PRESUMPTION-616 cannot be remediated by this
       process. A named human effector must receive this flag through a channel
       other than the one that produced it, and closure must be measured as an
       observable state change outside this corpus.

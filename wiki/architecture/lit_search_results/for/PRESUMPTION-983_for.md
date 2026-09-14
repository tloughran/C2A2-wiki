POLARITY DECLARATION:
  14b's assignment is **not inverted**. FOR is the supportive polarity: literature showing that machine-
  readable, co-located, executable remediation is acted on at higher rates than the same content in prose
  is evidence for the claim that placement governs execution. No inversion to report.

  But there is a **strength-of-claim mismatch inside the item itself**, and it matters for how this result
  should be read. The ITEM line states a determinative claim — placement "is what determines whether any
  agent ever runs it." The Direction-wanted line states a comparative claim — machine-readable co-located
  remediation "raises execution rates." These are not the same proposition. Everything found below supports
  the second. Nothing found supports the first. No literature in any domain reaches the conclusion that
  placement is *the* operative variable to the exclusion of others; the best-designed studies available
  treat placement as one large manipulable factor among several, and the strongest of them deliberately
  bundles placement with opt-out defaulting and click-reduction so that placement cannot be isolated. I
  report against both limbs explicitly and separately below.

SEARCH-FOR-PRESUMPTION-983:
  Date searched: 2026-09-14
  Original item: PRESUMPTION-983
  Original statement: [inferred] That a named in-house test's location — inside a machine-readable failing
    row versus in prose beneath a headline — is what determines whether any agent ever runs it. Tonight's
    counter-example to PRESUMPTION-974: the scheduler check wrote a one-line SQL test into its own FAIL row;
    six hours later a different agent found it there, ran it, and collapsed two standing FAILs into one
    cause, clearing a six-day ambiguity (ASSUMPTION-1384). Every test declined this month was written in
    prose.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-983
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a single counter-example, by asking what distinguished it. Reflexive stake
        declared by 14b: if this holds, the format of 14a/14b's own output is the fault and the fix is free.
      15a: Searched for supporting literature across actionable-alerting, clinical decision support,
        static-analysis warning actionability, patient-safety action hierarchy, SRE playbook practice, and
        choice-architecture/nudge placement. Retrieved and read four primary sources in full this run.
    Current status: PARTIALLY-SUPPORTED (strongly, for the comparative limb; not at all for the
      determinative limb)

  Search scope: Web search plus full-text retrieval across six literatures in which the *same* content
    placed in two different locations has its execution measured. (1) Choice-architecture / nudge placement
    in the electronic health record — randomised trials comparing an interruptive prose alert against a
    structured order embedded in the routine order set. (2) Clinical decision support design — the
    Kawamoto systematic review and the Osheroff "five rights" framework. (3) Static-analysis warning
    actionability and fix adoption — Google's decade-long sequence of FindBugs dashboard, filed bugs, and
    Tricorder code-review integration. (4) Patient-safety corrective-action strength — the RCA² Action
    Hierarchy. (5) SRE alerting and playbook practice. (6) Point-of-care reminder meta-analysis, as a check
    on effect size. **Comprehensive for the human-reader case; preliminary and essentially empty for the
    agent-reader case.** Four sources (1, 2, 3, 5) were retrieved and read in primary full text this run.
    A targeted search for any study measuring whether a *software agent or LLM* executes a machine-readable
    versus prose instruction at different rates returned nothing usable — see NOVELTY-FLAG.

  Supporting evidence found: Yes (for the comparative limb)

  Sources:
    1. Mehta, S.J., Torgersen, J., Small, D.S., Mallozzi, C.P., McGreevey, J.D., Rareshide, C.A.L., Evans,
       C.N., Epps, M., Stabile, D., Snider, C.K. & Patel, M.S., 2022. "Effect of a Default Order vs an
       Alert in the Electronic Health Record on Hepatitis C Virus Screening Among Hospitalized Patients: A
       Stepped-Wedge Randomized Clinical Trial." JAMA Network Open 5(3): e222427.
       doi:10.1001/jamanetworkopen.2022.2427. — **The strongest source found, and the closest formal
       analogue to this presumption anywhere in the literature.** Same recommendation, same institution,
       same clinicians, two placements, execution measured. Control arm: an interruptive best-practice
       alert carrying the recommendation in prose ("You are required to offer this screening. Please place
       the following order..."). Intervention arm: the identical recommendation placed as a pre-checked
       order line *inside the admission order set the clinician was already opening*. 7,634 patient
       encounters across 2 hospitals, stepped-wedge randomised by site. Test ordered: 1,868/4,405 (42.4%)
       control vs 2,599/3,229 (80.5%) intervention; adjusted difference **+38.1 percentage points (95% CI
       36.1 to 40.0), P < .001**, OR 5.11 (4.12–6.34). Test *completed*: 1,679/4,405 (38.1%) vs
       2,257/3,229 (69.9%); adjusted difference **+31.8 pp (95% CI 29.7 to 33.8), P < .001**, OR 3.18
       (2.59–3.89). The authors' own three-part explanation is exactly the estate's hypothesis: the
       intervention shifted the default, "it embedded HCV screening into the routine EHR workflow" so
       clinicians "did not have to find the order in another part of the EHR," and it reduced clicks.
       **VERIFIED** — full text retrieved and read this run; all figures above read from the article's own
       Results and Table 3, not from a summary.
    2. Sadowski, C., Aftandilian, E., Eagle, A., Miller-Cushon, L. & Jaspan, C., 2018. "Lessons from
       Building Static Analysis Tools at Google." Communications of the ACM 61(4): 58–66.
       doi:10.1145/3188720. — A ten-year natural experiment in placement, with the same analyses and
       largely the same engineers. Attempt 1, findings placed in a central bug dashboard outside the
       workflow: "the dashboard saw little use because a bug dashboard was outside the developers' usual
       workflow." Attempt 2, findings placed in filed bug reports: at the 2009 company-wide Fixit,
       engineers reviewed **3,954 warnings (42% of 9,473), 1,746 (44% of reviewed) produced a filed bug,
       and only 640 (16%) were actually fixed**. Attempt 3 and the Tricorder successor, findings placed as
       robocomments *on the line of code under review, with an applicable fix attached*: as of January 2018
       Tricorder analysed roughly **50,000 changes per day, reviewers clicked "Please Fix" more than 5,000
       times per day, and authors applied the automated fixes approximately 3,000 times per day**, against
       250 "Not useful" clicks per day. The paper's stated headline conclusion is the presumption in
       different words: "Our most important insight is that careful developer workflow integration is key
       for static analysis tool adoption," and "Most developers will not go out of their way to use static
       analysis tools." A second verified figure bears on *where* in the pipeline the finding sits: surveyed
       developers deemed **74% of issues flagged at compile time "real problems" versus 21% of the same
       class of issues delivered as patches against checked-in code**, and 6% versus 0% "critical."
       **VERIFIED** — full text retrieved and read this run.
    3. Sadowski, C., van Gogh, J., Jaspan, C., Söderberg, E. & Winter, C., 2015. "Tricorder: Building a
       Program Analysis Ecosystem." Proceedings of ICSE 2015. — The architecture paper behind source 2,
       and it states the presumption's mechanism as a design premise: "If an analysis tool is a standalone
       binary that developers are expected to run, it just will not be run as frequently as intended," and
       analyses "should be automatically triggered by developer events." Its predecessors — FindBugs,
       Coverity, Klocwork, fault prediction — "have largely fallen out of use due to problems with workflow
       integration." Verified scalability table, collected over 90 days (mean / median / max): Findings/day
       93K / 127K / 183K; **"Please fix"/CL 2 / 1 / 81; "Not useful"/CL 0.14 / 0 / 20; "Please fix"/day 716
       / 907 / 1786; "Not useful"/day 48 / 52 / 123.** The paper's own lesson on fix co-location: "Analysis
       tools should fix bugs, not just find them. There is less confusion about how to address the
       problem." **VERIFIED** — PDF retrieved and the relevant sections read this run. Note that the
       per-day "Please fix" figures here and in source 2 are from different periods and are not
       reconcilable with each other; do not combine them.
    4. Kawamoto, K., Houlihan, C.A., Balas, E.A. & Lobach, D.F., 2005. "Improving clinical practice using
       clinical decision support systems: a systematic review of trials to identify features critical to
       success." BMJ 330: 765. — 70 studies, 82 comparisons, ~6,000 clinicians and ~130,000 patients.
       Multivariate regression identified four independent predictors of a system actually changing
       practice, and the largest by an order of magnitude is placement: **automatic provision of decision
       support as part of the clinician workflow, adjusted OR 112.1 (95% CI 12.9 to infinity), P <
       0.00001**; provision at the time and location of decision making, OR 15.4 (1.3–300.6), P = 0.0263;
       provision of a recommendation rather than an assessment alone, OR 7.1 (1.3–45.6), P = 0.0187;
       computer-based, OR 6.3 (1.2–45.0), P = 0.0294. **Of the 32 systems possessing all four features, 30
       (94%) improved clinical practice.** The "recommendation rather than assessment alone" finding is the
       direct analogue of writing a runnable test rather than a description of a concern. **SECONDARY** —
       these figures were read this run from the CRD/DARE quality-assessed critical abstract (NBK71623) in
       full, not from the BMJ primary. The CI on the workflow odds ratio is unbounded above, and CRD's own
       commentary notes the regression sample was small and the English-only RCT search may have missed
       studies. Treat OR 112.1 as directionally load-bearing and numerically fragile.
    5. Institute for Healthcare Improvement / National Patient Safety Foundation, 2015 (tool rev. 2019).
       "Patient Safety Essentials Toolkit: Action Hierarchy (part of RCA²)," levels derived from the VA
       National Center for Patient Safety RCA tools. — The normative framework that ranks corrective
       actions by how little they depend on a person choosing to act. Weaker actions ask a person to behave
       differently; stronger actions change the artifact. Its worked Case Example 2 is, structurally, this
       presumption: an abnormal finding requiring follow-up is lost between services. **Stronger action:
       "Automatically include and flag test results that require follow-up in the discharge documentation
       that goes to the primary care doctor and require acknowledgment and follow-up." Weaker action:
       "Update a policy on appropriate test result communication and follow-up."** That is a prose document
       versus a flagged field in the machine-readable handoff artifact, ranked, with the structured
       placement ranked stronger. The toolkit adds that weaker actions "when used alone are unlikely to be
       sufficient for sustained improvement." **VERIFIED** — PDF retrieved and read in full this run.
       Caveat: this is expert consensus and a ranking convention, not measured execution rates.
    6. Beyer, B., Jones, C., Petoff, J. & Murphy, N.R. (eds.), 2016. *Site Reliability Engineering*,
       Chapter 1 (Treynor Sloss). O'Reilly / sre.google. — Two statements on point. On placement of
       procedure: "we have found that thinking through and recording the best practices ahead of time in a
       'playbook' produces roughly a **3x improvement in MTTR** as compared to the strategy of 'winging
       it.'" On the form an alert must take: "Monitoring should never require a human to interpret any part
       of the alerting domain. Instead, software should do the interpreting, and humans should be notified
       only when they need to take action." **VERIFIED** — chapter retrieved and read this run. The 3x
       figure is an uncontrolled internal observation with no method, denominator, or period attached;
       **DO-NOT-CITE as a measured effect.** Cite it as documented practitioner belief only.
    7. Osheroff, J.A. et al., "The Five Rights of Clinical Decision Support" (framework first articulated
       2007; developed in *Improving Outcomes with CDS: An Implementer's Guide*, 2nd ed. 2012). — The
       canonical statement that format and channel are first-class determinants alongside content: the
       right information, to the right person, in the **right format**, through the **right channel**, at
       the **right time in the workflow**. Directly relevant in that it treats "where and in what form"
       as co-equal with "what," which is the presumption's structure. **SECONDARY** — framework read at
       summary level; it is a design heuristic, not an evidence base.
    8. Shojania, K.G., Jennings, A., Mayhew, A., Ramsay, C.R., Eccles, M.P. & Grimshaw, J., 2009. "The
       effects of on-screen, point of care computer reminders on processes and outcomes of care." Cochrane
       Database of Systematic Reviews, CD001096. — Included **as a ceiling on the claim, not as support
       for it.** 28 studies, 32 comparisons. Point-of-care computer reminders — i.e. correctly placed,
       correctly timed, machine-generated prompts — achieved a median improvement in process adherence of
       only **4.2% (IQR 0.8% to 18.8%)**, and a median absolute improvement of 2.5% (IQR 1.3% to 4.2%) on
       dichotomous clinical endpoints. Correct placement alone, without a default or a forcing function,
       buys single-digit percentage points on average. **UNVERIFIED** — these figures come from a
       search-layer summary of the review's abstract; the Cochrane primary was not retrieved this run.
       **DO-NOT-CITE the 4.2% as verified.**
    9. **Adverse finding, reported rather than suppressed.** Facey, A. et al., 2024. "The ritualisation of
       the surgical safety checklist and its decoupling from patient safety goals." Sociology of Health &
       Illness; and (2024) "Surgical safety checklist compliance process as a moral hazard: An
       institutional ethnography." PLOS ONE 19(2): e0298224. — Where the structured artifact becomes the
       unit of compliance reporting, the artifact and the act come apart: nurses "pre-charted" compliance,
       ticking the EMR-housed compliance form ahead of the procedure, so that "the compliance form and not
       the [checklist] itself formed the basis for reporting," obscuring poor adherence. Moving a
       requirement into a machine-readable field creates a new failure mode in which the field is satisfied
       and the work is not. **SECONDARY** — abstract/summary level.
    10. Practitioner and vendor literature on embedding executable remediation in alerts (incident.io,
       Rootly, Cutover, Cast AI; several granted US patents on run-book automation with actionable
       documents, e.g. US 8,533,608 and US 11,960,378). — Converges unanimously on the presumption's
       prescription, in its own idiom: "every step should be a command, not a paragraph." Circulating
       figures of 30–50% MTTR improvement from automated runbooks are vendor marketing with no method.
       **UNVERIFIED**, and every quantitative claim in this stratum is **DO-NOT-CITE**. Reported only to
       record that the industry consensus exists and that it rests on no published measurement.

  Strength of support: **Strong** for the comparative limb (machine-readable, co-located, executable
    remediation is executed at substantially higher rates than the same content in prose, for human
    readers). **None** for the determinative limb (that placement is what decides, as opposed to one large
    factor among several).

  Summary: This is the best-supported item this searcher has returned. The comparative limb has a direct
    randomised test: Mehta et al. took one recommendation, left the content identical, moved it out of a
    prose alert and into a pre-checked line inside the order set the clinician was already opening, and
    execution rose 42.4% to 80.5% ordered and 38.1% to 69.9% completed — a +31.8 percentage-point adjusted
    difference on the outcome that is actually analogous to "did any agent run it." Google's ten-year
    sequence supplies the software-domain replication at scale and in the estate's own medium: the same
    findings, placed in a dashboard, went unread; placed in filed bug reports, were fixed 16% of the time;
    placed as a comment on the changed line with an applicable fix attached, drew over 5,000 "Please Fix"
    clicks and around 3,000 applied fixes per day. Kawamoto's regression puts a number on the general case
    — workflow-integrated placement is the single largest predictor of a decision-support system changing
    practice, larger than any property of the content — and the RCA² Action Hierarchy independently ranks
    "flag it in the machine-readable handoff and require acknowledgment" above "update the policy prose"
    as a matter of settled patient-safety doctrine. Two qualifications are load-bearing and neither is
    optional. First, the strongest source confounds: Mehta's intervention changed placement *and* flipped
    the default to opt-out *and* removed clicks, and the authors credit all three; no study found isolates
    placement from defaulting. Second, Shojania's meta-analysis shows that correct placement *without* a
    default or forcing function returns a median of a few percentage points, which is nowhere near "is what
    determines whether any agent ever runs it." The literature's own verdict is that the estate's scheduler
    check worked because it was simultaneously machine-readable, co-located, one-line, and attached to a
    failing status — a bundle, not a location.

  Caveats:
    - **The determinative limb has no support and the search was not close.** Every literature found treats
      placement as a manipulable factor with a measurable effect size, and every one of them also reports
      other factors with non-zero effects — ownership, trust, false-positive rate, cost of compliance,
      defaults. Kawamoto's own result is that four features are independently predictive, not one.
    - **Confounding in the best source.** Mehta et al. is a clean randomised comparison of two *bundles*,
      not of two placements. Placement, opt-out defaulting, and click reduction move together. The estate
      cannot cite the +31.8 pp figure as the effect of placement alone.
    - **The Tricorder and SRE sources are authored by the builders of the interventions they evaluate.**
      Sources 2, 3, 5, 6 and 10 are all advocacy-adjacent: written by the team that built the thing, in
      defence of a design philosophy, with no control arm. Publication bias here runs in exactly the
      direction of this presumption. Source 1 is the only randomised, blinded-analysis evidence in the set,
      and source 4 the only systematic review.
    - **Magnitude ceiling.** If the estate's remedy is placement alone — move the test into the row, change
      nothing else — Shojania's 4.2% median is the honest prior, not Mehta's 31.8 points. To get the large
      effect, the test must also be the default action, cheap to run, and attached to a failing status.
    - **The structured field creates its own failure mode (source 9).** Once a machine-readable field is
      the compliance signal, it can be satisfied without the work being done. For this estate that maps
      directly onto PREMISE-086/100/141 (a green line must carry the timestamp of its evidence): a test
      written into a FAIL row can be marked run without being run, and the same placement that raises
      execution rates also raises the value of faking them.
    - **Domain transfer is the largest single gap.** All ten sources concern human readers — clinicians,
      developers, on-call engineers. The estate's readership is agents. The mechanisms the literature
      credits (status-quo bias, click cost, attentional salience, professional trust, warning blindness)
      are human-psychological and do not transfer to an agent by assumption. An agent's version of the same
      effect would have to be mechanical — the string is or is not in a field the next reader parses — and
      that mechanism is untested. See NOVELTY-FLAG.
    - **The estate's own evidence base is n=1 with no variance.** One counter-example in the machine-
      readable condition and an unspecified number of declines in the prose condition, with no record of
      whether the scheduler check's test also differed in being one line, being SQL, being cheap, or being
      attached to a live FAIL. The literature would predict that all four of those mattered.
    - Sources 1, 2, 3, 5 and 6 were verified in primary full text this run. Source 4's figures are from the
      CRD quality-assessed abstract, not the BMJ primary. Sources 7, 8, 9 and 10 are SECONDARY or
      UNVERIFIED, and no figure from 8 or 10 should be quoted as verified.

  Recommendation: PARTIALLY-SUPPORTED
    (Comparative limb: SUPPORTED, Strong. Determinative limb: NO-SUPPORT-FOUND.)

NOVELTY-FLAG:
  Item: PRESUMPTION-983
  Searched: Randomised EHR choice-architecture trials comparing prose alerts against structured embedded
    orders; the Kawamoto systematic review and the Osheroff five-rights framework; the static-analysis
    warning-actionability literature including Google's FindBugs-to-Tricorder sequence and Johnson et al.
    (2013) on why developers do not use static analysis tools; the RCA² Action Hierarchy and forcing-
    function doctrine; SRE alerting and playbook practice; the Cochrane point-of-care reminder review;
    and a targeted sweep for empirical work on whether an autonomous software agent or LLM executes a
    machine-readable instruction at a different rate than the same instruction in prose.
  Finding: The presumption's *human*-reader form is well covered and is not novel — it is, in the CDS
    literature, close to settled. What is not addressed anywhere the search reached is the form the estate
    actually needs: **no study was found measuring whether an autonomous agent reading another agent's
    report executes a test at a different rate depending on whether the test sits in a structured field or
    in prose.** The adjacent 2025–2026 agent literature concerns an agent's adherence to its *own* output
    format and to instructions from a principal, not an agent's discovery-and-execution of a remediation
    left in an artifact by a peer for no particular reader. The estate's scheduler-check episode — a test
    written into a FAIL row by one agent, found and run by a different agent six hours later with no
    handoff — appears to be an observation of a phenomenon with no literature.
  Implication: Two separable contributions. (a) The mechanism is different in kind for agents: for humans
    the credited mechanisms are attentional and motivational (salience, click cost, status-quo bias); for
    agents it would be parse-level — the instruction either is or is not in a field the next reader's
    routine already reads. That predicts a *step function* rather than the graded effect sizes the human
    literature reports, which is an original and cheaply testable prediction. (b) The estate is in an
    unusually good position to run the test that the literature has not: it already emits both conditions
    daily and could randomise placement of the next N proposed tests between a FAIL-row field and prose
    beneath a headline, measuring execution within a fixed window. That would be an original measurement,
    not a recombination.
  Recommended status: NOVEL (for the agent-readership limb only; the human-readership limb is
    well-established prior art and should be cited, not claimed)

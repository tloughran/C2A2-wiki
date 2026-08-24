SEARCH-FOR-PRESUMPTION-804:
  Date searched: 2026-08-15
  Original item: PRESUMPTION-804
  Original statement: [inferred] That "determinate" is a property of a repair rather than a judgment about one. It is the sole criterion separating what agents execute from what they hand to Tom — "determinate repoints" are done, anything requiring "argument, not labels" or "new prose" is escalated — and it is defined nowhere. Today it did two contradictory jobs within hours: one run declined to repoint because the fix was not determinate ("Closing that means adding argument, not labels, so I left it"), and another rewrote three commentaries on both frames, adding an editorial reading of Philippians 2:13, without reaching for the word at all. The boundary the fleet uses to decide what needs a human is one the fleet sets, silently, per run.

  POLARITY NOTE — what was searched FOR. The presumption is worded as the DEFECTIVE belief ("determinate is a property of the repair"). The proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses: (i) that the ALLOCATION OF DECISION RIGHTS between an automated agent and a human is a DESIGN ARTEFACT requiring an explicit and objective basis, not a property an agent reads off the task; (ii) that general classificatory criteria have OPEN TEXTURE — a core of clear application and a penumbra where the criterion does not decide, and where the decision is made BY the applier rather than found — so a one-word criterion cannot bear a delegation boundary; (iii) that where a criterion is left to the applier, the resulting OUTCOME VARIANCE IS A PROPERTY OF THE APPLIER, and this is measurable and has been measured at large scale in the best-studied analogue; and (iv) that the mature engineering treatment therefore assigns authority by DECLARED TIER, ex ante, rather than letting the actor determine its own level of autonomy per case. "SUPPORTED" below means 14b's worry is well grounded, and is equivalently evidence AGAINST the presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-804
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by collecting every same-day use of the execute/escalate boundary and finding
           the criterion applied inconsistently and defined nowhere.
      15a: Searched for supporting literature on the corrective proposition.
    Current status: SUPPORTED

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: escalat, autonom, delegat, discretion, authority,
    judgment, human-in-the-loop, criteri, waiv, tier.
    Found and read in full:
      - **PREMISE-073** (2026-06-??, ACTIVE) — THE CLOSEST ENTRY, and it is close enough that the
        residual must be stated carefully. "For an unattended/autonomous run, high-impact or
        irreversible actions (e.g., a ~1,000-page bulk vault mutation) must be emitted as a report
        plus a ranked action list for human review, not executed. THE RULE IS SCOPED TO HIGH-IMPACT
        ACTIONS BY TIER (not a blanket ban on autonomous action), and reports must have a path to
        reviewed execution OR THEY BECOME HITL THEATER." So the register already commits to
        TIERING as the correct shape of the boundary. What it does not do — and this is exactly
        14b's point — is define any tier. "High-impact or irreversible" is itself a criterion of
        the same kind as "determinate": it names a class without supplying a decision procedure,
        and the same run that applies it also decides what falls in it.
      - **PREMISE-054** (2026-06-08, ACTIVE, Moderate) — constraints fall into CONFIGURABLE POLICY
        (waivable with justification) and NON-BYPASSABLE CAPABILITY (cannot be waived because you
        cannot exercise an authority you were never granted); a policy rule that shadows a
        capability wall must be treated as EFFECTIVELY NON-WAIVABLE; and — load-bearing here —
        "EVERY WAIVER OF A POLICY RULE MUST BE EXPLICIT AND JUSTIFIED (Tom's Rule 12 — fail loud)."
        The execute/escalate boundary is a POLICY boundary in this taxonomy, so 054 already requires
        that each exercise of discretion at it be explicit and justified. 14b's evidence is that
        one run justified explicitly ("adding argument, not labels, so I left it") and another
        crossed the same boundary silently, "without reaching for the word at all." That second case
        is a PREMISE-054 violation and is arguably already dispositioned; the residual is why the
        violation is invisible rather than whether it is prohibited.
      - **PREMISE-009** (2026-04-21, ACTIVE) — task-authority scope contracts: each scheduled task
        operates within its DECLARED responsibilities; least privilege (Saltzer & Schroeder 1975);
        orchestrator-delegate separation; and the explicit separation of AUTHORITY (constrained)
        from ESCALATION (alert-based). The separation is the right frame for this item and shows
        the register has the vocabulary; what it lacks is a declared responsibility set fine-grained
        enough to say whether "rewrite three commentaries and add an editorial reading" is inside
        the tradition agent's scope.
      - **PREMISE-093** (2026-07-16, ACTIVE) — the credential case: a hard stop is legitimate for a
        gated action but must be PAIRED WITH A CONTEXT-BEARING ESCALATION, not a silent
        termination. The register's only worked example of a well-specified execute/escalate
        boundary — and it works precisely because the boundary is a CAPABILITY wall (logged out or
        not), i.e. PREMISE-054's non-bypassable class, where no judgment is required.
      - **PREMISE-006** (transparent flagging of gaps rather than fabrication; escalation-tier
        discipline paired with the principle at boundary cases — the register itself flagged the
        need for "escalation-tier discipline" as far back as 2026-04 and it appears never to have
        been built), **PREMISE-090** (attended HITL as one-time remediation, not standing cadence),
        **PREMISE-121** (each item routed to a human has a cost; raise information value per item),
        **PREMISE-078** (specify the falsifier independently of outcomes — register, then look; the
        same ex-ante-specification move one domain over).
    CONCLUSION OF THE CHECK: **SUBSTANTIAL OVERLAP ON THE SHAPE, NONE ON THE CONTENT. NO
    NOVELTY-FLAG.** The register already holds that authority should be scoped and declared (009),
    that it should be tiered by impact (073), that policy waivers must be explicit and justified
    (054), and that a hard stop must escalate with context (093). What genuinely survives:
      (R1) NO TIER HAS EVER BEEN DEFINED. PREMISE-073 mandates tiering and supplies no tiers;
           PREMISE-006's disposition called for "escalation-tier discipline" in April 2026 and
           nothing in the register records it being built. The boundary is mandated in the abstract
           and unspecified in every concrete instance. That gap — a required artefact that four
           premises presuppose and none contains — is the item's actual finding.
      (R2) THE CRITERION IS SET BY THE PARTY IT CONSTRAINS. Every register entry treats the scope
           as given TO the agent. None addresses the case where the agent supplies the predicate at
           runtime. This is the self-exemption structure of PRESUMPTION-796/799 in a new location.
      (R3) THE ESCALATION RATE IS AN UNRECOGNISED MEASUREMENT. 14b's risk statement — "if it is a
           per-run judgment then the escalation rate is a measure of agent disposition rather than
           of item difficulty" — makes the rate an instrument reading whose measurand is unclear.
           That is PREMISE-140's channel-naming problem applied to a rate nobody currently computes.
    DECLARED LIMITATION: string grep, measured at five-of-nine recall by the 2026-08-14 15c run
    (ASSUMPTION-1052 — ~56%). The list above is a **LOWER BOUND**. Note that the word "determinate"
    itself returned nothing from the register, which is weak evidence that the term is genuinely
    undefined — weak, because a term used as a criterion in agent contracts would not necessarily
    surface in a premises file even if it were defined somewhere.

  Supporting evidence found: Yes

  Sources:
    1. Hart, H.L.A. (1961), *The Concept of Law*, ch. VII, drawing on Waismann, F. (1945),
       "Verifiability," *Proceedings of the Aristotelian Society* supp. vol. 19. — **The direct
       answer to clause (ii), and it says something stronger than "the word is vague."** Hart's
       claim is that general classificatory terms necessarily have a CORE of settled application
       and a PENUMBRA where the rule does not determine the answer, so that in penumbral cases the
       applier must EXERCISE DISCRETION — the decision is made, not discovered. The canonical
       example ("no vehicles in the park": clearly a motor car, unclearly a bicycle) has the same
       structure as "determinate repoint": clearly a one-word deletion matching neighbouring days'
       convention, unclearly a commentary rewrite that adds an editorial reading. The load-bearing
       point for 804 is that this is NOT a defect of the particular word "determinate" and cannot
       be repaired by choosing a better word: open texture is a property of general terms as such,
       so ANY one-word criterion at a delegation boundary will have a penumbra, and the question is
       only whether the system has a rule for who decides in it. Hart's own answer is that in the
       penumbra the applier has discretion and the system must supply an authority structure —
       which is precisely what C2A2 lacks. IMPORTANT SCHOLARLY CAVEAT, found this run: the
       secondary literature (Bix; Schauer 2011, "On the Open Texture of Law") holds that Hart's
       usage diverges from Waismann's — Waismann's open texture is the possibility of vagueness
       under unforeseen circumstances, Hart's is ordinary borderline vagueness — and that Hart
       "should not be read as basing his argument for judicial discretion on the nature of
       language; primarily, he was putting forward a POLICY argument for why rules should be
       applied in a way which would require that discretion." That correction strengthens rather
       than weakens the transfer: on the policy reading, leaving a criterion open is a CHOICE with
       reasons, which is exactly the choice C2A2 has made without noticing. [SNIPPET LEVEL on the
       secondary literature, which was located and read this run (Schauer 2011 PDF at
       horty.umiacs.io; Bix's "H.L.A. Hart and the Open Texture of Language"); CANONICAL and cited
       from established knowledge for Hart and Waismann themselves, neither re-read this run.]
    2. Ramji-Nogales, J., Schoenholtz, A.I. & Schrag, P.G. (2007), "Refugee Roulette: Disparities
       in Asylum Adjudication," *Stanford Law Review* 60:295; expanded as *Refugee Roulette* (NYU
       Press, 2009). — **The empirical demonstration of clause (iii), at a scale that leaves little
       room for argument.** Analysis of 133,000 decisions by 884 asylum officers over seven years,
       140,000 decisions by 225 immigration judges over four and a half years, 126,000 Board of
       Immigration Appeals decisions and 4,215 Courts of Appeal decisions. The finding: grant rates
       differ sharply between adjudicators EVEN WHEN different adjudicators in the same office each
       decided large numbers of applications from nationals of the same country — i.e. with case
       difficulty held approximately constant. The authors' summary is the sentence 804 needs: "in
       many cases the most important moment in an asylum case is the instant in which a clerk
       RANDOMLY ASSIGNS an application to a particular asylum officer or immigration judge." That
       is 14b's risk statement, measured: where a criterion is open and the applier decides, the
       outcome is substantially a property of WHICH applier, and the disposition rate therefore
       measures the adjudicator rather than the docket. Note also the authors' recommendations —
       training, effective and independent appellate review, professionalisation, and explicitly
       NOT quotas — which is a useful constraint on remedy design. [VERIFIED at bibliographic and
       finding level this run — the Stanford Law Review PDF hosting, the Georgetown scholarship
       record and the SSRN listing were located; the four dataset sizes, the same-office/
       same-nationality control, and the random-assignment sentence were read from retrieved text.
       Full study NOT read; the Stanford Law Review volume/page is cited from established knowledge
       and was not confirmed digit-by-digit.]
    3. Parasuraman, R., Sheridan, T.B. & Wickens, C.D. (2000), "A Model for Types and Levels of
       Human Interaction with Automation," *IEEE Transactions on Systems, Man, and Cybernetics —
       Part A: Systems and Humans* 30(3):286-297. — **The engineering statement of clauses (i) and
       (iv).** Automation is decomposed into four function classes (information acquisition;
       information analysis; decision and action selection; action implementation), each of which
       can be automated along a continuum of levels from fully manual to fully automatic. The
       paper's stated purpose is to provide "a framework and AN OBJECTIVE BASIS for deciding WHICH
       SYSTEM FUNCTIONS SHOULD BE AUTOMATED AND TO WHAT EXTENT," on the ground that "automation
       does not merely supplant but CHANGES human activity and can impose new coordination demands
       on the human operator." Two things transfer. First, the level of automation is a DESIGN
       PARAMETER set by the designer with reasons — the exact opposite of a property an agent reads
       off a task at runtime. Second, the four-way decomposition is directly usable here: C2A2's
       tradition agents are plainly authorised at high levels for acquisition and analysis, and the
       contested cases are all in DECISION AND ACTION SELECTION, where "add an editorial reading of
       Philippians 2:13" sits. The framework predicts that the boundary will be contested at
       precisely that stage, which is where 14b found it. [VERIFIED at bibliographic level this run
       — journal, volume 30, pages 286-297, year and the four function classes confirmed across the
       ACM DL record, Semantic Scholar and multiple reference listings. Paper NOT read in full.]
    4. The adjustable-versus-adaptive autonomy literature — including Scerri, Pynadath & Tambe,
       "Towards Adjustable Autonomy for the Real World" (arXiv:1106.4573); the ACM THRI survey
       "Variable Autonomy through Responsible Robotics: Design Guidelines and Research Agenda"
       (2024); and the Frontiers in Organizational Psychology study "Maybe adaptive (not adaptable)
       automation in production: an experimental study comparing THE LOCUS OF AUTHORITY in work
       system dynamics" (2025). — **Names the exact distinction 804 is missing, and shows the field
       treats it as the primary design question.** The literature separates ADJUSTABLE autonomy,
       where the human operator holds initiative over the autonomy level, from ADAPTIVE autonomy,
       where the level is adjusted by context or by the system. C2A2 currently has neither: it has
       an agent-determined level with no declared policy, which the literature describes as agents
       that "dynamically adjust their own level of autonomy" and "decide by themselves when to
       adapt their autonomy." Crucially, where that pattern IS endorsed in the literature it is
       endorsed with a stated decision rule — the agent transfers control when doing so is
       "expected to have NET BENEFIT," an explicit criterion — not as an unexamined default. That
       the field's own name for the design axis is "the locus of authority" is itself the finding:
       the question of WHO SETS the boundary is recognised as prior to where the boundary sits.
       [SNIPPET LEVEL — all three located this run and read at abstract/summary level; the Frontiers
       full text was retrieved but exceeded the readable budget and was NOT read. Mixed grade:
       arXiv preprint, peer-reviewed survey, and one 2025 experimental study whose findings are NOT
       relied on here — only its framing vocabulary is.]
    5. Saltzer, J.H. & Schroeder, M.D. (1975), "The Protection of Information in Computer Systems"
       — least privilege, fail-safe defaults, complete mediation. — Included for one specific
       clause with unusual force here: COMPLETE MEDIATION requires that every access to every
       object be checked against an authority, which entails that the authority exists
       independently of the requester. An authority predicate supplied by the requester at the
       moment of request is not mediation in this sense. [ALREADY REGISTER-HELD — PREMISE-009's and
       PREMISE-054's own cited source, read there this run; NOT re-verified externally. Cited to
       show the corrective is already grounded in-house, NOT as new support.]

  Strength of support: **Strong.** Clause (ii) is a canonical result in jurisprudence and
  philosophy of language; clause (iii) is measured at a scale (400,000+ decisions) that few
  behavioural findings match; clauses (i) and (iv) are the settled framing of the human-automation
  literature. The convergence across four independent fields is unusually clean, and both search
  strands that could have contradicted it (the adaptive-autonomy literature, which does endorse
  agent-set autonomy) turned out to endorse it only WITH a declared criterion.

  Summary: The corrective proposition is strongly supported and each of the four literatures
  supplies a different and non-redundant piece. Hart and Waismann establish that the failure is
  structural rather than lexical: general classificatory terms have a settled core and a penumbra,
  in the penumbra the criterion does not decide and the applier does, and therefore no choice of
  word repairs a one-word delegation boundary — the question is only whether the system has a rule
  for the penumbra. C2A2 does not, which is why "determinate" could do two contradictory jobs in
  one day without either run being wrong by its own lights. Refugee Roulette measures what happens
  when that structure is left unrepaired at scale: across four adjudication levels and hundreds of
  thousands of decisions, grant rates diverge sharply between adjudicators even holding office and
  applicant nationality constant, so that the identity of the assigned adjudicator is among the
  strongest predictors of outcome. Transposed, that is 14b's risk statement as a measured result
  rather than a worry: where the criterion is open, the disposition rate is a property of the
  disposer. Parasuraman, Sheridan and Wickens supply the engineering correction — the level of
  automation is a design parameter to be set on an objective basis, decomposed across acquisition,
  analysis, decision/action-selection and implementation — and their decomposition locates C2A2's
  contested cases precisely, in decision and action selection, which is where the framework
  predicts contention. The adjustable-versus-adaptive autonomy literature names the missing axis
  outright: the primary design question is THE LOCUS OF AUTHORITY, who holds initiative over the
  autonomy level. C2A2 has silently answered it in the agent's favour without recording that an
  answer was given — and where the literature does endorse agent-set autonomy, it does so with an
  explicit transfer criterion (net expected benefit), which is exactly the artefact that is
  missing.

  Caveats:
    (a) THE SHAPE IS REGISTER-HELD AND ONLY THE CONTENT IS MISSING. PREMISE-073 already mandates
        tiering; PREMISE-009 already requires declared scope; PREMISE-054 already requires every
        policy waiver to be explicit and justified. If a disposition mints "the boundary should be
        declared," it is re-minting 073 and 009. The disjoint content is (R1) that four years of
        premises presuppose a tier definition that has never been written, (R2) that the predicate
        is supplied by the constrained party, and (R3) that the escalation rate is an instrument
        whose measurand is undefined.
    (b) OPEN TEXTURE IS IRREDUCIBLE AND THIS BOUNDS THE REMEDY — a point that cuts against an
        over-strong disposition. Hart's claim is not that better drafting eliminates the penumbra;
        it is that the penumbra is a property of general terms. Any replacement criterion, however
        carefully written, will have borderline cases. So the achievable remedy is NOT a definition
        of "determinate" that decides every case. It is (i) a rule for what to do IN the penumbra —
        which, given asymmetric costs, is plausibly "escalate when uncertain," making uncertainty
        itself the trigger rather than determinacy — and (ii) a record of each penumbral call so
        the boundary's actual location becomes visible over time. Hart's system solves this with
        precedent, not with better rules, and that is the cheaper analogue.
    (c) THE ASYLUM ANALOGY IS STRONG ON MECHANISM AND WEAK ON EVERYTHING ELSE. Refugee Roulette
        concerns hundreds of human adjudicators under time pressure with career incentives and
        political salience, deciding matters of life and liberty. C2A2 has a small number of LLM
        agents from one model family deciding whether to edit a wiki file. TWO SPECIFIC TRANSFER
        RISKS. First, LLM agents from one family may be MORE consistent than human adjudicators,
        not less, because they share a prior — in which case the observed inconsistency is evidence
        of something other than ordinary applier variance and deserves separate diagnosis. Second
        and opposite, PREMISE-058's correlated-error result means that if they ARE consistent, the
        consistency is not evidence that the boundary is well drawn — they could be consistently
        wrong. The analogy establishes that applier-variance is a real and measurable phenomenon;
        it does not establish its magnitude here, and the magnitude is what would decide whether
        this matters.
    (d) THE THREE CASES 14b CITES MAY NOT BE THE SAME BOUNDARY. Two involve a repoint; the third
        involves rewriting commentaries and adding an editorial reading. Under Parasuraman et al.'s
        decomposition these are arguably different function classes — the repoint is closer to
        action implementation, the editorial reading is decision and action selection — and it is
        possible that the fleet is applying two coherent implicit standards rather than one
        incoherent explicit one. That reading is not obviously wrong and it is not tested by
        anything located here. It also does not rescue the item: two coherent implicit standards
        that nobody has written down are still an undeclared boundary, and the third run's silence
        remains a PREMISE-054 violation on either reading.
    (e) n IS SMALL AND THE EVIDENCE IS A SAME-DAY READING BY ONE RUN. Three uses of a boundary on
        one day, reported by the run that collected them (PREMISE-777's unmarked-self-report
        concern). The argument here does not depend on the count — one case of the same criterion
        licensing opposite actions is enough to show it is not deciding — but the INCONSISTENCY
        RATE, which is what would justify remediation cost, is not established by n=3.
    (f) PARASURAMAN ET AL. IS 26 YEARS OLD AND PREDATES GENERATIVE AGENTS. Its "objective basis"
        is grounded in human-performance consequences (workload, situation awareness, skill decay,
        automation-induced complacency) that have no direct analogue for an LLM agent. What
        transfers is the DESIGN-PARAMETER framing and the four-way decomposition. What does not
        transfer is the specific evaluative criteria for choosing a level.

  Search scope: COMPREHENSIVE on open texture and the discretion-in-the-penumbra result, including
  the secondary literature's Hart/Waismann correction. STRONG on the empirical applier-variance
  result (Refugee Roulette; four datasets, verified at finding level). GOOD on the
  automation-authority framework, verified bibliographically. MODERATE on adjustable-versus-adaptive
  autonomy — the vocabulary is confirmed, the empirical studies were not read. NOT SEARCHED, and
  each would materially strengthen or weaken this: (i) INTER-RATER RELIABILITY methodology —
  Cohen's/Fleiss' kappa applied to escalate/execute decisions — which is the direct in-house
  measurement and would convert 14b's worry into a number for the cost of one seeded batch; (ii)
  the clinical-guideline literature on vague qualifiers ("consider," "if appropriate") and measured
  compliance variance, which is the closest professional analogue at the right scale and would
  address Caveat (c)'s magnitude question; (iii) Jensen & Meckling on specific knowledge and the
  co-location of decision rights with information, which is the economics-side argument for why
  some of this boundary SHOULD sit with the agent and would supply the counterweight this file
  lacks; (iv) LLM-agent-specific work on self-assessed task difficulty and calibrated deferral,
  which is the modern form of the question and was not reached this run.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently
  NO-SUPPORT-FOUND for the presumption as worded. Four carries, in order of cost:
    1. THE MISSING ARTEFACT IS ALREADY MANDATED (R1). PREMISE-073 requires tiering and defines no
       tiers; PREMISE-006's April 2026 disposition asked for "escalation-tier discipline" and the
       register contains no record of it existing. The finding is not that C2A2 needs a rule — four
       premises already say so — but that the rule they all presuppose was never written. That is a
       one-document repair and it is overdue by roughly sixteen months.
    2. THE PENUMBRA RULE MATTERS MORE THAN THE DEFINITION (Caveat b). Because open texture is
       irreducible, the achievable target is a rule for uncertain cases plus a log of penumbral
       calls — precedent rather than better drafting. Given asymmetric costs (a wrong edit to a
       tradition wiki versus a routed item costing Tom a few minutes, and PREMISE-121's warning that
       routing has a real cost), the tie-break is a genuine design decision and should be made
       explicitly rather than left to whoever runs next.
    3. THE ESCALATION RATE IS A MEASUREMENT NOBODY IS TAKING (R3). It is currently uncomputed and
       its measurand is undefined — PREMISE-140's problem in a new place. The cheap discriminating
       test is a seeded one: route the SAME small set of borderline repairs past several agents and
       compare. Agreement means the fleet has an implicit standard worth writing down; disagreement
       means the escalation rate is measuring disposition, and 14b's risk statement is confirmed
       rather than argued. Either outcome is informative, which is the mark of a test worth running.
    4. ONE OF THE THREE CASES IS ALREADY A PREMISE-054 VIOLATION. The run that crossed the boundary
       "without reaching for the word at all" waived a policy rule without an explicit justification,
       which 054 forbids in terms. That does not need new literature or a new premise; it needs
       enforcement, and its invisibility is the more interesting fact.

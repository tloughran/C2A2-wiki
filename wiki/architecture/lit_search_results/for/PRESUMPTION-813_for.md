SEARCH-FOR-PRESUMPTION-813:
  Date searched: 2026-08-16
  Original item: PRESUMPTION-813
  Original statement: [inferred] That the sync channel's 17-day failure is a Chrome problem rather than a
    carrier-choice problem, with two unmentioned alternatives already in use for other purposes.
  Risk if wrong: High
  Search question (as queued): Coupling and failure modes of UI-automation integrations versus file- or
    API-mediated ones; single-channel dependency in human-in-the-loop systems.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE belief the
  designers held ("it is a Chrome problem"). The proposition searched FOR is the CORRECTIVE CONVERSE, in
  four clauses:
    (C1) DRIVING ANOTHER PROGRAM'S USER INTERFACE IS A RECOGNISED HIGH-BREAKAGE CARRIER. UI-mediated
         integration couples the integrator to the *presentation layer* of a system it does not control,
         and the presentation layer is the layer with the highest change rate and the weakest contract.
         Breakage from cosmetic, non-semantic change is the expected behaviour of such a carrier, not an
         anomaly, and it is measured.
    (C2) FILE- AND API-MEDIATED CARRIERS ARE THE NAMED, DOCUMENTED, LOWER-COUPLING ALTERNATIVES, and the
         trade (slower to stand up, immune to UI change) is stated explicitly in the integration
         literature. Choosing the UI carrier is therefore a DESIGN DECISION with a known cost, not a
         default.
    (C3) A CARRIER WITH NO ALTERNATE PATH IS A SINGLE POINT OF FAILURE, which is a property of the
         architecture, not of the vendor whose UI changed. Seventeen days of failure with no failover is
         a statement about the design.
    (C4) ATTRIBUTING A REPEATED LOSS TO A COMPONENT RATHER THAN TO THE CONTROL STRUCTURE IS THE
         CANONICAL ERROR of the chain-of-events / component-failure accident model, and system-safety
         practice has an explicit, mature replacement for it.
  "SUPPORTED" below therefore means 14b's worry is well grounded, and is equivalently evidence AGAINST
  the presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-813
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the designers were unaware
      they were treating a carrier choice as a vendor fault)
    Transform at each step:
      14b: Noted that seventeen days of reports name a CAUSE and none names a DESIGN.
      15a: Searched for supporting literature on the corrective proposition; performed the register
        check first and found that the register itself recorded the failure mode in advance.
    Current status: SUPPORTED

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: Chrome, extension, browser, automation, clipboard, paste,
    delivery, sync, dark, single channel, single point, fallback, carrier, coupling, filesystem, queue,
    inbox, outbox, API.
    Found and read in full:
      - **PREMISE-033** (2026-05-19, ACTIVE, High, re-check due **2026-08-19 — three days from the date
        of this file**) — THE DECISIVE REGISTER HIT AND THE MOST IMPORTANT SENTENCE IN THIS CHECK. It
        validated the cowork-to-chat delivery path as "technically sound," and its recorded challenge
        reads: "**execCommand deprecation risk in long-term Chromium roadmap; need documented
        fallback.**" The register named the carrier's dependence on a deprecated browser API and named
        the missing fallback FIFTEEN MONTHS AGO. The fallback was never documented and never built.
        PRESUMPTION-813 is therefore not a new discovery; it is the arrival of a consequence the
        register wrote down and did not act on — which is PREMISE-151's incubation pattern exactly.
      - **PREMISE-023** (2026-05-18, ACTIVE) — folder-as-queue + worker-script is a CANONICAL
        integration architecture at C2A2's scale. This is one of 813's "two unmentioned alternatives
        already in use for other purposes," already validated in the register as an acceptable carrier.
      - **PREMISE-024** (2026-05-18, ACTIVE) — filesystem inbox/outbox/done/failed with Maildir-style
        naming as a canonical, well-grounded coordination boundary. The second alternative carrier,
        likewise already validated.
      - **PREMISE-125** (2026-07-25, ACTIVE) — the two-Chrome-extension incident: redundancy without
        arbitration REDUCED availability on this exact channel. Same carrier, prior failure, different
        mechanism.
      - **PREMISE-131** (ACTIVE) — a warning is not a control, and an UNDELIVERED warning has ZERO
        effect; its Applicable-to already names "the sync/notification channel dark for 5 consecutive
        runs (ASSUMPTION-559 / OPEN-135) — any mitigation routed over it must be scored as zero until
        delivery is restored." The register already treats this channel as a scored-zero path.
      - **PREMISE-102** (ACTIVE) — fail-loud is reporting, not remediation; repeated identical
        non-processing converts a signal into a standing policy of non-coverage.
      - **PREMISE-164** (2026-08-14, ACTIVE) — durability of a declared record is a property of its
        ADDRESSING, and "declare it more prominently" is the wrong remedy shape for an addressing
        failure. The analogue here: "fix Chrome" is the wrong remedy shape for a carrier failure.
      - **PREMISE-166** (2026-08-15, ACTIVE) — a signal must terminate at a receiver OUTSIDE the failure
        domain. A delivery path that lives entirely inside one browser process does not.
      - **PREMISE-141** (2026-08-05, ACTIVE) and **PREMISE-110** — common-mode / single-channel-wearing-
        two-labels family, relevant because the "alternatives" must be checked for shared failure domain
        before being counted as alternatives.
    CONCLUSION OF THE CHECK: **HEAVY OVERLAP, AND ONE ENTRY IS A PRIOR WARNING OF THIS EXACT EVENT. NO
    NOVELTY-FLAG.** The register holds (a) the carrier's known fragility with a named missing fallback
    (PREMISE-033), (b) both alternative carriers as already-validated patterns (PREMISE-023/024), and
    (c) the rule that an undelivered mitigation scores zero (PREMISE-131). What the register does NOT
    hold, and what this file adds, is the ATTRIBUTION argument — the general claim that naming a
    component cause for a repeated loss is a recognised methodological error with a named replacement —
    and the QUANTITATIVE base rate for UI-carrier breakage.
    DECLARED LIMITATION: this was a STRING GREP, measured at ~56% recall (ASSUMPTION-1052) and at
    five-of-nine on a later run. The list above is a **LOWER BOUND** and the true overlap is likely
    larger. Given that it already returned nine entries, that argues for a narrower disposition.

  Supporting evidence found: Yes

  Sources:
    1. Leveson, N.G. — MIT 16.863J *System Safety*, Spring 2016, Week 2 class notes ("Accident Models;
       Systems Thinking; STAMP"), MIT OpenCourseWare; the material summarising *Engineering a Safer
       World: Systems Thinking Applied to Safety* (MIT Press, 2012). — **The direct and strongest
       support for clause (C4), and the source of the vocabulary 813 needs.** The notes state the
       standard approach to safety is "Reductionist — Divide system into components; ASSUME ACCIDENTS
       ARE CAUSED BY COMPONENT FAILURE; identify chains of directly related physical or logical
       component failures." They then present the Bhopal event chain and ask, pointedly, "**What was the
       'root cause'?**" — the demonstration that a chain-of-events narrative does not determine an
       answer, so any cause it names is a choice of where to stop. They list what analytic reduction
       "does not handle": component interaction accidents, **systemic factors (affecting all components
       and barriers)**, **system design errors**, and "migration of systems toward greater risk over
       time (e.g. in search for greater efficiency and productivity)." The Swiss-cheese limitations
       slide adds that such models "assume accidents are random events coming together accidentally" and
       give "no explanation of *why* events occurred." The prescription is stated as a one-line change
       of emphasis: "**'prevent failures' → 'enforce safety constraints on system behavior'**." Applied
       to 813: seventeen reports naming "Chrome" are seventeen instances of the component-failure model;
       the design question — what constraint should have been enforced so that no single un-backed
       carrier could take the channel dark — is the STAMP question, and no run asks it.
       [VERIFIED this run — the lecture-notes PDF was fetched and read in full. Every quoted phrase is
       read directly. NOTE: this is COURSEWARE summarising Leveson's book, not the book; treat
       slide-level phrasing as teaching text. The underlying claims are standard and are attributed in
       the notes to Leveson 2003 and Leveson 2011/2012.]
    2. Imtiaz, J., Sherin, S., Khan, M.U. & Iqbal, M.Z. (2019), "A Systematic Literature Review of Test
       Breakage Prevention and Repair Techniques," arXiv:1909.10750 (QUEST Lab, NUCES Islamabad; 41
       primary studies). — **The direct support for clause (C1), with the only quantitative anchor
       located this run.** The SLR defines TEST BREAKAGE as "premature stopping of test cases due to
       changes in the SUT" arising from "modifications in the application code such as **repositioning
       or renaming of existing elements, locator and layout changes**" — i.e. from changes that alter
       nothing semantic. It distinguishes STRUCTURAL changes ("the layout and structure of the
       application") from LOGICAL ones, and reports the magnitude: "**Even small modifications can lead
       to a large number of broken test cases, in some cases up to 74% of the test suite.**" Its
       taxonomy of breakage causes is organised by domain — code level, **web GUI level**, desktop GUI
       level, mobile GUI level — and it notes that in the GUI domain "the most common types of changes
       are the addition, deletion or modification of elements." The transfer to 813 is direct: a script
       that reaches a target by locating elements in a page it does not own is the same artefact class
       as a GUI test script, and its breakage rate is a property of that class.
       [VERIFIED this run — the arXiv PDF was fetched and substantial portions were read directly:
       abstract, introduction, research methodology, the RQ2 causes-of-breakage discussion, the tool and
       case-study tables, and the metrics section. The 74% figure is the SLR's own summary of its
       reference [3]; **the underlying study was NOT retrieved, so 74% is SNIPPET LEVEL and must be
       quoted as "as reported in the SLR."** This is a preprint of an SLR, not a peer-reviewed venue
       paper; its value is the taxonomy and the pooled framing, not any single number.]
    3. Alégroth, E. & Feldt, R. et al. (2016), "Maintenance of automated test suites in industry: An
       empirical study on Visual GUI Testing," *Information and Software Technology* (Elsevier);
       industrial study at Siemens and Saab. — **Corroboration for (C1) from a peer-reviewed industrial
       setting.** The reported finding is that maintenance cost is driven by the frequency and magnitude
       of changes to the UI, and that **the stability of the GUI is the main determinant of maintenance
       cost** — which is the same claim as (C1) stated as a cost function rather than a failure mode.
       [SNIPPET LEVEL — the ScienceDirect and Semantic Scholar listings were located this run and the
       findings were read from retrieved summaries; **the paper was NOT read.** Author list, venue and
       the two industrial sites are confirmed from the listing. Do not cite a figure or page from it.]
    4. Documented industry practice on RPA-versus-API integration — MuleSoft, "Crossing the chasm:
       Integration to Robotic Process Automation" and "Challenges of and opportunities for RPA"; Celigo,
       "Choosing between RPA and API integration." — **Support for clause (C2), at practitioner grade
       and explicitly labelled as such.** The consistent statement across these is that UI-driving bots
       are "highly sensitive to UI changes, especially with SaaS systems where you have no control over
       the changes made," and are therefore "high maintenance, prone to breaking with system updates";
       whereas API-mediated integration executes "behind the screens" and is "immune to changes of an
       application's GUI," with the acknowledged cost being "slower time to deployment if APIs do not
       exist." The one illustration worth carrying is the failure geometry: move a button and the bot
       "will keep looking for it" where it was. **PROVENANCE WARNING: these are VENDOR-AUTHORED
       marketing-adjacent sources with a commercial interest in the API conclusion. They are cited as
       evidence that the trade-off is DOCUMENTED AND WIDELY UNDERSTOOD, not as measurement.**
       [SNIPPET LEVEL — located this run and read at summary level; none of the pages was read in full.]
    5. C2A2-internal, and stronger than any of the above for this item: **PREMISE-033's own recorded
       challenge**, "execCommand deprecation risk in long-term Chromium roadmap; need documented
       fallback," dated 2026-05-19 and due for re-check 2026-08-19. — The fleet's own register
       identified the carrier's dependency, named the required mitigation, and the mitigation was not
       built. This is the single most useful sentence available on this item and it required no search.
       [VERIFIED this run — read directly from `validated_premises.md`.]
    6. Sagan, S.D. (2004), "The Problem of Redundancy Problem," *Risk Analysis* 24(4):935-946, and
       Perrow, C. (1984), *Normal Accidents*. — Carried for the standing caution that adding a second
       carrier is not automatically an improvement (813's "two unmentioned alternatives" must be checked
       for shared failure domain and for arbitration before being counted).
       [CANONICAL — cited from established knowledge via PREMISE-125's evidence line; NOT re-verified
       this run.]

  Strength of support: **Strong** on (C1), (C3) and (C4); **Moderate** on (C2).
    (C1) has a peer-reviewed industrial study and a 41-study SLR with a taxonomy that names exactly the
    change class at issue. (C4) has a mature, standardised discipline with a verified primary reading
    and an explicit replacement prescription. (C3) is near-definitional in system design and needs no
    heavy citation. (C2) is the weakest clause because the located sources are vendor-authored; the
    claim is nonetheless corroborated INTERNALLY at higher grade by PREMISE-023 and PREMISE-024, which
    validated both alternative carriers on their own literature two months apart.

  Summary: The corrective proposition is well supported, and the most striking feature of the search is
  that the strongest evidence was already inside the vault. Driving another program's user interface is
  a recognised, measured, high-breakage integration carrier: the systematic review defines test breakage
  as failure caused by "repositioning or renaming of existing elements, locator and layout changes" —
  changes that alter nothing semantic — and reports breakage of up to 74% of a suite from small
  modifications, while the Siemens/Saab industrial study finds GUI stability to be the main determinant
  of maintenance cost. The integration literature names file- and API-mediated carriers as the
  lower-coupling alternatives and states the trade explicitly, so the UI carrier is a design decision
  with a known cost rather than a default. Leveson supplies the frame for 14b's actual observation —
  that seventeen days of reports name a cause and none names a design. The component-failure model
  "assumes accidents are caused by component failure" and cannot handle "systemic factors" or "system
  design errors"; its own worked example asks "what was the root cause?" and demonstrates that the chain
  does not determine an answer, so any cause it names is a choice of stopping point. The prescribed
  correction is a change of emphasis from "prevent failures" to "enforce safety constraints on system
  behavior" — which for 813 means the question is not why Chrome changed but why one un-backed carrier
  could take a channel dark for seventeen days. And the register recorded the specific dependency on
  2026-05-19, named the specific missing mitigation ("need documented fallback"), and scheduled a
  re-check for 2026-08-19 — three days after this file. The fallback was never built.

  Caveats:
    (a) THE ALTERNATIVES ARE NOT AUTOMATICALLY INDEPENDENT AND MUST NOT BE COUNTED BEFORE THEY ARE
        CHECKED. PREMISE-141, PREMISE-110 and PREMISE-166 all bind here. A second delivery path that
        runs in the same sandbox, on the same scheduler, under the same credentials is a single channel
        wearing two labels. The filesystem carrier (PREMISE-023/024) is genuinely disjoint from the
        browser carrier at the presentation layer, but it is NOT disjoint at the scheduler or host
        layer, so it removes ONE coupling factor and not all of them. PREMISE-125 adds the second
        condition: an unarbitrated second carrier can REDUCE availability. Any move to a second carrier
        owes an explicit primary-selection rule.
    (b) THE VENDOR PROVENANCE OF SOURCE 4 IS MATERIAL AND IS NOT INCIDENTAL. MuleSoft and Celigo sell
        API integration. Their account of RPA fragility is consistent with the peer-reviewed GUI-testing
        evidence, which is why it is included, but no number from them should ever be quoted onward and
        the clause it supports (C2) should be treated as Moderate, not Strong, until a non-commercial
        source is found.
    (c) THE DOMAIN TRANSFER FROM GUI TEST AUTOMATION IS CLOSE BUT NOT EXACT. Test scripts and a delivery
        channel share the locator-fragility mechanism, but a test suite's breakage is DETECTED by the
        suite failing, whereas 813's channel went dark. Whether the sync channel's failure was
        loud-and-ignored or silent is not established by anything in this file, and it changes the
        remedy: a loud failure needs a fallback, a silent one needs PREMISE-110's affirmative,
        perishable heartbeat first.
    (d) THE STAMP TRANSFER IS CONCEPTUAL, NOT PROCEDURAL. STAMP/STPA is a hazard-analysis method for
        engineered socio-technical systems with a definable safety control structure. What transfers
        robustly is the ATTRIBUTION argument and the "enforce constraints, don't prevent failures"
        reframing. What does NOT transfer without work is the method itself; nothing here licenses a
        claim that a full STPA of the C2A2 fleet is warranted or affordable.
    (e) "17 DAYS" AND "TWO ALTERNATIVES" ARE 14b'S OBSERVATIONS AND WERE NOT INDEPENDENTLY VERIFIED BY
        THIS SEARCH. This file did not open the seventeen days of reports and did not enumerate the
        alternative carriers in use. It establishes that IF the observation holds, the literature
        supports the reading. Per PREMISE-124 that is not a calibrated measurement.
    (f) PUBLICATION BIAS RUNS THE ITEM'S WAY HERE AND SHOULD BE DISCOUNTED FOR. Papers about test
        breakage are written by people proposing repair techniques, who have an interest in breakage
        being common; the 74% figure in particular is a motivating statistic in an introduction. The
        direction of the effect is not in doubt; the magnitude should be treated as an upper end.

  Search scope: COMPREHENSIVE and VERIFIED on the attribution argument (Leveson lecture notes read in
    full). GOOD and VERIFIED on UI-automation breakage as a class (SLR read substantially; its 74%
    figure is second-hand). MODERATE on the carrier comparison (vendor sources only; corroborated
    internally by PREMISE-023/024). EXCELLENT on the register side, where the decisive evidence was
    found. NOT SEARCHED, and each would materially change this file: (i) whether `execCommand` has in
    fact been removed or restricted in the Chromium version in play — a one-check empirical question
    that would settle whether PREMISE-033's predicted deprecation is the actual mechanism, and which
    this file deliberately did not guess at; (ii) the human-in-the-loop half of the queued search
    question — SINGLE-CHANNEL DEPENDENCY IN HITL SYSTEMS SPECIFICALLY, as distinct from single points of
    failure generally — for which no on-point literature was located and which may be a genuine gap;
    (iii) any non-commercial empirical comparison of UI-mediated versus API-mediated integration
    reliability, which was sought and NOT FOUND — a clearly-labelled negative result, and the reason
    clause (C2) is graded Moderate.

  Recommendation: **SUPPORTED (Strong on C1/C3/C4, Moderate on C2)** for the corrective proposition;
  equivalently NO-SUPPORT-FOUND for the presumption as worded. Four carries:
    1. THE DISPOSITION SHOULD PROBABLY BE A RE-OPENING OF PREMISE-033, NOT A NEW PREMISE. Its re-check
       falls on 2026-08-19. This file is that re-check's evidence arriving three days early, and it
       reports that the premise's own named challenge ("need documented fallback") went unmet for
       fifteen months and then produced the predicted outcome. Per PREMISE-151 the correct reading is
       incubation, not discovery.
    2. THE ATTRIBUTION FINDING IS THE NEW CONTENT AND IT GENERALISES BEYOND THIS CHANNEL. "Seventeen
       reports name a cause and none names a design" is an instance of the component-failure accident
       model, which has a name, a documented failure profile, and a replacement. That is worth holding
       as a reading rule for the daily health report: a report that names a component has not yet named
       a design, and should say which constraint was absent.
    3. THE ALTERNATIVES ARE ALREADY REGISTER-VALIDATED, WHICH MAKES THIS CHEAP. PREMISE-023 and
       PREMISE-024 validated the filesystem carrier in May. Moving the channel is not a research task;
       it is a use of a pattern the register already holds — subject to caveat (a)'s arbitration rule
       from PREMISE-125.
    4. THE ONE THING TO GO AND LOOK AT. Before any remedy, establish whether the seventeen days were
       LOUD or SILENT. If silent, PREMISE-110's affirmative-and-perishable heartbeat is the first fix
       and the carrier change is the second; if loud, the ordering reverses. Nothing in this file
       settles it.

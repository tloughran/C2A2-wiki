SEARCH-FOR-PRESUMPTION-824:
  Date searched: 2026-08-17
  Original item: PRESUMPTION-824
  Original statement: [inferred] That waiting is a form of checking. The 15d design was falsified twice
    and the schedule did not change: 151 carry-overs advanced to 2026-08-23 in the same report.
  Risk if wrong: **High**. Priority: High.
  Search question (as queued): as ASSUMPTION-1117 (condition-based versus time-based maintenance;
    surveillance-interval evidence in screening; polling versus event-driven monitoring; the empirical
    basis for re-check intervals in systematic-review updating), plus the cost side — standing queue
    maintenance whose measured yield is zero, and inspection-interval optimisation.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE belief. The
  proposition searched FOR is the CORRECTIVE CONVERSE, in five clauses:
    (C1) ELAPSED TIME IS A WEAK PREDICTOR OF STATE CHANGE, and the discipline that spent the most money
         finding this out measured how weak.
    (C2) FIXED-INTERVAL INTERVENTION CAN BE WORSE THAN NONE, not merely wasteful.
    (C3) THE CORRECT TRIGGER IS A CONDITION OR SIGNAL, NOT A CLOCK.
    (C4) WHERE AN INTERVAL IS NEVERTHELESS USED, IT IS A DERIVED QUANTITY — computed from a hazard model
         and a cost ratio, and STRATIFIED — so an interval carried forward by default is an undeclared
         parameter, not a decision.
    (C5) A STANDING QUEUE IS NOT FREE. Its carrying cost is real, and a repeated re-check prompt has a
         documented failure mode of its own: it becomes a rubber stamp, manufacturing a false record of
         having looked.
  "SUPPORTED" below means 14b's diagnosis is well grounded, and is equivalently evidence AGAINST the
  presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-824
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the schedule was re-applied
      in the SAME report that recorded its second falsification, which means the re-application was not
      a judgement about the evidence — it was the absence of one)
    Transform at each step:
      14b: Inferred from the conjunction of two falsifications of the 15d design and an unchanged
        schedule advancing 151 carry-overs by seven days in the same document.
      15a: Searched for supporting literature on the corrective proposition; register check first.
    Current status: SUPPORTED (Strong on C1-C3, Moderate on C4-C5) — BUT SEE THE DUPLICATION WARNING;
      THIS IS AN ENFORCEMENT GAP, NOT A KNOWLEDGE GAP

  **DUPLICATION WARNING — READ BEFORE DISPOSITION. THE REGISTER ALREADY FORBIDS THE BEHAVIOUR OBSERVED.**
    - **PREMISE-154** (2026-08-13, ACTIVE) is directly on point and its binding clause is stated as
      NOT OPTIONAL: "**LOAD-BEARING FORM CONDITION, from 15b and not optional: the discharging mechanism
      must be TRIGGER-BOUND, NOT A CLOCK. Time-based expiry and scheduled full re-audit are the specific
      remedies with the WORST DOCUMENTED RECORD in the nearest analogous domain** — automatic closure of
      deferred items destroys accumulated triage state and forces re-derivation of judgements already
      made — **and a repeated re-audit prompt across six queues is predicted by the alert-fatigue
      evidence to become a RUBBER STAMP within a few cycles, which manufactures a false record of having
      looked** and is the fail-open pattern PREMISE-110 names." It further requires that a hold record,
      AT PLACEMENT, "(a) the observable whose change would make it wrong — its release condition — and
      (b) the party or process that reads that observable," and EXPLICITLY DECLINES to incorporate "a
      hold decays with elapsed time," recording that **no located source supports a decay model on the
      clock and none supplies a correct interval.** 151 carry-overs advanced by date, with no release
      condition read, is the exact behaviour PREMISE-154 forbids, four days after it was validated.
    - **PREMISE-095** (2026-07-09, ACTIVE, Moderate) holds the cost side with arithmetic already
      attached: at one run/day and 7-20 items/run against a ~55/week 15d re-trigger arrival rate, "**the
      refresh queue grows without bound absent a cadence change, admission cap, or throughput
      increase**" (Little 1961; Hopp & Spearman on rho>1). Its Applicable-to names "OPEN-115/OPEN-116
      (cadence/cap decision); 15d re-trigger design." **Its own re-check was due 2026-08-09 and this
      file is written on 2026-08-17 — the premise about overdue queues is itself eight days overdue,
      which is the item's own thesis realised on the register.**
    - **PREMISE-102** (High): fail-loud is reporting, not remediation; repeated identical non-processing
      converts a one-time signal into an undecided standing policy of non-coverage.
    - **PREMISE-151**: repeated disclosure of an unremediated condition NORMALISES it.
    - **PREMISE-133** (the parent of 154): a suspension is legitimate only if it names what would
      discharge it, who adjudicates, and a deadline after which continued suspension is itself reported
      as an unresolved exposure.
  Grep terms used against `validated_premises.md`: cadence, interval, carry-over, queue, trigger,
  clock, expiry, defer, hold, re-check, monitor, backlog, waiting, schedule. DECLARED LIMITATION: string
  grep at ~56% recall (ASSUMPTION-1052) — LOWER BOUND. **NO NOVELTY-FLAG.**
  **CONCLUSION OF THE CHECK: THIS IS NOT A LITERATURE GAP. IT IS AN ENFORCEMENT GAP AGAINST PREMISE-154
  AND PREMISE-095.** The register's own precedent for that situation (PRESUMPTION-781 and -783 on
  2026-08-13) is REVISE WITHOUT A MINT.

  Supporting evidence found: Yes

  Sources:
    1. Nowlan, F.S. & Heap, H.F. (1978), *Reliability-Centered Maintenance*, United Airlines / US
       Department of Defense (AD-A066579); and the RCM tradition built on it (SAE JA1011; the NASA RCM
       Guide). — **The support for clauses (C1) and (C2), and the largest empirical result located on
       this question in any domain.** The study analysed thousands of aircraft components and identified
       six failure patterns. The headline finding, as reported in the secondary literature retrieved
       this run, is that **only about 11% of failure modes are clearly age-related; roughly 89% are
       random with respect to age** — so a calendar-based intervention is aimed at a minority pattern.
       The second finding is sharper and is clause (C2): **about 68% of failures follow an
       infant-mortality curve**, so fixed-interval overhaul RESETS equipment into the high-hazard phase,
       "making failures more likely rather than less. In other words, TBM didn't just waste resources,
       it actively REDUCED reliability." The transfer to 824 is the conclusion, not the mechanism: where
       the state change you care about is not driven by elapsed time, a clock-driven check is targeting
       a variable that is not the one moving.
       **CITATION-HYGIENE WARNING, RECORDED PER PREMISE-132.** The figures above are reported
       INCONSISTENTLY across the secondary sources retrieved in this single search: one gives "roughly
       18 percent in subsequent corroborating studies" as the age-related fraction, another gives "~11%"
       and "~89%," another "68%" for infant mortality. These are not all the same statistic and the
       sources do not distinguish them carefully. **Do not carry any of these numbers into a premise
       without the primary report.**
       [SNIPPET LEVEL, AND THE WEAKEST-VERIFIED SOURCE IN THIS FILE. The primary Nowlan & Heap report was
       NOT retrieved. What was located and read at retrieved-summary level: the NASA RCM Guide (PDF,
       nasa.gov), Reliabilityweb's time-based-vs-condition-based article, SavvyAviation's RCM series,
       and several CMMS-vendor explainers (Tractian, Fiix, Oxmaint, Reliamag). **The majority are vendor
       marketing content.** Grade accordingly.]
    2. Shojania, K.G., Sampson, M., Ansari, M.T., Ji, J., Doucette, S. & Moher, D. (2007), "How Quickly
       Do Systematic Reviews Go Out of Date? A Survival Analysis," *Annals of Internal Medicine*
       147(4):224-233 (PMID 17638714). — **The support for clause (C4), and the best-identified source
       in this file because it treats the interval as an estimand rather than a convention.** Survival
       analysis of 100 quantitative systematic reviews indexed in ACP Journal Club, 1995-2005. Findings
       as retrieved: a signal for updating occurred **within 2 years for 23% of reviews and within 1
       year for 15%**, and **7% already had a signal AT THE TIME OF PUBLICATION**. Shorter survival was
       associated with cardiovascular topics (**HR 2.70**) and with heterogeneity in the original review
       (**HR 2.15**). Three things follow for 824. (i) The hazard is NOT uniform across the population —
       a single interval applied to every item is wrong for most of them by construction, and topic is a
       measurable stratifier. (ii) The 7% already-stale-at-publication figure is the direct analogue of
       ASSUMPTION-1117's 17-of-17: the clock had not started and the state had already changed, so
       elapsed-time-since-last-check is not even the right clock. (iii) The interval is derived from a
       measured hazard, which is what makes it a decision rather than a default.
       [SNIPPET LEVEL — the Annals landing page, the PubMed record, a ResearchGate copy, the Wikidata
       entry, an AHRQ/NCBI Bookshelf volume ("Identifying Signals for Updating Systematic Reviews"), and
       a companion editorial were LOCATED this run and read at retrieved-summary level. **The article was
       NOT fetched and read in full.** Authors, journal, year, PMID and the percentage and hazard-ratio
       figures are reported as retrieved and were consistent across three independent summaries.]
    3. Little, J.D.C. (1961), "A Proof for the Queuing Formula L = λW," *Operations Research* 9(3), with
       Hopp, W. & Spearman, M., *Factory Physics* (ρ>1 implies unbounded backlog). — **The support for
       clause (C5), and it is already held.** Where arrival rate exceeds service rate the queue grows
       without bound, and the average time in system rises with it — so a standing queue with a fixed
       re-trigger cadence and an unchanged service rate is not a holding pattern, it is a divergence.
       [REGISTER-HELD — these are PREMISE-095's own supporting citations, recorded 2026-07-09 with
       empirical run logs (arrival ~55/week against burns of 7-20/run; backlog 116 and monotone). NOT
       re-verified this run and counted as reinforcing, not independent. Per PREMISE-120, a second
       citation by a second agent is not a second measurement.]
    4. Delay-time modelling and inspection-interval optimisation (Christer and successors), and IEC
       61508's PROOF-TEST INTERVAL. — **The support for clause (C4)'s second half: an interval is a
       computed quantity.** In both traditions the interval is derived from a hazard model plus a cost
       ratio between inspection cost and the cost of an undetected defect; IEC 61508's form makes
       detection latency approximately half the interval, and where coverage is below 100% the latent-
       failure probability accumulates REGARDLESS of the interval — i.e. shortening the clock does not
       substitute for changing the method. Applied to 824: advancing 151 items by seven days changes the
       latency term and nothing else, and if the yield is zero the latency term was never the binding
       one.
       [MIXED — the IEC 61508 proof-test/diagnostic-coverage material was located and read at
       retrieved-summary level this run (GT Engineering; Risknowlogy; a ScienceDirect paper on proof-test
       interval and coverage) and is also SNIPPET-LEVEL register-held via PREMISE-169. **Christer's
       delay-time work was NOT retrieved this run and is cited from established knowledge only.**]
    5. Alert-fatigue and rubber-stamping evidence, via PREMISE-154. — Named because it is the register's
       own reason for preferring a trigger to a clock, and because it converts 824 from a waste argument
       into a HARM argument: a recurring prompt across many queues is predicted to become a rubber stamp
       within a few cycles, and a rubber stamp does not merely fail to check — it **manufactures a
       record of having checked**, which is worse than the absence of a check because it is consumed
       downstream as evidence.
       [REGISTER-HELD via PREMISE-154 (2026-08-13), whose 15b line supplied it. NOT re-retrieved.]

  Strength of support: **Strong** on (C1), (C2) and (C3); **Moderate-to-Strong** on (C4); **Moderate**
    on (C5) as an independent finding, though it is Strong as a register-held result.
    (C1)/(C2) rest on the single largest empirical programme on this question, but reached only through
    secondary sources with mutually inconsistent numbers, so the CONCLUSION is strongly supported while
    no FIGURE from it is safe to carry. (C4) rests on one well-identified quantitative study whose
    figures were consistent across independent summaries. (C5) is downgraded because both its sources
    are register-held rather than newly retrieved.

  Summary: The corrective proposition is well supported, and the register already holds it in binding
  form. The maintenance literature is the strongest evidence available in any domain: reliability-
  centred maintenance exists because United Airlines found that the large majority of failure modes are
  not age-related, so calendar-driven intervention addresses a minority pattern — and, in the
  infant-mortality cases, fixed-interval intervention actively reduces reliability rather than merely
  wasting effort. Systematic-review updating supplies the quantitative form of the same point in a
  domain much closer to C2A2's: signals for updating arrive on a hazard that varies by topic by a factor
  of nearly three, and 7% of reviews were already stale on the day they were published — so
  time-since-last-check is not even the right clock, which is precisely ASSUMPTION-1117's "the variable
  is the search, not the time." Where an interval is nonetheless used, both the delay-time and the
  functional-safety traditions treat it as a DERIVED quantity computed from a hazard model and a cost
  ratio; an interval that is carried forward because it was there yesterday is an undeclared parameter.
  On the cost side, PREMISE-095 already carries the arithmetic showing this queue diverges under current
  provisioning, and PREMISE-154 already carries the finding that a repeated re-check prompt becomes a
  rubber stamp — which means the standing schedule is not neutral: it produces carrying cost and a false
  record. **The literature adds nothing the register lacks. What is missing is enforcement.**

  Caveats:
    (a) **THIS IS AN ENFORCEMENT GAP AGAINST PREMISE-154, VALIDATED FOUR DAYS BEFORE THE BEHAVIOUR IT
        FORBIDS.** The right disposition is a REVISE against the 15d design, not a mint. Per the
        2026-08-13 batch's own finding, the binding constraint on this system is propagation, not
        validation, and 824 is a second data point for that.
    (b) **CLAUSE (C1) OVER-REACHES IF READ AS "TIME CARRIES NO INFORMATION," AND THE HONEST VERSION IS
        WEAKER.** The maintenance result is about WEAR-OUT, a physical mechanism with an age-dependent
        hazard. Wiki content has no wear-out mechanism at all — but the arrival of new external sources
        is plausibly a point process, and for a point process elapsed time IS informative about expected
        arrivals. So the defensible claim is not "waiting tells you nothing" but "**waiting is a very
        weak and undifferentiated signal that is dominated by any available condition signal, and it is
        being used here as a substitute for one.**" 824 as worded invites the stronger reading.
    (c) SHOJANIA DOES NOT SAY ABOLISH THE SCHEDULE — HE SAYS DERIVE AND STRATIFY IT. The study's own
        implication is a screening horizon on the order of two years with topic-based stratification.
        Read as support for having NO cadence, it would be misused. The support is for the interval
        being a computed, stratified quantity with a stated basis.
    (d) **NONE OF THE FIGURES IN SOURCE 1 IS SAFE TO CARRY** (see the citation-hygiene warning). Three
        mutually inconsistent age-related fractions were retrieved in a single search, from
        predominantly vendor sources. This is precisely the fabrication class ASSUMPTION-1112 names —
        a real study with drifting numbers attached — and it should be treated as a live hazard, not a
        footnote.
    (e) THE ZERO-YIELD MEASUREMENT THAT MOTIVATES 824 HAS NO DENOMINATOR IN THIS FILE. ASSUMPTION-1117's
        17-of-17 is two disjoint draws; PREMISE-168 bars a yield figure published without its
        denominator, and PREMISE-101 makes the count a property of a reading. The literature supports
        the DIRECTION strongly; it cannot certify that this queue's yield is zero.
    (f) THE ALTERNATIVE HAS A COST THE ITEM DOES NOT PRICE. A trigger-bound design requires an
        observable, a reader for it, and a mechanism that fires — three artefacts that must themselves be
        maintained and that can fail silently (which is PRESUMPTION-819's whole subject). PREMISE-154's
        requirement that a release condition be named AT PLACEMENT is the cheap form; a full
        event-driven re-check pipeline is not cheap, and no located source establishes that it pays at
        this scale.

  Search scope: GOOD on the conclusion, WEAK on verification. Searched: RCM / Nowlan & Heap and
    condition-based versus time-based maintenance; systematic-review updating intervals (Shojania
    2007); inspection-interval optimisation and IEC 61508 proof-test intervals. NOT SEARCHED, and each
    would materially change this file: (i) **the PRIMARY Nowlan & Heap report (AD-A066579)**, which is
    the only way to fix the numbers in source 1 and is a known-locatable DTIC document; (ii)
    **SURVEILLANCE-INTERVAL EVIDENCE IN CANCER SCREENING** — named in the queue's angle, not touched, and
    the domain with the best randomised evidence on interval choice; (iii) **POLLING VERSUS EVENT-DRIVEN
    MONITORING** in distributed systems, also named in the angle and not touched, and the closest
    structural analogue to the 15d design; (iv) **WIP-limit and standing-queue carrying-cost literature
    beyond Little's law** (Kanban/CONWIP, cost of delay), which is the cost side the item explicitly
    asked for and which this run reached only through the register.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently NO-SUPPORT-FOUND
  for the presumption as worded. **Disposition should be a REVISE AGAINST THE 15d DESIGN CITING
  PREMISE-154 AND PREMISE-095 — NO NEW PREMISE.** Four carries:
    1. NO NEW MINT. PREMISE-154 holds the trigger-not-clock requirement as a LOAD-BEARING, NOT-OPTIONAL
       form condition, and PREMISE-095 holds the queue arithmetic. Re-minting is barred by
       PREMISE-138(1) and PREMISE-135; the register's precedent for an enforcement gap is REVISE.
    2. THE SMALLEST CORRECTIVE ACTION IS ALREADY SPECIFIED AND IS NOT A NEW DESIGN. PREMISE-154 requires
       that each hold record, at placement, its release OBSERVABLE and the party that reads it. Applied
       to the 151 carry-overs, that is a one-off backfill, not a pipeline. Items that cannot be given a
       release observable are, on 154's own reasoning, defective at placement and should be closed
       rather than advanced.
    3. **PREMISE-095's OWN RE-CHECK IS EIGHT DAYS OVERDUE (due 2026-08-09) AND SHOULD BE RUN AS PART OF
       THIS DISPOSITION.** The premise that says this queue diverges is itself sitting in the queue it
       describes. That is the item's thesis instantiated on the register, it is checkable today, and it
       is the single most informative action available on this item.
    4. DO NOT ADOPT THE STRONG READING (caveat b). The supportable claim is that a clock is a weak
       signal dominated by any available condition signal — not that elapsed time is uninformative.
       Adopting the strong form would license removing cadence entirely, which neither Shojania nor the
       RCM literature supports and which would replace a low-yield check with no check.

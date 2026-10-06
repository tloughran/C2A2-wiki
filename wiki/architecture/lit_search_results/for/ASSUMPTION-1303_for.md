SEARCH-FOR-ASSUMPTION-1303:
  Date searched: 2026-09-10
  Original item: ASSUMPTION-1303
  Original statement: A gate whose actionable rate is around 2% (418 hits, single-digit actionable) is
    a gate that will stop being read, and the remedy is threshold amendment.
  Routed question (per the intake's Note): THE THRESHOLD QUESTION ONLY. The prior question — whether
    mtime can detect this quantity at all — is PRESUMPTION-946, is settled in-house, and PREMISE-200 is
    ACTIVE on it. I have not searched it and this file makes no claim about it.
  Two limbs, searched and reported separately:
    (L1) A gate at ~2% actionable will stop being read.
    (L2) The remedy is threshold amendment.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1303
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-09-09 measurement of a review gate returning 418 hits with a
        single-digit actionable set.
      15a: Searched for supporting literature (2026-09-10), FOR direction only. Register checked
        before searching.
    Current status: PARTIALLY-SUPPORTED — L1 SUPPORTED (Strong, with a verified named threshold);
      L2 PARTIALLY-SUPPORTED (Moderate, with a cost the literature says is usually unmeasured).

  PREMISE-REGISTER OVERLAP (checked before searching, per DEFECT-G): HEAVY on L1 — the MECHANISM is
    register-held; the NUMBER was not, and the number is what I went for.
    Grepped for: PREMISE-119, 121, 183; alarm fatigue, alert fatigue, desensitisation, positive
    predictive value, false positive rate, threshold.
    - PREMISE-121 (ACTIVE, Moderate) is the governing statement of L1 and it already holds the
      mechanism with its evidence base explicitly bounded: "In the best-measured operational analogue,
      review-queue acceptance is a function of workload and cumulative exposure rather than item merit:
      override rates run 49-96%, acceptance falls as volume and complexity rise, and desensitisation
      GENERALISES — true positives are discounted alongside false ones." Citing Ancker et al. (2017),
      BMC Med Inform Decis Mak, PMC5387195, and Nanji et al., PMID 24166725. It also carries the
      STRUCK sources (Danziger et al. 2011; ego depletion) so they are not re-argued. Its load-bearing
      clause — VALUE-WEIGHTED TRIAGE, "degradation tracks LOW-INFORMATION items specifically" — is
      directly relevant to L2 and points at a different remedy from threshold amendment.
    - PREMISE-183's Challenges section already holds the clinical non-actionable range (85%-99.4%) and
      already states the correct scope limit on it: "cited for the MECHANISM, not as a rate for a text
      pipeline." I have honoured that limit here.
    - PREMISE-119 (ACTIVE, Moderate-High) holds the queue side and supplies a SEQUENCING REQUIREMENT
      that binds this item: "establish that the service rate is greater than zero, and whether the
      consumer is SATURATED or ABSENT, before designing any admission policy." An amended threshold is
      an admission policy. If nobody is reading the 418 hits now, the gate has already stopped being
      read and L1 is not a prediction but a description — which changes the remedy.
    ASSESSMENT: L1's mechanism is REGISTER-HELD at PREMISE-121 and PREMISE-138 bars re-minting it.
    NARROWING APPLIED: I did not re-derive the CDS override literature. I searched only (i) whether any
    source states a NUMERICAL false-positive / actionable-rate threshold at which a warning channel is
    abandoned, which the register does not hold, and (ii) whether threshold amendment has a MEASURED
    effect, which the register also does not hold.

  Supporting evidence found: Yes for L1; Partial for L2.

  Sources:
    1. Bessey, A., Block, K., Chelf, B., Chou, A., Fulton, B., Hallem, S., Henri-Gros, C., Kamsky, A.,
       McPeak, S. & Engler, D. (2010), "A few billion lines of code later: using static analysis to
       find bugs in the real world," Communications of the ACM 53(2):66-75, doi:10.1145/1646353.1646374.
       [VERIFIED — FULL PDF FETCHED AND THE PASSAGES BELOW READ VERBATIM THIS RUN. This is the only
       primary-source verification in the item and it is the source the result rests on.]
       — THE ANSWER TO L1, AND IT SUPPLIES THE NUMBER THE ROUTED QUESTION ASKED FOR. Verbatim:
       "False positives do matter. In our experience, more than 30% easily cause problems. People
       ignore the tool. True bugs get lost in the false. A vicious cycle starts where low trust causes
       complex bugs to be labeled false positives, leading to yet lower trust."
       And on the operating target: "We aim for below 20% for 'stable' checkers. When forced to choose
       between more bugs or fewer false positives we typically choose the latter."
       And on the shape of the failure: "Talking about 'false positive rate' is simplistic since false
       positives are not all equal. The initial reports matter inordinately; if the first N reports are
       false positives (N = 3?), people tend to utter variants on 'This tool sucks.'"
       WEIGHT: STRONG for L1, and the margin is not marginal. The named breakdown point is 30% false
       positives; a gate at ~2% actionable is at ~98% false positives, more than three times past it.
       The vendor's own commercial operating target is below 20%. This is field experience across
       billions of lines and hundreds of customers, reported by the tool authors in a peer-reviewed
       venue, and it is the closest domain analogue the estate has: an automated warning channel over
       a text corpus, read by an expert who can walk away.
       SECOND FINDING FROM THE SAME PAGE, AND IT CUTS AT L2: "We initially thought false positives
       could be eliminated through technology. Because of this dynamic we no longer think so." The
       dynamic in question is the trust spiral — once trust is low, real bugs get relabelled false.
       That is a statement that threshold amendment does not fully undo the damage already done, which
       matters here because the estate's gate has already run at 2% for at least one measured cycle.
    2. Paine, C.W., Goel, V.V., Ely, E., Stave, C.D., Stemler, S., Zander, M. & Bonafide, C.P. (2016),
       "Systematic Review of Physiologic Monitor Alarm Characteristics and Pragmatic Interventions to
       Reduce Alarm Frequency," Journal of Hospital Medicine 11(2):136-144, doi:10.1002/jhm.2520.
       [PARTIALLY VERIFIED — I fetched and scraped the PMC author-manuscript (PMC4778561) this run and
       read the title, the framing sentences and one results-table cell verbatim. The full body did not
       render in my scrape and I did NOT read the review's methods or its per-study results. Figures
       below are marked individually.]
       — THE ANSWER TO L2, AND IT IS A REAL ONE. Verbatim from the scraped text, on a threshold change:
       an alarm limit of "85% instead of the standard 90% resulted in 61% fewer" alarms [READ VERBATIM,
       table cell]. From the review's own conclusions, at search-summary level and NOT verified in the
       body: "Widening alarm parameters, instituting alarm delays, and using disposable
       electrocardiographic wires or frequently changed electrocardiographic electrodes are the most
       promising interventions for reducing alarms," and "all studies measuring nonactionable alarms
       reported decreases."
       WEIGHT: Moderate-to-Strong for L2. This is a systematic review in a peer-reviewed journal whose
       headline conclusion is that THRESHOLD AMENDMENT (widening parameters, adding delays) is the
       most promising class of remedy for exactly this failure. It is the best direct support the item
       has for its remedy clause.
       THE QUALIFIER THAT MUST TRAVEL WITH IT, and it is the review's own: "only 5 of 8 intervention
       studies measured intervention safety" [search-summary level, NOT verified in the body]. The
       cost of raising a threshold is missed true positives, and by the review's own account that cost
       was unmeasured in most of the studies demonstrating the benefit. Amending a threshold is
       trading sensitivity for specificity; the literature has measured one side of that trade well
       and the other side badly.
    3. Alarm-delay effect sizes: a 15-second delay reported to reduce false-positive alarms by 60%; a
       14-second ICU delay by 50%; a 19-second delay by 67%.
       [SNIPPET-LEVEL ONLY, AND I AM FLAGGING IT. These came from search summaries of ICU
       alarm-reduction reviews. I did not identify the underlying primary studies and did not open any
       of them. DO NOT QUOTE THESE ONWARD AS FINDINGS.] — Recorded only because they are consistent
       in direction and magnitude with source 2 and because the DELAY mechanism (require a condition to
       persist before it fires) is a form of threshold amendment the estate could apply cheaply — the
       direct analogue being to require an mtime-derived hit to persist across two runs before it is
       reported. WEIGHT: None as evidence. Direction: for L2.
    4. Static-analysis adoption literature, secondary. [SEARCH-SUMMARY AND SECONDARY-SOURCE LEVEL.
       Includes an IEEE TSE survey ("Mitigating False Positive Static Analysis Warnings: Progress,
       Challenges, and Opportunities," doi:10.1109/TSE.2023.3329667 — TITLE AND VENUE CONFIRMED,
       CONTENT NOT READ) and a reported user-study finding that "developers expect a false-positive
       rate below 20% and the ability to configure the tool" whose primary source I could NOT trace.]
       — Also reported and untraced: that false positives ACCUMULATE over time because developers fix
       real defects and leave false positives in place, so an unamended gate's actionable rate falls
       monotonically. WEIGHT: Weak. Direction: for both limbs. The 20% figure independently echoes
       Bessey's verified "below 20% for stable checkers" target, which is mild corroboration of the
       ORDER OF MAGNITUDE and nothing more.
    5. Register-held and not re-searched: PREMISE-121's desensitisation-generalises finding. It is what
       makes L1 consequential rather than merely annoying — the estate does not just lose the 98%, it
       loses confidence in the 2%. It is also the reason the remedy cannot be "read it anyway."

  Strength of support: Strong for L1. Moderate for L2, with a named unmeasured cost.

  Summary: L1 is supported about as well as a claim of this kind can be. Bessey et al., verified at
  full text this run, name 30% false positives as the point at which "people ignore the tool" and
  describe the resulting trust spiral in which true bugs get relabelled false; their own commercial
  target is below 20%. A gate at 2% actionable sits at roughly 98% false positives — more than three
  times past the named breakdown point and five times past the operating target — in the closest
  available domain analogue. The estate's own PREMISE-121 already supplies the mechanism and the
  aggravating finding that desensitisation generalises to true positives. L2 is supported more weakly
  and more interestingly. Paine et al.'s systematic review does conclude that widening parameters and
  instituting delays are the most promising interventions, with a verified instance of a single
  threshold change producing 61% fewer alarms; that is real support for threshold amendment as a
  remedy class. But two qualifiers travel with it. First, by the review's own account most of the
  studies demonstrating the benefit did not measure the safety cost — the missed true positives — so
  the trade is evidenced on one side only. Second, Bessey et al. report explicitly that they abandoned
  the belief that false positives could be engineered away, because the trust damage outlasts the
  tuning. Set against PREMISE-119's sequencing requirement, that suggests the estate should establish
  whether the gate is currently being read AT ALL before amending its threshold: if service is already
  zero, an amended threshold is an admission policy applied to an absent consumer, which PREMISE-119
  already rules out.

  Caveats:
  (a) L2 IS THE WEAKER LIMB AND THE ITEM STATES IT AS THOUGH IT WERE THE SETTLED ONE. "The remedy is
      threshold amendment" is one remedy class among at least three the literature contains — the
      others being value-weighted triage (PREMISE-121's load-bearing clause) and removing the gate.
      Nothing I found compares them.
  (b) DOMAIN TRANSFER IS GOOD FOR SOURCE 1 AND WEAK FOR SOURCE 2. Bessey's setting is a text-corpus
      analyser read by an engineer, which is very close to the estate's case. The clinical alarm
      literature is a real-time physiological monitor with a patient at the other end; PREMISE-183
      already ruled that this literature is cited for MECHANISM, not for rates, and that ruling binds
      the 61% figure too — it is evidence that threshold changes move alarm volume, not a
      transferable magnitude.
  (c) NO SOURCE ADDRESSES THE ESTATE'S ACTUAL DECISION. Neither direction of the literature answers
      "given a gate already observed at 2% actionable, does amending the threshold restore readership."
      Source 1 says trust damage persists; source 2 measures volume, not readership. That is a real
      gap and the estate can close it cheaply: after any amendment, measure whether the hits are
      subsequently opened, not whether there are fewer of them.
  (d) SELF-REPORT IN SOURCE 1. Bessey et al. is a vendor's retrospective on its own product. It is
      candid to the point of being unflattering, which raises rather than lowers my confidence, but
      PREMISE-195 governs self-reported figures and the 30% is a self-reported operational judgement,
      not a measured breakpoint. It is stated as "in our experience."
  (e) SEARCH SCOPE: MODERATE — three query families (static-analysis false-positive adoption; clinical
      alarm PPV and thresholds; alarm-reduction intervention reviews), one of which was pursued to full
      text. NOT REACHED: the SRE/on-call alerting literature on actionable-alert ratios (Google SRE
      Chapter 6 has doctrine here); signal-detection-theory treatments of optimal operator cutoffs,
      which is where a principled PPV floor would actually be derived; and the IDS/SIEM false-positive
      literature, which has the largest false-positive rates on record and would test whether 98% is
      survivable anywhere.

  Recommendation: PARTIALLY-SUPPORTED
    (L1: SUPPORTED, Strong. A verified named threshold at 30% false positives, with the estate's gate
     more than three times past it, in the closest domain analogue.
     L2: PARTIALLY-SUPPORTED, Moderate. Threshold amendment is the literature's most-endorsed remedy
     class and has measured effects on volume; its safety cost is unmeasured in most of the same
     studies, and the one verified source denies that tuning undoes the trust damage.
     Overall strength: Strong / Moderate split.)

  NOVELTY-FLAG: NOT RAISED for either limb. The claim is well covered and the estate's gate is far
    outside the range any source treats as viable.

  DISPOSITION STEER FOR 15c: L1 is worth carrying as a NUMBER attached to PREMISE-121 rather than as a
    new premise — the register currently holds the mechanism with no threshold, and "30% false
    positives is where the channel is abandoned; below 20% is the operating target" is the missing
    quantity, verified at primary source. L2 should NOT be adopted as stated. If it is adopted at all
    it must carry PREMISE-119's sequencing requirement in front of it (measure whether the gate is
    read before amending it) and the unmeasured-safety-cost qualifier, and the post-amendment success
    criterion must be READERSHIP, not hit count.

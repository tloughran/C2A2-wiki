SEARCH-FOR-PRESUMPTION-817:
  Date searched: 2026-08-16
  Original item: PRESUMPTION-817
  Original statement: [inferred] That the nightly changelog is a record rather than a hypothesis; no
    register has a field for a finding withdrawn.
  Risk if wrong: High
  Search question (as queued): Retraction and correction rates as quality indicators; calibration of
    claim confidence; base-rate neglect in incident narratives.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE belief. The
  proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses:
    (C1) THE CONTENTS OF A KNOWLEDGE BASE ARE BELIEFS, NOT FACTS, AND THE DISCIPLINE THAT STUDIES SUCH
         SYSTEMS SAYS SO IN ITS OWN VOCABULARY. "Record" is the wrong word for a store whose entries are
         defeasible; "hypothesis" is closer, and the field has spent forty years working out what
         follows.
    (C2) A STORE OF DEFEASIBLE CONTENT REQUIRES WITHDRAWAL AS A FIRST-CLASS, FORMALLY SPECIFIED
         OPERATION — not as an occasional edit. In the AGM framework, contraction is one of the three
         primitive operations and revision is DEFINED as contraction followed by expansion, so a system
         with no contraction cannot revise at all, only accumulate.
    (C3) WITHDRAWAL WITHOUT DEPENDENCY TRACKING IS NOT WITHDRAWAL. Removing an assertion obliges removing
         what was derived from it; the standard task list for such a system includes "given an
         assumption, find the assertions derived from it" and "delete an assertion and all assertions
         derived from it." A register with no withdrawal field has neither task and therefore cannot
         know what a withdrawn finding took with it.
    (C4) A RETRACTION COUNT IS A CONFOUNDED QUALITY INDICATOR AND A ZERO IS UNINFORMATIVE. Retraction
         rate tracks scrutiny at least as much as error, so a register reporting no withdrawals is not
         thereby reporting accuracy — it may simply have no mechanism by which a withdrawal could be
         expressed.
  "SUPPORTED" below means 14b's diagnosis is well grounded, and is equivalently evidence AGAINST the
  presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-817
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: the pipeline applied its own
      test to its own output and found the schema, not the content, at fault)
    Transform at each step:
      14b: Applied REVISE-335's frame-independence test to 14a/14b's own output.
      15a: Searched for supporting literature on the corrective proposition; register check first.
    Current status: SUPPORTED

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: retract, withdraw, correction, corrigend, amend, changelog,
    provisional, hypothes, calibrat, base rate, base-rate, overconfiden, confidence label, revision.
    Found and read in full:
      - **PREMISE-143** (2026-08-05, ACTIVE, Moderate) — **the heaviest overlap and the entry any
        disposition must be measured against.** "A RETRACTION COUNT IS A MEASURE OF THE PRODUCING LAYER,
        NOT OF THE CATCHING LAYER, AND CORRECTING AN OUTPUT DOES NOT TERMINATE THE ERROR EVEN FOR THAT
        OUTPUT." Clause (2): "**14.8-24.4% of sampled post-release fixes in four operating systems were
        themselves incorrect and reached users (Yin et al. 2011). A correction issued and unreviewed
        carries a one-in-five-to-one-in-seven prior of being wrong.**" Clause (3) is the closest thing
        the register has to 817's schema claim: "**THE RECORD MUST SPLIT: every retraction produces TWO
        items with independent lifecycles — a corrected-output record, and an instrument-defect record
        that OUTLIVES the run that filed it and is NOT CLOSABLE BY THAT RUN.**" Its 15b steelman, which
        is PARTIALLY SUSTAINED in the premise, must travel with any use of 817: **public self-retraction
        is a genuine asset and this premise must not be cited to discourage it.**
      - **PREMISE-117** (2026-07-21, ACTIVE, Moderate-High) — publish-then-revise is codified practice;
        figures carry a REVISION FLAG; withdrawal is reserved for statistics not fit for purpose; **the
        defect is silence, not continuation**; a pre-committed corrections policy is required. This is
        the official-statistics answer to 817's schema question and it names the missing field —
        a revision flag — in a different vocabulary.
      - **PREMISE-118** (2026-07-21, ACTIVE, Moderate-High) — naming a defect triggers contain / assess
        impact / fix cause / verify, INCLUDING a retrospective impact assessment over every result since
        last known-good. Its clause (i) is the discipline of 817's clause (C3): the obligation is
        ASSESSMENT of what the defect touched, not automatic invalidation. Its SELF-APPLICATION note
        records that the premise was violated by the run that validated it.
      - **PREMISE-124** (ACTIVE) — self-measurement must cite an external baseline or be reported
        UNCALIBRATED; **FORBIDDEN MOVE: reading a single favorable self-observation as evidence a
        safeguard "works" (WYSIATI / base-rate neglect)**. This is the register already holding the
        third element of 817's queued search question.
      - **PREMISE-105** (2026-07-20, ACTIVE) — a definitional change breaks a series; correction is the
        standard and marking the fallback (Eurostat backcasting). The temporal-record form.
      - **PREMISE-103** (ACTIVE) — absence of primary text is a KIND-difference in evidence, not a
        degree-difference: "**no confidence label over metadata-only material is well-founded, and
        downgrading confidence is not a valid substitute for an explicit 'unfounded pending retrieval'
        state.**" This is 817's clause (C2) in miniature — the register has already established, in one
        domain, that a MISSING STATE cannot be simulated by adjusting a number.
      - **PREMISE-129** (ACTIVE) — an agent's stated verdict is a CLAIM, not a determination; LLM
        self-report is poorly calibrated and high confidence frequently accompanies wrong answers.
      - **PREMISE-126** (ACTIVE) — recency is not re-confirmation; a re-check that only advances a date
        certifies "not-yet-expired."
      - **PREMISE-151** (2026-08-10, ACTIVE) — repeated disclosure of an unremediated condition
        normalises rather than resolves it.
      - **PREMISE-135** (2026-08-14, ACTIVE) — terminality is purchased by enumerating the domain, not
        by accumulating instances; a correction may not be declared "the general case" on the strength
        of covering every instance seen so far. Directly relevant: a changelog entry is such a claim.
    CONCLUSION OF THE CHECK: **HEAVY OVERLAP ON THE RETRACTION QUESTION; A GENUINE GAP ON THE SCHEMA
    QUESTION. NO NOVELTY-FLAG, but the closest call of this batch.** Ten ACTIVE premises bear on this.
    PREMISE-143 holds the retraction-count claim, PREMISE-117 holds the publish-then-revise norm,
    PREMISE-118 holds the impact-assessment obligation, and PREMISE-124 holds the base-rate clause. What
    NO premise holds is:
      (R1) **THE SCHEMA CLAIM AS A CLAIM ABOUT REPRESENTABILITY.** PREMISE-143(3) says the record must
           SPLIT into two items; it does not say that neither item has a place to live. 817's finding is
           narrower and harder: **there is no field**, so a withdrawal is not merely unperformed but
           INEXPRESSIBLE. That is the same structural defect PREMISE-167 identified for escalations ("an
           escalation expressed only as a WITHHELD PASS-MARK has no representation on disk distinct from
           staleness") and PREMISE-103 identified for unfounded claims — and it has now appeared a third
           time, in a third register, which under PREMISE-130's recurrence rule may itself be the finding.
      (R2) **THE THEORETICAL GROUNDING IS ENTIRELY ABSENT FROM THE REGISTER.** No premise cites belief
           revision, truth maintenance, contraction, or dependency-directed retraction. That literature
           says something the register nowhere says: withdrawal is not a feature but a PRIMITIVE, and a
           store lacking it cannot revise, only accumulate.
    DECLARED LIMITATION: string grep, measured at ~56% recall (ASSUMPTION-1052). The list above is a
    **LOWER BOUND**; with ten hits the true overlap is likely larger.

  Supporting evidence found: Yes

  Sources:
    1. Shapiro, S.C. (1998), "Belief Revision and Truth Maintenance Systems: An Overview and a
       Proposal," SUNY Buffalo CSE Technical Report 98-10. — **The decisive support for clauses (C1),
       (C2) and (C3), and the source of the vocabulary 817 most needs and C2A2 entirely lacks.**
       On (C1), the paper's second page states the point 817 is making, about knowledge-based systems in
       general: "**Although the terms 'truth', 'fact', and 'knowledge' are used, no KBS can guarantee
       that any assertion it contains is true, and therefore a fact in the strict sense of that term,
       nor that any set of them constitutes knowledge. 'BELIEF' WOULD BE A MORE ACCURATE TERM THAN
       'KNOWLEDGE', and this is why some researchers prefer 'belief revision' to 'truth maintenance.'**"
       It further enumerates why such a system NEEDS revision, and two of the three reasons are C2A2's
       exactly: assertions entered from multiple sources that may contradict one another, and "old
       assertions might be retracted either because the world which it is about has changed, **or
       because the source of the assertion no longer wants it in the KB**."
       On (C2), the AGM section states the three primitive operations — expansion (adding), CONTRACTION
       (removing an assertion), and revision (adding something inconsistent with the base and restoring
       consistency) — and then the structural claim: "**Revision can be accomplished by a step of
       contraction followed by a step of expansion.**" A register with no withdrawal operation therefore
       has expansion only, and by this decomposition **cannot perform revision at all** — which is 817's
       point stated as a formal deficiency rather than a housekeeping complaint. It also supplies the two
       AGM constraints that would govern any implementation: minimise information lost, and retract the
       least entrenched.
       On (C3), the paper gives the standard task list every belief-revision system must support: "1.
       Given an assertion, find the assertions used to derive the given one. 2. **Given an assumption,
       find the assertions derived from it.** 3. **Delete an assertion and all assertions derived from it
       from the KB.**" C2A2's registers support task 1 partially (via PROVENANCE chains) and support
       tasks 2 and 3 not at all. The paper also names the failure mode of the naive alternative:
       chronological backtracking — undoing the most recent things first because you cannot tell what
       depended on what — which is "clearly inefficient" and was the problem the whole field was
       launched to solve.
       [VERIFIED this run — the PDF was fetched and read in full (10 pages including the reference
       list). Every quotation above is read directly. It is a TECHNICAL REPORT and a high-level overview,
       not a peer-reviewed research contribution; its value here is as an accurate, citable summary of
       two mature literatures, and it names the primaries it summarises.]
    2. Alchourrón, C.E., Gärdenfors, P. & Makinson, D. (1985), "On the logic of theory change: Partial
       meet contraction and revision functions," *The Journal of Symbolic Logic* 50(2):510-530. — The
       founding AGM paper, and the primary behind clause (C2). Contraction is one of its two named
       operations in the title.
       [SNIPPET LEVEL — the full citation was read this run from source 1's verified reference list, and
       the paper's role is described in source 1's body. **The paper itself was NOT retrieved or read.**
       Author list, title, journal, volume, issue, year and page range are confirmed from a verified
       secondary; nothing beyond its existence and its subject should be asserted.]
    3. Doyle, J. (1979), "A truth maintenance system," *Artificial Intelligence* 12(3):231-272. — The
       primary behind clause (C3): the first domain-independent justification-based TMS, in which each
       inferred assertion records the assertions that justify it, so that retraction can propagate along
       the dependency graph rather than by date order. The register's PROVENANCE chains are a
       justification structure that is written but never traversed.
       [SNIPPET LEVEL — full citation read from source 1's verified reference list; the JTMS mechanism
       (nodes, justifications, in/out labels, propagation on retraction) is described in source 1's body
       and is read from there. **Doyle's paper itself was NOT retrieved.**]
    4. Retraction and correction rates as quality indicators — Bar-Ilan & Halevi and the associated
       bibliometric literature; the PMC-hosted study "Journal Retraction Rates and Citation Metrics: An
       Ouroboric Association?" (PMC7748576); "Self-correction in biomedical publications and the
       scientific impact" (PMC3944419). — **The support for clause (C4), and it is the clause most
       likely to be misread, so the finding is stated carefully.** The retrieved position is that
       retraction "reflects the self-correcting nature of science," but that the rate is **CONFOUNDED
       WITH SCRUTINY**: highly cited journals retract MORE than lower-cited ones, partly because their
       papers "are read more widely and scrutinised more extensively" and are more likely to prompt
       replication. One study reports retraction rate NOT correlating with citation metrics in the
       expected direction. The consequence for 817 is the important one: **a low or zero retraction count
       is not evidence of accuracy — it is equally consistent with an absence of scrutiny, or, as 817
       claims, with an absence of any mechanism by which a retraction could be recorded.** This is the
       same polarity defect PREMISE-110 identifies in detectors and PREMISE-143 relocates to a count,
       arriving from the bibliometric side.
       [SNIPPET LEVEL — the PMC listings and abstracts were located this run and the findings read from
       retrieved summaries; **no paper was opened.** Titles, hosts and PMC identifiers are confirmed.
       Do not quote a figure or a page. NOTE: a further retrieved item, a pilot rubric for retraction-
       notice QUALITY (Taylor & Francis, *Accountability in Research*, 2024), is the closest located
       work to "what a withdrawal record should contain" and was NOT reached — see search scope.]
    5. ISO 9001:2015 clause 10.2's split between a CORRECTION (fix the output) and a CORRECTIVE ACTION
       (fix the cause, and verify effectiveness); ISO/IEC 17025 clauses 7.10 and 8.7 on nonconforming
       work. — The quality-systems form of the two-lifecycle requirement, and the standard that already
       supplies the missing schema: a nonconformance record and a corrective-action record are distinct
       objects with distinct closure criteria.
       [CANONICAL — cited from established knowledge, and **already register-cited** via PREMISE-143
       (ISO 10.2) and PREMISE-118 (ISO/IEC 17025). NOT re-verified this run and NOT independent evidence.]
    6. Kahneman, D. (2011), *Thinking, Fast and Slow* — WYSIATI and base-rate neglect. — Named because
       the queue asked for base-rate neglect in incident narratives. **No source specifically on
       base-rate neglect IN INCIDENT NARRATIVES was located this run**; the general result is canonical
       and is already register-held in PREMISE-124's FORBIDDEN MOVE clause.
       [CANONICAL — NOT re-verified this run; register-carried, therefore not independent.]

  Strength of support: **Strong** on (C1)-(C3); **Moderate** on (C4).
    (C1)-(C3) rest on a verified reading of an accurate overview of two mature formal literatures, where
    the relevant claims are definitional rather than empirical: contraction is a primitive of the AGM
    framework, revision decomposes into contraction plus expansion, and dependency traversal is on the
    standard task list. These are not findings that can fail to replicate. (C4) is Moderate because the
    bibliometric sources were read at abstract level only and because the confounding claim, while
    consistently reported, is an interpretation of correlational data.

  Summary: The corrective proposition is strongly supported, and the supporting discipline states 817's
  first clause almost word for word. Shapiro's overview opens by insisting that no knowledge-based
  system can guarantee any assertion it holds is true, and that "belief" is the more accurate term than
  "knowledge" — which is exactly 14b's point that the nightly changelog is a hypothesis wearing the
  grammar of a record. The formal consequence is sharper than the item claims. In the AGM framework
  there are three primitive operations, one of them is contraction, and revision is DEFINED as
  contraction followed by expansion; a register that supports only expansion therefore cannot revise at
  all, only accumulate, and its growth curve is not a measure of learning. The truth-maintenance
  tradition adds the operational half: the standard task list requires that a system be able to find
  what was derived from an assumption and to delete an assertion together with everything derived from
  it, and the failure mode of not having this is chronological backtracking — undoing things in date
  order because dependency is unrecorded — which is the problem the entire field was created to solve.
  C2A2 writes PROVENANCE chains, which is a justification structure, and never traverses them. The
  bibliometric literature supplies the last piece and inverts the reassuring reading: retraction rate is
  confounded with scrutiny, with highly cited journals retracting more precisely because they are read
  more, so a register reporting no withdrawals reports nothing about its accuracy — which is 817's claim
  that the absence of the field is invisible because its absence produces a clean number. Where this
  file must stop short of the item is that the register already holds the retraction-count claim as
  PREMISE-143, the publish-then-revise norm as PREMISE-117, and the impact-assessment obligation as
  PREMISE-118. What it does not hold is the representability claim — that a withdrawal is not merely
  unperformed but inexpressible — and the formal grounding for why that matters.

  Caveats:
    (a) PREMISE-143'S STEELMAN BINDS AND MUST TRAVEL WITH ANY USE OF THIS ITEM. The register records,
        as partially sustained, that "**public self-retraction is a genuine asset and this premise must
        not be cited to discourage it.**" 817 must not become a reason to file fewer corrections. What is
        at issue is a missing FIELD, not an excess of withdrawals — and if anything the correct
        prediction is that adding the field would increase the recorded rate, which under clause (C4)
        would be a sign of function rather than of decay.
    (b) THE DOMAIN TRANSFER FROM FORMAL BELIEF REVISION IS REAL BUT PARTIAL, AND THE MISMATCH IS
        SPECIFIC. AGM assumes a logically closed belief set over a well-defined logic with sound
        inference; TMS assumes propositional justifications recorded at inference time. C2A2's registers
        are natural-language findings with prose provenance notes and no formal entailment relation, so
        **no AGM operator can be implemented over them as they stand and nothing here licenses a claim
        that one could be.** What transfers robustly is the STRUCTURAL requirement — a first-class
        withdrawal state, and a recorded dependency edge from a finding to what was built on it — which
        is representable in a markdown register at negligible cost. What does not transfer is the
        machinery: no partial-meet contraction, no entrenchment ordering, no automatic propagation.
    (c) THE PROBLEM 817 NAMES HAS A KNOWN HARD PART AND THE LITERATURE ADMITS IT. Source 1 is explicit
        that finding the possible culprits is solved and **choosing among them is "much less clear"** —
        SNeBR simply presents all candidates to the user. So a withdrawal field plus dependency edges
        would surface the question "what else must go?" without answering it, and the answer would land
        on a review channel already known to have near-zero throughput (PREMISE-119, PREMISE-102). That
        is a real cost of the remedy and should be stated before it is adopted, not after.
    (d) THE THIRD-INSTANCE OBSERVATION IN (R1) IS AN INFERENCE OF THIS FILE AND IS NOT ESTABLISHED. The
        claim that "no representable state" has now appeared three times (PREMISE-103's unfounded-pending-
        retrieval, PREMISE-167's escalation-versus-staleness, and 817's withdrawn-finding) is drawn from
        reading the register, not from a source, and PREMISE-130's threshold requires **three distinct
        signatures in one component**, which three different registers may or may not satisfy. It is
        offered as a lead, explicitly not as a met threshold, and PREMISE-135 forbids treating the
        pattern as terminal on three instances.
    (e) SOURCE INDEPENDENCE IS LOWER THAN THE COUNT SUGGESTS AND MUST BE DISCLOSED PER PREMISE-120.
        Sources 2 and 3 are known to this file ONLY through source 1; they are not independent
        confirmations, they are source 1's own references. Sources 5 and 6 are register-carried and
        add no new weight. The genuinely independent external evidence here is TWO lines: the
        belief-revision overview, and the bibliometric retraction studies.
    (f) THE ITEM'S SELF-APPLICATION IS ITS STRONGEST FEATURE AND ALSO ITS RISK. 14b applied REVISE-335's
        frame-independence test to 14a/14b's own output, which is the reflexive discipline PREMISE-144
        requires of a governing layer. But per PREMISE-124 a self-measurement without an external
        baseline is UNCALIBRATED, and this file did not obtain one: **no count of how many prior findings
        would have been withdrawn had the field existed was made, by 14b or by this search.** Without
        that, the item establishes that the field is missing and does not establish that anything was
        lost by its absence.

  Search scope: COMPREHENSIVE and VERIFIED on the formal grounding (Shapiro 1998 read in full),
    including the AGM operations, the revision decomposition, the BRS task list and the
    chronological-backtracking failure mode. GOOD at abstract level on retraction-rate confounding.
    CANONICAL and register-held on the quality-systems schema and on base-rate neglect. NOT SEARCHED,
    and each would materially change this file: (i) **the Taylor & Francis pilot rubric for RETRACTION
    NOTICE QUALITY** (*Accountability in Research*, 2024, doi 10.1080/08989621.2024.2366281), which was
    LOCATED AND NOT REACHED and is the single most directly useful missing item — it is literally a
    specification of what a withdrawal record should contain, which is what 817 says the register lacks;
    (ii) **CrossMark / CREC and the COPE retraction-guideline machinery**, i.e. the publishing industry's
    actual SCHEMA for update-and-withdrawal notices, identified as the right precedent and not retrieved;
    (iii) **base-rate neglect in incident narratives specifically** — the queue asked for it and this
    search found NOTHING on point, a clearly-labelled negative result; the general Kahneman result is
    canonical but the incident-narrative application appears unstudied in what was reachable here.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently NO-SUPPORT-FOUND
  for the presumption as worded. Four carries:
    1. THE NEW CONTENT IS (R2), THE FORMAL GROUNDING, AND IT IS WORTH HOLDING BECAUSE IT CHANGES WHAT
       THE REMEDY IS FOR. Not "we should be tidier about corrections" but "**a store with expansion and
       no contraction cannot revise, only accumulate**," which makes the register's growth curve an
       uninterpretable quantity rather than a health signal — and that is the same result PREMISE-105
       reached about definitional breaks and PREMISE-168 about yields, arriving from formal logic.
    2. THE ADOPTABLE STEP IS TWO FIELDS AND ONE EDGE, AND IT IS CHEAP. A `Status: WITHDRAWN` state
       distinct from staleness (PREMISE-167's lesson), a `Withdrawn-because:` line, and a recorded
       edge from each finding to what was built on it (Doyle's justification, which the PROVENANCE
       chains already half-write). This satisfies BRS tasks 2 and 3 at markdown cost and creates no
       metric, so it does not collide with PREMISE-109 or PREMISE-168.
    3. DO NOT BUILD A WITHDRAWAL COUNT AND READ IT AS QUALITY. Clause (C4) and PREMISE-143 agree: the
       count measures the producing layer and the scrutiny level, not the catching layer. If the field
       is added, the expected and correct outcome is that the number goes UP.
    4. THE ONE THING TO GO AND LOOK AT, AND IT IS CHEAP. Take the last thirty days of findings and ask
       how many were subsequently contradicted by a later finding without either being marked. That is
       the external baseline PREMISE-124 requires, it is obtainable with no protocol change, and without
       it 817 establishes only that the field is missing — not that anything was lost.

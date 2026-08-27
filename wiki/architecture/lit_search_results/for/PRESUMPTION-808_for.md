SEARCH-FOR-PRESUMPTION-808:
  Date searched: 2026-08-16
  Original item: PRESUMPTION-808
  Original statement: [inferred] That `[Request interrupted by user]` means a user interrupted.
  Risk if wrong: Critical.

  POLARITY NOTE — what was searched FOR. The presumption is worded as the DEFECTIVE belief ("the
  marker means what it says"). The proposition searched FOR is the CORRECTIVE CONVERSE, in four
  clauses: (i) that a TERMINATION MARKER EMITTED BY AN AUTOMATED SYSTEM IS A CLASSIFICATION PRODUCED
  BY THAT SYSTEM, NOT AN OBSERVATION OF THE CAUSE, and that the mapping from marker to cause is
  many-to-one by construction at every layer of the stack that has been looked at; (ii) that
  ATTRIBUTION OF FAULT TO THE OPERATOR IS A DIRECTIONAL BIAS IN INCIDENT CLASSIFICATION rather than a
  neutral reading — it is made ex post facto with hindsight, it terminates the investigation, and the
  safety-science consensus for twenty-five years has been that it is the START of an inquiry and not
  its conclusion; (iii) that the widely-quoted BASE RATES for operator-caused failure are themselves
  artefacts of the classification scheme, to the point that when someone went looking for the origin
  of the canonical "80% human error" figure THEY COULD NOT FIND ONE; and (iv) that the correct
  engineering response, where it has been taken, is to REPLACE THE SINGLE MARKER WITH AN ENUMERATED
  CAUSE CODE SET, which is a design change and not a discipline change. "SUPPORTED" below means 14b's
  worry is well grounded, and is equivalently evidence AGAINST the presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-808
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight per the provenance
      protocol, because the designers were unaware they were reading a label as a report)
    Transform at each step:
      14b: Inferred by asking what supports the marker's claim on a day when no human spoke.
      15a: Searched for supporting literature on the corrective proposition; performed a register
        check first; and searched specifically for a MEASURED accuracy figure for automated
        termination-cause labels, which is reported below as a clean negative.
    Current status: SUPPORTED (Moderate-Strong) — with a duplication warning, see below.

  **DUPLICATION WARNING — READ BEFORE DISPOSITION.** The register already holds this item's core
  claim in two places, one of them verbatim on this exact string.
    (a) **PREMISE-141, SCOPE LIMIT, load-bearing, minted 2026-08-05 at High confidence:** "THE CAUSE
        OF `[Request interrupted by user]` IS UNDETERMINED and 15b's steelman on this point is NOT
        defeated. This premise licenses no claim that the interruptions were faults rather than
        deliberate human stops." That is PRESUMPTION-808's subject matter, on the same string, eleven
        days earlier. NOTE THE ASYMMETRY, because it is the whole of the residual: 141's limit runs in
        the direction *do not assume it was a fault*. PRESUMPTION-808 runs in the opposite direction —
        *do not assume it was a human*. Both are consequences of one underlying fact (the marker does
        not determine the cause), but the register states only one polarity, and the fleet has spent
        eleven days reading the unstated polarity as settled.
    (b) **PREMISE-160, minted 2026-08-14 at High confidence,** whose 15a evidence names "DIAGNOSIS
        MOMENTUM (a label passed between actors hardening into fact without re-test)" and records that
        it "has no register antecedent." PRESUMPTION-808 is that mechanism's second observed
        instance, two days later, and the label in question is machine-generated rather than
        human-generated — which makes it harden faster, not slower, because no actor in the chain
        ever authored it and so no actor feels answerable for it.
  A disposition that mints a new premise here is at risk of re-minting 141's scope limit, which
  PREMISE-138(1) and PREMISE-135 bar. The defensible increment is stated under RESIDUAL below.

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: `interrupted by user`, attribut*, "operator error", "human
    error", blame, "fault assign", "self-report", termination, label, diagnos*.
    Found and read in full:
      - **PREMISE-141** (2026-08-05, ACTIVE, High) — see DUPLICATION WARNING (a). Its clause (1) also
        bears: Cristian's failure-semantics taxonomy separates OMISSION (runs, produces no response)
        from CRASH (does not run); C2A2's run model is two-valued and "each reader supplies the
        missing value from their own prior." `[Request interrupted by user]` is exactly a reader
        supplying the missing value — except that here the *runtime* supplied it, which is worse,
        because it arrives pre-attributed and therefore invites no supplying at all.
      - **PREMISE-160** (2026-08-14, ACTIVE, High) — see DUPLICATION WARNING (b). Its BINDING
        PROHIBITION transfers to any remedy proposed for 808 and must be quoted forward: Norman et
        al. (2017), Academic Medicine 92(1):23-30 — bias-based accounts of diagnostic error are
        weakly supported and bias-RECOGNITION interventions have NO measured effect, so "remind runs
        to be sceptical of the marker" is contraindicated by the strongest available synthesis. The
        supported remedy shape is a DISCRIMINATING TEST or a DATA-MODEL CHANGE, not an exhortation.
      - **PREMISE-146** (2026-08-06, ACTIVE, Moderate) — the closest STRUCTURAL match in the register
        and the one that names the actual defect. Clause (3): "TEN ATTRIBUTIONS TO THE ACTOR AND ONE
        TO THE RULE IS THE DOCUMENTED PATHOLOGY, NOT DILIGENCE." Its item-type note records "ten
        consecutive runs attributed a structural defect to themselves WITHOUT THE OPTION OF
        ATTRIBUTING IT ELSEWHERE BEING REPRESENTABLE," and its Applicable-to names "the disclosure
        format itself, which currently has no ATTRIBUTION FIELD in which 'specification' is a
        representable answer." PRESUMPTION-808 is the same defect with the attribution running the
        other way: the marker has no field in which "cause unknown" or "resource gate" is
        representable, so the only representable answer is "user."
      - **PREMISE-140** (2026-08-02, ACTIVE, High) — "A METRIC DERIVED FROM ONE OBSERVATION CHANNEL
        MUST BE NAMED BY ITS CHANNEL, NOT BY THE THING THE CHANNEL PROXIES FOR." Directly on point
        and, importantly, 808 is its extension from NUMERIC quantities to CATEGORICAL ones. The
        correct form of the marker under 140 is not "a user interrupted" but "the session terminated
        without a completion record, cause not observed by this channel."
      - **PREMISE-155** (2026-08-13, ACTIVE, Moderate) — "A name is not an identity." 808 is the
        semantic analogue: a label is not a cause. 155's clause (2), differential observability, also
        applies: nothing in the architecture ever compares what the runtime's own marker asserts
        against any independent observation of whether a human was present.
      - **PREMISE-129** (ACTIVE) — an agent's stated verdict is a CLAIM, not a determination; LLM
        self-report is empirically unreliable and poorly calibrated. The marker is a runtime
        self-report about its own termination.
      - **PREMISE-113** (ACTIVE, Moderate) — a detector's findings are evidence about the detector
        until its precision is measured. The marker is an unmeasured classifier and its precision on
        the class "user interrupted" has never been estimated in this system.
      - **PREMISE-124** (ACTIVE) — no self-measurement of the pipeline's own accuracy without an
        external baseline. Whether a human spoke is externally checkable (session transcripts, wall
        clock, Tom); nothing checks it.
      - **PREMISE-152** (ACTIVE) — homogeneous runs concurring is weak evidence in both directions.
        Several runs all carrying the same marker is one observation of one classifier, not several.
    CONCLUSION OF THE CHECK: **SUBSTANTIAL OVERLAP; ONE NEAR-DUPLICATE; NO NOVELTY-FLAG.** Nine ACTIVE
    premises bear, one of them on this literal string. The residual is stated below.
    DECLARED LIMITATION: this was a STRING GREP, measured at ~56% recall (ASSUMPTION-1052) and at
    five-of-nine on a successive run. The list above is a **LOWER BOUND** and the true overlap is
    likely larger. Nine hits argues for a NARROWER disposition, not a wider one.

  RESIDUAL — what 808 contains that the register does not:
    (R1) THE POLARITY IS NEW. PREMISE-141 bars inferring FAULT from the marker. Nothing bars
         inferring HUMAN AGENCY from it. On a day when no human spoke, the second inference is the
         one actually being made, and it is unguarded.
    (R2) THE MARKER IS MACHINE-AUTHORED, WHICH IS AN AGGRAVATOR NOT A MITIGATOR. PREMISE-160's
         diagnosis-momentum finding concerns a label passed between actors. Here no actor authored
         the label at all; it arrives from the runtime with the grammatical form of an eyewitness
         report ("a user interrupted"), and the literature located below is unanimous that this is
         precisely the form in which attributions stop being examined.
    (R3) THE REMEDY SHAPE IS DIFFERENT FROM ANYTHING FILED. Every located precedent that fixed this
         class of problem did so by REPLACING ONE MARKER WITH AN ENUMERATED CAUSE-CODE SET (see
         source 5). That is a data-model change of the same family as PREMISE-141's third terminal
         state and PREMISE-146's missing attribution field, and it is cheap.

  Supporting evidence found: Yes

  Sources:
    1. Dekker, S. (2002/2006), *The Field Guide to Understanding Human Error* (and its 2000 draft
       predecessor, *The Field Guide to Human Error Investigations*), Ashgate. — **The canonical
       statement of clause (ii).** The book's organising contrast is the OLD VIEW, in which human
       error is the cause of an incident, against the NEW VIEW, in which human error is a SYMPTOM of
       deeper trouble in the system and is "the starting point of an investigation, rather than its
       conclusion." Dekker's specific mechanism is the one that matters here: human error is an
       ATTRIBUTION ASSIGNED IN HINDSIGHT from a point of view, produced by tracing time backwards —
       start with the outcome, assume human agency, work back, identify the "bad behaviour," assign
       it. The formulation usually quoted from the 2006 edition is "human error is not an explanation
       of failure, it demands an explanation." Applied to 808: the marker is the hindsight attribution
       arriving BEFORE the investigation rather than at its end, which removes even the opportunity
       for the backward trace to be examined. [SNIPPET LEVEL — the 2000 draft PDF was LOCATED at
       leonardo-in-flight.nl and multiple secondary summaries were read; NEITHER the draft nor either
       published edition was fetched and read this run. Edition/publisher details are from established
       knowledge. Do not quote a page number onward.]
    2. Hollnagel, E. & Amalberti, R. (2001), "The Emperor's New Clothes, or Whatever Happened to
       'Human Error'?", 4th International Workshop on Human Error, Safety and System Development. —
       **The STOPPING-RULE result, which is the sharpest single idea for 808.** Where "human error" is
       used as a cause or explanation for an adverse event it functions as a STOPPING POINT for the
       investigation, so contributory factors are systematically never reached. This is not a claim
       about carelessness; it is a claim about what a well-formed causal label DOES to an inquiry that
       encounters it. The marker `[Request interrupted by user]` is a stopping rule embedded in the
       telemetry, firing before any investigator arrives. [SNIPPET LEVEL — the workshop paper was NOT
       located as a full text this run; the stopping-rule finding and the Hollnagel & Amalberti 2001
       attribution were read from two independent secondary syntheses (an academic review and a
       safety-science commentary). Treat the attribution as confirmed and the wording as paraphrase.]
    3. Read, G.J.M., Salmon, P.M., Goode, N. & Lenné, M.G. et al. (2021), "State of science: evolving
       perspectives on 'human error'," *Ergonomics* 64(9), DOI 10.1080/00140139.2021.1953615. — **The
       recent peer-reviewed synthesis, and the source of the two propositions 808 most needs.** First:
       attribution of error is A JUDGEMENT ABOUT HUMAN PERFORMANCE MADE EX POST FACTO WITH THE BENEFIT
       OF HINDSIGHT, which makes it impossible to attribute incidents to "human error" consistently
       across cases — i.e. the label is not a stable classifier even among trained human
       investigators. Second, and this is the load-bearing one: human error is a NON-OBSERVABLE
       CONSTRUCT used to make causal inferences WITHOUT CLARITY ON THE MECHANISM BEHIND THE CAUSATION
       (attributed there to Dekker & Hollnagel 2004). A non-observable construct is exactly what a
       telemetry field must not assert. [SNIPPET LEVEL — the Taylor & Francis full-text page WAS
       located and FETCH RETURNED EMPTY (publisher block). The propositions above were read from the
       search-result synthesis and from a second commentary. Journal, volume, year and DOI confirmed;
       full author list NOT confirmed beyond the lead authors. Do not quote this source verbatim
       onward without retrieving it.]
    4. "Searching for the origins of the myth: 80% human error impact on maritime safety,"
       *Reliability Engineering & System Safety* (2021), ScienceDirect S0951832021004567. — **The
       negative-result paper, and the most quotable fact located this run.** The authors went looking
       for the provenance of the field's most-repeated statistic and report that THE ORIGIN OF THE
       80%-BELIEF COULD NOT BE IDENTIFIED, with few sources giving actual evidence or hard data in
       support. The transfer is direct and uncomfortable: a base rate for operator causation can
       circulate for decades, be treated as settled, structure investment and blame, and turn out to
       have no traceable measurement behind it. C2A2's marker is in the same position on day one.
       [SNIPPET LEVEL — the ScienceDirect page WAS located and FETCH RETURNED EMPTY (publisher block).
       Title, journal and PII confirmed from the search index; the finding was read from the
       search-result synthesis. Authors NOT confirmed. This source is USEFUL BUT UNVERIFIED and must
       be retrieved before it is quoted in any outbound artifact.]
    5. Session-termination cause-code practice — Juniper Junos OS, "Session Termination Causes and
       RADIUS Termination Cause Codes" and "AAA Termination Causes and Code Values"; and the TCP RST
       diagnostic literature. — **The engineering precedent for clause (iv), and the remedy shape.**
       Two things are established here as DOCUMENTED PRACTICE rather than as measured effect. First,
       the ambiguity is real at the wire level: a TCP reset can terminate a connection intentionally
       (a closed port, a policy rejection) or through timeouts, application crashes, or interference,
       and the same observable is produced by user cancellation, network partition, slowness and
       server death — a network failure cannot be distinguished from a server failure by the endpoint
       that sees the disconnect. Second, and this is the constructive part: the industries that
       operate at scale on this problem did NOT respond by making the single marker more trustworthy.
       They responded by DEFINING AN ENUMERATED SET OF TERMINATION CAUSE CODES, so that
       "user-requested," "idle timeout," "session timeout," "admin reset," "port error" and "lost
       carrier" are DIFFERENT VALUES rather than one default. The existence of standardised
       termination-cause enumerations in AAA/RADIUS is the field's answer to exactly PRESUMPTION-808,
       and it is a schema, not a habit. [SNIPPET LEVEL — Juniper documentation pages and the TCP RST
       diagnostic material were LOCATED and read at search-summary level only; neither page was
       fetched in full. The RADIUS Acct-Terminate-Cause attribute and its enumerated values are
       CANONICAL from established knowledge and were NOT re-verified against RFC 2866 this run.]
    6. Avizienis, A., Laprie, J.-C., Randell, B. & Landwehr, C. (2004), "Basic Concepts and Taxonomy
       of Dependable and Secure Computing," *IEEE Transactions on Dependable and Secure Computing*
       1(1):11-33. — **The formal apparatus that makes 808 a category error rather than a mistake.**
       The taxonomy's whole purpose is to keep FAULT (the adjudged or hypothesised cause), ERROR (the
       deviant internal state) and FAILURE (the observed deviation of delivered service) apart. A
       termination marker is an observation at the FAILURE level. "A user interrupted" is a claim at
       the FAULT level. The taxonomy holds that the second is ADJUDGED — it is a hypothesis about
       cause, not a datum — and the discipline exists because the two were routinely conflated.
       [SNIPPET LEVEL with strong bibliographic confirmation — the full PDF WAS located at
       landwehr.org and at diag.uniroma1.it, and the fetch SUCCEEDED but the document (119,423
       characters) EXCEEDED THE TOOL'S TOKEN LIMIT and the saved copy was not retrievable afterwards,
       so the paper was NOT read this run. Authors, title, journal, volume, year and page range are
       confirmed across four independent listings, and the fault/error/failure chain is CANONICAL from
       established knowledge.]

  CLEAN NEGATIVE RESULT, reported because it is the most decision-relevant thing in this file:
    **I searched for a MEASURED accuracy or precision figure for automated termination-cause labels —
    in agent runtimes, in LLM serving infrastructure, in job schedulers, or in RPC frameworks — and
    FOUND NOTHING ON POINT.** Searches covered "reliability of self-reported termination causes,"
    "cancellation attribution accuracy," "client-disconnect false attribution," and the
    distributed-systems cancellation literature. What exists is (a) architectural acknowledgement
    that the cause is ambiguous at the endpoint, and (b) enumerated cause-code schemas that PRESUME
    the ambiguity rather than measure it. NO SOURCE ANYWHERE reports "when this runtime says the user
    cancelled, it is right N% of the time." That is a literature gap, and it means the corrective
    proposition is supported STRUCTURALLY and not QUANTITATIVELY. It also means the in-house
    measurement below is not merely cheap — it is the only measurement of its kind I could find any
    demand for.

  Strength of support: **Moderate-Strong.** Clause (ii) is carried by a mature, converged, twenty-
  five-year safety-science literature with a named mechanism (stopping rule, hindsight attribution,
  non-observable construct) and is as close to consensus as that field gets. Clause (iii) has a
  peer-reviewed negative-result paper behind it. Clause (i) is established structurally at the
  protocol level and formally by the dependability taxonomy. Clause (iv) is documented industry
  practice with a standardised schema behind it. What holds the grade below Strong is that (a) the
  safety literature concerns HUMAN investigators attributing to HUMAN operators, and the transfer to a
  RUNTIME attributing to a human is analogical in one direction and stronger in the other (see
  Caveat b); (b) the two most on-point recent sources were both publisher-blocked and are unverified;
  and (c) there is no quantitative anchor anywhere, by the negative result above.

  Summary: The corrective proposition is well supported, and the striking feature of the literature is
  that the discipline which studies this problem professionally reached, twenty-five years ago, the
  exact conclusion 14b reached by inference: the label is where the inquiry begins, not where it ends.
  Dekker's formulation — human error is an attribution assigned in hindsight, and "not an explanation
  of failure, it demands an explanation" — describes a marker that arrives already containing the
  conclusion. Hollnagel and Amalberti supply the mechanism by which that is harmful rather than merely
  imprecise: a causal label functions as a STOPPING RULE, and contributory factors downstream of it
  are not reached, not because anyone declines to look but because the label has already answered the
  question. Read et al. add that the attribution is not even a stable classifier among trained
  investigators, since it is made ex post facto with hindsight, and that "human error" is a
  NON-OBSERVABLE CONSTRUCT — which is a precise statement of what a telemetry field must never assert.
  The maritime-safety provenance paper supplies the cautionary case: the field's most-quoted base rate
  for operator causation, on inspection, has no identifiable origin. Against this, the engineering
  world's answer is not vigilance but SCHEMA: standardised termination-cause enumerations exist
  precisely because one marker cannot carry the distinction between a user cancelling, an idle
  timeout, an admin reset and a lost carrier, and the dependability taxonomy's fault/error/failure
  split makes the same point formally — a marker observes a failure, an attribution hypothesises a
  fault, and the two are different kinds of statement. Where this file must stop is on measurement: no
  source located anywhere reports how often an automated termination label is right about its own
  cause, in any system. The register, meanwhile, already holds the negative half of this on the same
  literal string (PREMISE-141's scope limit), and the mechanism by which the positive half hardened
  (PREMISE-160's diagnosis momentum) was minted two days before this item was surfaced.

  Caveats:
    (a) THIS IS SUBSTANTIALLY PREMISE-141'S SCOPE LIMIT WITH THE SIGN REVERSED, AND THE DISPOSITION
        SHOULD SAY SO. The honest reading of 808 is not "a new finding" but "the register stated one
        direction of a two-directional constraint, and eleven days of runs used the unstated
        direction." Under PREMISE-151 a second recording of an unremediated condition is evidence of
        INCUBATION rather than of management; under PREMISE-135 terminality is not purchased by
        accumulating instances. The right output is probably an AMENDMENT to PREMISE-141's scope limit
        making it symmetric, plus the schema change, not a new premise.
    (b) THE DOMAIN TRANSFER IS ASYMMETRIC AND CUTS BOTH WAYS. The safety literature concerns human
        investigators reasoning under hindsight about human operators, with a documented motivational
        component (blame, liability, closure). A runtime emitting a fixed string has no motive, so the
        cognitive half of the mechanism does NOT transfer. What transfers, and transfers more
        strongly, is the STRUCTURAL half: a pre-attributed label terminates inquiry regardless of who
        wrote it, and a machine-written one is worse because it is uniform, unhesitating, carries no
        authorial uncertainty, and no actor in the chain feels answerable for having asserted it.
        Clause (ii) should be carried by the structural argument, not by the psychology.
    (c) THE MARKER MAY SIMPLY BE ACCURATE, AND PREMISE-160'S CAVEAT (a) BINDS HERE VERBATIM. Nothing
        located establishes that the marker is WRONG in any C2A2 instance. PREMISE-069 is the
        register's own counter-instance: a system-wide anomaly in this very system WAS correctly
        attributed to a benign artifact. 808 concerns WARRANT, not truth, and must not be cited as
        evidence that the interruptions were not human. The 2026-08-15 base-rate correction on
        PRESUMPTION-806 is the standing example of what happens when an inferred pattern is treated as
        established.
    (d) NO REMEDY OF THE FORM "BE MORE SCEPTICAL" IS SUPPORTED, AND ONE IS EXPLICITLY
        CONTRAINDICATED. PREMISE-160 carries Norman et al. (2017) as a BINDING PROHIBITION:
        bias-recognition interventions have no measured effect. Any disposition that resolves 808 by
        instructing runs to question the marker is contradicted by the register's own strongest
        synthesis on the point. The supported shapes are a SCHEMA CHANGE (source 5) or a
        DISCRIMINATING OBSERVATION (below).
    (e) TWO OF THE FOUR ACADEMIC SOURCES WERE PUBLISHER-BLOCKED AND ARE UNVERIFIED. Sources 3 and 4
        are the two most recent and most directly on point, and both fetches returned empty. Their
        findings are reported from search-result syntheses. Neither should be quoted verbatim, and
        source 4's authors are unknown to me. If either is to become load-bearing, retrieve it.
    (f) PUBLICATION-DIRECTION BIAS IS PRESENT AND SHOULD BE STATED. The "new view" is now the
        orthodoxy in human-factors publishing, so a search for support finds a great deal of it. The
        contrary position — that operator attribution is often simply correct and that the new view
        over-corrects — exists and was NOT searched, by design (that is 15b's assignment). Read the
        Strong half of this grade as "the supportive literature is deep and converged," not as "the
        question is settled."

  Search scope: GOOD and CONVERGED on the safety-science treatment of attribution (four independent
  syntheses agreeing on mechanism and wording; no primary text read in full). GOOD on the
  protocol-level ambiguity and the cause-code remedy, at practitioner/vendor level. CONFIRMED
  bibliographically on the dependability taxonomy, unread. **CLEAN NEGATIVE on any measured accuracy
  figure for automated termination-cause labels — see the boxed negative result above.** NOT SEARCHED,
  and each would materially change this: (i) the LLM-agent-runtime literature on cancellation and
  context-limit termination specifically, which is where a base rate would live if one existed;
  (ii) HFACS and the aviation accident-coding literature, which would give the measured inter-coder
  reliability of operator-attribution categories and is the right home for a quantitative anchor;
  (iii) the actual runtime source or documentation that emits this string, which is the cheapest
  possible resolution and was not attempted because it is not a literature question.

  Recommendation: **SUPPORTED (Moderate-Strong)** for the corrective proposition; equivalently
  NO-SUPPORT-FOUND for the presumption as worded. **But the disposition should be an AMENDMENT plus a
  schema change, not a new premise.** Four carries:
    1. MAKE PREMISE-141'S SCOPE LIMIT SYMMETRIC. It currently bars inferring FAULT from the marker; it
       should equally bar inferring HUMAN AGENCY from it. One sentence, no new premise, and it closes
       the polarity gap (R1) that is the whole of this item's novelty.
    2. THE DISCRIMINATING OBSERVATION IS FREE AND SHOULD BE MADE BEFORE ANYTHING ELSE. Whether a human
       was present during a marked termination is externally checkable — wall-clock time against the
       schedule, the presence or absence of any human utterance in the session, and Tom. Per
       PREMISE-107's cost guard and PREMISE-160's one-case rule, ONE marked termination on a day when
       no human spoke, confirmed against Tom, discharges or refutes the item outright. It is not a
       literature question and no premise is needed to authorise it.
    3. THE REMEDY SHAPE IS A CAUSE-CODE ENUMERATION, WHICH IS THE SAME FAMILY AS TWO EXISTING FILED
       CHANGES. PREMISE-141 filed a THIRD TERMINAL STATE; PREMISE-146 named a MISSING ATTRIBUTION
       FIELD in which "specification" is representable. 808 asks for a third instance of the same
       move: a termination record in which "cause not observed" is a representable value alongside
       "user-requested." Where C2A2 cannot change what the runtime emits, the fleet can still refuse
       to PROPAGATE the runtime's attribution into its own records — per PREMISE-140, record "session
       terminated without completion record; cause not observed by this channel."
    4. DO NOT REMEDY BY EXHORTATION. PREMISE-160's Norman et al. prohibition binds. Any proposal of
       the form "runs should treat the marker sceptically" should be rejected at disposition.

--- CYCLE RE-SEARCH: 2026-08-25 (15a) ---
  Date searched: 2026-08-25
  Trigger: 15d re-trigger (MONITOR-528, cycle 1). **A LOOKUP, NOT AN INFERENCE.** Does the marker
    `[Request interrupted by user]` actually mean a user interrupted? 15c's stated INCORPORATE
    condition is VENDOR DOCUMENTATION OR A CHANGELOG ENTRY settling the marker's emission semantics —
    anything less is not sufficient. 15b had already fetched one public issue tracker holding
    independent user reports, which is not sufficient alone.

  Search scope: Went to the vendor's own published changelog rather than to the literature. Retrieved
    `CHANGELOG.md` from the `anthropics/claude-code` repository at `raw.githubusercontent.com`
    (5,763 lines, the vendor's official release notes), and grepped it for interruption semantics,
    then resolved each hit to its release-version header. Also fetched one issue from the vendor's
    official issue tracker for the failure-mode description. Also checked the vendor's Agent SDK
    documentation for an enumerated termination-cause set. This closes the third item on the prior
    cycle's own NOT-SEARCHED list ("the actual runtime source or documentation that emits this
    string, which is the cheapest possible resolution").
    TOOL LIMIT DECLARED: the session's WebSearch budget (200 calls) was exhausted later in this
    cycle; it did not constrain this item, which was resolved by direct retrieval of the changelog.

  Supporting evidence found: **Yes — decisively, and from the vendor.**

  New sources this cycle:
    1. Anthropic, `anthropics/claude-code`, `CHANGELOG.md`, release **2.1.218** — **VENDOR CHANGELOG,
       FULL-TEXT retrieved and verified this cycle.** Verbatim: *"Fixed spurious `[Request interrupted
       by user]` messages after interrupted tool calls, and an unpaired `tool_use` block left in the
       transcript when a tool aborted mid-response."*
       **THIS IS THE INCORPORATE CONDITION, MET, ON THE LITERAL STRING.** The vendor's own release
       notes describe emissions of this exact marker as SPURIOUS, and identify the emitting condition
       as a TOOL CALL ABORTING MID-RESPONSE — a machine event, with no user in it. The marker's
       emission semantics are therefore settled by the vendor: the string is emitted on at least one
       code path that has nothing to do with a user, and the vendor classified that behaviour as a
       defect and shipped a fix for it. PRESUMPTION-808 is confirmed as a real defect, not a
       hypothesis.
    2. Anthropic, `anthropics/claude-code`, `CHANGELOG.md`, release **2.1.236** — VENDOR CHANGELOG,
       verified. Verbatim: *"SIGTERM in print/SDK mode no longer records an interrupted turn or
       synthetic tool denials before exiting; running commands are still terminated and the process
       still exits with code 143."*
       **The second independent code path, and the one most relevant to C2A2**, because C2A2's
       recurring runs are unattended SDK/print-mode invocations. This entry establishes that prior to
       2.1.236 an OS-level process signal — SIGTERM, sent by a supervisor, an orchestrator, a
       timeout, or a container shutdown, and by definition not a keystroke — WAS recorded as an
       interrupted turn. It also establishes that the runtime additionally fabricated "synthetic tool
       denials," i.e. it invented user-attributed refusals that no user made. That is the strongest
       single fact located across both cycles.
    3. Anthropic, `anthropics/claude-code`, `CHANGELOG.md`, release **2.1.216** — VENDOR CHANGELOG,
       verified. Verbatim: *"Fixed telemetry misreporting permission denials: failed permission-prompt
       requests no longer count as user rejections, and user interrupts are now reported as user
       aborts instead of rejections."* Vendor acknowledgement that the TELEMETRY layer specifically
       was mis-attributing machine-side failures to user action, which is PRESUMPTION-808's mechanism
       named in the vendor's own voice and located in the vendor's own metrics pipeline.
    4. Anthropic, `anthropics/claude-code`, `CHANGELOG.md`, release **2.1.221** — VENDOR CHANGELOG,
       verified. Verbatim: *"Fixed `CLAUDE_CODE_RESUME_INTERRUPTED_TURN=0` not disabling
       interrupted-turn auto-resume; falsy values are now honored."* Recorded because it establishes
       that "interrupted turn" is a first-class, named, configurable RUNTIME STATE with its own
       environment variable — not a description of an observed human act. A state the runtime can
       auto-resume from is a state the runtime assigns, which is clause (i) of the corrective
       proposition confirmed at the implementation level.
    5. Claude Agent SDK, `ResultMessage.subtype` enumeration (`success`, `error_max_turns`,
       `error_during_execution`), with `stop_reason` carried on both success and error results —
       VENDOR DOCUMENTATION, located and read at search-summary level this cycle; the reference pages
       themselves were NOT fetched. **This is clause (iv)'s remedy already partly built.** The SDK
       does expose an enumerated termination-cause field distinct from the transcript marker. The
       gap, and it is the actionable one, is that the enumeration has no value meaning "cause not
       observed" and no value distinguishing user cancellation from signal-driven termination — so
       the schema is enumerated but not complete for this purpose.
    6. `anthropics/claude-code` issue **#35738**, "[BUG] Spontaneous 'Request interrupted by user'
       triggered by Linux kernel 6.17.0-19-generic" (opened 18 Mar 2026, Claude Code 2.1.78, labelled
       `duplicate` by the vendor) — VENDOR ISSUE TRACKER, FULL-TEXT fetched this cycle. Reporter:
       *"Claude Code CLI spontaneously shows '[Request interrupted by user]' without any user action
       (no Ctrl+C, no Escape pressed)"*, with the cause isolated to a specific kernel build and
       resolved by downgrading it. Corroborative rather than load-bearing — the changelog entries
       above are what meet the INCORPORATE condition — but it establishes that the marker fires from
       causes as remote as a kernel version, and the vendor's `duplicate` label is itself an
       acknowledgement that the class is known.

  Strength of support: **Strong.** This is the highest grade assigned to this item across both cycles
    and the upgrade is entirely on provenance: the prior cycle carried a Moderate-Strong grade built
    on four publisher-blocked or snippet-level safety-science sources and an explicitly declared
    CLEAN NEGATIVE on anything quantitative. This cycle replaces the central factual question with a
    primary-source answer from the party that emits the string.

  Summary: The item is a lookup and the lookup returned. Anthropic's own published changelog for
    `claude-code` settles the marker's emission semantics in three independent entries, and settles
    them against the presumption. Release 2.1.218 records a fix for "spurious `[Request interrupted
    by user]` messages after interrupted tool calls" — the vendor's word is *spurious*, and the
    triggering condition is a tool aborting mid-response. Release 2.1.236 records that SIGTERM in
    print/SDK mode formerly recorded an interrupted turn and fabricated synthetic tool denials, which
    is decisive for C2A2 specifically because C2A2's recurring runs are unattended SDK-mode
    invocations and SIGTERM is exactly what a supervisor or timeout sends them. Release 2.1.216
    records the vendor fixing telemetry that miscounted machine-side failures as user rejections. So
    the marker is not an observation of a user; it is a runtime classification with at least three
    documented non-user emission paths, each of which the vendor treated as a defect. Two
    consequences follow. First, the eleven-day asymmetry identified in the prior cycle's DUPLICATION
    WARNING — PREMISE-141 barring the fault inference while nothing barred the human-agency inference
    — is now not merely unguarded but affirmatively wrong on the vendor's own account, and carry 1
    (make PREMISE-141's scope limit symmetric) should proceed. Second, the prior cycle's CLEAN
    NEGATIVE stands unchanged and should not be quietly dropped: the changelog establishes that the
    marker is sometimes wrong, and gives named mechanisms for how, but still nobody anywhere reports
    how OFTEN. The support remains structural, not quantitative.

  Caveats: (a) **VERSION SCOPE IS A REAL LIMIT AND MUST NOT BE ELIDED.** Every entry cited is a FIX.
    They establish that the marker was unreliable up to those releases; they do not establish that it
    is unreliable now, and a system on 2.1.236 or later has had all three of these paths closed. The
    honest claim is *the marker has a documented history of non-user emission and is a classification
    rather than an observation*, NOT *the marker is currently wrong*. What C2A2 actually needs, and
    what this file cannot supply, is the runtime version in force on the days in question — which is
    a local check, not a literature question, and is cheaper than anything else outstanding on this
    item.
    (b) Prior-cycle caveat (c) BINDS UNCHANGED AND SHOULD BE RE-READ AT DISPOSITION: nothing here
    establishes that the marker was wrong in any specific C2A2 instance. 808 concerns WARRANT, not
    truth. The vendor documenting a defect class is not evidence that C2A2 hit it, and PREMISE-069
    remains the register's own counter-instance. The 2026-08-15 base-rate correction on
    PRESUMPTION-806 is the standing example of the error this would be.
    (c) The changelog is release-note prose, not a specification. It tells us these paths existed; it
    does not enumerate all paths, and there is no vendor document that does. Absence of a fourth
    entry is not evidence of a fourth path's absence.
    (d) Source 5 (the SDK subtype enumeration) was read at search-summary level only and the SDK
    reference pages were not fetched. Before the remedy in carry 3 is designed against that
    enumeration, the actual field values should be read from the vendor reference directly.
    (e) The prior cycle's DUPLICATION WARNING is UNAFFECTED by this cycle and still governs. Nine
    ACTIVE premises bear, one on this literal string. Nothing found this cycle argues for a new
    premise; it argues that an existing one is asymmetric and should be amended. A disposition that
    mints a new premise here is still at risk under PREMISE-138(1) and PREMISE-135.

  Disposition-changer met: **YES.** 15c's INCORPORATE condition was vendor documentation or a
    changelog entry settling the marker's emission semantics. The citation that meets it is
    Anthropic, `anthropics/claude-code` `CHANGELOG.md`, release **2.1.218**: *"Fixed spurious
    `[Request interrupted by user]` messages after interrupted tool calls, and an unpaired `tool_use`
    block left in the transcript when a tool aborted mid-response"* — the vendor, on the literal
    string, calling the emission spurious and naming a non-user cause. Reinforced by release
    **2.1.236** on SIGTERM recording an interrupted turn in SDK mode, which is C2A2's own execution
    mode. **The marker does not mean a user interrupted. It means the runtime classified the turn as
    interrupted.**

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently NO-SUPPORT-FOUND
    for the presumption as worded, which the vendor's release notes contradict directly. The four
    carries from the 2026-08-16 file stand, with carry 1 (make PREMISE-141's scope limit symmetric)
    now resting on vendor documentation rather than on inference, and carry 2 (the free
    discriminating observation) narrowed to a single cheap step: **read the Claude Code version in
    force on the days the marker appeared and compare it against 2.1.218 / 2.1.236.** That is a
    lookup, it is local, and it converts this item from open to closed.

  PROVENANCE: Origin: 14b · Chain: [14b → 15a, 15b → 15c → 15d → 15a] · Item type: PRESUMPTION
    (unstated — surfaced by inference; extra weight per the provenance protocol) · Transform: 15a
    re-searched on 15d re-trigger, going to the vendor changelog rather than to the literature and
    closing the prior cycle's own third NOT-SEARCHED item · Current status: SUPPORTED (Strong) —
    INCORPORATE condition MET on vendor changelog; disposition remains an AMENDMENT to PREMISE-141
    plus a schema change, not a new premise

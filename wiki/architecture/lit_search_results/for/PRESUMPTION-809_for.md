SEARCH-FOR-PRESUMPTION-809:
  Date searched: 2026-08-16
  Original item: PRESUMPTION-809
  Original statement: [inferred] That a job which is loaded is a job which is running; more generally,
    that a register storing declarations about a thing is read as a report from it.
  Risk if wrong: Critical.

  POLARITY NOTE — what was searched FOR. The presumption is worded as the DEFECTIVE belief ("loaded
  means running; a declaration reads as a report"). The proposition searched FOR is the CORRECTIVE
  CONVERSE, in four clauses: (i) that A DECLARATION AND AN OBSERVATION ARE DIFFERENT KINDS OF RECORD
  and neither substitutes for the other — the systems that got this right store them in SEPARATE
  FIELDS and run a process whose entire job is to reconcile them; (ii) that CONFIGURATION-STATE-AS-
  HEALTH IS A NAMED AND DOCUMENTED FAILURE MODE with its own vocabulary in at least three independent
  disciplines (stale registry entries in service discovery, configuration drift in ITSM, registered-
  versus-ready in orchestration); (iii) that the SPECIFIC CLAIM ABOUT LOADED JOBS IS STATED BY THE
  VENDOR'S OWN DOCUMENTATION — Apple's guide says in terms that a loaded job may never run, and says
  so without any suggestion that anything would report the fact; and (iv) that DETECTING NON-EXECUTION
  REQUIRES A DETECTOR WITH STATED PROPERTIES, and that a register of declarations has the weakest
  possible value of the relevant property — it never suspects anything, ever. "SUPPORTED" below means
  14b's worry is well grounded, and is equivalently evidence AGAINST the presumption as worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-809
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight per the provenance
      protocol)
    Transform at each step:
      14b: Generalised the launchd finding to the form shared by three of the day's failures.
      15a: Searched for supporting literature on the corrective proposition, separately for the
        SPECIFIC claim (loaded ≠ running) and for the GENERAL claim (declaration ≠ report), because
        the register's holdings differ sharply between the two.
    Current status: SUPPORTED (Strong) on the specific claim — with a heavy duplication warning;
      SUPPORTED (Moderate) on the generalisation, which is where the increment is.

  **DUPLICATION WARNING — READ BEFORE DISPOSITION. THIS IS THE MOST HEAVILY REGISTER-HELD OF THE FIVE
  ITEMS IN THIS BATCH.** The specific claim is held at least six times over, in six different guises,
  by ACTIVE premises. **PREMISE-100** (ACTIVE): "A liveness signal (lastRunAt / heartbeat) is not
  evidence of correctness, and A HEALTH CHECK THAT CANNOT EXECUTE IN ITS RUNTIME CONTEXT REPORTS AS
  PASSING RATHER THAN AS ABSENT." **PREMISE-085** (ACTIVE), on launchd specifically, with a SCOPED
  CAVEAT that already narrows it to "PROCESS liveness only." **PREMISE-115** (ACTIVE): "FILE EXISTENCE
  IS A LIVENESS TEST, and the fault class this premise concerns is precisely the one liveness tests
  miss." **PREMISE-141 clause (1)** (ACTIVE, High): omission is not crash; the run model is two-valued
  and cannot represent a session that started and emitted nothing. **PREMISE-155 clause (1)** (ACTIVE):
  "A NAME IS NOT AN IDENTITY"; any freshness, presence or state assertion must bind to a resolved
  identity and must resolve it the way a consumer does. **PREMISE-166 clause (2)** (ACTIVE, minted
  YESTERDAY, 2026-08-15): "a heartbeat keyed to INVOCATION reports healthy through a stall of a
  started process... A status artefact written at entry is a SELF-KICK PROVING THE LIVENESS OF THE
  WRONG THING." That last one is PRESUMPTION-809 in the fleet's own words, minted the day before 809
  was surfaced. A disposition that mints a new premise for the specific claim would be re-minting at
  least three of these, which PREMISE-138(1) and PREMISE-135 bar.

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: liveness, loaded, launchd, "health check", presence,
    heartbeat, configur*, "declar.*report", "silent fail", freshness, registry.
    Found and read in full:
      - **PREMISE-166** (2026-08-15, ACTIVE, Moderate) — clause (2), quoted above. Its DECLARED
        NEGATIVE also transfers verbatim and constrains any remedy: "15a searched for and did NOT find
        an empirical failure rate for self-hosted stall detectors, and 15b searched for and did NOT
        find one either — the effectiveness of the remedy is practitioner consensus, not a measured
        result." I re-encountered the same gap this run and confirm it independently.
      - **PREMISE-100** (ACTIVE) — quoted above. The closest single antecedent for the SPECIFIC claim.
      - **PREMISE-085** (ACTIVE) — launchd/systemd is the correct posture for SINGLE-NODE PROCESS
        liveness and reboot restart, with the scoped caveat that "durable" means process liveness only
        and not data durability or availability. Already narrows the launchd claim once; 809 narrows
        it a second time, in a direction 085 does not cover — 085 concerns what supervision GIVES you
        when the job runs, 809 concerns whether it ran at all.
      - **PREMISE-086** (ACTIVE) — the dead-man's-switch: alarm on the AGE of the last dated PASS/FAIL,
        because absence/staleness IS the signal; with the CONDITIONAL that the report must alarm on
        AGE rather than display a last-known value, "else it becomes THE PERCEIVED-LIVENESS TRAP." The
        register named 809's failure mode, in those words, in June.
      - **PREMISE-089** (ACTIVE) — freshness/liveness is a PER-SOURCE property; and its refinement,
        that freshness-independence does not imply failure-independence because feeds sharing an
        upstream scheduler can freeze together.
      - **PREMISE-115** (ACTIVE) — quoted above; the EFFECTIVENESS CHECK AT CONTENT LEVEL clause is
        exactly 809's remedy shape, one layer up: check that the expected CONTENT appears, never that
        a file appears.
      - **PREMISE-141** (2026-08-05, ACTIVE, High) — clause (1), the missing third terminal state.
      - **PREMISE-155** (2026-08-13, ACTIVE, Moderate) — clause (1) name-vs-identity, clause (2)
        differential observability ("silent BY CONSTRUCTION rather than by oversight, because nothing
        in the architecture ever compares the two observation points"). 809's general form is the
        semantic sibling: nothing ever compares the declaration against an observation.
      - **PREMISE-110** (ACTIVE) — a monitor sharing a failure domain with its subject is a single
        channel wearing two labels; a monitor's pass state is systematically reachable while its
        subject is dead.
      - **PREMISE-137** (ACTIVE) — a difference-based check inherits its power from its baseline; a
        FIRST-EVER RUN has no reference and the check CANNOT FAIL. A register with no observations in
        it is in exactly this position permanently.
      - **PREMISE-164** (2026-08-14, ACTIVE, Moderate) — "a record is durable only if it is written to
        a location the NEXT EXECUTOR'S OWN PROCEDURE REQUIRES IT TO READ," and its explicit warning
        against "building a register with no scheduled reader." Adjacent from the other side: 164 is
        about registers nobody reads, 809 about registers read as something they are not.
    CONCLUSION OF THE CHECK: **NEAR-TOTAL OVERLAP ON THE SPECIFIC CLAIM; PARTIAL OVERLAP ON THE
    GENERALISATION; NO NOVELTY-FLAG.** Eleven ACTIVE premises bear. The residual is stated below and
    it is narrow.
    DECLARED LIMITATION: this was a STRING GREP, measured at ~56% recall (ASSUMPTION-1052). The list
    above is a **LOWER BOUND**. Eleven hits argues strongly for a narrow disposition.

  RESIDUAL — what 809 contains that the register does not:
    (R1) THE GENERALISATION IS THE ITEM, AND IT IS NOT HELD. The register holds this result SIX TIMES
         AS INSTANCES — heartbeat, file existence, freshness, name-vs-identity, invocation-keyed ping,
         inoperable check — and NOWHERE AS A TYPE. No premise states the abstract form: A RECORD OF
         WHAT WAS DECLARED AND A RECORD OF WHAT WAS OBSERVED ARE DIFFERENT KINDS OF OBJECT AND MUST
         NOT SHARE A FIELD. That the fleet has re-derived the same result six times from six
         directions is itself the evidence that the type-level statement is missing.
    (R2) BUT PREMISE-135 BINDS THE GENERALISATION, AND IT IS NOT SATISFIED. "TERMINALITY IS PURCHASED
         BY ENUMERATING THE DOMAIN, NOT BY ACCUMULATING INSTANCES." 809 generalises from three of one
         day's failures. Under 135 the generalisation owes (a) an enumerated POPULATION of registers
         in the system, (b) a TERMINATION CRITERION, and (c) ONE SEVERE TEST on a register kind that
         was NOT among the three that produced it. 809 supplies none of the three. This is the single
         most important constraint on how this item is dispositioned and it comes from the register,
         not from the literature.
    (R3) THE CROSS-DOMAIN VOCABULARY IS ABSENT AND IS CHEAP TO IMPORT. Three mature disciplines have
         independently named this and built machinery against it — CONFIGURATION DRIFT and
         RECONCILIATION in ITSM, STALE REGISTRY ENTRIES and REGISTERED-VERSUS-READY in service
         discovery, and SPEC-VERSUS-STATUS in declarative orchestration. None of that vocabulary
         appears anywhere in the register, and having it would have let the fleet see the six
         instances as one class the first time.

  Supporting evidence found: Yes

  Sources:
    1. Apple Inc., "Scheduling Timed Jobs," *Daemons and Services Programming Guide*, Documentation
       Archive, document version 6.3.4, updated 2016-09-13. — **The primary source for clause (iii),
       and it is the vendor stating the item's own claim.** Read in full. Three findings, all direct
       quotations: (a) "If the system is turned off or asleep, `cron` jobs do not execute; they will
       not run until the next designated time occurs." (b) "ALL OTHER `launchd` JOBS ARE SKIPPED when
       the computer is turned off or asleep; they will not run until the next designated time occurs."
       — note SKIPPED: not queued, not deferred, not reported. (c) The guide's own summary sentence:
       "Consequently, IF THE COMPUTER IS ALWAYS OFF AT THE JOB'S SCHEDULED TIME, BOTH `cron` JOBS AND
       `launchd` JOBS NEVER RUN. For example, if you always turn your computer off at night, a job
       scheduled to run at 1 A.M. WILL NEVER BE RUN." A job in exactly that condition remains loaded
       and remains listed. The documentation states the non-execution and says nothing whatever about
       any signal being emitted, because there is none. The only exception the guide grants is
       `StartCalendarInterval` under SLEEP, which does run on wake — which matters, because it means
       the fleet's jobs may fall on either side of the line depending on a plist key, and nothing in
       C2A2 records which. [**VERIFIED this run — the page was fetched and read in full.** All three
       quotations are read directly. Caveat: this is ARCHIVED documentation last updated 2016, and
       macOS scheduling behaviour has demonstrably changed since (Apple's own developer forums carry
       2024-2025 threads reporting altered `StartCalendarInterval` behaviour under sleep). The
       structural claim — loaded jobs can silently never run — is not in doubt; the exact
       sleep/wake semantics on the current OS are, and were NOT verified.]
    2. Chandra, T.D. & Toueg, S. (1996), "Unreliable Failure Detectors for Reliable Distributed
       Systems," *Journal of the ACM* 43(2):225-267. — **The formal apparatus for clause (iv), and the
       sharpest way to state what a declaration register is not.** A failure detector is characterised
       by exactly two properties: COMPLETENESS (its capability of eventually suspecting every faulty
       process) and ACCURACY (its capability of not suspecting correct processes). The paper's central
       and famous result is that consensus is solvable with detectors that make an INFINITE NUMBER OF
       MISTAKES — i.e., accuracy can be arbitrarily poor and the system still works — but the
       completeness requirement is not similarly negotiable. Apply this to 809: **a register of
       declarations has completeness ZERO. It will never suspect anything, under any circumstance, no
       matter how long the process has been dead.** It is not a bad failure detector; it is not a
       failure detector at all, and no amount of reading it more carefully changes that. This is the
       formal version of what PREMISE-166 clause (2) says operationally about a self-kick.
       [SNIPPET LEVEL — the JACM record (DOI 10.1145/226643.226647), the Semantic Scholar entry and a
       full PDF at cs.utexas.edu were all LOCATED this run; the paper was NOT read. Authors, title,
       journal, volume, issue, pages and year are confirmed across three independent listings. The
       completeness/accuracy definitions are CANONICAL from established knowledge and were confirmed
       against the retrieved summaries.]
    3. Service-discovery practice: the registered-versus-healthy distinction and the stale-registry
       problem (Netflix Eureka, HashiCorp Consul, Kubernetes liveness/readiness probes). — **The
       operational confirmation of clause (ii), from the domain where this failure is most expensive.**
       Four propositions, all documented practice: (a) REGISTRATION IS NOT HEALTH — an instance can be
       registered and alive at the process level while unable to serve, which is exactly why the
       probe model splits LIVENESS (is the process up; if not, restart it) from READINESS (can it
       serve; if not, remove it from traffic), and the two have DIFFERENT REMEDIES, so collapsing
       them loses the remedy as well as the signal. (b) THE STALE ENTRY IS THE NAMED CENTRAL PROBLEM
       of the whole pattern — "the biggest challenge in service discovery is ensuring the service
       registry has up-to-date information and doesn't contain stale entries" — with documented
       real-world incidents in which Eureka retained stale instances and routed traffic to services
       that were already gone. (c) THE FIX IS ALWAYS THE SAME SHAPE and it is never "read the registry
       more carefully": either the instance must actively HEARTBEAT within a TTL or the registry must
       actively PROBE it; in both cases an OBSERVATION is manufactured to sit alongside the
       declaration, and the entry expires in its absence. (d) Where availability is preferred to
       consistency, STALENESS MUST BE EXPECTED BY THE CLIENT as a design assumption, not treated as a
       fault. [SNIPPET LEVEL — multiple practitioner and system-design sources were located and read
       at search-summary level; NO primary vendor documentation (Consul, Eureka, Kubernetes probe
       docs) was fetched this run. This is DOCUMENTED PRACTICE, not measured effect, and the specific
       Eureka incident is a practitioner blog report, not a study.]
    4. Configuration-drift and CMDB-accuracy doctrine (ITIL/ITSM lineage; BMC Helix drift management;
       practitioner guidance). — **The generalisation's home discipline, and the source of the
       vocabulary R3 asks for.** The ITSM tradition faced precisely 809's general problem at
       enterprise scale and settled it in the item's favour, in four moves. (a) It NAMED the gap:
       DRIFT is "the difference between the current physical state of your IT environment and the
       expected or correct state" — i.e., the discipline's core operational concept IS the
       declaration/observation gap. (b) It DENIED that the register is self-warranting: "CMDB ACCURACY
       SHOULD BE TRACKED AS A METRIC, NOT ASSUMED AS A STATE." That single sentence is the corrective
       proposition. (c) It specified the METHOD: "compare discovery findings against CMDB records on a
       regular basis; measure the percentage of CIs where discovered attributes match" — a
       RECONCILIATION between a declared record and an independently produced observation, run on a
       schedule, whose output is a match rate. (d) It located the cause STRUCTURALLY rather than in
       carelessness: the CMDB depends on upstream systems each holding a different version of the same
       asset, so "without a reconciliation layer upstream, the CMDB INHERITS EVERY CONFLICT AND GAP
       from those sources rather than resolving them." [SNIPPET LEVEL — vendor and practitioner
       sources (BMC Helix documentation, Virima, Oomnitza, CloudQuery) located and read at
       search-summary level. **I SEARCHED FOR AND DID NOT FIND a formal academic study measuring CMDB
       accuracy against discovered state**; the search index returned only vendor material. Treat the
       vocabulary and the method as documented practice, and treat any accuracy figure from this
       domain as unsourced.]
    5. Declarative reconciliation as a data-model answer: the Kubernetes object model, in which every
       object carries a `spec` (the DESIRED state, declared by the user) and a `status` (the OBSERVED
       state, written by the system), with a controller whose entire function is to drive one toward
       the other. — **The strongest single design precedent for the generalisation, because it puts
       the answer in the SCHEMA rather than in anyone's discipline.** The relevant fact is not that
       reconciliation exists but that THE TWO STATES ARE DIFFERENT FIELDS WITH DIFFERENT WRITERS, so
       that reading a declaration as a report is not a mistake one can make — it is not
       representable. That is the exact remedy shape for 809, and it is the same move as PREMISE-141's
       third terminal state and PREMISE-146's missing attribution field. [**CANONICAL — cited from
       established knowledge, NOT re-verified this run.** The Kubernetes documentation page on working
       with objects was IDENTIFIED as the correct citation and the fetch was REFUSED by the tool's
       provenance rule (the URL had not appeared in a prior search result). Do not quote specific
       documentation wording onward without retrieving it.]
    6. Avizienis, A., Laprie, J.-C., Randell, B. & Landwehr, C. (2004), "Basic Concepts and Taxonomy
       of Dependable and Secure Computing," *IEEE TDSC* 1(1):11-33. — The formal separation of the
       SERVICE a system is specified to deliver from the SERVICE ACTUALLY DELIVERED, with failure
       defined as the deviation between them. A declaration record describes the former; only an
       observation reaches the latter. [SNIPPET LEVEL — PDF located at landwehr.org; fetch succeeded
       but EXCEEDED THE TOOL'S TOKEN LIMIT and the document was NOT read. Bibliographic details
       confirmed across four listings; the specified/delivered distinction is CANONICAL.]

  CLEAN NEGATIVE RESULTS, reported because both bear on the remedy:
    (a) **I searched for a measured SILENT-FAILURE RATE for scheduled jobs — cron, launchd or systemd
        timers — and found nothing.** Practitioner material asserts that silent scheduled-job failure
        is common; no source quantifies it. This independently reproduces PREMISE-166's declared
        negative from the opposite search direction, which is worth recording: two 15a runs and one
        15b run have now looked for this number and none has found it.
    (b) **I searched for an academic study of CMDB accuracy and found only vendor material.** The
        method (reconcile declared against discovered, report a match rate) is well documented; the
        typical match rate is not, at least not anywhere I could reach.

  Strength of support: **Strong on the specific claim; Moderate on the generalisation.** The specific
  claim is stated by the vendor's own documentation in unambiguous terms (source 1, verified, read in
  full) and is formally underwritten by the failure-detector definition (source 2). The generalisation
  is supported by convergence across three independent disciplines that each named and engineered
  against it, plus a design precedent that encodes the answer in a schema — but that convergence is
  carried by practitioner and vendor material rather than by measurement, and PREMISE-135's
  requirements on the inductive step are not met by the item itself.

  Summary: The corrective proposition is well supported, and on the narrow claim it is supported by
  the least contestable kind of source available: Apple's own guide says that a `launchd` job whose
  scheduled moment passes while the machine is off is SKIPPED and "will never be run," with no
  suggestion anywhere that this produces a signal. Loaded and running are therefore not merely
  distinguishable states — the documentation treats their divergence as ordinary and expected. Chandra
  and Toueg supply the formal statement of what follows: a failure detector is defined by COMPLETENESS
  (it eventually suspects every faulty process) and ACCURACY (it does not suspect correct ones), and
  their result is that accuracy can be arbitrarily bad while the system still works — but a register
  of declarations has completeness ZERO, so it is not a poor detector, it is not a detector. The
  generalisation is where the interesting support lies, because three unrelated disciplines
  independently hit this wall and each responded the same way. Service discovery names STALE ENTRIES
  as the central problem of the whole pattern, splits LIVENESS from READINESS because they have
  different remedies, and manufactures an observation — heartbeat within a TTL, or an active probe —
  to sit beside every registration. ITSM names the gap DRIFT, and states the corrective in one
  sentence: CMDB accuracy is to be TRACKED AS A METRIC, NOT ASSUMED AS A STATE, by periodically
  reconciling the declared record against independently discovered state and reporting the match rate.
  Declarative orchestration goes furthest and puts the answer in the schema: `spec` and `status` are
  different fields with different writers, so reading a declaration as a report is not a discipline
  failure one can commit — it is not expressible. All three arrived at the same place: you cannot fix
  this by reading the register more carefully, because the information is not in the register. Where
  this file must stop short is on the register's own holdings. Eleven ACTIVE premises bear on this
  item, and PREMISE-166 clause (2) — minted the day before 809 was surfaced — already says that a
  status artefact written at entry is "a SELF-KICK PROVING THE LIVENESS OF THE WRONG THING."

  Caveats:
    (a) THE SPECIFIC CLAIM IS SUBSTANTIALLY HELD SIX TIMES OVER AND SHOULD NOT BE MINTED AGAIN. See
        the DUPLICATION WARNING. The reading that survives is not "a new finding" but "a class the
        fleet has now derived from six directions without ever writing down the class." Under
        PREMISE-151 the repetition is evidence of incubation; under PREMISE-135 accumulating instances
        does not purchase terminality.
    (b) AND THE GENERALISATION — THE PART THAT IS GENUINELY NEW — IS THE PART PREMISE-135 CONSTRAINS
        MOST. This is the item's central tension and it should drive the disposition. 809 generalised
        from three of one day's failures. PREMISE-135 requires an enumerated POPULATION, a stated
        TERMINATION CRITERION, and ONE SEVERE TEST on a kind not among the generating instances. The
        symmetry clause of 135 also applies: name the WORST-COVERED instance of "declaration ≠ report"
        and go and look at it. None of this has been done, and a disposition that mints the general
        premise without it repeats exactly the error 135 exists to prevent.
    (c) THE SUPPORT FOR THE GENERALISATION IS CONVERGENT BUT NOT INDEPENDENT-IN-METHOD. Service
        discovery, ITSM and orchestration are three domains, but the sources located are almost
        entirely VENDOR AND PRACTITIONER material, which shares an incentive structure (each is
        selling reconciliation tooling) and a common ancestry. Per PREMISE-111 that is residual
        correlation rather than three confirmations. Only source 2 is peer-reviewed, and it was not
        read.
    (d) THE VENDOR DOCUMENTATION IS TEN YEARS OLD AND THE PLATFORM HAS CHANGED. Source 1 was last
        updated 2016-09-13 and is in Apple's Documentation ARCHIVE. Developer-forum threads from 2024
        and 2025 report changed `StartCalendarInterval` behaviour under sleep on current macOS. The
        structural claim survives; any specific prediction about what the fleet's jobs do on the
        current OS does NOT follow from source 1 and must be checked directly.
    (e) NEITHER NEGATIVE RESULT SHOULD BE READ AS "IT DOESN'T HAPPEN." No measured silent-failure rate
        for scheduled jobs was found, and no measured CMDB accuracy figure was found. Absence of
        measurement is not evidence of rarity, and it is also not licence to assert a rate. Per
        PREMISE-124 nothing here is a calibrated measurement.
    (f) THE REMEDY HAS A KNOWN COST AND SOURCE 3 STATES IT. Manufacturing an observation for every
        declaration means heartbeats, TTLs and probes — which is more moving parts, each of which can
        fail, and PREMISE-110 and PREMISE-166(1) both bar placing the new observer inside the failure
        domain it observes. PREMISE-155's FORM CONDITION also binds: prefer DISPLAYING an age to
        ADDING a pass/fail alert per artefact per path, because freshness is a high-volume alert class
        and the acceptance decay is real (PREMISE-121).

  Search scope: VERIFIED and COMPREHENSIVE on the launchd/cron specific claim (source 1 fetched and
  read in full, though archived). CONFIRMED bibliographically and CANONICAL on the failure-detector
  formalism, unread. GOOD but VENDOR-WEIGHTED on service discovery, configuration drift and the
  reconciliation pattern. CANONICAL and UNVERIFIED on the Kubernetes spec/status precedent, whose
  documentation fetch was refused by a tool provenance rule. **CLEAN NEGATIVE on any measured
  scheduled-job silent-failure rate, independently reproducing PREMISE-166's declared negative.**
  **CLEAN NEGATIVE on any academic measurement of CMDB accuracy.** NOT SEARCHED, and each would
  materially change this: (i) the systemd `OnFailure=` / `systemd-analyze` timer-monitoring literature
  and whether any distribution ships a default failure notification, which is the closest thing to a
  measured base rate that might exist; (ii) the cache-coherence and read-your-writes consistency
  literature, which BOTH search directions named as the missing formal analogue on PREMISE-155 and
  which is still unrun and would serve 809 equally; (iii) the specific plist keys of C2A2's own
  scheduled jobs, which is not a literature question but determines whether source 1's sleep exception
  applies to any of them.

  Recommendation: **SUPPORTED (Strong on the specific claim, Moderate on the generalisation)** for the
  corrective proposition; equivalently NO-SUPPORT-FOUND for the presumption as worded. **The
  disposition should almost certainly be a NAMING of the existing class rather than a new premise,
  plus one measurement.** Four carries:
    1. NO NEW PREMISE FOR THE SPECIFIC CLAIM. PREMISE-100, 085, 115, 141(1), 155(1) and 166(2) hold it
       between them, the last minted the day before this item was surfaced. Minting again is barred.
    2. THE DEFENSIBLE INCREMENT IS A NAME AND A CROSS-REFERENCE, NOT A CLAIM. Record that six ACTIVE
       premises are instances of ONE class — a declaration record and an observation record are
       different kinds of object — and import the vocabulary the three external disciplines already
       have (DRIFT, RECONCILIATION, REGISTERED-VERSUS-READY, SPEC-VERSUS-STATUS). That is an index
       entry, not a new finding, and it is what would have let the fleet see the sixth instance as the
       first.
    3. BEFORE THE GENERAL PREMISE IS MINTED, DISCHARGE PREMISE-135. Enumerate the registers in the
       system, state a termination criterion, and name ONE register kind not among the three that
       produced the generalisation — then predict in advance whether it has the defect and go and
       look. This is in-house, requires no authorisation, and is decisive either way. Until it is
       done, the generalisation is at the same standing every superseded abstraction had.
    4. THE ONE-COMMAND CHECK IS FREE AND SHOULD PRECEDE ALL OF THIS. For each scheduled job, compare
       what the register declares against the timestamp of the artefact the job is supposed to
       produce. Any job whose declaration is present and whose most recent artefact predates its last
       scheduled slot is the item, demonstrated in-system. Per PREMISE-115 the check must be on
       CONTENT, never on file existence — a file appearing is the very liveness test this item is
       about.

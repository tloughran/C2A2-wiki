SEARCH-AGAINST-PRESUMPTION-940:
  Date searched: 2026-09-10
  Original item: PRESUMPTION-940
  Original statement: [inferred] A configuration fix, once applied, stays applied — remediation needs
    verification at application but not thereafter.
  Risk if wrong, as stated at intake: Critical — all 218 revision flags become a record of intentions
    rather than states.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-940
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Generalised from ASSUMPTION-1298 — `permissionMode` absent for six days and the application
        rewriting its configuration from memory on relaunch — where the remedy recorded was one quit,
        one write and one relaunch, with no re-check scheduled thereafter.
      15b: Searched for challenging literature (2026-09-10), AGAINST direction only. Did not read the
        `for/` directory, `lit_search_returns.md`, or any 15a output for this item.
    Current status: CHALLENGED

  REGISTER CHECK, run before searching: the register holds two of the three limbs already, and one of
  them is close enough that this item should be read as a scope extension rather than a new finding.
    - **PREMISE-183** clause (1) (ACTIVE, 2026-08-25) states the governing rule in general form:
      "Verifying that a fix was implemented is explicitly NOT the same as verifying that recurrence
      has stopped, and a failed effectiveness check REOPENS the item rather than closing it with a
      note. This is the design the regulated world mandates for nonconformances (ISO 9001:2015 §10.2;
      FDA 21 CFR 820.100)." PRESUMPTION-940 is precisely the denial of that rule, restricted to
      configuration. The register therefore already answers the item, and answers it against.
    - **PREMISE-143** clause (2) (ACTIVE, 2026-08-05): "THE CORRECTION IS NOT SAFE: 14.8-24.4% of
      sampled post-release fixes in four operating systems were themselves incorrect and reached users
      (Yin et al. 2011). A correction issued and unreviewed carries a one-in-five-to-one-in-seven prior
      of being wrong, so 'corrected' is not a terminal state even for the single instance." This
      attacks the item from a second direction: not only may the fix not PERSIST, it may not have been
      RIGHT at application, and application-time verification of the wrong property will not reveal it.
    - **PREMISE-177** (ACTIVE) carries Yin et al. (2011) SOSP on 546 real-world misconfigurations,
      where environment and path errors are "a dominant and often SILENT failure cause" — the silence
      being the reason that a fix which stops holding produces no signal.
    - **PREMISE-181** (ACTIVE) holds the general class of "a run that silently fails to write and then
      parses the residue as its own output reports a clean verdict rather than an error." A
      configuration written and later overwritten is the same shape.
    CORRELATION DISCLOSURE: this file is substantially an APPLICATION of PREMISE-183 clause (1) and
    PREMISE-143 clause (2) to the configuration domain and must not be counted as independent
    corroboration of either. Its increment is the specific PERSISTENCE mechanism — an application that
    rewrites its own configuration from an in-process copy — which no existing premise names.

  Challenging evidence found: Yes.

  Sources:
    1. Zimmermann, T., Nagappan, N., Guo, P.J. & Murphy, B. (2012), "Characterizing and Predicting
       Which Bugs Get Reopened," ICSE 2012.
       [VERIFIED — full PDF retrieved and read this run; authors and affiliations confirmed from the
       paper itself. IMPORTANT NEGATIVE, recorded rather than glossed: the paper does NOT publish an
       absolute reopen rate. It reports "reopen ratios relative to the baseline percentages P and Q,
       which are the reopen rates for all bugs in Windows Vista and Windows 7 respectively," and P and
       Q are not disclosed. So this source supplies MECHANISM and PREDICTORS, not a base rate, and any
       claim of the form "X% of fixes fail to hold" cannot be sourced to it.] — What it does supply:
       from a survey of 358 Microsoft employees (20% response rate; 55% developers, 30% testers), six
       primary causes of reopens — bugs difficult to reproduce, misunderstood root causes, insufficient
       bug information, priority raised later, **regression bugs**, and **process-related issues**. The
       opening framing is the relevant one: "An underlying aspect is the effectiveness of fixes: if a
       fair number of fixed bugs are reopened, it could indicate instability in the software system."
       The paper's existence and its predictive modelling exercise are themselves the finding: in a
       professionally instrumented environment, whether a fix holds is treated as an open empirical
       question worth predicting, not as a default.

    2. "Revisiting reopened bugs in open source software systems," *Empirical Software Engineering*
       (2022, s10664-022-10133-6); with Shihab, E. et al., "Studying re-opened bugs in open source
       software," *Empirical Software Engineering* (2013, s10664-012-9228-6), covering Eclipse, Apache
       and OpenOffice.
       [SNIPPET-ONLY — search summaries only; neither opened; the 2022 paper's author list is NOT
       stated because I could not confirm it, and Shihab's co-authors are likewise unconfirmed.] —
       Reported: "around 6–10% of the bugs are reopened in four open source projects from the Eclipse
       product family." Bearing: this is the base rate the Zimmermann paper withholds, at
       snippet-level confidence. One fix in ten to one in sixteen does not hold in projects with
       version control, code review, regression suites and issue trackers — every structural support
       C2A2's configuration surface lacks. Treat the figure as indicative and re-verify before onward
       quotation.

    3. Yin, Z. et al. (2011), "How Do Fixes Become Bugs?", ESEC/FSE '11 — 14.8–24.4% incorrect-fix
       rate; and Yin, Ma, Zheng, Zhou, Bairavasundaram & Pasupathy (2011), "An Empirical Study on
       Configuration Errors in Commercial and Open Source Systems," SOSP '11 — 546 real-world
       misconfigurations, environment and path errors dominant and often silent.
       [REGISTER-HELD under PREMISE-143 and PREMISE-177 respectively; NOT independently verified this
       run; NON-INDEPENDENT of those premises.] — Bearing: the first attacks the item's premise from
       the correctness side, the second from the observability side. Together they say a configuration
       remediation has a substantial prior of being wrong at the moment it is applied, and that when
       configuration state is wrong the failure is frequently silent — so neither the error nor its
       later reversion generates a signal.

    4. Regulated-industry corrective-action practice: ISO 9001:2015 §10.2 and FDA 21 CFR 820.100;
       CAPA effectiveness-check practice as evidenced in FDA Form 483 observations.
       [MIXED: the standards are canonical and register-held via PREMISE-183; the 483 material is
       PRACTITIONER-GRADE (law-firm advisories and compliance vendors), SNIPPET-ONLY, and no
       peer-reviewed measurement of recurrence-after-CAPA was located.] — The convergent statements:
       CAPA plans must include "effectiveness evaluations to verify that the corrective measures
       successfully resolve the issue"; a documented 483 scenario involved "five CAPAs related to
       recurring manufacturing non-conformances that were closed without verification of effectiveness
       being performed"; CAPA deficiencies "have ranked in the top five 483 observations for medical
       device manufacturers for over a decade"; and the evidence accepted as demonstrating sustained
       improvement is "absence of recurrence over a justified period." Bearing: the entire regulatory
       architecture for corrective action is built on the proposition PRESUMPTION-940 denies. Two
       distinct verification steps are mandated — one at implementation, one after a defined interval
       — and the second exists because the first was found insufficient. That this is among the most
       frequently cited deficiency categories for more than a decade tells you it is also the step
       organisations most often skip, which is the item's exact failure mode occurring at industrial
       scale under regulatory compulsion.

    5. Configuration-drift and remediation-recurrence practitioner corpus.
       [GREY LITERATURE — vendor blogs and industry surveys. I searched specifically for peer-reviewed
       measurement of configuration-remediation persistence and did not find any; this line is
       included because the mechanism it describes matches the estate's case exactly, and it is
       labelled so it cannot be mistaken for research.] — Reported: "the same cloud misconfiguration
       resurfaces weeks later, the same alert fires again, and the cycle restarts"; "cloud failures
       often recur through templates, drift, and copied configurations rather than one-off mistakes";
       a worked example in which remediated servers were re-provisioned two weeks later from an
       unchanged golden image carrying the original defect; and a survey figure that "44% of
       organizations say vulnerabilities are reintroduced during deployment." The named metric —
       "vulnerability reopen rate" — exists as a category because practitioners found they needed it.

  Strength of challenge: Strong

  Summary: I found no source in any domain that treats application-time verification as sufficient,
  and several that exist specifically because it is not. The regulated world mandates two verification
  points for a corrective action — implementation and effectiveness-after-an-interval — and the second
  is among the most frequently cited deficiency categories in FDA inspections, which is to say it is
  both required and routinely skipped, exactly as here. Software engineering treats fix persistence as
  an open empirical question: Microsoft built a predictive model for it, and the open-source figure at
  snippet level is 6–10% of fixes reopened in projects with version control, review and regression
  suites. The correctness limb is worse than the persistence limb: Yin et al.'s 14.8–24.4%
  incorrect-fix rate, already register-held, means "corrected" is not a terminal state even for the
  single instance, and application-time verification confirms that a value was written, not that
  writing it was the right repair. The estate's specific mechanism makes all of this sharper rather
  than milder. ASSUMPTION-1298's finding is that the application rewrites its configuration file from
  an in-process copy on relaunch. That is not drift in the slow, entropic sense the vendor literature
  describes — it is an active writer with its own authoritative state, competing with the remediation.
  A fix applied while such a writer holds a stale copy has a defined and short expected lifetime, and
  its reversion is silent, because per Yin's SOSP corpus configuration errors are frequently silent
  and per PREMISE-181 a consumer reading the reverted file cannot distinguish it from a correct one.
  Finally, and this is the finding that determines the item's disposition: the register ALREADY holds
  the governing rule. PREMISE-183 clause (1) says in terms that verifying implementation is not
  verifying that recurrence stopped. PRESUMPTION-940 is that premise's negation, restricted to
  configuration, and it has been operating unnoticed alongside it.

  Specific risks: (a) The intake's own statement of the risk is correct and I can add only that it is
  measurable: if fixes do not persist and nothing re-checks, the 218 revision flags are a record of
  intentions. On the open-source reopen figure alone — 6–10%, in far better-instrumented conditions —
  the expected number of those flags that no longer describe reality is in the mid-teens to low
  twenties, and the estate cannot currently name which. (b) The silent-reversion risk is the one with
  no floor: a reverted configuration produces no error, so the estate's belief about its own
  configuration state is bounded above by its last verification and has no lower bound, which is the
  2026-09-09 flag's structure appearing in a fourth place. (c) The competing-writer risk is specific
  and probably the highest-probability failure here: any fix to a file that an application rewrites
  from memory will be lost at the next relaunch of that application unless the write order is
  controlled. The recorded remedy — quit, write, relaunch — is the correct sequence, which means
  someone understood the mechanism; the presumption is that the sequence, having worked once, has
  settled the matter. It has not, because every subsequent relaunch is another draw. (d) Correctness
  risk per Yin: roughly one remediation in five to seven is wrong on application, and an
  application-time check that reads back the value it just wrote is the check least capable of
  detecting that class.

  Mitigations available: All cheap; two are already required by ACTIVE premises and simply unenforced
  on this surface — which is itself the pattern PREMISE-171's run note called the highest-value
  observation in its cohort.
    (i)   **Apply PREMISE-183 clause (1) to configuration remediations.** Define the effectiveness
          condition at the time of the fix and test it after a stated interval. A failed check REOPENS
          the item. This is not new policy; it is enforcement of existing policy on an unenforced
          surface.
    (ii)  **Re-check after the event that threatens the fix, not after an arbitrary period.** For a
          competing writer the threatening event is the application's next launch. The check is: read
          the file after the next relaunch. That is one command, it is decisive, and it is the
          discriminating test PREMISE-107 licenses applying directly because it is cheap, reversible
          and immediately observable.
    (iii) **Store expected configuration state as data and diff continuously** — the declaration-plus-
          divergence architecture PREMISE-171 already endorses (Kubernetes spec/status, ITSM drift
          reconciliation), including its load-bearing negative: do not answer this with a heartbeat.
          A content hash per configuration file, compared against an expected value, converts silent
          reversion into an event. This is the same content-hash build PREMISE-200's operational
          consequence already asks for, so it serves two open items at once.
    (iv)  **Audit the 218 revision flags against current state rather than against their own text.**
          This is the retrospective test named below and it is the only way to convert the intake's
          Critical risk statement from a worry into a number.
    (v)   A caution: do not conclude from this file that every remediation needs a standing monitor.
          The register already mints faster than it closes, and the 2026-09-09 flag's TRIR evidence
          warns against adding instruments reflexively. The stratified form is the affordable one —
          re-check where a competing writer, a provisioning path, or a shared template exists, and
          record the rest as verified-at-application-only so that the epistemic status is at least
          visible.

  Search scope: Moderate for coverage, mixed for quality, with one genuine full-text verification. Two
  queries; one full-text retrieval attempted and SUCCEEDED (Zimmermann et al., read in full — and the
  reading is what revealed that the paper does not publish the base rate the search summary implied,
  which is exactly the class of error this register has been burned by before). Literatures covered:
  bug reopening and fix effectiveness; configuration-error empirical studies (via register);
  corrective-action verification in regulated quality systems; configuration-drift practitioner
  material. NOT covered, and these are real gaps: infrastructure-as-code drift measurement in the
  peer-reviewed literature, which I believe exists and did not reach; idempotence and convergence
  guarantees in configuration-management systems (Puppet/Chef/Ansible formal work), which is the most
  directly relevant CS literature to "does a fix stay applied" and which I did not search at all; and
  any peer-reviewed measurement of configuration-remediation persistence specifically — I searched for
  it directly and found only vendor material, which I am recording as a genuine literature gap rather
  than as insufficient searching, though a broader search would be warranted before that gap is
  asserted with confidence.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-940
  Strongest counterargument: The presumption is the exact negation of a rule this estate validated
  five weeks ago and has been carrying ACTIVE ever since. PREMISE-183 clause (1) says, in terms, that
  verifying a fix was implemented is not the same as verifying that recurrence has stopped, and cites
  the two regimes — ISO 9001:2015 §10.2 and 21 CFR 820.100 — that make the second check mandatory. The
  regulated world does not require two verification points out of ceremony; it requires them because
  the first was found insufficient across decades of inspection, and "closed without verification of
  effectiveness being performed" is a documented, recurring FDA observation category. So the strongest
  form of the challenge is not that the literature disagrees with the presumption. It is that the
  presumption is a lapse in applying a rule the estate already holds, on a surface where nobody
  noticed it applied. Now the domain specifics, which make it worse rather than better. In software,
  fix persistence is treated as an open empirical question by people with far better instrumentation:
  Microsoft built a predictive model for bug reopening across Windows Vista and Windows 7, and the
  open-source figure is 6–10% reopened in projects with version control, code review and regression
  suites. C2A2's configuration surface has none of those. Then Yin et al.: 14.8–24.4% of post-release
  fixes were themselves incorrect and reached users — so even at the moment of application, roughly
  one in five to one in seven remediations is wrong, and reading back the value you just wrote is the
  check least able to detect it. And then the mechanism that makes this item urgent rather than
  theoretical. ASSUMPTION-1298 found that the application rewrites its configuration from an
  in-process copy. That is not entropy; it is an adversary with a clock. The fix's expected lifetime
  is one relaunch. Its reversion is silent, because configuration errors are silent by nature and a
  consumer reading a reverted file cannot tell it from a correct one. Which means the estate's
  configuration knowledge decays at a rate it does not measure, in a direction it cannot see, on 218
  flags it treats as states. The intake called that Critical. On this evidence the word is right.
  What would need to be true for C2A2 to be safe: One of three, and the estate satisfies none. (1) No
  process other than the remediation writes the configuration. ASSUMPTION-1298 establishes the
  opposite for at least one file, and the honest reading is that this is the general case for
  application-managed configuration rather than a peculiarity of one app. (2) A reverted configuration
  produces an observable failure. It does not: Yin's SOSP corpus makes silence the norm for
  configuration errors, and PREMISE-181 holds that a consumer reading a stale artefact reports a clean
  verdict. (3) The estate re-reads configuration state on a cadence tied to the threatening event.
  There is no such re-read. A weaker sufficient condition worth naming: if the 218 revision flags are
  never consulted as evidence of current state — if they are read only as history — then the intake's
  Critical risk does not bite, because nothing is relying on them being true. That is a disjunction
  the estate can settle by enumerating the flags' consumers, and it should, because if the flags DO
  have consumers then their staleness is load-bearing.
  How to test: Three tests, retrospective, in-house, and the first is decisive and small.
  **Test A, the one-command test on the founding instance.** After the application's next relaunch,
  read the configuration file and check whether `permissionMode` is present. Present → the fix held
  across at least one relaunch and the competing-writer hypothesis is weakened. Absent → the
  presumption is falsified on its founding case, in one observation, and every remediation to an
  application-managed file in the register is suspect by the same mechanism. Note that this test has a
  deadline built into it: it must be run after a relaunch, not at an arbitrary time, or it measures
  nothing. **Test B, the flag audit, which converts the Critical risk into a number.** Take all 218
  revision flags. For each, extract the state it asserts and check that state against the system NOW.
  Three columns: still true, no longer true, not checkable. The middle column is the count of flags
  that are records of intentions rather than states, and the third column is the count the estate
  cannot even ask about — which may be the more interesting number. Sample first if 218 is too many;
  a random 30 gives a usable proportion with an honestly wide interval, per PREMISE-136's scope guard.
  **Test C, the persistence base rate.** For every configuration remediation in the last 90 days,
  record whether any subsequent check exists at all. If the answer is "none, in any case", then the
  presumption has never been tested here even once, and the register's entire configuration section
  rests on an untested premise — which is a finding in its own right and is cheaper to establish than
  either of the other two.

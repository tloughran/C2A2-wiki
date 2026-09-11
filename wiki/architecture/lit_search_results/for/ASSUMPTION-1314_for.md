SEARCH-FOR-ASSUMPTION-1314:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1314
  Original statement: "Status file rewritten as `PASS` with an explicit `VERIFIED-NOT-REGENERATED`
    qualifier — **a bare `FAIL` would have fired `morning-system-health` over feeds that are genuinely
    current, and a bare `PASS` would have claimed work I didn't do.**"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1314
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed. The day's one status decision made *for* the downstream
        reader's alarm rather than for the register, and the fourth item that day to end in a request for
        a ruling from a channel silent since 2026-08-27. The direction of the protection is surfaced as
        PRESUMPTION-955.
      15a: Searched for supporting literature; found strong, standardised support for the third-state
        claim across four independent engineering traditions, and strong empirical support for the
        false-alarm-cost premise.
    Current status: SUPPORTED

  Register pre-check: Two ACTIVE premises bear very closely and one of them may already settle it.
    - PREMISE-141: "ABSENCE OF A REPORT IS A THIRD TERMINAL STATE, NOT A VALUE OF THE OTHER TWO... (1)
      OMISSION IS NOT CRASH. Cristian's failure-semantics taxonomy separates a component that runs and
      produces no response..." This is the same proposition at one remove, and it is ACTIVE. The new
      content ASSUMPTION-1314 adds is the *repair* (invent an explicit third value) rather than the
      diagnosis.
    - PREMISE-167: "AN ESCALATION AND A MEASUREMENT ARE DIFFERENT OBJECTS AND MUST BE STORED AS DIFFERENT
      OBJECTS... an escalation expressed only as a WITHHELD PASS-MARK has no representation on disk
      distinct from staleness, so any later writer re-computing the same predicate silently..." Directly
      on point and arguably dispositive in favour.
    - PREMISE-063: gap-honest visualisation — a dashboard must distinguish measured from inferred values
      and must encode absence as distinct from a true zero.
    - PREMISE-100: a liveness signal is not evidence of correctness, and a health check that cannot
      execute in its runtime context reports as passing rather than as absent.
    - PREMISE-185: before a joint-state field is written, establish that the instrument set can decide
      the joint state at all; a joint reading must be carried qualified, not as prose. NOTE: this cuts
      *against* the chosen implementation — `PASS` + a prose qualifier is exactly the "carried as prose"
      form PREMISE-185 warns about.
    Searched anyway per OPEN-192.

  Supporting evidence found: Yes

  Sources:
    1. ISO/IEC 9646-3 / TTCN and TTCN-3 (ETSI ES 201 873). — SECONDARY (verdict set retrieved from
       multiple independent descriptions including ETSI TTCN-3 library documentation; standard text not
       fetched) — The predefined verdicts in TTCN-3 are `pass`, `inconc`, `fail`, `error`, `none`.
       `inconc` is defined as "a situation where neither a pass nor a fail can be assigned"; `error`
       denotes a fault in the *test device* rather than in the system under test; `none` is the
       not-yet-assigned initial value. This is the strongest single source: an international conformance-
       testing standard that found a two-valued verdict vocabulary insufficient and standardised five,
       including two states that both mean "the test apparatus could not decide."
    2. Nagios / Icinga plugin exit-code convention: 0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN. — SECONDARY
       (convention confirmed from Nagios support-forum documentation retrieved via search; the canonical
       plugin development guidelines page could not be fetched — see Caveats) — UNKNOWN is documented to
       indicate "a condition where the check cannot give a clear, unambiguous status, and does not
       necessarily indicate a problem," and is conventionally routed to a different notification path
       than CRITICAL. This is the direct operational analogue: the monitoring ecosystem the status file
       feeds already has a name for the state the run needed.
    3. ANSI/ISA-18.2-2016, Management of Alarm Systems for the Process Industries. — SECONDARY (standard
       PDF located, alarm-state-diagram content not read in full) — Specifies an alarm lifecycle with
       multiple distinct states and requires ongoing alarm-system performance monitoring, on the premise
       that alarm systems degrade when low-value alarms accumulate. Supports the design principle, not
       the specific three-state claim.
    4. Clinical alarm fatigue literature — multiple retrieved sources. — SECONDARY — 72-99% of patient
       monitoring alarms are technically false or clinically irrelevant; 80-99% of ECG monitor alarms are
       false or clinically insignificant; Chambrin et al. measured monitor alarm sensitivity 97%,
       specificity 58%, positive predictive value 27%. The documented consequence is desensitisation:
       high false-positive rates "train practitioners to ignore alarms," and caregivers disable, silence
       or ignore them. This is the empirical basis for the run's asymmetric-cost reasoning: a bare FAIL
       over genuinely current feeds is a false alarm, and false alarms have a measured, cumulative cost
       to the detector's future credibility.
    5. Three-valued logic in data systems (SQL NULL; IEEE 754 NaN; HTTP 5xx-vs-4xx separation; POSIX exit
       codes). — SECONDARY, ILLUSTRATIVE ONLY — A convergent design pattern across unrelated systems:
       when a binary value cannot represent "not determinable," systems add a distinct third token rather
       than overload one of the two. Named as convergence, not as evidence.

  Strength of support: Strong (for the claim that a binary vocabulary cannot carry the third state);
                       Moderate (for the claim that inventing a third value is the right repair);
                       Weak (for the specific implementation chosen).

  Summary: Three limbs, and they should be rated separately. Limb (a) — that a two-valued PASS/FAIL
    vocabulary cannot carry "verified current but not produced by me" — is strongly supported and is
    close to a settled engineering result. ISO/IEC 9646's TTCN-3 standardised five verdicts precisely
    because two were inadequate, and it separates the two cases this item cares about: `fail` (the system
    is wrong) from `error` (the test apparatus could not run), which is exactly the sandbox-cannot-
    regenerate case. Limb (b) — that adding a third value is the correct repair — is supported by the
    same sources plus the operational convention already present in the alarm consumer (Nagios UNKNOWN,
    exit code 3), and the alarm-fatigue literature supplies the cost that justifies it: false alarms are
    not free, they degrade the detector, and the measured PPVs in clinical monitoring (27%) show how far
    that degradation goes. Limb (c) — that the *specific* implementation, `PASS` plus a prose qualifier,
    is the right form — is the weakest and I rate it Weak. Every source found implements the third state
    as a distinct *value in the enumeration*, not as the optimistic value with an annotation. That is
    PREMISE-167 and PREMISE-185 both.

  Caveats:
    - The implementation chosen inherits the failure mode it was trying to avoid. A consumer that reads
      the status token and not the qualifier sees `PASS` and infers regeneration — which is precisely
      PREMISE-188 ("an evidentiary qualifier travels with the claim or it does not travel") and
      PREMISE-099 ("a documented-discrepancy flag that annotates without gating does not prevent the
      discrepant value from being emitted"). A third enumerated value (`INCONCLUSIVE` / `UNKNOWN` /
      `VERIFIED-NOT-REGENERATED` as a token, not a suffix) is what the literature actually supports.
    - The asymmetric-cost argument is not symmetric in the direction the run assumed. Alarm-fatigue
      evidence establishes the cost of *false* alarms; it says nothing about the cost of a missed
      detection in this system, and the run did not price that side. PRESUMPTION-955's framing — that the
      vocabulary protects the alarm before it protects the reader — is a live concern and this search
      does not dispose of it.
    - Domain transfer: clinical alarm PPV figures come from continuous physiological monitoring with
      thousands of alarms per patient-day. A daily telemetry status check has a completely different
      arrival rate and the desensitisation dynamics may not apply at n≈1/day. The direction transfers;
      the numbers do not.
    - Could not retrieve: the Nagios plugin development guidelines page (nagios-plugins.org/doc/
      guidelines.html) was outside the fetch provenance set. The exit-code convention is well attested in
      the retrieved forum documentation but the canonical specification was not read.
    - The item ends in a request for a ruling from a channel silent since 2026-08-27. Nothing in this
      literature substitutes for that ruling, and under PREMISE-102 the silence converts the run's
      one-time question into a standing undecided policy.

  Search scope: comprehensive search — alarm management standards (ANSI/ISA-18.2), monitoring check-state
    vocabularies (Nagios/Icinga UNKNOWN), conformance-testing verdict sets (ISO/IEC 9646, TTCN-3),
    alarm fatigue and false-alarm rates / positive predictive value in clinical monitoring, asymmetric
    costs of false alarm vs missed detection, three-valued logic in data systems.

  Recommendation: SUPPORTED — resting on limbs (a) and (b). The strongest single source is ISO/IEC 9646 /
    TTCN-3, which is an international standard that settled this exact design question in favour of a
    verdict set larger than two, with a named state for "the apparatus could not decide." Recommend the
    ruling requested by the run be answered in the direction it proposed, but with the implementation
    amended: make the third state an enumerated token, not `PASS` with a qualifier, and give
    `morning-system-health` a distinct routing rule for it (the Nagios UNKNOWN pattern).

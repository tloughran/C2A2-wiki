SEARCH-AGAINST-ASSUMPTION-1684 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-12
  Original item: ASSUMPTION-1684
  Original statement: A QC sweep reported "the review was lighter than a full read" and checked
    commentaries mechanically (sections, PRS phrasing, leaked labels), on the stated basis that each had
    had a full review on 09-19 or 09-20. (MONITOR-618 gloss: after one full review, later structural
    checks are enough to keep a text's pass status.)
  Under test this cycle (MONITOR-618, Medium): Owed — "a primary source on checklist-vs-holistic
    re-review efficacy, or an in-house measure". Cycle 0 both directions found no primary evidence
    (15b: NO-CHALLENGE-FOUND, Weak). I searched the auditing rule for relying on prior-period evidence
    (closest codified analogue to "prior full review + lighter later checks") and the inspection
    literature on checklist vs other reading techniques.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read lit_search_results/for/ or 15a sections of
    lit_search_returns.md. I read my own cycle-0 file (Urbach 2014; Shojania 2007; Wright 1988; ISA 330
    cited unverified) and did not re-use them except ISA 330, now read in full. No fetch refused as
    "already fetched".

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: ASSUMPTION-1684
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a (2026-09-28): Extracted from 8c58d8ca (Summa QC); quote confirmed in transcript.
      15a (cycle 0): [not read — independence]
      15b (cycle 0, 2026-09-29): NO-CHALLENGE-FOUND (Weak); ISA 330 cited as unverified background.
      15c: DISPOSITION-1002 → MONITOR-618 (Medium).
      15d (2026-10-11): re-triggered, cycle 0 → 1.
      15b (cycle 1, 2026-10-12): 2 searches (audit rollforward/prior-period reliance; checklist vs
        ad hoc vs scenario reading); 2 fetches (ASA 330 Requirements, full; Porter author page, full).
    Current status: PARTIALLY-CHALLENGED
    Sources this cycle: ASA 330 (ISA 330 conforming) paras 12–16 [full text]; Porter, Votta & Basili
      1995 via A. Porter's UMD page [full page; paper itself not read]; CAQ/securityscientist
      rollforward guidance [search-result only].
    Date: 2026-10-12

  EVIDENCE GRADE: MODERATE for the boundary condition (codified standard read in full); PRELIMINARY for
    the efficacy claim (author summary of a replicated experiment). Still no primary study of
    checklist-vs-holistic RE-review of prose.

  Challenging evidence found: Partial (boundary conditions; upgraded from cycle 0's "none")

  Sources:
    1. Auditing and Assurance Standards Board (AU), ASA 330 (Dec 2021), Requirements paras 13–15
       (conforming to IAASB ISA 330). [fetched, full text] Relying on evidence "obtained in previous
       audits" is permitted ONLY after establishing "continuing relevance and reliability" by
       "obtaining audit evidence about whether significant changes ... have occurred", via "enquiry
       combined with observation or inspection"; if changes occurred, retest in the current period; if
       not, still retest "at least once in every third audit", and "test some controls each audit";
       over a significant risk, "test those controls in the current period" with no carry-forward.
       Para 16: absence of detected misstatements is not evidence of control effectiveness. Bearing:
       the discipline that formalised "full review once, lighter checks after" permits it only with
       (a) an affirmative check that the object has not changed since the full review, (b) a maximum
       carry-forward horizon with full re-test, (c) rotating partial full-tests every cycle, and (d) no
       carry-forward for high-risk items. The 8c58d8ca sweep satisfies none of these explicitly: it
       checked structure, not change-since-review, and set no horizon.
    2. Porter, A. A., Votta, L. G. & Basili, V. R. (1995). "Comparing Detection Methods for Software
       Requirements Inspections: A Replicated Experiment." IEEE TSE 21(6). As summarised on A. Porter's
       UMD page [fetched, full page; paper NOT read]: 48 graduate students + 21 Lucent professionals;
       "Checklist reviewers were no more effective than Ad Hoc reviewers"; Scenario reviewers (specific,
       distinct responsibilities) had higher detection rates; "one of the most widely replicated
       experiments". Bearing: even in initial inspection, a general checklist adds no detection over
       unstructured reading; a mechanical checklist is unlikely to catch the defect classes a full
       semantic read targets. Transfer caveat: requirements documents, initial review, human readers —
       not re-review of interpretive prose by an LLM.
    3. Practitioner rollforward guidance (CAQ alert 2013-11; securityscientist "rollforward testing").
       [search-result only] Inquiry alone is weak evidence of no change; the risk is "anything broke or
       was bypassed during the period you didn't explicitly test".

  Strength of challenge: Moderate (up from Weak)

  Summary: The assumption is not refuted — auditing practice explicitly allows carrying forward a prior
    full test. But it allows it only under conditions the QC sweep did not meet: an affirmative
    check that nothing changed since the full review, a bounded carry-forward horizon (every third
    cycle at most), rotation of full re-tests, and no carry-forward for high-risk items. The inspection
    literature adds that general checklists catch no more than unstructured reading in the first place.

  Specific risks: texts edited after 09-19/20 (re-ingest, citation fixes, length trims) keep "pass"
    status on structure alone; a pass carried indefinitely becomes a stale certificate; the in-house
    measure (how many mechanical-only passes later fail full re-review) is never run because nothing
    triggers a full re-review.

  Mitigations available: record a content hash at full review and make "unchanged since full review"
    the first mechanical check (change → full re-review); set a carry-forward horizon (e.g. full re-read
    at least every third QC cycle); full-re-read a rotating sample each sweep (this also produces the
    owed in-house measure); exclude high-risk texts (open escalations, length flags) from carry-forward.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1684 / MONITOR-618
  Strongest counterargument: The profession that has thought hardest about relying on last period's
    full test allows it only if you first show the thing has not changed, and even then forbids
    relying on it for more than two further periods or for anything high-risk. A structural checklist
    does not show "unchanged"; it shows "still well-formed". And controlled experiments find general
    checklists catch no more defects than unstructured reading. So "had a full review on 09-19" is a
    reason to look lighter only if you have also proved nothing changed since — which the sweep did not.
  What would need to be true for C2A2 to be safe: an unchanged-since-review check (hash/diff), a
    carry-forward horizon, and rotating full re-reads.
  How to test: in-house — full re-read a random sample of commentaries that passed mechanical-only
    sweeps since 09-20; report n and failures. Diff each against its 09-19/20 version first; stratify
    failures by changed vs unchanged.

  Search scope: preliminary — 2 searches, 2 fetches. Owed primary source (checklist-vs-holistic
    RE-review of prose) still not found; codified analogue now in hand.

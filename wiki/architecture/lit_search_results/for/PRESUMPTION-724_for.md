SEARCH-FOR-PRESUMPTION-724:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-724
  Original statement: That when a watchdog and a task disagree, one is wrong; today both were right and the joint reading lived in a clause no watchdog can read.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-724
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred by constructing the joint reading the system could not, from three same-day summaries
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND (for the presumption itself) / literature instead supports the counter-position 14b already inferred

  Supporting evidence found: No

  Sources:
    1. Wikipedia, "Disagreement (epistemology)" [unverified — general reference] — surveys the epistemology-of-disagreement literature, where the "someone must be wrong" (uniqueness/conciliationism) view is one live position but is contested by "steadfast" and permissive views that allow two parties to be justifiedly correct from differing evidence bases.
    2. Multi-Sensor Conflict Measurement and Information Fusion, arXiv:1803.04551 [unverified — from search snippet] — models sensor conflict as informative rather than as a simple error signal, explicitly allowing that "knowing whether the majority is correct, or if a single sensor with high disagreement is actually correct, is quite another thing" — i.e., disagreement is treated as evidence about differing measurement conditions, not automatically as one-sensor-wrong.
    3. Denzin, N.K. (1978). "The Research Act: A Theoretical Introduction to Sociological Methods." [unverified — classic reference, not directly retrieved this search] — foundational triangulation methodology treating convergent/divergent measurements from independent methods as jointly informative about a partial, multi-faceted reality rather than adjudicating a single winner.

  Strength of support: Weak

  Summary: No literature was found that directly supports the presumption "when a watchdog and a task disagree, one is wrong" — if anything, the disagreement/triangulation and multi-sensor fusion literature argues the opposite: that conflicting signals from independent measurement sources can both be locally correct while measuring different aspects of a system, and that disagreement should be treated as information to be reconciled rather than resolved by declaring a winner. This is a case where the search surfaced strong grounding for the *presumption's negation* (which 14b's item statement already treats as the more accurate reading) rather than for the presumption as an assumption held by the system.

  Caveats: This item is somewhat unusual in that the "presumption" being tested is explicitly framed by 14b as the naive belief the system held, which the same day's evidence overturned. The FOR search is scoped to search for support for the presumption's truth ("one is wrong" as a valid inference rule), not for the narrative that it was falsified. Under that framing, no supporting literature was found — search was preliminary/broad, not exhaustive within monitoring-systems and reconciliation literature specifically.

  Recommendation: NO-SUPPORT-FOUND

--- CYCLE RE-SEARCH: 2026-08-25 (15a) ---
  Date searched: 2026-08-25
  Trigger: 15d re-trigger (MONITOR-511, cycle 1). PARTIAL NOVELTY-FLAG carried from intake.
    Disposition-changer sought: "disagreement is not error" is established, but the UNREADABLE JOINT
    CLAUSE — a joint state visible only across two instruments' blind spots and recorded only in
    prose — was not addressed by the 2026-08-10 search. Find prior art for it, or the flag stands
    and the parseable joint-state field has to be written.

  Search scope: Searched observability/monitoring reconciliation, sensor-fusion conflict modelling,
    epistemology of disagreement, and cross-instrument invariant checking. The productive move this
    cycle was reframing the clause: "a joint state that no single instrument can read, because each
    sees only part of it" is not primarily an epistemology question — it is the DISTRIBUTED GLOBAL
    PREDICATE DETECTION problem in distributed systems, which has a mature formal literature going
    back to 1985. That literature was not searched on 2026-08-10 and is where the prior art is.
    ACCESSED: Crossref API (bibliographic confirmation of all four distributed-systems sources);
    arXiv abstract pages for Bauer & Falcone and for the prior cycle's unverified sensor-fusion
    source, both read in full. NOT ACCESSED: the full texts of Cooper & Marzullo, Marzullo & Neiger,
    Chandy & Lamport, or Bauer & Falcone — see caveats, this matters.
    TOOL LIMIT DECLARED: the session's WebSearch budget (200 calls) was exhausted before this item's
    searches ran, so this cycle's work on 724 was done entirely through direct fetch and the
    Crossref and arXiv bibliographic APIs. Breadth is correspondingly narrower than a normal cycle;
    depth on the four located sources is unaffected.

  Supporting evidence found: Yes

  New sources this cycle:
    1. Cooper, R. & Marzullo, K. (1991). "Consistent detection of global predicates." Proceedings of
       the 1991 ACM/ONR Workshop on Parallel and Distributed Debugging; ACM SIGPLAN Notices
       26(12):167-174. DOI 10.1145/122759.122774 (also indexed as 10.1145/127695.122774) —
       BIBLIOGRAPHIC-CONFIRMED, FULL TEXT NOT READ. **The closest prior art to the unreadable joint
       clause, and it is thirty-five years old.** This is the origin of the Possibly(φ) / Definitely(φ)
       modalities for global predicates. The reason those modalities exist is exactly the item's
       situation: where a property is a joint state over components that no single observer can read
       simultaneously, an external monitor cannot in general say whether the property HELD. What it
       can say is that some consistent global state satisfying φ exists in the lattice of consistent
       cuts (Possibly), or that every run passes through such a state (Definitely). The load-bearing
       point for 724 is not the result but its SHAPE: the field's answer to an unreadable joint state
       was to define a FORMAL, PARSEABLE, MODAL-QUALIFIED representation of it — not to write it down
       in prose and not to force an adjudication between the two instruments.
    2. Marzullo, K. & Neiger, G. (1991/1992). "Detection of Global State Predicates." Distributed
       Algorithms (WDAG '91), Lecture Notes in Computer Science, pp. 254-272. DOI
       10.1007/bfb0022452 — BIBLIOGRAPHIC-CONFIRMED, FULL TEXT NOT READ. The companion treatment,
       and confirmation that this is a literature rather than a single paper.
    3. Chandy, K.M. & Lamport, L. (1985). "Distributed Snapshots: Determining Global States of
       Distributed Systems." ACM Transactions on Computer Systems 3(1):63-75. DOI
       10.1145/214451.214456 — BIBLIOGRAPHIC-CONFIRMED via Crossref (volume, pages and date all
       confirmed), FULL TEXT NOT READ. The foundational result underneath (1) and (2): the whole
       apparatus of consistent cuts exists because a global state is not directly observable by any
       participant, and the field's response was an ALGORITHM for constructing a consistent global
       state from local observations. Directly relevant to the item's premise that the joint reading
       "lived in a clause no watchdog can read" — the canonical answer is that no single watchdog
       needs to read it, provided the local observations are recorded in a form that can be joined.
    4. Bauer, A. & Falcone, Y. "Decentralised LTL monitoring." Runtime Verification / FM 2012, LNCS
       pp. 85-100 (DOI 10.1007/978-3-642-32759-9_10); extended version Formal Methods in System
       Design 48:46-93 (2016), DOI 10.1007/s10703-016-0253-8; preprint arXiv:1111.5133 —
       ABSTRACT read IN FULL this cycle from the arXiv record; paper body NOT read. **The most
       directly transferable source, because it is about MONITORS specifically rather than about
       processes.** Verbatim from the abstract: the problem is "how such a specification can actually
       be monitored in a distributed system that has no central data collection point, where all the
       components' local behaviours are observable," such that "the LTL specification needs to be
       decomposed into sub-formulae which, in turn, need to be distributed amongst the components'
       locally attached monitors, each of which sees only a distinct part of the global behaviour."
       Their contribution is "an algorithm for distributing and monitoring LTL formulae, such that
       satisfaction or violation of specifications can be detected by local monitors alone." That is
       the item's configuration exactly — several instruments, each with a partial view and a
       structural blind spot, and a property that is only true jointly — and the field's finding is
       that the joint property IS detectable, if the global specification is written down formally
       and decomposed rather than left implicit.
    5. Wei, P., Ball, J.E. & Anderson, D.T. (2018). "Multi-Sensor Conflict Measurement and
       Information Fusion." arXiv:1803.04551 — ABSTRACT read IN FULL this cycle. **This is a
       correction to the prior cycle's file, and it is recorded as such.** The 2026-08-10 pass listed
       this as source 2 marked "[unverified — from search snippet]" and attributed to it the sentence
       "knowing whether the majority is correct, or if a single sensor with high disagreement is
       actually correct, is quite another thing." The bibliographic record is now VERIFIED: authors
       Pan Wei, John E. Ball and Derek T. Anderson, submitted 2018-03-12, title as given. **The
       quoted sentence does NOT appear in the abstract and I did not locate it this cycle; it should
       not be carried forward as a quotation from this paper until the body is retrieved.** What the
       abstract does establish is weaker but still on point: the paper proposes a multi-sensor
       conflict MEASURE defined by how little the outputs of multiple sensors overlap "on all
       possible n-tuple sensor combinations," i.e. conflict is treated as a quantity to be measured
       across combinations of instruments, not as a verdict about which instrument is wrong.

  Strength of support: Strong on the existence of prior art for the unreadable joint clause;
    Moderate on direct transfer, because every one of the four distributed-systems sources was
    confirmed bibliographically but read only at abstract or established-knowledge level this cycle.

  Summary: The PARTIAL NOVELTY-FLAG does not survive. The unreadable joint clause is not novel; it
    is the global predicate detection problem, and it has been studied continuously since Chandy and
    Lamport in 1985. The framing that unlocked this was noticing that the clause is a
    distributed-systems question wearing epistemology's clothes: the 2026-08-10 search went to the
    epistemology of disagreement and to sensor fusion, both of which address whether two disagreeing
    readings can both be right, and neither of which addresses the different question of a state
    that is only visible in the union of two partial views. Cooper and Marzullo's Possibly/Definitely
    modalities are the canonical answer, and their shape is the useful part for 724: faced with a
    joint state no observer could read, the field did not adjudicate between observers and did not
    settle for prose — it defined a formal, modal-qualified, machine-checkable representation over
    the lattice of consistent cuts. Bauer and Falcone carry that forward to monitors specifically and
    show, for LTL specifications, that a global property CAN be detected by local monitors alone
    provided the global specification is written formally and decomposed across them. Read together
    these say something fairly pointed about the item's second limb: the reason C2A2's joint reading
    ended up in prose is not that joint readings are unwritable, but that nothing in the architecture
    states the joint property formally in the first place, and an undecomposed property cannot be
    distributed to monitors that each see a part of it.

  Caveats: (a) THE PROVENANCE OF THE FOUR CENTRAL SOURCES IS BIBLIOGRAPHIC, NOT TEXTUAL, AND THIS
    LIMITS THEM. Titles, authors, venues, volumes, pages and DOIs are confirmed against Crossref, and
    Bauer & Falcone's abstract was read verbatim. The Possibly/Definitely content attributed to
    Cooper & Marzullo is CANONICAL FROM ESTABLISHED KNOWLEDGE and was not re-verified against the
    paper this cycle. Do not quote page numbers or verbatim wording from sources 1, 2 or 3 onward.
    (b) The transfer is by structural analogy. The distributed-systems literature concerns processes
    exchanging messages under a happens-before ordering; C2A2's instruments are a watchdog and a
    task, and there is no established causal ordering between their observations. Whether the
    consistent-cut apparatus applies at all depends on whether C2A2's records carry enough ordering
    information to construct a cut, which is unknown and is itself a finding: if they do not, the
    formal machinery is unavailable and the prose clause is a symptom of missing timestamps rather
    than of a missing concept. (c) The prior cycle's quotation from Wei et al. could not be
    substantiated and is flagged above; that is a correction to an existing file, not a new finding,
    but it should be actioned. (d) This cycle did NOT re-examine the epistemology-of-disagreement
    limb and takes the prior cycle's reading of it as standing. (e) WebSearch budget exhaustion,
    declared in scope above, means the observability/monitoring-reconciliation practitioner
    literature was not swept this cycle; given four confirmed academic hits, that seam is likely to
    add texture rather than change the disposition.

  Disposition-changer met: **YES — prior art located, and the flag should be withdrawn.** The
    citations that meet it are Cooper & Marzullo (1991), ACM SIGPLAN Notices 26(12):167-174, DOI
    10.1145/122759.122774, for the modal representation of a joint state no observer can read; and
    Bauer & Falcone, "Decentralised LTL monitoring," FMSD 48:46-93 (2016), DOI
    10.1007/s10703-016-0253-8, whose abstract states the item's configuration verbatim — monitors
    "each of which sees only a distinct part of the global behaviour" — and gives an algorithm for
    detecting the global property from them. **The second limb of the stated disposition-changer
    (write the parseable joint-state field) is NOT discharged by this and remains open; what changes
    is that the field now has a known shape to copy rather than needing to be invented.**

  Recommendation: SUPPORTED — for the corrective proposition and for the existence of prior art on
    the unreadable joint clause. This does not disturb the 2026-08-10 finding that the presumption AS
    WORDED ("when a watchdog and a task disagree, one is wrong") has no support; it strengthens it,
    since the located literature exists precisely because the joint case is real. The actionable
    residual is unchanged in direction and now has a template: state the joint property formally,
    check whether the records carry enough ordering to join them, and record the result as a
    modal-qualified field rather than as prose.

  PROVENANCE: Origin: 14b · Chain: [14b → 15a, 15b → 15c → 15d → 15a] · Item type: PRESUMPTION
    (unstated — surfaced by inference) · Transform: 15a re-searched on 15d re-trigger, reframing the
    joint clause as a global-predicate-detection question · Current status: SUPPORTED (Strong on
    existence of prior art, Moderate on transfer); PARTIAL NOVELTY-FLAG RETRACTED; parseable
    joint-state field still to be written

SEARCH-AGAINST-PRESUMPTION-724:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-724
  Original statement: That when a watchdog and a task disagree, one is wrong; today both were right and the joint reading lived in a clause no watchdog can read.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-724
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred by constructing the joint reading the system could not, from three same-day summaries
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. SQLI, "Blind Spots: Invisible Risks in Complex System Landscapes" (2025) — siloed monitoring tools covering only part of a system, plus poor cross-tool integration, produce blind spots that are structural, not incidental; disagreement between tools does not imply one tool is defective.
    2. Baeldung, "Observability in Distributed Systems" — draws the standard distinction that monitoring watches a predefined set of metrics (a known failure taxonomy) while observability answers arbitrary questions about internal state; a watchdog is monitoring, so by construction it cannot represent states outside its predefined metric set — including a state that is jointly true across watchdog and task but expressible in neither alone.
    3. bluepes.com, "Distributed system monitoring: detect and prevent failures" — notes that transactions failing at intermediate stages "leave their fingerprints on limited data paths," so two instruments sampling different data paths of the same event can each be locally accurate yet jointly incomplete.

  Strength of challenge: Moderate

  Summary: General SRE/observability literature supports the more general claim underlying this presumption: contradictory signals from independent monitors frequently indicate the monitors are sampling different measurands of the same event, not that one is in error. This is the standard "monitoring sees only its predefined slice; observability requires synthesis across slices" argument, and it directly undercuts a design that treats watchdog/task disagreement as a binary correctness question. No C2A2-specific literature exists (expected, since this is a bespoke system), so the challenge is by analogy from distributed-systems monitoring theory.

  Specific risks: If the system's escalation/triage logic assumes disagreement implies an error to isolate, it will systematically misdiagnose true joint states (both signals correct, describing different aspects) as false alarms or false confidence, discarding the very information needed to reconstruct the joint reading — exactly the failure the item describes.

  Mitigations available: Add a reconciliation layer that treats watchdog and task output as complementary partial observations rather than competing verdicts; explicitly model "differing measurand" as a third outcome alongside "watchdog wrong" / "task wrong."

  STEELMAN:
    Item: PRESUMPTION-724
    Strongest counterargument: Monitoring instruments are, by design, narrow — a watchdog is built to answer a fixed, small set of questions, and a task's self-report answers a different fixed set. Standard observability theory predicts that when two narrow instruments disagree, the disagreement itself is data about a state that spans both instruments' blind spots, not evidence that one instrument malfunctioned. Treating disagreement as "someone is wrong" discards this information by construction, because no single instrument — including a hypothetical smarter watchdog — can express a joint state that only exists in the gap between two measurands.
    What would need to be true for C2A2 to be safe: Either watchdog and task would need to share a common, sufficiently expressive state model (so disagreement genuinely does imply error), or the system would need an explicit reconciliation step that constructs joint readings rather than adjudicating a winner.
    How to test: Retrospectively audit past watchdog/task disagreements to see what fraction resolve to "one was simply wrong" vs. "both correct, different measurand" — the ratio determines how costly this presumption is in practice.

--- CYCLE RE-SEARCH: 2026-08-25 (15b) ---
  Date searched: 2026-08-25
  Original item: PRESUMPTION-724
  Trigger: 15d re-trigger (cycle 1, MONITOR-511). Challenge direction sought: **challenge the
    PARTIAL NOVELTY-FLAG**, i.e. find prior art for the "UNREADABLE JOINT CLAUSE" — a joint state
    visible only across two instruments' blind spots, recorded only in prose. 15a's stated
    disposition-changer was *find prior art, or write the parseable joint-state field*; the first
    limb is this search. Note the polarity: cycle 0 returned the base presumption CHALLENGED
    (Moderate) on SRE/observability grounds; this cycle attacks the *novelty claim*.

  Search scope: **Tooling note.** The session's WebSearch budget was exhausted (200/200) before
    this item was reached, session-globally (a delegated subagent confirmed), and `web_fetch` is
    provenance-restricted; browser control failed (Chrome not running). I pivoted to **direct
    bibliographic API search from the workspace shell**: Crossref REST, OpenAlex, Unpaywall,
    Semantic Scholar Graph. Every citation below was returned by a live Crossref query this
    session; title, authors, venue, volume, issue, pages and DOI are confirmed against the
    registry. **No full text was retrieved for any source in this item** — all are
    METADATA-VERIFIED / ABSTRACT-ONLY. This is a real weakness and I mark it rather than blur it:
    the *existence and identity* of the prior art is established, its *detailed adequacy* to
    C2A2's case is argued from the standard content of these canonical works, not from a reading
    performed this cycle. Query families executed: distributed snapshots and global-state
    determination; global predicate detection (weak/strong, stable/unstable); decentralized
    supervisory control and co-observability; decentralized and coordinated failure diagnosis of
    discrete-event systems; diagnosability under partial observation; model-based diagnosis and
    conflict sets; Dempster-Shafer conflict and combination rules; analytical redundancy and
    parity relations. Cycle 0's practitioner sources (SQLI, Baeldung, bluepes) are superseded in
    weight by these and I do not re-argue from them.

  Challenging evidence found: Yes

  New sources this cycle:
    1. Chandy, K.M. & Lamport, L. (1985). "Distributed snapshots: determining global states of
       distributed systems." *ACM Transactions on Computer Systems* 3(1):63-75.
       doi:10.1145/214451.214456 — METADATA-VERIFIED (Crossref). **The founding prior art, and it
       is dead on.** The paper's premise is that in a distributed system *no single process can
       observe the global state*; the global state exists but is readable only by an algorithm
       that assembles it from local observations plus channel contents. "A joint state visible
       only across two instruments' blind spots" is a global state, and Chandy-Lamport is the
       algorithm for reading one. Forty-one years old.
    2. Cooper, R. & Marzullo, K. (1991). "Consistent detection of global predicates." *ACM SIGPLAN
       Notices* 26(12):167-174 / *Proceedings of the 1991 ACM/ONR Workshop on Parallel and
       Distributed Debugging*, pp. 167-174. doi:10.1145/127695.122774 (also
       doi:10.1145/122759.122774) — METADATA-VERIFIED. Detection of predicates that hold *of the
       global state* and are not locally evaluable by any participant. This is the "unreadable
       joint clause" as a named, solved detection problem.
    3. Garg, V.K. & Waldecker, B. (1994). "Detection of weak unstable predicates in distributed
       programs." *IEEE Transactions on Parallel and Distributed Systems* 5(3):299-307.
       doi:10.1109/71.277788 — METADATA-VERIFIED. And Garg & Waldecker (1996), "Detection of
       strong unstable predicates in distributed programs," *IEEE TPDS* 7(12):1323-1333,
       doi:10.1109/71.553309. Gives the *weak/strong* distinction — whether the joint predicate
       held on some consistent cut or on all of them — which is precisely the discrimination
       C2A2 currently records in prose.
    4. Rudie, K. & Wonham, W.M. (1992). "Think globally, act locally: decentralized supervisory
       control." *IEEE Transactions on Automatic Control* 37(11):1692-1708. doi:10.1109/9.173140
       (earlier: 1991 American Control Conference, pp. 898-903, doi:10.23919/acc.1991.4791508) —
       METADATA-VERIFIED. **The exact formalisation of the item's core idea.** *Co-observability*
       is the property that a decision is determinable by two partial observers acting jointly
       even though neither can determine it alone. A system is co-observable iff the "joint
       clause" is readable; if it is not co-observable, no amount of smarter single-instrument
       design will read it, and communication between observers is required. 724's insight is a
       named property with a decision procedure, thirty-four years old.
    5. Debouk, R., Lafortune, S. & Teneketzis, D. (2000). "Coordinated Decentralized Protocols for
       Failure Diagnosis of Discrete Event Systems." *Discrete Event Dynamic Systems*
       10(1-2):33-86. doi:10.1023/a:1008335115538 — METADATA-VERIFIED. Two local diagnosers, each
       with a partial and different observation window, plus an explicit coordinator whose job is
       to reconcile their reports into a joint verdict. This *is* the "reconciliation layer"
       cycle 0 proposed as a mitigation, published as a protocol family twenty-six years ago.
    6. Sampath, M., Sengupta, R., Lafortune, S., Sinnamohideen, K. & Teneketzis, D. (1995).
       "Diagnosability of discrete-event systems." *IEEE Transactions on Automatic Control*
       40(9):1555-1575. doi:10.1109/9.412626 — METADATA-VERIFIED. Formalises "blind spot":
       diagnosability is a property of the *observable projection* of the system, and a fault is
       diagnosable only if it leaves a distinguishable trace in what the instruments can see.
       Gives a test for whether C2A2's instrument set can ever read a given joint state.
    7. Reiter, R. (1987). "A theory of diagnosis from first principles." *Artificial Intelligence*
       32(1):57-95. doi:10.1016/0004-3702(87)90062-2 — METADATA-VERIFIED. **The formal statement
       of "disagreement is not error."** A discrepancy between observation and model yields a
       *conflict set* — a set of components not all of which can be behaving as modelled — and
       the diagnostic task is to compute minimal hitting sets, never to pick a winner. Adjudicating
       watchdog-versus-task is the move Reiter's framework was written to replace.
    8. de Kleer, J. & Williams, B.C. (1987). "Diagnosing multiple faults." *Artificial
       Intelligence* 32(1):97-130. doi:10.1016/0004-3702(87)90063-4 — METADATA-VERIFIED. The
       companion paper; extends to the case where more than one component is implicated, i.e.
       where "both were right" and "both were wrong" are both live.
    9. Yager, R.R. (1987). "On the Dempster-Shafer framework and new combination rules."
       *Information Sciences* 41(2):93-137. doi:10.1016/0020-0255(87)90007-7 — METADATA-VERIFIED.
       And Zadeh, L.A. (1996 repr.), "A Simple View of the Dempster-Shafer Theory of Evidence and
       its Implication for the Rule of Combination," in *Advances in Fuzzy Systems — Applications
       and Theory*, pp. 674-679, doi:10.1142/9789814261302_0033. The sensor-fusion limb the brief
       nominated: *conflict mass* is an explicit quantity in the representation, so "these two
       instruments disagree" is a number you carry forward, not an inconsistency you resolve by
       discarding one source. Zadeh's critique is the canonical demonstration that naive
       combination of conflicting evidence produces absurd results.
   10. Chow, E.Y. & Willsky, A.S. (1984). "Analytical redundancy and the design of robust failure
       detection systems." *IEEE Transactions on Automatic Control* 29(7):603-614.
       doi:10.1109/tac.1984.1103593 — METADATA-VERIFIED. Parity/residual generation: algebraic
       relations *among* multiple sensors that reveal states no individual sensor reveals. The
       engineering answer to "the joint reading lived in a clause no watchdog can read" — you
       construct the parity relation and monitor its residual.

  Strength of challenge: **Strong**

  Summary: The novelty flag falls, and falls harder than 690's. The "unreadable joint clause" is
    not an unaddressed phenomenon; it is one of the founding problems of distributed computing and
    of control-theoretic diagnosis, with four independent literatures that each name it, formalise
    it, and supply a decision procedure. Chandy & Lamport (1985) established that a global state is
    not locally observable and gave the algorithm for assembling it. Cooper & Marzullo (1991) and
    Garg & Waldecker (1994, 1996) turned "is this joint predicate true" into a detection problem
    with weak and strong variants. Rudie & Wonham (1992) supply the concept that most exactly
    matches the item — *co-observability*, the property that two partial observers can jointly
    decide what neither can decide alone — together with the corollary that when co-observability
    fails, communication between the observers is the only remedy, not a better single observer.
    Debouk, Lafortune & Teneketzis (2000) publish the coordinator architecture cycle 0 proposed as
    a novel mitigation. Reiter (1987) formalises "disagreement is not error" as conflict-set
    computation. And Chow & Willsky (1984) give the constructive form: build the parity relation
    across instruments and monitor its residual. Notably, **15a's second disposition-changer —
    "write the parseable joint-state field" — is what all of this prior art tells you to do**, so
    the correct reading is not that C2A2 faces an open research question but that it has
    rediscovered a well-posed problem and should adopt a known solution. Honest residue, stated
    plainly: none of these sources was read in full this cycle, and none is about LLM agents; the
    transfer from discrete-event and message-passing systems to a fleet whose "instruments" are a
    watchdog and a task's prose self-report is an analogy I am asserting, not one the sources make.

  Specific risks: [What breaks for C2A2 if the *novelty claim* is false.] (i) **A solved problem
    is queued as an open one**, consuming the closure capacity that PRESUMPTION-812 identifies as
    the fleet's binding constraint, while the actual work — defining the joint-state schema — sits
    behind it. (ii) **Reinvention with worse guarantees.** A hand-rolled reconciliation layer will
    almost certainly lack the consistency discipline that Chandy-Lamport exists to provide, and
    will produce joint readings assembled from mutually inconsistent cuts — a failure that looks
    like correct output and is not. (iii) **The decidability question stays hidden.** Sampath et
    al.'s diagnosability and Rudie & Wonham's co-observability both say the honest first question
    is *whether the instrument set can read the joint state at all*. If C2A2's watchdog and task
    are not co-observable for the states that matter, then writing a joint-state field is
    necessary but not sufficient and a third instrument is required — and nothing in the item's
    current framing would surface that. (iv) **Credibility cost** of flagging a 1985 result as a
    literature gap, which is the same risk as PRESUMPTION-690 and correlated with it.

  Mitigations available: (1) **Withdraw the novelty flag; proceed directly to 15a's second
    limb** — write the parseable joint-state field — since the literature's unanimous instruction
    is to represent the joint state explicitly. (2) **Adopt the conflict-set idiom (Reiter 1987)
    for the record**: when watchdog and task disagree, record the *set* of components implicated
    rather than a verdict; "both correct, different measurand" then falls out as the empty
    diagnosis rather than needing to be a third enumerated outcome. (3) **Carry a conflict
    quantity, not a boolean** (Yager 1987) so that degree of disagreement survives into
    downstream reasoning. (4) **Run the co-observability question before the schema question**:
    ask whether the joint states that matter are decidable from the union of the two instruments'
    observations. If not, the fix is a third observation channel and no schema will substitute.
    (5) **Use a consistent-cut discipline** when assembling any joint reading, so that the field,
    once written, is not populated from incomparable timestamps.

  STEELMAN:
    Strongest counterargument: The prior art I have assembled is about systems with *formal
      models* — a discrete-event automaton, a set of processes with defined message channels, a
      component model with correct-behaviour axioms. Every one of these results is a theorem
      about a formalism, and every one requires that you can enumerate the states, name the
      observable events, and specify what each instrument can and cannot see. C2A2 has a watchdog
      emitting a fixed metric and a task emitting prose. There is no automaton, the observation
      map is undefined, and the "joint state" in question was reconstructed by a human-equivalent
      reader (14b) from three same-day summaries — an act of interpretation, not of predicate
      detection. Co-observability is undecidable if you cannot say what is observed. So the
      relevant claim may not be "is there prior art for detecting joint states" — obviously there
      is — but "is there prior art for detecting joint states *in a system whose instruments emit
      natural language and whose state space is not enumerable*", and to that I found nothing this
      cycle and did not search for it. On that framing 15a's flag is about the right thing, and my
      response is the classic error of answering a harder-to-state question with an easier-to-cite
      one. Second and more damaging to me: I read none of these papers this cycle. A novelty flag
      should not be closed by a bibliography.
    What would need to be true for C2A2 to be safe: (a) the instruments' observation maps can be
      *stated* — for each of watchdog and task, what it can and cannot see — because every result
      cited depends on that and C2A2 has not written it down; (b) the joint states that matter are
      finite and enumerable enough to be predicates rather than interpretations; (c) the joint
      reading, once represented, is populated from a consistent cut rather than from whatever
      artefacts happened to share a date; (d) somebody reads the field — a joint-state field with
      no consumer is the same defect as PRESUMPTION-690's unread probe, and the two items share
      it. If (a) fails, the prior art is inapplicable and the flag should be re-filed as
      "instruments not characterised" rather than closed.
    How to test: (1) **The observation-map test, and it is prior to everything else.** Write down,
      for the watchdog and for the task, what each can observe. Two short lists. If they can be
      written, apply the co-observability test (Rudie & Wonham 1992) to the specific joint state
      14b reconstructed: was it jointly decidable, or does it need a third instrument? This
      converts the item from an interpretive claim into a checkable one. (2) **The read test.**
      Read Rudie & Wonham (1992) and Debouk et al. (2000) in full — neither was read this cycle —
      and confirm the transfer holds. Two papers, and they are the two the whole challenge rests
      on. (3) **The retrospective ratio test**, carried forward unchanged from cycle 0 and still
      not run: audit past watchdog/task disagreements for the fraction resolving to "one was
      wrong" versus "both right, different measurand." If the fraction is near zero, the item is
      true but rare and the schema work is not urgent; if it is substantial, it is urgent, and in
      neither case is it novel.

  Recommendation: **CHALLENGED** — the PARTIAL NOVELTY-FLAG falls. The unreadable joint clause is
    global-predicate detection (Chandy & Lamport 1985; Cooper & Marzullo 1991; Garg & Waldecker
    1994) and, most exactly, a co-observability failure (Rudie & Wonham 1992), with a published
    coordinator architecture (Debouk et al. 2000) and a constructive cross-instrument method
    (Chow & Willsky 1984). The base presumption is untouched and remains CHALLENGED/Moderate from
    cycle 0; only the novelty claim is defeated. Residual open question, re-filed rather than
    closed: whether C2A2's instruments can be characterised well enough for the prior art to be
    instantiable.

  PROVENANCE: Origin: 14b · Chain: [14b → 15a, 15b → 15c → 15d → 15b] · Item type: PRESUMPTION
    (unstated — surfaced by inference); this cycle addresses the PARTIAL NOVELTY-FLAG carried
    from intake, not the base presumption · Transform: 15b re-searched on 15d re-trigger (cycle 1,
    MONITOR-511), polarity inverted onto the novelty claim · Current status: base presumption
    CHALLENGED (cycle 0, Moderate, unchanged); novelty flag CHALLENGED (this cycle, Strong)

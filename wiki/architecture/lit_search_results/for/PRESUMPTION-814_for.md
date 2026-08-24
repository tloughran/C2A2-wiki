SEARCH-FOR-PRESUMPTION-814:
  Date searched: 2026-08-16
  Original item: PRESUMPTION-814
  Original statement: [inferred] That the right response to a closed review gate is to keep producing.
  Risk if wrong: High
  Search question (as queued): Work-in-progress limits and pull systems; queueing with an unavailable
    server; the cost of unreviewed inventory in software and manufacturing.

  POLARITY NOTE — WHAT WAS ACTUALLY SEARCHED FOR. The item is worded as the DEFECTIVE belief. The
  proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses:
    (C1) WHEN THE DOWNSTREAM STAGE CANNOT ACCEPT WORK, THE CORRECT RESPONSE IS TO STOP PRODUCING, and
         this is not a counsel of despair but the explicit, named, canonical control rule of every
         mature flow discipline — jidoka and the andon cord in the Toyota Production System, WIP
         constraints in Reinertsen, backpressure in distributed systems.
    (C2) PRODUCTION AUTHORISATION SHOULD COME FROM A DOWNSTREAM SIGNAL, NOT FROM A CLOCK. The
         push/pull distinction is precisely the distinction between "the schedule says produce" and
         "the consumer says produce," and pull is the discipline that makes an unavailable consumer
         automatically halt the producer without anyone having to notice.
    (C3) UNREVIEWED OUTPUT IS INVENTORY, NOT PROGRESS, and inventory has a cost that is invisible
         because it is not booked anywhere — which is exactly why thirteen days of it passed without
         anyone naming an alternative.
    (C4) CONTINUING TO PRODUCE INTO A CLOSED GATE ACTIVELY DEGRADES THE GATE when it reopens, via batch
         size and review fatigue, so the choice is not "produce or waste the day" but "produce now and
         pay at the gate" versus "stop now and pay less."
  "SUPPORTED" below means 14b's question — what alternative to continued production was considered on
  any of thirteen days — is well grounded, and is equivalently evidence AGAINST the presumption as
  worded.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-814
    Item type: PRESUMPTION (unstated — surfaced by inference; extra weight: no run states the belief,
      and no run states an alternative to it either)
    Transform at each step:
      14b: Asked what alternative to continued production was considered on any of thirteen days.
      15a: Searched for supporting literature on the corrective proposition; register check first.
    Current status: SUPPORTED — BUT SEE THE DUPLICATION WARNING

  **DUPLICATION WARNING — READ BEFORE DISPOSITION.** The register check below found that
  PRESUMPTION-814's substance is held by **PREMISE-119, minted 2026-07-21 at Moderate-High confidence**,
  whose statement opens "Production and judgment are not independently schedulable" and whose
  Applicable-to line already reads "**The review channel awaiting Tom (arrival ~4/day, service 0/day
  across 15 days, 67 carried items)**." That is PRESUMPTION-814's situation, twenty-six days earlier,
  with the numbers. It is reinforced by **PREMISE-106** (2026-07-20) on the unstable-queue regime. A
  disposition that mints a new premise here would be minting PREMISE-119 a second time, which
  PREMISE-138 clause (1) and PREMISE-135 both bar. This file proceeds because the queue asked for the
  search and because there is a narrow genuine residual, identified as (R1)-(R2) below.

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: WIP, work-in-progress, queue, backlog, unreviewed, inventory,
    throughput, production, pull system, Little's Law, bottleneck, review gate, gate, backpressure,
    admission, saturated, service rate.
    Found and read in full:
      - **PREMISE-119** (2026-07-21, ACTIVE, Moderate-High) — see DUPLICATION WARNING. Holds: producing
        and reviewing stages are PROVABLY COUPLED; "unbounded production imposes a congestion
        externality on the constrained stage"; "service rate is not independent of arrival rate because
        reviewer acceptance falls with cumulative exposure"; "backpressure is a correctness requirement,
        not an optimisation." Its SEQUENCING REQUIREMENT transfers to 814 verbatim and is load-bearing:
        **establish whether the consumer is SATURATED or ABSENT before designing any admission policy**,
        because "where service is zero the steady-state relations do not hold at all and no reduction in
        arrivals bounds the queue — cutting 4/day to 1/day still diverges." Its EXCLUSION also
        transfers: a flat per-day admission cap is excluded, because fixed WIP limits "bind immediately
        against an existing backlog and are raised on first bind." Its ADOPTABLE-NOW clause is the
        thing 814 most needs and is still not built: **a "produced and unreviewable" state, which the
        current scheme cannot represent.**
      - **PREMISE-106** (2026-07-20, ACTIVE, High) — the lit-search queue is in the UNSTABLE regime;
        arrival exceeds service so the backlog grows without bound; "this is a proved queueing result,
        not a hypothesis, and no scheduling discipline recovers it." Corollary (ii) is directly 814's
        answer: **arrival and service are BOTH decision variables**, the enqueue stream is generated by
        C2A2's own agents and is not exogenous, so admission control is available, and bounding arrival
        is sufficient on its own.
      - **PREMISE-107** (2026-07-20, ACTIVE) — "Delivering more signal into a channel with demonstrated
        zero throughput is not throughput but INVENTORY, and can degrade the disposition of signals
        already working." This is 814's clause (C3) and (C4) already in the register, in one sentence.
      - **PREMISE-102** (2026-07-19, ACTIVE) — repeated identical non-processing converts a one-time
        signal into an undecided STANDING POLICY of non-coverage. Thirteen days is that.
      - **PREMISE-154** (2026-08-13, ACTIVE) — scope-extension of PREMISE-133's discharge requirement to
        the DEFERRAL/QUEUE cohort in trigger-bound form: a suspension must name what discharges it, who
        adjudicates, and a deadline.
      - **PREMISE-153** (2026-08-12, ACTIVE) — uncommitted work held on ephemeral compute is an ACTIVE
        DATA-LOSS EXPOSURE, not a scheduling deferral. The storage-side form of "inventory is not
        neutral."
      - **PREMISE-001/002 family** (the HITL-bottleneck premises at the head of the register) — human
        review capacity is a documented bottleneck in human-in-the-loop AI systems and is "the binding
        constraint" on throughput.
      - **PREMISE-151** (2026-08-10, ACTIVE) — repeated disclosure of an unremediated condition
        NORMALISES it; the disclosure record is evidence of incubation.
    CONCLUSION OF THE CHECK: **NEAR-TOTAL OVERLAP; ONE ENTRY IS A SUBSTANTIVE DUPLICATE. NO
    NOVELTY-FLAG.** Eight ACTIVE premises bear on this and PREMISE-119 holds the claim outright. The
    genuine residual is two things PREMISE-119 does not contain:
      (R1) THE STOP-THE-LINE OPTION IS NOT IN THE REGISTER AT ALL. PREMISE-119 reasons about ADMISSION
           POLICY — how much to let in — and explicitly EXCLUDES the flat cap. Neither 119 nor 106 nor
           107 contains the manufacturing answer, which is not a cap but a HALT: an authorisation
           mechanism under which production simply cannot proceed while the consumer is unavailable, and
           in which halting is a normal, expected, non-exceptional operating state that any participant
           may trigger. That is a different remedy shape from a quota, it is not excluded by 119's
           exclusion, and it is what 14b's question ("what alternative was considered?") is actually
           asking for.
      (R2) THE ABSENCE OF DELIBERATION IS THE FINDING, NOT THE PRODUCTION RATE. 14b did not observe
           over-production; it observed that across thirteen days NO RUN NAMED AN ALTERNATIVE. That is a
           claim about the decision record, not about the queue, and no premise addresses it.
    DECLARED LIMITATION: string grep, measured at ~56% recall (ASSUMPTION-1052). The list above is a
    **LOWER BOUND**; the true overlap is likely larger, which argues for a narrower disposition.

  Supporting evidence found: Yes

  Sources:
    1. The Toyota Production System — jidoka and the andon cord. Ohno, T., *Toyota Production System:
       Beyond Large-Scale Production* (Productivity Press, 1988); Toyota Motor Corporation's own
       statement of the two pillars; the Art of Lean / Lean Enterprise Institute accounts of the seven
       wastes. — **The direct and strongest support for clause (C1), and the answer to 14b's question
       in its most explicit form: STOPPING IS THE DESIGNED RESPONSE, AND IT IS SOMEONE'S JOB.** TPS
       rests on two pillars, just-in-time and jidoka, where jidoka is "automation with a human touch":
       machines and processes detect their own abnormalities and STOP automatically, and — the clause
       that matters here — plant-floor personnel are "treated as experts permitted to stop the
       production line if they perceive a potential quality issue." The andon cord is the instrument
       that makes halting a normal, low-ceremony, any-participant action rather than an escalation. And
       the seven-wastes taxonomy places OVERPRODUCTION first and treats it as the most fundamental
       waste, on the reasoning that it generates the others (inventory, waiting, defects discovered
       late). Applied to 814: a closed review gate is precisely the abnormality jidoka exists to
       respond to, and the response the discipline prescribes is to stop, surface, and fix — not to
       accumulate.
       [SNIPPET LEVEL, with the caution that this is a well-known body of practice reported here from
       secondary sources located this run (Art of Lean's TPS encyclopedia and seven-wastes pages;
       Toyota's official vision-and-philosophy page; Vorne and Center for Lean explanatory pages). The
       two-pillar structure, the human-jidoka clause and overproduction's position in the seven wastes
       were read from those summaries. **Ohno's book was NOT opened this run and no page or quotation
       should be attributed to it onward.** Some of this is also CANONICAL — widely known independently
       of any source read here — and is flagged as such rather than dressed up as retrieval.]
    2. Reinertsen, D.G. (2009), *The Principles of Product Development Flow: Second Generation Lean
       Product Development*, Celeritas Publishing. — **The support for clauses (C1) and (C3) in the
       product-development setting, which is closer to C2A2 than the factory floor is.** The relevant
       principles as reported: **WIP constraints are the primary mechanism for controlling queue size**;
       "by providing local WIP constraints for each queue and NOT ALLOWING UPSTREAM WORKFLOWS TO ADD
       WORK TO FULL QUEUES, over-utilisation at one workflow can fairly quickly propagate to upstream
       workflows, leading them to adjust their rate of work production" — which is (C1) as a mechanism
       rather than a slogan. And the framing claim that gives (C3) its force: **"invisible and unmanaged
       queues are the underlying root cause of poor product development performance."** Reinertsen's
       distinctive move is to insist the cost be QUANTIFIED — an economic framework for cost of delay
       and holding cost — rather than argued qualitatively.
       [SNIPPET LEVEL — the book's listings and several substantive summaries (BPTrends review PDF;
       Limited WIP Society talk notes; sobrief chapter summary) were located and read this run; **the
       book was NOT read.** The WIP-constraint and invisible-queue claims are well attested across the
       summaries. Do not quote a page number.]
    3. Push versus pull production control; kanban and CONWIP. — **The support for clause (C2), and the
       clean statement of what "authorisation to produce" means.** In a push system, production is
       scheduled from a forecast or a clock and materials move forward "regardless of whether downstream
       processes are ready." In a pull system, production is AUTHORISED by a downstream consumption
       signal — a kanban card, an electronic signal, a withdrawal from a controlled buffer — so items
       are "produced because something was used, shipped, or pulled by the next step." CONWIP
       generalises this to a fixed pool of system-wide authorisation cards: **a new order may enter the
       system only when a finished part leaves.** The transfer to 814 is exact and is the cleanest
       formulation available: under a pull discipline, a review gate that has accepted nothing for
       thirteen days would have issued no authorisations, and production would have halted on day one
       WITHOUT ANYONE HAVING TO NOTICE — which is precisely the failure 14b identifies, since noticing
       is what did not happen.
       [SNIPPET LEVEL — the Wikipedia CONWIP article, IndustryWeek's push-vs-pull piece, and several
       practitioner explainers were located and read at summary level this run; **no primary source
       (Spearman, Woodruff & Hopp's CONWIP paper; Hopp & Spearman's *Factory Physics*) was retrieved.**
       The CONWIP card rule is standard textbook material and is CANONICAL as well as retrieved.]
    4. Code-review flow evidence for clause (C4). — Practitioner analyses converge on two effects that
       make continued production actively costly at the gate: **when small units get stuck in a review
       queue, producers batch them into larger units, and reviewer effectiveness degrades sharply with
       size** (the widely-cited SmartBear/Cisco figure of degradation past ~400 lines, with review
       effectiveness reported around 80-90% under 200 lines and below 50% over 1,000); and **queue
       pressure produces rubber-stamping** — approval without review — which converts a blocked gate
       into a nominally-open one that catches nothing. **This is the mechanism by which a backlog does
       not merely delay review but destroys it**, and it is the empirical form of PREMISE-119's clause
       that "reviewer acceptance falls with cumulative exposure."
       [SNIPPET LEVEL AND WEAK PROVENANCE, flagged prominently. These figures circulate through
       practitioner blogs (gitautoreview, avestahq, codeant, Medium) that cite SmartBear's *Best Kept
       Secrets of Peer Code Review* and a Cisco case study at second or third hand. **The primary
       SmartBear/Cisco study was NOT retrieved this run and the numbers must NOT be quoted onward as
       measurements.** They are reported here because the DIRECTION is consistent across independent
       practitioner accounts and matches PREMISE-119's already-validated mechanism; the magnitudes are
       not established.]
    5. Little's Law and the elementary queueing result that a queue with arrival rate > 0 and service
       rate 0 diverges without bound. — CANONICAL, and already held at High confidence as PREMISE-106.
       Restated here only because it is the formal backbone of (C1): no scheduling discipline, no
       prioritisation, and no cap recovers a queue whose server is not serving.
       [CANONICAL — cited from established knowledge, NOT re-verified this run.]

  Strength of support: **Strong**, with the qualification that the strength is concentrated in the
  clauses the register already holds. (C1) and (C2) are supported by two mature, independently developed
  disciplines that reached the same rule — stop the line, and let the consumer authorise production —
  and (C2) in particular supplies a mechanism, not just a norm. (C3) is Reinertsen's central claim and
  is also PREMISE-107 verbatim. (C4) is the weakest clause on external evidence (practitioner sources
  only) but is the best supported INTERNALLY, since PREMISE-119 already validated the same mechanism
  from the queueing literature.

  Summary: The corrective proposition is strongly supported, and the notable finding is that two
  independent traditions — Japanese manufacturing practice and Western product-development flow theory
  — converge on the same answer to 14b's question, and it is an answer no C2A2 run gave. In TPS, a
  downstream stage that cannot accept work is exactly the abnormality jidoka exists for; the prescribed
  response is to STOP, and the andon cord exists to make stopping a normal, any-participant,
  low-ceremony action rather than an escalation. Overproduction sits first in the seven wastes precisely
  because it manufactures the others. Reinertsen supplies the mechanism: WIP constraints work by NOT
  ALLOWING UPSTREAM WORKFLOWS TO ADD WORK TO FULL QUEUES, so that congestion propagates backwards and
  the producer adjusts — and his framing claim, that invisible and unmanaged queues are the root cause
  of poor development performance, is 814's diagnosis of why thirteen days passed unremarked. The
  push/pull literature gives the sharpest formulation available: under pull, production is authorised by
  a downstream signal rather than by a clock, and CONWIP's rule that a new item may enter only when a
  finished item leaves would have halted production on day one without anyone having to notice. That is
  decisive for this item, because not-noticing is the failure. The code-review evidence closes the loop
  on why continuing is not free: queued work gets batched, batching degrades reviewer effectiveness, and
  queue pressure produces rubber-stamping — so unreviewed inventory does not merely wait, it corrodes
  the gate it is waiting for. Where this file must stop short of the item is that the register already
  holds the finding: PREMISE-119 minted "production and judgment are not independently schedulable" on
  2026-07-21, with this exact channel and its numbers in its Applicable-to line.

  Caveats:
    (a) THIS IS SUBSTANTIALLY PREMISE-119 AGAIN AND THAT SHOULD DRIVE THE DISPOSITION. See the
        DUPLICATION WARNING. The correct reading of 814 is "the second observed instance of a finding
        validated twenty-six days ago, on which nothing has changed." Per PREMISE-151, a second
        recording of an unremediated condition is evidence of incubation, not of confirmation.
    (b) PREMISE-119'S SEQUENCING REQUIREMENT BINDS AND IS THE MOST LIKELY WAY TO GET THIS WRONG. Before
        any remedy: **is the reviewer SATURATED or ABSENT?** If service is zero, no admission policy
        bounds the queue and throttling production "directs effort at the arrival term while the term
        that is actually zero goes untouched, and reports a control in place." Thirteen days of a closed
        gate is prima facie ABSENT rather than saturated, in which case the pull-system remedy is
        correct but the WIP-cap remedy is not, and the real question is who reopens the gate — which is
        PREMISE-154's discharge-rule territory, not a flow-control question at all.
    (c) THE MANUFACTURING TRANSFER HAS A KNOWN LIMIT AND IT CUTS AGAINST THE ITEM. Stopping the line is
        cheap in a factory because the line resumes exactly where it stopped and the workers are paid
        either way. In a system of scheduled autonomous agents, "stop producing" may mean the day's
        knowledge-generation opportunity is lost irrecoverably, and knowledge work is not
        conserved the way physical WIP is. The honest form of the remedy is therefore not "stop" but
        "**switch to work that does not require the gate**" — and nothing located this run establishes
        that such work exists in quantity for these agents. That is the load-bearing unknown.
    (d) THE SOURCE QUALITY IS UNEVEN AND THE STRONGEST-SOUNDING NUMBERS ARE THE WEAKEST. Source 4's
        review-effectiveness figures are third-hand practitioner citations of a vendor white paper. They
        should not be quoted. Sources 1-3 are canonical bodies of practice reported from secondary
        summaries, not from primary texts read this run.
    (e) PUBLICATION AND ADVOCACY BIAS IS SUBSTANTIAL IN THIS LITERATURE. Lean and Kanban writing is
        largely produced by consultants and advocates; the failure cases of WIP limits are
        under-reported. PREMISE-119 already absorbed the strongest known counter — that fixed WIP limits
        bind immediately against an existing backlog and are raised on first bind — and that counter
        applies here too.
    (f) "THIRTEEN DAYS" AND "NO ALTERNATIVE NAMED" ARE 14b'S OBSERVATIONS AND WERE NOT VERIFIED HERE.
        This file did not read the thirteen days of run records. Per PREMISE-124 nothing here is a
        calibrated measurement.

  Search scope: GOOD on the flow disciplines (TPS/jidoka, Reinertsen, push-pull/CONWIP), all at
    secondary-summary level with primaries identified and NOT retrieved. WEAK and explicitly flagged on
    the review-degradation magnitudes. EXCELLENT on the register side. NOT SEARCHED, and each would
    materially change this file: (i) **queueing models with SERVER VACATIONS / server breakdown**, which
    is the formally correct model for "the server is absent rather than slow" and is the one piece of
    the queued search question this file did not reach — it was identified as the right literature
    (M/G/1 with vacations; unreliable-server queues) and NOT retrieved, and it is where a defensible
    statement about what thirteen days of zero service implies would come from; (ii) the primary
    SmartBear/Cisco code-review study, which would upgrade source 4 from anecdote to measurement;
    (iii) any empirical work on WHAT KNOWLEDGE WORKERS DO when a gate closes — the substitution question
    in caveat (c) — for which nothing on point was located, a clearly-labelled negative result.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently NO-SUPPORT-FOUND
  for the presumption as worded. **But the disposition should almost certainly be a RE-CONFIRMATION of
  PREMISE-119 rather than a new premise.** Four carries:
    1. NO NEW PREMISE. PREMISE-119 holds this at Moderate-High and its Applicable-to already names this
       channel. Minting again is barred by PREMISE-138(1) and PREMISE-135.
    2. THE RESIDUAL WORTH CARRYING IS (R1): THE HALT OPTION, WHICH THE REGISTER DOES NOT CONTAIN.
       PREMISE-119 reasons about admission caps and excludes the flat one. The manufacturing answer is
       not a cap but an AUTHORISATION MECHANISM plus a normalised, any-participant halt. That is a
       different remedy shape, it is not covered by 119's exclusion, and it directly answers 14b's
       question about what alternative existed.
    3. THE ADOPTABLE-NOW ITEM FROM PREMISE-119 IS STILL NOT BUILT AND 814 IS THE COST OF THAT. "A
       'produced and unreviewable' state, which the current scheme cannot represent" was named on
       2026-07-21 as adoptable and uncontested by either search direction. Thirteen days of output with
       no such state is what the omission looks like. This is an ENFORCEMENT gap, not a knowledge gap.
    4. RESOLVE THE SATURATED-VERSUS-ABSENT QUESTION BEFORE ANYTHING ELSE (caveat b). It is a one-look
       determination, it changes which remedy is correct, and PREMISE-119 already requires it.

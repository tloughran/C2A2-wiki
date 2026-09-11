SEARCH-FOR-PRESUMPTION-951:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-951
  Original statement: "[inferred] That a defect logged as 'needing a human' is in a queue rather than in
    a dead-letter office — that thirty days of no ruling is a decision pending, not a decision made."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-951
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a stated deferral whose addressee has been silent for the full life of the
        item; recorded as a generalisation of OPEN-190 from proposals to defects, raised as OPEN-193.
      15a: Searched for supporting literature; found genuine FOR-direction support in issue-tracker
        practice, conditional in every case on a declared aging policy the estate does not have.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check:
    - PREMISE-133 (ACTIVE) — "ABSTENTION IS A DECISION AND REQUIRES A WRITTEN DISCHARGE RULE. Declining
      to adopt is an action inside the decision problem with its own cost, not an exit from it."
    - PREMISE-154 (ACTIVE) — scope-extension of PREMISE-133 to the deferral/queue cohort in
      trigger-bound form: a suspension must name what would discharge it, who adjudicates, and a
      deadline. PREMISE-154's own note is recorded as having *declined* to license the backlog/queue
      cohort, which is precisely the gap PRESUMPTION-951 occupies. These two together come close to
      ruling the item before any search.
    - PREMISE-183 (ACTIVE) — a filed flag is a live obligation with a closure test, not a discharged
      duty.
    - PREMISE-102 (ACTIVE) — where a notified channel has demonstrated zero throughput, repeated
      identical non-processing converts a one-time signal into an undecided standing policy of
      non-coverage. This is the item's mechanism, already stated.
    Recording the hits per OPEN-192; searched anyway.

  LIMB SPLIT:
    Limb A (PENDING IS A LEGITIMATE STATE): an item blocked on a named human may properly remain open
      and unresolved without that constituting a decision against it.
    Limb B (PENDING NEEDS NO EXPIRY): thirty days, or any duration, of silence leaves the item in the
      same state it started in, and no reclassification is owed.

  Supporting evidence found: Yes (Limb A), No (Limb B)

  Sources:
    1. GitHub stale-bot practice and its critics (jestjs/jest issue #12496; GitLab triage-ops MR 586
       "Fix the close stale bugs policy"; Duck Alignment Academy "How to close issues"). — SECONDARY —
       This is the genuine FOR-direction evidence and it is real: mature projects routinely **exempt**
       bug-labelled and needs-review items from stale auto-close, so that "a bug label or a needs-review
       label keeps an item alive indefinitely." The practitioner argument against auto-close is stated
       directly: "Autoclosing issues is not only user-hostile, but it encourages noisy behavior when
       people leave a comment just to keep the issue open." A confirmed defect awaiting a decision is
       exactly the class these exemptions protect. Supports Limb A.
    2. Elizabeth-Wessel / Santos et al., 2019. "Should I Stale or Should I Close? An Analysis of a Bot
       That Closes Abandoned Issues and Pull Requests." MSR/ICSE-adjacent. — SECONDARY (located via
       ResearchGate listing; not retrieved) — Reported finding that bug-report-tagged issues are exempt
       from staleness, as are PRs awaiting input. Named here as the primary study for this question; no
       quantitative figure from it is used because I could not retrieve it.
    3. Apache Arrow bug-report policy (arrow.apache.org developer docs, v25/v26). — SECONDARY — A worked
       example of the *bounded* form: 365 days of inactivity adds a `Status: stale-warning` label, then
       14 further days of inactivity closes. Note the shape: the exemption is not unlimited; it is a
       long, **declared**, two-stage aging policy with a warning before terminal state. This is Limb A
       granted and Limb B denied in one policy.
    4. Dead-letter-queue design in message infrastructure (Elastic Logstash DLQ docs
       `dead_letter_queue.retain.age` and `dead_letter_queue.storage_policy`; AWS SQS DLQ retention;
       Azure Service Bus dead-letter queues; RabbitMQ TTL/expiration). — SECONDARY — Every major broker
       ships an age policy and a storage policy (`drop_newer` / `drop_older`) as first-class settings,
       i.e. the infrastructure assumes an undeliverable item acquires a terminal state by time. The
       Logstash documentation also carries a caveat directly relevant to the estate: "the age policy is
       verified and applied on event writes and during pipeline shutdown, which means your
       dead-letter-queue folder may store expired events for longer than specified" — an expiry policy
       that only runs on activity does not expire anything in a quiet channel.
    5. Audit-recommendation aging practice (Oakland City Auditor 2024 follow-up report; internal-audit
       follow-up guidance, eCampusOntario "Internal Auditing: A Practical Approach" §10.03). —
       SECONDARY — A Recommendation Implementation Status Summary is sent to the audited department
       **90 days** after the final report for unimplemented recommendations, requesting status and a
       targeted implementation date; reporting carries aging buckets at 30/60/90 days. This is the
       nearest institutional analogue to "needs a human" and it has both a threshold and a forced
       response.
    6. MSP/ITSM stale-ticket practice (Giant Rocketship, "Cleaning the Backlog"). — SECONDARY — Tickets
       in "Waiting on Client" or "Pending Vendor" with no status change in 14, 30 or 60 days are
       targeted for auto-close, typically via a final notice with a 7-day window. Low-quality vendor
       source; included only because it names the *state* the estate's items are actually in —
       "waiting on client" — and shows that the state is universally instrumented with a clock.

  Strength of support: Moderate (Limb A), None (Limb B)

  Summary: Limb A is genuinely supported and I want to state that without hedging, because the
    FOR-direction result here is not a formality: issue-tracker practice deliberately exempts confirmed
    defects and input-blocked items from staleness, and the argument against auto-closing them is a
    serious one about not destroying information. The estate's instinct that the duplicate-anchor defect
    is *pending* rather than *declined* is the same instinct. Limb B finds no support anywhere. Every
    system I looked at — brokers, trackers, audit offices, ITSM — instruments the waiting state with a
    declared age policy, and the exemptions in Limb A's favour are exemptions from a *default* clock,
    not the absence of one: Apache Arrow's bug exemption still terminates at 365+14 days, and audit
    offices force a status response at 90. The estate has the exemption without the clock. One detail
    transfers unusually well: Logstash's caveat that an age policy applied only on writes lets expired
    items sit indefinitely in a quiet queue — which is precisely what happens when the only mechanism
    that would reclassify a stalled item is a run that the stall itself suppresses.

  Caveats: Issue trackers hold feature requests and unreproducible reports alongside confirmed defects,
    and the anti-auto-close argument is largely about the former; the estate's item is a *confirmed,
    demonstrated-live* defect, which is the class trackers protect most and also the class they escalate
    fastest. The DLQ analogy is imperfect because a dead-lettered message has no adjudicator waiting,
    whereas here there is a real person who did answer 36 cards in one act on 09-09 — so the channel is
    not dead, it is bursty, and an expiry policy tuned as if it were dead would be wrong. None of the
    six sources was retrieved as primary research; the Santos et al. paper is the one that should be
    read if this is pursued.

  Search scope: comprehensive — searched dead-letter queue retention and age policies across four
    brokers, stale-bot policies and their critiques in open-source trackers, ITSM stale-ticket
    auto-close thresholds, and audit-recommendation aging and follow-up requirements. Did not search
    the legal literature on laches or constructive denial, which is the closest normative analogue to
    "declined by silence" and would be the right frame if the estate wants a principled threshold rather
    than a conventional one.

  Recommendation: PARTIALLY-SUPPORTED. The recommendation rests on the split. Limb A is SUPPORTED: the
    item is legitimately pending and should not be reclassified as declined merely because it is old.
    Limb B is NO-SUPPORT-FOUND and carries the High risk: what the literature uniformly requires, and
    the estate uniformly lacks, is a *declared* threshold with a forced status response — the audit
    90-day RISS is the cleanest transferable pattern. Note that this is PREMISE-154's requirement
    (name the discharge, the adjudicator and the deadline) applied to the cohort PREMISE-154 explicitly
    declined to license, so the correct disposition may be a scope extension of PREMISE-154 rather than
    a new premise. The `stat` 14b specifies remains the decisive in-house measurement.

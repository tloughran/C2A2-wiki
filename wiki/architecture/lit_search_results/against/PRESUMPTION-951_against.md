SEARCH-AGAINST-PRESUMPTION-951:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-951
  Original statement: "[inferred] That a defect logged as 'needing a human' is in a queue rather than in a
    dead-letter office — that thirty days of no ruling is a decision pending, not a decision made."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-951
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a stated deferral whose addressee has been silent for the full life of the item;
        recorded as OPEN-190's shape generalised from proposals to defects, raised as OPEN-193.
      15b: Searched for challenging literature; found a whole legal doctrine (administrative silence /
        deemed refusal) built on the proposition that silence past a deadline IS a decision, plus the
        dead-letter-queue design literature requiring a max-age policy.
    Current status: CHALLENGED

  Register pre-check:
    - **PREMISE-133 (ACTIVE) — directly contrary.** "ABSTENTION IS A DECISION AND REQUIRES A WRITTEN
      DISCHARGE RULE. Declining to adopt is an action inside the decision problem with its own cost, not
      an exit from it, and suspension of judgement is a committal attitude requiring its own warrant."
      PRESUMPTION-951 is the estate acting as though abstention were a null state. PREMISE-133 says it
      is not, and says so in the register's own words.
    - **PREMISE-154 (ACTIVE) — the scope extension already exists.** It extends PREMISE-133 to the
      deferral/queue cohort in TRIGGER-BOUND form: a suspension must name what would discharge it, who
      adjudicates, and a deadline. Note PREMISE-133's own Applicable-to field explicitly DECLINED to
      license the backlog/queue cohort and PREMISE-154 was minted to close that. So the estate has
      already been here once, on this exact cohort.
    - **PREMISE-147 (ACTIVE)** — the statistic that carries the information is AGE, not count. 14b's
      proposed `stat` is exactly this premise applied.
    - PREMISE-183 (ACTIVE) — a filed flag is a live obligation with a closure test; a repeat filing is a
      reopening.
    - PREMISE-102 (ACTIVE) — where the notified channel has demonstrated zero throughput, repeated
      identical non-processing converts a one-time signal into an undecided standing policy of
      non-coverage. This is the item's mechanism, already minted.
    - PREMISE-108 (ACTIVE) — transmission is not delivery; the finding is held by nobody while the record
      shows it discharged.

  Challenging evidence found: Yes

  Sources:
    1. The administrative-silence doctrine in continental and EU administrative law — deemed refusal
       (silence négative / silenzio-rifiuto) and deemed approval (silenzio-assenso / tacit authorisation).
       Sources located: "Administrative Silence: omission of public administration to react as an
       administrative decision-taking"; "Administrative silence as the challenge in regulation of
       administrative proceedings… EU countries"; "When silence equals refusal," World IP Review.
       — SECONDARY (search summaries retrieved; no primary statute or full text read this run) — This is
       the strongest available challenge and it is a whole doctrine, not a finding. Legal systems that
       have had to decide what silence means have universally refused to let it mean "pending
       indefinitely." They choose one of two constructions — silence is a REFUSAL (France from the Law of
       17 July 1889; Italy, Spain, Germany followed in the 20th century) or silence is an APPROVAL (the
       deregulatory model; EU practice commonly sets a three-month default after which an application is
       deemed granted) — and in both cases the *deadline* is the load-bearing element, because it is what
       makes the applicant's position reviewable. "Pending" with no deadline is the one option the
       doctrine treats as intolerable, precisely because it leaves the subject with no remedy.
    2. Dead-letter-queue design practice — AWS SQS DLQ documentation, Elastic Logstash DLQ documentation,
       and the practitioner literature (Vercel's DLQ guide, ActiveMQ DLQ management guides). — SECONDARY
       (search summaries; AWS/Elastic docs located but not fetched) — The named and universal failure mode
       is unbounded DLQ growth, and the named remedy is a retention/max-age policy plus alerting on DLQ
       *depth and age*. Practitioner formulation retrieved this run and worth quoting for its precision:
       a message that ages out of the queue unexamined is one you decided to lose without deciding to lose
       it. Typical stated max-age bands for never-processed records are 30–90 days, at which point the
       record is summarised and archived or discarded — i.e. the discipline is that the reclassification
       threshold must be *stated*, which is precisely 14b's proposal.
    3. Internal-audit follow-up literature — EUROSAI "Follow-up of the implementation of audit
       recommendations: best practices guide"; the ISACA follow-up-audit material; "Literature Review on
       Non-Implementation of Internal Audit Recommendations in an Organization." — SECONDARY (search
       summaries; EUROSAI PDF located but not retrieved) — The profession's answer to "is this
       recommendation pending or declined?" is an explicit tri-state rating (Implemented / Partially
       Implemented / Not Implemented) assigned at a scheduled follow-up, plus a target horizon — one SAI
       uses 90% of unresolved major-study issues addressed within three years. The discipline exists
       because the profession discovered that without a scheduled re-rating, "open" absorbs both
       categories. NEGATIVE RECORDED: I could not retrieve a reliable overall non-implementation base
       rate; the figures surfaced (71% completed in one 45-recommendation follow-up; a 90% three-year
       target) are single-organisation and are not a literature base rate. No weight rests on them.
    4. Alarm shelving semantics, EEMUA 191 — SECONDARY (search summary) — a deliberately suppressed signal
       carries a default expiry (4 hours) after which it un-suppresses itself. The design principle is
       that suppression must be self-clearing; a human-blocked item with no expiry is suppression with no
       clearing.

  Strength of challenge: **Strong**.
    Limb split:
      - "Thirty days of no ruling is a decision pending": **Strong** challenge. The administrative-silence
        doctrine exists because this construction was tried and abandoned; DLQ practice treats it as the
        canonical defect; PREMISE-133 and PREMISE-154 already hold the estate to the contrary.
      - "The correct reclassification is 'declined'": **Weak** challenge — indeed the literature partly
        cuts the other way. The deemed-approval model is equally well-attested and is the *dominant*
        modern direction (deregulatory, business-oriented). So the doctrine supports "silence must be
        given a construction" much more strongly than it supports "the construction is refusal." For
        C2A2, deemed-approval would mean: after N days with no ruling, the agent is authorised to make the
        repair. That reading is at least as well-supported and is operationally far better, since the four
        registers get fixed.
      - "A stated threshold is required": **Strong**. Universal across all four source families.
    The recommendation rests on the first and third limbs. The second limb — which way to construe the
    silence — is a design choice the literature does not settle, and I am explicitly not recommending
    "declined" over "deemed authorised."

  Summary: Every domain that has had to formalise what silence means has refused to leave it
    unconstrued. Administrative law gives it a construction by statute and attaches a deadline; DLQ
    practice gives it a max-age and alerts on age; audit practice gives it a scheduled re-rating with a
    tri-state outcome. The common element is not the direction of the default but the existence of a
    stated threshold, and that is exactly what the estate lacks: nothing distinguishes an item awaiting a
    ruling from an item declined by silence, and `decisions.md` has not moved in fourteen days while nine
    rulings are owed. The register already holds the governing rule twice (PREMISE-133, PREMISE-154) and
    the second of those was minted specifically to cover this cohort. Notably, the literature is *more*
    favourable to a deemed-authorisation default than to a deemed-decline default, which would resolve the
    four corrupted registers rather than merely re-labelling their status.

  Specific risks: Four live registers carry a defect that has demonstrated it can corrupt an append. The
    defect is held open by a ruling that may not be coming, and the holding pattern is itself the reason
    no agent may repair them — so the mechanism that protects the registers from unauthorised change is
    the mechanism preventing their repair. Under PREMISE-102 this is not a pending state at all: repeated
    identical non-processing in a zero-throughput channel has already converted into an undecided standing
    policy of non-coverage. The item is 31 days old today and has misfired at least once.

  Mitigations available:
    - **State a threshold.** One number in the protocol: items tagged "needs a human" reclassify at N
      days. This is the entire fix for the third limb and costs one line. 14b's `stat` supplies N by
      giving the current age distribution.
    - **Choose the construction deliberately, and prefer deemed-authorisation for reversible repairs.**
      Distinguish irreversible decisions (which must remain deemed-declined and escalate louder) from
      reversible one-line repairs under version control (which can safely deem-authorise at expiry). The
      duplicate-anchor fix is in the second class. PREMISE-176 supplies the discriminator: for an
      irreversible operation, reversibility is the control, not review.
    - **Alert on age, not depth.** PREMISE-147's statistic, and DLQ practice's, are the same statistic.
    - **Separate the objects.** PREMISE-167 requires that an escalation have a representation on disk
      distinct from the normal case; "needs a human" currently has no representation distinguishable from
      staleness, which is why one `stat` is even necessary.

  STEELMAN:
    Item: PRESUMPTION-951
    Strongest counterargument: The addressee is one person, not an institution, and the
      administrative-silence doctrine is built for institutions with staff, statutory duties and a
      caseload — where silence really does indicate capacity failure or evasion. A single principal who
      answered 36 cards in one act on 2026-09-09 is not silent; he is batching. Latency and abandonment
      look identical over a 30-day window but are radically different processes, and the estate has direct
      positive evidence of the first (the batch APPROVE) and no evidence at all of the second. Worse, an
      auto-reclassification rule in a single-principal system does not route the item anywhere — it just
      changes a label on an item nobody is working on, which manufactures the appearance of resolution
      while the defect remains. And a deemed-authorisation default hands an agent write access to
      registers it was deliberately denied, by the passage of time rather than by a decision — which is a
      capability grant obtained by waiting, and PREMISE-196 holds that capability withholding is the
      strong control precisely because it is not probabilistic.
    What would need to be true for C2A2 to be safe: (a) the latency distribution must be bounded — i.e.
      items do eventually get rulings, and the 36-card batch is representative rather than exceptional;
      (b) an item reclassified as declined must go SOMEWHERE, not merely change label, or the
      reclassification is itself PRESUMPTION-949's defect; (c) if deemed-authorisation is adopted, it must
      be scoped to reversible repairs with a tombstone, per PREMISE-176, and must never widen a write
      scope by default. All three are satisfiable and none is satisfied today.
    How to test: 14b's `stat`, exactly as specified — the age distribution of items tagged "needs a human"
      across the estate. Add the survival question, which is the one that discriminates: of items tagged
      "needs a human" in the last 90 days, what fraction received a ruling, and at what age? A distribution
      with a long right tail and a high eventual-resolution rate supports the steelman (latency). A
      distribution where a large fraction never resolves supports the presumption's challenge
      (abandonment). This is one pass over the registers and it is decisive.

  Search scope: comprehensive — administrative-silence / deemed-refusal / deemed-approval doctrine across
    EU jurisdictions; dead-letter-queue retention and aging design (AWS SQS, Logstash, ActiveMQ,
    practitioner guides); internal-audit follow-up and recommendation-implementation practice; alarm
    shelving expiry semantics. NEGATIVE RECORDED: no reliable cross-organisation base rate for
    audit-recommendation non-implementation was retrievable, and none of this file's ratings depends on
    one.

  Recommendation: CHALLENGED

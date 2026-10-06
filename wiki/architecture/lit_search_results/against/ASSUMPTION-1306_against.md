SEARCH-AGAINST-ASSUMPTION-1306:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1306
  Original statement: "A post-run sweep found the same defect in `arkanihamed`, `stump`, `loughran`,
    `macintyre` — all already logged as 'needing a human' on 2026-08-11. **It has now actually misfired
    once, so it stops being a tidiness note.**"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1306
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim. The defect was logged 2026-08-11 and is thirty days unruled; the
        manifestation is what moved it, not the elapsed time. Raised as OPEN-193.
      15b: Searched for challenging literature; found the rule is the definition of reactive/run-to-
        failure maintenance, that it is legitimate ONLY under a prior criticality assessment that was
        never made here, and that the manifestation itself disqualifies the remaining four from it.
    Current status: CHALLENGED

  Register pre-check:
    - PREMISE-202 (ACTIVE) — "A HARM AVERTED BY CHANCE IS AN EVENT AND OPENS A RECORD; 'damage is nil,
      but by luck' is the criterion for OPENING an item, not for CLOSING one." On the accident-precursor
      definition. **This is a direct pre-answer and it denies the assumption**: the four un-manifested
      registers are precursors, and precursor status is itself the ground for opening.
    - PREMISE-130 (ACTIVE) — RECURRENCE RECLASSIFIES: when the same component fails repeatedly in
      distinct signatures the unit of analysis is a DEFECT CLASS, not independent bugs; prior fault count
      is the dominant predictor of future faults. Five registers with one shared defect is a class.
    - PREMISE-128 (ACTIVE) — a defect that produces no error and plausible-looking output cannot be
      certified benign; blast radius is unknown at the point of failure. The hoffman misfire landed four
      triplets mid-file with no exception raised — this is exactly that class.
    - PREMISE-151 (ACTIVE) — repeated disclosure of an unremediated condition normalises it; the
      disclosure record is evidence of incubation, not management. Thirty days of "needing a human."
    - PREMISE-118 (ACTIVE) — naming a defect in an instrument does not license continued use; it triggers
      contain / assess impact / fix cause / verify, **including a retrospective impact assessment over
      every result since last known-good**. Not done for the four.
    - PREMISE-173 (ACTIVE) — a remedy consisting only of observing/recording is not a remedy; name the
      final element.

  Challenging evidence found: Yes

  LIMB STRUCTURE — two limbs:
    LIMB A — "manifestation is sufficient to raise priority." (Trivially true and uncontested.)
    LIMB B — "manifestation is NECESSARY — before it misfires, it is a tidiness note." (The live limb;
      this is what licensed leaving the other four in place.)

  Sources:
    1. Dillon, R.L. & Tinsley, C.H. (2008). "How Near-Misses Influence Decision Making Under Risk: A
       Missed Opportunity for Learning." *Management Science* 54(8), 1425-1440. — SECONDARY (abstract and
       multiple independent summaries retrieved; full text not retrieved) — People who receive
       information about prior near-misses make **riskier** subsequent decisions than those who receive
       no such information, because they process the near-miss as a signal of relief rather than a
       warning; both novices and field experts showed the effect. The four un-manifested registers are
       near-misses, and this is the measured bias that makes them feel like tidiness notes.
    2. Dillon, Tinsley, Madsen & Rogers (2016). "Organizational Correctives for Improving Recognition of
       Near-Miss Events." *Journal of Management*. — UNVERIFIED (title and venue confirmed via SAGE
       listing; I did not retrieve the article) — cited only to record that an organisational-corrective
       literature exists; carries no weight in the rating.
    3. Run-to-failure / reactive maintenance literature (Tractian, eMaint, MaintainX, Makula, Cryotos
       glossaries and practitioner guides; RCM tradition) — SECONDARY (several independent practitioner
       sources retrieved; no primary RCM standard retrieved) — **This is the most interesting result and
       it cuts both ways.** Run-to-failure is a *legitimate, named* strategy — but only where a prior
       criticality assessment establishes that failure has no safety, quality or production consequence,
       and it is conventionally scoped to roughly 20% of assets, with safety-critical and
       production-critical assets explicitly excluded. The rule "wait until it misfires" is RTF applied
       *by default rather than by assessment*, which is the form the same literature calls reactive
       maintenance and treats as the failure mode.
    4. Deming / SPC and the outcome-bias tradition (Baron & Hershey 1988 lineage, via the SPC and
       near-miss summaries retrieved) — SECONDARY/UNVERIFIED — judging the quality of a decision by its
       realised outcome rather than by the information available at decision time is the textbook
       definition of outcome bias. "It has now actually misfired once" is an outcome-keyed priority rule.

  Strength of challenge: Strong (on LIMB B, which is the limb that matters)

  Summary: The assumption's operative limb is the necessity direction — that absent manifestation, a
    known latent defect is a tidiness note — and the literature runs against it from three directions at
    once. Near-miss research measures the specific bias this rule institutionalises: unmanifested
    precursors are systematically read as reassurance rather than warning, by experts as well as novices.
    Maintenance engineering does contain a legitimate "wait for failure" strategy, but it is licensed by
    a prior criticality assessment, not by the accident of which instance fired first — and the very fact
    that the defect DID misfire, silently, mid-file, reclassifies the failure consequence and removes the
    remaining four from RTF eligibility. The register already denies the assumption twice over:
    PREMISE-202 makes a harm-averted-by-chance the criterion for opening a record, and PREMISE-130 makes
    five instances of one defect a class rather than five notes. Nothing in this search supports leaving
    `arkanihamed`, `stump`, `loughran` and `macintyre` in place.

  Specific risks: Four registers carry a known, now-demonstrated corrupting defect. Its signature is
    silent (PREMISE-128): no exception, plausible-looking output, appended content landing mid-file where
    later readers will parse it as if it were in sequence. The blast radius is unknown by construction,
    and the retrospective impact assessment PREMISE-118 requires has not been run over any of the five.
    Worse, the *rule itself* is the durable risk: it licenses every future latent defect to sit until it
    fires, in a system whose defects are specifically of the silent kind. With one misfire already
    observed in five known instances, a naive rate puts the remaining exposure at four more.

  Mitigations available:
    - Apply PREMISE-118 as written: contain, assess impact retrospectively over all five registers since
      2026-08-11, fix cause, verify. The impact assessment is the missing step, not the fix.
    - Replace the manifestation trigger with a criticality trigger: a defect whose failure mode is SILENT
      is never RTF-eligible, regardless of how tidy it looks. That is one sentence of policy and it is
      the RCM answer.
    - Add the max-id-vs-stated-total check (which caught the hoffman case in-run) as a standing
      pre-append assertion on all ten registers, so the defect cannot misfire silently anywhere.
    - Treat the four as a defect class per PREMISE-130 and close them as one item, not four.
    - The "renumbering live ids is your decision" escalation needs a date and an owner; per PREMISE-102
      and PREMISE-138, filing it into a channel with demonstrated zero throughput is not a mitigation.

  STEELMAN:
    Item: ASSUMPTION-1306
    Strongest counterargument: Priority is a scarce resource and manifestation is genuine Bayesian
      evidence — it raises the estimated probability that the defect is reachable in practice, not merely
      in principle, and a triage system that cannot use reachability evidence will drown in theoretically
      possible faults. The run did not *ignore* the other four; it swept for them, found them, recorded
      them, and declined only the specific act of renumbering live IDs, which is destructive and outside
      a daily run's authority. That is not run-to-failure; it is correctly refusing to take an
      irreversible action unilaterally (PREMISE-176) while raising the item's priority on new evidence.
      Read that way the assumption is a statement about *evidence*, and it is correct.
    What would need to be true for C2A2 to be safe: (1) the four un-repaired registers must not be
      appended to before the repair, or the append path must carry the max-id check — otherwise the raised
      priority buys nothing; (2) the escalation must reach a channel that acts, within a stated window;
      (3) the failure mode must actually be benign in the interim, which PREMISE-128 says cannot be
      certified from the visible outcome; and (4) the priority raise must be recorded as a *class* item
      with a closure test, not four notes.
    How to test: In-house and decisive. Run the max-id-vs-stated-total check retrospectively over all
      ten `prs_triplets.md` registers for every append since 2026-08-11 and count how many appends landed
      mid-file. If the answer is 1 (the hoffman case), the interim really was benign and the steelman
      holds. If it is >1, limb B has already cost the estate data integrity and the manifestation trigger
      is refuted empirically, in-house, today. Cost: one script, one pass.

  Search scope: comprehensive for the near-miss and maintenance-strategy angles; preliminary elsewhere.
    Searched: near-miss reporting and near-miss bias (Dillon & Tinsley lineage); outcome bias; run-to-
    failure / reactive vs proactive maintenance and RCM criticality assessment; latent-fault
    prioritisation in software; normalization of deviance. NOT searched: the aviation ASRS/CHIRP
    voluntary-reporting effectiveness literature, and the software-specific "dormant defect" /
    defect-latency studies, either of which could sharpen the quantitative side.

  Recommendation: CHALLENGED — resting on LIMB B. LIMB A is NO-CHALLENGE-FOUND (and uninteresting).

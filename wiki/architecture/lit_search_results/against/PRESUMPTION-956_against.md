SEARCH-AGAINST-PRESUMPTION-956:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-956
  Original statement: "[inferred] That an agent's edit boundary is also its responsibility boundary —
    that declining to fix something outside one's write scope discharges the finding."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-956
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from two independent runs declining two different repairs on the same ground on the
        same day; both instances are correct agent behaviour under the current design, so the presumption
        is in the design, not the conduct.
      15b: Searched for challenging literature; retrieved AHRQ's handoff standard, which states the
        contrary explicitly and in the form of a rule ("you are accountable until the other party is
        aware of the transfer"), and found PREMISE-163 holding the same thing in the register.
    Current status: CHALLENGED

  Register pre-check — 14b's guess was right; PREMISE-163 bears directly:
    - **PREMISE-163 (ACTIVE).** "Production-completion is not lifecycle-completion. A producer may be
      retired only through a HANDOVER GATE THAT NAMES A SUCCESSOR OWNER for the open defect classes in its
      output; the producer's continued existence is NOT the control." The mechanism PRESUMPTION-956 says
      does not exist — a handover gate naming a successor owner — is already the register's stated
      requirement for a different transition. Extending it from producer-retirement to scope-boundary
      transfer is a scope extension, not a new premise.
    - **PREMISE-108 (ACTIVE) — decisive.** "Transmission is not delivery. A finding 'flagged for' a named
      agent does not transfer responsibility for it; the loop is closed only on evidence that the
      recipient received AND acted, and until then the finding is held by nobody while the record shows it
      discharged. That state is worse than not flagging." Writing the finding down is transmission. It is
      not delivery, and the register says so.
    - PREMISE-123 (ACTIVE) — a validated finding does not reach the agent it governs unless an explicit
      propagation mechanism carries it; producing a FLAG and changing behaviour are distinct steps.
    - PREMISE-131 / 138 / 173 (ACTIVE) — the warning/final-element family; PREMISE-138's only admissible
      function for repetition in an effector-less channel is "transfer of obligation to a NAMED ACTOR
      outside the channel," which is precisely what a scope-declination does not do.
    - PREMISE-186 (ACTIVE) — "AN ABSENCE OF INSTRUCTION IS NOT A GRANT; RESIDUAL DECISION AUTHORITY IS AN
      ALLOCATION; AND A SPECIFIED TERM IS NOT A GAP." The corollary that bears: an absence of a routing
      obligation is not a determination that none is owed; it is an unallocated residual.
    - PREMISE-196 (ACTIVE) — cuts the other way, and must be reported: an access restriction enforced in
      the capability grant has a lower violation rate than the same restriction expressed as an
      instruction. The write-scope limit is a real and well-chosen control and nothing here argues for
      widening it.

  Challenging evidence found: Yes

  Sources:
    1. Agency for Healthcare Research and Quality, TeamSTEPPS 3.0, "Tool: Handoff" (content last reviewed
       May 2023). — **VERIFIED** (page retrieved and read in full, 2026-09-11) — This is the single
       clearest refutation available and it is a federal standard of practice, stated as a rule:
         - "A handoff is a standardized method for transferring information, **along with authority and
           responsibility**, during transitions in patient care."
         - "**Transfer of responsibility and accountability:** When handing off, it is your responsibility
           to know that the person who must accept responsibility is aware of assuming responsibility.
           Similarly, **you are accountable until the other party is aware of the transfer of
           responsibility.**"
         - "**Acknowledgment by receiver:** Until it is acknowledged that the handoff is understood and
           accepted, **you cannot relinquish your responsibility.** This step is particularly crucial for
           handoffs that occur electronically."
         - "You must use appropriate communication channels and **cannot assume that the person obtaining
           responsibility will read or understand the communication without confirmation.**"
       Note the specificity of the last two to C2A2's case: the standard singles out electronic handoffs
       as the ones most needing acknowledgement, and explicitly forbids assuming the recipient will read.
       AHRQ also records the causal basis: "Lack of clarity about who is responsible for care and for
       decision making or exactly when the authority is being transferred have been major contributors to
       medical error (as identified in root cause analyses of sentinel events and poor outcomes)."
    2. Incident-management and on-call handoff practice (incident.io on-call best practices; escalation-
       management frameworks; shift-handover practice in mission-critical control rooms; the XFlow
       multi-agent protocol paper, arXiv:2606.14790). — SECONDARY (search summaries) — The engineering
       formulation converges on the same rule and adds the piece C2A2 lacks: "responsibility transfer
       determines who owns the next action after a condition is met," and it is explicitly distinguished
       from control flow — "a transition says where execution may go, while a handoff says which actor or
       role should continue the work." That distinction is exactly what the estate is missing: it has a
       write-scope topology (control flow) and no ownership topology (handoff). The named recurring
       failures in incident rehearsals are "delayed escalations, unclear handoffs."
    3. Patient-safety incident-report processing literature (PMC12510765). — SECONDARY — reporters'
       measured experience that reports were not discussed and produced no concrete changes; the
       structural point being that a report routed to a generic recipient is a report with no owner.
    4. Cyentia Institute / Kenna Security, P2P Vol. 3 (2019). — VERIFIED at the authoring institute's own
       summary — "the typical organization only fixes about 10% of its vulnerabilities in any given
       month," and capacity is invariant to finding volume. Included here because it bounds the steelman:
       queueing every scope-blocked finding behind one actor has a measured throughput ceiling in
       environments far better staffed than this one.

  Strength of challenge: **Strong**.
    Limb split:
      - "An agent's write scope should be limited": **No challenge**, and it should not be recorded as
        one. PREMISE-196 supports it; AHRQ says nothing against it; the safety property is real and
        deliberately chosen. Both of today's agents behaved correctly.
      - "The write-scope limit therefore carries no routing obligation": **Strong** challenge. AHRQ states
        the rule in the opposite direction — accountability persists until the receiver acknowledges — and
        PREMISE-108 and PREMISE-163 hold the same thing in the register. An absence of a stated routing
        obligation is PREMISE-186's unallocated residual, not a determination that none is owed.
      - "Writing the finding down discharges it": **Strong** challenge. This is PREMISE-108 verbatim and
        AHRQ's "cannot assume that the person obtaining responsibility will read or understand the
        communication without confirmation."
      - "The only escalation path is upward to a human, and that is acceptable": **Moderate-to-Strong**
        challenge. The handoff literature's requirement is a NAMED receiver who ACKNOWLEDGES; a single
        unacknowledging addressee satisfies neither half, and the Cyentia ceiling bounds what one
        addressee can absorb. But the literature does not establish that agent-to-agent repair is the
        right remedy, only that the current arrangement is not a transfer.
    The recommendation rests on the second and third limbs. It does NOT rest on any claim that write
    scopes should be widened.

  Summary: The challenge is strong and it is unusually clean, because the question C2A2 is asking has a
    published federal answer. AHRQ's handoff standard makes the transfer of responsibility a distinct act
    from the transfer of information, requires the receiver's acknowledgement before the sender may
    relinquish, and specifically warns against assuming an electronic recipient will read. On that
    standard, "`inbox/` and `approved/` are outside what this agent edits" describes a capability boundary
    correctly and says nothing about where the responsibility went — and the register already holds the
    same rule twice, as PREMISE-108 (transmission is not delivery; the flagged-and-unheld state is worse
    than not flagging) and PREMISE-163 (a producer is released only through a handover gate that names a
    successor owner). The novel content of PRESUMPTION-956 is not that the boundary is wrong, but that the
    estate has a control-flow topology and no ownership topology: nothing in the design says who holds a
    finding after the agent that raised it cannot act on it. That is an unallocated residual under
    PREMISE-186, and both of today's instances are live one-line fixes sitting in it.

  Specific risks: Two live defects with known one-line fixes will recur on every run until a human acts,
    and the estate's human-latency figure is fourteen days. One of them (PROP-2026-08-14-033, held against
    a retrieval target WATCH-002 retired on 09-08) will misfire on every future ingest. Compounding: under
    PREMISE-108 the record shows both findings discharged while nobody holds them, which is the state the
    premise calls worse than not flagging — so the estate's defect ledger systematically overstates how
    much has been handled, and the overstatement grows with every correctly-behaved agent. Because the
    only addressee is the same human PRESUMPTION-953 is about, 956 and 953 fail together: 956 makes the
    human the sole receiver and 953 asks whether the receiver receives.

  Mitigations available:
    - **Add an acknowledgement requirement, not a wider write scope.** AHRQ's rule needs no new
      capability: a finding raised outside scope stays OPEN and attributed to the raiser until a named
      receiver acknowledges. This is a status-lifecycle change, not a permissions change, and it preserves
      PREMISE-196's capability control entirely.
    - **Scope-extend PREMISE-163 from producer-retirement to scope-boundary transfer.** The handover gate
      that names a successor owner already exists as a requirement; it is currently scoped to one
      transition and this is a second one of the same shape.
    - **Build an ownership topology.** One table: for each register/directory, which agent holds write
      scope. A finding outside the raiser's scope routes to the holder by lookup rather than to the human
      by default. This is the "which actor should continue the work" layer the incident-management
      literature distinguishes from control flow, and it does not require agent-to-agent write access —
      only agent-to-agent addressing.
    - **Where no holder exists, say so in the finding.** "No agent in the estate holds write scope for
      `inbox/`" is materially different information from "outside what this agent edits," and it is the
      sentence that would have made the design defect visible on 08-14 rather than on 09-10.
    - **Run 14b's count** — findings closed in the last 30 days by an agent other than the one that raised
      them. If near zero, the ownership topology does not exist as a path and the estate should say so
      explicitly rather than leave it as an assumed capability.

  STEELMAN:
    Item: PRESUMPTION-956
    Strongest counterargument: Write-scope limits are a safety property and the pressure this item creates
      runs directly against it. PREMISE-196 holds that a restriction enforced in the capability grant has a
      lower violation rate than the same restriction expressed as an instruction — which is exactly why
      the boundary is a grant and not a policy. An agent that acquires a "routing obligation" acquires a
      soft pressure to find a way to discharge it, and the cheapest way to discharge it is to route to an
      agent that *does* hold the scope, which is one short step from an agent-to-agent repair channel with
      no human in it. That channel is the thing the design deliberately does not have. Moreover, AHRQ's
      standard is built for a setting with a defined receiving role always staffed on the next shift; C2A2
      has no such role for `inbox/`, so "hand off to the owner" is not an available act — there is no
      owner. Declining a repair one is not authorised to make, and writing down precisely what the repair
      is, may genuinely be the maximal correct act available, and both agents performed it. On this
      reading the finding is not undischarged; it is correctly parked at the only boundary the design
      admits, and the defect is a staffing gap in the human layer rather than a design flaw in the agent
      layer.
    What would need to be true for C2A2 to be safe: (a) the sole receiver must actually receive — which is
      PRESUMPTION-953 and is unmeasured; (b) the parked findings must not compound — a one-line fix that
      misfires on every ingest is compounding, so at minimum the ledger must distinguish inert parked
      findings from active recurring ones; (c) the record must not claim more than it delivers — a finding
      marked as transferred when it is merely written is the PREMISE-108 state and is worse than no flag;
      (d) if there is genuinely no owner for a scope, that fact must be recorded as a design finding in its
      own right rather than re-derived each time an agent bumps into it. (c) and (d) cost nothing and are
      compatible with every word of the steelman.
    How to test: 14b's count, plus one discriminator that separates the steelman from the presumption.
      Count findings closed in the last 30 days by an agent other than the raiser (expect near zero). Then,
      for every scope-blocked finding raised in that window, record whether any agent in the estate holds
      write scope for the target. If the answer is usually "yes, another agent could have," the ownership
      topology is missing and the presumption holds. If the answer is usually "no agent holds it," the
      steelman holds and the correct item is a human-layer staffing finding, not an agent-design one. Both
      counts come from one pass over the registers plus the scope table.

  Search scope: comprehensive — clinical handoff standards (AHRQ TeamSTEPPS, I-PASS, SBAR family),
    incident-management escalation and on-call handoff practice, shift handover in control rooms,
    multi-agent responsibility-transfer protocol work, and referral/closing-the-loop duties. NOT RETRIEVED:
    the Joint Commission handoff standard and the I-PASS trial (located in the AHRQ curriculum navigation
    but not fetched) — recorded as a gap; nothing in this file depends on them, since the AHRQ tool page
    was read in full and states the rule directly.

  Recommendation: CHALLENGED

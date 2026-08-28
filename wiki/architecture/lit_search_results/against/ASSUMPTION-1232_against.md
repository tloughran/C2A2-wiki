SEARCH-AGAINST-ASSUMPTION-1232:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1232
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: When an instruction's wording does not support the distinction an agent draws,
    governance practices short of halting exist and are appropriate.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1232
    Item type: ASSUMPTION (stated self-disclosure)
    Transform at each step:
      14a: Extracted verbatim; filed alongside ASSUMPTION-1223 as the second unratified-convention instance
        of the day.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: WebSearch, 2026-08-28, one dedicated query on whether an agent should halt or abstain under
    ambiguity. Reached: Orseau & Armstrong, "Safely Interruptible Agents" (MIRI-hosted copy of the UAI 2016
    paper); arXiv 2606.02965 on evaluating abstention competence in autonomous agents; arXiv 2608.00783 on
    safety invariants for irreversible state transitions; Microsoft Learn's guidance on reducing autonomous
    agentic AI risk; Microsoft Security's defence-in-depth post (2026). NOT COVERED: the incomplete-contracts
    literature; and any empirical study measuring outcomes of escalation vs abstention. All SNIPPET-ONLY.
    Confidence: MODERATE.

  Challenging evidence found: Yes

  Sources:
    1. Anon. (2026), "What Benchmarks Don't Measure: The Case for Evaluating Abstention Competence in
       Autonomous Agents" (arXiv:2606.02965) [SNIPPET-ONLY; authors unverified] —
       Scores conservative refusal, preview and clarification requests as *passes* on under-specified
       prompts: "refusing on an under-specified prompt is itself correct safety behaviour." Introduces
       Informed Refusal Rate — the fraction of blocking responses naming the specific unmet precondition —
       as the quality measure. This challenges the assumption's framing that halting is the option to avoid.
    2. Microsoft Learn, "Reduce autonomous agentic AI risk" [SNIPPET-ONLY]
       https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-risk —
       Human oversight means meaningful control to guide, correct and interrupt "especially when input is
       ambiguous." Ambiguity is named as the trigger for human control, not for autonomous interpretation.
    3. Orseau, L., & Armstrong, S., "Safely Interruptible Agents" [SNIPPET-ONLY]
       https://intelligence.org/files/Interruptibility.pdf ; arXiv 2608.00783 on irreversible state
       transitions [SNIPPET-ONLY; authors unverified] — Interruptibility as a design requirement, and a
       sharper boundary condition: the tolerance for autonomous interpretation should scale inversely with
       the irreversibility of the action.

  Strength of challenge: Moderate-Strong

  Summary: The challenge is that the assumption's own remedy set does not exist independently of a human,
    and this estate's human channel has a demonstrated multi-week latency. Every practice the for direction
    located — confidence-threshold escalation, human-in-the-loop checkpoints, risk-class routing — is a
    referral, and a referral into an unresponsive channel is a halt with extra steps and no record that it
    is one. The abstention literature pushes further: on an under-specified instruction, refusal is scored
    as the *correct* behaviour, with the quality measure being whether the refusal names the unmet
    precondition. That inverts the item's framing. The one clean concession the against direction makes is
    that indiscriminate refusal is also a failure — an agent that refuses everything is broken, not safe —
    so the answer is a threshold, and the estate has not set one.

  Specific risks: (a) "Governance short of halting" becomes, in practice, "proceed on my own reading and log
    it," because the escalation target does not answer — which is autonomous rule-making with an audit trail
    rather than governance. (b) The irreversibility dimension is unhandled: the same interpretive latitude is
    being applied to reversible and irreversible actions alike. (c) This is the day's second unratified
    convention (with ASSUMPTION-1222), and the pattern is the finding.

  Mitigations available: Adopt informed refusal as the default for irreversible actions: block, name the
    unmet precondition, and record it as blocked rather than as decided. For reversible actions, proceed on
    the stated reading but tag the output with the interpretation taken, so it can be reversed cheaply when
    the human channel opens. Set the threshold explicitly by reversibility rather than by confidence.

  STEELMAN:
    Item: ASSUMPTION-1232
    Strongest counterargument: An agent that halts on every wording ambiguity in an estate this large would
      halt permanently, since natural-language instructions are ambiguous everywhere on inspection. The
      abstention literature itself concedes this — refusing everything is broken. Given a human channel that
      does not answer, proceeding on a declared interpretation and recording it is the only option that
      keeps work moving *and* keeps the interpretation reviewable; the alternative is an estate that
      produces nothing and has no record of why.
    What would need to be true for C2A2 to be safe: the interpretations taken would have to be enumerable
      and reversible — recorded in one place, with the actions they licensed traceable — so that a later
      human ruling can be applied retroactively rather than only prospectively.
    How to test: ask whether any such register exists. If the interpretations are scattered through run
      reports, they are not reviewable and the steelman fails on its own terms. (This is the same object
      PRESUMPTION-887 names as shadow policy; the two items should be read together.)

  Recommendation: CHALLENGED

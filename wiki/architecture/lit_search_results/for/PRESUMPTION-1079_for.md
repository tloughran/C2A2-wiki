SEARCH-FOR-PRESUMPTION-1079:
  Date searched: 2026-09-24
  Original item: PRESUMPTION-1079
  Original statement: Escalation to an absent authority works as a terminal state for automated
    agents and does not produce action.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1079
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred the unstated presumption that "escalate to human" ends the run without effect.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Bainbridge, L., 1983. "Ironies of Automation." Automatica 19(6). — Automation leaves the human
       responsible for monitoring and takeover in abnormal situations; when that human is absent or
       out of practice, the escalation path fails to produce corrective action. Theoretical support
       that escalation without a present responder is effectively a dead end.
    2. Cvach, M., 2012. "Monitor Alarm Fatigue: An Integrative Review." Biomedical Instrumentation &
       Technology 46(4):268–277 (PubMed 22839984). — 72-article review: excessive alarms lead to
       desensitization and alarms being silenced or ignored. Empirical precedent that escalation
       signals routinely terminate without action when the recipient is saturated or absent.
    3. Darley, J.M. & Latané, B., 1968. "Bystander intervention in emergencies: Diffusion of
       responsibility." JPSP 8(4):377–383 (DOI 10.1037/h0025589 per listing). — Helping fell from
       85% to 31% when others were believed present. Analogous support: handing a problem to "someone
       else" reduces the probability anyone acts.
    4. LangChain "Human-in-the-loop" and Temporal "Human-in-the-loop AI agent" documentation (primary
       framework docs, seen in search). — Standard HITL interrupts pause execution and persist state;
       agents can wait "for hours, days or indefinitely." Confirms that in mainstream frameworks
       escalation is implemented as a blocking wait, i.e., a terminal state absent a responder.
    5. "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety,"
       NeurIPS 2025 / arXiv 2510.16492 (seen in search; authors unconfirmed). — Quitting/withdrawal is
       a designed terminal state that improves safety (+0.39 on 0–3 scale) with little helpfulness
       loss; supports treating non-action as the intended outcome of escalation.

  Strength of support: Moderate

  Summary: Two literatures support the presumption in different senses. Human-factors and social-
    psychology work (Bainbridge; alarm fatigue; diffusion of responsibility) shows that escalation to
    an absent or overloaded authority reliably yields no corrective action. Agent-framework practice
    and the selective-quitting literature show that escalation is typically built as a blocking,
    terminal state. Together these support "does not produce action" as the expected outcome.

  Caveats: The presumption bundles a descriptive claim (no action results) with a normative one
    (it "works as" a terminal state). Support is stronger for the descriptive half. The literature on
    agent "compulsion to act" (cited within the quitting paper) and on escalation after tool failure
    suggests agents do not always stop at escalation; that evidence bears against and is left to 15b.
    Human-alarm findings transfer to automated agents only by analogy.

  Search scope: Preliminary — four searches (automation surprises/out-of-the-loop; alarm fatigue;
    bystander effect; HITL agent deferral) plus one on agent quitting.

  Excluded results: dev.to, Galileo, permit.io, Elastic and IBM tutorial blogs on HITL (vendor
    content); Medium posts on Bainbridge; Quizlet flashcard page for Darley & Latané (PubMed record
    used instead).

  Recommendation: PARTIALLY-SUPPORTED

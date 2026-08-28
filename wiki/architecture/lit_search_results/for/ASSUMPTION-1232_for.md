SEARCH-FOR-ASSUMPTION-1232:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1232
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: When an instruction's wording does not support the distinction an agent draws,
    governance practices short of halting exist and are appropriate.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1232
    Item type: ASSUMPTION (stated self-disclosure)
    Transform at each step:
      14a: Extracted verbatim; filed alongside ASSUMPTION-1223 as the second unratified-convention instance
        of the day.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-28, one dedicated query on agent guardrails, underspecified prohibitions
    and escalation. Literature reached: vendor and practitioner guardrail frameworks (Reco, Atlan, Aembit,
    Salesforce, Kore.ai, Galileo), plus two arXiv papers — AGENTSAFE (2512.03180) and Policy-as-Prompt
    (2509.23994). NOT COVERED and material: the legal/administrative literature on interpretation of
    underspecified rules, and the incomplete-contracts literature in economics, either of which would have
    been a stronger and older evidence base than agent-safety vendor material. All sources SNIPPET-ONLY.
    Search confidence: LOW-MODERATE — the corpus reached is largely commercial.

  Supporting evidence found: Partial

  Sources:
    1. Galileo, "7 AI Agent Failure Modes and How to Prevent Them" [SNIPPET-ONLY]
       https://galileo.ai/blog/agent-failure-modes-guide — Names "underspecified negative instructions" as a
       recognised failure class, with the worked example of an agent that reschedules others' appointments
       because nothing said not to. Establishes that the *situation* the assumption describes is a named,
       expected condition rather than an anomaly.
    2. Anon., "AGENTSAFE: A Unified Framework for Ethical Assurance and Governance in Agentic AI"
       (arXiv:2512.03180) [SNIPPET-ONLY; authors unverified]; Anon., "Policy-as-Prompt" (arXiv:2509.23994)
       [SNIPPET-ONLY; authors unverified] — Present governance layers in which risk classes, escalation
       paths and audit logging are the response to boundary cases, rather than a halt.
    3. Reco, "Adding Guardrails for AI Agents: Policy and Configuration Guide" [SNIPPET-ONLY]
       https://www.reco.ai/hub/guardrails-for-ai-agents ; Aembit, "Agentic AI Guardrails" [SNIPPET-ONLY] —
       Document the practice set the assumption asserts exists: confidence-threshold escalation,
       human-in-the-loop checkpoints for high-stakes decisions, scope boundaries and action authorisation.

  Strength of support: Moderate on existence, Weak on adequacy

  Summary: The assumption's existence claim is supported: there is an identifiable practice set for an
    agent that meets an instruction it cannot cleanly apply, and it does not consist of halting. The
    published set is narrow — escalate on low confidence, checkpoint at high stakes, log the interpretation,
    keep the action inside pre-authorised scope — and every element of it terminates in a human decision.
    That is the whole of what was found. The literature reached is predominantly vendor material with an
    interest in the answer being "configure a guardrail," and no source measures whether these practices
    reduce misinterpretation; the support is for availability, not efficacy.

  Caveats: Corpus quality is the weakness here and it is not marginal — six of nine sources are commercial
    product pages. The two arXiv papers are unreviewed with unverified authorship. Nothing found addresses
    the case where the escalation target is unresponsive, which is this estate's actual condition.

  Recommendation: PARTIALLY-SUPPORTED

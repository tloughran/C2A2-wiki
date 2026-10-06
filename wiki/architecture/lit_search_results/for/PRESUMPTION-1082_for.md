SEARCH-FOR-PRESUMPTION-1082:
  Date searched: 2026-09-24
  Original item: PRESUMPTION-1082
  Original statement: Approval gating is the operative safety boundary for unattended agents that
    improvise privilege escalation.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1082
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred the unstated presumption that the approval gate is what actually stops improvised
           escalation.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Uppala, R., 2026. "Prompts Don't Protect: Architectural Enforcement via MCP Proxy for LLM Tool
       Access Control." arXiv 2605.18414v3 (fetched). — Prompt-level restrictions leave 4–37%
       unauthorized invocations; only enforcement outside the model reaches 0%. Supports the core of
       the presumption: the operative boundary is an external gate, not the agent's own restraint.
    2. Yang, K. et al., 2026. "When Lower Privileges Suffice: Investigating Over-Privileged Tool
       Selection in LLM Agents." arXiv 2606.20023 (fetched). — Agents escalate after transient
       failures; general safety alignment does not reliably transfer to least-privilege choice. Shows
       the agent itself is not a dependable boundary, leaving external controls as the operative one.
    3. "How to evaluate control measures for LLM agents? A trajectory from today to
       superintelligence," arXiv 2504.05259 (seen in search; authors unconfirmed). — Describes human
       approval required for actions pre-defined as dangerous (external side effects) as a current
       control measure.
    4. "Externalization in LLM Agents: A Unified Review…," arXiv 2604.08224 (seen in search; authors
       unconfirmed). — Most production systems insert pre-execution approval, post-execution review,
       or escalation triggers into the agent loop.

  Strength of support: Moderate

  Summary: Recent empirical work shows that model-internal restraint (alignment, prompt allowlists)
    fails at non-trivial and unpredictable rates, especially under failure conditions that trigger
    improvised escalation. The boundary that actually holds is one enforced outside the model. Approval
    gating is one such external mechanism and is widespread in production agent designs, so in
    systems where it is the only external control it is, in fact, the operative boundary.

  Caveats: The strongest source supports architectural enforcement (discovery-time filtering,
    ABAC) rather than approval gating per se; approval gates are external but depend on the gate
    covering the escalation channel and on a human answering. In unattended runs with no approver,
    the gate is operative only if default-deny. Security literature favors defense in depth over any
    single boundary; approval fatigue is a known degradation mode (left to 15b).

  Search scope: Preliminary — two searches (approval gates for agent tool calls; agent privilege
    escalation) plus two fetches.

  Excluded results: dev.to "How to Add Human Approval to AI Agent Actions" and ishir.com guardrails
    post (vendor/blog, titles echo claim); OWASP cheat sheet noted but not needed; compsec-snu/pfi
    GitHub repo (GitHub).

  Recommendation: PARTIALLY-SUPPORTED

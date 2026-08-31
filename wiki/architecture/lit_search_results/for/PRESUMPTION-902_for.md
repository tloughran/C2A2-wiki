SEARCH-FOR-PRESUMPTION-902:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-902
  Original statement: [inferred] An agent's job boundary is knowable in advance and encodable as a
    permission set.
  Generalizable limb searched: Can the set of capabilities an agent will need be determined ahead
    of execution and expressed as a static permission grant, with acceptable coverage?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run; no full-text reads. Searched
    together with ASSUMPTION-1235 and ASSUMPTION-1240 as the intake required, since 902 carries
    the counter-case to both. The 94.8% coverage figure below is snippet-level and unverified.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-902
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference as the load-bearing precondition of ASSUMPTION-1235 and
           ASSUMPTION-1240; neither remedy works unless the boundary is knowable in advance
      15a: Searched for supporting literature (2026-08-31)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. ALPS authors, 2026. "ALPS: Automated Least-Privilege Enforcement for Securing Serverless
       Functions." arXiv:2603.25393. — The strongest positive evidence found. Snippet reports 94.8%
       coverage for least-privilege extraction across an evaluation of 8,322 real-world functions
       on AWS, Google Cloud and Azure. If a required permission set can be derived automatically at
       ~95% coverage from code alone, the boundary is substantially knowable in advance for
       well-scoped units of work.
    2. Microsoft Security Blog, 2026-07-16. "Least privilege for AI agents: Identity, access, and
       tool binding." — Recommends treating every agent as a first-class principal with a
       lifecycle-managed identity, explicit roles, and tool usage scoped to a *preconfigured tools
       manifest*. This is the presumption stated as vendor-recommended practice.
    3. Microsoft, n.d. "Agent Control Specification: Portable runtime governance for AI Agents."
       commandline.microsoft.com. — A single manifest binds a Rego policy to the pre_tool_call
       intervention point and declares the tool the policy reasons about. Concrete evidence that
       ahead-of-time encoding of a boundary is an implemented, shipping practice.
    4. ToolGuardian authors, 2026. "ToolGuardian: Declarative Security for AI Agent-Tool
       Interactions." arXiv:2607.21835. — Snippet: fully specified realizations classify all
       scenarios correctly; ablations removing compositional and conformance rules substantially
       degrade performance. Supports the presumption *conditionally* — the boundary is encodable
       when the specification is complete, which is the whole question.
    5. Traefik Hub documentation, 2026. "Understanding Task-Based Access Control." — TBAC's
       effectiveness depends on well-structured OAuth scopes and JWT claims; works across agent
       frameworks without modification. Practical confirmation that pre-declared scopes are
       operationally workable.

  Strength of support: Moderate

  Summary: There is real support, but it is conditional and the same searches surfaced the
    conditions. On the positive side, automated derivation of a required permission set from code
    is demonstrated at ~95% coverage over thousands of real serverless functions, several major
    vendors ship manifest-based pre-declaration of agent tool scope, and TBAC is an operational
    pattern rather than a proposal. So for tasks with well-defined inputs, outputs and logic, the
    boundary is largely knowable in advance. On the other side, the literature is actively moving
    *away* from static sets: multiple 2026 papers frame task-scoped, dynamically derived permissions
    as the successor to static role assignment precisely because static grants become overscoped
    once one agent branches across systems in a single workflow, and one snippet asserts the general
    problem is formally undecidable — that it cannot be determined whether an arbitrary agent
    satisfies a safety property defined by a static permission set. The honest reading is that the
    presumption holds well for narrow, stable remits and degrades as the remit becomes open-ended
    or evolving. That is the exact profile of a general analysis agent, which weakens the transfer
    to this case.

  Caveats: (a) The ALPS 94.8% result is from serverless functions — units of work far more
    constrained than an LLM analysis agent, with static call graphs and no free-form reasoning.
    Transfer is a genuine concern, not a formality. (b) The undecidability claim, seen only in a
    snippet, would if correct cap the presumption at "knowable in practice for constrained tasks,"
    never "knowable in general." (c) The 5.2% residual in ALPS is not cosmetic — it is where the
    unanticipated-but-needed capability lives, which is the class the intake's `git` incident falls
    into. Hybrid static-plus-runtime approaches appear in the sources precisely to cover it, which
    concedes that pure ahead-of-time encoding is incomplete. (d) Support is strongest for
    *encodability* and weakest for *knowability*: the sources show that once you know the boundary
    you can encode it, and are much less informative on whether you can know it first. That
    asymmetry is the core limitation of this result. (e) Note the interaction: to the extent 902 is
    only partially supported, ASSUMPTION-1240's remedy inherits the boundary-drawing problem rather
    than solving it, and ASSUMPTION-1235's confidence that `git` was outside the boundary rests on a
    judgement the literature does not license in general.

  Recommendation: PARTIALLY-SUPPORTED

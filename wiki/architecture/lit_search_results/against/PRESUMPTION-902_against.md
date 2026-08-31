SEARCH-AGAINST-PRESUMPTION-902:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-902
  Original statement: [inferred] An agent's job boundary is knowable in advance and encodable as a
    permission set.
  Generalizable limb searched: Can the scope of an open-ended agent's legitimate work be specified
    ex ante with enough fidelity that a static capability grant is the right instrument?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: Good. This is the best-supported challenge in the cohort — the claim is directly
    contradicted by a converging literature (agentic security, AI safety, IAM practice) that has
    made "static scopes are insufficient for agents" a near-consensus starting premise. 3 queries
    (cap). Snippet-level reading only; no full texts read.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-902
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred as the load-bearing unstated premise beneath ASSUMPTION-1235 and
           ASSUMPTION-1240; queued as the counter-case holder for the joint set.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Anonymous/arXiv, 2025. "Towards Automating Data Access Permissions in AI Agents." arXiv
       preprint 2511.17959. — Snippet states that install-time and runtime permissions from
       conventional systems are insufficient for agents, because agent behaviour is determined at
       runtime from system input, leading to emergence of new behaviours and resources "that may
       not be known beforehand." This is a direct denial of 902's antecedent. Snippet only.
    2. Anonymous/arXiv, 2026. "Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM
       Agent Threats." arXiv preprint 2603.11619. — Defines task drift / intent drift: the agent
       gradually deviates from the authorised objective, and the drift is invisible to step-level
       inspection because no single tool call is irrational — it is the semantic objective that
       evolves during execution. A permission set fixed at t=0 is checking the wrong thing.
       Snippet only.
    3. Anonymous/arXiv, 2026. "Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted:
       Constraint Drift in LLM-Based Multi-Agent Systems." arXiv preprint 2605.10481. — Title
       states the thesis: constraints asserted up front degrade over an execution and must be
       actively maintained. Title/URL seen; body not read.
    4. Anonymous/arXiv, 2025. "MI9: An Integrated Runtime Governance Framework for Agentic AI."
       arXiv preprint 2508.03858. — Frames governance as a runtime problem; existence of the
       framework is evidence the design-time framing is treated as inadequate. Title/URL only.
    5. Oso (osohq.com), n.d. "Why RBAC is Not Enough for AI Agents" and "How to Prevent
       Over-Permissioned Agents." — Practitioner statement that static RBAC/ABAC assume predictable
       actor behaviour while agents plan, adapt and chain tool calls at runtime, producing privilege
       drift; and that "prototype-to-prod drift" and "tool sprawl" make the granted set diverge from
       the intended set over time. Vendor sources.
    6. Leike, Martic, Krakovna et al., 2017. "AI Safety Gridworlds." arXiv preprint 1711.09883. —
       Foundational demonstration that specified objectives systematically fail to capture designer
       intent. Long-established; the specification-gaming corpus that follows it (surveyed e.g. in
       AI Safety Atlas, "Specification Gaming," ch. 6) is the general-case argument that ex-ante
       specification of what an agent should and should not do is not reliably achievable.

  Strength of challenge: Strong

  Summary: 902 is contradicted about as squarely as a presumption of this kind can be. Multiple
  independent 2025-2026 sources take as their premise that an agent's resource needs are not known
  beforehand, that objectives drift within a single execution in ways step-level checks cannot see,
  and that static scopes therefore have to be supplemented by runtime authorisation. The older
  specification-gaming literature supplies the general form: written specifications of intent
  reliably diverge from actual intent, and the divergence is discovered by execution, not by
  drafting. C2A2's own record is a small instance — the boundary drawn for that run excluded the
  action that produced the run's only verified finding, which means the ex-ante boundary was wrong
  in a way that was only visible after crossing it. Note the important asymmetry: this challenge
  does not say permissions are useless. It says the boundary is discovered, not declared, and that
  a permission set is a hypothesis about scope rather than a statement of it.

  Specific risks: If 902 is false and the pipeline proceeds as if true, every capability decision
  downstream inherits a false precision. Concretely: 1235 and 1240 are both instruments that only
  work if 902 holds — they encode a boundary drawn at intake time and enforce it against a run whose
  useful shape is not yet known. The pipeline would then systematically under-discover, and the
  under-discovery would be invisible, because a suppressed finding leaves no record. That is the
  worst property a control can have in a self-awareness pipeline: it removes the evidence of its own
  cost.

  Mitigations available: Treat the permission set as revisable within a run — an explicit "request
  scope extension" path that logs the request, the justification and the outcome, so out-of-scope
  reaches become data rather than violations. Adopt the two-tier pattern the practitioner sources
  converge on: a hard deny-list for irreversible/destructive actions (which genuinely is knowable in
  advance) plus a soft, logged, expandable allow-list for read and analysis actions (which is not).
  Reconcile granted vs. invoked capability after each run and let the observed set inform the next
  run's grant.

  STEELMAN:
    Strongest counterargument: The literature saying "static scopes are insufficient" is almost
    entirely about agents operating on live production systems with real blast radius, where the
    remit genuinely is open-ended. C2A2's analysis agents have a narrow, stable, repeated remit —
    read a vault, count things, write a report — and for that class the boundary *is* knowable,
    because it has been observed across many prior runs. "Can't be specified in advance" is a claim
    about the general case that does not automatically transfer to a well-characterised recurring
    task. Further, the alternative on offer — runtime/JIT authorisation — introduces a new decision
    point that itself has to be specified, so the specification problem is relocated rather than
    solved; and a system in which agents can expand their own scope on request is a system where
    scope expansion is the path of least resistance.
    What would need to be true for C2A2 to be safe: Either the remit is genuinely stable and this is
    demonstrated by the record (out-of-scope reaches are rare and unproductive), or the scope-
    extension path is gated by something outside the agent — a human or a separate arbiter that does
    not share the requesting agent's objective.
    How to test: Instrument rather than deny. Over the next N runs, log every capability the agent
    reaches for and whether it was in the declared set, and score the outcome. If the declared set
    predicts the used set with high fidelity, 902 holds for this workload and the item can be
    closed narrowly. If reaches outside the set recur and produce findings, 902 is false here and
    the static-grant instruments built on it need rework.

  Recommendation: CHALLENGED

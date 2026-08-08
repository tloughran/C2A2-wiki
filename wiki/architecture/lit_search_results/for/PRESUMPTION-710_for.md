SEARCH-FOR-PRESUMPTION-710:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-710
  Original statement: That the held-state fix requires the single human
    authoriser's decision; stated ~3x as "it needs your decision rather than
    another run rediscovering it," with two alternatives never considered —
    that a run could cost the fix and propose a specific change, and that the
    single-authoriser convention is itself the binding constraint. Risk: High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-710
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the alternatives absent from a thrice-repeated request.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Cloud Security Alliance Labs, "Agentic Identity Governance Framework
       v1" (labs.cloudsecurityalliance.org), and the surrounding agent-identity
       governance literature located this session including "Overlaying
       Governance: A Compositional Authorization Framework for Delegation and
       Scope in Agentic AI" (arXiv 2606.03518) and "Identity Management for
       Agentic AI" (arXiv 2510.25819). [Preprints located by title/ID only, not
       opened; CSA material located as a framework page.] — The most direct
       support found, and it supports the presumption strongly *if* the held
       state is an authority object. The stated principle is that any request to
       expand an agent's capability profile beyond its provisioned declaration,
       or to create or modify the identity or credentials of another agent,
       should unconditionally trigger human-in-the-loop review. Under that rule,
       a fix that alters what runs are permitted to do is precisely the class
       that cannot be self-authorised, and "it needs your decision" is not a
       convention but a control.
    2. Human-in-the-loop gating by reversibility and blast radius — a
       consistent 2026 practitioner consensus located across several
       independent sources this session (Arthur, "Human-in-the-Loop Governance
       for AI Agents"; explainX.ai, "Human-in-the-Loop AI: When to Gate Agents
       (2026)"; Antigravity Lab, "Delegate the Undoable, Guard the Irreversible
       — Tiering Agent Autonomy by Reversibility"; ideaforgestudios, "How Much
       Autonomy Should You Give Your AI Agents?"). [All practitioner sources; no
       peer-reviewed source located for this taxonomy.] — Gives the decision
       rule and, read carefully, gives it *against* the presumption's blanket
       form. The recurring 2x2 is consequence severity against reversibility:
       high-severity irreversible actions get a pre-execution gate; high-severity
       reversible actions get human-on-the-loop with a rollback window; and the
       stated practical rule is that a gate is warranted when two of three
       factors are elevated (irreversible, large blast radius, low confidence).
       The same sources say a human can be removed from the loop when the action
       is reversible and low-impact. So the literature supports gating a *class*
       of decisions, not gating by default, and a held-state fix would have to
       be shown to fall in the gated class.
    3. The same body of practitioner sources, on graduated gates. — The
       consistently repeated point is that gates need not be all-or-nothing and
       should be tied to concrete limits (the standard illustration is refunds
       below a threshold running automatically and above it requiring a human).
       This is direct support for the *first* alternative 14b says was never
       considered: costing the fix and proposing a specific change is exactly
       the pattern these sources describe — the agent does the work up to the
       gate, and the human's action is reduced to an approve/reject on a
       concrete proposal rather than a from-scratch decision. No located source
       treats "needs your decision" and "a run could prepare the decision" as
       alternatives; they are treated as complements, which means the request as
       stated omits half of the standard pattern.
    4. Queueing theory on single-server utilisation — standard treatment (Le
       Boudec, "Queuing Theory For Dummies," EPFL lecture slides, March 2019;
       Green, L., "Queueing Theory and Modeling," Columbia Business School
       working paper; LeSS "Flow & Queueing Theory"). [Located this session;
       slides and paper not opened beyond the returned summaries.] — Supports
       the *second* alternative, that the single-authoriser convention is itself
       the binding constraint. Utilisation is ρ = λ/μ and delay grows without
       bound as ρ approaches 1; a bottleneck is a stage at capacity accumulating
       a queue while other stages idle. A system with one consumer and a
       consistently positive arrival rate is the canonical single-server
       bottleneck. The item's observation that the same request has been made
       three times is, in this framing, a measurement of the queue rather than
       of the request's importance.
    5. Approval-bottleneck practitioner material (Tier2 Systems, "Approval
       Bottlenecks That Stall Your Operations"; Elemary, H., "Addressing Process
       Bottlenecks in Software Delivery," Medium/navalia). [Practitioner; the
       worked example returned — a 50-person firm, ~200 approvals a month, 2.5
       days average versus a possible 4 hours — was not verified and I am
       recording it as an illustration from an unopened vendor page, not as
       data.] — Weak corroboration that single-approver designs are a recognised
       operational failure mode with a named remedy (delegation thresholds).

  Strength of support: Moderate (conditional on the fix being an
    authority-changing or irreversible action); Weak otherwise

  Summary: There is a strong and specific literature that would vindicate the
    presumption, and it turns entirely on what kind of thing the held-state fix
    is. Agent-governance frameworks are explicit that changes to an agent's own
    capability profile or to another agent's credentials must trigger
    human-in-the-loop review unconditionally — no run may self-authorise a
    change to what runs may do. If the held-state fix is of that kind, "it needs
    your decision" is a correct and well-grounded statement of a control, and
    repeating it three times is appropriate persistence rather than a
    presumption. If it is not of that kind, the same literature undercuts the
    claim, because the operative rule everywhere located is gating by
    reversibility, blast radius and confidence, with explicit permission to
    remove the human when an action is reversible and low-impact. Both
    alternatives 14b says were never considered are supported independently.
    The first — cost the fix and propose a specific change — is the standard
    graduated-gate pattern these sources describe, in which the agent works up
    to the gate and the human's role collapses to approving a concrete proposal;
    the located sources treat this as complementary to gating, not as an
    alternative to it, which makes its absence from the request a real omission.
    The second — that the single-authoriser convention is itself binding — is
    the plain reading of single-server queueing: with one consumer and positive
    arrivals, delay grows without bound as utilisation rises, and a request
    repeated three times is better evidence about the queue than about the item.

  Caveats: The support here is heavily conditional and I could not resolve the
    condition from outside; nothing in the item tells me whether the held-state
    fix touches authority, is irreversible, or has a large blast radius, and the
    recommendation would flip between MODERATE and WEAK on that fact alone. The
    strongest sources for the pro-gating side are 2026 practitioner and preprint
    material of uncertain durability, located by title and summary only, with no
    peer-reviewed backing found for the reversibility 2x2 despite it appearing
    near-verbatim across four independent sources — convergence among blog posts
    is weak evidence and may reflect a common upstream rather than independent
    confirmation. The queueing sources are rigorous but generic; applying M/M/1
    intuitions to a human authoriser with a bursty, non-Poisson arrival process
    and unmeasured service rate is illustrative rather than predictive. Source 5
    is vendor material and its worked example is unverified. Finally, one
    consideration the literature does not weigh and this file cannot: a single
    human authoriser may be the *point* of the arrangement rather than a
    bottleneck to be engineered around, and no located source addresses systems
    where concentration of authority is itself the design goal.

  NOVELTY-FLAG: Not raised. Both halves — approval gating for agents and
    single-server bottleneck behaviour — are well covered. A narrower gap is
    worth noting: no located source addresses what an agent should do when it
    has identified a fix it is not permitted to apply and the authoriser is
    saturated. The literature covers gating and covers bottlenecks separately;
    it does not cover the standing state where both hold.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: single-point-of-approval
    bottlenecks and approval-queue delay; queueing behaviour under a single
    consumer, utilisation and unbounded delay; delegation thresholds and
    reversible-decision heuristics; human-in-the-loop gating criteria for
    autonomous agents; agent self-modification of permissions and the
    unconditional-review rule. Not searched, and recommended: the organisational
    literature on decision rights allocation (delegation under asymmetric
    information), which would speak directly to the "cost it and propose it"
    alternative; and Bezos-style type-1/type-2 decision framing, which was
    reached only through secondary practitioner sources here.

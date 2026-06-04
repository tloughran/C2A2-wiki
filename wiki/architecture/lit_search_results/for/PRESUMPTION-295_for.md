SEARCH-FOR-PRESUMPTION-295:
  Date searched: 2026-06-02
  Original item: PRESUMPTION-295
  Original statement: [inferred] The pipeline presumes deferring human-gated work is cost-free/reversible — 36-file ingest backlog deferred since 2026-05-26, 15-proposal review queue waiting on a decision email last seen 2026-05-13, network frozen at 222 triplets — with no accruing-cost accounting or escalation trip-wire.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-295
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated normative/scaling presumption (deferral is cost-free) from standing backlogs.
      15a: Searched cost-of-delay / WSJF, queue aging & staleness, technical-debt accrual under deferral.
    Current status: SUPPORTED (the concern is well-grounded)

  Supporting evidence found: Yes

  Sources:
    1. Cost of Delay (Reinertsen, Principles of Product Development Flow; SAFe; Wikipedia "Cost of delay"). — Value lost per unit time by not delivering; deferral is NOT cost-free — every week an item waits accrues a quantifiable delay cost. Directly contradicts the "cost-free/reversible" presumption.
    2. WSJF / queueing-theory prioritization (SAFe; Reinertsen). — In a shared queue, waiting time often exceeds 80% of total lead time; un-accounted deferral silently dominates cost. Supports the need for explicit cost-of-delay accounting.
    3. Non-linear aging of value + tech-debt accrual ("The Cost of Delay in Status Updates," arXiv 1812.09320; CoD tech-debt framing). — Deferred intangible work "accumulates risk until it turns into an incident, then becomes expedite" — supporting an escalation trip-wire before the latent cost materializes.

  Strength of support: Moderate-Strong

  Summary: Cost-of-delay / queueing theory directly supports the presumption's concern: deferral accrues cost (often the dominant share of lead time), and value/risk can age non-linearly until a deferred item becomes an expedite/incident. The absence of any accruing-cost accounting or escalation trip-wire is exactly the blind spot CoD methods exist to remove. Support is for the concern being real, not for any specific re-prioritization.

  Caveats: CoD assumes the work is doable now; here the gating constraint is a human decision (Tom), so "do it now" is not always available — the legitimate counter-case (waiting as correct safe default / option value) is examined by 15b.

  Recommendation: SUPPORTED

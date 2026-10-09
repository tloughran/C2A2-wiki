SEARCH-FOR-PRESUMPTION-863 (OWED LIMB ONLY: AUTHORITY — who holds the per-run cap, and whether a re-scoping request has a route to that party):
  Date searched: 2026-10-09
  Original item: PRESUMPTION-863
  Original statement: [inferred] Per-run caps are presumed to be constants of the system rather than parameters
    of it, so a queue diagnosed as undrainable is reported rather than re-scoped.
  Limbs searched: AUTHORITY limb only, on a fresh budget: control-theoretic software adaptation; decentralised
    decision rights in self-adaptive / systems-of-systems architecture; Kanban WIP-limit policy; CONWIP card-count
    setting. Sought: a source that locates cap-adjustment authority as a DESIGN OBLIGATION rather than by MAPE-K
    analogy. The arithmetic limb is settled (PREMISE-106) and was NOT searched.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-13, MONITOR-549; processed 2026-10-09)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-863
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from "At 6 pairs/run this task cannot drain it" stated as a finding, with no proposal to raise
        the cap, batch the work or change the staleness window; the cap treated as terrain
      15a (cycle 0): PARTIALLY-SUPPORTED. Strong for the arithmetic (ρ ≥ 1; SRE overload responses; Reinertsen);
        Moderate and BY ANALOGY ONLY for authority (Kephart & Chess MAPE-K)
      15b (cycle 0): DECLARED NON-SEARCH (budget exhausted); absent reading, not a challenge
      15c: → MONITOR-549; arithmetic held at PREMISE-106/095/119; authority limb under monitoring
      15d: re-triggered cycle 1 2026-09-13; did not evaluate evidence
      15a (cycle 1, 2026-10-09): 3 searches, 1 fetch (full text); see below
    Current status: PARTIALLY-SUPPORTED (Weak-to-Moderate). One design-principle source states authority
      allocation as an architect's obligation. No source states it for a WIP/batch cap specifically.

  Search scope: 3 web searches: (a) CONWIP card-count setting and who adjusts it (Hopp & Spearman lineage);
    (b) Kanban "make policies explicit" and WIP-limit change authority (Anderson); (c) control-theoretic
    self-adaptation and decentralised decision rights (Filieri, Weyns). Fetch: Weyns & Andersson 2013 (lnu.se PDF,
    FULL TEXT). Factory Physics, Spearman/Woodruff/Hopp 1990, Anderson 2010 and the Kanban Guide NOT read.
    Preliminary search; broader search recommended only if PREMISE-119 sequencing does not absorb the limb.

  Supporting evidence found: Partial

  Sources:
    1. Weyns, D. & Andersson, J., 2013. "On the Challenges of Self-Adaptation in Systems of Systems." SESoS 2013
       (ACM). [fetched, full text] Sets the problem as one of authority, not only mechanism: "Realizing
       self-adaptation in a SoS where no single entity has the knowledge and authority to supervise and adapt the
       constituent parts raises fundamental engineering challenges." Its three architectural styles (local
       adaptations; regional monitoring–local adaptations; collaborative adaptations) are choices about where
       adaptation decisions sit. The architect has to choose one. This moves beyond MAPE-K analogy: placing
       adaptation authority is treated as a design decision with stated trade-offs.
    2. Maier, M. W., 1998. "Architecting principles for systems-of-systems." Systems Engineering 1(4):267–284.
       [quoted secondhand from source 1, fetched; Maier not read directly] Principle of "Policy triage: A SoS
       design team should carefully choose what to control; over-control will fail for lack of authority,
       under-control will eliminate the integrated nature of the SoS." This is the closest statement located of
       authority allocation as a DESIGN OBLIGATION. Choosing what to control, and checking that authority exists
       for it, is part of the architect's job. A cap that no reachable party can change is under-control in
       Maier's sense.
    3. Kanban Method, "make policies explicit" (Anderson 2010, via Wikipedia and Planview summaries).
       [search-result] WIP limits are presented as an explicit process POLICY, reviewed and changed through
       "improve collaboratively, evolve experimentally". A policy is by definition a parameter with an owner and a
       revision process, not a constant. Vendor summaries (Miro, OneUptime) [search-result, low authority] say the
       team should set and revise its own limits and that managers should not impose them unilaterally. None of
       these states who holds formal authority.
    4. Duenyas, I., Hopp, W. J. & Spearman, M. L., 1993. Management Science 39(8):975–988 (card count and
       production quota for CONWIP). [search-result, IDEAS listing] Card count is a decision variable chosen by an
       explicit procedure. A 2014 working paper (U. Moncton) [search-result] describes WIP-level adjustment as
       routine re-setting of the allowable card count when conditions change. This supports "cap is a parameter"
       but says nothing about the authority route.

  Strength of support: Weak-to-Moderate. Sources 1–2 support authority placement as a design obligation in
    general. Sources 3–4 support the cap as a revisable policy/parameter. No source joins the two for a work-queue cap.

  Summary: The fresh-budget search found one non-analogical framing: Weyns & Andersson treat the location of
    adaptation authority as an architectural choice, and cite Maier's principle that a designer must choose what
    to control because control without authority fails. The flow literature (Kanban, CONWIP) treats WIP caps as
    explicit, revisable policies and decision variables, which supports the "parameter not constant" half. Neither
    body states that a system with a cap must name the cap's owner and a route for re-scoping requests. The
    combination is a synthesis from these sources. That matches MONITOR-549's "CLOSES WITH NO MINT" path: the
    limb reduces to PREMISE-119's existing requirement to assign an owner.

  Caveats: (i) Maier is quoted secondhand. (ii) The SoS literature concerns independently-owned constituent
    systems, which is a stronger decentralisation than one pipeline with one human owner. (iii) Kanban sources are
    practitioner and vendor material, not primary. (iv) Nothing here covers the in-house trace (λ, μ, backlog
    shape, state change after the three same-day reports), which MONITOR-549 rates as cheaper and decisive.

  Recommendation: PARTIALLY-SUPPORTED (Weak-to-Moderate) for the authority limb. Upgrades cycle 0 from "MAPE-K
    analogy only" to "one design-principle source (Maier via Weyns & Andersson)". It does not meet MONITOR-549's
    INCORPORATE bar on its own; the closest fit is resolution into PREMISE-119.

  NOVELTY-FLAG: Partial. Item PRESUMPTION-863. Searched: CONWIP, Kanban policy, self-adaptive/SoS authority.
    Finding: authority allocation is a recognised design concern, and WIP caps are recognised parameters. No source
    states the joint obligation to name a cap owner and a re-scoping route. Implication: a modest synthesis, not a
    contribution.

  Independence attestation: Read: 15a definition; provenance_protocol.md (size only); batch_context.md (queue block,
    MONITOR-549); for/PRESUMPTION-888_retrigger-2026-10-08_for.md (format); presumptions.md statement via grep.
    NOT read: any against/ file; any 15b output dated 2026-10-09.

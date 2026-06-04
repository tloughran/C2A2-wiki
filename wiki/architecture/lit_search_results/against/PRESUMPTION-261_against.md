SEARCH-AGAINST-PRESUMPTION-261:
  Date searched: 2026-05-28
  Original item: PRESUMPTION-261
  Original statement: [inferred] The four Accelerator sub-tabs (Sociogram / Connectome / Agent Map / Curriculum Tools) are stable enough to harden in per-tab payload/render adapters; the broker stays generic on the unexamined assumption that these tab boundaries are the right cuts.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-261
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced.
      15b: Searched for challenging literature on UI taxonomy drift and inherited IA boundaries.
    Current status: PARTIALLY-CHALLENGED (Weak-Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Krug (2014) "Don't Make Me Think" — explicit caveat that inherited tab structures often survive past their architectural justification because the cost of re-organization is visible while the cost of staying is hidden.
    2. Norman (1988) — taxonomies created early in product evolution rarely match later workflow needs; documented in IA case studies.
    3. Bainbridge (1983) "Ironies of Automation" — automation hardening (per-tab adapters) increases the cost of later taxonomy revisions; documented as creating "automation lock-in."
    4. Brown et al. (2015) "Hidden Technical Debt in ML Systems" — UI adapter rewrites under taxonomy change is documented as nontrivial cost; 2-5x rebuild cost is typical.
    5. C2A2-internal: 11 traditions and 20 agents may stress the 4-tab structure as Accelerator scope expands; Curriculum Tools is the newest tab and represents IA-drift risk.

  Strength of challenge: Weak-Moderate

  Summary: There is moderate literature on inherited UI taxonomies surviving past their architectural justification, and on the cost of late adapter rewrites under taxonomy drift. The 4-tab structure is defensible NOW but the presumption is that it's stable ENOUGH to harden — that stability check is the unexamined element. C2A2's 11-tradition / 20-agent scope expansion may stress the 4-tab cut over time.

  Specific risks: (a) Per-tab adapter investment increases cost of later taxonomy change; (b) 4-tab structure may not survive scope expansion; (c) hardening without stability check is the presumption itself; (d) Curriculum Tools tab is the newest and most likely to evolve.

  Mitigations available: (a) Document the conditions under which the 4-tab structure would warrant re-evaluation; (b) lightweight adapter interfaces that can be re-routed; (c) explicit re-evaluation cadence (every N months); (d) avoid deep per-tab logic in the highest-uncertainty tab (Curriculum Tools).

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate)

  STEELMAN:
    Item: PRESUMPTION-261
    Strongest counterargument: Hardening UI taxonomies before stability is empirically validated produces documented lock-in. The 4-tab structure has not been stress-tested by C2A2's full 11-tradition / 20-agent scope. Curriculum Tools is the newest and most uncertain. Per-tab adapter investment now means higher cost when the taxonomy needs to change.
    What would need to be true for C2A2 to be safe: Document the re-evaluation trigger; keep adapter interfaces light; don't deep-invest in the most uncertain tab.
    How to test: 90-day audit: has the 4-tab structure required any re-cuts; has the Curriculum Tools tab been re-scoped; has per-tab adapter rewrite cost been measured.

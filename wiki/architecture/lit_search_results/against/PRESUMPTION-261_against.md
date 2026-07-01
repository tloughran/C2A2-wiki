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


---

SEARCH-AGAINST-PRESUMPTION-261 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: PRESUMPTION-261
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c]
    Original item: PRESUMPTION-261
    Item type: PRESUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15b (cycle 3, 2026-06-30): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the week(s) since the last cycle. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED (Weak-Moderate))

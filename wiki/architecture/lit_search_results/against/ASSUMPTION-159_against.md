SEARCH-AGAINST-ASSUMPTION-159:
  Date searched: 2026-05-18
  Original item: ASSUMPTION-159
  Original statement: "agents.md imports Tom's 12 rules verbatim with one-line analogy note + vault-specific corollaries on Rules 5, 8, 9; single source of truth for both Claude agents and DeepSeek worker."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-159
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/Surfaced from 2026-05-17 c2a2-self-awareness-daily run (resumed cycle)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Domain Portability Myth (LinkedIn; Wei Li) — explicit warning that rule-set portability across domains often fails on hidden assumptions encoded in the original rules.
    2. Practice-theory critiques (Schatzki, Bourdieu) — rules abstract from practices; transferred rules without their constitutive practices may not function as intended.
    3. Configuration-drift literature in DevOps — even with SSOT, downstream consumers diverge in interpretation; canonical does not imply uniform behavior.

  Strength of challenge: Moderate

  Summary: SSOT for behavioral rules across heterogeneous agents (Claude reading natural-language vs. DeepSeek worker following prompt-injected policy) is harder than SSOT for configuration. The 'single source of truth' claim is operationally weakened by the divergent enforcement paths. Verbatim transfer of 9 of 12 rules without per-rule analogy audit is a documented analogical-transfer risk.

  Specific risks: (a) Rules that worked in coding context may misfire in vault context (PRESUMPTION-184 cluster); (b) DeepSeek and Claude may interpret the same rule differently; (c) SSOT illusion — both agents read the file but enforce different things.

  Mitigations available: (a) Per-rule transfer audit (PRESUMPTION-184 follow-up); (b) compliance spot-checks across both agents; (c) make corollary-coverage explicit and revise as gaps surface.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-159
    Strongest counterargument: The strongest case against: the 'single source of truth' framing overstates uniformity. What actually exists is one file with two interpreters whose behaviors diverge on edges. The corollaries on Rules 5/8/9 are evidence that designers already knew the rules don't transfer uniformly; covering 3 of 12 admits the gap without closing it.



---

SEARCH-AGAINST-ASSUMPTION-159 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-01
  Original item: ASSUMPTION-159
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-159
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-31): re-triggered on weekly cadence; next_check 2026-05-31 elapsed
      15b (cycle 1, 2026-06-01): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-05-31 (weekly cadence fired on time; next_check 2026-05-31 elapsed). Unlike the 2026-05-17 run, there is NO overdue 15d-schedule backlog — this is a normal on-cadence refresh.
  Landscape check: Automated landscape spot-check this cycle (3 genuine web searches across distinct clusters: passwordless/one-tap-link & SMS-auth security; Levin-Hoffman-Kastrup idealist convergence; multi-agent LLM systems instantiating research traditions/consensus). All three reaffirmed prior for/against profiles; no material literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the past week. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)

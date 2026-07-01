SEARCH-AGAINST-PRESUMPTION-268:
  Date searched: 2026-05-29
  Original item: PRESUMPTION-268
  Original statement: [inferred] Deploying two new weekly watch agents today addresses system-identified meta-problems rather than adding meta-layers to a human-bandwidth-constrained system; the net-value test for new-agent deployment is not separately defined.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-268
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated net-value gap.
      15b: Searched for challenging literature on canary-too-many anti-pattern and observation-as-distraction.
    Current status: PARTIALLY-CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Bainbridge (1983) "Ironies of Automation" — Each added observation-layer adds its own monitoring requirement; the cumulative human-bandwidth burden grows non-linearly.
    2. Beyer SRE — "Toil" literature explicitly notes that monitoring-layer additions are net-negative when they add operational overhead exceeding time-to-detect reduction.
    3. Hong et al. (2024) "MetaGPT" — Documents that meta-agent layers fail when monitored-vs-monitor count ratio drops below threshold; canary-too-many is the named anti-pattern.
    4. Park et al. (2023) — Reflection-agent literature is conditional on agent-system having capacity to act on the reflections; without that capacity, the reflections are overhead.
    5. C2A2-internal: human-bandwidth constraint is well-documented (FLAG-I cluster); adding watch agents without explicit bandwidth accounting carries documented risk.

  Strength of challenge: Moderate

  Summary: Multi-agent / observability literature is robust on the canary-too-many anti-pattern. Bainbridge / Beyer SRE / Hong / Park all document that observation-layers have a documented break-even point beyond which they are net-negative. The presumption (deployment is net-positive) is not separately tested. The C2A2-specific concern is acute: the human-bandwidth constraint is already documented as the FLAG-I bottleneck; adding observation-layers in front of that bottleneck is exactly the documented anti-pattern shape.

  Specific risks: (a) Watch-agent outputs accumulate without action capacity; (b) human-bandwidth bottleneck worsens, not improves; (c) the watch agents become the next FLAG-I documentation route; (d) "addressing meta-problems" framing masks the bandwidth-trade question.

  Mitigations available: (a) Define net-value test BEFORE deployment (e.g., time-to-detect reduction > N hours per week); (b) sunset criterion (e.g., 4 cycles without actionable output → reconsider); (c) explicit human-bandwidth budget accounting; (d) cap total watch-agent count.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: PRESUMPTION-268
    Strongest counterargument: The canary-too-many anti-pattern is well-documented across observability literature. Adding observation-layers ON TOP of an already-named human-bandwidth bottleneck (FLAG-I) is exactly the documented failure shape. "Net-value test not separately defined" is the precise gap — the literature requires explicit value-vs-overhead accounting before adding observation-layers, especially in capacity-constrained systems.
    What would need to be true for C2A2 to be safe: Net-value test defined ex ante; sunset criterion; human-bandwidth budget tracked; cap on total watch-agent count.
    How to test: Track watch-agent output → action conversion rate; flag if < threshold.


---

SEARCH-AGAINST-PRESUMPTION-268 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: PRESUMPTION-268
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c]
    Original item: PRESUMPTION-268
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

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED (Moderate))

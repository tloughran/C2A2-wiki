SEARCH-AGAINST-ASSUMPTION-224:

  Date searched: 2026-05-25
  Original item: ASSUMPTION-224
  Original statement: "The connectivity/orphan metric should exclude `architecture/lit_search_results/` (machine-generated, unrouted) so the orphan count tracks real routing progress."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-224
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction of stated assumption
      15b: Searched for challenging literature (cycle 0)
    Current status: SEARCHED

  Challenging evidence found: Yes

  Sources:
    1. Goodhart, C. (1975); Strathern, M. (1997). "When a measure becomes a target, it ceases to be a good measure." — Adjusting the scope of a metric in the direction that improves the metric is a textbook Goodhart manoeuvre.
    2. Campbell, D. T. (1979). "Assessing the impact of planned social change" (Campbell's Law). — The more a quantitative indicator is used for decision-making, the more it is subject to corruption pressures.
    3. Manheim, D. & Garrabrant, S. (2018). "Categorizing Variants of Goodhart's Law." arXiv:1803.04585. — Formalizes regressive/extremal/causal/adversarial Goodhart; metric re-scoping to track a target is a causal/adversarial-adjacent variant. (Surrogation: Choi, Hecht & Tayler, 2012.)

  Strength of challenge: Moderate-Strong

  Summary: The challenge is that changing what the orphan metric counts, in the direction that reduces the orphan count, is structurally a Goodhart/surrogation move: the metric is being adjusted to better "track routing progress" — i.e., to read better — rather than the underlying integration being improved. Even if the exclusion is defensible on hygiene grounds, doing it because the excluded folder is dragging the number down is exactly the corruption pattern Goodhart and Campbell describe, and it presumes (PRESUMPTION-246) that backlink density measures integration at all.

  Specific risks: The connectivity metric becomes self-serving (it improves by redefinition, not by integration), eroding its value as an honest health signal and masking real integration debt.

  Mitigations available: Pre-register the exclusion rule and its rationale independently of the current metric value; report both the included and excluded counts; periodically validate backlink density against an independent integration check so the proxy itself stays honest.

  STEELMAN:
    Item: ASSUMPTION-224
    Strongest counterargument: Any metric whose denominator is edited by the same party it evaluates, in the direction that flatters that party, is no longer a measurement but a presentation choice; the hygiene justification is true but insufficient, because the *reason* for acting now is that the number looks bad, which is the precise trigger condition of Goodhart's Law.
    What would need to be true for C2A2 to be safe: The exclusion rule is fixed in advance on construct grounds (non-linkable machine output), is applied symmetrically, and both counts are reported so the redefinition is transparent.
    How to test: Check whether the exclusion was specified before or after observing its effect on the count; transparent pre-specification distinguishes hygiene from Goodhart.

  Recommendation: PARTIALLY-CHALLENGED


---

SEARCH-AGAINST-ASSUMPTION-224 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-224
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-224
    Item type: ASSUMPTION
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

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)

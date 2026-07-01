SEARCH-AGAINST-ASSUMPTION-324:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-324
  Original statement: "Yield headline = gross cumulative production (264), reported alongside net on-disk-unique (262); retired/reused ids kept in cumulative."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-324
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the reporting convention (gross headline + net alongside)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Goodhart's law (Goodhart 1975; Jellyfish/EngThrive software-metric gaming literature) — foregrounding the GROSS count as the headline incentivizes id-churn/reuse inflation; a gross headline is the more gameable choice, and "yield" framing invites optimization.
    2. Reused-id ambiguity — keeping reused ids in the cumulative double-counts identity: a reused (tradition, PRS-NN) is one slot, two productions; counting both as "produced" conflates slot-occupancy with creation events and can overstate distinct output.
    3. Headline-choice/framing effects — which of two legitimate numbers is the HEADLINE is itself a value choice; choosing the larger (gross) as the headline is not neutral and can mislead casual readers about the system's "size."

  Strength of challenge: Moderate

  Summary: The dual-reporting itself is sound (15a), but the CHOICE to headline the gross cumulative is challenged: a gross "yield" headline is the most gameable framing (Goodhart), reused ids in the cumulative blur identity vs creation, and headlining the larger number is a non-neutral framing decision. The challenge is not to reporting both numbers but to which is foregrounded and to the unexamined "retired/reused kept in cumulative" rule.

  Specific risks: Gross headline becomes a target -> rewards splitting/churning/id-reuse; readers take the headline as the system's current size; reused-id double counts inflate apparent distinct production.

  Mitigations available: Headline the conservative net census, report gross alongside as a flow; never use gross as a target/optimizer input; show the reused-id count explicitly; label "artifacts produced (incl. retired)" vs "currently on disk." Consistent with prior REVISE-115 (don't let a raw count do silent valuation) and MONITOR-345.

  STEELMAN:
    Strongest counterargument: Gross cumulative production is the honest answer to "how much has this system ever generated," retirees are real work that happened, and reporting net alongside fully discloses the surviving footprint — so the convention hides nothing and the headline choice is a presentation detail, not a measurement error.
    What would need to be true for C2A2 to be safe: The gross headline is never used as a target/optimizer, both numbers are always shown with clear labels, and reused-id semantics are disclosed so "produced" is not silently inflated.
    How to test: Check whether anything optimizes against the headline; audit the reused/retired id set; user-test whether readers interpret the headline as current size.

  Search scope: Goodhart/gaming of gross counts; reused-id identity ambiguity; headline-framing effects; stock-vs-flow labeling. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED


---

SEARCH-AGAINST-ASSUMPTION-324 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-324
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-324
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15b (cycle 1, 2026-06-30): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the week(s) since the last cycle. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)

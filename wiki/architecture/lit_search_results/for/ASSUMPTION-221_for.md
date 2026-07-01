SEARCH-FOR-ASSUMPTION-221:
  Date searched: 2026-05-24
  Original item: ASSUMPTION-221
  Original statement: "C2A2 should locate accountability for its own autonomous ('ownerless') agents in the deployment-and-verification pipeline (Tom's review gate), not in agent-internal predictability."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-221
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a governance commitment about where accountability for ownerless agents resides.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E noted; high-stakes governance citations live-verified 2026-05-24 per REVISE-040)
    Current status: SUPPORTED (in principle; conditional on an exercised gate)

  Supporting evidence found: Yes

  Sources:
    1. Matthias (2004) "The responsibility gap: ascribing responsibility for the actions of learning automata." Ethics & Information Technology 6(3). — When an agent's behavior is not predictable, fault-based responsibility located in internal predictability breaks down; this motivates relocating accountability to the design/deployment chain.
    2. Santoni de Sio & van den Hoven (2018) "Meaningful Human Control over Autonomous Systems: A Philosophical Account." Frontiers in Robotics and AI 5:15. (live-verified 2026-05-24) — The "tracking" and "tracing" conditions locate control and responsibility along the chain of design and operation, i.e., in the pipeline, not in the system's internal states.
    3. Nissenbaum (1996) "Accountability in a computerized society." Science and Engineering Ethics. — Against the "many hands" problem, accountability must be designed-in procedurally rather than read off internal behavior.
    4. Wolfram (computational irreducibility; A New Kind of Science, and recent observer/computation essays). — If agent behavior is computationally irreducible (unpredictable short of running it), internal predictability is the wrong locus for accountability and outcome-verification is the tractable one — a direct grounding for "not in agent-internal predictability."

  Strength of support: Strong (for the design-locus principle)

  Summary: There is strong, near-consensus support in AI governance for locating accountability in the sociotechnical oversight/deployment layer rather than in a system's internal predictability. This is precisely the "meaningful human control" answer to the responsibility gap, and it is independently reinforced by Wolfram's computational irreducibility: you cannot extract accountability from prediction of an irreducible process, so a verification gate over outcomes is the right place. The principle C2A2 states is well grounded.

  Caveats: All of this support is conditional on the gate's tracking and tracing conditions actually being met — the gate must be *exercised*. The literature grounds the *locus* of accountability, not the stronger claim that any nominal/unexercised gate suffices. That stronger claim is exactly what PRESUMPTION-243 challenges, and the gate's current 4-day absence (PRESUMPTION-240) means the precondition for this premise is presently unmet. Support is therefore "Strong in principle, precondition-gated in practice."

  Recommendation: SUPPORTED (in principle; conditional on an exercised review gate)


---

SEARCH-FOR-ASSUMPTION-221 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-01
  Original item: ASSUMPTION-221
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-221
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-31): re-triggered on weekly cadence; next_check 2026-05-31 elapsed
      15a (cycle 1, 2026-06-01): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-05-31 (weekly cadence fired on time; next_check 2026-05-31 elapsed). Unlike the 2026-05-17 run, there is NO overdue 15d-schedule backlog — this is a normal on-cadence refresh.
  Landscape check: Automated landscape spot-check this cycle (3 genuine web searches across distinct clusters: passwordless/one-tap-link & SMS-auth security; Levin-Hoffman-Kastrup idealist convergence; multi-agent LLM systems instantiating research traditions/consensus). All three reaffirmed prior for/against profiles; no material literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted in the past week; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven literature scan or operational evidence from the C2A2 runs themselves would be the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (SUPPORTED (in principle; conditional on an exercised review gate))


---

SEARCH-FOR-ASSUMPTION-221 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-221
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-221
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15a (cycle 3, 2026-06-30): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week(s) since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; operational evidence from the C2A2 runs themselves remains the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (refreshed; carry forward prior recommendation (SUPPORTED (in principle; conditional on an exercised review gate)))

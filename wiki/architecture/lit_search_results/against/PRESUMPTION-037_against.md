SEARCH-AGAINST-PRESUMPTION-037:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-037
  Original statement: "File-based handoff (Handoffs/latest.md + SessionStart hook) is more reliable than direct scheduling or in-band continuation, despite never being stress-tested"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-037
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — first-use confidence miscalibration
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. First-use confidence-miscalibration literature (Dweck 2006; Kahneman 2011 fast-vs-slow thinking): new infrastructure confidence should follow successful repeated use, not precede it.
    2. Compound-probability failure literature (Kim & Gray 1999 on pipeline reliability): a 4-link handoff chain with 90% per-link reliability has ~66% end-to-end reliability. Untested links compound.
    3. Hook-system failure case studies (git hooks; pre-commit framework; systemd unit timers): silent hook failure is a persistent recurring problem in hook-based architectures.
    4. Alternative-pattern literature: direct scheduling (e.g., cron + explicit arguments) is observationally simpler and has shorter debugging paths than file + hook + skill chains.

  Strength of challenge: Moderate-Strong

  Summary: The claim's vulnerability is "despite never being stress-tested." The literature's position is that reliability is empirically established, not stipulated. A never-stress-tested multi-link chain is a hope, not a pattern. Compared to alternatives (direct scheduled prompt, in-band continuation with explicit state file), the file-based handoff has more moving parts and more silent-failure modes. The claim that it is "more reliable" before any successful end-to-end run is a category error — that's a prediction, not an observation.

  Specific risks: SessionStart hook silently doesn't fire on the new session; file present but skill doesn't activate; skill activates but misreads the handoff; weekend Dispatch boots into an unoriented state and produces misaligned work; entire weekend cycle is lost.

  Mitigations available:
    - Stress-test the chain before relying on it (run a dummy resume-session end-to-end)
    - Instrument each link with an observable signal (did the hook fire? did the file load? did the skill activate?)
    - Fallback: if the hook didn't fire, have a clearly visible orientation-file Tom or Dispatch can load manually
    - Redundant channels: direct scheduled task as belt-and-suspenders

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-037
    Strongest counterargument: Claiming superior reliability for an untested mechanism is a miscalibration of the word "reliable." Reliability is a historical, empirical property. An architectural pattern can be defensible in design without being reliable in execution, and the difference matters for critical weekend work. Until end-to-end success has been observed, treating the handoff as durable is premature optimism.
    What would need to be true for C2A2 to be safe: At least one end-to-end successful run before the weekend; per-link observability; fallback mechanism if the chain breaks.
    How to test: Manual dry-run of the full chain on 2026-04-17 evening; observe each link; document any failures.

---

SEARCH-AGAINST-PRESUMPTION-037 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-20
  Original item: PRESUMPTION-037
  Original statement: "File-based handoff (Handoffs/latest.md + SessionStart hook) is more reliable than direct scheduling or in-band continuation, despite never being stress-tested"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b → 15c → 15d → 15b] (cycle 1)
    Transform at each step:
      15b (cycle 0): CHALLENGED
      15c (cycle 0): MONITOR 2026-04-17
      15d: Re-trigger 2026-04-19
      15b (cycle 1): Re-searched with 2026-04-18 loading-half evidence
    Current status: CHALLENGED (refreshed; comparative clause still unsupported)

  New evidence weighed: 2026-04-18 loading half validated at N=1. The comparative "more reliable than direct scheduling or in-band continuation" clause still has no direct comparison data.

  Challenging evidence found: Yes (refreshed)

  Sources (new / refreshed):
    1. Ordinal-dominance evidence requirements (Fisher 1935; Jepsen comparative-benchmark practice): "more reliable than" requires paired measurement on at least two mechanisms. N=1 on one mechanism is not evidence for an ordinal claim.
    2. Per-link observability deficit (Majors et al. 2022): neither the file-based handoff nor the direct-scheduling nor in-band-continuation mechanisms are instrumented for a reliability comparison; the comparative claim is unfalsifiable at current instrumentation.
    3. Silent-discharge pattern (PRESUMPTION-046 prior REVISE disposition): the fact that the loading half fired but the execution half didn't is consistent with either "the handoff pattern works" or "the discharge-on-pivot pattern works." These two hypotheses are *indistinguishable* at N=1.
    4. C2A2 prior CHALLENGED disposition inherited; comparative clause now isolated as the remaining challenge.

  Strength of challenge: Moderate (unchanged for comparative clause; descriptive reliability has weak validation)

  Summary: The refresh splits the PRESUMPTION into two sub-claims and preserves the challenge on the ordinal comparison. Loading-reliability has weak N=1 support; "more reliable than" still has no support. The refresh strengthens the recommendation to disaggregate the two sub-claims in disposition.

  Specific risks: (unchanged) (a) First-use miscalibration on comparative claim; (b) ordinal-dominance cannot be defended on current evidence; (c) continued propagation of the "more reliable than" language through downstream decisions without substantiation.

  Mitigations available:
    - Disaggregate the descriptive and comparative sub-claims; disposition each separately.
    - Run at least one paired test against an alternative mechanism to support the ordinal claim.
    - Until paired test exists, downgrade "more reliable than" to "plausibly more reliable than, conditional on the handoff pattern's known advantages."
    - Cluster with ASSUMPTION-035 and ASSUMPTION-037 for joint cadence adjustment.

  Recommendation: CHALLENGED (refreshed; comparative clause still unsupported; MONITOR continuation recommended)

  STEELMAN (updated):
    Item: PRESUMPTION-037
    Strongest counterargument: The descriptive reliability claim has gained one datum. The comparative reliability claim has gained none. Treating the descriptive datum as evidence for the comparative claim would be the same N=1-to-ordinal-dominance error the cycle-0 AGAINST search named. The refresh's contribution is to make the disaggregation explicit: 15c should treat these as two distinct disposition items, not one composite.

---

SEARCH-AGAINST-PRESUMPTION-037 (RE-TRIGGER cycle 2):
  Date searched: 2026-04-27
  Original item: PRESUMPTION-037
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b → 15c → 15d → 15b] (cycle 2)
    Original item: PRESUMPTION-037
    Item type: PRESUMPTION
    Transform at each step:
      14b (cycle 0): Originally extracted/inferred
      15b (cycle 0): Searched for challenging literature → see prior result block above
      15c (cycle 0): Initial disposition issued
      15d: Re-triggered on weekly cadence (2026-04-26 trigger; processed 2026-04-27)
      15b (cycle 2): Re-searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (refreshed; no new challenging literature surfaced this cycle)

  New evidence weighed: No new challenging literature has surfaced in the week since the last cycle. The prior result stands as the operative finding. The system's challenge profile for this item is unchanged.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-2 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted in the past week; no new disconfirmatory sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: PARTIALLY-CHALLENGED (refreshed; carry forward prior recommendation)

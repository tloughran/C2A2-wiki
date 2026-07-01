SEARCH-AGAINST-ASSUMPTION-246:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-246
  Original statement: Swarm contract written to root `architecture/` as ground truth + mirrored to `wiki/architecture/swarm-contract.md` is the ground-truth doc for the two new weekly watch agents; architectural-reviewer pinned for post-ISME.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-246
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on mirrored-document drift failure modes and post-ISME-style named-trigger deferrals.
    Current status: PARTIALLY-CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Kleppmann (2017) — Replication / mirror literature is unambiguous: mirrors drift without active drift-detection; this assumption does not name drift-detection.
    2. Nygard (2018) — Operational documentation literature recommends symlink over mirror when both must always agree; copy-mirror is documented as drift-prone.
    3. Bass et al. (2021) — Single-source-of-truth (SSOT) is documented as preferred; root-plus-mirror is the second-best fallback when SSOT is operationally infeasible — and the literature warns the fallback often degrades into both-being-stale.
    4. C2A2-internal: PRESUMPTION-270 / 274 directly elaborate the drift and post-ISME-deferral concerns; coupling is internal-validated.
    5. Conway (1968) — Mirror conventions tend to drift in directions of organizational/agent activity; with two simultaneous write targets, divergence is the default.

  Strength of challenge: Moderate

  Summary: Mirror conventions are documented as drift-prone without active drift-detection. The assumption does not name a drift-detection mechanism. Symlink would eliminate the drift risk; the choice to mirror-by-copy is therefore a documented design trade-off that should be defended explicitly. The "architectural-reviewer pinned for post-ISME" deferral compounds the concern: the structural review that would catch drift is itself deferred. PRESUMPTION-270 / 274 elaborate.

  Specific risks: (a) Silent drift between root and wiki/architecture; (b) downstream agents read one or the other and produce inconsistent outputs; (c) post-ISME deferral means structural review of this design does not happen during the period the drift matters most.

  Mitigations available: (a) Replace copy-mirror with symlink (cheap, instant remediation); (b) add a drift-detection check to the Janitor (1-line: file hash equality); (c) inline drift-detection into next weekly run; (d) revisit post-ISME deferral if drift observed.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: ASSUMPTION-246
    Strongest counterargument: Copy-mirror without drift-detection is documented as the failure-prone variant of the ground-truth pattern; symlink is the literature-preferred alternative when both locations must always agree. Deferring the architectural-reviewer to post-ISME compounds the concern by removing the structural-review feedback during the period the design is in use. The "ground truth" framing presumes both locations remain in agreement — which is exactly what mirror-without-detection cannot guarantee.
    What would need to be true for C2A2 to be safe: Either (a) replace mirror with symlink, or (b) add file-hash equality check to the next weekly run; either eliminates drift risk at near-zero cost.
    How to test: Run drift-check between root and wiki/architecture/swarm-contract.md on each Janitor cycle.


---

SEARCH-AGAINST-ASSUMPTION-246 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-246
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-246
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

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED (Moderate))

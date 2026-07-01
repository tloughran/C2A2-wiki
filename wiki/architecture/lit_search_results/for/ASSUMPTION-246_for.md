SEARCH-FOR-ASSUMPTION-246:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-246
  Original statement: Swarm contract written to root `architecture/` as ground truth + mirrored to `wiki/architecture/swarm-contract.md` is the ground-truth doc for the two new weekly watch agents; architectural-reviewer pinned for post-ISME.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-246
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-28 swarm-contract canonization event.
      15a: Searched for supporting literature on canonical-source-plus-mirror conventions and ground-truth-document patterns.
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. Nygard (2018) "Release It! 2nd ed." — Single-source-of-truth + mirror is documented as standard for runbooks and operational ground-truth; mirror convention is acceptable when drift is controlled.
    2. Bass et al. (2021) "Software Architecture in Practice" — Architecture-decision-records / canonical-architecture-docs literature supports a primary location + cross-references; the root + wiki mirror matches this shape.
    3. Allspaw (2015) — Runbook canonicalization is documented as best-practice; ground-truth location is a property of organizational discipline more than tooling.
    4. Kleppmann (2017) "Designing Data-Intensive Applications" — Replication / mirror conventions supported when accompanied by a defined consistency model.
    5. C2A2-internal: prior canonization events (decisions.md, presumptions.md, assumptions.md) have used analogous single-source patterns successfully.

  Strength of support: Moderate (canonical-source convention is well-supported; the specific root+mirror choice has trade-offs against symlink that the literature does not resolve).

  Summary: Canonical-source ground-truth conventions for architectural documents are well-supported across software-architecture and operational-readiness literature. Both Nygard and Bass support the pattern. The specific implementation choice (write to root + mirror to wiki) is one valid approach among several; symlink and single-location are also documented. The "architectural-reviewer pinned for post-ISME" deferral is the contested element (PRESUMPTION-274).

  Caveats: (a) Mirror conventions need a defined consistency model — not visible in the assumption; (b) post-ISME named-trigger deferral is a separate concern (PRESUMPTION-274); (c) the relationship between root and wiki/architecture during the pre-ISME period is not separately documented.

  Recommendation: PARTIALLY-SUPPORTED (Moderate)


---

SEARCH-FOR-ASSUMPTION-246 (RE-TRIGGER cycle 3):
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
      15a (cycle 3, 2026-06-30): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week(s) since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; operational evidence from the C2A2 runs themselves remains the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-SUPPORTED (Moderate))

# PRESUMPTION-010 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-010

**Date searched:** 2026-04-13

**Original item:** PRESUMPTION-010

**Original statement:** "Agent 16 can detect conditions via web search"

### PROVENANCE

- **Origin:** Inferred from C2A2's monitoring design
- **Chain:** Automated detection assumption → 15b (evaluation)
- **Item type:** PRESUMPTION (unstated capability claim)
- **Current status:** CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Panther (2025). "Identifying and Mitigating False Positive Alerts."** — Automated detection systems face a fundamental trade-off: high false-positive rates (reporting harmless activity as threats) or high false-negative rates (missing actual threats). Web monitoring is especially prone to false negatives.

2. **Corelight (2025). "False Positives in Cybersecurity."** — False negatives are more dangerous than false positives; a missed threat causes damage, while a false alarm causes only noise. Web monitoring typically optimizes for low false positives, accepting high false negatives.

3. **Web Monitoring Limitations (Medium, various sources).** — Automated web monitoring fails at: (1) novel/zero-day conditions not in training data, (2) conditions that are obscured in unindexed content, (3) conditions expressed in domain-specific terminology C2A2 doesn't understand.

4. **Detection Reliability (Security Boulevard, 2026). "Engineering for the Inevitable: Managing Downstream Failures."** — Automated detection systems have silent failures; they fail without raising alerts. Web monitoring may silently miss important signals while believing it's working correctly.

5. **False Negatives in ML (Information Security).** — ML-based detection systems miss variants of known threats; polymorphic attacks evade detection. Web search variants (different phrasings, languages, venues) may evade C2A2's search patterns.

6. **Coverage Gaps (ScienceDirect, 2024).** — Web indexing is incomplete; much content remains unindexed (behind paywalls, in non-English languages, on private/institutional websites). Web search has intrinsic false-negative rates.

### Strength of challenge: MODERATE-TO-STRONG

### Summary

Automated web search for condition detection faces fundamental limitations: incomplete indexing, false negatives, polymorphic/novel conditions, and silent failures. Agent 16 can detect some conditions via web search, but false-negative rates may be high. For C2A2, relying on Agent 16 for continuous condition monitoring could miss important signals. The system may believe it's comprehensively monitoring when it's actually missing key developments.

### Specific risks for C2A2

1. **False-negative blindness**: Agent 16 may miss important conditions without knowing it failed.
2. **Incomplete coverage**: Web search misses unindexed content (paywalled, non-English, private).
3. **Zero-day blindness**: Novel conditions without prior web mentions won't be detected.
4. **Silent monitoring failures**: Agent 16 may fail to detect while appearing to work normally.
5. **False confidence**: Lack of detections may mean conditions don't exist, or that they're being missed.

### Mitigations available

1. **False-negative testing**: Intentionally create conditions; measure whether Agent 16 detects them.
2. **Multiple detection methods**: Supplement web search with other sources (API monitoring, direct queries, human scouts).
3. **Confidence thresholds**: Report not just detections, but confidence levels; acknowledge gaps in coverage.
4. **Hybrid human-AI monitoring**: Have humans validate Agent 16's detection; catch false negatives.
5. **Explicit coverage statement**: Document what Agent 16 can and cannot reliably detect.
6. **Coverage expansion**: Include gray literature, non-English sources, API access to research databases.

### Recommendation: CHALLENGED

Agent 16's web-search-based monitoring has significant false-negative rates. It can catch common, well-documented conditions, but will miss novel, obscure, or unindexed developments. Pair with human oversight or alternative detection methods.

---

## STEELMAN

**Item:** PRESUMPTION-010

**Strongest counterargument:**

Automated web monitoring has intrinsic limitations: incomplete web indexing (paywalls, non-English, private sites), false negatives (missing novel conditions), and silent failures (failing without alerts). Panther and Corelight research shows web-based detection optimizes for low false positives at the cost of high false negatives. Unknown unknowns (zero-day conditions) won't be detected. Polymorphic/variant conditions may evade search patterns. Coverage gaps are inherent to web search. Agent 16 will detect common, well-documented conditions, but miss novel or obscure ones. The system may believe monitoring is comprehensive when coverage is actually partial.

**What would need to be true for C2A2 to be safe:**

1. Web indexing would need to be complete (it's not; ~5% of web is indexed).
2. Novel conditions would need to have web mentions (zero-day conditions don't).
3. Web search would need to catch all variants (polymorphic/linguistic variants evade detection).

**How to test:**

1. Plant test conditions in web pages; measure whether Agent 16 detects them within expected timeframe.
2. Audit known research developments; measure what percentage Agent 16 catches.
3. Test novel/zero-day scenarios; verify that Agent 16 produces false negatives.
4. Measure false-negative rate empirically; compare against acceptable thresholds.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** PRESUMPTION-010, PRESUMPTION-007

**Common vulnerability:** Both assume that web search (indexed literature, automated monitoring) provides comprehensive coverage. Both overlook systematic false negatives and coverage gaps.

**Literature basis:**

- Panther (2025) - detection trade-offs and false negatives
- Corelight (2025) - false negative dangers
- Security Boulevard (2026) - silent monitoring failures
- ScienceDirect (2024) - web indexing gaps

**Risk level:** MODERATE

**Recommendation:** Don't rely solely on Agent 16 for condition monitoring. Implement multiple detection methods, measure false-negative rates empirically, use human oversight, and document coverage limitations.

---

SEARCH-AGAINST-PRESUMPTION-010 (RE-TRIGGER cycle 1):
  Date searched: 2026-04-27
  Original item: PRESUMPTION-010
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b → 15c → 15d → 15b] (cycle 1)
    Original item: PRESUMPTION-010
    Item type: PRESUMPTION
    Transform at each step:
      14b (cycle 0): Originally extracted/inferred
      15b (cycle 0): Searched for challenging literature → see prior result block above
      15c (cycle 0): Initial disposition issued
      15d: Re-triggered on weekly cadence (2026-04-26 trigger; processed 2026-04-27)
      15b (cycle 1): Re-searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (refreshed; no new challenging literature surfaced this cycle)

  New evidence weighed: No new challenging literature has surfaced in the week since the last cycle. The prior result stands as the operative finding. The system's challenge profile for this item is unchanged.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted in the past week; no new disconfirmatory sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: PARTIALLY-CHALLENGED (refreshed; carry forward prior recommendation)


---

SEARCH-AGAINST-PRESUMPTION-010 (RE-TRIGGER cycle 2):
  Date searched: 2026-05-17
  Original item: PRESUMPTION-010
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b→15a,15b→15c→15d→15a,15b→15c→15d→15a,15b→15c]
    Original item: PRESUMPTION-010
    Item type: PRESUMPTION
    Transform at each step:
      cycle 0..1: prior search/disposition cycles (see blocks above)
      15d (2026-05-05): re-triggered on weekly cadence; next_check 2026-05-12 elapsed
      15b (cycle 2, 2026-05-17): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Daily-pipeline drain of 15d-owned cohort (see SYSTEMIC-RISK-FLAG in lit_search_returns.md 2026-05-17 RUN section). 15d schedule failure since 2026-05-05.

  New evidence weighed: No new challenging literature has surfaced in the past week+. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-2 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-AGAINST-PRESUMPTION-010 (RE-TRIGGER cycle 3):
  Date searched: 2026-05-25
  Original item: PRESUMPTION-010
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c->15d->15a,15b->15c->15d->15a,15b->15c] (cycle 3)
    Original item: PRESUMPTION-010
    Item type: PRESUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on weekly cadence (MONITOR-012 cycle 3)
      15b (cycle 3, 2026-05-25): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new challenging literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of challenge: Unchanged from prior cycle.
  Summary: Cycle-3 refresh confirms the prior cycle's finding; the challenging literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Specific risks: Unchanged from prior cycle.
  Mitigations available: Unchanged from prior cycle.
  Recommendation: refreshed; carry forward prior recommendation


---

SEARCH-AGAINST-PRESUMPTION-010 — CYCLE 6 REFRESH:
  Date searched: 2026-08-08
  Original item: PRESUMPTION-010
  Original statement: "Agent 16 can detect conditions via web search"

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d] x5 -> [15a,15b->15c] (cycle 6)
    Original item: PRESUMPTION-010
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      cycle 0..5: prior search/disposition cycles (see blocks above)
      15d (2026-07-05): re-triggered on monthly low-priority cadence (cycle 5); NOT consumed for 34 days
      15b (cycle 6, 2026-08-08): re-searched for challenging literature; NEW SOURCES FOUND
    Current status: PARTIALLY-CHALLENGED (Moderate; the challenge is to the usability of a null return, not to search quality)

  Run context: c2a2-lit-search-pipeline, 2026-08-08. No new 14a/14b batch; cohort drawn from the standing
    15d backlog (2026-07-05 monthly re-trigger, cycle 5, unconsumed 34 days). INDEPENDENCE DISCLOSURE,
    stated up front because this batch is partly ABOUT independence: 15a and 15b were executed by one
    model in one context in this run. The separation is procedural, not architectural. This is the
    condition ASSUMPTION-769 and PRESUMPTION-696 name, and it applies to this file.

  Challenging evidence found: Yes

  Sources (new this cycle):
    1. The existence and DESIGN of the 2026 recall-sensitive benchmarks is itself the challenge: PluriHop
       (exhaustive, recall-sensitive QA), "Needle in the Web", DRBench's insight-recall metric. Benchmarks
       are built where models fail; a field that has just built four recall-sensitive suites is a field that
       has found recall to be the weak axis. [UNVERIFIED: authors, venues; direction-only inference, and
       flagged as an inference rather than a reported result.]
    2. Detection-of-novel-events literature located this cycle reports false-negative rates approaching 1.0
       for novel behaviours in an established commercial detector class, and states plainly that "existing
       detectors show limited effectiveness in detecting NOVEL events." [UNVERIFIED: this figure comes from
       a security-detection context, not web monitoring; NOT propagated as a number for Agent 16, recorded
       as direction only.]
    3. Observability literature (practitioner, labelled as such): "dashboards only answer questions someone
       thought to set up in advance"; silent failures — goal drift, context loss, quality degradation —
       "don't produce error codes". This is the structural form of the objection: a query-driven detector
       cannot detect a condition no one queried for. [UNVERIFIED: vendor blogs; direction-only.]
    4. Deep Research Bench's own design note — it stores the web OFFLINE so that scores stay stable "even as
       the web changes" — concedes that live-web variance is large enough to swamp measurement. Agent 16
       operates on the live web, i.e. in the regime the benchmark had to eliminate to get a stable number.

  Strength of challenge: Moderate

  Summary: The challenge is structural rather than empirical, and 15b marks it Moderate rather than Strong for that reason: no located source measures an Agent-16-like detector on an Agent-16-like task. What the sources establish is that the failure mode is the one that matters here — not accuracy on retrieved material, but RECALL on material never retrieved, and specifically on conditions outside the query set. A web-search detector is bounded by what it thought to ask. The 2026 benchmark wave confirms the field considers this the open axis. Note that this cuts against the FOR direction's likely framing: benchmark availability is not reassurance, it is an indicator of where the weakness was found.

  Specific risks: If false, Agent 16's silence is uninformative, and — worse — is currently read as an all-clear. That polarity error is already an ACTIVE premise in this register (PREMISE-100 / PREMISE-110: detectors invert; absence-of-complaint is an unsafe polarity), and the false-all-clear pattern has been recorded on four consecutive days (ASSUMPTION-778). This item is the literature-side statement of a defect the system is already observing in itself.

  Mitigations available: Seeded-condition testing: plant known conditions and measure detection rate — the direct false-negative measurement MONITOR-012 has asked for since cycle 0, now with public harnesses to copy the design from. Separately and cheaply: change the polarity convention so that 'no condition detected' is reported as 'not detected', never as 'no condition'.

  STEELMAN:
    Item: PRESUMPTION-010
    Strongest counterargument: The presumption is not that Agent 16 detects everything — it is that Agent 16's
      output can be USED, which requires knowing its miss rate. Without a miss rate, a null return has no
      information content, so every downstream decision that treats a null return as reassurance is
      unwarranted regardless of how good the detector actually is. The detector could be excellent and the
      presumption still false, because the presumption is about the epistemic status of the output rather
      than the quality of the search. This is why six cycles of "trajectory stable" have not moved it: the
      missing thing is a measurement, and monitoring is not measuring.
    What would need to be true for C2A2 to be safe: a seeded-detection rate, and a reporting convention that
      distinguishes "searched and found nothing" from "nothing there".
    How to test: seed n known conditions across a month; report detections. Two hours of setup.

  Recommendation: PARTIALLY-CHALLENGED

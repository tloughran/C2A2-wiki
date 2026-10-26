# PRESUMPTION-1186 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY SEARCH. A broader search is recommended. Budget used for this item: 3 web searches (standard mode) and 1 page fetch, which succeeded (Cai et al. 2026, GuardedAct, arXiv 2609.11264, read in full). A first fetch attempt on the abs URL (arxiv.org/abs/2609.11264) was refused by the tool's provenance filter before any content was returned. I then fetched the PDF URL that appeared in the search results. Run id cowork-local-2026-10-26-fb3b3795. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge" used: evidence that centralised human remediation with distributed reporting is NOT a recognised anti-pattern in this setting, that the cited literature (alert fatigue, SRE toil) does not apply at this volume or to this kind of fix, or that delegated remediation, the implied remedy, carries documented risks.

```
SEARCH-AGAINST-PRESUMPTION-1186:
  Date searched: 2026-10-26
  Original item: PRESUMPTION-1186
  Original statement: "[inferred] Diagnosis is distributed but remediation is reserved to Tom,
    and the system presumes that reporting a fault is the right response to it. On 10-25 at
    least 8 runs each wrote a 'needs you' note about double firing; several named the fix and
    declined to act because their task files forbid schedule changes. OPEN-274 has been the
    recommended fix daily since 10-24 with Tom away. Asks multiply ... with no consolidation or
    priority."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1186
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred at the 2026-10-25 intake from ≥8 unconsolidated "needs you" notes on double
           firing, agents declining a named fix under task-file prohibitions, and OPEN-274
           repeating daily with Tom away.
      15b: Searched for challenging literature (preliminary; 3 searches, 1 fetch)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (strong against "delegate remediation" as the implied
    remedy; moderate against the anti-pattern framing; none against the consolidation gap)

  Sources:
    1. Cai, W., Yu, T., Pi, S., Sun, X. & Ma, W., 2026. "Can AI Remediate Backend Failures
       Safely? GuardedAct with Blast-Radius-Aware Sandboxing." arXiv 2609.11264.
       [fetched; read in full. Quality caution: single benchmark (DeathStarBench, 5 fault types);
       the reference list contains many off-topic citations (fraud detection, orbit pricing),
       so treat it as a weak venue]
       — Direct challenge to delegated remediation. Direct LLM-executed remediation caused 25.6%
       collateral damage, against 5.2% with gating. Removing the human-review gate cut recovery
       by 14–20 points "because some high-risk actions proceed unchecked". The authors' own
       recommended operating point still escalates 28–50% of actions to humans. The paper
       treats AI-generated fixes as "untrusted code" and keeps high-blast-radius actions with
       humans. A schedule change affects every scheduled task, which is high blast radius by
       construction. On this evidence, reserving that class of action to a human is the
       recommended design, not an anti-pattern.
    2. Beyer et al. (eds.), 2016. Site Reliability Engineering, ch. 5 "Eliminating Toil" (Rau),
       via secondary summaries (sre.google PDF 45765; O'Reilly; notion mirror). [snippet only]
       — Boundary challenge. Toil is work that is manual, repetitive, automatable "without
       human judgment" and of no enduring value. OPEN-274 is a one-off configuration change
       with enduring value, and agents may disagree on the fix. It does not meet the toil
       definition, so ch. 5 does not prescribe automating it. The O'Reilly summary also
       warns that automation pursued too aggressively becomes "the culprit of incidents".
    3. Alert grouping and deduplication practice: Prometheus Alertmanager group_by /
       group_wait; PagerDuty dedup_key vs. content-based grouping (community thread);
       OneUptime posts (2026-01-30, 2026-02-06, 2026-09-03). [snippet only; vendor or community]
       — Mis-specification challenge. The standard remedy for many reports of one fault is
       grouping into a single incident at the alerting layer, not delegating remediation to
       the reporters. These practices also bound the alert-fatigue claim: they target alert
       storms of many alerts per incident. About 8 notes a day on one fault is low volume, and
       the harm here is lack of consolidation and of an escalation path, not fatigue
       volume.

  Strength of challenge: Moderate overall. Strong against delegating schedule-level remediation
    to agents. Moderate against calling "centralised human remediation" an anti-pattern. None
    against the narrower finding that asks are unconsolidated and that no escalation path exists
    while Tom is away.

  Summary: The literature found does not support calling human-reserved remediation an
    anti-pattern for high-blast-radius changes. The automated-remediation research
    recommends exactly that split (auto-execute low-risk reversible actions, escalate the
    rest), and reports large collateral-damage costs when the gate is removed. SRE's toil
    concept does not cover a one-off schedule fix. What incident-management practice treats
    as the defect is different: duplicate reports are not grouped into one incident, and
    there is no escalation policy (secondary owner, timeout) when the single human is
    unavailable. 1186 is better framed as a single point of human failure with no
    deduplication than as "reporting is the wrong response".

  Specific risks: If C2A2 reads 1186 as licence to let agents change schedules: (a) several
    concurrent agents may each apply their own named fix, which is the same double-firing
    pattern moved onto the remedy; (b) an agent-applied schedule change has system-wide
    blast radius and, per 1185, its success would again be self-reported; (c) a wrong
    diagnosis can be auto-executed, which GuardedAct lists as an unsolved limitation.

  Mitigations available: (i) Consolidate: a single incident key per fault (e.g. "double-firing")
    that later reporters append to rather than restate. (ii) Escalation policy: a time-boxed
    fallback when Tom is unavailable (a pre-authorised, reversible, single-actor action such as
    disabling one duplicate trigger, gated and logged). (iii) Tiered authority by reversibility
    and blast radius rather than blanket prohibition or blanket delegation.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1186
  Strongest counterargument: Keeping schedule changes with the human is what current
    auto-remediation research recommends for high-blast-radius actions. Ungated
    LLM remediation causes roughly five times the collateral damage of gated remediation in
    the one controlled study found. The 8 agents that declined to act were working as
    designed. Had each acted on its own named fix, a multi-writer coordination failure would
    have hit the scheduler itself. The real gaps are a missing incident-grouping key and a
    missing escalation route for an absent owner. Both are standard, low-risk fixes that do
    not require giving agents remediation authority.
  What would need to be true for C2A2 to be safe: duplicate reports collapse into one tracked
    incident with a single priority; there is a defined fallback when the owner is away; any
    delegated action is single-actor, reversible, pre-approved by class, and verified from
    state (not narration).
  How to test: (a) Count distinct faults versus "needs you" notes over 7 days. A high ratio
    confirms a grouping gap, not a volume problem. (b) In a sandbox, let two agents each apply
    a named schedule fix concurrently and check whether the outcome is consistent.
```

```
SYSTEMIC-RISK-FLAG (CANDIDATE — preliminary, for 14b reconciliation):
  Date: 2026-10-26
  Affected items: PRESUMPTION-1184, PRESUMPTION-1185, PRESUMPTION-1186
  Common vulnerability: "Artefact-as-proof." In all three, an agent-produced artefact stands in
    for an enforced state transition: an output file stands in for a committed result (1184),
    narration for lock state (1185), and a "needs you" note for incident ownership and
    resolution (1186). AGAINST-side caveat: in each case the literature challenges the implied
    remedy (validate the predecessor, audit the narration, delegate the fix) more than the
    diagnosis. All three proposed remedies add another reading or attesting agent, while the
    literature's fixes are enforced at the state layer: atomic commit markers, fencing tokens,
    and a single incident key with gated actuation.
  Literature basis: Derosiaux 2024 (atomic dedup; read in full); Kleppmann 2016 fencing tokens
    (snippet only); Cai et al. 2026 GuardedAct (read in full; weak venue).
  Risk level: High (structural)
  Recommendation: 14b to consider one cross-cutting rule: coordination facts (done, locked,
    reported) exist only as atomic, run-id-tagged state changes that the target rejects or
    accepts, and never as agent narration or post-hoc checks.
```

Source-reading status: Source 1 [fetched; read in full; weak-venue caution above]. Sources 2 and 3 [snippet only]. I did not read SRE ch. 5 or the SRE Workbook directly, so the toil wording is UNVERIFIED as quoted. I found no primary literature on alert-fatigue thresholds at this volume.

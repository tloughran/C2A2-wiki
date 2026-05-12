SEARCH-AGAINST-PRESUMPTION-050:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-050
  Original statement: "4-day stale .git/index.lock classified as single incident, not escalation (asymmetric with ASSUMPTION-042 Chrome threshold)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-050
    Item type: PRESUMPTION (unstated — surfaced by inference) — INTERNAL-CONSISTENCY with ASSUMPTION-042
    Transform at each step:
      14b: Surfaced as asymmetric classification across channel pairs
      15b: Searched for challenging literature
    Current status: STRONGLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Incident vs. Problem classification (ITIL v4; Google SRE book ch. 14): a 4-day unresolved static blocker is a *problem*, not a single incident. The classification change triggers different response expectations (standing remediation, documented workaround, root-cause analysis).
    2. INTERNAL-CONSISTENCY with ASSUMPTION-042 (C2A2 prior): ASSUMPTION-042 established a 5-of-3 threshold for Chrome failure escalation. The 4-day git-lock does not cross an analogous threshold — because no analogous threshold exists for git-lock. The asymmetry is the presumption's own content: it treats the same class of signal with incompatible classification rules. This extends the INTERNAL-CONSISTENCY cluster (previously 1 pair, now 2 pairs).
    3. Standing-remediation lifecycle literature (Google SRE ch. 14 error budgets; Allspaw 2012 postmortems): persistent known blockers have a canonical lifecycle — opened, documented, assigned, resolved, closed. A 4-day open standing remediation without escalation violates this lifecycle at the assigned/resolved step.
    4. DECISION-018 history in the wiki: the git-lock issue is *already* a known standing condition. Classifying it as a single incident is inconsistent with the decision record.
    5. Alert-fatigue / normalization-of-deviance literature (Ancker et al. 2017; Vaughan 1996): persistent unescalated conditions create the "normalized deviance" failure mode — people stop noticing the signal.

  Strength of challenge: Strong

  Summary: The challenge is convergent across ITIL, SRE, standing-remediation literature, and C2A2's own prior disposition (ASSUMPTION-042, DECISION-018). All point to the same conclusion: a 4-day unresolved standing blocker should be classified as a problem with escalation and SLA, not as a single incident. The INTERNAL-CONSISTENCY cluster has now grown from 1 pair to 2 pairs — ASSUMPTION-042 is paired with both PRESUMPTION-044 (retry-past-threshold) and PRESUMPTION-050 (no-threshold-for-git-lock). The underlying gap is that ASSUMPTION-042's escalation structure is not applied uniformly.

  Specific risks: (a) INTERNAL-CONSISTENCY cluster expands to 2 pairs — ASSUMPTION-042 becomes the shared failure-mode center; (b) master-wiki updates blocked for 4+ days without escalation (visible via PRESUMPTION-047 narrative-discrepancy); (c) downstream consumers of the wiki (Dispatch, briefings) operate on stale data without awareness; (d) once normalization-of-deviance sets in, future 5-day / 6-day / 10-day blockers are harder to escalate.

  Mitigations available:
    - Define a git-lock-specific threshold analogous to ASSUMPTION-042 (e.g., 24h → attempt auto-clear; 48h → alert; 72h → block master-wiki writes and escalate).
    - Apply ASSUMPTION-042's structure uniformly across all operational-drift channels (there are now 4+ channels per the OPERATIONAL-DRIFT-FLAG).
    - Execute DECISION-018 remediation to remove the blocker at source.
    - Surface channel state uniformly in all briefings.

  Recommendation: STRONGLY-CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-050
    Strongest counterargument: The asymmetry isn't just a calibration gap — it's a structural gap. ASSUMPTION-042 defined a threshold for one channel and then never generalized. Now, four channels share the OPERATIONAL-DRIFT-FLAG but only one of them has a documented escalation threshold. The system has a *template* (ASSUMPTION-042) and is *not applying it*. The 4-day git-lock is the visible tip of the asymmetry; the same structural gap applies to the other two drift channels. Left unchallenged, the INTERNAL-CONSISTENCY cluster will grow mechanically with each new channel that drifts.
    What would need to be true for C2A2 to be safe: Generalize ASSUMPTION-042 from a Chrome-specific threshold to a channel-agnostic template; instantiate per-channel thresholds; uniformly report channel state; execute DECISION-018.
    How to test: Audit every OPERATIONAL-DRIFT channel for (a) defined threshold, (b) automated escalation, (c) surfacing in briefing. Count the channels without all three.

  INTERNAL-CONSISTENCY-FLAG (updated):
    Date: 2026-04-20
    Affected items: ASSUMPTION-042 (Chrome threshold) + PRESUMPTION-044 (retry past threshold) + PRESUMPTION-050 (no git-lock threshold)
    Common vulnerability: ASSUMPTION-042's escalation structure is not uniformly applied; each non-Chrome channel reveals a different form of the same gap.
    Risk level: Medium-High
    Recommendation: Treat ASSUMPTION-042 as a *template* and audit all OPERATIONAL-DRIFT channels for compliance.

SEARCH-AGAINST-ASSUMPTION-1153 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-09
  Original item: ASSUMPTION-1153
  Original statement: Three (four) instruments retracted their own confident, specific findings within
    the same day, and one retraction prevented the reversal of correct repairs — read as an anomaly
    requiring architectural explanation.
  Under test this cycle (MONITOR-542): the body both directions reported UNREACHED twice — formal
    statistical decision theory (Neyman-Pearson thresholds, inspection games, audit sampling) — and
    whether it supplies the missing ASYMMETRIC LOSS separating detection-direction from
    correction-direction error.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.
  INDEPENDENCE INCIDENT: my fetch of pcaobus.org AS 2315 was refused as "Already fetched … 14s ago in
    this session." I did not fetch it earlier; another agent sharing the fetch layer did. No content
    returned to me. See today's SYSTEMIC-RISK flag.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: ASSUMPTION-1153
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a (2026-08-18): Collected four same-day self-retractions and one near-miss; paired against
        the prior night's opposite failure mode.
      15a (cycle 0): reported decision-theory body unreached.
      15b (cycle 0, 2026-08-19): PARTIALLY-CHALLENGED (Moderate) — base rates (76–>90% FP) make the
        day unremarkable; named the corrective-direction asymmetry; decision theory unreached.
      15c: → MONITOR-542 (High); carried the asymmetry into REVISE-363.
      15d (2026-08-30): Re-triggered, cycle 1; owed = NP/inspection games/audit sampling + stated loss.
      15b (re-trigger cycle 1, 2026-10-09): 3 searches (inspection games; audit sampling risks;
        cost-sensitive thresholds); 2 fetch attempts, BOTH FAILED (PCAOB AS 2315 dedup, no content;
        arXiv:1306.4219 abs page blocked — URL not in provenance set, search returned the PDF URL).
    Current status: CHALLENGED

  EVIDENCE GRADE: PRELIMINARY, search-result level. The AS 2315 text is quoted from search-result
    snippets of the standard itself (pcaobus.org), not from a fetched page. Inspection-games content
    via a secondary paper's description. The decision-theory body is now REACHED at search-result
    level for the first time; it is not yet read.

  Challenging evidence found: Yes

  Sources:
    1. Avenhaus, R., von Stengel, B. & Zamir, S. 1995. "Inspection Games." Handbook of Game Theory
       Vol. III (as described in arXiv:1306.4219, "Inspection and crime prevention: an evolutionary
       perspective"). [search-result; fetch blocked] The inspector's errors are a false-alarm
       probability α and non-detection probability β; the inspector "first fixes the false-alarm
       probability α … then picks the test that minimizes the worst-case non-detection probability"
       — Neyman-Pearson logic inside a game; α itself is set in a second, non-zero-sum game.
       Bearing: in the formal theory a rational inspector OPERATES at α > 0 by design. A nonzero rate
       of confident findings later withdrawn is the equilibrium output of a correctly-tuned inspector,
       not an anomaly. The claim's framing has no α against which "four in a day" could be anomalous.
    2. PCAOB AS 2315, Audit Sampling. [search-result — snippets of the standard's own text; fetch
       failed (dedup)] Defines risk of incorrect REJECTION (sample says misstated when it is not) and
       incorrect ACCEPTANCE; incorrect rejection "relate[s] to the efficiency of the audit," and "if
       the auditor's evaluation of an audit sample leads him to the initial erroneous conclusion that
       a balance is materially misstated when it is not, the application of additional audit
       procedures and consideration of other audit evidence would ordinarily lead the auditor to the
       correct conclusion." Bearing: this is exactly the asymmetric loss MONITOR-542 says "no part of
       this system states": false alarms are an EFFICIENCY cost the profession expects to be caught
       by follow-up; false acceptances are an EFFECTIVENESS cost. Every one of the four retractions —
       and the near-miss, caught by "one grep" — is an incorrect rejection corrected by an additional
       procedure, which is the standard working as designed.
    3. Cost-sensitive threshold selection (r-statistics.co "Thresholds Under Asymmetric Costs";
       casrai.org Youden's J guide; Horvitz AISTATS ROC note). [search-result] Optimal operating point
       is where ROC slope = ((1−p)/p)·(C_FP/C_FN); raising miss cost lowers the threshold and RAISES
       the false-alarm rate. Bearing: given ASSUMPTION-1152/PREMISE-181's push for more detection
       sensitivity (i.e. C_FN high), more retractions are the PREDICTED consequence; they are evidence
       the policy is being followed, not a malfunction.

  Strength of challenge: Moderate (would be Strong if the AS 2315 and Handbook texts were read in
    full; the arguments are standard but my access was search-result only)

  Summary: Formal decision theory removes the ground for calling the day anomalous. Inspection-game
    equilibria fix a positive false-alarm probability; cost-sensitive thresholds raise false alarms
    whenever misses are costed higher, which PREMISE-181 does; and audit sampling explicitly prices
    incorrect rejection as an efficiency loss that follow-up procedures are expected to correct. The
    four retractions and the near-miss all fit that pattern: confident wrong detections caught by a
    second procedure before action. What the literature also supplies is the missing loss structure:
    detection-direction error = efficiency; acting on an uncorrected detection (the corrective
    direction) converts an efficiency loss into an effectiveness loss. The architectural lesson is
    therefore not "explain the anomaly" but "require the follow-up procedure before any corrective
    action" — a gate, not an investigation.

  Specific risks: (i) treating the retraction rate as a defect and tightening instruments raises β —
    the opposite failure, already seen (ASSUMPTION-1152); (ii) the near-miss was caught by luck of a
    grep, not by a mandated second procedure — AS 2315's "ordinarily" presumes the procedure is
    required; (iii) without a stated α (or C_FP/C_FN), no rate can be called high or low, so the
    system cannot tell drift from noise.

  Mitigations available: state the loss explicitly — detection false alarms cost one re-check;
    corrective actions on unverified detections cost a reversal of correct work (assign e.g. ≥10×);
    mandate an independent confirming procedure before any corrective edit (audit-sampling analogue);
    log retraction rate as the realised α and monitor it for drift rather than for occurrence.

  Recommendation: CHALLENGED — on the "anomaly requiring architectural explanation" framing. The
    corrective-direction asymmetry (preserved by 15c) is SUPPORTED by this same literature, i.e. the
    surviving content is REVISE-363, not ASSUMPTION-1153. Broader search: fetch AS 2315 ¶¶ .12–.19
    and the Avenhaus/von Stengel/Zamir chapter.

STEELMAN:
  Item: ASSUMPTION-1153
  Strongest counterargument: Every mature inspection discipline expects confident false alarms and
    builds the follow-up step that catches them. Game-theoretic inspectors choose a positive
    false-alarm rate on purpose; auditors classify a wrong "misstated" finding as an efficiency cost
    that further procedures ordinarily correct; and a system that has just decided to weight misses
    heavily is mathematically committed to more false alarms. Four retractions in a day, each caught
    before action, is the signature of an inspection regime working — calling it an anomaly invites
    a fix that will reintroduce the silent-pass failure of the night before.
  What would need to be true for C2A2 to be safe: corrective actions are gated by a mandatory
    confirming procedure; the retraction rate is tracked as α against a stated target.
  How to test: over 30 days, count instrument findings, retractions, and corrective actions taken
    on findings later retracted. Retractions with zero wrong corrective actions = regime working;
    any wrong corrective action = the gate is missing (REVISE-363), regardless of retraction count.

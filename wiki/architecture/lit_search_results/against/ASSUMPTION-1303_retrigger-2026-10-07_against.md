SEARCH-AGAINST-ASSUMPTION-1303 (RE-TRIGGER cycle 1, derived question only):
  Date searched: 2026-10-07
  Original item: ASSUMPTION-1303 (dispositioned INCORPORATE, limb-split, as PREMISE-201)
  Statement watched (MONITOR-598, derived): "Amending a gate's threshold RESTORES attention to a channel
    that has already been abandoned." 15b direction: seek hysteresis / non-recovery — attention not
    returning after precision is improved.
  Standing instruction (for_lit_search.md): a second null is a FINDING, not a reason for a third pass.
    NOT-REACHED lanes from cycle 0 to search first: low-base-rate vigilance; SRE alert precision.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: ASSUMPTION-1303
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-09-09 intake (418-hit gate, single-digit actionable; threshold amendment proposed).
      15b (2026-09-10): remedy limb CHALLENGED (Strong); declared gap: no before/after measurement of
        precision improvement in an ABANDONED channel; hysteresis open.
      15c: DISPOSITION-923 → PREMISE-201 + MONITOR-598 on the gap.
      15d (2026-09-20): Re-triggered; owed = narrow before/after search.
      15b (re-trigger cycle 1, 2026-10-07): 3 searches, 1 fetch. NOT a null this time: found one direct
        before/after measurement, and it shows non-recovery.
    Current status: CHALLENGED

  EVIDENCE GRADE: one fetched secondary report of a conference abstract (single site); two search-result
    sources from the trust-in-automation / cry-wolf literature. The SRE lane was again NOT reached
    (budget spent on the clinical hit, which is more on point).

  Challenging evidence found: Yes

  Sources:
    1. Kunadu, A. et al. 2017. Harlem Hospital Center ICU alarm-reduction program, CHEST 2017 annual
       meeting abstract (Chest 152(4) suppl.); reported by Zoler, M.L., "Alarm reductions don't improve
       ICU response times," *The Hospitalist*, 5 Dec 2017. [fetched — news report of the abstract;
       primary abstract NOT retrieved] A 20-bed adult ICU with prior alarm fatigue (prior studies cited:
       up to 99% non-actionable) RAISED THRESHOLDS on monitors, pumps and ventilators "to decrease alarm
       frequency and boost the clinical importance of each alarm," with concurrent staff education.
       Alarms fell 4.5 → ~2 → 1.3 per patient-hour over 4 months. Timely response (<60 s) FELL from 60%
       at month 1 to 12% at month 4. Investigator: "Even though we made the alarms more actionable the
       conditioning remained"; "it may take years to recondition clinicians." Bearing: this is the
       before/after study MONITOR-598 asked for — precision improved in a channel with documented prior
       abandonment, outcome measured as RESPONSE (a reading-rate proxy), not volume — and attention did
       not return; it declined. CAVEATS: single site, conference abstract, no pre-intervention response
       baseline in the report (60% is post-intervention month 1, so the early figure may be an
       education/novelty bump decaying), no control unit; acuity and staffing not reported.
    2. Lee, J. & Moray, N. 1992. "Trust, control strategies and allocation of function in human-machine
       systems." Ergonomics 35(10). [search-result, via secondary summaries incl. arXiv:2107.07374]
       Trust drops sharply after faults; failures move trust more than successes ("difficult to build,
       lost quickly"); trust modelled as autoregressive (trust_t depends on trust_{t-1}). HONEST CAVEAT:
       summaries also say trust "recovered shortly after" faults in that task. Bearing: asymmetry and
       autoregression are the formal ingredients of hysteresis; recovery in a lab task with few faults
       is not recovery after chronic ~98% false positives.
    3. Breznitz, S. 1984. *Cry Wolf: The Psychology of False Alarms.* [search-result, via Nautilus
       "Crying Wolf in an Age of Alarms"] Each false alarm reduced perceived trustworthiness of the
       warning system. Search did NOT surface any result on credibility recovery after reliable warnings
       resume — a null on the recovery question in this lane.

  Strength of challenge: Moderate-to-Strong (direction clear and directly on the question; evidential
    base is one single-site abstract)

  Summary: The second pass did not return a second null. It found one before/after measurement on the
    exact question: an ICU that had been conditioned to ignore alarms raised thresholds, cut alarm volume
    by ~70%, made each surviving alarm more actionable, educated staff — and saw prompt response fall
    from 60% to 12% over four months. The investigators' own reading is hysteresis: conditioning
    persists after the precision that produced it is gone. The trust-in-automation literature supplies
    the mechanism (losses weigh more than gains; trust is autoregressive) and the cry-wolf literature
    finds cumulative credibility loss with no located recovery evidence. Nothing found shows attention
    returning to an abandoned channel because its precision improved.

  Specific risks: PREMISE-201's plan for the 418-hit gate assumes the amended gate will be read again.
    On this evidence the amendment can succeed on volume and precision and still fail on attention —
    and the failure is invisible to any metric that counts hits rather than reads.

  Mitigations available: Re-site rather than re-tune (new channel/name/format so prior conditioning does
    not attach); measure read/response rate directly after any amendment; forcing-function acknowledgement
    for the surviving high-precision hits.

  Recommendation: CHALLENGED — evidence of non-recovery found; supports MONITOR-598's REVISE branch
    ("do not amend; re-site the signal"), subject to the single-site caveat.

STEELMAN:
  Item: ASSUMPTION-1303 (derived restoration claim)
  Strongest counterargument: Abandonment is learned, and unlearning is not triggered by a change the
    reader has stopped looking at. A channel that is no longer read cannot communicate that it has
    become more precise — the very improvement is delivered through the channel that is being ignored.
    The one measured case found shows exactly this: precision up, volume down by two-thirds, education
    delivered, and response collapsing anyway. Threshold amendment therefore treats the CAUSE of
    abandonment while leaving the abandonment itself — a conditioned habit — untouched.
  What would need to be true for C2A2 to be safe: the reader of the 418-hit gate is an agent with no
    conditioning (re-reads every hit from scratch each run) — in which case hysteresis does not apply;
    or the amended gate is moved to a new, unconditioned channel.
  How to test: log whether each surviving hit after amendment is opened/acted on within one run; compare
    with the pre-amendment read rate. If the reader is a stateless agent, record that explicitly as the
    condition under which restoration holds.

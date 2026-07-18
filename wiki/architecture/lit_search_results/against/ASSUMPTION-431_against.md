SEARCH-AGAINST-ASSUMPTION-431:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-431
  Original statement: "A failing QC signal (qc_sweep 'fidelity fail') can be reclassified as environmental (absent sandbox cache) without independent re-verification of content."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-431
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extraction (stated assumption, MEDIUM-HIGH, QUEUED-EMPIRICAL, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Leveson, N., Turner, C., 1993. "An Investigation of the Therac-25 Accidents." IEEE Computer 26(7). — The paradigm case: 5-10 malfunction messages per day, mostly spurious, conditioned operators to reclassify error signals as routine and proceed without verification; a real overdose signal ("Malfunction 54") was dismissed under the same habit. Also documents investigators asserting a cause (microswitch failure) without evidence that reproduced or confirmed it — cause-assignment without verification.
    2. "Alarm fatigue." Wikipedia (summarizing NTSB and clinical-alarm literature, incl. the 2009 DC Metro collision investigation). — Documents the general mechanism: environments with high false-alarm rates produce a default of dismissal, and the dismissal habit — not the false alarms themselves — is what converts a true alarm into an accident.
    3. Journal of Safety Research, 2022. "A qualitative systematic review on the application of the normalization of deviance phenomenon within high-risk industries." (ScienceDirect S0022437522001827). — Cross-industry evidence that "known spurious" labels attached to warning signals are a recurring precursor pattern: each unverified dismissal that goes unpunished strengthens the label.

  Strength of challenge: Strong

  Summary: The safety literature's core lesson on alarm handling is precise here: it is often correct that a given alarm is environmental, and it is still catastrophic as a policy to reclassify without verification, because the policy is what fails, not the instance. The Therac-25 operators were right that most malfunction messages were noise — which is exactly why they proceeded past the one that was not. Reclassifying a fidelity failure as "absent sandbox cache" based on a plausible environmental story, without independently re-verifying the content the QC was guarding, establishes a dismissal precedent: the next fidelity fail in a cache-absent context will inherit the "known environmental" label automatically. The plausibility of the environmental explanation is not evidence about the content; only re-verification of the content is.

  Specific risks: A genuine fidelity failure (corrupted or truncated wiki content, bad transform) co-occurring with the environmental condition is waved through — and cache absence may CAUSE both the QC artifact and real content damage, making co-occurrence likely rather than coincidental; the QC channel's authority erodes (once one fail is overridden by narrative, all fails are negotiable); "known spurious under condition X" hardens into an unwritten rule that survives long after condition X's behavior changes.

  Mitigations available: Rule: reclassification requires one independent check of the guarded property (re-run qc_sweep in an environment with the cache present; direct diff/hash of content against source) — the environmental story picks which check, it does not replace the check; log every reclassification with its verification evidence; periodically inject a known-bad content sample under the environmental condition to confirm the QC would still catch it (alarm-integrity testing).

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Not all alarm dismissals are Therac: when a failure mechanism is fully understood and deterministic — the fidelity check REQUIRES the sandbox cache, the cache was verifiably absent, and the check is known to fail closed in that state — then the reclassification is a diagnosis, not a dismissal. Demanding content re-verification for every mechanistically-explained environmental failure imposes unbounded cost and its own alert-fatigue burden. Engineering practice legitimately distinguishes "alarm output invalid because instrument precondition unmet" from "alarm signal ignored."
    What would need to be true for C2A2 to be safe: The causal chain from cache absence to this specific failure signature must be established (reproduced), not just plausible; the failure signature of "cache absent" must be distinguishable from the signature of real fidelity failure; cache absence must not itself be capable of causing content damage; the reclassification must be one-time-diagnosed, with recurrence triggering the full check rather than inheriting the label.
    How to test: [QUEUED-EMPIRICAL — decisive test is in-house] Re-run qc_sweep on the same content with the sandbox cache present: pass confirms the environmental diagnosis; fail refutes it. Additionally, run qc_sweep on deliberately corrupted content with the cache absent to check whether the two failure signatures are even distinguishable.

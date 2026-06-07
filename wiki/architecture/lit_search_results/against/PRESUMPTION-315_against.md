SEARCH-AGAINST-PRESUMPTION-315:
  Date searched: 2026-06-07
  Original item: PRESUMPTION-315
  Original statement: [inferred] Dispositioning the app.js:1314 error as a stale buffer artifact presumes single-reload non-reproduction + one positive handler-fires check is a complete exoneration; reachability of the throwing init-state from real user sequences was not established.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-315
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that single-reload non-repro + one positive check fully exonerates the error.
      15b: Searched for evidence that single non-reproduction is not exoneration (heisenbug / non-determinism).
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Heisenbug / non-deterministic-defect literature (the term and its concurrency/timing causes). — Bugs whose triggering conditions are timing-, memory-layout-, or init-order-sensitive routinely fail to reproduce on a single attempt and reappear under different conditions; non-reproduction is the SIGNATURE of these bugs, not evidence of their absence. Direct challenge.
    2. Race-condition / initialization-order analysis. — An init-order race or an uninitialized-state path can throw only on specific load orderings; a single clean reload exercises one ordering and says nothing about the others. Challenges "complete exoneration."
    3. "Absence of evidence ≠ evidence of absence" testing principle; reachability analysis. — One positive handler-fires test confirms one path; it does not establish that the throwing init-state is UNREACHABLE from real user sequences (the property actually at issue). Challenges the inference.

  Strength of challenge: Moderate-Strong

  Summary: The presumption is well challenged. The error's own symptom — present once, gone after reload — is the classic heisenbug profile of an init-order/timing-sensitive defect, for which a single non-reproduction provides essentially no exoneration. A passing handler-fires check confirms one happy path but does not establish unreachability of the throwing state from real user sequences, which is the actual safety property. "Stale buffer artifact" is a plausible hypothesis, not a verified diagnosis; closing on it conflates "did not recur once" with "cannot recur."

  Specific risks: A latent init-order race remains shippable and may surface for real users under load orderings the single test never exercised; because it was dispositioned as exonerated, no guard or instrumentation is in place to catch recurrence (silent-failure risk).

  Mitigations available: Cheap, decisive re-test rather than closure — repeated/randomized reloads and cold-vs-warm cache loads; add a lightweight assertion/telemetry around the init-state so a recurrence is logged rather than silent; attempt to reach the throwing state from realistic user sequences (the reachability question); keep the item OPEN-pending-recurrence rather than closed.

  STEELMAN:
    Item: PRESUMPTION-315
    Strongest counterargument: The disposition treats two weak signals — "didn't happen the one time I reloaded" and "the handler fired once" — as a proof of absence, but the error's vanish-on-reload behavior is exactly what an init-order/timing bug does. The property that matters is reachability of the throwing state from real user sequences, and neither check addresses it; a stale-buffer story is the most convenient hypothesis, not the tested one. Calling it exonerated removes the pressure to add the cheap guard that would actually catch a recurrence.
    What would need to be true for C2A2 to be safe: The throwing init-state is genuinely unreachable in the shipped build under realistic load orderings — established by repeated/varied reproduction attempts plus reachability reasoning, not a single reload.
    How to test: Repeated randomized reloads + cold-cache loads; add telemetry around app.js init so any recurrence is recorded; only then close.

  Recommendation: CHALLENGED

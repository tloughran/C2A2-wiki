SEARCH-AGAINST-PRESUMPTION-445:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-445
  Original statement: "[inferred] That a human-mediated compile loop (agent pastes commands, human runs regen/reload) is a reliable substrate for iterative debugging."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-445
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the session workflow (agent produces commands, human executes regen/reload by hand) that this loop was being treated as a reliable debugging substrate
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Swain, A.D., Guttmann, H.E., 1983. "Handbook of Human Reliability Analysis with Emphasis on Nuclear Power Plant Applications" (THERP, NUREG/CR-1278). — Baseline human error probabilities for procedure execution: omission of a step when procedures lack checkoff provisions is assigned ~4.2E-3 per item, with higher rates under stress; multi-step manual loops accumulate these per iteration. Directly quantifies the unreliability of "human pastes and runs commands" as a substrate.
    2. Williams, J.C., 1988. "A data-based method for assessing and reducing human error to improve operational performance" (HEART). — Error-producing conditions include time pressure, unfamiliarity, and poor feedback — all present in a deadline-week manual regen/reload loop; multipliers raise base error rates by 3x–17x.
    3. Leigh Partnership, "The perils of 'Swivel Chair Integration'." — When a human is the integration layer between systems, errors are introduced that are "very hard to track and resolve" and the human becomes a single point of failure; this is exactly the agent→human→shell→browser loop.
    4. ConnectorHub / practitioner swivel-chair literature. — Manual re-entry/hand-execution carries roughly 1% per-transaction error rates in industry estimates, compounding across debugging iterations.
    5. Design Gurus, "Why Your Cache Is Serving Stale Data (5 Invalidation Bugs Explained)" and related practitioner sources. — State-drift failure mode: the artifact under inspection (browser view) can silently lag the artifact just built (stale reload, cached file), so the human reports test results for the wrong version — the classic "did you refresh?" failure that invalidates debugging inferences.

  Strength of challenge: Strong

  Summary: Human reliability analysis (THERP, HEART) provides decades of quantified evidence that humans executing multi-step procedures without checkoff provisions err at rates around 10^-3 to 10^-2 per step, with substantial multipliers under time pressure — and a debugging loop runs many iterations, so per-session failure probability is material. The swivel-chair integration literature independently documents that using a human as the transport layer between systems is error-prone, hard to audit, and a single point of failure. Most damaging for debugging specifically is state drift: with manual regen/reload there is no guarantee the observed behavior corresponds to the just-edited code (stale reload, wrong file, skipped regen), so negative results are uninterpretable — the loop doesn't just add errors, it corrupts the evidence the debugging process depends on. No literature was found defending manual human-mediated loops as reliable; the practitioner consensus is that they are a stopgap to be automated away.

  Specific risks: A skipped or mis-ordered regen step makes a real fix look like a failure (or vice versa), sending the agent down false debugging paths near a deadline; version/observation mismatch produces confident but wrong conclusions about the artifact that ships to ISME; error attribution is impossible after the fact because the manual steps leave no log.

  Mitigations available: Single wrapper script (regen + validate + cache-busting reload marker) so the human runs one command, not a sequence; embed a build timestamp/hash in the artifact and have the human read it back, converting "did you refresh?" into a verifiable check; checklist with explicit checkoff (THERP shows checkoff provisions cut omission rates); where possible move execution to the agent side (workspace shell) and reserve the human for observation only.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-445
  Strongest counterargument: The human-mediated loop fails not primarily by being slow but by being epistemically unsound: every observation the agent receives is conditioned on the human having executed the right commands, in the right order, on the right files, and having actually reloaded the right view — and human reliability data says each of those steps fails at non-negligible rates that time pressure multiplies. Because failures are silent (a stale page looks exactly like an unfixed bug), the loop generates false negatives that cannot be distinguished from true negatives, so debugging conclusions drawn through it — including the "known minor defect" classification feeding ASSUMPTION-414 — inherit unquantified uncertainty. Industry treats such swivel-chair loops as anti-patterns to be eliminated, not substrates to be relied on.
  What would need to be true for C2A2 to be safe: Every human-executed cycle must be verifiable after the fact — e.g., a build hash visible in the artifact that the human reports back — so version/observation mismatch is detectable rather than silent.
  How to test: Inject a deliberate no-op change with a visible marker and run the loop; measure how often the human's report reflects the pre-change state. Alternatively audit the ISME session transcript for instances where a "failed fix" was later found to be a stale reload.

SEARCH-AGAINST-ASSUMPTION-035:
  Date searched: 2026-08-23
  Cycle: 5 (15d monthly re-trigger; cohort 2026-07-05; unconsumed 49 days)
  Original item: ASSUMPTION-035 (MONITOR-040)
  Original statement: "Cross-session handoff via ~/Documents/Claude/Handoffs/latest.md + a SessionStart hook will RELIABLY orient the Saturday Dispatch session."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15b (cycle 5)]
    Original item: ASSUMPTION-035
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — stated cross-session orientation mechanism for the Saturday Dispatch
      15b (cycle 0, 2026-04-17): CHALLENGED — compound-probability failure across an untested 4-link chain
      15b (cycle 1, 2026-04-20): PARTIALLY-CHALLENGED — loading half validated at N=1; execution half unobserved (pivot-on-arrival confound, PRESUMPTION-046)
      15b (cycles 2–4): refresh only; no new literature surfaced
      15b (cycle 5, 2026-08-23): Searched for challenging literature — NEW MATERIAL FOUND
    Current status: CHALLENGED (escalated from PARTIALLY-CHALLENGED)

  Challenging evidence found: Yes — and materially new this cycle.

  Sources:
    1. anthropics/claude-code Issue #10373, "SessionStart hooks not working for new conversations" (opened by jeremybarnes, 2025-10-26; still OPEN as of 2026-08-23; labels: bug, has repro, area:core, platform:macos). Fetched and read in full. The reporter demonstrates on macOS (Darwin 24.6.0, Claude Code 2.0.27) that SessionStart hooks DO execute — verified by file logging — but their stdout is never parsed into `hookSpecificOutput.additionalContext`, no `hook_additional_context` attachment is created, and nothing is injected into the model's context for a brand-new interactive session. Hooks work correctly for `/clear`, `/compact`, and URL-resume, and fail silently only for new sessions. The reporter's test used a canary ("the secret word is bamboozle"); Claude had no knowledge of it. THIS IS THE EXACT MECHANISM AND EXACT PLATFORM C2A2 RELIES ON, and it produces a failure that is invisible from the hook side. Direct URL: https://github.com/anthropics/claude-code/issues/10373
    2. anthropics/claude-code Issue #33612, "[BUG] SessionStart hooks in remote-settings.json silently ignored by non-terminal clients" (opened by harald-voca, 2026-03-12; closed as not planned / stale; labels: bug, area:hooks, has repro). Fetched and read in full. SessionStart hooks defined in `~/.claude/remote-settings.json` do not fire under non-terminal clients (MCP-based or web); the command is silently skipped, no error, no output injected — while other settings in the same file (permissions.deny) ARE honoured, so the file is demonstrably being read. Entry-point-dependent hook activation is therefore a documented, unpatched class. URL: https://github.com/anthropics/claude-code/issues/33612
    3. anthropics/claude-code Issue #10997, "[BUG] SessionStart hooks don't execute on first run with GitHub marketplace plugins" — marketplaces load asynchronously and the hook fires before the fetch completes; a first-run race. (Surfaced in search; title and framing verified via search index, issue body not fetched.)
    4. "The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break," arXiv:2604.11978 (2026, preprint). Attributes long-run agentic failure principally to subplanning errors and catastrophic forgetting that accumulate as runs lengthen — i.e. even a correctly loaded payload degrades in utilisation over the session, which is the second half of "orient."
    5. "Why Retrying Fails: Context Contamination in LLM Agent Pipelines," arXiv:2605.08563 (2026, preprint). Failed state persists in the context window and is re-consumed on retry; recovery from a bad rehydration is not free, it is actively contaminated.
    6. Hanley, J.A. & Lippman-Hand, A. 1983. "If Nothing Goes Wrong, Is Everything All Right? Interpreting Zero Numerators." JAMA 249(13):1743–1745. The canonical statement that zero observed failures does not license a zero-risk inference; carried forward from the cycle-3 reliability line and now given specific numeric force (see item 3 file).
    7. Bornholt, J., Kaufmann, A., Li, J., Krishnamurthy, A., Torlak, E. & Wang, X. 2016. "Specifying and Checking File System Crash-Consistency Models." ASPLOS 2016. POSIX `rename` is atomic in namespace semantics but NOT in persistence semantics; without a directory fsync the rename itself can be lost. A `latest.md` that is written-then-renamed can be absent, empty, or partial after an untimely reboot.

  Strength of challenge: Strong (UPGRADED from Moderate at cycles 1–4)

  New since cycle 0/1: YES — and this is the first cycle since cycle 1 with genuinely new material. The change is not incremental. At cycles 0–1 the compound-failure argument was a priori: "each of these links could fail." As of this cycle there is a documented, reproduced, still-open defect in the exact product, on the exact platform, in which the SessionStart hook FIRES SUCCESSFULLY AND ITS PAYLOAD IS SILENTLY DISCARDED for brand-new interactive sessions (Issue #10373). This converts the cycle-1 phrase "loading half validated at N=1" into an actively unsafe description, because the 2026-04-18 observation of "the hook fired" is not the same observation as "the payload reached the model," and the defect report shows those two can come apart with no error surfaced. Unless the 2026-04-18 test verified a canary token present in the model's own output — which the record does not show — the single supporting datum does not discriminate between success and this documented failure mode.

  Summary: The cycle-5 search found the strongest challenging evidence in this item's history, and it is specific rather than generic. Issue #10373 documents that on macOS, for new interactive sessions, SessionStart hook stdout is executed but never injected — a failure indistinguishable from success unless the session is probed for the payload's content. Issue #33612 shows the same silent-skip behaviour is entry-point-dependent, so a hook that works from the terminal may not work from a scheduled or non-terminal invocation, which is precisely how a Saturday Dispatch might be launched. Two independent 2026 preprints add that even a correctly loaded payload is not reliably utilised over a long session. Taken together, the word "reliably" in the original statement is now challenged on the LOADING half as well as the execution half — a reversal of the cycle-1 finding, which had treated loading as the settled part.

  Specific risks: (a) The Dispatch session boots, the hook fires, the log shows success, and the model has none of the handoff content — and no one can tell, because the only evidence anyone collects is "the hook fired"; (b) the failure is entry-point-conditional, so a manual terminal smoke test can pass while the actual scheduled/non-terminal path fails; (c) the cycle-1 disposition ("loading half validated") is now the load-bearing error, and every downstream item that inherited it inherits a claim contradicted by a still-open upstream defect; (d) `latest.md` can be lost or truncated by an untimely crash between write and rename with no application-visible signal.

  Mitigations available:
    - CANARY TEST, not a log check. Put a nonce token in `latest.md` and require the Dispatch session to echo it back in its first output. Absence of the nonce is the only reliable detector of the #10373 failure mode.
    - Test the hook from the SAME entry point the real Dispatch uses, not from an interactive terminal (per #33612 and #10997).
    - Known workaround from #10373: issuing `/clear` at session start does trigger hook processing. This is available today and cheap.
    - Do not treat "hook executed" logs as evidence of orientation. Instrument the consumption side.
    - Write `latest.md` with write-to-temp + fsync + rename + directory fsync, or accept a documented small probability of a truncated payload.
    - Downgrade the language: the mechanism is "orientation-capable," not "reliable."

  Search scope: Comprehensive for the platform-specific failure-mode question (Claude Code issue tracker fetched and read directly for two issues); moderate for 2026 agentic-reliability preprints; preliminary for file-system crash-consistency (canonical sources located, not exhaustively surveyed).

  Recommendation: CHALLENGED (upgraded; recommend 15c revisit the cycle-1 "loading half validated" finding in light of Issue #10373)

STEELMAN:
  Item: ASSUMPTION-035
  Strongest counterargument: The single piece of evidence ever offered for this assumption is that on 2026-04-18 the hook fired and the session appeared oriented. Issue #10373 shows that on this exact platform, a hook can fire, log success, and have its entire payload discarded before it reaches the model — with no error anywhere. That means the observation C2A2 recorded is compatible with both hypotheses, and cannot distinguish them. The assumption is therefore not weakly supported; it is unsupported, and has been for four months while four refresh cycles reported "no change." Worse, the failure is entry-point-conditional (#33612), so the natural way to reassure oneself — run it from a terminal and watch it work — is exactly the test that cannot detect the failure in the scheduled path.
  What would need to be true for C2A2 to be safe: (a) The Dispatch launch path is verified to be one where SessionStart context injection actually occurs on the installed Claude Code version; (b) verification is by content-level canary echoed by the model, not by hook exit code or log line; (c) at least one such canary-verified run exists from the real launch path; (d) a fallback exists (explicit `/clear`, or an in-prompt file read) that does not depend on hook injection at all.
  How to test: Place a random nonce in `latest.md`. Launch a Dispatch session via the real path. First instruction: "state the nonce in the handoff file." If the session cannot state it without reading the file itself, the hook injection did not occur, regardless of what the hook log says. Repeat three times; record N successes. Until then, "reliably" has no basis on either half of the chain.

SEARCH-AGAINST-PRESUMPTION-736:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-736
  Original statement: The interrupt marker (`[Request interrupted by user]`) is read as exogenous (genuinely user-caused) and has never been diagnosed — four sessions died at this marker on a day with no attended session.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-736
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced the unstated presumption that the interrupt marker reliably indicates genuine user action rather than harness/infrastructure failure.
      15b: Searched for challenging literature.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. GitHub anthropics/claude-code Issue #2809, "Unexpected Interruption Detection in Claude Code Interaction" — reports what the issue title itself frames as "an apparent false interruption detection... a potential bug in the interaction handling mechanism." Directly on point: the interrupt marker can fire without genuine user action.
    2. GitHub anthropics/claude-code Issue #35741, "[BUG] Interrupted · What should Claude do instead? randomly firing across multiple parallel sessions" — describes interrupt messages firing randomly across parallel sessions with no user input, and recurring even after "continue" is typed.
    3. GitHub anthropics/claude-code Issue #35643, "[BUG] Session keeps getting interrupted without any external interventions like pressing escape" — title states the failure mode directly: sessions interrupted with zero external (user) action.
    4. GitHub anthropics/claude-code Issue #70543, "[BUG] Claude Code fabricated a user interruption/instruction and preserved it after compaction" — a related but distinct failure: the system can synthesize an interruption artifact that did not originate from the user and then persist it as if it were real, which would look identical in logs to a genuine interrupt.
    5. openclaw/openclaw Issue #59946, "Subagent killed by LLM provider streaming idle timeout (~60s) — no retry or graceful handling" and Issue #88907 (chronic silent-timeout failures) — document a distinct, non-Claude-Code-specific mechanism: provider-side streaming idle timeouts silently kill sessions with no distinguishing signal from a genuine interrupt, and orchestrators receive no actionable failure signal ("silent" termination).
    6. Sociotechnical incident-analysis literature: attribution-bias research (e.g., work summarized around "fundamental attribution error" in incident investigation, and Dekker-style "New View" safety literature referenced via identecsolutions.com and theagileadmin.com) — establishes a general, well-documented cognitive bias in which investigators default to attributing failures to the nearest human-associated cause ("operator error" / "user interrupted") rather than investigating latent system/infrastructure causes, especially when the human-attributed cause requires no further engineering work to accept.

  Strength of challenge: Strong

  Summary: There is direct, documented evidence — filed as open bugs against the exact software C2A2 runs on — that the `[Request interrupted by user]` class of marker can be produced by the harness itself with no user action: false-interruption detection bugs, interrupts firing across sessions with no input, and even fabricated interruption artifacts that persist in context. Independently, provider-side streaming idle-timeouts are documented to silently kill agent sessions with no distinguishing log signal. On top of the mechanical evidence, the incident-investigation literature independently predicts exactly the failure PRESUMPTION-736 flags: investigators (human or automated) default to attributing an ambiguous termination to the nearest labeled human-associated cause rather than digging into infrastructure, because that is cognitively and operationally cheaper. All three lines of evidence converge on the same conclusion: treating the marker as reliably exogenous is not a safe default.

  Specific risks: If C2A2 logs these four sessions as user-caused, it will (a) miscount uptime/reliability of the autonomous cycle, (b) fail to open an infrastructure investigation into a real harness or provider-side bug that could recur and silently truncate future work, and (c) potentially misattribute blame in downstream postmortems or trust calibration for the autonomous system, compounding over cycles if unaddressed.

  Mitigations available: The item's own proposed discriminator — correlating the marker against session length, subagent fan-out, tool class, and wall-clock time — is exactly the right in-house test and is cheap. This is directly supported by the literature found: distinguishing genuine interrupts from streaming-timeout kills or false-detection bugs requires log-level signals (timing regularity, correlation with specific tool/fan-out patterns) rather than trusting the marker text.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-736
  Strongest counterargument: Even granting that false-interruption bugs exist in Claude Code and that streaming timeouts exist in other harnesses, it does not follow that these four specific sessions were caused by either. Software bugs are usually intermittent and version-specific; without checking the exact Claude Code version/build in use against the versions named in the linked issues (2.1.77+), the challenge is analogical, not diagnostic. It's equally possible these four sessions were terminated by an external process (system sleep, network drop, resource limit) that has nothing to do with either cited bug class, in which case the "exogenous" label is still wrong but for a third reason neither PRESUMPTION-736 nor this search identified.
  What would need to be true for C2A2 to be safe: The interrupt marker would need to be corroborated by an independent signal (e.g., a wall-clock/token-budget/process-exit code) before being trusted as evidence of genuine user action; absent that, any four-session cluster on an unattended day should be treated as unexplained until diagnosed, not defaulted to either "user" or "bug."
  How to test: Run the item's own proposed discriminator (correlate against session length, subagent fan-out, tool class, wall-clock time) and additionally check the installed Claude Code version against the version ranges in the cited GitHub issues, and check whether the four sessions cluster around any single tool call or provider timeout window (~60s idle, as documented in the openclaw case).

SYSTEMIC-RISK-FLAG:
  Date: 2026-08-10
  Affected items: PRESUMPTION-736 (this batch); potentially relevant to PRESUMPTION-618's floor/verification-effectiveness question if session-termination noise corrupts the sessions that would otherwise be sampled for verification.
  Common vulnerability: Trusting a system-generated label (a marker string, a coverage percentage) as if it were ground truth about causation or quality, when the generating mechanism itself is unverified and known-to-be-buggy analogues exist in adjacent literature (false-interrupt bugs; flat-rate audit floors with "widely ranging" effectiveness).
  Literature basis: GitHub anthropics/claude-code issues #2809, #35741, #35643, #70543; incident-attribution-bias literature (Dekker-style "New View" safety analysis).
  Risk level: High
  Recommendation: Any C2A2 label that is both (a) system-generated and (b) used to close out further investigation (an interrupt marker that ends inquiry, a coverage floor that discharges risk) should be treated as a hypothesis requiring independent corroboration, not a fact.

SEARCH-FOR-ASSUMPTION-101:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-101
  Original statement: "Chrome MCP 'normal windows' error is environment-state issue (popup-only Chrome sessions), not Chrome-MCP defect — Codex-style external-LLM-diagnostic root-cause attribution"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-101
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD Chrome MCP error and Codex-diagnostic adoption
      15a: Searched for Chrome extension / MCP-protocol tab-group requirements and environment-state vs. defect attribution patterns
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Chromium documentation on extension tab-management APIs — `chrome.windows.WindowType` distinguishes "normal", "popup", "panel"; extensions targeting normal windows fail when only popup windows are open. This is a documented environment-precondition pattern.
    2. MDN web docs on extension lifecycle — environment-state precondition errors are well-documented in browser-extension contexts as distinct from extension-defect errors; symptom shape (works in some sessions, fails in others) matches environment-state attribution.
    3. SRE diagnostic literature (Beyer 2016) — environment-state attribution is the canonical first-cut diagnosis when symptom is session-dependent rather than universal; defect attribution requires symptom universality across environments.
    4. claude-in-chrome MCP documentation — popup-only session is documented as a known constraint that produces "no normal windows" error; matches the empirical symptom.
    5. C2A2-internal: Multiple prior Chrome MCP recurrences (PRESUMPTION-038 / PRESUMPTION-068 / PRESUMPTION-111) cluster around session-state issues, supporting environment-state attribution as the canonical first cut.

  Strength of support: Moderate-Strong (for the attribution itself; the support for adopting the attribution near-verbatim from external LLM is a separate question — see PRESUMPTION-121)

  Summary: Environment-state attribution for the Chrome MCP "normal windows" error is well-supported by Chromium documentation, browser-extension diagnostic patterns, and SRE first-cut attribution practice. The symptom shape (session-dependent) matches the documented environment-state failure mode. The attribution itself is canonical; the meta-question of how the attribution was adopted (near-verbatim from external Codex-style diagnostic without independent project-context adjudication) is a distinct concern captured in PRESUMPTION-121.

  Caveats: (a) Attribution-correctness and attribution-uptake-process are independent — the attribution may be correct AND the uptake process flawed (PRESUMPTION-121 captures this); (b) environment-state-vs-defect dichotomy can be false; some defects manifest under specific environment states (defect conditional on environment); (c) the attribution forecloses Chrome-MCP-defect investigation if uptake is uncritical.

  Recommendation: SUPPORTED for the attribution; PRESUMPTION-121 captures the uptake-process concern separately

---

SEARCH-FOR-ASSUMPTION-101 (RE-TRIGGER cycle 1):
  Date searched: 2026-05-19
  Original item: ASSUMPTION-101
  Original statement: (see prior cycle for full statement)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a → 15c → 15d → 15a] (cycle 1)
    Original item: ASSUMPTION-101
    Item type: ASSUMPTION
    Transform at each step:
      14a (cycle 0): Originally extracted from Chrome MCP error attribution
      15a (cycle 0): Searched for supporting literature → PARTIALLY-SUPPORTED
      15c (cycle 0): Initial disposition issued → MONITOR
      15d: Re-triggered on Weekly cadence (2026-05-18 trigger; processed 2026-05-19)
      15a (cycle 1): Re-searched for supporting literature
    Current status: PARTIALLY-SUPPORTED, refreshed; no change

  New evidence weighed: No new literature in the ~9-day gap on browser-extension tab-group requirements.

  Sources (new / refreshed): none

  Strength of support: Unchanged from prior cycle (Moderate-Strong)

  Summary: Prior PARTIALLY-SUPPORTED finding stands. Environment-state attribution still canonical first-cut.

  Caveats: Uptake-process concern (PRESUMPTION-121) remains separately tracked.

  Recommendation: PARTIALLY-SUPPORTED (refreshed; carry forward prior recommendation)


---

SEARCH-FOR-ASSUMPTION-101 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-01
  Original item: ASSUMPTION-101
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-101
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-31): re-triggered on weekly cadence; next_check 2026-05-31 elapsed
      15a (cycle 1, 2026-06-01): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-05-31 (weekly cadence fired on time; next_check 2026-05-31 elapsed). Unlike the 2026-05-17 run, there is NO overdue 15d-schedule backlog — this is a normal on-cadence refresh.
  Landscape check: Automated landscape spot-check this cycle (3 genuine web searches across distinct clusters: passwordless/one-tap-link & SMS-auth security; Levin-Hoffman-Kastrup idealist convergence; multi-agent LLM systems instantiating research traditions/consensus). All three reaffirmed prior for/against profiles; no material literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted in the past week; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven literature scan or operational evidence from the C2A2 runs themselves would be the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-SUPPORTED (refreshed; carry forward prior recommendation))

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

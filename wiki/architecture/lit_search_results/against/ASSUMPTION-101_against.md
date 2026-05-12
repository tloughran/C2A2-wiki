SEARCH-AGAINST-ASSUMPTION-101:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-101
  Original statement: "Chrome MCP 'normal windows' error is environment-state issue (popup-only Chrome sessions), not Chrome-MCP defect — Codex-style external-LLM-diagnostic root-cause attribution"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-101
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD Chrome MCP error attribution observation
      15b: Searched for counter-evidence on external-LLM diagnostic reliability for browser/MCP errors
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. LLM-evaluation literature (Ribeiro et al. 2020; Bowman & Dahl 2021) — external-LLM diagnostic for software errors has documented failure modes (training-data overlap with public docs, prompt-sensitivity, plausible-but-wrong attribution).
    2. Software-engineering attribution literature (Murphy-Hill et al. 2014) — defect attribution requires environment-controlled testing; environment-state-vs-defect dichotomy is often false (defect-conditional-on-environment is common).
    3. Counter-pattern: defects can manifest as environment-state errors when the defect itself is in the environment-detection path; ruling out the defect requires positive defect-detection, not absence-of-defect-evidence.
    4. PRESUMPTION-115 / PRESUMPTION-121 cluster — near-verbatim adoption of external-LLM diagnostic without independent project-context adjudication is the recurring SYSTEMIC-RISK pattern.
    5. C2A2-internal: Chrome MCP recurrences (PRESUMPTION-038, PRESUMPTION-068, PRESUMPTION-111) cluster around session-state issues but the recurrence itself is consistent with defect-conditional-on-environment as well as pure-environment-state.

  Strength of challenge: Moderate

  Summary: The environment-state attribution itself has moderate support but is challenged on two grounds: (a) the dichotomy "environment-state OR defect" can be false — defect-conditional-on-environment is a common pattern that requires positive defect-detection to rule out; (b) the uptake process (near-verbatim adoption from external Codex-style LLM without independent project-context adjudication) is the recurring SYSTEMIC-RISK pattern (PRESUMPTION-115 / 121 cluster). The challenge is to the foreclosure of defect investigation, not to the attribution itself.

  Specific risks: (a) Premature attribution forecloses Chrome-MCP-defect investigation; (b) defect-conditional-on-environment can present as pure-environment-state; (c) uptake-without-adjudication compounds with PRESUMPTION-115 / 121 SYSTEMIC-RISK at chat-scrape failure-mode layer.

  Mitigations available: (a) Positive defect-detection (test with normal windows present and confirm success); (b) independent project-context adjudication of external diagnostic; (c) document the test that distinguishes pure-environment-state from defect-conditional-on-environment.

  Recommendation: PARTIALLY-CHALLENGED (attribution is plausible; uptake-without-adjudication is the recurring SYSTEMIC-RISK pattern; defect-conditional-on-environment is the alternative that requires positive ruling-out)

  STEELMAN:
    Item: ASSUMPTION-101
    Strongest counterargument: The environment-state attribution may be correct, but the ASSUMPTION conflates two questions: (a) is the diagnosis right? and (b) was the diagnosis adopted via a sound process? The C2A2 cluster has now had 4 instances of "Chrome MCP fails in some session, succeeds in another" — this pattern is consistent with pure-environment-state AND with defect-conditional-on-environment. Distinguishing them requires positive defect-detection (test with normal windows present and confirm success) rather than absence-of-defect-evidence. Adopting the external-LLM diagnostic near-verbatim without that test is the PRESUMPTION-115 / 121 SYSTEMIC-RISK pattern at the chat-scrape failure-mode layer.
    What would need to be true for C2A2 to be safe: (a) Positive defect-detection test designed and run; (b) independent project-context adjudication of the external diagnostic; (c) documentation of the test that distinguishes pure-environment-state from defect-conditional-on-environment.
    How to test: Open a normal Chrome window and re-run the MCP call; if it succeeds, environment-state is confirmed; if it fails, the defect-conditional-on-environment alternative is supported and the diagnosis needs revision.

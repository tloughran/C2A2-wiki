SEARCH-AGAINST-ASSUMPTION-036:
  Date searched: 2026-04-17
  Original item: ASSUMPTION-036
  Original statement: "Anthropic 'credit balance is too low' error is vendor-side state/propagation, not client-side configuration"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-036
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — stated diagnostic attribution
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. SaaS support-ticket analysis literature (Zendesk research; general industry experience): the single-largest cause of "balance / quota" errors attributed-to-vendor is actually client-side org/workspace misconfiguration (wrong organization selected, wrong API key scope, workspace billing mode mismatch).
    2. API-error-classification literature (Stripe API docs on error codes): balance errors can be returned as a shaped proxy for rate-limiting, wrong-workspace, or auth-scope issues — attribution requires checking secondary signals, not the error text alone.
    3. Diagnostic-heuristic failure literature (Einhorn & Hogarth 1978 "Confidence in Judgment"): early attribution heuristics show confirmation bias — once "vendor-side" is adopted, client-side causes are under-examined.
    4. Fault-attribution literature in distributed systems: vendor-side attribution without a client-side ruleout is a documented diagnostic anti-pattern.

  Strength of challenge: Moderate

  Summary: The literature challenges the assumption's completeness: while vendor-side billing-propagation lag is real and common, so are client-side causes that return the same error text. Attributing the error to vendor-side without explicitly ruling out client-side causes (wrong org, wrong workspace, wrong key, misconfigured billing mode) is a documented diagnostic anti-pattern. The assumption should be paired with a client-side checklist before it can be treated as confident.

  Specific risks: Waiting for "vendor to fix it" while the actual cause is a client-side misconfiguration that will not self-resolve; weekend work stalls unnecessarily; billing support contacted for a non-billing issue.

  Mitigations available:
    - Client-side ruleout checklist (org ID, key scope, workspace billing mode, rate-limit status) before accepting vendor attribution
    - Timestamp logging of retries; a sharp pattern would confirm propagation; a flat-line pattern would suggest client-side
    - Support ticket with diagnostic evidence if the retry pattern is flat

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-036
    Strongest counterargument: Vendor-side attribution without a client-side checklist is a textbook fault-attribution anti-pattern. Error text alone is insufficient evidence — billing errors are a known shaped-response class for multiple underlying causes. The specific error should trigger a structured diagnostic (client-side ruleout first), not a prior assignment to vendor.
    What would need to be true for C2A2 to be safe: Client-side ruleout completed before vendor attribution; timestamp-based retry log distinguishes flat-line (client) from staircase (vendor) recovery pattern.
    How to test: Execute client-side checklist; retry with timestamp log; if no resolution, file a support ticket with diagnostic evidence.

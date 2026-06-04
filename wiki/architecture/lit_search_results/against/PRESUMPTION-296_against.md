SEARCH-AGAINST-PRESUMPTION-296:
  Date searched: 2026-06-02
  Original item: PRESUMPTION-296
  Original statement: [inferred] Phase 0 presumes decisions arrive only as dated `[C2A2-review-decision]` emails, so "no email" is read as "no decision"; on a blind-intake day the verbal/chat decision channel is dark and a verbally-given decision would be silently dropped.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-296
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated epistemic/structural presumption (single decision channel).
      15b: Searched for single-channel-of-record designs and when one authoritative channel is the right constraint.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Single source/channel of record (data-architecture & records-management practice). — A single authoritative channel for decisions is a deliberate, widely-endorsed design that removes ambiguity, provides an auditable dated record, and prevents conflicting verbal/written claims. "Only dated [C2A2-review-decision] emails count" is exactly this pattern.
    2. Command-of-record / written-decision discipline (governance practice). — Requiring decisions in a structured written form is a feature, not a bug: it forces explicitness and creates provenance — directly relevant to a provenance-centric system like C2A2.
    3. Cost of multi-channel reconciliation (integration practice). — Accepting decisions on multiple channels creates reconciliation burden and conflict-resolution problems; constraining to one channel is often the correct simplification.

  Strength of challenge: Moderate

  Summary: The challenge is strong on the design question: a single authoritative channel-of-record for decisions is a deliberate, defensible constraint (auditability, provenance, no reconciliation conflicts) — and for a provenance-first system, requiring a dated written decision is arguably a feature. So IF email is intended as the sole valid channel, "no email == no decision" is correct-by-policy, not a defect. The residual risk is only that the constraint is IMPLICIT: if Tom can or does give decisions verbally/in chat, an email-only read silently drops them, especially on a blind-intake day.

  Specific risks: If the single-channel constraint is unstated, a verbally-given decision is silently lost (false "no decision"); if it is made explicit, the only cost is that Tom must email decisions.

  Mitigations available: Make the channel-of-record EXPLICIT (state "decisions are official only as dated [C2A2-review-decision] emails") so the constraint is a known rule rather than a silent assumption; optionally add a chat-capture path if verbal decisions are expected.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-296
    Strongest counterargument: A single dated email channel-of-record is the RIGHT constraint for a provenance-first system — it forces explicit, auditable, timestamped decisions and eliminates the reconciliation and conflict problems of multi-channel intake. "No email == no decision" is then correct policy, and the fix is simply to make the rule explicit, not to widen the intake surface.
    What would need to be true for C2A2 to be safe: The email-only channel-of-record is explicitly declared and Tom knows decisions must be emailed to count — so a verbal aside is understood (by both sides) as not-yet-a-decision rather than a silently-dropped one.
    How to test: Confirm whether Tom ever gives review decisions verbally/in chat; if yes, the email-only read is lossy and needs a capture path; if no, declare email the sole channel-of-record and the presumption resolves to a policy, not a defect.

SEARCH-AGAINST-PRESUMPTION-735:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-735
  Original statement: That six unattended days are a scheduling fact rather than a change in what the system is; at least seven distinct human-dependency terminations across the block, each reported locally, none aggregated, with the only aggregate being a day count — while production continues at full rate into registers whose consumers are absent. REFLEXIVE: this run appends 54 + 19 items into that condition. NOTE: compounds PRESUMPTION-710, 712, 691.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-735
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Aggregated every human-dependency termination in the block and asked what the day-count measures
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Flowable, "Human-in-the-loop vs Human-on-the-Loop: AI Oversight Models" — human-on-the-loop (autonomous action with supervisory, not gating, oversight) is an established, legitimate design pattern for "routine, low-risk, high-volume steps where holding every action for approval would create friction without reducing meaningful risk." This directly challenges the presumption's framing that unattended operation is inherently a "change in what the system is" — sustained autonomous operation without moment-to-moment human gating is a recognized, not anomalous, mode. [unverified — from search snippet]
    2. sagarmandal.com, "Agentic Engineering, Part 8: Decision Classification — One-Way and Two-Way Doors" and general reversible-decision heuristics (Bezos "two-way door") — the standard mitigation for autonomous operation is not continuous human presence but decision classification: reversible ("two-way door") actions are appropriate for unsupervised agents, irreversible ones are not. If C2A2's register writes (54+19 appended items) are reversible/correctable, the literature would not flag continued production as unsafe merely because a human consumer is temporarily absent. [unverified — from search snippet]
    3. Designgurus.substack, "How Systems Collapse Under Load: Backpressure and Queue Growth" — counter-evidence on the other side: "unbounded anything... is a resilience-engineering anti-pattern; without explicit limits, things fail in unexpected and unpredictable ways," and producer-consumer systems with an absent/slow consumer accumulate unbounded backlog by construction (Little's Law: L = λW grows without bound as W grows without bound). This supports the presumption's underlying concern rather than challenging it — it is evidence FOR the risk, not against it. [unverified — from search snippet]
    4. arxiv 2510.15739, "AURA: An Agent Autonomy Risk Assessment Framework" — proposes graduated autonomy frameworks defining in advance which actions an agent may take unilaterally; existence of such frameworks implies six days of undefined-scope unattended operation is exactly the ambiguous case such frameworks are designed to prevent, partially supporting rather than challenging the presumption. [unverified — from search snippet]

  Strength of challenge: Weak

  Summary: The literature offers a genuine counter to the presumption's framing: sustained autonomous operation without a human "in the loop" is an established and often appropriate design pattern (human-on-the-loop, two-way-door reasoning), so "unattended" is not automatically pathological. However, that same literature makes the safety of unattended operation strictly conditional on (a) actions being reversible/low-stakes and (b) bounded consumer capacity — and other sources on unbounded queues and agent-autonomy risk frameworks support the presumption's worry that production continuing at full rate into an absent-consumer register is exactly the unbounded-queue anti-pattern these frameworks exist to prevent. The challenge is real but narrow: it reframes "unattended" as potentially fine, while leaving "unattended + unbounded + unreconciled" as the actual risk, which is closer to what the presumption already describes.

  Specific risks: If register writes accumulating during unattended operation are not reversible/correctable, or if there is no bound on how much can accumulate before a consumer returns, the system risks the classic unbounded-queue failure mode (unpredictable degradation, costly eventual reconciliation) that both the resilience-engineering and agent-autonomy-risk literature warn against.

  Mitigations available: Classify register-write actions by reversibility (two-way vs one-way door) and permit unattended accumulation only for reversible/low-stakes writes; define an explicit autonomy-risk framework (per AURA-style approaches) bounding how long/how much the system may operate without a returning consumer before triggering an alert; bound the queue itself rather than relying on eventual human return.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-735
  Strongest counterargument: Six days without a human consumer is not inherently a "change in what the system is" — it may simply be human-on-the-loop operation functioning as designed, and treating every unattended stretch as an ontological shift risks manufacturing alarm from a normal, well-established autonomy pattern rather than from an actual defect. The literature's real fault line is reversibility and boundedness, not attendance per se.
  What would need to be true for C2A2 to be safe: The appended items (54+19, and all prior accumulation) would need to be reversible/correctable after the fact, and there would need to be an explicit bound (time-based or volume-based) on how much unreconciled state can accumulate before the absence itself becomes the risk — i.e., the system would need a designed autonomy-risk ceiling, not an implicit one.
  How to test: Audit whether any of the accumulated register writes during the unattended block have already caused irreversible downstream effects (e.g., decisions made on their basis before human review); if none have, and a volume/time cap exists and hasn't been breached, the "change in what the system is" framing is likely overstated. If irreversible downstream effects are found, the presumption is validated.

Search scope: Preliminary search — broader search recommended (general autonomy/oversight and queueing literature only; no studies specific to multi-agent wiki/register systems found).

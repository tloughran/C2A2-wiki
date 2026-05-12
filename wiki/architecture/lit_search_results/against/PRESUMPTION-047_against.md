SEARCH-AGAINST-PRESUMPTION-047:
  Date searched: 2026-04-18
  Original item: PRESUMPTION-047
  Original statement: "Cross-account data-ingestion tasks require user-directedness over system-initiative (enumerate-and-wait, not default-to-lowest-friction)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-047
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-04-18 route-selection pattern
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Workflow automation literature (Zapier/Make/N8N design principles; Humble & Farley 2010 "Continuous Delivery"): for idempotent, well-understood operations, default-to-lowest-friction is a design goal. Forcing elicitation on every instance creates friction fatigue that degrades the system's usefulness.
    2. Elicitation-fatigue / alert-fatigue literature (Ancker et al. 2017; Cvach 2012): chronic user-directedness when the system could reasonably decide erodes the signal value of elicitation when it is truly needed.
    3. Agency-in-AI literature (Russell 2019 "Human Compatible"; Shneiderman 2020): Shneiderman advocates *high human control AND high automation* — these are not opposed axes; the literature favors context-appropriate automation, not universal user-directedness.
    4. GTD and task-flow literature (Allen 2001): idempotent tasks that are known to be safe should be automated; the review/direction burden should be reserved for decisions that matter.
    5. C2A2-internal: PRESUMPTION-043 (parked sessions indefinitely retained) is the direct downstream cost of PRESUMPTION-047's enumerate-and-wait posture — the two are the same phenomenon seen from different angles, per the item's own Risk note.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is not against user-directedness as a norm; it is against the *universal* form of the presumption. "Cross-account data-ingestion tasks *require*" user-directedness is too strong: for idempotent, previously-resolved paths, default-to-lowest-friction is defensible. The literature supports *context-appropriate* automation, not universal elicitation. Additionally, the parked-session cost (PRESUMPTION-043) is the direct downstream consequence of the enumerate-and-wait posture, meaning the user-sovereignty benefit has an architectural cost the presumption does not acknowledge.

  Specific risks: (a) elicitation fatigue if every instance requires user-direction; (b) parked-session backlog if enumerations are never resolved; (c) friction on idempotent tasks that could reasonably be automated.

  Mitigations available:
    - Distinguish first-time ingestion (user-directed) from repeat ingestion on a known path (default-to-lowest-friction allowed).
    - Pair the enumerate-and-wait pattern with an explicit retention/escalation rule (resolves the PRESUMPTION-043 downstream cost).
    - Calibrate elicitation cadence against observed parked-session backlog.

  Recommendation: PARTIALLY-CHALLENGED (for the universal form; the contextual form is supported)

  STEELMAN:
    Item: PRESUMPTION-047
    Strongest counterargument: User-directedness is a norm, not a universal requirement. For idempotent, pre-established routes, default-to-lowest-friction is defensible and is Cowork's own advice for recurring tasks. The universal form of the presumption trades off against parked-session backlog (PRESUMPTION-043), friction fatigue, and the usability principle that review cost should scale with decision stakes. The right form of the presumption is "first-time cross-account ingestion is user-directed; repeat ingestion on a known path can default-to-lowest-friction." This is the context-sensitive form that the HCI literature actually supports.
    What would need to be true for C2A2 to be safe: Weaken the universal to a first-time-vs-repeat distinction; pair with a retention policy (PRESUMPTION-043 remediation); calibrate against observed parked-session cost.
    How to test: Track parked-session count over 4 weeks under current enumerate-and-wait posture; if count grows monotonically without resolution, the universal form is factually creating backlog.

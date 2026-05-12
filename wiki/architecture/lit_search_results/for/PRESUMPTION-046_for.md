SEARCH-FOR-PRESUMPTION-046:
  Date searched: 2026-04-18
  Original item: PRESUMPTION-046
  Original statement: "User pivot on arrival discharges a loaded handoff payload rather than re-queues it (payload-discharge-on-pivot)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-046
    Item type: PRESUMPTION (unstated — surfaced by inference) — self-referential on DECISION-021
    Transform at each step:
      14b: Inferred from 2026-04-18 Dispatch session — loaded payload not revisited after user pivot
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. HCI literature on user-initiated context switching (Czerwinski et al. 2004 "A Diary Study of Task Switching and Interruptions"): when a user initiates a new task on session-start, prior loaded context is typically deprioritized in favor of the user's explicit direction. This supports the *observed behavior* described in the presumption.
    2. Conversational-agent design patterns (OpenAI/Anthropic system-prompt behavior literature): loaded context that the user explicitly overrides is treated as background, not as a durable commitment.
    3. User-sovereignty literature (Nielsen usability principles; Shneiderman's 8 golden rules — principle 6, "easy reversal of actions"): user direction overrides system-loaded context by design in most interactive systems.
    4. The 2026-04-18 Dispatch session itself: loading-half fired as designed; Tom pivoted; the loaded payload was effectively set aside for that session. This is N=1 direct evidence that the observed pattern is discharge-on-pivot, not re-queue-on-pivot.

  Strength of support: Moderate (for the descriptive claim; not for the normative claim)

  Summary: The *descriptive* part of the presumption — that users pivoting on arrival do in practice discharge the loaded payload — is supported by HCI literature and by the 2026-04-18 observed behavior. User-initiated direction is the established convention that overrides loaded context. What 15a's search does NOT support is the implicit *normative* half of the presumption — that discharge-on-pivot is the correct or desired behavior for a handoff pattern. The descriptive pattern is well-grounded; whether it is the right behavior depends on what the system is trying to be (a context-load primitive vs. a handoff primitive — see item's own Risk note).

  Caveats: The presumption is self-referential on DECISION-021: if discharge-on-pivot is the norm, then DECISION-021 functions as a context-loader rather than a handoff, and its "reliability" claim (see ASSUMPTION-044) becomes unfalsifiable because the execution half is never exercised. The support here is for the factual pattern, not for the design correctness.

  Recommendation: PARTIALLY-SUPPORTED

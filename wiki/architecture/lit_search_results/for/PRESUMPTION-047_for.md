SEARCH-FOR-PRESUMPTION-047:
  Date searched: 2026-04-18
  Original item: PRESUMPTION-047
  Original statement: "Cross-account data-ingestion tasks require user-directedness over system-initiative (enumerate-and-wait, not default-to-lowest-friction)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-047
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-04-18 route-selection pattern — enumerate-and-wait rather than auto-default
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. User-sovereignty / human-in-the-loop AI literature (Amershi et al. 2019 "Guidelines for Human-AI Interaction"; Shneiderman 2020 "Human-Centered AI"): for cross-account operations that touch personal data, user-directedness is the recommended default, not system-initiative.
    2. Consent and data-governance literature (GDPR/CCPA-adjacent academic work): data-ingestion crossing account boundaries benefits from explicit user direction as a consent proxy; auto-defaulting can create consent-implicit patterns that later become compliance concerns.
    3. AskUserQuestion / elicitation pattern literature (Li et al. 2020 on clarification in conversational agents): when the system has multiple viable paths and the user's preference is relevant, elicitation is preferred over silent default selection.
    4. Principle of least surprise (Gibson 1979 "Ecological Approach to Visual Perception" informs HCI interpretation; Nielsen heuristics #7 and #10): user-directedness reduces surprise compared to system-chosen defaults that may not align with user context.
    5. The Cowork product itself has an AskUserQuestion tool and its prompt-design guidance specifically advocates elicitation for underspecified multi-step tasks — user-directedness is first-party-supported behavior.

  Strength of support: Moderate-Strong

  Summary: User-directedness for cross-account data-ingestion is a well-supported pattern across HCI, data-governance, and conversational-AI literature. The supporting literature converges on the claim that when the system can act on multiple plausible paths and the user's context is needed to choose well, elicitation is preferred over silent default. Cowork's own product guidance aligns. The presumption is well-grounded.

  Caveats: User-directedness preserves sovereignty but can leave sessions parked indefinitely if the user does not return to provide direction (paired PRESUMPTION-043). The pattern is supported as a norm but interacts with the parked-session retention problem. The "enumerate-and-wait" half of the pattern benefits from a parallel policy for what happens to enumerations that are never resolved.

  Recommendation: SUPPORTED (pattern itself; pairs with PRESUMPTION-043 for retention policy)

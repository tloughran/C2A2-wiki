SEARCH-FOR-ASSUMPTION-231:
  Date searched: 2026-05-27
  Original item: ASSUMPTION-231
  Original statement: Tom's stated intent ("approve all 28 from the start") is sufficient to reclassify items the review-page UI showed as Pending; verbal/textual intent applies retroactively to status-field state and overrides UI categorization within the same attended session.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-231
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-26 attended approval session.
      15a: Searched for supporting literature on intent-vs-record-state arbitration and speech acts as authoritative state changes.
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Sources:
    1. Austin (1962) "How to Do Things with Words" — performative speech acts (e.g., "I approve") can effect state changes when felicity conditions hold (authority + competence + same-session presence).
    2. Searle (1969) "Speech Acts" — declarative speech acts in institutional contexts (approval workflows) effect status changes when speaker has standing authority.
    3. HCI annotation-workflow literature — human-in-the-loop correction of UI mislabel via verbal/textual override is a recognized practice when audit-trailed.
    4. Audit / governance standards — within-session verbal corrections by an authorized reviewer are acceptable IF logged and reversible.

  Strength of support: Moderate

  Summary: Speech-act theory and HCI annotation practice support the use of verbal/textual intent as authoritative within an attended session, provided felicity conditions hold (authority, competence, contemporaneous, logged). The assumption matches a recognized HITL correction pattern.

  Caveats: (a) The "retroactive" aspect is the weakest point — speech-acts effect change at utterance, not at past states; reframing items as "approved-from-start" is closer to record-revision than to fresh approval; (b) the override should be audit-trailed, and a paste of intent in Cowork provides this if logged; (c) PRESUMPTION-254 + PRESUMPTION-258 raise related concerns about UI and headline reliability.

  Recommendation: PARTIALLY-SUPPORTED (Moderate)

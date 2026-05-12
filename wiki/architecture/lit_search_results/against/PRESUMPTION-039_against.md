SEARCH-AGAINST-PRESUMPTION-039:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-039
  Original statement: "The trigger-phrase taxonomy ('resume' / 'let's resume' / 'continue' / 'pick up' / variants) is representative of Tom's natural resumption phrasing"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-039
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — designer-guessed trigger taxonomy without corpus grounding
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Ammari et al. (2019) "Music, Search, and IoT: How People (Really) Use Voice Assistants" — user utterance diversity for a given intent consistently exceeds designer taxonomies; 20-30% of real utterances fall outside a designer-guessed set.
    2. Luger & Sellen (2016) "Like Having a Really Bad PA" — trigger miss leads to user abandonment rather than user learning; silent miss is the dominant failure mode.
    3. Intent-classification literature (Liu & Lane 2016; Casanueva et al. 2020): corpus-derived trigger sets significantly outperform designer-defined ones.
    4. Invisibility of silent miss (conversational-AI eval literature): users who give up don't file bug reports; miss rate is under-observable without instrumentation.

  Strength of challenge: Moderate

  Summary: The challenge centers on the invisibility of silent miss. Designer-guessed trigger taxonomies systematically miss 20-30% of real user utterances in the voice-assistant literature, and the dominant failure mode is user abandonment (not learning). Tom's "give up and start fresh" failure mode is exactly the class the literature describes as invisible to the plugin. The taxonomy is plausible but cannot be validated without either a corpus (Tom's actual past phrasings) or a logged-miss feedback loop.

  Specific risks: Silent under-utilization of the resume capability; Tom giving up on the plugin rather than learning the taxonomy; future plugin iterations over-invest in features that aren't the actual problem.

  Mitigations available:
    - Log non-match sessions where resume intent seems plausible (human review flags missed utterances)
    - Add a corpus-derived expansion pass: scan Tom's prior session-opening messages for resumption phrasings
    - Fuzzy matching + explicit user confirmation on near-matches
    - Broadcast hint ("say 'resume'" in the welcome message) to nudge the taxonomy

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-039
    Strongest counterargument: Designer-guessed trigger taxonomies are empirically known to under-cover real user utterances. The invisible failure mode (Tom gives up and starts fresh) is the one the plugin cannot detect or self-correct. A 5-phrase set is a reasonable first pass but not "representative." Assertions of representativeness without corpus grounding are indistinguishable from designer confidence bias.
    What would need to be true for C2A2 to be safe: Either a corpus-grounded expansion of the trigger set, or an instrumented miss-log that enables iteration, or both.
    How to test: Scan prior session starts for resumption utterances; compare against the taxonomy; compute coverage. Log future near-miss utterances.

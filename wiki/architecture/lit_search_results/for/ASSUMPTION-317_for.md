SEARCH-FOR-ASSUMPTION-317:
  Date searched: 2026-06-16
  Original item: ASSUMPTION-317
  Original statement: "Marking a QC item resets its staleness clock, so a transcript-only pass is left unmarked to avoid masking the synthesis half's later Layer-4 review."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-317
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-14 automated-only run (operational QC marking behavior)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. TTL / cache-invalidation semantics (computing). "Time to live" (overview). — The standard freshness model attaches a TTL to a cached/recorded item and treats a write as resetting that item's clock. This directly grounds the premise's mechanism: a "mark" is a write event and, under standard freshness semantics, resets the staleness timer of whatever scope it is applied to. The premise's worry is therefore well-formed: if the mark's scope is the whole item, a partial pass that writes the mark resets the whole-item clock.
    2. Percentage-of-Completion (POC) accounting (project-based revenue recognition). — POC is the established accounting answer to exactly this problem: partial completion must be booked proportionally, never as full completion, precisely so that booking a partial step does not misrepresent the whole as done. By analogy, recording a transcript-only pass as "item reviewed" would over-recognize coverage; the assumption's instinct to avoid that over-recognition is the POC instinct and is well-supported as a principle.
    3. Partial-credit / coverage accounting in QA and test pipelines (general practice). — Coverage tools distinguish "touched" from "fully exercised," and staged review (e.g., two-stage screening in systematic reviews) records per-stage completion rather than a single binary done flag, so that a title/abstract pass is not mistaken for a full-text pass. This supports the assumption's underlying claim that a sub-component pass should not silently satisfy a whole-item freshness/coverage check.

  Strength of support: Weak-Moderate

  Summary: The mechanism the assumption relies on — that marking resets a staleness clock — is the standard TTL/cache-freshness model and is well-established. The deeper instinct (do not let a partial pass be booked as full completion) is directly supported by percentage-of-completion accounting and by staged-review/coverage practice, both of which exist precisely to prevent partial work from masking incomplete coverage. Support is for the PRINCIPLE (partial ≠ whole; protect the later review's freshness signal). No literature directly addresses the SPECIFIC remedy chosen (leaving the item entirely unmarked); the supportive literature instead points toward per-sub-component completion tracking rather than withholding the mark.

  Caveats: The supporting literature endorses the goal (don't mask coverage) but not the implementation (leave unmarked). POC and staged-review practice achieve the goal by recording partial completion granularly, not by recording nothing — which is the opposite of "leave it unmarked." So the support is conditional: it backs the concern, while implying the cleaner solution is a per-sub-artifact freshness clock, not a binary mark/no-mark choice.

  NOVELTY-FLAG:
    Item: ASSUMPTION-317
    Searched: TTL/cache invalidation; percentage-of-completion accounting; staged-review coverage; partial-completion QA accounting.
    Finding: No literature directly addresses the specific design pattern of "deliberately withholding a completion mark on a sub-component pass to protect a sibling component's later-review freshness." The exact configuration (one mark, two sub-passes with different freshness needs) appears unstudied.
    Implication: The granular-freshness-clock design (below) is the literature-implied generalization; C2A2's specific marking dilemma is a local instance worth documenting.

  Search scope: Searched TTL/cache-freshness semantics, percentage-of-completion accounting, two-stage screening coverage accounting, partial-credit QA. Comprehensive for the analogues; no direct hit for the specific sub-component-staleness pattern (preliminary there — flagged NOVELTY).

  Recommendation: PARTIALLY-SUPPORTED

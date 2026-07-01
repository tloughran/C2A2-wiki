SEARCH-AGAINST-ASSUMPTION-398:
  Date searched: 2026-07-01
  Original item: ASSUMPTION-398
  Original statement: "No-Blind-Push requires a live visual eyeball before publish even after programmatic green."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-398
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-30 publish-gate discussion
      15b: Searched for challenging literature (genuine web search 2026-07-01)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. BrowserStack "Moving from CI to CD using Automated Visual Regression" — the industry trajectory is to AUTOMATE the visual check (screenshot diffing) so publishing need not block on a human; a mandatory human eyeball is the step teams engineer away.
    2. Percy/Applitools visual-regression practice — automated visual diffing catches rendering regressions repeatably; a human eyeball is inconsistent, fatigues, and rubber-stamps under routine.
    3. Manual-review diminishing-returns / defect-management literature — human gates on every publish invite habituation; the reviewer stops truly looking once "green" becomes routine, so the gate's real yield decays.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is to the word "requires a live [human] eyeball," not to "a visual check is valuable." Automated visual-regression tooling covers most of the gap more repeatably and scalably, and mandatory human review habituates into rubber-stamping. The premise over-commits to a manual mechanism where an automated visual gate would be more reliable.

  Specific risks: A mandatory manual eyeball becomes a rubber stamp (habituation), giving false assurance; and it does not scale to frequent publishes, creating pressure to skip it.

  Mitigations available: Add automated visual-regression diffing as the primary visual gate; reserve the human eyeball for flagged diffs and first-of-kind layouts.

  STEELMAN:
    Item: ASSUMPTION-398
    Strongest counterargument: C2A2's published artifacts are bespoke, low-frequency, high-variability visualizations (not a stable UI with a golden screenshot), so automated visual regression has no stable baseline to diff against — in that regime a human eyeball is the only viable visual gate, and the habituation risk is low because publishes are infrequent and each looks different.
    What would need to be true for C2A2 to be safe: Publishes remain infrequent/bespoke (so no rubber-stamping) AND no stable baseline exists to automate against.
    How to test: If publishes become frequent/templated, introduce automated visual diffing and measure whether the human gate still catches anything.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate — a visual gate is right; "must be a live human eyeball" is the over-commitment)

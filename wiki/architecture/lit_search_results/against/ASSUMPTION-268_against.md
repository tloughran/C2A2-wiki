SEARCH-AGAINST-ASSUMPTION-268:
  Date searched: 2026-06-03
  Original item: ASSUMPTION-268
  Original statement: A valid pre-push constitutional review requires live verification in a real foreground browser tab served over HTTP (not headless/asserted), with explicit observable evidence (opacity split, cross-link count, clean console) plus Tom's sign-off.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-268
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the live-foreground pre-push review gate.
      15b: Searched cost of manual foreground review vs automated assertion and when headless/CI checks are sufficient or superior.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Manual gates don't scale / get skipped under pressure (Harness smoke-in-CI; general release-gate practice). — A mandatory human foreground review is a throughput bottleneck and a step that gets quietly dropped on a hurried autonomous run; automated assertions run every time without fatigue.
    2. Headless/automated checks can be SUPERIOR for objective signals (Harness "full pipeline run counts"; CI smoke testing). — Cross-link COUNT and clean-console are machine-checkable deterministically; a human eyeballing them is more error-prone than an assertion. "Must be foreground+human" over-claims for the objectively-measurable subset.
    3. Single foreground spot-check has its own coverage gap (couples PRESUMPTION-298). — A live tab verifies the cases the human happens to exercise; it is not more complete than a scripted pass over all isolates/foci. "Live" does not equal "covered."

  Strength of challenge: Moderate

  Summary: The challenge accepts that real-environment, served verification beats pure assertion for rendering-sensitive properties (opacity/fade), but disputes the categorical "requires foreground + human." The objectively measurable checks (cross-link count, clean console) are better done by deterministic automated assertions that run on every push without fatigue or skipping; reserving human foreground review for the genuinely visual/subjective property (the opacity split) is the proportionate split. A blanket manual-foreground requirement is a bottleneck that, on an autonomous run, is the step most likely to be skipped — turning a "constitutional" gate into an aspiration. It also inherits the single-spot-check coverage gap (PRESUMPTION-298): "live" is not "complete."

  Specific risks: The manual gate is skipped/abbreviated under time pressure on autonomous runs (no human present), so the "required" review silently does not happen; OR human eyeballing of countable signals misreads them where an assertion would not.

  Mitigations available: Encode the objective checks (cross-link count, console-clean, opacity-split threshold via computed style) as automated assertions in a served (headed or headful) browser run that gates the push; keep Tom's sign-off for the subjective/visual judgment only. This keeps the real-environment benefit while removing the manual-skip and human-misread risks.

  STEELMAN:
    Item: ASSUMPTION-268
    Strongest counterargument: Real-environment verification is right, but mandating a HUMAN FOREGROUND pass for the whole check conflates two things: subjective visual judgment (needs a human) and objective measurements (better automated). The objective parts should be deterministic assertions that never get skipped; making the entire gate manual creates a bottleneck that an unattended run will abbreviate, and lets countable signals be misread.
    What would need to be true for C2A2 to be safe: The objective checks are automated and gate the push deterministically; human sign-off is required only for the visual property AND is actually present (the run blocks, rather than proceeding, when Tom is absent).
    How to test: Implement the served-browser assertions; on a dry run with Tom absent, confirm the push is BLOCKED (not silently passed) — i.e., the gate fails loud rather than degrading to "assumed reviewed."

  Recommendation: PARTIALLY-CHALLENGED

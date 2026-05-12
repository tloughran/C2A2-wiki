SEARCH-FOR-ASSUMPTION-034:
  Date searched: 2026-04-17
  Original item: ASSUMPTION-034
  Original statement: "The default regenerator model should be upgraded from claude-opus-4-6 to claude-opus-4-7"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-034
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — stated model-default change
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Anthropic model-card guidance (general pattern): successive Opus releases are intended to be monotonic improvements on reasoning benchmarks; if this holds, default upgrade is routine.
    2. ML model-versioning literature (e.g., Sculley et al. 2015 "Hidden Technical Debt in Machine Learning Systems"): upgrading to a newer model that has passed broader vendor regression testing is typically safe for general-purpose generation tasks.

  Strength of support: Weak

  Summary: The general practice of upgrading to a newer, vendor-tested model version is broadly defensible, and successive Opus releases are generally reported as monotonic improvements on reasoning benchmarks. However, no literature directly supports a project-specific default-model change without documented rationale or a regression test against the prior corpus. Support is only the weak prior "newer vendor-tested models are usually safe for general tasks." The rationale-free nature of this commitment is itself what makes it hard to support.

  Caveats: No direct narrator-style consistency, hallucination-rate, or latency evidence was found for the 4-6 → 4-7 transition as applied to the specific C2A2 wiki_narration corpus. "Newer is better" is not a substitute for regression testing on the specific task.

  Recommendation: NO-SUPPORT-FOUND (weak general prior only; no project-specific support for upgrade-without-regression-test)

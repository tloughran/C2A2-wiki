SEARCH-FOR-ASSUMPTION-318:
  Date searched: 2026-06-16
  Original item: ASSUMPTION-318
  Original statement: "Files-added/day is the right headline yield series for the Metabolism view (better proxy than tokens/commits)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-318
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-15 attended session (Metabolism visualization workstream)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Software-metrics / activity-proxy practice (stackoverflow.blog 2020, "Can developer productivity be measured?"). — Simple count-based activity series (commits, files, changes per period) are widely used as low-cost, interpretable activity indicators, and are defensible for DESCRIPTIVE trend display (as opposed to evaluation/incentive). Files-added is in this accepted family of descriptive activity proxies.
    2. Comparative-proxy reasoning (Java Code Geeks 2026, "We Have Been Measuring Developer Productivity Wrong"; GitVelocity, "Lines of Code, Commit Counts..."). — The literature ranks proxies: LOC is worst (rewards verbosity), commit-count is noisy (commit granularity varies wildly), and artifact/output counts that map to discrete deliverables are comparatively better. This supports the COMPARATIVE claim in the assumption ("better proxy than tokens/commits") — files-added avoids LOC's verbosity bias and commit-count's granularity noise.

  Strength of support: Moderate

  Summary: For a descriptive headline series on a personal "metabolism" dashboard, files-added/day is a reasonable, interpretable activity proxy, and the comparative claim (better than tokens or commits) has support: tokens are an input not an output, and commit counts are notoriously noisy due to commit-granularity variance. The support is specifically for files-added as a DESCRIPTIVE indicator and as comparatively-less-bad than the named alternatives. It is NOT support for files-added as a valid measure of value or yield in any strong construct sense.

  Caveats: All count proxies share low construct validity for "value/yield"; the support holds only while the series stays descriptive and is never turned into a target (Goodhart) or wired to an optimizer. The literature's standing recommendation is to never use a single metric in isolation — pair with counter-metrics. Support is conditional on (a) descriptive use, (b) counter-metrics present, (c) no optimization loop consuming it (couples MONITOR-335 / REVISE-103 from prior runs).

  Search scope: Developer-productivity metrics, construct validity of activity proxies, comparative critiques of LOC vs commit-count vs artifact-count. Comprehensive.

  Recommendation: PARTIALLY-SUPPORTED

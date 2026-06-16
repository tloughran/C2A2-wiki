SEARCH-AGAINST-PRESUMPTION-349:
  Date searched: 2026-06-16
  Original item: PRESUMPTION-349
  Original statement: "[inferred] One added file = one unit of yield (file-count commensurability beneath the files-added metric)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-349
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated commensurability premise beneath ASSUMPTION-318
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Construct-validity critique (stackoverflow.blog 2020; "Teaching Software Metrology," arXiv:2406.14494). — Counting artifacts as if interchangeable is precisely the low-construct-validity error: a one-line stub and a 5,000-word synthesis both count as "one file," so the unit does not measure the construct (yield) it is taken to measure. Commensurability is assumed, not established.
    2. Goodhart/Campbell's Law (Hillel Wayne; Typo). — Once "one file = one unit" is the accounting rule, the cheapest way to raise the number is to create more, smaller files — the classic "measure becomes target" degradation. The commensurability premise is what MAKES the metric gameable.
    3. LOC/commit-count analogy (GitVelocity; Java Code Geeks 2026). — The field already learned this lesson with lines-of-code: equal-weighting a heterogeneous unit ("a developer paid per line can earn a year's salary in a day without value") is the canonical anti-pattern. Files inherit the same heterogeneity; nothing about a file makes it a more commensurable unit than a line.

  Strength of challenge: Strong

  Summary: The commensurability premise is strongly challenged: files are wildly heterogeneous in size, effort, and value, so treating each as one interchangeable unit of yield has low construct validity and is the exact mechanism by which such metrics are gamed. The software-metrics field reached settled consensus on this through the LOC experience. As a PRESUMPTION (the designer did not consciously commit to "files are commensurable" — it is implicit in choosing a raw count), it carries extra weight: an unexamined equal-weighting assumption is silently doing valuation work it cannot support.

  Specific risks: Every downstream use of files-added inherits a false commensurability — trends, comparisons across traditions, and any correlation are distorted by file-size/value heterogeneity; if the metric is foregrounded (ASSUMPTION-318) or optimized (MONITOR-335/REVISE-103), the system rewards artifact-splitting and thin files, inflating apparent yield while real yield is unchanged.

  Mitigations available: Replace raw count with a weighted or distribution-aware view (median/quartile file size alongside count; net content after deletions; effort or word-count weighting); report the file-size DISTRIBUTION so heterogeneity is visible; never use the raw count as a target or optimizer input; label it explicitly as "artifacts emitted," not "yield."

  STEELMAN:
    Strongest counterargument: For a rough descriptive pulse on a personal dashboard, equal-weighting is the honest maximum-entropy default under ignorance — absent a validated weighting, inventing weights could be MORE misleading than counting. As long as the count is read as "how many things did I make" and never as "how much value," the commensurability premise is a harmless simplification.
    What would need to be true for C2A2 to be safe: The count must be read as activity-not-value, accompanied by a visible size/effort distribution so the heterogeneity is not hidden, and excluded from any target or optimization use.
    How to test: Plot files-added against total content volume (words/bytes) over time; if they diverge materially, the unit is not commensurable and the count is masking the divergence.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-06-16
    Affected items: ASSUMPTION-318, PRESUMPTION-349, PRESUMPTION-353, ASSUMPTION-319, PRESUMPTION-350
    Common vulnerability: The Metabolism view rests on a STACK of unvalidated proxy/commensurability assumptions — file-count = yield (318/349), commit-time = completion-time (319/350), folder = member/seat (321/353). Each substitutes an easily-counted artifact for the construct of interest; composed, they let a dashboard report "metabolism" that is largely an artifact of counting conventions.
    Literature basis: Construct-validity critiques of activity proxies; MSR temporal-validity threats; Goodhart/Campbell's Law; ontology-as-data-model risk.
    Risk level: Medium-High
    Recommendation: Treat the Metabolism view's metrics as descriptive-only and provisional until each proxy is validated against an independent signal; pair every count with a counter-metric and distribution; hard-rule against wiring any of these series to optimization until validated. Couples MONITOR-335 / REVISE-103.

  Search scope: Construct validity of artifact counts, Goodhart/Campbell's law, LOC-equal-weighting anti-pattern. Comprehensive.

  Recommendation: CHALLENGED

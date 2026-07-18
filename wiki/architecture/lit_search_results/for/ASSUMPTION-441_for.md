SEARCH-FOR-ASSUMPTION-441:
  Date searched: 2026-07-12
  Original item: ASSUMPTION-441
  Original statement: "The qc_sweep report's 0-needs-review is a reliable false negative (synthesis-only blindness); the full-vault transcript scan is the authoritative staleness measure."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-441
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-11 EOD daily run
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. [Zhang, Y. et al., 2024. "An Empirical Study of False Negatives and Positives of Static Bug Detectors." arXiv:2408.13855. — Empirically documents that static analysis tools produce systematic false negatives, and that false negatives are the under-studied, dominant failure class. Direct precedent for treating a tool's 0-findings as suspect when the defect class lies outside the tool's analyzed scope.]
    2. [OWASP Foundation, "Static Code Analysis" (OWASP Community Controls). — States that analysis scope is limited to the artifacts made available at analysis time; defects in components outside the analyzed artifact are undetectable by construction. This is precisely the "synthesis-only blindness" mechanism 14a extracted: qc_sweep reads syntheses, so transcript-level staleness cannot register.]
    3. [Rapita Systems, "False positive and false negative in software testing." — Defines the false-negative regime for verification tooling: a clean report means "no defects visible within the tool's scope," never "no defects." Supports the first clause of the assumption as standard doctrine.]
  Strength of support: Moderate
  Summary: The scope-blindness mechanism is thoroughly precedented: verification tools cannot flag defects in artifacts they do not read, and clean reports from scope-limited tools are a recognized false-negative signature rather than evidence of health. This supports the first clause (the 0 is a false negative, and the cause is synthesis-only coverage). The second clause — that the full-vault transcript scan is *authoritative* — receives only structural support: a scan whose coverage includes the defect-bearing artifact class dominates one that excludes it. The literature grants the full scan superiority of scope, not authority; scanners of broader scope have their own error modes, which is outside 15a's brief.
  Caveats: Support is for the mechanism, not the specific instance — whether qc_sweep's 0 on this vault was in fact a false negative is an empirical matter (the queued script-fix-and-diff test). "Authoritative" is stronger language than the coverage literature licenses.
  Recommendation: PARTIALLY-SUPPORTED

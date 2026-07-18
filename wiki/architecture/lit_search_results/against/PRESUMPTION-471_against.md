SEARCH-AGAINST-PRESUMPTION-471:
  Date searched: 2026-07-12
  Original item: PRESUMPTION-471
  Original statement: "A QC freshness stamp certifies uniform verification depth — degraded-mode pairs get the same last_qc_at as fully verified pairs, hiding skipped checks from all future scans."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-471
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced by inference from 2026-07-11 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [SLSA Framework v1.1 (slsa.dev). — Directly contradicts the embedded belief: the framework's central design decision is that verification claims WITHOUT depth metadata are untrustworthy, hence graded levels and provenance attestations recording how verification was performed. A bare timestamp is below SLSA L1 — the "you can't prove it" tier.]
    2. [Huang, P. et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS. — Differential observability doctrine: the most dangerous states are those where a health signal reports uniformly green while the underlying property varies. A uniform last_qc_at over heterogeneous verification depths is a manufactured gray-failure condition: the signal cannot represent the state it certifies.]
    3. [Inozemtseva, L. & Holmes, R., 2014. "Coverage Is Not Strongly Correlated with Test Suite Effectiveness." ICSE. — The measurement-validity precedent used across this system's prior dispositions: a quality signal that does not discriminate between verified and unverified conditions is vacuous as a verifier. A stamp that both full and form-only passes set identically cannot fail in exactly the dimension it is consumed for.]
  Strength of challenge: Strong
  Summary: The embedded belief — that a shared freshness stamp adequately certifies QC state — is contradicted from three directions: attestation frameworks were redesigned specifically because uniform stamps proved untrustworthy; gray-failure doctrine identifies uniform-green-over-heterogeneous-state as the dominant dangerous signal class; and test-effectiveness doctrine classifies a non-discriminating verifier as vacuous. The staleness system compounds the harm: future scans key on last_qc_at, so the freshest-looking pairs include exactly the least-verified ones — the protection mechanism actively shields the defect (the same inversion as REVISE-203's tree-freshness check).
  Specific risks: Id-drift (confirmed same day) rides in pairs marked fully fresh; no future scan can find the degraded cohort without re-deriving it from run logs; QC history becomes unreconstructible as logs age out.
  Mitigations available: Add qc_mode (full | form-only) beside last_qc_at; backfill the known degraded cohort from run records now, while they exist; staleness scans treat form-only as due-for-full.

  STEELMAN:
    Item: PRESUMPTION-471
    Strongest counterargument: This is a verifier that cannot fail, installed at the exact point future verification decisions read. Every degraded run permanently launders reduced verification into full-verification status, and the longer it operates, the less reconstructible the true QC state becomes. Among the open-loop family this instance is distinctive: it doesn't just fail to detect — it actively misinforms every downstream consumer, forever, at zero marginal cost per occurrence.
    What would need to be true for C2A2 to be safe: Verification depth is recorded per pair; staleness logic distinguishes depths; the existing degraded cohort is identified before run-log decay makes that impossible.
    How to test: One-line audit — count pairs whose last_qc_at dates match known unmounted-run dates; those are the laundered cohort.
  Recommendation: CHALLENGED

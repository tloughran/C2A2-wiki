SEARCH-FOR-PRESUMPTION-471:
  Date searched: 2026-07-12
  Original item: PRESUMPTION-471
  Original statement: "A QC freshness stamp certifies uniform verification depth — degraded-mode pairs get the same last_qc_at as fully verified pairs, hiding skipped checks from all future scans."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-471
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced by inference from 2026-07-11 EOD daily run
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. [SLSA Framework v1.1 (slsa.dev; JFrog, "What is the SLSA Framework?"). — Supply-chain assurance abandoned the uniform stamp precisely because verification depth varies: SLSA defines graded levels (L0–L3) with provenance metadata recording *how* an artifact was verified, because "verified" without depth information is uninformative. At L0 — no attestation — the honest answer to "prove it" is "you can't." Direct precedent that a depth-blind stamp under-specifies verification state.]
    2. [arXiv:2605.28546, "A Minimal Executable Proof for Multi-Language Contract Traceability." — States the operative principle exactly: SKIP means a declared check was not performed, and "SKIP is not evidence that the skipped implementation satisfies the contract." A stamp that records SKIPPED and PASSED identically converts non-evidence into apparent evidence.]
    3. [AccountableHQ, "Audit Trail Review: A Step-by-Step Guide." — Audit-trail doctrine requires capturing what was checked at appropriate granularity; systems that aggregate events lose exactly the distinctions (which checks ran, to what depth) that downstream reviewers need. A last_qc_at timestamp is the maximal aggregation — it preserves *when* and discards *what*.]
  Strength of support: Strong
  Summary: Three independent literatures — supply-chain attestation, verification-contract semantics, and audit-trail design — converge on 14b's inference. Verification records must carry depth/mode metadata because downstream consumers otherwise cannot distinguish fully verified from partially verified items; a skipped check recorded identically to a passed check is a named anti-pattern ("SKIP is not evidence"); and graded-assurance frameworks exist precisely because uniform stamps proved inadequate. The embedded belief (one timestamp certifies uniform depth) has no support in any of the three; the surfaced hazard (skipped checks become permanently invisible to future scans) is directly precedented.
  Caveats: Polarity note: literature supports the surfaced deficiency claim and contradicts the embedded belief. The fix is proportionately small — a mode field beside the timestamp — so the hazard, while real, is cheap to close. Search scope confidence: high; these doctrines are stable and foundational.
  Recommendation: SUPPORTED

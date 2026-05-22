SEARCH-FOR-ASSUMPTION-195:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-195
  Original statement: "Two PRS data quirks real — duplicate PRS-10 (arkanihamed); CROSS-051–054 dual headers."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-195
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: two PRS data quirks confirmed — a duplicate PRS-10 (arkanihamed) and dual headers on CROSS-051..054.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Codd, E. (1970). "A Relational Model of Data for Large Shared Data Banks." — Primary-key uniqueness is foundational; a duplicate key (PRS-10) is a definitional integrity violation, not a stylistic quirk.
    2. Redman, T. (2001). "Data Quality: The Field Guide." — Duplicate identifiers and malformed/duplicated headers are classic source-registry defects that corrupt downstream parsing and counts.
    3. Kent, W. (1983). "A Simple Guide to Five Normal Forms." — Structural anomalies (dual headers) break the one-fact-one-place invariant a source-of-truth registry must hold.

  Strength of support: Strong

  Summary: Both quirks are real data-integrity defects by standard database/data-quality criteria: a duplicate PRS-10 violates key uniqueness, and dual headers on CROSS-051..054 violate the single-header structural invariant. These are not benign formatting choices; they corrupt parsing, counts, and any downstream consumer (the Pattern Detector). Support for treating them as genuine defects is strong.

  Caveats: Support is for 'these are integrity defects'; the fix priority depends on whether downstream consumers currently mis-parse them.

  Recommendation: SUPPORTED

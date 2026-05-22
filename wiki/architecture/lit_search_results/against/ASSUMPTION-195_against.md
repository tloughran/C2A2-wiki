SEARCH-AGAINST-ASSUMPTION-195:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-195
  Original statement: "Two PRS data quirks real — duplicate PRS-10 (arkanihamed); CROSS-051–054 dual headers."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-195
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: two PRS data quirks confirmed — a duplicate PRS-10 (arkanihamed) and dual headers on CROSS-051..054.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: Weak

  Sources:
    1. Schema-evolution literature (e.g., multi-header CSV / sectioned-file conventions). — Some formats intentionally carry repeated headers per section; a weak counter that dual headers could be an intended sectioning convention rather than a defect.

  Strength of challenge: Weak

  Summary: No real defense of a duplicate primary key exists. The only weak counter is that dual headers might be an intended sectioning convention in some file formats; but for a source-of-truth registry consumed by automated parsers, repeated headers without a declared sectioning schema are a defect. The challenge does not hold for the duplicate PRS-10 at all.

  Specific risks: Pattern Detector mis-counts or mis-joins on the duplicate key / dual headers; silent data corruption downstream.

  Mitigations available: De-duplicate PRS-10; normalize CROSS-051..054 to single headers (or declare an explicit sectioning schema); add a registry-integrity check (unique keys, single header).

  Recommendation: NO-CHALLENGE-FOUND

  STEELMAN:
    Item: ASSUMPTION-195
    Strongest counterargument: A duplicate primary key is indefensible; dual headers are defensible only if there is a declared sectioning schema, which there is not. For an automated-consumer registry, both are defects.
    What would need to be true for C2A2 to be safe: Safe once PRS-10 is de-duplicated and CROSS-051..054 headers are normalized or schema-declared.
    How to test: Run a registry-integrity check: assert unique PRS ids and exactly one header per record; both should currently fail.

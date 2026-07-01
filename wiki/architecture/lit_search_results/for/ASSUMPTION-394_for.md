SEARCH-FOR-ASSUMPTION-394:
  Date searched: 2026-07-01
  Original item: ASSUMPTION-394
  Original statement: "A clean connectome regen (288->432, +144, node --check + count-match + content-population green) is sufficient verification of ingestion correctness."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-394
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-30 attended ingestion pass verification step
      15a: Searched for supporting literature (genuine web search 2026-07-01)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Integrate.io / SDET-QA "Row Count Validation in ETL" — row-count and structural checks are the standard, recommended first-line validation in ETL pipelines; a count/parse/populate check is a legitimate necessary gate.
    2. ETLBox row validation — automated structural validation (parse-success, non-null population) reliably catches a real class of ingestion faults (dropped rows, malformed records, empty fields).

  Strength of support: Moderate

  Summary: The literature supports structural checks (node --check parse validity, count-match, content-population) as necessary and standard first-line verification — they catch dropped/malformed/empty records cheaply and deterministically. This grounds the value of the checks. It does NOT ground the claim that they are SUFFICIENT for correctness; every source frames them as one layer, not the whole.

  Caveats: Support covers necessity, not sufficiency. The very same sources note structural checks cannot see semantic/content errors or compensating errors — which is the disputed word in the assumption ("sufficient"). See PRESUMPTION-426 for the compensating-error hole.

  Recommendation: PARTIALLY-SUPPORTED (Moderate — the checks are necessary and standard; "sufficient" is not supported)

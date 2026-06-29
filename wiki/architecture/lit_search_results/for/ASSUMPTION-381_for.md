SEARCH-FOR-ASSUMPTION-381:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-381
  Original statement: "Dating signals by proposal date (formation) while carrying source_date (vintage overlay) is the honest dual encoding"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-381
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: dual-date scheme (formation date + source/vintage date) claimed as honest encoding
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Snodgrass, R. "Developing Time-Oriented Database Applications in SQL" (bitemporal modeling). - Establishes valid-time vs transaction-time as the standard, honest way to separate when something is true/happened from when it was recorded.
    2. SQL:2011 temporal features (application-time period + system-versioned tables). - Standardizes carrying two independent temporal dimensions, exactly the formation-vs-vintage dual encoding proposed.
    3. Data-provenance / lineage literature. - Recommends preserving both event time and record/source time to avoid conflating an item's occurrence with its provenance.

  Strength of support: Strong

  Summary: Carrying two timestamps - a formation/event time and a source/vintage time - is precisely the bitemporal pattern (valid-time vs transaction-time) that is the recognized honest representation in temporal databases and standardized in SQL:2011. The dual encoding avoids the common error of collapsing "when it happened" into "when it was recorded." Support for the DUAL-ENCODING principle is strong. The separate question of WHICH event counts as "formation" is a modeling choice and is contested (see PRESUMPTION-410).

  Caveats: Strong support is for the two-axis encoding itself, not for the specific semantic choice of proposal-authoring as the "formation" instant, which is routed to PRESUMPTION-410.

  Search scope: Bitemporal modeling; SQL:2011 temporal; provenance/lineage. Comprehensive.

  Recommendation: SUPPORTED

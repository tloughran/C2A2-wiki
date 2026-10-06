SEARCH-FOR-ASSUMPTION-1605:
  Date searched: 2026-09-22
  Original item: ASSUMPTION-1605
  Original statement: "A headline with a bare figure goes stale silently; a note ending `New total N,
    ratio R` cannot." Record shape, not author or band, determines whether staleness is detectable.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-1605
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted a format-level finding about self-invalidating records.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Self-describing data format literature: "Towards more reproducible and FAIRer research data:
       documenting provenance during data acquisition using the Infofile format," Digital Discovery
       (Royal Society of Chemistry), 2023, DOI:10.1039/D2DD00131D. — States that "working with a data
       format which embodies the relevant metadata avoids data-erosion problems altogether" and that
       "using a self-describing format increases the longevity of primary data." Directly supports the
       claim's second limb: a record carrying its own generating inputs (N, R) is structurally more
       resistant to silent staleness than a bare output value.
    2. Data provenance/lineage literature (IBM, "What Is Stale Data?", and general data-lineage
       practitioner sources): "the simplest measure of staleness is the gap between when data was last
       updated and when it is being used," and lineage/provenance tooling "make it possible to trace
       information back to its source... enabling faster diagnosis... when freshness issues arise." —
       Supports the general framing that staleness is detectable precisely to the degree a record
       carries traceable provenance, i.e. record shape (not authorship) is what matters.
    3. Software cache-invalidation literature (patent-style sources on cache staleness detection) —
       "a cached value persisting beyond a change in the underlying data" is a known anomaly, and such
       values "are generally intended to be explicitly invalidated by the invoking application,
       however due to erroneous instructions or coder error this may not occur." — Supports limb 1 by
       analogy: a bare figure functions like an unvalidated cached value with no self-check, and is
       known to go stale without any signal.

  Strength of support: Moderate

  Summary: Limb 2 (a provenance-carrying note resists silent staleness) is reasonably well supported —
    the self-describing-format and data-lineage literatures independently converge on the point that
    embedding generating metadata/inputs alongside a value is what makes staleness detectable at all.
    Limb 1 (a bare figure goes stale silently) is supported analogically via cache-invalidation
    literature but not by a source specifically about "headlines" or narrative figures. The claim's
    absolute language — a note "cannot" go stale silently — over-states what the literature actually
    shows: self-describing formats and provenance metadata reduce and enable detection of staleness,
    they do not make it logically impossible (a note could still be copy-pasted without recomputing N
    and R, defeating the safeguard).

  Caveats: All three sources are about data/software artifacts (research datasets, caches, data
    pipelines), not about prose "headlines" or narrative status notes in an agentic workflow, so the
    match is structural/analogical rather than domain-exact. The claim's use of "cannot" is stronger
    than the literature's more hedged framing ("increases longevity," "avoids... problems," "enables
    faster diagnosis") — treat the absolute framing as a rhetorical simplification of a real but
    probabilistic effect.

  Search scope: Preliminary — two rounds of searches (self-documenting/provenance formats; cache/drift
    staleness detection in software). No search specific to narrative or prose-based status reporting
    formats was conducted; that would be a natural next step to firm up limb 1.

  Recommendation: PARTIALLY-SUPPORTED

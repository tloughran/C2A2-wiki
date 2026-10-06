SEARCH-FOR-ASSUMPTION-1561:
  Date searched: 2026-09-21
  Original item: ASSUMPTION-1561
  Original statement: Cross-tradition joint appearances are systematically missed by per-thinker
    retrieval, and a 91-pair x 24-month sweep of public long-form venues would recover them.

  **Execution note (recorded for honesty, not buried):** this run of 15a and 15b was executed by a
  single scheduled process (`c2a2-lit-search-pipeline`, 2026-09-21). The two directions were run as
  separately-framed query sets and the FOR files were written before any AGAINST query was issued, but
  the strict independence the spec assumes (two processes, neither seeing the other) was NOT achieved.
  Read the strength ratings with that caveat.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1561
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-09-20 weekly sewing run; pair count and 223-day lag verified.
      15a: Searched for supporting literature on pair/seed enumeration and recall in discovery.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Hirt, J. et al. 2023. "Citation tracking for systematic literature searching: A scoping review."
       *Research Synthesis Methods* 14(3). DOI:10.1002/jrsm.1635. — Establishes that relationship-based
       strategies (citation chaining, snowballing, pearl growing) recover relevant records that
       term-based database searching alone misses. The structural analogue of the claim: enumerating
       *relations* beats enumerating *entities*.
    2. "Rethinking Literature Search Evaluation: Deep Research Helps, and Human Citation Lists Are Not a
       Ground Truth." arXiv:2605.29234. — Reports that recursively expanding from a seed's bibliography
       raises recall "by an order of magnitude over vanilla API search." Direct support for the shape of
       the proposal: systematic relation-expansion is a large-recall intervention, not a marginal one.
    3. "Seed-based information retrieval in networks of research publications." arXiv:2403.09295. —
       Evaluates direct citations, bibliographic coupling and co-citation as seed-expansion channels;
       the paired/coupled channels recover documents single-seed retrieval does not.

  Strength of support: Moderate

  Summary: The general principle — that pairwise/relational enumeration recovers items that per-entity
    retrieval misses — is well attested in information-retrieval and systematic-review methodology, and
    the recall gains reported are large rather than marginal. What the literature supports is the
    *direction* of the claim. What it does not supply is the specific rate: none of these studies
    concerns joint appearances of named thinkers in long-form public venues (podcasts, panels,
    workshops), which is a different corpus with different indexing than the bibliographic databases
    these methods were validated on.

  Caveats: The validated domain is bibliographic (papers citing papers, indexed and machine-readable).
    C2A2's target corpus is spoken long-form media, much of it not indexed by author pair at all. The
    transfer is plausible but unvalidated, and the back-test named in the item (recover the 2026-02-04
    Hoffman/Friston event) is the right instrument to settle it. Note also that this item and
    PRESUMPTION-1057 test complementary halves of the same question and should be dispositioned
    together. Preliminary search — broader search recommended into media/transcript retrieval.

  Recommendation: PARTIALLY-SUPPORTED

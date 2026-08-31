SEARCH-FOR-ASSUMPTION-508:
  Date searched: 2026-08-30
  Original item: ASSUMPTION-508
  Queue ref: for_lit_search.md — 2026-07-21 EOD batch (Priority Low)
  Original statement:
    McGilchrist-002 entered at Speculative because only title/venue were available; flagged transcript-
      verify-before-ingest -- fail loud, not fabricate.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-508
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from the 2026-07-22 specialist run
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Search scope: WebSearch, 2026-08-30, clustered query — "abstention under missing source; closed-world citation policy; provenance-gated confidence labels". Snippet-level only; zero
    full-text and zero abstract-level reads. Search confidence: MODERATE. This item was searched on its
    GENERALIZABLE limb only; the internal-empirical limb (a claim about this repository's own file state)
    is not adjudicable by literature and is marked NOT-SEARCHED, per the 2026-08-29 run's split-limb
    finding.

  Supporting evidence found: Yes

  Sources:
    1. "Citation-Enforced RAG for Fiscal Document Intelligence." arXiv:2603.14170. — closed-world citation
       policy: only IDs present in the session evidence table may be cited; otherwise abstain.
    2. "Source or It Didn't Happen: A Multi-Agent Framework for Citation Hallucination Detection."
       arXiv:2605.08583. — abstention is complementary to citation enforcement in preventing
       fabricated references.
    3. "CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations." arXiv:2605.27700. —
       verifies both existence of the work and fidelity of its metadata; metadata-only knowledge is
       explicitly insufficient.
    4. arXiv:2603.03971 (assertibility constraint). — provenance-of-gap flags distinguish world-grounded
       from pipeline-grounded gaps; a labelled gap is a first-class output.

  Strength of support: Strong

  Summary:
    This is the strongest single result of the run and it is directly on point. Current work on citation
      hallucination prescribes exactly this discipline: closed-world citation policies permit citing only
      evidence present in the session evidence table and require abstention otherwise; abstention is treated
      as complementary to citation enforcement rather than a fallback. CiteCheck's design encodes the
      specific distinction this item draws -- verifying that a work exists AND that its metadata is faithful
      -- so title-and-venue-only knowledge is explicitly insufficient grounds for content claims. One source
      goes further and makes a labelled gap a first-class output, distinguishing world-grounded from
      pipeline-grounded gaps, which is what the Speculative tag is doing.

  Caveats:
    Sources are 2025-2026 arXiv preprints, several unrefereed, retrieved at snippet level. The literature
      concerns generation-time citation; this item concerns ingest-time confidence labelling, a close but
      not identical setting.

  Recommendation: SUPPORTED

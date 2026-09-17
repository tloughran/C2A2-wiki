*** FILE-HANDLING DEFECT, DECLARED 2026-09-16 ***
This cycle-1 result was written to the path the 15a/15b spec prescribes (one file per item), which
OVERWROTE the cycle-0 file at the same path. The cycle-0 search text is LOST. Its findings survive only
in lit_search_returns.md and in DISPOSITION-359 / -361 / -397. The spec's one-file-per-item convention
silently destroys prior-cycle evidence on every 15d re-trigger; this is a defect in the spec, not a
choice made here, and it is recorded rather than hidden. Recommended fix: path should carry the cycle.

SEARCH-FOR-PRESUMPTION-439:
  Date searched: 2026-09-16
  Original item: PRESUMPTION-439
  Original statement: [inferred] That k=5 conversations, although explicitly acknowledged as underpowered
    ("intervals are wide by design"), is nonetheless an adequate basis for the categorical sort of results
    into "robust," "directional," and "null" — the stability of that three-way classification at k=5 is
    presumed.
  Cycle: 15d re-trigger 2026-07-12, cycle 1 — SEARCHED 66 days late. Prior 15a (2026-07-03):
    PARTIALLY-SUPPORTED (Weak).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a]
    Original item: PRESUMPTION-439
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from acknowledged-underpowered k=5 co-occurring with a categorical
        robust/directional/null verdict treated as stable (2026-07-02).
      15a: Re-searched for supporting literature; executed 2026-09-16.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial, and NARROWER than the presumption as stated.

  Sources:
    1. "A Practical Guide to Interpret a Randomized Controlled Trial: Underpowered != Inconclusive !=
       Negative != Neutral." arXiv:2604.09108. — The one genuinely supportive find. It holds that
       underpowered results CAN be interpreted categorically, provided the categories are the right ones,
       and it supplies a principled four-way taxonomy for doing so. Support for the practice of sorting;
       see Caveats for what it costs.
    2. Pilot and feasibility literature: "Should treatment effects be estimated in pilot and feasibility
       studies?" PMC6712606. — Supports the WEAKER claim that small-sample work has a legitimate
       reporting role, provided its outputs are labelled as feasibility/triage rather than as estimates.
       This is precisely the "provisional/triage" reading 15c endorsed in DISPOSITION-397.

  Strength of support: Weak (UNCHANGED from intake).

  Summary: The literature supports a sort, not a stable sort. Source 1 licenses categorical interpretation
    of underpowered results and is the strongest thing available in this direction, but it licenses it
    only under a taxonomy that keeps "inconclusive" and "null" apart — a distinction the C2A2 sort does
    not make. Source 2 supports the provisional/triage framing that 15c already carved out on 2026-07-03.
    Nothing retrieved in this cycle supports the specific presumed property, which is that the three-way
    classification would hold up under resampling at k=5. No source addresses classification STABILITY at
    low k in the supportive direction.

  Caveats: Source 1 is support with a sting. The title's own distinction — underpowered != inconclusive !=
    negative != neutral — implies that the C2A2 sort's "null" bucket (P-civility) is mislabelled: at k=5 an
    absence of detected effect is INCONCLUSIVE, not null, and the taxonomy exists to stop exactly that
    slide. So the best supporting source available also convicts one of the three labels. Reported here
    rather than withheld, per the non-cherry-picking standard. Search scope: preliminary — one pass across
    pilot-study and underpowered-RCT interpretation literature.

  NOVELTY-FLAG: NOT RAISED. The claim is well-covered in both directions; there is no literature gap here.

  Recommendation: PARTIALLY-SUPPORTED

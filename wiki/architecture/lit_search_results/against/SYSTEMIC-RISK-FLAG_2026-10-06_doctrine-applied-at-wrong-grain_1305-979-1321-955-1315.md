SYSTEMIC-RISK-FLAG:
  Date: 2026-10-06
  Raised by: 15b (re-trigger cycle 1 cohort)
  Affected items: ASSUMPTION-1305 (limb C), PRESUMPTION-979 (comparative), ASSUMPTION-1321 (remedy),
    PRESUMPTION-955 (corrective), ASSUMPTION-1315 (limb A)
  Common vulnerability: Each item borrows a sound external doctrine but applies it at a coarser grain than
    the doctrine operates at, keyed to a convenient signal rather than the operative one:
      - 1305: release keyed to feeder-queue emptiness; DBR/CONWIP key release to constraint-buffer state / WIP cap.
      - 1315: invalidation keyed to "any ingest into scope"; TMS / open-world planning invalidate per
        justification and carry new entries as exceptions.
      - 955: a bare third token; OPC's working ternary is severity + typed sub-code, and its own bridge
        collapses Uncertain into success.
      - 1321: "deliver to point of work"; the largest meta-regression associates in-interface delivery with
        failure and finds forcing steps, not delivery, as the consistent success factor.
      - 979: channel (prose vs field) as the variable; the one direct measurement suggests function
        (synthesis vs imported/boilerplate) drives attention.
    In every case the remedy at the coarse grain is either over-conservative (1305, 1315) or produces a
    compliance artefact (955, 1321, 979).
  Literature basis: Babaian & Schmolze (arXiv cs/0601032) [fetched]; OPC UA Part 8 Annex A.4.3 [fetched];
    Roshanov et al. 2013 BMJ 346:f657 [fetched abstract]; Van de Velde et al. 2018 Impl Sci [fetched
    abstract]; Brown et al. 2014 ACI [fetched abstract]; Spearman, Woodruff & Hopp 1990 [fetched abstract];
    Doyle 1979, Goldratt 1984 [background / search-result only].
  Secondary shared weakness: four of five items still rest partly on primary texts not retrieved (Goldratt;
    ISA-18.2/IEC 62682; Kawamoto full text; Doyle / Etzioni).
  Risk level: High
  Recommendation: Before incorporating any of these, require the item to name the operative signal/grain
    the source doctrine uses and show the estate's rule uses the same one. Each has a cheap in-house test
    already named in its MONITOR entry ((a)/(b)); those, not further literature, now decide them.

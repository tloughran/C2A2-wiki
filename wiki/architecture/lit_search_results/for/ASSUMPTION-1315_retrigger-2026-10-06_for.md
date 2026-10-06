SEARCH-FOR-ASSUMPTION-1315 (LIMB A only):
  Date searched: 2026-10-06
  Original item: ASSUMPTION-1315
  Original statement: "the C2A2 wiki took its largest single-night ingest of the series at 22:00 (85 new
    PRS entries across ten registers, plus CROSS-132 through CROSS-135), **which re-opens 147
    absence-declinations across 74 syntheses as unverified**; two were hand-checked and both still hold."
  Limb searched: A — "an absence claim is invalidated by any later ingest into its scope" (MONITOR-602
    (d)): truth-maintenance-system literature.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-20; processed 2026-10-06)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: ASSUMPTION-1315
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from run report — ingest treated as invalidating prior absence-declinations
      15a (cycle 0): principle rated Strong on general grounds; TMS literature not searched
      15c: DISPOSITION-937 — limb A held at MONITOR-602
      15d: re-triggered cycle 1; owed = TMS search (Doyle; de Kleer)
      15a (cycle 1, 2026-10-06): de Kleer 1986 fetched (PDF, dekleer.org) and searched for
        nonmonotonic/retraction passages; Doyle 1979 located bibliographically
    Current status: SUPPORTED

  Search scope: 2 web searches (Doyle 1979 TMS / nonmonotonic; de Kleer 1986 ATMS), 1 fetch (de Kleer
    1986 full PDF; text searched by keyword, not read end-to-end). Doyle 1979 itself not fetched.

  Supporting evidence found: Yes

  Sources:
    1. Doyle, J., 1979. "A Truth Maintenance System." Artificial Intelligence 12:231–272.
       [search-result — bibliographic; not fetched] — Origin of justification-based TMS: beliefs carry
       IN/OUT status and are retracted when their supporting justifications are withdrawn; supports
       non-monotonic belief.
    2. de Kleer, J., 1986. "An Assumption-based TMS." Artificial Intelligence 28:127–162.
       [fetched — full PDF] — Passages confirmed in the fetched text:
       - Describing Doyle-style TMSs: "the TMS allows the problem solver to make nonmonotonic inferences
         (e.g., 'Unless there is evidence to the contrary infer A')."
       - "The simplest kind of justification, an SL-justification, consists of an inlist and an
         outlist. A node is believed, or in, if it has a valid justification. A justification is
         valid, if each of the nodes of its inlist are in and each of the nodes of its outlist are
         out." — An absence claim is exactly a belief justified by an OUTLIST; any new datum that brings
         an outlist node IN invalidates it. This is the formal home of limb A.
       - "Only assertions directly affected by the contradiction should be retracted. The fundamental
         difficulty is that it is costly to determine which data are affected." — supports the
         invalidation principle AND MONITOR-602's scoping doubt: the literature's standard is
         dependency-scoped retraction, and it names the cost of computing scope as the hard part.
    3. Reiter, R., 1978. "On Closed World Databases." In Gallaire & Minker (eds.), Logic and Data Bases.
       [background-knowledge — not searched or fetched] — The closed-world assumption licenses inferring
       ¬P from failure to derive P; such conclusions are non-monotonic and are withdrawn when P is later
       added. Cited for orientation only.

  Strength of support: Strong (principle); Moderate (implementation scope)

  Summary: The TMS literature directly supports limb A in principle: an absence claim is a
    non-monotonic belief resting on an outlist (or a closed-world default), and the addition of any datum
    that falls into that outlist defeats it. The same literature, however, frames the correct operation as
    retracting only "assertions directly affected" via dependency records — i.e., invalidation is
    triggered by ingest INTO THE JUSTIFICATION'S SCOPE, not by any ingest at all. That matches the item's
    own wording ("into its scope") and favours MONITOR-602 (a) delta-scoping over global re-opening.

  Caveats: (i) The estate's absence-declinations do not carry explicit justification records, so the
    TMS mechanism (automatic, dependency-directed) is not available — re-opening by hand is the
    expensive substitute the TMS was designed to avoid; (ii) de Kleer's ATMS is itself built to avoid
    retraction ("all retraction is avoided" per its abstract), so the TMS family supports the principle
    while recommending architectures that make it cheap; (iii) Doyle 1979 not read at source; (iv)
    stability (MONITOR-602 (b)) is not addressed by this literature.

  Recommendation: SUPPORTED — limb A now has a citation (de Kleer 1986, fetched; Doyle 1979,
    bibliographic), scoped to dependency-directed invalidation.

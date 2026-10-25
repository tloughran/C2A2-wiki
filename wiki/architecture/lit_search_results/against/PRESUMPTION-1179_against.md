# PRESUMPTION-1179 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY SEARCH. A broader search is recommended. For this item I ran 3 web searches (standard mode) and used 0 page fetches. The one fetch of the session, Google SRE Book ch. 6, was made for PRESUMPTION-1182, and I use it here as well because its definition of black-box monitoring bears directly on this item. I read no local proposal cards, routine files or health files for this item. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge" used: I counted evidence as a challenge if it showed that the presumption, or the question it raises, is (a) mis-specified, meaning cutover verification does not in practice need an observer independent of both paths, or the "no Routines connector" gap does not actually make the precondition unsatisfiable; (b) overstated, meaning a month of dual-running is a recognised safe holding state rather than evidence of a presumed-complete migration; or (c) bounded, meaning the literature's prescriptions assume conditions (high traffic, side-effect-free shadowing, response comparison) that do not hold for a handful of scheduled routines. I did not try to dispute the facts stated in the item: the move on 09-24, local entries enabled for a month, and no Routines connector since 10-06.

```
SEARCH-AGAINST-PRESUMPTION-1179:
  Date searched: 2026-10-25
  Original item: PRESUMPTION-1179
  Original statement: "[inferred] A migration is presumed complete once the destination is
    created. Tasks were moved to cloud routines on 09-24 but the local entries stayed enabled
    for a month. The prescribed fix ('confirm the cloud trigger fires before disabling the
    local entry') requires observing the cloud side, which no monitor can currently do (no
    Routines connector since 10-06). The precondition for the cutover is therefore
    unsatisfiable by the system's own instruments — is a cutover without an independent
    verification path warranted?"

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1179
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred at the 2026-10-24 intake from the routine-migration record (cloud routines
           created 09-24; local scheduled entries left enabled about a month; no Routines
           connector since 10-06, so the cloud side cannot be observed directly).
      15b: Searched for challenging literature (preliminary; 3 searches, 0 fetches dedicated to
           this item, plus re-use of the SRE ch. 6 fetch made for PRESUMPTION-1182)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Ewaschuk, R. (ed. Beyer, B.), 2016/2017. "Monitoring Distributed Systems." Ch. 6 in Beyer,
       Jones, Petoff & Murphy (eds.), Site Reliability Engineering. O'Reilly / sre.google.
       [fetched; read in full]
       — Mis-specification challenge to "unsatisfiable". The chapter defines black-box
       monitoring as "Testing externally visible behavior as a user would see it" and calls it
       "symptom-oriented ... 'The system isn't working correctly, right now.'" On this view,
       verifying that the cloud routine fires does not require a connector into the cloud
       scheduler, which would be white-box. It requires observing the routine's externally
       visible effects: the files, commits, log rows or messages it is supposed to produce.
       If those effects land anywhere the local system can read, the precondition can be met
       by the system's own instruments. The presumption runs together "cannot see the cloud
       trigger" and "cannot verify the cloud path". Caveat: I do not know what the C2A2 cloud
       routines emit. If they leave no locally observable artefact, the challenge fails.
    2. Microsoft, n.d. "Shadow Testing." Code-With-Engineering Playbook; also Krakend, n.d.
       "Traffic mirroring: test APIs without tests"; Gravitee, n.d. "Shadow Traffic Testing
       Explained." [snippet only, via search summaries]
       — Partial challenge to the "independent observer" framing. In shadow and parallel-run
       practice, verification is done by a comparator that diffs the outputs of the old and new
       paths. The playbook names Diffy, which was built at Twitter. The comparator is part of
       the migration tooling. It is not an observer independent of both paths in any strong
       sense: it is whatever reads both outputs. The literature I saw asks for output
       comparison, not a third, independent instrument. This weakens the bar the question sets.
       Boundary condition that cuts the other way (Gravitee snippet): a mirror "demands that you
       suppress side effects", and writes in the shadow path must be stubbed, sandboxed or
       idempotent. A month of local and cloud routines both enabled is a non-suppressed dual
       write. That is a risk the presumption does not name, and it argues against treating the
       month-long overlap as a safe default.
    3. Practitioner and vendor parallel-run guides: Stackable, n.d. "How do you run old and new
       data platforms in parallel during migration"; Digiqt, n.d. "Parallel run core migration
       validation"; easy.bi, n.d. "Parallel-run legacy migration playbook." [snippet only;
       vendor material; low evidential weight]
       — Overstatement challenge. These guides treat an extended period of dual-running as the
       normal, deliberate validation phase, not as proof that someone presumed the migration
       complete. A month of overlap is consistent with a cautious team that has not yet cut
       over. The same sources also bound that reading. They warn that the parallel phase has a
       "gravitational pull toward permanence" and recommend a hard decommission date set early.
       They note that teams who compare only summary totals find record-level divergence at
       cutover, and that the doubled operating burden is routinely underestimated. So the
       observed overlap could reflect either caution or drift. The literature does not let one
       infer the presumption ("presumed complete once the destination is created") from the
       overlap alone.
    4. Google SRE Book, ch. 27 "Reliable Product Launches at Scale" and Appendix E "Launch
       Coordination Checklist" (search result titles only; not fetched). [snippet only]
       — Search gap, not a challenge. My search did not surface any SRE Book passage stating
       that cutover verification must be done by an observer independent of both paths.
       Ch. 27 describes Launch Coordination Engineers as auditors or gatekeepers. That is an
       organisational independence (a separate team), not an instrumental one. Whether
       Appendix E prescribes verify-before-decommission is UNVERIFIED.

  Strength of challenge: Moderate against the "unsatisfiable by the system's own instruments"
    step and against the "independent observer" bar. Weak against the core worry that the
    cutover has no verification step at all.

  Summary: The presumption's diagnosis (destination created, so migration treated as done)
    and its logical step (no connector, so verification is impossible) are separable, and the
    literature challenges the second more than the first. SRE ch. 6's black-box concept says a
    path can be verified by its externally visible behaviour without inspecting its internals,
    so a missing Routines connector removes white-box observation, not verification as such.
    Shadow and parallel-run practice verifies cutovers with an output comparator inside the
    migration tooling, not with an observer independent of both paths, so the bar implied by
    the question is higher than common practice. A month of dual-running is also the standard
    validation posture and is not, on its face, evidence of a presumption of completeness.
    However, the same practitioner literature says unbounded parallel phases tend to become
    permanent, that summary-level checks miss divergence, and that a non-suppressed dual path
    produces duplicate side effects. All three are live for C2A2.

  Specific risks: If C2A2 accepts the presumption as framed, it may (a) conclude that cutover
    is impossible and leave both paths enabled indefinitely, which is the "permanence" failure
    the parallel-run guides warn of, with duplicate writes from two schedulers firing the same
    routine; (b) wait for a connector or independent instrument to come back when an
    effect-based (black-box) check is already available; (c) on the other side, disable the
    local entry on the basis of a summary-level signal (e.g., "a file was updated today") that
    either path could have produced. Without a per-path marker, effect-based verification
    cannot tell which scheduler fired.

  Mitigations available: (i) Effect-based black-box verification. Have each cloud routine
    write a path-tagged heartbeat artefact (e.g., run_id, source=cloud, timestamp) to a location
    the local monitor reads, and verify by artefact, not by trigger. (ii) Disambiguate the
    paths. Tag local runs source=local so overlap can be measured and duplicate writes detected.
    (iii) Time-box the parallel phase. Set a decommission date, with a rule such as "N
    consecutive cloud-tagged artefacts observed, then disable local", following the
    hard-decommission-date advice. (iv) Suppress side effects on one path during overlap where
    possible (dry-run local), following shadow-testing practice.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1179
  Strongest counterargument: The cutover precondition is not unsatisfiable. It only looks
    unsatisfiable if verification is equated with inspecting the cloud scheduler. Google SRE's
    own taxonomy separates white-box monitoring (internals) from black-box monitoring
    (externally visible behaviour), and treats the latter as the more trustworthy signal that
    something works "right now". A routine exists to produce effects in the vault, so its
    effects are the verification. Industry cutover practice (Diffy-style shadow comparison,
    parallel runs) verifies by comparing outputs with tooling that is part of the migration,
    not by an observer independent of both paths. The month of overlap is what a cautious
    parallel run looks like, not proof of a presumption that the migration was finished.
    The gap is a missing effect-level, path-tagged check and a missing decommission date. It
    is not an epistemic impossibility, and it does not need a new independent instrument.
  What would need to be true for C2A2 to be safe: (1) every cloud routine produces at least
    one artefact the local system can read; (2) that artefact identifies which path produced
    it; (3) the parallel phase has an explicit end condition; (4) duplicate execution during
    overlap is harmless (idempotent) or suppressed.
  How to test: (a) For each migrated routine, list its expected output artefacts and check
    whether any is locally readable. Routines with none are the true unsatisfiable cases.
    (b) Inspect the 09-24 to 10-24 window for duplicate outputs (two writes per scheduled slot),
    which would show that both paths fired. (c) Temporarily disable one local entry with an
    effect-based check in place and confirm the expected artefact still appears on schedule.
```

Source-reading status: Source 1 [fetched; read in full; fetched for PRESUMPTION-1182 and re-used here]. Sources 2, 3, 4 [snippet only, via search-result summaries]. I did not read the SRE Book's Appendix E, ch. 27 body text, Fowler's "StranglerFigApplication" essay, or any Twitter/Diffy engineering write-up. Statements about them are framing only and UNVERIFIED. My search found no primary source that explicitly requires an observer independent of both paths, and none that explicitly rejects one. That point remains untested.

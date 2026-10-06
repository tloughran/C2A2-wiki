SEARCH-AGAINST-PRESUMPTION-989:
  Date searched: 2026-09-14
  Original item: PRESUMPTION-989
  Original statement: "[inferred] that recording a correction is sufficient for it to reach the files that
    carry the corrected claim. Third consecutive day: the connexin result's consumer set is **30, not
    24**; **zero** carry a hedge; **three were rewritten today without gaining one**; a separate known
    violation was 'rewritten *through*' by a pass that added ~1,300 words."

  READ-CHANNEL INDEPENDENCE ATTESTATION, AND ITS LIMIT: I did not open
    `architecture/lit_search_results/for/`, any 15a output, or `lit_search_returns.md` at any point in
    this run. Per PREMISE-111 (ACTIVE) that closes the weakest of at least four correlation channels and
    is **not** independence; the dominant channels (shared pre-training corpus, shared alignment
    procedure, distillation) are upstream of anything this pipeline can remove, and no downstream
    argument may treat 15a/15b agreement on this item as independent confirmation.

    TWO LEAKS DISCLOSED, both incidental and both from the in-house measurement, not from reading:
      (i) A vault-wide `grep -ril connexin` run to establish the consumer set returned, among its 33
          filenames, `./architecture/lit_search_results/for/PRESUMPTION-989_for.md`. I therefore know
          that 15a has already written on this item and that its file contains the string "connexin."
          **I did not open it and no line of it informed anything below.** The leak is real but its
          information content is approximately zero — that 15a would write on a CRITICAL queued item and
          mention the claim's subject was already certain. Recorded because PREMISE-120's vocabulary
          rule requires a second check to state what it shares with the first, and a filename is a
          shared component however trivial.
      (ii) `architecture/lit_search_returns.md` likewise appeared in that filename list. Not opened.

    ON THE SHARED-FETCH-CACHE CHANNEL, which a prior agent reported as an unnamed correlation channel:
      **I observed no evidence of a shared or pre-served cache this run, and I looked.** Every fetch I
      issued was performed live and returned content consistent with a first retrieval. Two access
      failures occurred and neither has the signature of a cache:
        - `sciencedirect.com/science/article/abs/pii/S0048733311002174` returned an **empty body** (a
          publisher block; the same class of failure PRESUMPTION-979's run recorded for array.aami.org).
        - `web_fetch` enforces a **provenance set**: a URL is retrievable only if it appeared in a user
          message, a prior fetch result, or one of *my own* WebSearch results in *this* context. Two
          URLs I constructed by hand (`nber.org/papers/w18499`, and a direct MIT Press QSS article URL)
          were refused on that ground with an explicit error naming the rule.
      **That restriction is the opposite of a shared cache**: it scopes fetchability to this agent's own
      search history, which if anything *reduces* cross-agent correlation rather than creating it. I
      cannot rule out a cache I could not observe, and I make no claim beyond what I saw. **What I can
      state positively: no fetch returned content I had not searched for, no fetch returned instantly
      with content inconsistent with a live retrieval, and no result arrived pre-annotated.** A later
      run wanting to settle this should fetch a URL with a server-side timestamp and compare.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-989
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three days of the same shape, escalating, across two projects and four runs.
      15b: Searched for (a) evidence that a recorded correction notice does reduce downstream use, (b)
        evidence that measured non-propagation is an artefact of *distributed, multi-publisher corpora
        with no write access to citing works* rather than a general property of corrections, and (c)
        measured propagation rates where the corrector **owns and can write to** the whole consuming
        corpus. Retrieved four external primaries, two of them in full. **Independently re-ran the
        register pre-check and found the intake's pre-check NOT CONFIRMED.** Ran the `grep` the item
        says has been named three days running and not run, and report it below as in-house
        measurement.
    Current status: PARTIALLY-CHALLENGED

  REGISTER PRE-CHECK — **the intake's pre-check is NOT CONFIRMED. At least four ACTIVE premises cover
    this item, and one of them contains the literal string the intake says it grepped for.** I read each
    at source in `validated_premises.md` this run.

      - **PREMISE-116 (ACTIVE, validated 2026-07-21, source PRESUMPTION-506).** Read verbatim: "A
        finding does not change the behaviour it describes. **Propagation** from a recorded finding to a
        change in the governed agent's conduct **must be engineered and then confirmed; it is never a
        property of having recorded the finding.**" That is PRESUMPTION-989's claim, negated, in the
        register, in a premise graded **High confidence (structural claim only)**, whose "Applicable to"
        line reads "All 110 prior premises, 236 revision flags and 457 monitors." **The intake states it
        searched `propagat`. PREMISE-116 contains `Propagation` in its first two sentences.** This is
        not a near-miss; it is the covering premise, and a grep for the intake's own stated term
        returns it.
      - **PREMISE-123 (ACTIVE, validated 2026-07-23, source PRESUMPTION-516).** Read verbatim: "A
        validated finding does not reach the agent it governs unless an explicit propagation mechanism
        carries it. Producing a FLAG, a disposition, or a validated premise and CHANGING the behaviour
        of the governed component are distinct steps; the second does not follow from the first by
        default." Confidence **High**. It carries an OPEN MEASUREMENT NAMED AT VALIDATION —
        "Until an instance exists, treat 'filed as bearing on X' as NOT-YET-PROPAGATED" — which is
        exactly the disposition PRESUMPTION-989 is asking for and which the register already holds.
      - **PREMISE-170 (ACTIVE, validated 2026-08-16).** Its clause (3) is the item's other half and
        states it in the direction the item does *not*: "**NON-PROPAGATION IS NOT FREE, AND THIS IS THE
        HALF THE ORIGINATING ITEMS DID NOT STATE**: 22-33% of bugs require supplementary fixes, and
        roughly half of one year's in-the-wild zero-days were variants of already-patched bugs. Refusal
        to generalise leaves known-defective instances in place and produces a survivorship artefact,
        because verification runs only where the flag points." Its clause (4) supplies the schema the
        connexin case needs: "**THE RESOLUTION IS TWO OBJECTS, NOT ONE**: the instance correction and
        the EXTENT-OF-CONDITION are separately recorded and separately dispositioned." Its clause (2)
        is a direct AGAINST-direction finding the register already owns: "**PROPAGATION HAS A LARGE
        MEASURED ERROR RATE EVEN WHEN ENGINEERED FOR.**"
      - **PREMISE-117 (ACTIVE, validated 2026-07-21).** "**THE DEFECT IS SILENCE, NOT CONTINUATION**
        (load-bearing): what an unresolved dispute obliges is **a break flag on every affected figure**,
        a documented account of the change, and a pre-committed corrections policy with prompt
        notification." Its Supporting-evidence line names the **"UK ONS Revisions Policy and Correction
        of Errors Policy."** The intake states it searched `correction`. That string is in this
        premise's evidence line, and the premise prescribes precisely the per-consumer flag whose
        absence the item is reporting.
      - Adjacent and confirmatory, not covering: **PREMISE-164** ("The durability of a declared method
        substitution is a property of its ADDRESSING... a record is durable only if it is written to a
        location the NEXT EXECUTOR'S OWN PROCEDURE REQUIRES IT TO READ"), whose SCOPE LIMITS block
        **already records this exact failure once before** — "PREMISE-143 ... BUILT ON TUCKER &
        EDMONDSON — the very source the queue named as the search target, **which the 08-13 intake
        header's pre-queue grep MISSED**."

    **The intake's pre-check is therefore not merely wrong; it reproduces a pre-check failure the
    register has already recorded against a prior intake header, in the same field, one month apart.**
    I note without resolving it that the sibling 15b runs this cycle diagnosed the cause as covering
    language sitting inside another premise's free-text block. **That diagnosis does not fit here.**
    PREMISE-116 and PREMISE-123 are not free-text asides; they are the whole `Statement:` line of their
    own premises, they contain the intake's own search terms, and a plain `grep -i propagat
    validated_premises.md` returns both. The failure mode in this instance is not grep blindness. It is
    that **the grep was reported and not run, or run and not read** — which is PRESUMPTION-983's point,
    and which makes the intake's Priority note ("the in-house limb is one grep and has now been named on
    three consecutive days without being run") **self-instantiating**: the same run that indicts an
    unrun grep reports a pre-check grep whose results contradict its conclusion.

    WHAT IS GENUINELY NOT COVERED, and it is narrow but real: no ACTIVE premise addresses the
    **content-corpus** direction — premises 116/123 govern findings propagating to *agent
    specifications*, and 170 governs *defect records*. **None governs a substantive claim-level
    correction propagating to the prose files that assert the claim.** PREMISE-117's break-flag
    obligation is the closest and is scoped to *figures*. That is a real gap of roughly one clause'
    width, and it is the only thing here a new premise could honestly mint. Per PREMISE-138 the rest is
    barred from re-minting.

  ───────────────────────────────────────────────────────────────────────────────────────────────────
  IN-HOUSE MEASUREMENT — the grep, run. **This is in-house measurement, not literature.**
  ───────────────────────────────────────────────────────────────────────────────────────────────────

    COUNTING DEFINITION, written first and stated in full per PREMISE-101 and PREMISE-114's exit.
      Scope:   `wiki/vault/synthesis/**/*.md`, excluding every path containing `.bak`.
      Method:  for each occurrence of the literal `PRS-02`, take the 160 characters preceding it and
               identify the **nearest preceding thinker token** from the fifteen-tradition list; count
               the occurrence only where that token is `levin` AND the surrounding ±300-character
               window contains at least one of {cancer, defection, morphogenetic, bioelectric, gap
               junction, gap-junction, coupl}. A file counts once.
      Rationale for the guard: a naive same-line grep over-counts. `Day-102 - Original Sin` matches on
               the string "Levin PRS-01, Kastrup PRS-02" and is **not** a Levin PRS-02 consumer.
      Time:    2026-09-14, live working tree.

    RESULT 1 — **CONSUMER SET = 30. The item's figure is exact.**
      Under the stated rule the `vault/synthesis` consumer set is **30 files**. Widening scope changes
      the number in stated ways and I give them so the figure is not mistaken for scope-free: 35 adding
      `synthesis/levin_wolfram_bridge.md` and four `vault/transcripts` day files; 41 adding the
      `architecture/` and `inbox/` self-awareness and intake layers, which are not consumers of the
      claim and are excluded by construction. **The 30 is not a coincidence of my rule.** I did not
      reverse-engineer it — I wrote the rule, ran it, and it returned 30.

    RESULT 2 — **HEDGES = 0. The item's figure is exact.**
      Zero of the 30 contain any of: `connexin`, `overexpress`, `non-monotonic` / `nonmonotonic`,
      `PROP-2026-09-12-004`, `stage-dependent`, `coupling returns`, `coupling rises`. The same search
      over the wider 35-file and 41-file scopes also returns **zero**. **No file in the estate that
      consumes Levin PRS-02 carries any trace of the 2026-09-02 result, twelve days after it landed and
      two days after the challenge was filed.**

    RESULT 3 — **THREE REWRITTEN TODAY WITHOUT GAINING ONE. The item's figure is exact.**
      Three of the 30 carry an mtime of **2026-09-14 02:00**: `Day-199 - Man's Downfall`, `Day-080 -
      Sorrowful Remedies`, `Day-079 - Sorrowful Effects`. None gained a hedge. (`synthesis/
      levin_wolfram_bridge.md` was also touched at 02:00 and also gained none, but sits outside the 30.)
      `Day-079`'s own `length_note` records that the 2026-09-13 pass "added ~685 words, the largest
      single addition this file has taken," to a file whose Bridges block states PRS-02 as "cancer as
      *defection* from the body's cooperative morphogenetic community" without qualification. **The
      "rewritten through" pattern is confirmed at the file level and the ~1,300-word figure the item
      cites for the separate violation is of the same order as what is visible here.**

    RESULT 4 — **THE 24 vs 30 GAP IS DEFINITIONAL, NOT INSTRUMENTAL, AND IS PREMISE-114'S CASE
      EXACTLY.** OPEN-201 records the Summa verification run's reading: "**24 syntheses, 23 carrying
      the coupling-loss vocabulary**, with Day 080 citing PRS-02 without it." My rule returns 30 for the
      same conceptual object. I then built a second detector for "coupling-loss vocabulary" and it
      returned 11 of 30, against the Summa run's 23 of 24. **I am not publishing that 11 as a finding
      and it must not be quoted.** Per PREMISE-124 it is an uncalibrated self-produced number from an
      instrument I wrote this run with no external referent, and per PREMISE-114 two uncalibrated
      instruments of one system that disagree do not yield a winner. What the divergence *does*
      establish is the diagnosis: **the underlying quantity is deterministic over a frozen tree, so the
      24/30 disagreement is definitional, and the procedure owed is to write the counting definition
      first, designate it the reference, and re-derive both readings.** PREMISE-114 already prescribes
      this and it has not been done. **The item is right that the set is 30 under a defensible rule; it
      is not entitled to say the Summa run was wrong, because no reference definition exists to make
      either reading wrong.**

    RESULT 5 — **THE FACT THAT MOST BEARS ON MY ASSIGNED DIRECTION, AND NEITHER THE ITEM NOR OPEN-201
      STATES IT: THE CORRECTION HAS NOT BEEN APPROVED.** `inbox/proposals/pending/2026-09-12_levin_
      vmem-connexin-metastasis-paradox.md` reads `status: pending`. It sits in `pending/`, not
      `approved/`. Its correction limb is **PRS-CANDIDATE-02, graded `Confidence: Speculative`**, and
      its own Evidence line reads verbatim: "the interpretation is the wiki's and must not be attributed
      to the authors. **Ingest only after the full text is read.**" Its provenance note states "The
      mechanism the paper proposes for the joint switch was **not** retrieved." **On the estate's own
      documented gate, a Speculative candidate in a pending proposal that explicitly forbids its own
      ingestion is not yet a correction — it is a filed challenge.** PREMISE-051's quarantine-with-
      expiry rule and PREMISE-117's break-flag rule pull in opposite directions here and the estate has
      not chosen between them. This materially reframes the item: **thirty files failing to absorb an
      unapproved Speculative candidate is, on one defensible reading, the intake gate working.** It is
      *not* a complete defence — PREMISE-117 obliges a break flag on affected material under an
      *unresolved* dispute, which is exactly this state, and zero flags exist. But the item's framing
      ("recording a correction") presupposes a correction the register does not yet have.

  ───────────────────────────────────────────────────────────────────────────────────────────────────

  Challenging evidence found: **Partial — and the challenge is strong on two limbs and fails on the
    third, which is the limb the item actually rests on.**

  Sources:

    1. **Furman, J.L., Jensen, K. & Murray, F. (2012), "Governing knowledge in the scientific community:
       Exploring the role of retractions in biomedicine," *Research Policy* 41(2):276–290,
       doi:10.1016/j.respol.2011.11.001.** — **VERIFIED** (author's final manuscript record and full
       abstract read this run at DSpace@MIT, hdl 1721.1/102181; the ScienceDirect page returned an empty
       body). This is the assigned source and it delivers. Read verbatim: the authors "analyze the
       universe of peer-reviewed scientific articles retracted from the biomedical literature between
       1972–2006 and comparing with a matched control sample"; "the mean time to retraction is **less
       than two years**"; and, decisively, "**retraction causes an immediate, severe, and long-lived
       decline in future citations.**" Two features make this unusually good for the AGAINST direction
       and I want both on the record. (i) The authors characterise their object, in their own words, as
       "**a distributed, peer-based system for the governance of validity**" — so the corpus that
       delivered a severe and long-lived decline is precisely the distributed, multi-publisher,
       no-write-access corpus the item's remedial framing treats as the hard case. (ii) Their stated
       conclusion is affirmative: "these results support the view that **distributed governance systems
       can be designed to uncover false knowledge relatively swiftly and to mitigate the costs**."
       **THE LIMIT, WHICH IS THE WHOLE BALL GAME AND WHICH I WILL NOT SOFTEN: this measures the FLOW of
       new citations, not the STOCK of existing ones.** Furman et al. establish that a notice reduces
       *future* uptake. It establishes nothing whatever about whether already-published citing works
       were amended — in a journal corpus they cannot be. C2A2's thirty consumers are stock, not flow.
       **No unverified figure from this paper is used**; see DO-NOT-CITE.
    2. **Lu, S.F., Jin, G.Z., Uzzi, B. & Jones, B. (2013), "The Retraction Penalty: Evidence from the
       Web of Science," *Scientific Reports* 3:3146, doi:10.1038/srep03146.** — **VERIFIED** (abstract
       read verbatim from the publisher-hosted PDF at kellogg.northwestern.edu this run; the Nature
       landing page was also retrieved and its metadata agrees). Read verbatim: "a single retraction
       triggers citation losses through an author's prior body of work. Compared to closely-matched
       control papers, **citations fall by an average of 6.9% per year for each prior publication**.
       These chain reactions are sustained on authors' papers (a) published up to a decade earlier and
       (b) connected within the authors' own citation network by **up to 4 degrees of separation** from
       the retracted publication. Importantly, however, **citation losses among prior work disappear
       when authors self-report the error.** Our analyses and results span the range of scientific
       disciplines." **Why this is a genuine AGAINST source and exactly how far it goes.** It is the
       strongest published demonstration that a correction notice propagates *further than anyone
       designed it to* — four degrees out in a citation network, across a decade of prior work, in every
       discipline. A notice is not inert. And the self-report clause is the one finding in this file
       that speaks directly to the owner-corrects-own-corpus condition: **where the corrector is the
       author, the propagation profile changes measurably.** **THE LIMIT: the propagating quantity is a
       reputational discount on the author's *other papers*, not a correction reaching the *text* of
       citing works.** It is transmission, not delivery — PREMISE-108's distinction — and I will not
       claim more for it.
    3. **Wright, H.K., Jasper, D., Klimek, M., Carruth, C. & Wan, Z. (2013), "Large-Scale Automated
       Refactoring Using ClangMR," ICSM 2013, pp. 548–551.** — **VERIFIED** (full four-page paper
       retrieved and read this run from hyrumwright.org). The assigned case, and the figures are read
       verbatim: "there were roughly **45,000 callers** of `SplitStringUsing`"; "The initial ClangMR
       program transformed about **35,000 callers**... and these changes were mailed for review in
       **3,100 separate chunks**"; "an **80th-percentile review time of just over two minutes**"; "The
       bulk of reviews were completed over **two months**, with a small number requiring another month."
       And the mechanism the item's remedy would need: "the transformation could be **repeated**. During
       the course of this effort, we frequently **re-ran the tool to find any additional uses which had
       been added since the initial run**." That re-run property is the direct technical answer to
       "three were rewritten today without gaining one" — in a corpus the owner controls, a rewrite that
       reintroduces the defect is caught by the next sweep. **THE PAPER'S OWN STATED LIMITS, which are
       load-bearing against my direction and which I quote rather than paraphrase:** "ClangMR can only
       refactor changes which are **self-contained within translation units**. **Large sets of changes
       still require tedious manual review.**" And: "In some complex situations, **we chose to defer the
       edits to be done manually.**" ~35,000 of ~45,000 is roughly **78%** in the first pass; the
       remainder was human work.
    4. **Wright, H., "Large-Scale Changes," Chapter 22 of Winters, T., Manshreck, T. & Wright, H. (2020),
       *Software Engineering at Google*, O'Reilly.** — **VERIFIED** (full chapter retrieved and read
       this run at abseil.io, CC BY-NC-ND 4.0). The best-documented case anywhere of a single owner
       correcting its own corpus at scale, and it cuts both ways with unusual clarity. **FOR MY
       DIRECTION**, read verbatim: `scoped_ptr` had "more than **500,000 references**... scattered among
       millions of source files"; "At the height of the migration process, we were consistently
       generating, testing and committing **more than 700 independent changes, touching more than 15,000
       files per day.** Today, we sometimes manage **10 times that throughput**"; "**10% to 20%** of the
       changes in a project" are LSC-derived; "all of this happens with **only a few dozen engineers**
       supporting tens of thousands of others." And the backsliding control, which is the item's
       "rewritten through" problem solved: "it's important to have a system that **prevents additional
       introductions** of the symbol or system that the large-scale change worked hard to remove... we
       use the Tricorder framework... to **flag at review time** when an engineer introduces a new use
       of a deprecated object, and this has proven **an effective method to prevent backsliding.**"
       **AGAINST MY DIRECTION, and these are the chapter's own words, not my gloss:** "**LSCs really
       work only when the bulk of the effort for them can be done by computers, not humans.** As good as
       humans can be with ambiguity, **computers rely upon consistent environments**"; "The majority of
       LSCs across Google actually have **near-zero functional impact**: they tend to be widespread
       textual updates"; "LSCs tend to be **pure refactorings** and therefore very narrow in scope,
       **preserving local semantics**"; and the threshold that decides this item — "**if a change
       requires more than 500 edits, it's usually more efficient for an engineer to learn and execute
       our change-generation tools rather than manually execute that edit.**" The chapter also records
       the human-run variant: Operation RoseHub sent "**more than 2,600 patches**" using "**more than 50
       humans**" rather than automation, for a time-sensitive security fix.
    5. **Facebook Codemod (Rosenstein, c. 2008) and jscodeshift.** — **SECONDARY** (repository
       descriptions via the search layer; neither repository nor any paper retrieved). The
       self-description is worth one line because it states the boundary in the vendor's own framing:
       codemod assists "with large-scale codebase refactors that can be **partially automated but still
       require human oversight and occasional intervention.**" **No figure from this source is used and
       none should be imported by a later run.**
    6. **DO-NOT-CITE — figures encountered and deliberately excluded, named so a later cycle does not
       re-import them believing them checked.**
         - "annual citations to retracted articles drop by **65%** following retraction; **50%** in the
           first year; **72%** by year 10," attributed to Furman, Jensen & Murray 2012. **Search-layer
           only.** The published abstract I verified says "immediate, severe, and long-lived decline"
           and gives **no percentage**. The ScienceDirect full text returned an empty body and the
           DSpace PDF was not parsed. **These numbers are unusable and the rating below does not depend
           on them.** They are the single most quotable figures in this literature and the most likely
           to be laundered into the register by a later run; that is why they are named here.
         - Post-retraction acknowledgment rates — "between **3 and 8%** acknowledge the retraction"
           (attributed to Budd et al. 1999; Neale et al. 2010), "**less than 2%** explicitly mention the
           retraction" (Bolboacă et al. 2019; Bar-Ilan & Halevi 2017), "**46%** of retracted articles
           cited at least once after retraction" (Cassai et al. 2022). **All search-layer summaries; no
           primary retrieved.** These run *against* my assigned direction, and I am excluding them for
           the same reason I exclude the 65% — unverified is unverified regardless of which way it
           points. A 15a-direction or reconciliation run that wants this limb must retrieve them.
         - LLM/RAG "knowledge-base freshness" and "coverage drift" vendor material surfaced by the
           corpus-ownership search. **Marketing content, no measurement, excluded entirely.**
         - `nber.org/papers/w18499` (Azoulay, Furman, Krieger & Murray, "Retractions") — **refused by
           the provenance rule**; the NBER PDF was retrieved but exceeded the read budget and was not
           parsed. **Not cited.** A later run should reach it: it is the nearest thing to a
           spillover-to-the-intellectual-field measurement and it is absent from this file.

  Strength of challenge: **Moderate. Limb-split, because the three limbs separate cleanly and the
    aggregate rating would be misleading.**

    - **"A recorded correction does not reduce downstream uptake": STRONGLY CHALLENGED.** Source 1 is a
      matched-control study over the universe of biomedical retractions 1972–2006 finding an
      "immediate, severe, and long-lived decline in future citations," and source 2 finds a notice
      propagating four degrees out through a citation network across a decade of prior work. **A
      correction notice is not inert. The general form of the item's claim is wrong, and the literature
      on which the FOR direction would most naturally rest is the same literature that says so.**
    - **"Measured non-propagation is confined to distributed, uncontrolled, multi-publisher corpora with
      no write access to citing works": PARTIALLY CHALLENGED, and the assigned framing does not survive
      contact with source 1.** The framing the task set me was that biomedical non-propagation is an
      artefact of a distributed corpus, which is NOT C2A2's situation. Source 1 undercuts this from the
      inside: Furman et al. *call* their object distributed and *conclude* that distributed governance
      works. The contrast the item needs — "distributed corpora fail, owned corpora succeed" — is
      therefore not the contrast the evidence draws. **The real contrast, and it is sharper, is
      FLOW versus STOCK.** In a journal corpus the stock of citing works is physically unamendable, so
      every measured success is a flow effect. C2A2's distinctive property is not that it is owned but
      that **its stock is writable** — and there is no published measurement of stock-correction rates
      in an owned prose corpus, in either direction. I searched for one and did not find it.
    - **"Owned corpora propagate corrections at high rates": CHALLENGED AS STATED, AND THE BOUNDARY IS
      THE ITEM'S UNDOING.** Sources 3 and 4 are the best evidence in existence that a single owner can
      push a change through hundreds of thousands of consuming sites — 35,000 of 45,000 call sites in
      one pass; 15,000 files a day sustained; 500,000 references migrated; a few dozen engineers. **But
      every one of those changes is machine-decidable.** The chapter states the precondition in its own
      voice — "LSCs really work only when the bulk of the effort for them can be done by computers, not
      humans" — and characterises the class: "pure refactorings," "near-zero functional impact,"
      "preserving local semantics." **A connexin hedge is none of those things.** It is a semantic
      qualification whose correct wording differs per file, it changes meaning rather than preserving
      it, and it cannot be expressed as an AST match. Source 3's own limitation section is the
      concession: "**Large sets of changes still require tedious manual review**," and "in some complex
      situations, we chose to defer the edits to be done manually." **The owned-corpus literature
      therefore supports the item's remedy for mechanical changes and is silent — at best — for this
      one.**
    - **THE FINDING THAT DECIDES THE ITEM, AND IT COMES FROM THE AGAINST LITERATURE ITSELF: AT N=30
      THIS IS NOT A PROPAGATION PROBLEM.** Source 4 states Google's own break-even: "**if a change
      requires more than 500 edits**, it's usually more efficient for an engineer to learn and execute
      our change-generation tools rather than manually execute that edit." **The connexin consumer set
      is 30.** That is one-seventeenth of the threshold at which the best-instrumented owned corpus in
      the world says *stop hand-editing and build a tool*. Operation RoseHub did 2,600 patches with
      fifty humans and no automation at all. **So the whole apparatus the item gestures toward — "a
      scheduled cross-tradition pass, not a local edit" — is, on the evidence of the literature the item
      points at, over-engineered for this instance by nearly two orders of magnitude.** Thirty files is
      an afternoon. **The item has correctly identified that the thirty files are unhedged and has
      mis-identified the cause as a missing propagation mechanism. The evidence is equally consistent
      with, and the in-house facts are better explained by, an unassigned thirty-file manual edit and an
      unapproved source correction** (RESULT 5). PREMISE-026 — "long-unowned cohorts are ownership-
      boundary problems, not item-ageing problems; remediation requires owner assignment" — is the
      register's own diagnosis of this shape and it is ACTIVE.
    - **What survives all of the above, undamaged.** Zero of thirty. Twelve days. Three rewritten today,
      through the claim, gaining nothing. No hedge anywhere in the estate. **Nothing in the literature I
      retrieved explains that away, and PREMISE-117's break-flag obligation is unmet on its own terms
      whether or not the proposal is approved.** My direction constrains the *diagnosis* and the
      *remedy*. It does not touch the *observation*, and the observation is the item's real contribution.

  Summary: The item's general claim is challenged and its in-house instance is confirmed exactly.
    Furman, Jensen and Murray's matched-control study over the universe of biomedical retractions
    1972–2006 finds that retraction causes "an immediate, severe, and long-lived decline in future
    citations," and Lu, Jin, Uzzi and Jones find the signal propagating four degrees out through an
    author's citation network across a decade of prior work, disappearing only when the author
    self-reports — so a recorded correction is demonstrably not inert. But both measure the **flow** of
    new citations, never the **stock** of existing ones, which in a journal corpus cannot be amended;
    C2A2's thirty consumers are stock. The owned-corpus literature is spectacular on volume — ClangMR
    converted ~35,000 of ~45,000 call sites in one repeatable pass, and Google's LSC platform sustained
    700 changes and 15,000 files a day through a 500,000-reference migration with a few dozen engineers
    — but states its own precondition in its own voice: "LSCs really work only when the bulk of the
    effort for them can be done by computers, not humans," over changes that are "pure refactorings"
    with "near-zero functional impact." A connexin hedge is a semantic judgment and qualifies for none
    of that. The same chapter supplies the figure that reframes the item: Google's break-even for
    building tooling instead of hand-editing is **500 edits**, and this consumer set is **30**. Two
    in-house facts then close it. The item's numbers replicate exactly — **30 consumers, 0 hedges, 3
    rewritten today** — but the correction itself is **`status: pending`, graded Speculative, and
    carries the instruction "Ingest only after the full text is read,"** so what has failed to propagate
    is not yet a correction. **And the intake's register pre-check is NOT CONFIRMED: PREMISE-116 and
    PREMISE-123 state this item's claim as their whole Statement line, PREMISE-170 clauses 2–4 own the
    extent-of-condition schema, PREMISE-117 obliges the break flag — and PREMISE-116 contains the word
    "propagation" twice in the two sentences the intake says it grepped for.**

  Specific risks:
    - **The remedy this item is trending toward is the expensive one, and the literature says so.**
      "A scheduled cross-tradition pass" for a 30-file semantic edit is 6% of Google's tooling
      break-even. Building a propagation mechanism here consumes the remedial slot and defers the
      afternoon of work that would actually close it — PRESUMPTION-974's pathology, in a new subsystem.
    - **The register already holds this finding four times and the estate is about to mint it a fifth.**
      PREMISE-116, PREMISE-123, PREMISE-170 and PREMISE-117 are ACTIVE and cover all but one clause of
      this item. PREMISE-138 bars re-minting. The live risk is register duplication under the appearance
      of discovery — which is what the missed pre-check produces mechanically.
    - **The pre-check failure is the more general defect and it has now recurred.** PREMISE-164's scope
      limits record the 08-13 intake header's pre-queue grep missing its target; this is the same
      failure one month later, on terms the intake itself named. Under PREMISE-130 the reclassification
      trigger is a third distinct signature, and two are now on the record. **A pre-check that is
      reported rather than run makes every "no covering premise" claim in the queue unreliable, which
      is a defect in the intake instrument, not in any one item.**
    - **Symmetric risk, and it is the larger one: if the AGAINST reading is over-weighted, thirty files
      stay unhedged.** Everything above constrains diagnosis and remedy. None of it licenses inaction.
      PREMISE-117 obliges a break flag on affected material under an *unresolved* dispute — which is
      precisely the current state — and there are zero flags. **PREMISE-170 clause 3 is explicit that
      non-propagation is not free**: refusal to generalise "leaves known-defective instances in place
      and produces a survivorship artefact." A reconciliation that reads this file as "no action needed"
      has misread it.
    - **The 24/30 dispute will recur every time anyone counts, until a definition is designated.** Two
      instruments of one system now disagree on the size of this set and a third (mine) disagrees with
      both on the vocabulary sub-count. PREMISE-114 prescribes the exit and it has not been taken.
    - **Outbound exposure is live and unmeasured.** Thirty synthesis files assert cancer-as-lost-coupling
      without qualification. ASSUMPTION-1336's syntheses are the adjacent instance. If any of these has
      been sent outside the estate, the unqualified claim has travelled.

  Mitigations available:
    - **Do the thirty files by hand, and stop designing the mechanism.** This is the literature's own
      recommendation at this N (source 4's 500-edit threshold; RoseHub's fifty humans and 2,600
      patches). It needs an owner, not an architecture — PREMISE-026.
    - **Resolve the proposal's status first, because it determines what the edit says.** While
      PROP-2026-09-12-004 is `pending`/`Speculative` with "Ingest only after the full text is read," the
      correct edit to the thirty files is a **break flag under PREMISE-117** ("a claim under unresolved
      challenge; see PROP-2026-09-12-004"), **not** the corrected gloss. Those are different edits and
      writing the second one now would ingest a Speculative candidate against its own instruction.
      **Retrieving the paper's full text is the single highest-value action available and it is not
      named anywhere in the item.**
    - **Designate the counting definition before anyone recounts.** Write the rule (scope, attribution
      test, gloss test), designate it the reference, re-derive the Summa run's 24 and this run's 30
      against it, and expect convergence. PREMISE-114, unexecuted.
    - **Add the backsliding guard, which is the cheap durable part and the one place the owned-corpus
      literature transfers cleanly.** Source 4's Tricorder pattern — flag at write time when a file
      introduces a use of a flagged claim — is stated in the chapter as "an effective method to prevent
      backsliding," and source 3's repeatable re-run is the same idea. **This is the direct answer to
      "three were rewritten today without gaining one" and it does not require a propagation
      mechanism**: it requires the QC pass that touched Day-079, Day-080 and Day-199 to read a flag
      list. That is a task-file edit, which is PREMISE-164's addressing remedy.
    - **Escalate on a counter, per PREMISE-164's "CHEAPEST REMEDY."** A condition named on N consecutive
      days without the named action being taken should escalate on the count alone. Three consecutive
      days is already the register's stated actionable trigger and the condition is met.
    - **Fix the intake instrument, not just this item.** A pre-check that reports a grep should record
      the command and its hit count, so "searched `propagat`, 0 covering hits" is falsifiable. Here it
      would have returned PREMISE-116 immediately. Per PREMISE-116's own INSTRUMENTATION CONSTRAINT, a
      field reading "pre-check: done" reproduces the defect exactly — the evidence must be the output.

  STEELMAN:
    Item: PRESUMPTION-989
    Strongest counterargument (i.e. the strongest case AGAINST my own AGAINST finding, stated at full
      strength): Every piece of external evidence in this file is about a corpus that cannot be edited,
      and the one case that *can* be edited is disqualified by a boundary I drew myself and then used to
      dismiss the item. That move does not hold up. Furman et al. and Lu et al. measure flow because
      flow is all a journal corpus *has* — the stock is physically frozen, so their silence on stock
      correction is not evidence about stock correction, it is the absence of a possible measurement.
      Invoking it against C2A2 is an argument from a gap. Meanwhile the Google case, read honestly,
      argues *for* the item rather than against it: the chapter's whole thesis is that propagation at
      scale is **an engineered achievement with a dedicated platform, a standing committee, a
      sharding service, a CI train and a backsliding detector**, and that organic migration does not
      happen — "organic migrations are unlikely to fully succeed, in part because engineers tend to use
      existing code as examples when writing new code," and "nobody likes unfunded mandates." **That is
      PRESUMPTION-989's claim in Google's own words.** The estate has no committee, no sharding, no
      detector, and no owner; it has a proposal file and a prose note. And my 500-edit rebuttal cuts the
      wrong way: Google's threshold is the point at which *tooling beats hand-editing*, which
      presupposes that somebody is doing the hand-editing. **Nobody is.** Thirty files below the
      tooling threshold and above zero is exactly the regime in which a change never gets made at all,
      because it is too small to justify a mechanism and too large for anyone to absorb incidentally —
      and the estate's own data shows the thirty sitting untouched for twelve days while three of them
      were actively rewritten through the claim. Finally, RESULT 5 proves less than I claimed: an
      unapproved proposal is a perfectly good reason not to write the *corrected gloss*, and no reason
      at all not to write a *flag*. PREMISE-117 obliges the flag precisely *because* the dispute is
      unresolved. **Zero flags on thirty files is the item's claim, fully instantiated, and nothing in
      the retrieved literature touches it.**
    What would need to be true for C2A2 to be safe: (a) someone must own the thirty-file edit, and no
      one does — this is the binding condition and it is currently false; (b) the flag-versus-gloss
      distinction must be made explicit, or the next pass will either ingest a Speculative candidate
      against its own instruction or do nothing, and both have happened in this estate; (c) the QC pass
      that rewrites these files must read a flag list, or the backsliding continues by construction —
      Day-079 took ~685 words yesterday and Day-079, Day-080 and Day-199 took more at 02:00 today, all
      through an unhedged claim; (d) the intake's pre-check must produce falsifiable output, because on
      this item it produced a conclusion contradicted by a one-line grep, for the second recorded time
      in a month; (e) the counting definition must be designated, or the 24/30 dispute recurs on every
      recount and consumes the attention the edit needs.
    How to test: **Three tests, all in-house, all cheap, and the first is the one that settles the item.**
      (1) **The assignment test.** Assign the thirty-file flag edit to a named owner with a date. If it
      completes in one session, the item is an ownership gap (PREMISE-026) and no propagation mechanism
      was ever needed. If it does not complete despite being assigned, the item is right and the gap is
      structural. **This discriminates between the two live diagnoses and nothing else in this file
      does.** (2) **The backsliding test.** Record the thirty files' current state. Let the QC schedule
      run one week. Recount hedges and count how many of the thirty were rewritten in that week. If
      files continue to be rewritten through the claim *after* a flag exists, source 4's Tricorder
      finding is refuted in this estate and the remedy must move up a tier. (3) **The pre-check test,
      which is the generalisable one.** Take the last N intake items claiming "no covering premise."
      For each, re-run the stated grep against `validated_premises.md` and record the hit count. This
      run's item returns PREMISE-116 on the intake's own term. **If the rate of pre-checks contradicted
      by their own stated command is materially above zero, the defect is in the intake instrument and
      every "no covering premise" claim in the queue is uncalibrated** — which is a larger finding than
      PRESUMPTION-989 and is measurable today with one loop.

  Search scope: **Comprehensive on the assigned directions; one named gap.** Four angles searched:
    (i) retraction and correction notices reducing subsequent citation — the assigned Furman/Jensen/
    Murray and retraction-penalty literatures, both located and both primaries verified; (ii) effective
    correction propagation where the corrector controls the corpus — Google's ClangMR paper and the
    *Software Engineering at Google* Large-Scale Changes chapter, both retrieved **and read in full**,
    plus Facebook Codemod/jscodeshift at secondary level only; (iii) whether measured non-propagation is
    confined to distributed multi-publisher corpora — searched, and the answer **partly refutes the
    framing I was given**, which is recorded above rather than smoothed; (iv) measured correction or
    staleness propagation rates in owned prose corpora, internal wikis and knowledge bases — **searched
    and found nothing usable.** That last is the declared gap and it is the one that matters: **I
    located no published measurement, in either direction, of the rate at which a substantive claim-level
    correction reaches the prose files of a corpus its owner can write to.** The software literature
    measures mechanical transformations; the scientometric literature measures unamendable stock. **The
    exact question PRESUMPTION-989 asks appears to be unmeasured in the literature**, which is why all
    three recommended tests are in-house. Reported as a genuine evidential gap, not as absence of
    evidence. Three external primaries were read at source this run (Furman et al. abstract; Lu et al.
    abstract verbatim; ClangMR in full) and one full book chapter (Google Ch. 22); **every figure quoted
    above was read in a primary, and the entire post-retraction percentage literature is excluded by
    name as DO-NOT-CITE because no primary could be retrieved for it.** No unverified number appears in
    the rating.

  Recommendation: **PARTIALLY-CHALLENGED**
    The general claim — "recording a correction is sufficient for it to reach the files carrying the
    corrected claim" — is challenged: notices measurably reduce downstream uptake (source 1), propagate
    four degrees through a citation network (source 2), and a single owner can push a change through
    500,000 consuming references (sources 3–4). The item's **diagnosis** and implied **remedy** are
    challenged harder: at N=30 this sits at 6% of the best-documented owned corpus's own
    tooling-versus-hand-editing threshold, the correction is `status: pending` and graded Speculative
    with an explicit instruction not to ingest it, and the register already holds the propagation
    finding four times over. **The item's in-house observation is not challenged at all — 30, 0 and 3
    each replicate exactly under a stated rule — and PREMISE-117's break-flag obligation is unmet
    regardless of how the diagnosis resolves.**

  SYSTEMIC-RISK-FLAG:
    Date: 2026-09-14
    Affected items: PRESUMPTION-989 (this item); PRESUMPTION-983 (the named-but-unrun action); and,
      by construction, **every queued item whose intake asserts "no covering premise."**
    Common vulnerability: **The intake pre-check is self-reported and unfalsifiable, and it has now
      failed twice on the record in one month.** PRESUMPTION-989's intake states it searched
      `correction`, `retraction`, `propagat`, `blast radius`, `erratum` and opened the three nearest
      hits, concluding "no covering premise." A single `grep -i propagat validated_premises.md` returns
      **PREMISE-116**, whose Statement line is this item's claim negated, at High confidence.
      **PREMISE-164's own SCOPE LIMITS block already records the identical failure against the 08-13
      intake header** ("the very source the queue named as the search target, which the 08-13 intake
      header's pre-queue grep MISSED"). The sibling runs' diagnosis — covering language buried in
      another premise's free text — **does not fit this instance**, which makes it the more serious
      shape: the language was not buried, and the check still returned the wrong answer.
    Literature basis: PREMISE-116's own INSTRUMENTATION CONSTRAINT, read at source — "a propagation step
      that produces a 'propagated: yes' field reproduces the defect exactly; the measure must be a
      behavioural change in the governed agent's OUTPUT." A pre-check field reading "read at source —
      no covering premise" is that defect in its purest form. Supported externally by source 4's
      treatment of verification as an engineered artefact (TAP reports "used as **evidence** that an LSC
      is safe to submit") rather than an assertion.
    Risk level: **High.** Not Critical: the failure inflates the register with duplicates and wastes
      15a/15b cycles rather than corrupting a published claim, and PREMISE-138's re-minting bar is a
      partial backstop. It is High because **every downstream disposition that relies on "this is a
      genuine gap in the register" inherits an uncalibrated input**, and because the estate cannot
      currently distinguish a real gap from an unrun grep.
    Recommendation: Require intake pre-checks to record **the command and its hit count**, not the
      conclusion. Then run the retrospective sweep in How-to-test (3) over the last N items claiming no
      covering premise. Per **PREMISE-118**, naming a defect in an instrument does not license continued
      use of it — it triggers contain / assess impact / fix cause / verify, **including a retrospective
      impact assessment over every result produced since last known-good**. Two recorded failures one
      month apart is the trigger, and PREMISE-118's own SELF-APPLICATION note warns that this estate has
      previously named such a defect and produced eighteen further dispositions without performing the
      assessment.

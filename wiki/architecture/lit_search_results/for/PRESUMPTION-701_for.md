SEARCH-FOR-PRESUMPTION-701:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-701
  Original statement: That determinacy of target is sufficient warrant for a
    vault-wide sweep; a bulk repair cleared because "this has one determinate
    target, so a vault-wide sweep is safe," on the same day the same agent
    family warned that a sweep keyed on a similar identifier "would have
    corrupted one of them." Risk: High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-701
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read two same-day rulings from one agent family against each other.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Opdyke, W.F., 1992. "Refactoring Object-Oriented Frameworks." PhD
       thesis, University of Illinois at Urbana-Champaign. [Located this
       session via IDEALS, ACM Digital Library (5555/169783) and secondary
       readings; thesis itself not opened.] — The foundational theoretical
       grounding, and it supports the presumption's form directly. Opdyke
       defines refactoring as behaviour-preserving transformation and, crucially
       for this item, supplies the notion that a transformation is licensed by
       a set of stated preconditions that can be checked before the change is
       applied. The doctrine that "if the precondition holds, the sweep is
       safe" is precisely Opdyke's doctrine. This item's reasoning — one
       determinate target, therefore safe — is a recognisable instance of a
       standard and respectable methodology, not an ad hoc excuse.
    2. Name binding preservation as a rename precondition — located this
       session via "Language-Parametric Reference Synthesis (Extended)" (arXiv
       2502.19143) and a systematic mapping study, Ó Cinnéide et al. or
       similar, "On preserving the behavior in software refactoring: A
       systematic mapping study," Information and Software Technology, 2021
       (ScienceDirect S0950584921001348). [Author list for the mapping study
       NOT verified — the result snippet did not give it and I did not open the
       paper. Treat the attribution as uncertain.] — Names the exact condition
       the presumption invokes. Behaviour preservation for a rename requires
       that references resolve to the same distinct declarations after the
       change as before; renaming is unsafe precisely when it can cause a
       reference to bind to a different declaration. "One determinate target"
       is a plain-language statement of the binding-preservation precondition.
       The presumption is using the right concept.
    3. The same body of work, on sufficiency. — The mapping-study material
       located states explicitly that Opdyke's proposed preconditions are not
       sufficient to guarantee behaviour preservation after transformation, and
       a companion result located this session ("Bugs in the Shadows: Static
       Detection of Faulty Python Refactorings," arXiv 2507.01103, not opened)
       exists as an entire paper about refactorings that satisfy their stated
       preconditions and are nonetheless wrong. This is supporting evidence for
       the practice and against the sufficiency claim: determinacy is the right
       precondition, it is necessary, and it is documented as not sufficient.
    4. Dry-run and diff-review protocols in mass code and data correction —
       jscodeshift's --dry and --print flags (project documentation, located
       via a Medium walkthrough this session); Moderne's position that recipes
       can be dry-run and tested locally before large-scale application
       (moderne.ai engineering blog); Atlassian developer blog on AI-assisted
       large-scale refactoring. [All practitioner sources; no peer-reviewed
       source located for this specific practice.] — Supports the presumption
       only in a qualified way. The consistent practitioner position is that
       large-scale changes are made safe by batching, dry-running, reviewing
       the diff before apply, and running tests at each step — that is,
       safety is produced by a *procedure*, and precondition-checking is one
       step in it rather than a substitute for it. No located source treats a
       satisfied precondition as licence to skip the dry run.
    5. Uniqueness constraints in data quality practice (general data-cleaning
       literature located this session; no single authoritative citation
       obtained — the results were textbook-level and vendor material). — Two
       relevant points. First, uniqueness is a checkable schema property:
       "to detect a uniqueness violation, a check is made for each value of the
       attributes in question to see if it exists only once in the data set."
       This is real support, and it is the operative distinction for this item:
       uniqueness that has been *checked* warrants the sweep; uniqueness that
       has been *asserted* does not, and the two are cheap to tell apart.
       Second, the same literature treats identifier collision as a routine,
       expected condition requiring an explicit disambiguation strategy rather
       than an unusual one.

  Strength of support: Moderate (for the checked-determinacy reading);
    Weak (for the reading the item actually surfaces)

  Summary: The presumption's reasoning has a real and reputable pedigree. The
    refactoring literature going back to Opdyke's 1992 thesis is built on
    exactly this move — state a precondition, check it, and treat the
    transformation as licensed when it holds — and name binding preservation is
    the standard precondition for a rename, which is a formalisation of "one
    determinate target." So the *form* of the inference is supported. Two
    qualifications reduce the support to partial, and both bear directly on
    what 14b noticed. First, the same literature reports that Opdyke's
    preconditions are known to be insufficient to guarantee behaviour
    preservation, and there is an active line of work on refactorings that pass
    their preconditions and are still faulty; determinacy is necessary, not
    sufficient. Second, and more sharply, the literature's warrant attaches to
    *verified* determinacy — the data-quality framing is explicit that
    uniqueness is established by checking each value's occurrence count, not by
    inspection or assumption. The near-miss the item cites, where a sweep keyed
    on a similar identifier would have corrupted one of two records, is the
    textbook demonstration of the gap between assumed and verified uniqueness,
    and its occurrence on the same day is evidence that this system's
    determinacy claims are not reliably being checked. Every located source on
    bulk-change practice also treats dry-run and diff review as standard
    regardless of precondition status; none treats a satisfied precondition as
    grounds for skipping them.

  Caveats: The refactoring sources are about code, where the binding structure
    is machine-checkable by a compiler or type system, and a wiki vault has no
    equivalent oracle; the transfer is on reasoning form rather than on
    tooling. Source 2's author attribution is unverified and should be
    corrected before reuse. Sources 4 and 5 are practitioner-level; the
    dry-run recommendation is consistent across every source located but no
    controlled study quantifying its benefit was found, so its strength here is
    consensus rather than measurement. Nothing located addresses the specific
    case of a Markdown wiki with wikilink identifiers, so the base rate of
    identifier collision in this particular substrate is unknown — which cuts
    both ways, since the item's own near-miss is currently the only local
    datapoint and one datapoint does not establish a rate either. Finally, a
    genuine defence the search did not refute: if determinacy is verified by
    enumeration rather than asserted, the two same-day rulings are not
    inconsistent at all, and the literature would endorse both. The item's
    force depends on whether the check was actually run, which is a local
    question no literature can settle.

  NOVELTY-FLAG: Not raised. Precondition-based safety for bulk transformation
    is a mature field with a known sufficiency gap.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: safety conditions and preconditions
    for automated bulk edits; behaviour preservation and name binding
    preservation in rename refactoring; Opdyke's precondition methodology and
    its documented insufficiency; dry-run, diff-review and batching protocols
    in large-scale code change; uniqueness violation detection and identifier
    collision handling in automated data cleaning. Not searched: the blast-radius
    and change-management literature from site reliability practice (staged
    rollout, canary application of a bulk change), which would speak to the
    "vault-wide" scope rather than the "determinate target" premise, and is the
    most promising follow-up seam.

SYSTEMIC-RISK-FLAG G1

  Date: 2026-08-18

  Raised by: Agent 15b (Literature Search AGAINST), group G1

  Affected items:
    - ASSUMPTION-1126 (14a) — "that streak was never a YouTube problem"
    - ASSUMPTION-1129 (14a) — two regex instruments wrong by construction
    - ASSUMPTION-1132 (14a) — QC queue 90–96% residue by five reports; unstable selector
    - PRESUMPTION-829 (14b) — a scheduled task which fires has run
    - PRESUMPTION-830 (14b) — a recorded diagnosis is as durable as a recorded measurement
    - PRESUMPTION-834 (14b) — capability is a property of contract, not session

  Common vulnerability:

    Two distinct but interlocking patterns run through all six items.

    (G1-a) MONOCAUSAL INFERENCE FROM SINGLE-DAY, NON-INDEPENDENT, UNCONTROLLED
    OBSERVATION — and the correction inheriting the standing of the thing it corrected.
    Every one of the six is grounded in one day's operational data. Four of them
    (1126, 1132, 830, 834) reach a single-cause or single-determinant verdict:
    "never a YouTube problem", "the determinant of success was the Documents mount",
    "the register format gives a cause the same standing", "five independent reports".
    None of these verdicts was produced with a control, a stratification, a second
    day, or a disconfirming test. Critically, the *corrections* are being written into
    the same register, in the same one-cause-per-field shape, with the same finality as
    the entries they replace — so the pipeline that detects wrong causes is structurally
    identical to the pipeline that produced them. PRESUMPTION-830 names this problem
    and then instantiates it.

    (G1-b) THE PROPOSED REMEDY IS SUBJECT TO THE FAILURE MODE IT IS MEANT TO CATCH.
    In 829, 834, 1129 and 830, the implied fix is an instrument, a declaration, a
    gate, or a provenance tag. In each case the literature shows the fix carries the
    same class of defect: liveness properties are not monitorable from finite traces
    and failure detectors are unreliable by construction (829, 834); pre-flight
    capability checks are TOCTOU-vulnerable (834); human/agent review of an automated
    aid degrades by automation bias and does not improve with training (1129);
    provenance labelling of retracted claims demonstrably fails to stop their reuse,
    at a measured ~5% acknowledgement rate over two decades (830). The system is at
    risk of building a layer of controls whose presence is mistaken for their
    efficacy, converting loud failures into quiet ones with an audit trail.

  Literature basis:

    Monocausal inference and hindsight (G1-a):
      Peerally, M.F., Carr, S., Waring, J., Dixon-Woods, M. 2017. "The problem with
        root cause analysis." BMJ Quality & Safety 26(5):417–422.
        DOI 10.1136/bmjqs-2016-005511. — inappropriate focus on single-point causation
        as a standing weakness of incident analysis.
      Dekker, S. "The Field Guide to Understanding 'Human Error'." Ashgate/CRC. —
        causal attribution as a product of hindsight; counterfactual reasoning
        collapses complexity into a linear story.
      Knight, J.C. & Leveson, N.G. 1986. "An Experimental Evaluation of the Assumption
        of Independence in Multiversion Programming." IEEE TSE SE-12(1):96–109. —
        ~50% correlated faults across 27 independently written versions; independence
        rejected at 99% confidence. Bears directly on "five independent reports"
        (1132) and on twenty-nine same-day runs treated as independent trials (834).
      Simpson's paradox literature (Stanford Encyclopedia of Philosophy entry;
        PMC7175433 simulation study). — no test detects spuriousness from observational
        data alone; univariable analysis cannot manage confounding.
      Howard, J. 2019. "Premature Closure: Anchoring Bias, ... Search Satisficing,
        Diagnosis Momentum ..." Springer, DOI 10.1007/978-3-319-93224-8_23. — the
        search stops when a satisfying finding appears.

    Remedies carrying the same defect (G1-b):
      Alpern, B. & Schneider, F.B. 1985. "Defining Liveness." Information Processing
        Letters 21(4):181–185; with the runtime-verification monitorability literature
        (Springer 2019, "Refining the Safety–Liveness Classification of Temporal
        Properties According to Monitorability"). — many liveness properties admit no
        verdict from any finite prefix.
      Chandra, T.D. & Toueg, S. 1996. "Unreliable Failure Detectors for Reliable
        Distributed Systems." JACM 43(2):225–267. DOI 10.1145/226643.226647; with
        Fischer, Lynch & Paterson 1985, JACM 32(2):374–382. — slow and crashed are
        indistinguishable; every detector trades completeness against accuracy.
      Parasuraman, R. & Riley, V. 1997. "Humans and Automation: Use, Misuse, Disuse,
        Abuse." Human Factors 39(2):230–253; Parasuraman, R. & Manzey, D.H. 2010.
        "Complacency and Bias in Human Use of Automation." Human Factors 52(3):381–410.
        — automation bias in naive and expert operators alike, not preventable by
        training; false alarms drive disuse.
      Hsiao, T-K. & Schneider, J. 2021. "Continued use of retracted papers..."
        Quantitative Science Studies 2(4):1144–1169. — 722 of 13,252 post-retraction
        citation contexts (5.4%) acknowledged the retraction; Budd, Sievert & Schultz
        1998 (JAMA 280(3):296–297) and the later Budd et al. replication report ~3–8%.
        Formal retraction metadata does not stop reuse.
      Yin, Z. et al. 2011. "An Empirical Study on Configuration Errors in Commercial
        and Open Source Systems." SOSP '11. DOI 10.1145/2043556.2043572. —
        parameter mistakes dominate (70.0–85.5%); environment/provisioning is a real
        but minority class.

  Risk level: High

    Rationale: G1-a is a correctness risk on the intake queue itself — if the
    correction pipeline reproduces the error mode it diagnoses, the observed rate of
    overturned causes will not fall, and confidence in the register will be
    unwarranted in both directions. G1-b escalates this to High rather than Medium
    because ASSUMPTION-1129 sits on an irreversible operation (memory-entry deletion)
    whose only described guard is agent review, and the automation-bias evidence says
    that guard is not a control. A false absence acted on by a retirement pass is not
    recoverable, and a rubber-stamped approval trail makes it look reviewed.

  Recommendation:

    1. Do not act on 1129's destructive path until the false-absence rate of every
       deletion-authorising instrument is measured against a labelled fixture and a
       numeric precision floor is set. Bound the per-pass blast radius. Treat "an
       agent will notice" as no guard at all.
    2. Require a disconfirming test, not a plausible mechanism, before any cause is
       marked settled (1126, 834). For 834 specifically, stratify the mount/outcome
       association by task type and runtime across multiple days, and run the direct
       mount-present / mount-absent intervention before committing to any remedy.
    3. Change the register shape before adding provenance tiers (830). Version all
       fields — measurements and causes alike — with supersession links, and push
       corrections to citers rather than tagging them at source; the retraction
       evidence predicts passive tags will not propagate.
    4. Publish the error rates of every new instrument alongside its output (829, 834).
       An unreliable detector reported as reliable is a net loss.
    5. Break the correlation in aggregated estimates (1132). Have one residue estimate
       produced from an independently written definition; if it agrees, the 90–96%
       figure is corroborated, and if it does not, the five reports were one report.
    6. Reconsider the direction of the 1132 remedy: professional audit standards
       (IAASB ISA 240) affirmatively require unpredictability in inspection selection.
       Seeded pseudorandom selection with the seed recorded gives reproducibility and
       unpredictability together; a frozen queue gives neither safely.

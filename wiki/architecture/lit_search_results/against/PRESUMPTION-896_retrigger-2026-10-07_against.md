SEARCH-AGAINST-PRESUMPTION-896 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-07
  Original item: PRESUMPTION-896
  Original statement (per MONITOR-585): [inferred] "Filing a defect discharges the obligation to fix it,
    where the fix was already computed."
  Owed this cycle (for_lit_search.md, 15d re-trigger 2026-09-20): (a) the remediation-rate literature —
    what fraction of filed/flagged software defects are ever fixed; (b) a replication check on the
    moral-licensing mechanism cited at cycle 0.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output. Context read: monitor_queue.md (MONITOR-585),
    for_lit_search.md (~L22390-22420), and my own cycle-0 file PRESUMPTION-896_against.md.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-896
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a pattern in which surfacing a defect into the register was the terminal action,
        with no tracked commitment to repair.
      15b (2026-08-31): PARTIALLY-CHALLENGED (Moderate); 2 queries; mechanism rested on Cain/Loewenstein/
        Moore 2005 and Blanken et al. 2015; remediation-rate limb only practitioner folklore.
      15c: DISPOSITION-875 → MONITOR-585.
      15d (2026-09-20): Re-triggered; owed = remediation-rate literature + licensing replication check.
      15b (re-trigger cycle 1, 2026-10-07): 3 searches, 1 fetch. Found peer-reviewed remediation-rate
        measurements (static-analysis alerts; kernel bug reports). Found that the licensing mechanism is
        WEAKENED by a bias-corrected meta-analysis — reported against my own cycle-0 file.
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: one abstract-level fetch (Kuper & Bott); remaining sources search-result/snippet level.
    Search scope: preliminary — broader search recommended only on limb (a) if the in-house closure-
    capacity number (MONITOR-585 tripwire) is not produced.

  Challenging evidence found: Yes on limb (a); limb (b) cuts AGAINST my own cycle-0 mechanism.

  Sources:
    1. Imtiaz, N., Murphy, B. & Williams, L. 2019. "How Do Developers Act on Static Analysis Alerts? An
       Empirical Study of Coverity Usage." ISSRE 2019 (Microsoft Research listing). [search-result;
       authors/venue from background knowledge, not verified this run] Across Linux, Firefox, Samba,
       Kodi and oVirt, only 27.4–49.5% (median 36.7%) of alerts were acted on ("actionable"); the fixes
       were small (median 4 lines) yet took 36–245 days (median 96) to land. Bearing: even when the fix
       is cheap and known — the exact condition in 896 ("fix already computed") — a filed alert waits a
       median of ~3 months, and the majority are never acted on. Filing is not followed by fixing at
       anything like a 1:1 rate.
    2. Guo, P.J. & Engler, D. 2009. "Linux kernel developer responses to static analysis bug reports."
       USENIX ATC 2009. [search-result] Overall triage rate 61% across checker types, varying 38%–79%
       by bug type. Bearing: ~2 in 5 machine-filed reports were not even triaged, let alone fixed; the
       remediation rate depends on the TYPE of report, not on the act of filing.
    3. LLVM bug-lifecycle BoF thread, cfe-dev, Oct 2018. [search-result; practitioner, not peer-reviewed]
       ~50% of first-time reporters' bugs never received any reply. Weight: low; corroborative only.
    4. Kuper, N. & Bott, A. 2019. "Has the evidence for moral licensing been inflated by publication bias?"
       Meta-Psychology 3, doi 10.15626/MP.2018.878. [fetched — abstract page] Prior meta-analyses gave
       d > .30; "several large replication studies have either not found the effect or reported a
       substantially smaller effect size." Bias-adjusted estimates: d = −0.05 (PET-PEESE, n.s.) and
       d = 0.18 (3-PSM); "both the evidence for and the size of moral licensing effects has likely been
       inflated by publication bias." Bearing: REPORTED HONESTLY — this weakens the MECHANISM my cycle-0
       file leaned on (Blanken et al. 2015). The challenge to 896 can no longer rest on licensing.
    5. "Observation Moderates the Moral Licensing Effect: A Meta-Analytic Test of Interpersonal and
       Intrapsychic Mechanisms." Personality and Social Psychology Bulletin, 2025. [search-result,
       title + one-line snippet only; authors not confirmed] Reported to find licensing moderated by
       observation (reputation-based). Bearing, speculative: if any residual effect is reputational, a
       PUBLIC register entry is the observed condition — but I did not read the paper and do not lean on it.

  Strength of challenge: Moderate (unchanged in grade; changed in basis)

  Summary: The basis of the challenge has moved. At cycle 0 the challenge was a psychological mechanism
    (moral licensing) plus folklore about backlog rot. This cycle the mechanism is substantially weakened
    — the bias-corrected licensing effect may be near zero — so it should no longer be cited as why
    filing substitutes for fixing. In its place there is now direct peer-reviewed measurement of the
    outcome: in mature projects with dedicated maintainers, roughly a third to a half of tool-filed
    alerts are acted on, and the ones that are fixed take a median ~96 days despite median 4-line fixes.
    The empirical fact the presumption must survive is not "people feel licensed" but "filed and fixed
    are different populations, and the gap is large and slow even when the fix is trivial." This is a
    rate fact; it holds without any psychological mechanism.

  Specific risks: If 896 is held, the register's growth is read as diligence while an unknown and
    probably majority share of its entries are never remediated. The register currently has no measured
    closure rate to compare with the 36.7% / 61% external baselines, so nobody can tell whether the
    estate is better or worse than Linux.

  Mitigations available: Measure the estate's own filed→fixed ratio and median time-to-fix (the
    closure-capacity number MONITOR-585 names); compare to the Imtiaz and Guo baselines; route
    "fix already computed" items to an auto-apply or explicit owner rather than to the general register.

  Recommendation: PARTIALLY-CHALLENGED — remediation-rate limb now evidenced (peer-reviewed, snippet);
    licensing limb withdrawn as support for the challenge (fetched).

STEELMAN:
  Item: PRESUMPTION-896
  Strongest counterargument: The best-maintained software projects on earth, with paid staff and
    triage processes, act on barely a third of filed static-analysis alerts and take three months to
    apply four-line fixes. Nothing about C2A2's register suggests it has more remediation capacity than
    the Linux kernel. "Filing discharges the obligation" is therefore not a description of a working
    handoff; it is a description of the step at which the majority of defects stop moving. The
    collapse of the licensing literature does not rescue the presumption — it removes the need for a
    psychological story at all, because the rate data are sufficient on their own.
  What would need to be true for C2A2 to be safe: a downstream stage exists that is TRIGGERED by filings
    and has a measured throughput at or above the filing rate (cycle-0 15b steelman of role separation
    stands only under this condition).
  How to test: compute filed→closed-as-fixed ratio and median age for register entries whose fix was
    pre-computed; if below ~37% or median age >96 days, the estate is at or worse than the external baseline.

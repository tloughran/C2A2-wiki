# PRESUMPTION-772 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-772

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-772

**Original statement:** That a monitoring cycle's null result is a measurement — four cycles logged "no new sources" for items a fifth cycle found material for at 12 of 12.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from a 12/12 hit rate on a fifth cycle that the four preceding null cycles cannot have been measurements; risk graded Critical.
  - 15b: Searched for challenging literature on liveness/heartbeat signalling, no-data vs zero semantics in monitoring, and the identifiability of missing-data mechanisms.
- **Current status:** PARTIALLY-CHALLENGED

**What is being challenged:** not that non-execution can masquerade as a null, but the specific inference that the 12/12 result *demonstrates* the earlier cycles did not execute. A recall/coverage difference between search strategies is an equally consistent and arguably better-supported explanation.

### Challenging evidence found: Partial

### Sources

1. **Missing-data mechanism identifiability literature (Molenberghs & Verbeke, 2005, and the sensitivity-analysis tradition summarised in BMC Med Res Methodol 2022, doi:10.1186/s12874-022-01727-1) — [Molenberghs & Verbeke citation unverified — referenced secondarily in search snippets].** — It is not possible to distinguish MAR from MNAR — here, "searched and found nothing" from "did not search" — using the observed data alone; the mechanism is formally unidentifiable and the discipline's response is bounded sensitivity analysis, not a determination. This directly challenges the presumption's evidentiary move: the 12/12 result is consistent with non-execution *and* with a genuine recall gain, and the observed data cannot arbitrate.
2. **Heartbeat / dead-man's-switch monitoring practice (OneUptime, "Heartbeat and Dead Man's Switch Alerts," 2026-02-06; AlertOps heartbeat documentation; ilert Prometheus heartbeat docs) — [unverified — practitioner sources from search snippets].** — The no-data-versus-zero distinction is a solved, cheap problem: "a query returns nothing if the time series disappears — it does not return zero," and the standard fix is an out-of-band liveness beacon. Challenges the Critical severity: the exposure is real but the remedy is a few lines of configuration, and the literature treats it as routine hygiene rather than an architectural defect.
3. **"Automatic quality estimation for ASR system combination," *Computer Speech & Language* / arXiv:1706.07238.** — Cited here for the general method: confidence in a retrieval or recognition result can be estimated without a reference, meaning a null can be scored for *plausibility* even when it cannot be verified. Challenges the binary framing "a null is either a measurement or it is not" — nulls admit graded confidence.

### Strength of challenge: Moderate

### Summary

The literature grants the failure mode and undercuts the inference. Formally, the distinction between "measured and found nothing" and "did not measure" belongs to the class of unidentifiable missing-data mechanisms: no amount of downstream evidence, including a later cycle's 12/12 hit rate, settles it from the observed record. The competing explanation is mundane and common — the fifth cycle used a broader or better-targeted query family and simply had higher recall, which is the ordinary experience of iterative literature search and would produce exactly this pattern with all five cycles executing correctly. Monitoring practice also challenges the severity: the no-data-is-not-zero problem is a recognised, cheaply fixed hygiene item addressed by heartbeat beacons and freshness checks, not a structural flaw. The strongest residual support for the presumption is the *magnitude* — 12 of 12 is a suspiciously complete reversal — but magnitude alone does not distinguish the two mechanisms.

### Specific risks

If the presumption is accepted as stated, C2A2 may retroactively void a large body of legitimately-executed null cycles, discarding real negative information and incurring rework; it may also install execution-attestation machinery when the actual deficiency was search-strategy recall. Conversely, if the challenge is accepted and the presumption was right, four cycles of undetected non-execution continue silently, and the yield metrics that consumed those nulls remain inflated. The asymmetry matters: the second error is self-concealing and the first is not.

### Mitigations available

Cheap and decisive: require every monitoring cycle to log the queries issued, the result counts per query, and a cycle-completion beacon. This single change resolves the identifiability problem prospectively — a null with an attached query log and a nonzero raw-result count is a measurement; a null with an empty query log is not — and it costs nothing. For the four historical cycles, run a bounded sensitivity analysis: re-execute the *original* query family and see whether it reproduces the null. If it does, the fifth cycle's gain was recall, not liveness.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-772

**Strongest counterargument:** A statistician would say the presumption reasons backwards from an outcome to a mechanism across an identifiability gap. Whether the four nulls were measurements is a question about the missing-data mechanism, and the missing-data literature's settled result is that this mechanism cannot be recovered from observed data — the 12/12 reversal is exactly as consistent with a fifth cycle that widened its query family as with four cycles that never ran. Iterative search with expanding coverage routinely produces near-total reversals on previously-dry items; this is the normal behaviour of recall improvement, not evidence of dead cycles. Grading the item Critical on this inference converts an ordinary recall finding into an integrity finding, and the remedy the finding points to (execution attestation) is more expensive and less useful than the remedy the actual deficiency points to (log the queries and the raw counts).

**What would need to be true for C2A2 to be safe:** Every monitoring cycle must emit, alongside its verdict, the queries it ran and the pre-filter result counts — the minimal record that makes a null self-authenticating. Given that record, a null is a measurement by construction and the presumption cannot recur.

**How to test:** Re-run the four historical cycles' original query strings verbatim against the same items. If they now return the material the fifth cycle found, the cycles were dark (presumption corroborated). If they return nothing and only the broadened queries hit, the cycles ran and the gain was recall (challenge holds). This is a direct, decisive experiment and should be run before the item is graded.

---

## Search scope

Preliminary. Three query families executed (missing-data identifiability; heartbeat/no-data semantics; reference-free quality estimation). Not searched: systematic-review methodology on search-strategy recall and inter-searcher variability, which is the most on-point literature for the competing explanation and should be added. Broader search recommended.

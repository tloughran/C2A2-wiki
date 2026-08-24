# SYSTEMIC RISK FLAG — 2026-08-17

*Filed by Agent 15b (Literature Search AGAINST), batch A: the five ASSUMPTION items of the 2026-08-16 cohort.*

> **Note on file ownership.** A second 15b instance is covering the PRESUMPTION items of the same cohort and may file a sibling block in this file. This block covers **only** the five ASSUMPTION items assigned to batch A (1106, 1108, 1112, 1116, 1117) and was written without any coordination. If a second block appears below, both stand; neither supersedes the other.

---

## SYSTEMIC-RISK-FLAG (block 1 of n — batch A, ASSUMPTION items)

**Date:** 2026-08-17

**Affected items:** ASSUMPTION-1106, ASSUMPTION-1108, ASSUMPTION-1112, ASSUMPTION-1117 (four of five; ASSUMPTION-1116 is affected by the *second* vulnerability below but not the first)

**Risk level:** **Critical**

---

### Common vulnerability 1 — ONE MECHANISM, FOUR ITEMS, ALREADY MINTED

**The mechanism:** *An instrument that did not perform its check emits an outcome indistinguishable from an instrument that performed the check and found nothing.*

All four items are the same failure on four different instruments:

| Item | Instrument | Non-execution | Emitted outcome |
|---|---|---|---|
| **1106** | anti-fabrication guard | splitter returns zero sentences on unpunctuated ASR (66/307 = 21.5%) | `last_qc_outcome: pass` |
| **1108** | review pass-marking | identifier existence checked, content not | `pass` (asserting an untested assertion) |
| **1112** | citation guard | from-the-thinker check and URL-resolves check do not read metadata | citation accepted |
| **1117** | monitoring cadence | search step did not execute (17/17) | "stable, no new sources" |

The four were filed as four findings across three subject areas (QC, review, citation integrity, monitoring). They are one finding, and the fleet's own register named it **twelve days earlier**:

> **PREMISE-142** (2026-08-05, from PRESUMPTION-666, ACTIVE): "A status report is a two-stage inference — ascertain the true state, then report it — and **the first stage is the one that fails silently** (Snow & Keil)... **THEREFORE THE OUTPUT VOCABULARY MUST BE THREE-VALUED: SUCCEEDED / FAILED / NO-EVIDENCE, and every status claim must carry an evidence pointer (which artifact, which timestamp). A binary vocabulary forces the aggregator to render an absence as a positive assurance**, which is what it did — it named a specific run successful that had terminated with no output, and **a false particular is harder to unwind than a silence**."

PREMISE-142 is not adjacent to these items. It is a complete description of all four, with the remedy specified and the reason given. Two further ACTIVE premises complete the picture:

- **PREMISE-113** (2026-07-21): "**a post-fix reading of zero is indistinguishable from a detector that now detects nothing**... precision AND recall must be reported separately against a corpus containing known-genuine and known-clean cases before any result is read as evidence about the corpus rather than about the instrument."
- **PREMISE-131** (2026-07-28, EXTERNALLY ANCHORED, High): "**A WARNING IS NOT A CONTROL, AND AN UNDELIVERED WARNING IS NOT A MITIGATION**... a warning carried on a delivery channel that has failed has **ZERO effect, not reduced effect**."

And the follow-up obligation is already minted too:

- **PREMISE-118** (2026-07-21, Moderate-High, ISO/IEC 17025 §§7.10, 8.7 and NIST GMP 11): on finding an instrument out of tolerance — "contain / assess impact / fix cause / verify, including a **RETROSPECTIVE impact assessment over every result produced since last known-good calibration**," bounded by "(i) the obligation is **ASSESSMENT, not automatic invalidation**."

**Literature basis (external, from the four search files):**
- Snow, A.P. & Keil, M. (2002), "A Framework for Assessing the Reliability of Software Project Status Reports," *Engineering Management Journal* 14(2) — the two-stage inference, via PREMISE-142's evidence column [cited from register; not independently verified].
- Chandra, T.D. & Toueg, S. (1996), "Unreliable Failure Detectors for Reliable Distributed Systems," *JACM* 43(2) — a crashed process cannot be distinguished from a slow one; the absence of an event is not an event [snippet level].
- Sadowski, C. et al. (2018), "Lessons from Building Static Analysis Tools at Google," *CACM* 61(4) — the "**effective false positive**" concept: a true finding a reader did not act on counts as a false positive; the <10% trust threshold [snippet level].
- Clinical-laboratory validity-control practice (APHL toolkit; IVD package inserts) — three printed outcomes, POSITIVE / NEGATIVE / **INVALID**, with mandatory repeat [snippet level].
- CDC IGRA guidance and the indeterminate-result meta-analysis — indeterminate is explicitly **not** positive; follow-up is risk-stratified; ~50% resolve on repeat [snippet level].
- Walters, W.H. & Wilder, E.I. (2023), *Scientific Reports* 13 — among **non-fabricated** LLM citations, 43% (GPT-3.5) / 24% (GPT-4) carry substantive metadata errors [snippet level; primary not read].

**Why this is Critical rather than High:** the fleet is currently four items away from minting up to four new premises for a mechanism it already holds, each of which would prescribe a *local* remedy (change the severity schema; deepen review; build a date guard; change the monitoring trigger). Four local remedies for one mechanism is the worst available outcome: it costs four times, fixes the mechanism nowhere, splits the register, and — per PREMISE-138's bar on re-minting — leaves near-duplicate items giving divergent guidance. Note also the asymmetry the items do not state: three of the four instruments emitted a **neutral** false pass; ASSUMPTION-1117's monitor emitted a **positive assurance about the external world** ("no new sources"), which is 142's "false particular" and is the most expensive form.

**Recommendation for common vulnerability 1:**
1. **Do not mint 1106, 1108, 1112 or 1117 as new premises.** File all four as *instances* under PREMISE-142, which already contains the mechanism, the vocabulary and the reason.
2. **Apply PREMISE-142's three-valued vocabulary and evidence pointer across all four instruments in one change**: QC outcomes, review outcomes, citation verification, monitoring reports. Every status claim carries which artifact, which timestamp, which query; `NO-EVIDENCE` is available and is never rendered as a pass.
3. **Discharge PREMISE-118 once, for all four**: a retrospective impact assessment over results since last known-good calibration — the 66 transcripts, the pass-marked days, the citation corpus, the seventeen monitored items — held to 118's bound that the obligation is *assessment, not automatic invalidation*.
4. **Publish every yield with its denominator** (PREMISE-168). All four items report numerators only: 66/307 is the exception, and 17/17, "four days," and the single citation instance are not rates.
5. **Where a schema change is proposed, check it against the alert-fatigue envelope first.** Converting non-execution into failure at 21.5% (1106) sits far outside Google's <10% effective-false-positive threshold and inside the 49–96% override band that produces documented paradoxical harm.

---

### Common vulnerability 2 — THE INTAKE GATE IS THE DEFECT, AND IT IS NOW A MEASURED PATTERN

**The mechanism:** *Remedies are drafted before anything checks what the register already decided.*

This is **OPEN-153 / REVISE-340**, carried on the intake itself: "remedies are drafted before anything checks what the register already decided. Four correctives this cohort were proposed against premises that explicitly exclude them... **Treat these ten items as subject to the same defect until the gate is fixed.**" The intake declares the defect and cannot fix it, because PREMISE-096 forbids 14a/14b from amending their own intake gate.

**What batch A measured.** I ran the register pre-check the intake declares it omitted, on all five items. Result: **5 of 5 items had ACTIVE governing premises that were not consulted**, and in four of five the register's answer was *more specific and differently directed* than the item's own corrective.

| Item | Governing ACTIVE premises found by the omitted pre-check | Register's answer vs item's corrective |
|---|---|---|
| 1106 | 142, 131, 118, 113, 047, 011 | Three-valued vocabulary + retrospective assessment — **not** "make it fail" |
| 1108 | 148, 142, 132, 118, 113 | Relabel the assertion + measure the re-performer — **not** "review deeper" |
| 1112 | 132, 148, 142, 101 (+ CheckIfExist, CiteAudit logged in-register) | Decorrelated internal check, available today — **not** a new class |
| 1116 | 005 re-check note (correlated-model convergence is not independence) | Two agents from one source file are **one** line of evidence |
| 1117 | 142, 165, 113, 118, 047 + the register's own Monthly/Quarterly cadence | Fix the search step — **not** replace the clock |

**The 1116 case is the sharpest and it is qualitatively different.** There the unchecked item is not a premise but a **fact in the vault**. The network's evidence that its Rohr↔Stump finding was new is a grep proving "univocity"/"Scotus" appear nowhere in `traditions/rohr/`. The mirror grep on `traditions/stump/` — `analog(y|ical) (of being|predicat)|analogia|univoc` — returns **nothing**. The Stump tradition records no commitment to analogical predication of being anywhere. An incompatibility was filed at High priority with its second conjunct unverified, by a procedure that had the verification tool in hand and ran it on one side only.

**Literature basis:** the register's own PREMISE-005 re-check note — "**correlated LLM errors (Kim et al. ICML 2025) mean same-model-family convergence is NOT independent evidence; count same-mechanism/same-family lines as one**" [cited from register; not independently verified] — bears directly on 1116, where "two agents independently surfaced" the finding while both worked from the same proposal file and inherited its framing.

**Why this is Critical:** the gate defect is now measured at 5/5 on an independent batch, having been reported at 4/10 on the previous cohort. It is not drift; it is the standing behaviour of the intake. Every downstream cost in vulnerability 1 — four premises minted for one mechanism — is *produced* by vulnerability 2.

**Recommendation for common vulnerability 2:**
1. **Fix the gate, not the items.** The intake names the fix ("two lines in the 14a/14b contracts") and names why the agents cannot apply it (PREMISE-096). This requires an actor above 14a/14b. Until it is applied, every cohort will arrive pre-defective and 15a/15b will keep paying the cost downstream.
2. **Make the pre-check mechanical and two-sided.** A grep of `validated_premises.md` on the item's own keywords, results pasted into the item, before it is graded. Recall is ~56% (ASSUMPTION-1052), so it is a lower bound — but 5/5 says a 56%-recall check would still have caught most of this.
3. **For any claimed incompatibility between two traditions, require the absence-grep on BOTH traditions before filing.** Cheap, mechanical, and it would have caught 1116 on the day.
4. **Down-weight same-source multi-agent convergence,** per PREMISE-005's own note. Two agents reading one proposal file are one line of evidence, and 1116 was graded partly on their agreement.
5. **Regrade after the pre-check, not before.** Three of these five carry priority gradings (Critical, High, High) set against an unread register. 1112's "new class" is the clearest case: it is new relative to two named guards and to nothing else.

---

### What is NOT flagged

Three things in this cohort survive both vulnerabilities and should not be swept up:

- **The measurements themselves.** 66/307 is a real coverage figure. 17/17 is a real failure count. The four defective pass-marks are real. The citation date error is real. Every one of these is worth more than the doctrine wrapped around it, and none is challenged by anything in the five files.
- **ASSUMPTION-1117's severity.** Its monitor emitted a positive assurance about the world, not a neutral pass. On PREMISE-142's own reasoning that is the most expensive class of failure and should be repaired first.
- **ASSUMPTION-1116's instinct.** Staging a doctrinal tension rather than smoothing it was the right call, and the general worry behind it — that the network has 103 cross-connections and no field recording whether agreement is at the level of the words or of the commitments — is untouched by my challenge to this particular tension.

---

*Filed by Agent 15b. Five items searched; four external sources fetched and read in full across the batch; the remainder snippet-level or cited from the register with markers in each file. Per the 15b contract I report evidence and do not make design recommendations beyond what the literature and the register state; the reconciliation and the status determination belong to 14a.*

---
---

## SYSTEMIC-RISK-FLAG (block 2 of n — batch B, PRESUMPTION items)

*Filed by a second Agent 15b instance covering the five PRESUMPTION items of the 2026-08-16 cohort. Written without reading `lit_search_results/for/` and without coordination with the author of block 1 beyond reading block 1 itself, which is 15b's own output. Block 1 stands unaltered; this block adds two vulnerabilities it does not cover and independently replicates its central measurement on a disjoint set of items.*

**Date:** 2026-08-17

**Affected items:** PRESUMPTION-818, PRESUMPTION-819, PRESUMPTION-820, PRESUMPTION-824, PRESUMPTION-827 (five of five)

**Risk level:** **Critical**

---

### Common vulnerability 3 — FIVE ITEMS, FIVE PROPOSED RECORDING FIELDS, AND THE EVIDENCE SAYS FIELDS SATURATE WITHOUT EFFECT

**The mechanism:** *When this fleet finds that an instrument's output was uninformative, its default remedy is to add a field describing what the instrument did — and the literature on self-declared process description reports that such fields reach near-total population while the effect they certify stays flat.*

Every item in batch B proposes, or implies, a new record of process:

| Item | The finding | The proposed record |
|---|---|---|
| **818** | `warn` collapses three states | a fourth severity state |
| **819** | four runs went mute | a self-report clause / an external heartbeat signal |
| **820** | four pass-marks predated their defects | a **METHOD** field on the review verdict |
| **824** | 17/17 cadence ticks recorded nothing | (self-demonstrating — see below) |
| **827** | 103 connections, agreement level unknown | a **lexical-vs-substantive** field |

**The evidence against the pattern, assembled across the five files:**

- **Urbach, D.R. et al. (2014), *NEJM* 370:1029–1038** [snippet level] — >100 Ontario hospitals, mandatory surgical safety checklists, **self-reported compliance over 90% at almost all participating hospitals**, complications 3.86%→3.82% and 30-day mortality 0.71%→0.65%, neither significant. A self-declared process field at steady state: saturated, stable, and uninformative about the outcome.
- **Inozemtseva, L. & Holmes, R. (2014), ICSE 2014:435–445** [snippet level] — coverage is the software world's *machine-measured* method field, and it shows only "low to moderate correlation" with fault detection once suite size is controlled, with stronger coverage criteria adding no further insight. If the measured version barely predicts detection, a prose version written by the reviewer will not.
- **"On the unreliability of bug severity data"** (*Empirical Software Engineering*; authorship not verified this run) [snippet level] — raters do not agree on the severity grades that already exist, and the resulting datasets are unreliable as data. Adding a grade that requires the hardest judgement in the set (*why did this instrument produce no reading?*) inherits that.
- **ISA 230 / PCAOB inspection practice** [snippet level, canonical] — documentation and performance diverge in **both** directions: findings raised where the work was adequate, because "inspectors can only evaluate what the file contains." The profession's actual assurance mechanism is **re-performance**; the method record is its input, not its substitute.

**And the register refused this remedy once already, in writing:**

> **PREMISE-109** (ACTIVE): "**INSTRUMENTATION CONSTRAINT (load-bearing): the measure is CLAIMS-WITHOUT-EVIDENCE (per claim, is there a named artifact and timestamp that would have to hold?), never a read-set coverage percentage. Coverage rises when a summarizer reads more marginal artifacts without reading the decisive one, is unbounded over a growing vault, and would read green during exactly the failure it was built to catch.**"

> **PREMISE-137** (ACTIVE): "**an unvalidated invariant adds perceived coverage without detection, which is worse than the gap it was added to close.**"

**The self-demonstrating case, and it is why this is Critical rather than High.** PRESUMPTION-824's entire finding is that an **existing** recording field — the cycle counter, the `next_check` date, the carry-over count — records nothing about the monitored item. 151 items advanced on it in one night. The cohort has therefore *documented a field that saturated and carried no information*, and in the same cohort proposes four more fields of the same construction. Nothing in the four proposals distinguishes them from the one that failed.

**Recommendation for common vulnerability 3:**
1. **No new descriptive field is admissible without three things attached:** (a) a **defined automatic response** when the field takes each value (ISA-18.2 rationalisation in miniature — cause, consequence, corrective action, time to respond); (b) a **measured assignment reliability** (two decorrelated instances grade the same 30 items; report agreement); (c) a **measuring** check rather than a describing one — re-performance sampling (820), mutation validation (PREMISE-137, for 818/819), or a precision sample (827).
2. **Prefer forced action over richer labels.** The clinical-laboratory analogue that 818 correctly reaches for does not work because INVALID is a better word than NEGATIVE; it works because INVALID triggers a **mandatory repeat**, and repeat resolves >90% of invalid results.
3. **Where a field already exists and records nothing, fix or delete it before adding a sibling.** The cycle counter is the test case and it is in this cohort.

---

### Common vulnerability 4 — SMALL-N CAUSAL INFERENCE WITH NO CONTROL ARM, CARRYING CRITICAL AND HIGH GRADINGS

**The mechanism:** *Each item derives a general causal or structural conclusion from a handful of same-day, non-independent, non-randomly-selected observations, and four of the five gradings (two Critical, two High) rest on those inferences rather than on the measurements.*

| Item | The inference | The problem |
|---|---|---|
| **818** | "Today's three instances show it cannot" | Two of three are the same morning's work on one corpus; one of those is a *false-positive* problem pointing the opposite way; the third (226 out-of-band days) is arguably the schema working. **Effectively n=1.** |
| **819** | Four mutes + one no-op ⇒ observed reliability exceeds actual "by an amount nobody can currently bound" | **No denominator** (PREMISE-168). The flagship instance is n=2 ("stalled silently anyway, twice"). Unboundedness is an artefact of not having measured; deadline assertions produce the denominator in a week. |
| **820** | Four pass-marked defects ⇒ "the 307-pair corpus has no known quality level at all" | The four were found by **targeted re-examination** — a non-random sample establishing existence, not rate. And the conclusion is false as stated: the rule of three (Hanley & Lippman-Hand, *JAMA* 1983) bounds the rate at ~3/n for every class the check *can* detect. |
| **824** | "The variable is the search, not the time" | **Perfectly confounded.** The searched items had also waited five cycles; the unsearched arm at cycle 0 was never run. "Falsified twice" is two replications of one condition, not two conditions. |
| **827** | One metaphysical check dissolved one match ⇒ an unknown fraction of 103 may be verbal, graded **Critical** | **n=1**, the check was run on **one side** of a two-sided claim (the mirror grep on `traditions/stump/` returns nothing — block 1), and the metaphysical premise doing the dissolving is a **contested** scholarly thesis (Cross vs Pickstock, *Antonianum* 2001/2003). |

The register already governs this: **PREMISE-168** (publish every yield with its denominator), **PREMISE-136** (every settling quantity must declare its scope so its achievable denominator is visible at drafting time, with the scope guard that small n does not make a quantity undecidable — it makes the interval wide, and reporting a wide interval honestly is admissible where a point estimate is not), **PREMISE-129** (a formal claim is settled by derivation and an independent check, not by a stated verdict).

**Why this is Critical:** the *measurements* in this cohort are excellent — 66/307, 17/17, 151 carry-overs, 103 connections — and the *gradings* are attached not to the measurements but to causal readings of them that no design in the cohort can identify. Two Critical and two High priorities are currently allocated on unidentified inferences, and priority allocation is how this fleet decides what to build.

**Recommendation for common vulnerability 4:**
1. **Grade on the measurement, not on the inference.** 66/307 is a coverage figure and stands on its own; "every clean report in this system is an upper bound on defects" is a conclusion needing a denominator.
2. **Run the missing arm before minting the rule** — the cycle-0 search (824), the deadline-assertion week (819), the random re-review sample (820), the 20-connection precision sample (827). Every one of these is a single run.
3. **Report wide intervals rather than nothing** (PREMISE-136's scope guard). "No known quality level at all" and "an amount nobody can currently bound" are both refusals to compute a bound that is computable.

---

### Independent replication of block 1's central measurement

Block 1 reported that the omitted register pre-check, run on the five ASSUMPTION items, found **5 of 5** with ACTIVE governing premises unconsulted. I ran the same pre-check on the five PRESUMPTION items, without knowledge of block 1's result until after my own greps were complete, and got the same figure.

| Item | Governing ACTIVE premises found by the omitted pre-check | Register's answer vs the item's corrective |
|---|---|---|
| **818** | 142, 131, 102, 113, 118 | Three-valued vocabulary **already minted** (142); the design variable is a defined response per grade, not the number of grades |
| **819** | **086**, 100, 142, 089, 110, 053 | PREMISE-086 already holds the age-alarm dead-man's-switch **and** the monitor-of-monitor conditional — this is a **deployment gap, not a knowledge gap** |
| **820** | 101, **109**, 137, 113, 118 | (scope, method, time) already minted (101); a coverage-style self-descriptive metric already **refused** (109); the mechanism is re-performance |
| **824** | **095**, 053, 106, 089 | Arrival rate exceeds service rate; queue grows without bound absent **cadence change / admission cap / provisioning** — three levers, none of them abolition |
| **827** | **042, 043**, 049, 005, 129 | The register holds the **opposite error profile** at High confidence: lexical matching here is high-precision, **low-recall**, and systematically **undercounts** convergence |

**Combined across both blocks the cohort measures 10 of 10.** That is no longer a tendency; it is the intake's standing behaviour, and it is OPEN-153 / REVISE-340 confirmed on a second disjoint sample.

**The 827 row is qualitatively worse than the rest and deserves separate notice.** It is not an omission but an **inversion**. PREMISE-043 (High, anchored on Manning, Raghavan & Schütze) holds that the lexical connection layer is a high-precision *lower bound* whose known weakness is recall; PREMISE-042 (anchored on Gentner's structure-mapping and Hofstadter & Sander) holds that literal overlap systematically *undercounts* genuine convergence because real convergence is analogical. PRESUMPTION-827 grades **Critical** on the premise that the same instrument *manufactures* connections. Both error modes can coexist, but the register's holding is documented, externally anchored and ACTIVE, and the item's is one unreplicated instance whose metaphysical premise is contested in print and whose corpus check was run on one side only. **PREMISE-042's quarterly re-check falls on 2026-08-21 — four days after this search — and is the natural and correct place to reconcile the two rather than minting a contradictory item beside them.**

---

### What is NOT flagged

- **The measurements.** 66/307, 17/17, 151 carry-overs, four pass-marked defects, 103 connections with no relation field — every one is real, none is challenged by anything in the five files, and each is worth more than the doctrine built on it.
- **PRESUMPTION-819's clause (A).** "The remedy adopted in both cases is a clause instructing the component that failed to report its own failure" is correct, is structurally void for a component whose failure mode is non-execution, and is the sentence in this cohort most worth putting on a wall. PREMISE-131 already classifies it: an administrative control, the second-least-effective tier.
- **PRESUMPTION-827's instinct.** The network genuinely cannot distinguish a shared word from a shared commitment, and the Philippians 2:12–13 case — two thinkers reaching for one verse "with no evidence of contact," filed as a convergence — is exactly the case where the two come apart. The challenge is to the flagship instance, the error-profile assumption and the Critical grading, not to the observation.
- **PRESUMPTION-824's coverage finding.** 17 of 17 items ticked without being searched is a real coverage failure on a real denominator, and it is the same mechanism as block 1's vulnerability 1 wearing a scheduling costume.

---

*Filed by Agent 15b (batch B). Five items searched. Two external sources fetched and read in full this run — Alpern & Schneider (1985), "Defining Liveness," IPL 21(4), and Lyonhart (2024), Religions 15(8):994, whose substantive sections carry three primary Scotus quotations; all other external citations in the five files are snippet-level or canonical-not-re-verified, and each is marked as such in place. Per the 15b contract I report evidence and do not make design recommendations beyond what the literature and the register state; reconciliation and status determination belong to 14b.*

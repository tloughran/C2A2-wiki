# 2026-10-15 — lit pipeline: concurrent second instance, CONFLICT, results NOT applied

PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c (this instance; withdrawn)] | Items: PRESUMPTION-1141, PRESUMPTION-1146 | Transform: orchestrator conflict report | Status: NOT APPLIED — for Tom

## What happened
- This instance wrote `lit_pipeline.lock` LOCKED at 04:34:38Z (00:34 local) and backed up the five registers (`*.bak.20261015-pre-15pipeline`, taken before either instance wrote).
- A second instance of `c2a2-lit-search-pipeline` committed at 00:38:13 local without honouring that lock. It dispositioned PRESUMPTION-1141 → MONITOR-691 (DISPOSITION-1085) and PRESUMPTION-1146 → REVISE-518 (DISPOSITION-1086).
- This instance appended its own DISPOSITION-1085/1086 and REVISE-518 at 00:38:55, then detected duplicates and **removed its own appends** (lit_search_returns.md −9,784 B; revision_flags.md −2,921 B). The other run's entries were not edited. Rule: surface conflicts, don't average (10-01 precedent).
- **Data loss:** the other run overwrote this instance's four 15a/15b result files (8–9 KB each, abstract/full-text reads) with its own 2–3 KB files (title-level). This instance's SYSTEMIC-RISK flag is moved here: `2026-10-15_withdrawn_SYSTEMIC-RISK-FLAG_unaudited-observation-channel.md`.

## Where the runs disagree
| Item | Committed run | This run (withdrawn) |
|---|---|---|
| P-1141 | 15a PARTIAL (Weak) / 15b PARTIAL-CHALLENGED (Moderate), both title-level → **MONITOR-691** | 15a PARTIAL (Moderate narrow; Weak as operated; None for attribution), Saltzer et al. 1984 read in full / 15b CHALLENGED (Moderate-Strong), W3C PROV-Overview read in full → **REVISE** (new flag: run record per artifact; valid artifact without own run record = UNATTRIBUTED, not PASS) |
| P-1146 | **REVISE-518** (new; registry-based sampling frame) | Same direction, but **attached to REVISE-515** (coverage-stated negatives) instead of minting a new number |

The root of the disagreement is evidence depth. The committed run's searchers made 2 searches each and 0 fetches. This run read abstracts and full text (Saltzer 1984, W3C PROV, Haddaway 2015, Lewandowski & Mayr 2006, Pirkola 2009). Both runs agree that neither presumption holds as operated.

## Decisions for Tom
1. P-1141: keep MONITOR-691, or upgrade it to REVISE using the action text below.
2. P-1146: keep REVISE-518 standalone, or fold it into REVISE-515.
3. The lock was ignored, the second time (after 10-01) that a concurrent run overwrote result files. Find the duplicate scheduler entry (cloud/local twin? cf. ASSUMPTION-1776) and disable one. Alternatively, have result files use run-unique names.

## Withdrawn register text (this instance)
### Withdrawn from lit_search_returns.md
```
## 15a/15b/15c RUN — 2026-10-15 (scheduled c2a2 lit-search pipeline; NEW 14a/14b intake of 2026-10-14, 2 literature items: PRESUMPTION-1141, PRESUMPTION-1146)
Scope: the two literature items in the 2026-10-14 local intake. Its 17 [IN-HOUSE] items are not literature-lane and were not searched. The 133-item bare backlog (queue_scan.py: 120 from 2026-07, 7 from 2026-08, 6 from 2026-10 incl. these 2) was not touched beyond these two; batch kept small given the standing token-overrun items (ASSUMPTION-1783).
15a and 15b ran as separate subagents in parallel; neither read the other's directory. Same model family, so independence is partial (cf. PREMISE-234, REVISE-488). Shared sources counted once by 15c: Saltzer, Reed & Clark 1984 (15a read in full; 15b summaries only) and Martín-Martín et al. 2018 (both snippet). 15b filed SYSTEMIC-RISK (High): lit_search_results/against/SYSTEMIC-RISK-FLAG_2026-10-15_unaudited-observation-channel.md.

### 15a returns (FOR)
RETURN-TO-14b:
  Original item: PRESUMPTION-1141
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate (narrow claim: strong independent output checks can verify correctness); Weak (as operated: timestamp/syntax checks); None (attribution)
  Key source: Saltzer, Reed & Clark 1984, "End-to-End Arguments in System Design," ACM TOCS 2(4) [read in full]; Blum & Kannan 1995 JACM [snippet]; McConnell et al. 2011 "Certifying Algorithms" [snippet]
  Summary: The end-to-end argument, program result checking and certifying algorithms support checking outputs instead of tracing processes, but only with strong, independent checks (checksum against source, witness, schema plus statistical bounds). No source treats timestamps or syntax as such a check, and none says output checks can show which job wrote an artifact.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-1141_for.md
  PROVENANCE: Origin: 14b | Chain: [14b → 15a] | Original item: PRESUMPTION-1141 | Item type: PRESUMPTION (unstated — surfaced by inference) | Transform at this step: literature search for supporting evidence (2026-10-15) | Current status: PARTIALLY-SUPPORTED

RETURN-TO-14b:
  Original item: PRESUMPTION-1146
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Weak
  Key source: Haddaway et al. 2015, PLOS ONE [abstract + conclusions read]; Martín-Martín et al. 2018, J. Informetrics [snippet]; Google Search Central 2019 "evergreen Googlebot" [snippet, vendor doc]
  Summary: Web search works reasonably well for known-item retrieval of a prominent author's formally published, well-linked work. The same studies report gaps for grey, organisation-hosted and recent material, and no source supports reading zero hits as the author's silence. NOVELTY: no (narrow gap: LLM-agent search coverage of individual-author recent output is unstudied).
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-1146_for.md
  PROVENANCE: Origin: 14b | Chain: [14b → 15a] | Original item: PRESUMPTION-1146 | Item type: PRESUMPTION (unstated — surfaced by inference) | Transform at this step: literature search for supporting evidence (2026-10-15) | Current status: PARTIALLY-SUPPORTED

### 15b returns (AGAINST)
RETURN-TO-14b:
  Original item: PRESUMPTION-1141
  Search direction: AGAINST (challenging)
  Result: CHALLENGED
  Strength: Moderate-Strong (conceptual case strong; no study measuring how often output checks miss process faults)
  Key source: Groth & Moreau (eds.) 2013, W3C PROV-Overview [read in full]; Barr et al. 2015, "The Oracle Problem in Software Testing," IEEE TSE 41(5) [abstract]
  Summary: Provenance standards treat "which agent and run produced this" as information the artifact's content cannot supply. Syntax and timestamp checks are weak oracles that accept plausible-but-wrong or stale output, so output validation does not replace process provenance, especially with twin writers. STEELMAN: the end-to-end argument favours endpoint checks, but only strong ones.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-1141_against.md
  PROVENANCE: Origin: 14b | Chain: [14b → 15b] | Original item: PRESUMPTION-1141 | Item type: PRESUMPTION (unstated — surfaced by inference) | Transform at this step: literature search for challenging evidence (2026-10-15) | Current status: CHALLENGED

RETURN-TO-14b:
  Original item: PRESUMPTION-1146
  Search direction: AGAINST (challenging)
  Result: CHALLENGED
  Strength: Strong (convergent lines; some sources dated or not peer-reviewed)
  Key source: Lewandowski & Mayr 2006, "Exploring the Academic Invisible Web" [abstract]; Lewandowski et al. 2006 / Lewandowski 2008 freshness studies, J. Inf. Sci. [snippet]; Pirkola 2009, Information Research 14(2) [abstract]; Bućko 2022 (Onely) JS crawl delay [read; industry]
  Summary: Search indexes are incomplete, lag by days to weeks, favour well-linked HTML and return non-reproducible results, so web search is a biased sampling frame for an author's recent work. Reporting "nothing new" as the thinker's silence is unsupported and likely uneven across thinkers. STEELMAN: tracked thinkers are prominent, well-linked English-language figures, the population search covers best — but that still does not license "no hits = silence".
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-1146_against.md
  PROVENANCE: Origin: 14b | Chain: [14b → 15b] | Original item: PRESUMPTION-1146 | Item type: PRESUMPTION (unstated — surfaced by inference) | Transform at this step: literature search for challenging evidence (2026-10-15) | Current status: CHALLENGED

### 15c dispositions (2026-10-15)
DISPOSITION-1085:
  Date: 2026-10-15 | Item: PRESUMPTION-1141 | Item type: PRESUMPTION (unstated — surfaced by inference)
  15a: PARTIALLY-SUPPORTED (Moderate narrow / Weak as operated / None attribution) | 15b: CHALLENGED (Moderate-Strong)
  Net assessment: The two directions converge. Output checking can stand in for process tracing only when the check is strong and independent of the producer (end-to-end argument, result checking); the checks actually used (file timestamp, syntax) are weak oracles, and no output check can say which of two twin jobs wrote the file (W3C PROV models attribution separately because content cannot carry it). The presumption as operated is not supported.
  Disposition: REVISE (REVISE-518)
  Reasoning: Heuristic "PRESUMPTION with strong challenge → lean REVISE" applies; 15a's own support is explicitly conditional on checks C2A2 does not run. The correctness limb is already covered by PREMISE-231 (existence ≠ freshness ≠ correctness) and PREMISE-236; the new content is attribution, which no existing PREMISE covers, so no INCORPORATE was minted for the narrow limb. Consistency: compatible with PREMISE-231/232/236/237; no contradiction. Urgency set Medium, not High: 14b rated risk-if-wrong Medium and no study measures the miss rate.
  What is at risk: Telemetry PASS rows and any health verdict built from artifact checks while cloud/local twins overlap (ASSUMPTION-1776, ASSUMPTION-1811, OPEN-260); a broken extractor hidden behind a twin's or a stale success.
  Recommended action: see REVISE-518.
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Original item: PRESUMPTION-1141 | Item type: PRESUMPTION (unstated — surfaced by inference) | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED
  Results: wiki/architecture/lit_search_results/for/PRESUMPTION-1141_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-1141_against.md

DISPOSITION-1086:
  Date: 2026-10-15 | Item: PRESUMPTION-1146 | Item type: PRESUMPTION (unstated — surfaced by inference)
  15a: PARTIALLY-SUPPORTED (Weak; known-item retrieval of well-linked published work only) | 15b: CHALLENGED (Strong)
  Net assessment: Clear asymmetry. 15a's best support covers known-item retrieval of formally published work, which is not the operated use (discovering unknown recent output, including Substack/JS/members-only material). Both sides agree that zero hits cannot be read as the thinker's silence. Martín-Martín 2018 appears on both sides at snippet level, counted once.
  Disposition: REVISE — ATTACHED TO REVISE-515 (no new REVISE number minted). "Nothing new" from a search-only channel is a negative reported without its coverage, which is exactly REVISE-515's rule; this is also the 10-12 SYSTEMIC-RISK pattern "silence read as evidence".
  Reasoning: Weak support + strong challenge on a PRESUMPTION → REVISE. A new number would duplicate REVISE-515 (AWAITING-TOM, High). The attachment adds the tradition-agent instance and its specific mitigation (per-thinker direct channels). Consistency: compatible with PREMISE-230 (a null counts only if the instrument could have observed the outcome).
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Original item: PRESUMPTION-1146 | Item type: PRESUMPTION (unstated — surfaced by inference) | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED (attached to REVISE-515)
  Results: wiki/architecture/lit_search_results/for/PRESUMPTION-1146_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-1146_against.md

15c response to SYSTEMIC-RISK-FLAG_2026-10-15_unaudited-observation-channel: accepted. Both items are one design gap — a verdict from presence/absence of an observation without a record of how the observation was produced. REVISE-515 (coverage stated with every negative) plus REVISE-518 (run record with every artifact) together cover it; no third flag minted.

Running totals after this run: PREMISE-237 (unchanged) | MONITOR-690 (unchanged) | REVISE-518 (1 new; 1 attachment to REVISE-515) | DISPOSITION-1086.
```

### Withdrawn from revision_flags.md
```
# ==== 2026-10-15 15c (append-only; entries above not edited) ====

REVISE-518:
  Date: 2026-10-15 | Source: DISPOSITION-1085 (15c) | Item: PRESUMPTION-1141 (PRESUMPTION (unstated — surfaced by inference))
  What is at risk: Telemetry PASS and other health verdicts built from artifact timestamps/syntax while cloud/local twins overlap; a broken job hidden behind a twin's or a stale success. ASSUMPTION-1776; ASSUMPTION-1811; OPEN-260; cf. PREMISE-231.
  Recommended action: Each scheduled job writes a minimal run record at write time (job, run ID, host/twin, start/end, output content hash; inputs where cheap) beside or inside the artifact. PASS requires the job's OWN run record for this run plus a content check at PREMISE-231's correctness rung; a valid artifact with no matching run record is reported UNATTRIBUTED, never PASS. Distinct output paths or an exclusive-writer lock per twin until ASSUMPTION-1776 is decided. Tom to choose scope (all jobs vs telemetry-bearing jobs first).
  Urgency: Medium
  Status: AWAITING-TOM
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Original item: PRESUMPTION-1141 | Item type: PRESUMPTION (unstated — surfaced by inference) | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED
  Results: wiki/architecture/lit_search_results/for/PRESUMPTION-1141_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-1141_against.md ; SYSTEMIC-RISK: lit_search_results/against/SYSTEMIC-RISK-FLAG_2026-10-15_unaudited-observation-channel.md

REVISE-515: [ATTACHMENT 2026-10-15, DISPOSITION-1086 ← PRESUMPTION-1146]
  Instance: tradition agents report "nothing new" / 0 proposals from search-surfaced links only (d487abb2; McGilchrist Substack unread).
  Evidence this cycle: 15b CHALLENGED (Strong) — Lewandowski & Mayr 2006 [abstract]; Lewandowski freshness studies [snippet]; Pirkola 2009 [abstract]; Bućko 2022 [industry]. 15a PARTIALLY-SUPPORTED (Weak) — known-item retrieval only.
  Added mitigation for this instance: per-thinker channel registry (RSS/Atom incl. Substack /feed, author/lab pages, podcast/video feeds, arXiv/ORCID/Crossref author queries); report "no new items found via [channels], checked [date]"; paywalled/unindexed channels are NOT-INSPECTED, never counted as silence. Coverage likely uneven across thinkers, so per-tradition proposal counts should not be compared until channels are listed.
  Also answers SYSTEMIC-RISK-FLAG_2026-10-15_unaudited-observation-channel jointly with REVISE-518.
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Original item: PRESUMPTION-1146 | Item type: PRESUMPTION (unstated — surfaced by inference) | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED (attached)
  Results: wiki/architecture/lit_search_results/for/PRESUMPTION-1146_for.md ; wiki/architecture/lit_search_results/against/PRESUMPTION-1146_against.md
```
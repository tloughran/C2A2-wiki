SYSTEMIC-RISK-FLAG:
  Date: 2026-10-02
  Raised by: 15b (Literature Search AGAINST)
  Affected items: PRESUMPTION-1103, PRESUMPTION-1104, PRESUMPTION-1105 (ASSUMPTION-1730 adjacent; see below)

  PROVENANCE:
    Origin: 15b
    Chain: [14b → 15b]
    Original items: PRESUMPTION-1103, PRESUMPTION-1104, PRESUMPTION-1105
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-10-01 sessions (lit-pipeline concurrent-run conflict and related).
      15b: Cross-item synthesis after disconfirmatory searches on 2026-10-02; all three CHALLENGED.
    Current status: FLAGGED

  Common vulnerability: Agents treat a shared artefact as having one coherent state with no coordination primitive. The artefact may be a queue item's meaning (1103), a register file's contents (1104), or the inclusion rule for a corpus (1105). Each agent acts on its own reading or its own write, and nothing checks afterwards that the readings matched, that writes did not collide, or that discretionary departures were not skewed. In each case the failure is silent. Two divergent tests look like evidential disagreement, a lost update looks like "never written", and a skewed exception set looks like corpus structure.

  Literature basis:
    - Cemri et al. 2025, "Why Do Multi-Agent LLM Systems Fail?" arXiv:2503.13657 (specification issues + inter-agent misalignment + missing verification as top-level MAS failure categories). VERIFIED.
    - Data-Wise/craft PR #288 (2026): 40/80 lost writes under unlocked tmp-and-mv by agent-issued shell; a hidden second writer. VERIFIED.
    - Cochrane Handbook v5.1 §2.1: post hoc inclusion decisions "highly susceptible to bias"; document and run sensitivity analyses. VERIFIED.
    - Yang et al. 2025, arXiv:2505.13360 (underspecified prompts unstable across model/prompt changes). VERIFIED (abstract via search).
    - Simmons, Nelson & Simonsohn 2011 (undisclosed flexibility). VERIFIED (bibliographic).

  Risk level: High

  Recommendation (what the system should consider; not a design prescription): Treat cross-agent agreement and write integrity as properties that must be checked, not assumed. Candidates from the literature: a structural single target per item, echoed and compared at reconciliation; single-writer or locked/CAS registers plus a run lock against duplicate instances; recorded and set-reviewed discretionary exceptions. Each of these replaces silent divergence with a detectable event.

  Relation to existing flags (checked by filename only; contents not read): May overlap with SYSTEMIC-RISK-FLAG_2026-10-01_silence-read-as-health.md (silent failure read as success) and SYSTEMIC-RISK-FLAG_2026-09-10_no-second-look_1297-939-940-944.md (unaudited decisions). Neither filename names the concurrency/coordination mechanism, so this is minted as a new flag. A reconciler may choose to fold it in as an extension. ASSUMPTION-1730 (a daily SELECT 1 "succeeds" while the pause criterion may not be met) fits the silence-read-as-health pattern better than this one and is noted there as a candidate, not filed.

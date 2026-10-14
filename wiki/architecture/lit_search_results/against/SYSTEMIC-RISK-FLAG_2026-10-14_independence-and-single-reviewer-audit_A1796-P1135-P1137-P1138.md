PROVENANCE:
  Origin: 14a (ASSUMPTION-1796); 14b (PRESUMPTION-1135, PRESUMPTION-1137, PRESUMPTION-1138)
  Chain: [14a → 15b]; [14b → 15b]
  Original items: ASSUMPTION-1796, PRESUMPTION-1135, PRESUMPTION-1137, PRESUMPTION-1138
  Item type: mixed — ASSUMPTION (stated); PRESUMPTION (unstated — surfaced by inference)
  Transform at each step:
    14a/14b: Extracted/inferred from 2026-10-13 transcripts and wiki files.
    15b: Searched for challenging literature; cross-item synthesis by 15b (scheduled unattended run, 2026-10-14).
  Current status: SYSTEMIC-RISK-FLAG (High)

SYSTEMIC-RISK-FLAG:
  Date: 2026-10-14
  Affected items: ASSUMPTION-1796, PRESUMPTION-1135, PRESUMPTION-1137, PRESUMPTION-1138
  Common vulnerability: All four turn on the same two hidden conditions. (1) INDEPENDENCE: whether layered proxies (1796), overlapping monitors (1135) and summary-derived cards (1137) reduce error depends on their failures being uncorrelated; in C2A2 these checks are mostly produced by the same model family reading the same files, which is the textbook setting for common-mode failure. (2) A SINGLE GROUND-TRUTH CHANNEL: the only check "against reality" for proxies (1796), the only consumer who can reconcile monitor FAILs (1135), the only gate on paratext-derived cards (1137) and the server of the proposal queue (1138) is the same human reviewer — and that channel currently shows no decisions since 10-09. The literature's escape routes from each concern (validated surrogates, redundancy, triage-then-full-text, batch catch-up) all presuppose that this channel has spare capacity.
  Literature basis: Knight JC & Leveson NG 1986 (IEEE TSE 12(1)) — independently built versions fail coincidentally far above independence; Sagan SD 2004 (Risk Analysis 24(4)) — redundancy breeds common-mode error and social shirking; Landau 1969 / Bendor 1985 — redundancy raises reliability only under independence; Buyse et al. 2000 (Biostatistics) — surrogates need at least one outcome calibration; Little 1961 / queueing stability (ρ < 1); Sjøberg 2018 (ESEM) — WIP-limit benefits empirically unsettled. All at snippet/abstract level except Sjøberg (abstract read).
  Risk level: High
  Recommendation: Treat "how independent are our checks?" and "what is the reviewer's actual decision capacity?" as shared upstream questions to be measured once, rather than re-litigated item by item. Candidate measures: per-check data-source diversity (are two checks reading the same log/file?); a shared ground-truth sample of known past failures scored against every monitor/proxy; and weekly arrival-vs-decision rate for the human gate. (15b reports literature, not designs; these are offered as tests, per the STEELMAN "How to test" convention.)

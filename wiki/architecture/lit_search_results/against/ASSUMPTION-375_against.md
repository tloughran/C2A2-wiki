SEARCH-AGAINST-ASSUMPTION-375:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-375
  Original statement: "Peak-hour torn copies are environment (WAL checkpoint) contention, not a code defect; the 06:15 quiet window is the right production posture"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-375
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: torn copies attributed to environment, not code; quiet-window adopted as posture
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. SQLite backup-API guidance vs naive copy. - If torn copies come from copying a hot DB without the snapshot API, the root cause is the COPY METHOD (code), not the environment; contention only changes how often the latent defect manifests. "Not a code defect" is likely a misdiagnosis.
    2. Heisenbug / probabilistic-failure literature. - Attributing an intermittent fault to "contention" and mitigating by reducing load is a classic way to mask, not fix, a deterministic defect; the bug remains and resurfaces when load returns.
    3. Off-peak scheduling as probabilistic mitigation. - Choosing a quiet window lowers failure PROBABILITY but provides no guarantee; relying on it as "the right posture" substitutes luck for correctness.

  Strength of challenge: Moderate-Strong

  Summary: The diagnosis "environment, not code" is the weak point. The torn-copy literature says a hot-DB copy taken without the backup API is a deterministic defect whose visibility is merely modulated by contention; moving to 06:15 reduces the manifestation rate without removing the cause. Declaring it environmental risks closing the issue on a probabilistic mitigation while the real fix (snapshot-API copy + completeness validation) goes unmade.

  Specific risks: Latent torn-copy bug persists; resurfaces whenever the window stops being quiet (see PRESUMPTION-407); a code/method defect is mis-booked as an irreducible environment cost.

  Mitigations available: Switch to backup API / VACUUM INTO and re-test AT PEAK; if torn copies vanish regardless of hour, the cause was method (code), not contention; keep the quiet window only as defense-in-depth, not as the fix.

  STEELMAN:
    Item: ASSUMPTION-375
    Strongest counterargument: "Environment, not code" is the kind of attribution that quietly converts a fixable deterministic bug into an accepted operational constraint; the quiet window mitigates symptoms while the actual defect (copy method) survives untouched and re-emerges with load.
    What would need to be true for C2A2 to be safe: A snapshot-API copy produces consistent results at PEAK; i.e., the failure is genuinely load-dependent even with a correct copy method.
    How to test: Run the corrected copy method at peak and measure torn-copy rate; a zero rate falsifies the "environmental" diagnosis.

  Search scope: WAL contention vs copy method; intermittent-fault attribution; off-peak mitigation limits. Comprehensive.

  Recommendation: CHALLENGED

SEARCH-AGAINST-PRESUMPTION-1081:
  Date searched: 2026-09-24
  Original item: PRESUMPTION-1081
  Original statement: [inferred] Both large-db jobs presume a full copy of the database fits in
    scratch space. The db grows ~60-70 MB a day, and the shortfall against 5.9 GB free widens
    daily. (Tested formulation: a copy-whole-then-read pattern for growing databases fails on a
    predictable date given the growth rate and scratch size.)

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1081
    Item type: PRESUMPTION (unstated, surfaced by inference)
    Transform at each step:
      14b: Inferred the full-copy presumption behind connect_ro and the metabolism copy.
      15b: Searched for challenging literature (lane: capacity planning; snapshot ETL scalability)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (challenges "predictable date", not "fails")

  Sources:
    1. Beyer, B. et al. (eds.) (2016). Site Reliability Engineering, "Introduction: Demand
       Forecasting and Capacity Planning". sre.google. [Fetched.] Capacity plans must model organic
       growth (steady adoption) and inorganic growth (launches, business-driven changes)
       separately, and need load testing to map raw capacity to service capacity. A single linear
       growth rate misses step changes, such as a new ingestion source or a backfill.
    2. SQLite project. "Write-Ahead Logging" (sqlite.org/wal.html). [Fetched.] The -wal file can
       grow without bound under checkpoint starvation or large write transactions. Copies that
       include or checkpoint the WAL therefore vary in size from day to day, not along the
       db-size trend line.
    3. SQLite project. "Online Backup API". [Fetched.] VACUUM INTO is listed as a consistent-copy
       alternative. Its output drops free pages, so the copy's size is the live-data size, not the
       file size. The failure date therefore depends on the freelist, which a file-size trend does
       not show.
    4. Disk-forecast practice sources (SolarWinds, Stedman Solutions, ManageEngine; seen in search
       results; vendor pages, not relied on for claims). Prediction intervals widen with horizon.
       Forecasts need months of history to be reliable.

  Strength of challenge: Weak-to-Moderate

  Summary: Nothing found challenges the core point: a copy-whole pattern against a growing source
  and fixed scratch space eventually fails. Here it is already failing (7.2 GB vs 5.9 GB). What is
  challenged is "on a predictable date". The effective copy size is not the file-size trend. It
  depends on the freelist (VACUUM INTO compacts), on WAL state at copy time, on other tenants of
  scratch space, and on inorganic growth steps. So the failure boundary is a band, not a date:
  runs can fail before the trend-line date (a WAL spike, other scratch use) or succeed after it
  (compaction). This matters for any "fix" that restores headroom. It will fail intermittently
  first, and that is harder to diagnose than a clean cutoff.

  Specific risks: A headroom fix (clearing scratch, compaction) is taken as having bought "N days"
  and then fails early and intermittently. The intermittent failures look like flakiness, feed
  PRESUMPTION-1083-style normalization, and delay abandoning the copy-whole pattern.

  Mitigations available: Drop the copy-whole pattern (read in place, export needed subsets). If a
  copy is kept, monitor copy size against scratch space as a ratio with an alert well below 1.0,
  and measure live-data size (page_count minus freelist_count), not file size.

  Search scope: Preliminary: 2 searches plus reuse of 3 fetches from ASSUMPTION-1663.

  Excluded results: SolarWinds, PRTG/Paessler, ManageEngine and Stedman Solutions disk-forecast
  pages (vendor); USPTO patent PDFs on storage forecasting (not evidence of practice); oneuptime.com
  and thesimplifiedtech.com blogs; Medium summaries of the SRE book (the primary was fetched).

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1081
  Strongest counterargument: "Fails on a predictable date" overstates how regular the failure is.
    The quantity that must fit is the effective copy size: live pages plus WAL state plus
    concurrent scratch use. None of these tracks the db file's trend line. Capacity practice warns
    that single-rate forecasts miss step growth. In practice the pattern fails in a band of
    intermittent failures, not at a clean cutoff. A system that expects a date will read early
    failures as noise.
  What would need to be true for C2A2 to be safe: Either the pattern is abandoned, or the monitored
    quantity is the effective copy size, alerted as a ratio to scratch space with margin.
  How to test: Log (page_count − freelist_count) × page_size, the -wal size, and free scratch space
    at each run start for two weeks. Compare the variance against the linear trend.

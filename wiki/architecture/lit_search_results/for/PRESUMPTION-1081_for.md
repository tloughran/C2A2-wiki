SEARCH-FOR-PRESUMPTION-1081:
  Date searched: 2026-09-24
  Original item: PRESUMPTION-1081
  Original statement: A copy-whole-then-read pattern for growing databases fails on a predictable date
    given the growth rate and scratch size.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1081
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred the unstated presumption that full-copy snapshotting has a computable failure date.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Prometheus project, "Query functions" documentation (prometheus.io/docs/prometheus/latest/
       querying/functions/; seen in search, not fetched). — predict_linear() predicts a series value t
       seconds ahead by simple linear regression; the canonical use is alerting when a filesystem
       will fill within N hours. Established practice that storage exhaustion is forecastable from
       growth rate.
    2. Beyer, B., Jones, C., Petoff, J. & Murphy, N.R. (eds.), 2016. Site Reliability Engineering:
       How Google Runs Production Systems. O'Reilly. — Lists demand forecasting and capacity
       planning as core SRE responsibilities: ensure sufficient capacity for projected future demand.
    3. US patent family "Capacity forecasting for backup storage" (USPTO documents 8688927, 9063839,
       9251051; seen in search, assignee unconfirmed). — Extrapolates a linear regression of backup
       storage use to the point where capacity is reached (x = (y − α)/β) to obtain an exhaustion
       date. Direct precedent in the backup/snapshot domain.
    4. SQLite project, "SQLite Backup API" (sqlite.org/backup.html; fetched). — A backup produces a
       full copy of the source; hence scratch demand grows one-for-one with database size.

  Strength of support: Moderate

  Summary: Capacity-planning practice treats storage exhaustion under steady growth as a
    deterministic, forecastable event, with standard tooling (linear extrapolation, time-to-full
    alerts) and patented methods specifically for backup storage. Because a copy-whole snapshot
    requires scratch at least equal to the (growing) database size, the failure date follows directly
    from growth rate and scratch capacity. The presumption is an application of well-established
    practice rather than a novel claim.

  Caveats: Predictability depends on growth being roughly linear/stationary; bursts, VACUUM-driven
    shrinkage, WAL growth during the copy, and competing scratch consumers make the date a band, not a
    point. Sources establish forecasting practice generally; none studies snapshot-based ETL on SQLite
    specifically.

  Search scope: Preliminary — three searches (capacity/disk-exhaustion forecasting; Prometheus
    predict_linear; SRE capacity planning).

  Excluded results: oneuptime.com posts (vendor blog, including a 2026-09-15 capacity-exhaustion
    post), KodeKloud notes, Medium SRE post, dbi-services and Robust Perception blogs (secondary
    practitioner blogs; official docs used instead); VictoriaMetrics GitHub alerts file (GitHub).

  Recommendation: SUPPORTED

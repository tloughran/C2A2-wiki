SEARCH-AGAINST-ASSUMPTION-445:
  Date searched: 2026-07-12
  Original item: ASSUMPTION-445
  Original statement: "BOSCO archive completeness is established by fetched-count equaling the enumerated total (30,529/30,529)."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-445
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-11 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [dbSeer, "Data Migration Validation Guide"; Airbyte, "How to Validate Data Integrity After Migration." — The very literature that endorses count reconciliation classifies it as the FIRST layer only: counts detect dropped batches, and are explicitly documented as blind to content corruption, truncation, and — critically — enumeration gaps. "Complete" claims require the further layers (checksums, field-level checks, independent totals).]
    2. [Hook, E.B. & Regal, R.R., 1995 (and IJE 23(6):1111 review). "Capture-recapture methods and registry completeness." — A count produced by the same process being audited cannot certify that process's coverage; missingness in the enumeration source is undetectable from within. 30,529/30,529 verifies the fetch loop against the enumeration, and says nothing about whether the enumeration saw every message.]
    3. [Internal precedent: PRESUMPTION-473 / the 307/307 case. — C2A2's own record contains a self-produced N-of-N completion figure that is known wrong — a live, in-house counterexample to "fetched-count = enumerated-total establishes completeness."]
  Strength of challenge: Strong
  Summary: The challenge is structural: the claim's denominator is self-produced. Fetched=enumerated is genuine evidence of zero fetch-loop loss, but "archive completeness is established" requires the enumeration itself to be complete, which nothing checked — provider-side enumeration can silently exclude folders, date ranges, spam/trash, or messages the API declines to list. Migration-validation doctrine explicitly reserves "complete" for multi-layer verification, and the system's own 307/307 known-wrong precedent shows exactly this failure mode already occurred in-house. Because "complete" is a terminal state, an error here has no remaining detection path — the strongest reason to demand the independent count before declaring it.
  Specific risks: Permanently missing messages with no future audit trigger; downstream analyses silently built on a gapped archive.
  Mitigations available: One independent count (provider-side mailbox total via a different interface, or IMAP folder counts) settles it permanently — cheap relative to the archive's permanence.

  STEELMAN:
    Item: ASSUMPTION-445
    Strongest counterargument: N/N where the denominator comes from the same session that produced the numerator is a tautology dressed as a verification — the archive is being graded against its own answer key. The literature's completeness layers exist because every migration that lost data quietly also reported matching counts against its own enumeration. Terminal states deserve the strongest check precisely because they end all future checking; here the check applied was the weakest.
    What would need to be true for C2A2 to be safe: The enumerated total is corroborated by at least one independent source before "complete" becomes a terminal status.
    How to test: Provider-side or independent mailbox count vs the archive's total (already the queued test); any discrepancy → enumerate the difference set.
  Recommendation: CHALLENGED

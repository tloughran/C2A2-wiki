SEARCH-AGAINST-PRESUMPTION-1207:
  Date searched: 2026-11-02
  Original item: PRESUMPTION-1207
  Original statement: A reading that departs sharply from the previous one is presumed to be a measurement fault, and is then explained away or dropped.
  Claim tested (literature): whether treating sharp departures as faults is reasonable or necessary practice.
  Reading used for the AGAINST direction: evidence that suspecting a fault first is a sound default (faults are common; alarm fatigue punishes over-reaction), so the practice is not a flaw as such.
  Search scope: PRELIMINARY. 3 web searches, 0 fetches (same searches serve both directions; run by one orchestrator, so independence is procedural only: this file was written without reading the 15a file). Title-only hits. Not reached: sensor-fault vs event discrimination papers, base rates of connector/lookup failures.
  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15b
    Original item: PRESUMPTION-1207
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: inferred from connector health dropping a 0-connector reading as a failed lookup
      15b: Searched for challenging literature (preliminary; 3 searches, 0 fetches)
    Current status: PARTIALLY-CHALLENGED
  Challenging evidence found: Partial (weak)
  Sources:
    1. NIST/SEMATECH e-Handbook of Statistical Methods, outlier detection https://itl.nist.gov/div898/handbook/eda/section3/eda33e8.htm [title only] - standard guidance treats outlier screening as legitimate, provided it is documented. Challenges the claim that dismissing outliers is itself the flaw; the flaw is silent dismissal.
    2. Alarm-fatigue review https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9424650/ [title only] - the literature's concern is too many false alarms; a policy of escalating every sharp departure would worsen it. Cuts against a blanket reading of the presumption.
    3. Faults are common in real sensor/lookup systems [from memory, unsourced here]: in a connector lookup, a transient failure is often the more probable explanation, so a fault-first prior can be correct.
  Strength of challenge: Weak
  Summary: Nothing found says fault-first handling is wrong. The challenge is to the framing: the default can be rational when faults are common, and escalating everything has its own cost. The failure the item describes occurs where the dismissal is final and unlogged.
  Specific risks: A real drop (e.g. connectors actually disconnected) is read as a fault and never surfaces; the monitor reports health when it is blind.
  Mitigations available: Verify the fault hypothesis (retry the lookup, second source) before dropping; record every rejected reading with its reason and a later outcome; track the confirmed-fault rate so the prior can be tested.
  Recommendation: PARTIALLY-CHALLENGED
  STEELMAN:
    Item: PRESUMPTION-1207
    Strongest counterargument: In an unattended monitor a sharp jump from one reading is far more often a failed call than a real change; treating it as a fault is the correct Bayesian default, and alerting on each one trains the owner to ignore alerts. The presumption is only a defect if faults are rarer than the agents act as if.
    What would need to be true for C2A2 to be safe: Dismissals are verified or at least logged with a reason, and the confirmed-fault rate is measured and high enough to justify the prior.
    How to test: In-house: count readings dropped as faults since 09-01 and how many were later confirmed (the item's own in-house limb; not run).
  SYSTEMIC-RISK note: possible echo of 'a named check treated as a check performed' (a dropped reading counted as checked); not flagged, single-item evidence.

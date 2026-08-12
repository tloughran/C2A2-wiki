# PRESUMPTION-771 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-771

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-771

**Original statement:** That two runs meeting on the same file is redundancy rather than contention — two collisions in one day against a convention-only mitigation.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from two same-day write collisions that a convention-only coordination scheme is inadequate; risk graded High.
  - 15b: Searched for challenging literature on optimistic concurrency control, the contention regimes in which it is preferred, and the failure modes locks and leases introduce.
- **Current status:** CHALLENGED

**What is being challenged:** the inference that two collisions per day indicates inadequate coordination. Optimistic, convention-only coordination is the *recommended* design in exactly the low-contention regime that two collisions per day describes; the diagnostic question is whether collisions are detected, not whether they occur.

### Challenging evidence found: Yes

### Sources

1. **Kung, H.T. & Robinson, J.T., 1981. "On Optimistic Methods for Concurrency Control." *ACM Transactions on Database Systems* (doi:10.1145/319566.319567).** — The foundational result: two families of non-locking controls that permit transactions to proceed unsynchronised and validate at commit, appropriate where "conflicts are rare," yielding higher throughput than locking by avoiding lock management and lock waiting entirely. Directly challenges the presumption: at low contention the optimistic scheme is not a weak substitute for locking, it is the superior choice, and occasional collisions are the expected and priced-in cost.
2. **Optimistic concurrency control survey material (Wikipedia, "Optimistic concurrency control"; Brewer, CS262 lecture notes, UC Berkeley; Grokipedia entry) — [secondary sources, verified as describing the Kung–Robinson result].** — Consistent statement that OCC is used specifically in low-contention environments and that its critical requirement is a *validation* phase that detects conflicts at commit time. This relocates the correct question from "are there collisions?" to "does the system have a validation phase?"
3. **"Improved optimistic concurrency control and its use in distributed database systems," IEEE (ieeexplore.ieee.org/abstract/document/11850).** — Extends OCC to distributed settings, confirming that the optimistic posture remains the recommended baseline for distributed multi-writer workloads rather than being confined to single-node databases.
4. **Helland, P., 2007. "Life Beyond Distributed Transactions: An Apostate's Opinion." CIDR 2007 / *CACM* (doi:10.1145/3009826).** — Documents that pessimistic coordination across distributed writers degrades availability and scalability because of "strict locking requirements combined with slow and unreliable network-based communication." Challenges the presumption's implied remedy: introducing locks or leases imports lease-expiry, stale-lock, and liveness failures that convention-only coordination does not have.

### Strength of challenge: Moderate

### Summary

The literature reframes the finding rather than denying it. Optimistic concurrency control exists precisely for workloads where conflicts are rare, and its central claim — established since 1981 and unchallenged for that regime — is that avoiding lock management outperforms preventing conflicts when the conflict rate is low. Two collisions in one day, against whatever the total write volume was, is prima facie the low-contention regime, and in that regime "convention-only mitigation" is not a gap in the design; it is the design the field would recommend. What the literature *does* insist on, and what the presumption does not distinguish, is the validation phase: OCC is only sound because conflicting transactions are detected at commit and backed out. So the load-bearing question is how the two collisions were found. If a validation mechanism detected them, the scheme is working as designed and the presumption's High grading is unsupported. If they were found by accident — noticed by a human, or inferred from a corrupted artefact — then C2A2 has the optimistic posture without the validation phase, which is the genuinely unsafe configuration, and the finding is correct but for a different reason than stated. The presumption does not report which, and that omission is the weakest point in the item.

### Specific risks

If the presumption drives adoption of locks or leases at this contention level, C2A2 imports the failure modes Helland catalogues — a run that dies holding a lock blocks all successors, and lease expiry under variable run durations produces either premature revocation or long stalls. Given PRESUMPTION-770 in this same batch (sessions dying mid-run), a lock-based scheme is specifically contraindicated: dying writers and mandatory locks compose into deadlock. If the finding is dismissed without checking for a validation phase, then lost updates continue to occur and go undetected, which is the worse error because it is silent.

### Mitigations available

(a) Determine whether a validation phase exists — did something *detect* the two collisions, or were they noticed? This single question determines whether the item is closed or escalated. (b) If validation is absent, add the cheap OCC-standard version: a content hash or mtime read before write, compared at write time, with backoff and retry on mismatch. This is optimistic, needs no coordinator, and is immune to dying writers. (c) Do not add mandatory locks; if exclusion is ever required, prefer a short lease with automatic expiry well under a typical run duration, and accept the resulting spurious revocations. (d) Measure the conflict rate as a fraction of writes, so the regime is established empirically rather than by count.

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-771

**Strongest counterargument:** A database engineer would say the presumption has misread which variable matters. Kung and Robinson's result — that optimistic, non-locking coordination beats locking when conflicts are rare — makes "convention-only mitigation" the *correct* choice for a workload producing two collisions a day, not a shortfall, and Helland's later work explains why the pessimistic alternative is actively worse for distributed writers: locks plus unreliable participants plus dying processes yields blocked successors and lost liveness. The presumption's own evidence, read against the literature, is closer to a validation of the current design than an indictment of it. The one question the literature says actually determines safety — does a validation phase detect conflicts at write time? — is the question the item does not ask. Two collisions *detected* is a healthy optimistic system; two collisions *stumbled upon* is an optimistic system missing its validation phase, which is unsafe and would be unsafe at any contention level. Escalating on the collision count instead of on the validation question risks the specific bad outcome of adding locks to a system whose runs are known to die mid-flight.

**What would need to be true for C2A2 to be safe:** A pre-write validation step must exist — read a version marker (hash or mtime) at the start of a write-modify cycle and verify it is unchanged at write time, retrying on mismatch — and the conflict rate must remain low enough that retries do not dominate. Under those conditions convention-only coordination is not merely acceptable but preferable.

**How to test:** Two measurements. First, reconstruct how each of the two collisions was discovered; if neither was reported by an automated check, the validation phase is absent and that is the finding. Second, instrument writes to count conflicts as a fraction of total writes over a week. Below roughly a percent, the optimistic regime is confirmed and the challenge holds; materially above, contention is real and coordination merits redesign — but even then leases, not locks, given that runs die.

---

## Search scope

Moderate. Query families executed: optimistic concurrency control foundations and contention regimes; distributed-transaction critique. Not searched: the lease-management literature (Gray & Cheriton leases; Chubby/ZooKeeper operational experience) and the CRDT/conflict-free replication literature, which would supply the strongest alternative to both convention and locking. Broader search recommended for mitigation design.

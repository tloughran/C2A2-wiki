SEARCH-AGAINST-ASSUMPTION-318:
  Date searched: 2026-06-16
  Original item: ASSUMPTION-318
  Original statement: "Files-added/day is the right headline yield series for the Metabolism view (better proxy than tokens/commits)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-318
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-15 session (Metabolism headline metric choice)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Construct-validity critique of count metrics (stackoverflow.blog 2020; "Teaching Software Metrology," arXiv:2406.14494). — "Simple productivity measures such as counting commits or modified lines of code suffer from low construct validity." Files-added is the same family: it counts a byproduct (artifacts emitted), not the construct of interest (knowledge yield/value). Calling it the "right" headline overstates a low-validity proxy.
    2. Goodhart's / Campbell's Law (Hillel Wayne, "Goodhart's Law in Software Engineering"; Typo, "Goodhart's Law"). — "When a measure becomes a target, it ceases to be a good measure." A HEADLINE series is the one most likely to become a target (it is what the dashboard foregrounds and what the user will steer toward), so promoting files-added to headline status maximizes Goodhart exposure for the weakest-validity quantity.
    3. Counter-metric requirement (Java Code Geeks 2026; GitVelocity vanity-metrics). — "The antidote to Goodhart's Law is to never use a single metric in isolation... a system of counter-metrics." A single headline series violates this directly; files-added with no paired counter-metric (size, depth, rework, deletion) is a vanity metric.

  Strength of challenge: Strong

  Summary: The challenge is strong on construct validity and Goodhart exposure: files-added is a low-validity byproduct proxy, and elevating it to the single HEADLINE series both overstates its meaning and creates the worst conditions for metric gaming (the foregrounded number becomes the target). The literature's standing prescription — never a single metric, always counter-metrics — is violated by a lone headline series. The comparative claim (better than tokens/commits) may hold, but "least-bad proxy" is not "right headline metric."

  Specific risks: The user (its only audience) begins to optimize file count — splitting work into more files, creating thin artifacts — inflating the series while real yield is flat or declining. The Metabolism view then reports increasing "metabolism" that is partly an artifact of responding to its own headline. If the series is ever wired to an optimizer/bandit (the project has contemplated this — MONITOR-335/REVISE-103), the Goodhart failure becomes automated.

  Mitigations available: Demote from sole headline to one of several co-equal series; pair with counter-metrics (median file size, net lines after deletions, rework rate, distinct-area coverage); label it explicitly as a descriptive activity proxy, not a yield/value measure; hard-rule against feeding it to any optimization layer until validated (couples REVISE-103).

  STEELMAN:
    Strongest counterargument: For a private, single-user reflective dashboard with no external incentive attached, Goodhart pressure is minimal (the user gains nothing by gaming themselves), and a simple, legible activity series is more useful than a complex composite the user won't trust or read. As a DESCRIPTIVE pulse — "did I make things this week?" — files-added is fit-for-purpose and the comparative claim against tokens/commits is correct.
    What would need to be true for C2A2 to be safe: The series must stay descriptive (never an incentive or optimizer input), be paired with at least one counter-metric so inflation is visible, and be labeled as activity-not-value.
    How to test: Track files-added against an independent value signal (e.g., later PRS-triplet completions, or human-rated weekly progress) for a quarter; correlation near zero confirms low construct validity and argues for demotion.

  Search scope: Construct validity of productivity proxies, Goodhart/Campbell's law in software metrics, vanity-metric and counter-metric literature. Comprehensive. (Couples PRESUMPTION-349, the commensurability substrate.)

  Recommendation: PARTIALLY-CHALLENGED

SEARCH-AGAINST-PRESUMPTION-464:
  Date searched: 2026-07-10
  Original item: PRESUMPTION-464
  Original statement: "The daily-walk Chat is the sole canonical human-context channel and browser delivery its only transport; on failure, waiting is the only remedy."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-464
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference from 2026-07-09 EOD cohort
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. [Rocket.Chat blog. "In-band vs Out-of-band communication in incident response: which is better?" — Relying on a single channel for critical communication is identified as a dangerous single point of failure; only ~9% of organizations avoid network outages in an average quarter, so single-transport designs are expected to be severed regularly.]
    2. [TrustedSec. "To OOB, or Not to OOB? Why Out-of-Band Communications are Essential for Incident Response." — Establishes the design norm: critical human-communication paths need an alternative technology outside the primary system, available before the primary fails — "waiting" is explicitly not an incident-response strategy.]
    3. [HipLink. "The Evolution of Critical Alerting: From Paging Roots to Multi-Channel Resilience." — Multi-channel delivery (app, SMS, voice, email) is framed as "resilience by design"; the industry moved away from single-transport delivery precisely because any one transport fails.]
    4. [ArmorText. "Look Who's Talking About Out of Band Comms." — Post-CrowdStrike-2024 analyses: organizations whose only human-coordination channel rode the affected infrastructure lost their coordination capability exactly when they needed it; the lesson drawn industry-wide is pre-provisioned secondary channels.]
    5. [VoiceDrop. "Send Automated IT Outage Notifications When Slack Is Down." — Practical pattern literature: cellular/SMS/voice paths independent of the primary transport are the standard remedy for primary-channel outage, demonstrating that "only transport" is a choice, not a constraint.]

  Strength of challenge: Strong

  Summary: The operations literature treats single-channel, single-transport human communication as a recognized anti-pattern with a standard name (single point of failure) and a standard remedy (out-of-band, multi-channel redundancy provisioned in advance). Survey data cited in the OOB literature indicates transport outages are routine, not exceptional, so a design whose only remedy is waiting will predictably and repeatedly sever the human-in-the-loop link. The CrowdStrike 2024 outage is the era-defining case study: coordination channels that shared fate with the failed infrastructure left teams unable to communicate during the one period communication mattered most. For C2A2, whose human context arrives through one Chat over one browser transport, every browser/client/platform failure silently cuts the only human feed, and the system has institutionalized passivity ("waiting") as its response.

  Specific risks: During any browser or platform outage the human operator's context, corrections, and priorities stop reaching the system; agents proceed on stale human intent (or stall), and time-sensitive human input (e.g., "stop doing X") is undeliverable — the severed link is invisible from inside the system because absence of messages is indistinguishable from absence of instruction.

  Mitigations available: Pre-provision at least one secondary ingest channel for human context (e.g., a watched file/directory the human can write to directly, an email-to-file bridge, or a second chat surface) with an explicit precedence rule; add a heartbeat convention so the system can distinguish "human silent" from "channel dead"; document a manual fallback procedure the human can execute without the browser.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Availability engineering has spent two decades converging on one rule for critical communication: never depend on a single transport, and never discover you need the backup during the outage. A single browser-delivered Chat as the sole human-context channel violates both halves, and "waiting" as the failure remedy means the system's human-in-the-loop guarantee is void for the duration of any client-side fault — the class of fault most likely to occur. The cost of a second channel (a watched file the human can edit) is trivially low relative to the cost of a severed human link.
    What would need to be true for C2A2 to be safe: Browser/Chat delivery would need availability high enough that outages are shorter than the acceptable human-context staleness window, and no time-critical human instruction may ever coincide with an outage — assumptions the outage-frequency data contradict.
    How to test: Log Chat-delivery failures over a month and measure severed-link duration against the longest tolerable human-silence window; run a drill where the human must deliver an urgent instruction with the browser unavailable and time how long it takes to land.

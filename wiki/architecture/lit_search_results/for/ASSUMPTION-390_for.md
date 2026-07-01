SEARCH-FOR-ASSUMPTION-390:
  Date searched: 2026-06-30
  Original item: ASSUMPTION-390
  Original statement: "Liveness of the OpenStory activity feed does not imply liveness of the PRS/signals approval axes — feeds are independent (one current through today, the others frozen 6–12 days)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-390
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-29 self-awareness cohort (metabolism-axis / liveness / push-pattern review)
      15a: Searched for supporting literature (first-time, genuine web search 2026-06-30)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Elementary Data, "Data Freshness: Best Practices & Key Metrics" — freshness is a PER-SOURCE / per-table property; one pipeline being current says nothing about another. Independent sources require independent freshness tracking.
    2. Sifflet, "What Is Data Freshness in Data Observability" — "stale data looks perfectly normal"; freshness must be measured per dataset because staleness in one feed is invisible from another.
    3. Metaplane, "What is data freshness" & the "data downtime" concept (Moses et al.) — freshness SLAs are defined per source; cross-source liveness inference is an known anti-pattern.

  Strength of support: Strong

  Summary: This assumption is directly and strongly supported by data-observability practice: freshness is a per-source property and the liveness of one feed carries no information about another. Treating OpenStory, PRS, and signals as independently-fresh is exactly correct; inferring all-fresh from one-fresh is the error the assumption guards against.

  Caveats: The assumption is correct AS A NEGATIVE claim (one feed's liveness != others'). The positive obligation it implies — per-axis freshness marking — is the subject of P-422 (separately flagged REVISE).

  Recommendation: SUPPORTED (Strong — per-source freshness independence is standard data-observability doctrine)

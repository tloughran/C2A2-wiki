SEARCH-FOR-ASSUMPTION-1730:
  Date searched: 2026-10-02
  Original item: ASSUMPTION-1730
  Original statement: Supabase free-tier projects pause after 7 days of inactivity, and a daily `SELECT 1` prevents the pause.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1730
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the keep-warm task prompt (1c750b65).
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Supabase docs, "Project Pausing". https://supabase.com/docs/guides/platform/free-project-pausing [fetched] — Free project inactive if it lacks 'sufficient user database activity over the past week'; 'a few user requests to the database each day over the previous week is enough'; dashboard visits and API calls listed as activity; warning email about a week before pause.

  Strength of support: Moderate

  Summary: The roughly one-week inactivity window is confirmed and regular daily database requests are documented as sufficient. The docs do not say whether an internal SELECT 1 counts as 'user database activity', and no official statement endorses keep-alive pings.

  Caveats: Fetch summarized by a small model; verify wording on the page. 'Pause after 7 days' is approximately right, not a stated exact figure.

  Search scope: preliminary search — broader search recommended (1 search, 1 fetch); web-only; fetched pages passed through a summarizing model, so wording is paraphrase.

  Recommendation: PARTIALLY-SUPPORTED

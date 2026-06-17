/* C2A2 Heartbeat — public client config.
 * These are PUBLISHABLE credentials, safe to ship in a public repo: the
 * publishable/anon key only permits what row-level security allows, and all
 * user_preferences rows are owner-only via RLS. The service-role key is never
 * placed here. To rotate, replace the key below and in Supabase project settings.
 */
window.HB_CONFIG = {
  supabaseUrl: "https://akhcocmgfwybdovqeovd.supabase.co",
  supabaseKey: "sb_publishable_D58-hPgxlOSAz5VQNzkXHA_RKya1-x5"
};

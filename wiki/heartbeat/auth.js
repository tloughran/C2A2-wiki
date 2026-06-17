/* C2A2 Heartbeat — optional account layer (Phase 2b).
 *
 * Adds magic-link sign-in (Supabase Auth) and syncs the reader's preference lens
 * to a per-user `user_preferences` row (RLS: owner-only). It is strictly additive:
 * if the Supabase CDN or config is missing (e.g. file://), this module no-ops and
 * the tab keeps working with the per-device localStorage lens from app.js.
 *
 * Contract with app.js (loaded first):
 *   window.HB_getPrefs()      -> current lens object
 *   window.HB_setPrefs(obj)   -> adopt a lens (merges + re-renders)
 *   window.HB_onPrefsSaved(p) -> called by savePrefs() on every local change
 */
(function () {
  "use strict";
  var cfg = window.HB_CONFIG || {};
  var authBox = document.getElementById("hb-auth");
  var hint = document.getElementById("lens-hint");

  // Graceful no-op: stay local-only if the SDK or config didn't load.
  if (!cfg.supabaseUrl || !cfg.supabaseKey || !window.supabase || !window.supabase.createClient) {
    return;
  }

  var client = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseKey);
  var user = null;

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c];
    });
  }
  function setHint(t) { if (hint) hint.textContent = t; }

  function renderAuth() {
    if (!authBox) return;
    authBox.hidden = false;
    if (user) {
      authBox.innerHTML =
        '<span class="hb-auth-who">Signed in as <strong>' + esc(user.email) + '</strong> · lens synced</span>' +
        '<button type="button" id="hb-signout" class="hb-auth-btn">Sign out</button>';
      authBox.querySelector("#hb-signout").addEventListener("click", function () { client.auth.signOut(); });
      setHint("synced to your account");
    } else {
      authBox.innerHTML =
        '<form id="hb-signin" class="hb-auth-form">' +
          '<span class="hb-auth-lead">Sign in to sync your lens across devices:</span>' +
          '<input id="hb-email" type="email" placeholder="you@example.com" autocomplete="email" required>' +
          '<button type="submit" class="hb-auth-btn">Email me a sign-in link</button>' +
          '<span id="hb-auth-msg" class="hb-auth-msg" role="status"></span>' +
        '</form>';
      authBox.querySelector("#hb-signin").addEventListener("submit", function (e) {
        e.preventDefault();
        var email = (authBox.querySelector("#hb-email").value || "").trim();
        var msg = authBox.querySelector("#hb-auth-msg");
        if (!email) return;
        msg.textContent = "Sending link…";
        client.auth.signInWithOtp({ email: email, options: { emailRedirectTo: window.location.href } })
          .then(function (r) {
            msg.textContent = r.error ? ("Error: " + r.error.message)
                                      : "Check your email for the sign-in link.";
          })
          .catch(function (err) { msg.textContent = "Error: " + (err && err.message ? err.message : err); });
      });
      setHint("stored on this device");
    }
  }

  // On sign-in: adopt the account lens if one exists, otherwise seed it from the
  // current device lens (first sign-in carries local preferences up).
  function syncFromAccount() {
    if (!user) return;
    client.from("user_preferences").select("prefs").eq("user_id", user.id).maybeSingle()
      .then(function (res) {
        if (res.error) return;
        var hasRow = res.data && res.data.prefs && Object.keys(res.data.prefs).length;
        if (hasRow) {
          if (window.HB_setPrefs) window.HB_setPrefs(res.data.prefs);
        } else {
          var local = window.HB_getPrefs ? window.HB_getPrefs() : null;
          if (local) {
            client.from("user_preferences")
              .upsert({ user_id: user.id, prefs: local, schema_ver: 1 })
              .then(function () {});
          }
        }
      });
  }

  // Push on every local change while signed in (called by app.js savePrefs()).
  window.HB_onPrefsSaved = function (prefs) {
    if (!user) return;
    client.from("user_preferences")
      .upsert({ user_id: user.id, prefs: prefs, schema_ver: 1, updated_at: new Date().toISOString() })
      .then(function () {});
  };

  client.auth.getSession().then(function (res) {
    user = res.data && res.data.session ? res.data.session.user : null;
    renderAuth();
    if (user) syncFromAccount();
  });
  client.auth.onAuthStateChange(function (_event, session) {
    user = session ? session.user : null;
    renderAuth();
    if (user) syncFromAccount();
  });
})();

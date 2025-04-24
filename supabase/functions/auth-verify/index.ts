// supabase/functions/auth-verify/index.ts
/* deno-lint-ignore-file no-explicit-any */
import { serve } from "https://deno.land/std@0.224.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.42.2";
import { signJwt } from "./jwt.ts";

const supabase = createClient(
  Deno.env.get("SUPABASE_URL")!,
  Deno.env.get("SERVICE_ROLE_KEY")!,
  { auth: { autoRefreshToken: false, persistSession: false } }
);
const JWT_SECRET = Deno.env.get("SESSION_JWT_SECRET")!;

serve(async (req) => {
  const origin = req.headers.get("Origin") ?? "";
  const cors = {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST,OPTIONS"
  };
  if (req.method === "OPTIONS") return new Response(null, { headers: cors });

  try {
    const { idToken } = await req.json();
    if (!idToken) throw new Error("missing-token");

    // 1. Verify Supabase Auth
    const { data: authData, error: authErr } = await supabase.auth.getUser(idToken);
    if (authErr || !authData?.user) throw new Error("invalid-token");
    const u = authData.user;
    const uid    = u.id;
    const email  = u.email!;

    // 2. Safe metadata
    const meta    = u.user_metadata ?? {};
    const name    = typeof meta.full_name  === "string" ? meta.full_name  : email.split("@")[0];
    const picture = typeof meta.avatar_url === "string" ? meta.avatar_url : null;

    // 3. Upsert
    const { data, error: dbErr } = await supabase
      .from("users")
      .upsert({ uid, email, name, picture }, { onConflict: "uid" })
      .select("id")
      .single();
    if (dbErr) throw dbErr;

    // 4. Issue session JWT with Web Crypto
    const payload = {
      sub:  data.id,
      apps: ["AllyFast","AllyScore","AllyStation"],
      exp:  Math.floor(Date.now() / 1000) + 3600  // 1 hour
    };
    const sessionToken = await signJwt(
      { alg: "HS256", typ: "JWT" },
      payload,
      JWT_SECRET
    );

    return new Response(JSON.stringify({ sessionToken }), {
      headers: { "Content-Type": "application/json", ...cors }
    });
  } catch (e: any) {
    return new Response(JSON.stringify({ error: e.message }), {
      status: 401,
      headers: { "Content-Type": "application/json", ...cors }
    });
  }
});

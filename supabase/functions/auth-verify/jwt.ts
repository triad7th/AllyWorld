// supabase/functions/auth-verify/jwt.ts
/* deno-lint-ignore-file no-explicit-any */

// Encode a Uint8Array or string into Base64URL
export function base64Url(input: Uint8Array | string): string {
    const str = typeof input === "string"
      ? input
      : String.fromCharCode(...input);
    return btoa(str)
      .replace(/=/g, "")
      .replace(/\+/g, "-")
      .replace(/\//g, "_");
  }
  
  // Sign a JWT using Web Crypto HMAC-SHA256
  export async function signJwt(
    header: object,
    payload: object,
    secret: string
  ): Promise<string> {
    const enc = new TextEncoder();
    const h64 = base64Url(enc.encode(JSON.stringify(header)));
    const p64 = base64Url(enc.encode(JSON.stringify(payload)));
    const data = `${h64}.${p64}`;
  
    const key = await crypto.subtle.importKey(
      "raw",
      enc.encode(secret),
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign"]
    );
  
    const sigBuffer = await crypto.subtle.sign("HMAC", key, enc.encode(data));
    const signature = base64Url(new Uint8Array(sigBuffer));
  
    return `${data}.${signature}`;
  }
  
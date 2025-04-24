import { VERIFY_URL } from "../config";

export async function exchangeToken(idToken) {
  const res = await fetch(VERIFY_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ idToken }),
    credentials: "include"          // future-proof if you switch to cookies
  });
  if (!res.ok) throw new Error("SSO verify failed");
  const { sessionToken } = await res.json();
  localStorage.setItem("aw_session", sessionToken);
  return sessionToken;
}

import { useState } from "react";
import { signInWithEmailAndPassword, createUserWithEmailAndPassword } from "firebase/auth";
import { exchangeToken } from "../utils/auth";

export default function AuthEmail({ auth, onFinish }) {
  const [email, setEmail] = useState("");
  const [pass,  setPass]  = useState("");
  const [err,   setErr]   = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      let cred;
      try {
        cred = await signInWithEmailAndPassword(auth, email, pass);
      } catch (e) {
        if (e.code === "auth/user-not-found")
          cred = await createUserWithEmailAndPassword(auth, email, pass);
        else throw e;
      }
      const idToken = await cred.user.getIdToken();
      await exchangeToken(idToken);
      onFinish();
    } catch (e) {
      setErr(e.message);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input
        type="email"
        placeholder="Email"
        className="w-full px-3 py-2 rounded text-black"
        value={email}
        onChange={e => setEmail(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Password"
        className="w-full px-3 py-2 rounded text-black"
        value={pass}
        onChange={e => setPass(e.target.value)}
        required
      />
      {err && <p className="text-red-300 text-sm">{err}</p>}
      <button className="w-full py-2 rounded bg-emerald-500 hover:bg-emerald-600">
        Continue
      </button>
    </form>
  );
}

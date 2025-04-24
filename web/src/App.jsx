import { useState } from "react";
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut } from "firebase/auth";
import { FIREBASE_CONFIG } from "./config";
import { exchangeToken } from "./utils/auth";
import AuthEmail from "./components/AuthEmail";

initializeApp(FIREBASE_CONFIG);
const auth  = getAuth();
const gp    = new GoogleAuthProvider();

export default function App() {
  const [stage, setStage] = useState(
    localStorage.getItem("aw_session") ? "welcome" : "choose"
  );

  async function google() {
    const { user } = await signInWithPopup(auth, gp);
    await exchangeToken(await user.getIdToken());
    setStage("welcome");
  }

  return (
    <div className="h-screen flex items-center justify-center bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 text-white">
      <div className="w-full max-w-md bg-white/10 p-8 rounded-2xl backdrop-blur-sm">
        <h1 className="text-3xl font-bold text-center mb-6">Welcome to AllyWorld</h1>

        {stage === "choose" && (
          <>
            <button onClick={google}
              className="w-full py-2 mb-4 rounded bg-blue-600 hover:bg-blue-700">
              Sign in with Google
            </button>
            <button
              onClick={() => setStage("email")}
              className="w-full py-2 rounded bg-emerald-500 hover:bg-emerald-600">
              Sign in with Email
            </button>
          </>
        )}

        {stage === "email" && (
          <AuthEmail auth={auth} onFinish={() => setStage("welcome")} />
        )}

        {stage === "welcome" && (
          <>
            <p className="text-center mb-4 text-lg">Welcome to AllyWorld!</p>
            <button
              onClick={() => { signOut(auth); localStorage.clear(); setStage("choose"); }}
              className="w-full py-2 rounded bg-white/20 hover:bg-white/30">
              Log out
            </button>
          </>
        )}
      </div>
    </div>
  );
}

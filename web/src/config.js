export const VERIFY_URL =
  import.meta.env.MODE === "development"
    ? "http://localhost:5001/allyworld-sso/us-central1/api/auth/verify"
    : "/auth/verify"; // Hosting rewrite in prod

export const FIREBASE_CONFIG = {
  apiKey:       import.meta.env.VITE_FB_API_KEY,
  authDomain:   import.meta.env.VITE_FB_AUTH_DOMAIN,
  projectId:    import.meta.env.VITE_FB_PROJECT_ID
};

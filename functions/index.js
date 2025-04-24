// functions/index.js (v1)
const functions = require('firebase-functions');
const express = require('express');
const cors = require('cors');
const admin = require('firebase-admin');
const jwt = require('jsonwebtoken');
const { Pool } = require('pg');

admin.initializeApp();

const cfg = functions.config();
const DATABASE_URL = cfg.sso.database_url;
const JWT_SECRET = cfg.sso.jwt_secret;

const pool = new Pool({ connectionString: DATABASE_URL });
const app = express();

app.use(cors({ origin: ['http://localhost:8080', 'http://127.0.0.1:8080', 'http://localhost:5173'], credentials: true }));
app.use(express.json());


// ---------- /auth/verify ----------
app.post('/auth/verify', async (req, res) => {
    const { idToken } = req.body;
    if (!idToken) return res.status(400).json({ error: 'idToken required' });

    try {
        const decoded = await admin.auth().verifyIdToken(idToken);
        const { uid, email, name, picture } = decoded;

        const client = await pool.connect();
        const upsert = `
      INSERT INTO users (uid,email,name,picture)
      VALUES ($1,$2,$3,$4)
      ON CONFLICT (uid) DO UPDATE
        SET email=EXCLUDED.email,name=EXCLUDED.name,picture=EXCLUDED.picture
      RETURNING id;
    `;
        const { rows } = await client.query(upsert, [uid, email, name || null, picture || null]);
        client.release();

        const sessionToken = jwt.sign(
            { sub: rows[0].id, apps: ['AllyFast', 'AllyScore', 'AllyStation'] },
            JWT_SECRET,
            { expiresIn: '1h' }
        );

        res.json({ sessionToken });
    } catch (err) {
        console.error(err);
        res.status(401).json({ error: 'Invalid token' });
    }
});

// export the HTTPS function (name: api)
exports.api = functions.https.onRequest(
    { region: 'us-central1' },
    app
);
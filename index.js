require('dotenv').config();
const express = require('express');
const admin = require('firebase-admin');
const jwt = require('jsonwebtoken');
const { Pool } = require('pg');

// Initialize Firebase Admin with the service account
admin.initializeApp({
  credential: admin.credential.applicationDefault(),
});

const pool = new Pool({ connectionString: process.env.DATABASE_URL });

const app = express();
app.use(express.json());

// POST /auth/verify
app.post('/auth/verify', async (req, res) => {
  const { idToken } = req.body;
  if (!idToken) return res.status(400).json({ error: 'idToken required' });

  try {
    // 1. Verify Firebase token
    const decoded = await admin.auth().verifyIdToken(idToken);
    // const { uid, email, name, picture } = decoded;

    // // 2. Upsert user in Postgres
    // const client = await pool.connect();
    // const upsert = `
    //   INSERT INTO users (uid, email, name, picture)
    //   VALUES ($1,$2,$3,$4)
    //   ON CONFLICT (uid) DO UPDATE
    //     SET email = EXCLUDED.email,
    //         name  = EXCLUDED.name,
    //         picture = EXCLUDED.picture
    //   RETURNING id;
    // `;
    // const { rows } = await client.query(upsert, [uid, email, name || null, picture || null]);
    // client.release();

    // // 3. Return your own JWT good for 1 hour
    // const sessionToken = jwt.sign(
    //   { sub: rows[0].id, apps: ['AllyFast', 'AllyScore', 'AllyStation'] },
    //   process.env.SESSION_JWT_SECRET,
    //   { expiresIn: '1h' }
    // );

    res.json({ decoded });
  } catch (err) {
    console.error(err);
    res.status(401).json({ error: 'Invalid token' });
  }
});

// Start server
app.listen(process.env.PORT || 4000, () =>
  console.log(`SSO listening on http://localhost:${process.env.PORT || 4000}`)
);

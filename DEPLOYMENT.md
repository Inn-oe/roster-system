# Deployment Guide — Koyeb + Supabase + Vercel
# All free, no credit card, never sleeps

## Stack
| Service | Purpose | Cost |
|---------|---------|------|
| **Koyeb** | Backend hosting (always on) | Free forever |
| **Supabase** | PostgreSQL database (persistent) | Free forever |
| **Vercel** | Frontend hosting | Free forever |

---

## Step 1 — Database: Supabase (Free PostgreSQL)

1. Go to **https://supabase.com** → Sign up with GitHub (no credit card).
2. Click **New Project** → fill in project name: `roster`, choose a password, pick a region.
3. Wait ~2 min for it to provision.
4. Go to **Project Settings → Database → Connection string → URI**.
5. Copy the connection string — it looks like:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxxx.supabase.co:5432/postgres
   ```
   Save this — you'll need it in Step 2.

---

## Step 2 — Backend: Koyeb (Always-On, Free, No Credit Card)

1. Go to **https://www.koyeb.com** → Sign up with GitHub.
2. Click **Create Service** → **GitHub** → select `Inn-oe/roster-system`.
3. Set:
   - **Branch**: `master`
   - **Build type**: `Dockerfile`
   - **Dockerfile location**: `Dockerfile`
4. Under **Environment Variables**, add:
   - `DATABASE_URL` → paste the Supabase connection string from Step 1
5. Under **Regions**, pick **Frankfurt** (closest free region).
6. Click **Deploy**.
7. Once live, copy your Koyeb URL (e.g. `https://roster-system-xxx.koyeb.app`).

---

## Step 3 — Frontend: Vercel

1. Go to **https://vercel.com** → Sign in with GitHub.
2. Click **Add New Project** → Import `Inn-oe/roster-system`.
3. Set **Root Directory** to `frontend`.
4. Add Environment Variable:
   - Key: `VITE_API_URL`
   - Value: your Koyeb URL from Step 2
5. Click **Deploy**.

---

✅ Your full roster system is now live, always active, and completely free!

# Deployment Guide

## Architecture
- **Backend**: Fly.io — always active, free tier, never sleeps
- **Database**: SQLite stored on a persistent Fly.io volume (no external DB needed, no cost)
- **Frontend**: Vercel — free, always active

---

## Step 1 — Install Fly CLI
Download and install from: https://fly.io/docs/hands-on/install-flyctl/

Or run this in PowerShell:
```powershell
iwr https://fly.io/install.ps1 -useb | iex
```

---

## Step 2 — Log in to Fly.io
```powershell
flyctl auth login
```
This opens a browser to sign up / log in (free account, no credit card required).

---

## Step 3 — Deploy the Backend

```powershell
cd c:\Users\Innoe\Desktop\ROSTER
flyctl launch --no-deploy
flyctl volumes create roster_data --size 1
flyctl deploy
```

After deploy, copy your backend URL (e.g., `https://roster-system.fly.dev`).

---

## Step 4 — Deploy the Frontend (Vercel)
1. Go to https://vercel.com and sign in with GitHub.
2. Click **Add New Project** → Import `Inn-oe/roster-system`.
3. Set **Root Directory** to `frontend`.
4. Add Environment Variable:
   - Key: `VITE_API_URL`
   - Value: your Fly.io backend URL (e.g. `https://roster-system.fly.dev`)
5. Click **Deploy**.

---

Your roster system will be live, always on, and completely free!

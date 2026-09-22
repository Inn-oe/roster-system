# Deployment Guide

This guide explains how to deploy your Roster System to free hosting services.

## Prerequisites
1. Create a GitHub account if you don't have one, and push this folder to a new repository.
2. Create an account on [Neon](https://neon.tech/) for the free Serverless Postgres database.
3. Create an account on [Render](https://render.com/) for the free Python backend.
4. Create an account on [Vercel](https://vercel.com/) for the free React frontend.

## 1. Database (Neon)
- Go to Neon console, create a new project.
- Once created, copy the connection string (it looks like `postgresql://user:password@endpoint.neon.tech/dbname?sslmode=require`).

## 2. Backend (Render)
- On Render, go to **Dashboard > Blueprints > New Blueprint Instance**.
- Connect your GitHub repository.
- Render will read the `render.yaml` file in the root directory.
- It will ask for the `DATABASE_URL` environment variable. Paste the connection string from Neon.
- Click **Apply**. Render will automatically build and deploy the FastAPI backend.
- Once deployed, copy the backend URL (e.g., `https://roster-backend-xyz.onrender.com`).

## 3. Frontend (Vercel)
- Go to Vercel and **Add New Project**.
- Connect your GitHub repository.
- Expand **Framework Preset** and select **Vite**.
- Set the **Root Directory** to `frontend`.
- Add an Environment Variable: `VITE_API_URL` and set its value to your Render backend URL.
- Click **Deploy**.

That's it! Your system is fully deployed.

# Deployment Guide
This guide describes how to deploy the **Inventory & Order Management System** online using free-tier services.
---
## 1. Push Code to GitHub
To submit your project, you first need to host it on a public GitHub repository.
1. **Initialize Git locally** in the project root:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Inventory and Order Management System"
   ```
2. **Create a repository on GitHub** (e.g., `inventory-order-management`).
3. **Link and push**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   git push -u origin main
   ```
---
## 2. Option A: Full Multi-Container Cloud Deployment
If the assessment evaluator wants to run your project using your custom Docker Hub images:
### Step 2.1: Build & Push Images to Docker Hub
1. **Login to Docker Hub** (free account):
   ```bash
   docker login
   ```
2. **Build and Tag the Backend**:
   ```bash
   docker build -t YOUR_DOCKER_USERNAME/inventory-backend:latest ./backend
   ```
3. **Build and Tag the Frontend**:
   ```bash
   docker build -t YOUR_DOCKER_USERNAME/inventory-frontend:latest ./frontend
   ```
4. **Push Images**:
   ```bash
   docker push YOUR_DOCKER_USERNAME/inventory-backend:latest
   docker push YOUR_DOCKER_USERNAME/inventory-frontend:latest
   ```
### Step 2.2: Hosting on Render / Railway with Docker Compose
You can host a full Docker Compose stack on paid/free services, or deploy the individual components.
- **Railway**: Simply import your GitHub repository. Railway reads the `docker-compose.yml` automatically, provisions the Postgres DB, builds both Docker images, and deploys them to public URLs. (Highly recommended for speed).
---
## 3. Option B: Separate Free Hosting (Easiest & Free)
This is the standard approach for hosting websites and APIs on individual free-tier cloud platforms.
```mermaid
graph LR
    Vercel[Vercel (Frontend)] -->|Public URL Requests| Render[Render Web Service (FastAPI)]
    Render -->|Internal URL| NeonDB[(Neon.tech Serverless Postgres)]
```
### Step 3.1: Host PostgreSQL Database (Free Tier)
We recommend **Neon.tech** or **Supabase** (both provide free managed serverless PostgreSQL databases).
1. Go to [Neon.tech](https://neon.tech/) and create a free account.
2. Spin up a new PostgreSQL database.
3. Copy the connection string. It will look like:
   `postgresql://alex:password@ep-cool-snowflake-12345.us-east-2.aws.neon.tech/neondb?sslmode=require`
### Step 3.2: Host the Backend API (Render.com)
1. Go to [Render](https://render.com/) and sign up.
2. Click **New** -> **Web Service**.
3. Connect your GitHub repository.
4. Set the following details:
   - **Name**: `inventory-api`
   - **Language**: `Python`
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. In **Environment Variables**, add:
   - `DATABASE_URL`: *(Your Neon PostgreSQL connection string)*
   - `ENVIRONMENT`: `production`
6. Click **Deploy Web Service**. Render will build and deploy your API and provide a public URL (e.g., `https://inventory-api.onrender.com`).
### Step 3.3: Host the Frontend (Vercel)
1. Go to [Vercel](https://vercel.com/) and link your GitHub account.
2. Click **Add New** -> **Project** and select your repository.
3. Configure the Project:
   - **Framework Preset**: `Vite`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
4. Add **Environment Variables**:
   - `VITE_API_URL`: *(Your Render Backend API public URL, e.g., `https://inventory-api.onrender.com`)*
5. Click **Deploy**. Vercel will build and host your app on a public URL (e.g., `https://inventory-order-system.vercel.app`).
---
## 4. Final Submission Checklist
When turning in the project, submit:
1. **GitHub Repository URL**: `https://github.com/YOUR_USERNAME/YOUR_REPOSITORY`
2. **Docker Hub Image Links**:
   - Backend: `YOUR_DOCKER_USERNAME/inventory-backend:latest`
   - Frontend: `YOUR_DOCKER_USERNAME/inventory-frontend:latest`
3. **Live App URLs**:
   - Frontend Hosted Link: `https://YOUR_SUBDOMAIN.vercel.app`
   - Backend API Hosted Link: `https://YOUR_SUBDOMAIN.onrender.com`
   - API Docs URL (interactive testing): `https://YOUR_SUBDOMAIN.onrender.com/docs`

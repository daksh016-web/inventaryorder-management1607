# StockFlow | Inventory & Order Management System
StockFlow is a modern, high-performance **Inventory & Order Management System** designed for retail and catalog operations. It features a Python backend API, a React frontend dashboard, and containerized deployment pipelines.
---
## 🚀 Key Features
*   **Executive Dashboard**: Real-time sales metrics, catalog telemetry, and automated low-stock warnings (Stock &le; 5 units).
*   **Inventory Catalog**: Complete CRUD capabilities for managing products with strict **unique SKU** verification.
*   **Customer Profiles**: Onboard customers, manage billing/contact details, and view individual purchase history logs.
*   **Transactional Checkout**:
    *   Multi-item checkout builder.
    *   **Atomic Stock Operations**: When placing an order, stock levels are updated inside a single database transaction. If any product has insufficient stock, the *entire transaction rolls back* to prevent partial updates.
    *   **Stock Restoration**: Cancelling a previous order automatically restores the items back into inventory.
*   **Responsive UI**: A premium dark-mode interface styled with modern Vanilla CSS, glassmorphism card designs, and micro-animations.
---
## 🛠️ Technology Stack
*   **Backend**: Python FastAPI, SQLAlchemy ORM, Pydantic v2
*   **Frontend**: React (Vite), Lucide Icons, Custom Vanilla CSS
*   **Database**: PostgreSQL (Docker / Cloud) & SQLite (Local plug-and-play fallback)
*   **Containerization**: Docker & Docker Compose
---
## 💻 Local Quickstart (Localhost)
The project includes an automatic **SQLite fallback** for simple local execution without setting up PostgreSQL manually.
### 1. Backend Setup
Navigate to the `backend/` directory:
```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```
*   **API URL**: `http://localhost:8000`
*   **Interactive Docs (Swagger UI)**: `http://localhost:8000/docs`
### 2. Frontend Setup
Navigate to the `frontend/` directory:
```bash
cd frontend
npm install
npm run dev
```
*   **Web App URL**: `http://localhost:5173`
---
## 🐳 Docker Compose Deployment (PostgreSQL)
To launch the full system with a persistent PostgreSQL database:
1.  Clone the directory and run:
    ```bash
    docker compose up --build
    ```
2.  The containers will spin up and orchestrate automatically:
    *   **Frontend**: `http://localhost` (Served via Nginx)
    *   **Backend API**: `http://localhost:8000`
    *   **Postgres DB**: `localhost:5432`

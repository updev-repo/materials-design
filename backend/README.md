# Materials Design API

FastAPI backend with MongoDB for the materials collection.

## Structure

```
backend/
├── src/
│   ├── core/         # Config, database connection
│   ├── models/       # Collection names, constants
│   ├── schemas/      # Pydantic request/response schemas
│   ├── services/     # Business logic, database operations
│   ├── views/        # API routes
│   └── main.py       # Application entry point
├── requirements.txt
└── .env.example
```

## Setup

1. Create virtual environment and install dependencies:

   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and configure:

   ```bash
   cp .env.example .env
   ```

3. Run the server:

   ```bash
   uvicorn src.main:app --reload
   ```

   API docs: http://localhost:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/materials` | List materials (paginated, with filters) |
| GET | `/api/materials/by-id/{id}` | Get material by MongoDB ObjectId |
| GET | `/api/materials/by-material-id/{material_id}` | Get material by material_id (e.g. mp-b) |
| GET | `/health` | Health check |

### Query Parameters for `GET /api/materials`

| Parameter | Type | Description |
|-----------|------|-------------|
| page | int | Page number (default: 1) |
| size | int | Page size (default: 20, max: 100) |
| formula | str | Filter by formula (partial match) |
| elements | str | Comma-separated elements (e.g. `Cs,O`) |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| MONGODB_HOST | localhost | MongoDB host |
| MONGODB_PORT | 27017 | MongoDB port |
| MONGODB_USERNAME | - | MongoDB username (optional) |
| MONGODB_PASSWORD | - | MongoDB password (optional) |
| MONGODB_DB_NAME | materials_design | Database name |

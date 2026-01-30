# Materials Design

Materials Design API backend + frontend using [mp-react-components](https://github.com/materialsproject/mp-react-components) (Materials Project React components).

## Quick start

1. **Backend**: From `backend/`, copy `.env.example` to `.env`, then run `uvicorn src.main:app --reload` (API at http://localhost:8000).
2. **Frontend**: From `frontend/`, copy `.env.example` to `.env.development` (or set `REACT_APP_BASE_URL=http://localhost:8000/api/materials`), then run `npm install` and `npm start` (app at http://localhost:3000).

The frontend uses Materials Explorer (SearchUI) and material detail pages, talking to the backend `/api/materials` endpoints.

## Backend

See `backend/README.md` for API details.

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| MONGODB_HOST | localhost | MongoDB host |
| MONGODB_PORT | 27017 | MongoDB port |
| MONGODB_USERNAME | - | MongoDB username (optional, for auth) |
| MONGODB_PASSWORD | - | MongoDB password (optional, for auth) |
| MONGODB_DB_NAME | materials_design | Database name |

Copy `backend/.env.example` to `backend/.env` and configure.

## Frontend

The frontend uses a standard React structure and **mp-react-components** (Materials Project React components):

```
frontend/
├── public/
│   └── index.html          # Entry HTML
├── src/
│   ├── main.tsx             # Entry point
│   ├── App.tsx              # Router and routes
│   ├── Layout.tsx           # Navbar and main layout
│   ├── styles.less          # Global styles
│   ├── pages/               # App pages + mp-react-components pages
│   │   ├── MaterialDetailPage/
│   │   ├── MaterialsExplorer/
│   │   ├── CrystalStructureAnimationViewer/
│   │   └── ...
│   ├── components/          # mp-react-components
│   └── ...
```

- **Materials Explorer** (SearchUI) at `/` – listing and filtering (calls backend `GET /api/materials/summary`).
- **Material Detail** at `/materials/:materialId` – single material (calls `GET /api/materials/by-material-id/:id`).
- **Crystal Animation** at `/crystal_animation` – mp-react-components demo page.

### Frontend environment

| Variable | Description |
|----------|-------------|
| REACT_APP_BASE_URL | Base URL for materials API (e.g. `http://localhost:8000/api/materials`). Explorer uses `REACT_APP_BASE_URL + '/summary/'`. |
| REACT_APP_AUTOCOMPLETE_URL | (Optional) Formula autocomplete endpoint. |
| REACT_APP_API_KEY | (Optional) API key for requests. |

Copy `frontend/.env.example` to `frontend/.env.development` (or `.env`) and set `REACT_APP_BASE_URL` to your backend URL.
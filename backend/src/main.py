from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.database import close_mongodb_connection, connect_to_mongodb
from src.views.material import router as material_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongodb()
    yield
    await close_mongodb_connection()


app = FastAPI(
    title="Materials Design API",
    description="API for materials database",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(material_router, prefix="/api")


@app.get("/health")
async def health():
    return {"status": "ok"}

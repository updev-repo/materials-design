"""Material API views."""

from fastapi import APIRouter, HTTPException, Query

from src.schemas.material import MaterialListResponse, MaterialResponse
from src.services import material as material_service

router = APIRouter(prefix="/materials", tags=["materials"])


@router.get("", response_model=MaterialListResponse)
async def get_materials(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Page size"),
    formula: str | None = Query(None, description="Filter by formula (partial match)"),
    elements: str | None = Query(None, description="Comma-separated elements to filter"),
):
    """Get materials with pagination and optional filters."""
    elements_list = [e.strip() for e in elements.split(",")] if elements else None
    items, total = await material_service.get_materials(
        page=page,
        size=size,
        formula=formula,
        elements=elements_list,
    )
    return MaterialListResponse(items=items, total=total, page=page, size=size)


@router.get("/by-id/{material_id}", response_model=MaterialResponse)
async def get_material_by_id(material_id: str):
    """Get a material by MongoDB ObjectId."""
    doc = await material_service.get_material_by_id(material_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Material not found")
    return doc


@router.get("/by-material-id/{material_id}", response_model=MaterialResponse)
async def get_material_by_material_id(material_id: str):
    """Get a material by material_id field (e.g. mp-b, mp-1)."""
    doc = await material_service.get_material_by_material_id(material_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Material not found")
    return doc

"""Material API views."""

from fastapi import APIRouter, HTTPException, Query

from src.schemas.material import MaterialListResponse, MaterialResponse
from src.services import material as material_service

router = APIRouter(prefix="/materials", tags=["materials"])


def _to_search_ui_item(item: dict) -> dict:
    """Transform list item to SearchUI-compatible shape (formula_pretty, symmetry, nsites)."""
    return {
        **item,
        "formula_pretty": item.get("formula"),
        "symmetry": {
            "crystal_system": item.get("crystal_system"),
            "symbol": item.get("space_group_symbol"),
            "number": None,
        },
        "nsites": item.get("sites"),
    }


@router.get("/summary")
async def get_materials_summary(
    _limit: int = Query(15, alias="_limit", ge=1, le=100),
    _skip: int = Query(0, alias="_skip", ge=0),
    formula: str | None = Query(None),
    elements: str | None = Query(None, description="Comma-separated elements"),
    material_ids: str | None = Query(None, alias="material_ids"),
):
    """
    List materials in SearchUI-compatible format.
    Returns { data: [...], meta: { total_doc: total } } for mp-react-components SearchUI.
    """
    page = (_skip // _limit) + 1 if _limit else 1
    size = _limit
    elements_list = [e.strip() for e in elements.split(",")] if elements else None
    items, total = await material_service.get_materials(
        page=page,
        size=size,
        formula=formula,
        elements=elements_list,
    )
    data = [_to_search_ui_item(i) for i in items]
    return {"data": data, "meta": {"total_doc": total}}


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
    return MaterialListResponse(data=items, total=total, page=page, size=size)


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

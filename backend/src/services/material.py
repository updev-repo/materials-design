"""Material service for database operations."""

from bson import ObjectId

from src.core.database import get_database
from src.models.material import COLLECTION_NAME


async def _serialize_doc(doc: dict) -> dict:
    """Convert MongoDB document for JSON serialization."""
    if not doc:
        return doc
    result = dict(doc)
    if "_id" in result and isinstance(result["_id"], ObjectId):
        result["_id"] = str(result["_id"])
    return result


def _to_material_list_item(doc: dict) -> dict:
    """Map MongoDB document to material list item with only required fields."""
    symmetry = doc.get("symmetry") or {}
    if not isinstance(symmetry, dict):
        symmetry = {}
    return {
        "material_id": doc.get("material_id"),
        "formula": doc.get("formula_pretty"),
        "crystal_system": symmetry.get("crystal_system"),
        "space_group_symbol": symmetry.get("symbol"),
        "sites": doc.get("nsites"),
        "energy_above_hull": doc.get("energy_above_hull"),
        "band_gap": doc.get("band_gap"),
    }


async def get_materials(
    page: int = 1,
    size: int = 20,
    formula: str | None = None,
    elements: list[str] | None = None,
) -> tuple[list[dict], int]:
    """
    Get materials with optional filters and pagination.
    Returns only: material_id, formula, crystal_system, space_group_symbol,
    sites, energy_above_hull, band_gap.
    """
    db = await get_database()
    collection = db[COLLECTION_NAME]

    filter_query: dict = {}
    if formula:
        filter_query["formula_pretty"] = {"$regex": formula, "$options": "i"}
    if elements:
        filter_query["elements"] = {"$all": elements}

    projection = {
        "_id": 0,
        "material_id": 1,
        "formula_pretty": 1,
        "symmetry.crystal_system": 1,
        "symmetry.symbol": 1,
        "nsites": 1,
        "energy_above_hull": 1,
        "band_gap": 1,
    }

    total = await collection.count_documents(filter_query)
    skip = (page - 1) * size
    cursor = collection.find(filter_query, projection).skip(skip).limit(size)

    items = []
    async for doc in cursor:
        items.append(_to_material_list_item(doc))

    return items, total


async def get_material_by_id(material_id: str) -> dict | None:
    """Get a single material by MongoDB ObjectId."""
    db = await get_database()
    collection = db[COLLECTION_NAME]
    try:
        obj_id = ObjectId(material_id)
    except Exception:
        return None
    doc = await collection.find_one({"_id": obj_id})
    return await _serialize_doc(doc) if doc else None


async def get_material_by_material_id(material_id: str) -> dict | None:
    """Get a single material by material_id field (e.g. mp-b)."""
    db = await get_database()
    collection = db[COLLECTION_NAME]
    doc = await collection.find_one({"material_id": material_id})
    return await _serialize_doc(doc) if doc else None

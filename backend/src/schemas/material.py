"""Pydantic schemas for Material API."""

from typing import Any

from pydantic import BaseModel, Field


class MaterialListItem(BaseModel):
    """Material summary for list response - only key fields."""

    material_id: str | None = None
    formula: str | None = None
    crystal_system: str | None = None
    space_group_symbol: str | None = None
    sites: int | None = None
    energy_above_hull: float | None = None
    band_gap: float | None = None


class MaterialListResponse(BaseModel):
    """Paginated list of materials."""

    data: list[MaterialListItem]
    total: int
    page: int
    size: int


class MaterialResponse(BaseModel):
    """Full material document response schema."""

    id: str = Field(..., alias="_id")
    material_id: str | None = None
    formula_pretty: str | None = None
    elements: list[str] | None = None
    volume: float | None = None
    density: float | None = None
    nsites: int | None = None
    deprecated: bool | None = None
    structure: dict[str, Any] | None = None

    model_config = {"populate_by_name": True, "extra": "allow"}

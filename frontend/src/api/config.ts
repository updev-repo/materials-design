/**
 * Materials Design API – matches backend endpoints from /docs (OpenAPI).
 * Base URL: no trailing slash.
 */
const BASE = (process.env.REACT_APP_BASE_URL || 'http://localhost:8000/api').replace(
  /\/+$/,
  ''
);

export const apiConfig = {
  /** Base URL for materials API (e.g. http://localhost:8000/api) */
  base: BASE,

  /** GET /api/materials – List in SearchUI format (data + meta.total_doc) */
  materialsSummary: `${BASE}/materials`,

  /** GET /api/materials/by-id/{material_id} – Get by MongoDB ObjectId */
  materialById: (id: string) => `${BASE}/by-id/${id}`,

  /** GET /api/materials/by-material-id/{material_id} – Get by material_id (e.g. mp-123) */
  materialByMaterialId: (materialId: string) => `${BASE}/by-material-id/${materialId}`,
};

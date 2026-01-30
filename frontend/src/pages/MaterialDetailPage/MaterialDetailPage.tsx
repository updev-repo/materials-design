/**
 * Material detail page – fetches material by material_id from the backend API.
 * Uses GET /api/materials/by-material-id/{material_id}
 */
import * as React from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';
import { apiConfig } from '../../api/config';

export const MaterialDetailPage: React.FC = () => {
  const { materialId } = useParams<{ materialId: string }>();
  const [material, setMaterial] = React.useState<any>(null);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState<string | null>(null);

  React.useEffect(() => {
    if (!materialId) return;
    setLoading(true);
    setError(null);
    axios
      .get(apiConfig.materialByMaterialId(materialId))
      .then((res) => {
        setMaterial(res.data);
        setLoading(false);
      })
      .catch((err) => {
        setError(
          err.response?.status === 404 ? 'Material not found' : err.message
        );
        setLoading(false);
      });
  }, [materialId]);

  if (loading) {
    return (
      <div className="container">
        <p>Loading...</p>
      </div>
    );
  }
  if (error || !material) {
    return (
      <div className="container">
        <p className="has-text-danger">{error || 'Material not found'}</p>
        <Link to="/">Back to Materials Explorer</Link>
      </div>
    );
  }

  return (
    <div className="container">
      <nav className="breadcrumb" aria-label="breadcrumbs">
        <ul>
          <li>
            <Link to="/">Materials Explorer</Link>
          </li>
          <li className="is-active">
            <a href="#/" aria-current="page">
              {material.material_id || material.formula_pretty || materialId}
            </a>
          </li>
        </ul>
      </nav>
      <h1 className="title is-2">
        {material.formula_pretty || material.material_id || materialId}
      </h1>
      <p className="subtitle">
        {material.material_id && (
          <span className="tag is-medium">ID: {material.material_id}</span>
        )}
      </p>

      <div className="content">
        <h2 className="title is-4">Properties</h2>
        <table className="table is-striped">
          <tbody>
            {material.formula_pretty != null && (
              <tr>
                <th>Formula</th>
                <td>{material.formula_pretty}</td>
              </tr>
            )}
            {material.elements != null && (
              <tr>
                <th>Elements</th>
                <td>{material.elements.join(', ')}</td>
              </tr>
            )}
            {material.volume != null && (
              <tr>
                <th>Volume (Å³)</th>
                <td>{Number(material.volume).toFixed(2)}</td>
              </tr>
            )}
            {material.density != null && (
              <tr>
                <th>Density (g/cm³)</th>
                <td>{Number(material.density).toFixed(2)}</td>
              </tr>
            )}
            {material.nsites != null && (
              <tr>
                <th>Sites</th>
                <td>{material.nsites}</td>
              </tr>
            )}
            {material.deprecated != null && (
              <tr>
                <th>Deprecated</th>
                <td>{material.deprecated ? 'Yes' : 'No'}</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

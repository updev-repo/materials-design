import * as React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Layout } from './Layout';
import { MaterialsExplorer } from './pages/MaterialsExplorer';
import { CrystalStructureAnimationViewer } from './pages/CrystalStructureAnimationViewer';
import { MaterialDetailPage } from './pages/MaterialDetailPage';

export const App: React.FC = () => {
  return (
    <Router>
      <Layout>
        <Switch>
          <Route path="/materials/:materialId">
            <MaterialDetailPage />
          </Route>
          <Route path="/crystal_animation">
            <CrystalStructureAnimationViewer />
          </Route>
          <Route path="/">
            <MaterialsExplorer />
          </Route>
        </Switch>
      </Layout>
    </Router>
  );
};

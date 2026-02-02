import * as React from 'react';
import { Link, useLocation } from 'react-router-dom';

interface LayoutProps {
  children: React.ReactNode;
}

export const Layout: React.FC<LayoutProps> = ({ children }) => {
  const location = useLocation();
  const isExplorer = location.pathname === '/' || location.pathname.startsWith('/materials');

  return (
    <>
      <header className="app-header">
        <div className="app-header-inner">
          <div className="app-header-left">
            <Link to="/" className="app-header-logo">
              <i className="fas fa-search app-header-icon" aria-hidden />
              <span className="app-header-title">Materials Design</span>
            </Link>
          </div>
          <div className="app-header-right">
            <a href="#references" className="app-header-link">References</a>
            <a href="#documentation" className="app-header-link">Documentation</a>
            {!isExplorer && (
              <>
                <Link to="/" className="app-header-link">Materials Explorer</Link>
                <Link to="/crystal_animation" className="app-header-link">Crystal Animation</Link>
              </>
            )}
          </div>
        </div>
      </header>
      <main className="app-main">{children}</main>
    </>
  );
};

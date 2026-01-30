import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { App } from './App';
import '../node_modules/bulma/css/bulma.min.css';
import '../node_modules/bulma-tooltip/dist/css/bulma-tooltip.min.css';
import './styles.less';

const root = document.getElementById('root');
if (root) {
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    root
  );
}

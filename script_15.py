# Create the index.js file
index_js = """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);"""

with open('src/index.js', 'w') as f:
    f.write(index_js)

print("Created src/index.js")
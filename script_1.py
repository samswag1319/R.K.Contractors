# Create the React application structure
import os

# Create directories
os.makedirs('src/components', exist_ok=True)
os.makedirs('src/data', exist_ok=True)
os.makedirs('src/styles', exist_ok=True)
os.makedirs('src/hooks', exist_ok=True)
os.makedirs('public', exist_ok=True)

# Create package.json
package_json = """{
  "name": "rk-contractors-react",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.4",
    "@testing-library/react": "^13.3.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}"""

with open('package.json', 'w') as f:
    f.write(package_json)

print("Created package.json")
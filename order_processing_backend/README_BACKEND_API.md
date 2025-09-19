# Backend API usage and troubleshooting

Base URL:
- Backend (Django): https://vscode-internal-40589-beta.beta01.cloud.kavia.ai:3001
- Health check: GET https://vscode-internal-40589-beta.beta01.cloud.kavia.ai:3001/api/health/
- Orders: GET https://vscode-internal-40589-beta.beta01.cloud.kavia.ai:3001/api/orders/

Frontend configuration:
- Ensure the frontend uses a full API base URL, not a relative path.
- Recommended environment variable in React: REACT_APP_API_BASE_URL=https://vscode-internal-40589-beta.beta01.cloud.kavia.ai:3001
- Example fetch:
  fetch(`${process.env.REACT_APP_API_BASE_URL}/api/orders/`).then(r => r.json())

CORS:
- Development CORS is permissive (CORS_ALLOW_ALL_ORIGINS=True).
- If you lock down CORS for production, set CORS_ALLOWED_ORIGINS to include your frontend origin (e.g., https://vscode-internal-40589-beta.beta01.cloud.kavia.ai:3000) and disable CORS_ALLOW_ALL_ORIGINS.

Common causes of "Error: Failed to fetch":
- Frontend is hitting /api/orders/ relative to port 3000 (frontend) instead of the backend port 3001. Solution: use REACT_APP_API_BASE_URL above.
- Backend not running or migrations not applied. Run:
  python manage.py migrate
  python manage.py insert_portal_sample_order
- Mixed origin without proper CORS. Current settings allow all origins for GETs.

Manual verification steps:
1) Open health endpoint in browser:
   https://vscode-internal-40589-beta.beta01.cloud.kavia.ai:3001/api/health/
   Expected: {"message": "Server is up!"}

2) Open orders endpoint:
   https://vscode-internal-40589-beta.beta01.cloud.kavia.ai:3001/api/orders/
   Expected: JSON array of orders (run insert_portal_sample_order first if empty).

3) API Docs available at:
   https://vscode-internal-40589-beta.beta01.cloud.kavia.ai:3001/docs

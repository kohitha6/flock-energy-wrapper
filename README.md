# Flock Energy - Urja Meter Ops API Wrapper

A robust Python FastAPI service that wraps the legacy Urja Meter Ops portal, transforming server-rendered HTML tables into clean, structured REST JSON endpoints.

## Features
- **Session Management:** Programmatic authentication with persistent cookie handling using `requests.Session`.
- **HTML Parsing:** Clean extraction of meter inventories and operational statuses using `BeautifulSoup4`.
- **OpenAPI Documentation:** Automatically generated Swagger UI at `/docs`.

## Installation & Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
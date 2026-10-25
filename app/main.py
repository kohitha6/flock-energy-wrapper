from fastapi import FastAPI, HTTPException, Query
from app.scraper import UrjaOpsScraper
from app.models import LoginRequest, MetersResponse

app = FastAPI(
    title="Urja Meter Ops API Wrapper",
    version="1.0.0",
    description="Clean REST API wrapper for the legacy Urja Meter Ops utility portal."
)

scraper = UrjaOpsScraper()

@app.post("/api/v1/auth/login")
def login_portal(credentials: LoginRequest):
    success = scraper.login(credentials.username, credentials.password)
    if not success:
        raise HTTPException(status_code=401, detail="Invalid credentials or login failed.")
    return {"status": "success", "message": "Successfully authenticated with Urja Meter Ops."}

@app.get("/api/v1/meters", response_model=MetersResponse)
def get_meters(page: int = Query(1, ge=1, le=21)):
    try:
        data = scraper.get_meters(page=page)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
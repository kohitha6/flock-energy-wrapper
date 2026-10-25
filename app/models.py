from pydantic import BaseModel
from typing import List, Optional

class LoginRequest(BaseModel):
    username: str
    password: str

class MeterItem(BaseModel):
    meter: str
    serial: str
    make: str
    phase: str
    status: str
    dt: str

class MetersResponse(BaseModel):
    page: int
    total_count: int
    meters: List[MeterItem]
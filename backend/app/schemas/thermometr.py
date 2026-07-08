from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal

class STemperatureBase(BaseModel):
    temperature: float = Field(..., ge=-40, le=80)
    humidity: float = Field(..., ge=0, le=100)

class STemperatureIn(STemperatureBase):
    pass

class STemperatureCreate(STemperatureBase):
    timestamp: datetime
    location: Literal["indoor", "outdoor"]
from pydantic import BaseModel, Field, field_validator
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

    model_config = ConfigDict(from_attributes=True)

class STemperatureGet(BaseModel):
    period: datetime
    avg_temperature: float
    avg_humidity: float

    @field_validator("avg_temperature", "avg_humidity")
    @classmethod
    def round_values(cls, value):
        return round(value, 1)
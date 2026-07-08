from fastapi import APIRouter
from ..models.database import SessionDep
from typing import Literal
from schemas.thermometr import STemperatureCreate, STemperatureIn
from models.thermometr import ThermometerModel
from datetime import datetime
from ..models.database import SessionDep

thermometr_router = APIRouter(prefix="/thermometr")

@thermometr_router.post("/{location}")
async def add_temperature(location: Literal["outdoor", "indoor"], session: SessionDep, data: STemperatureIn) -> STemperatureCreate:
    timestamp = datetime.now()

    new_record = ThermometerModel(timestamp=timestamp, temperature=data.temperature, humidity=data.humidity, location=location)
    session.add(new_record)
    await session.commit()

    return {"timestamp": timestamp, "temperature": data.temperature, "humidity": data.humidity, "location": location}


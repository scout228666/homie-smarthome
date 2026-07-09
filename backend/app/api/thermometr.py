from fastapi import APIRouter
from app.database import SessionDep
from typing import Literal
from app.schemas.thermometr import STemperatureCreate, STemperatureIn, STemperatureGet
from app.models.thermometr import ThermometerModel
from datetime import datetime, timedelta
from sqlalchemy import func, select

thermometr_router = APIRouter(prefix="/thermometr")

@thermometr_router.post("/{location}")
async def add_temperature(location: Literal["outdoor", "indoor"], session: SessionDep, data: STemperatureIn) -> STemperatureCreate:
    timestamp = datetime.now()

    new_record = ThermometerModel(timestamp=timestamp, temperature=data.temperature, humidity=data.humidity, location=location)
    session.add(new_record)
    await session.commit()

    return {"timestamp": timestamp, "temperature": data.temperature, "humidity": data.humidity, "location": location}

@thermometr_router.get("/10-day-records")
async def get_last_ten_days(location: Literal["outdoor", "indoor"], session: SessionDep) -> list[STemperatureGet]:
    now_timestamp = datetime.now()
    day = func.date_trunc('day', ThermometerModel.timestamp).label("period")
    query = select(day, func.avg(ThermometerModel.temperature).label("avg_temperature"), func.avg(ThermometerModel.humidity).label("avg_humidity")).where(ThermometerModel.timestamp >= now_timestamp - timedelta(days=10), ThermometerModel.location == location).group_by(day).order_by(day)
    
    result = await session.execute(query)
    return result.mappings().all()
    
@thermometr_router.get("/hourly")
async def get_hourly_temp(location: Literal["outdoor", "indoor"], session: SessionDep) -> list[STemperatureGet]:
    now_timestamp = datetime.now()
    hour = func.date_trunc('hour', ThermometerModel.timestamp).label("period")
    query = select(hour, func.avg(ThermometerModel.temperature).label("avg_temperature"), func.avg(ThermometerModel.humidity).label("avg_humidity")).where(ThermometerModel.timestamp >= now_timestamp - timedelta(hours=24), ThermometerModel.location == location).group_by(hour).order_by(hour)
    
    result = await session.execute(query)
    return result.mappings().all()


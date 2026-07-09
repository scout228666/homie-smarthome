from sqlalchemy.orm import Mapped, mapped_column
from app.database import Model
from datetime import datetime
import enum
from sqlalchemy import Enum

class LocationEnum(str, enum.Enum):
    indoor = "indoor"
    outdoor = "outdoor"

class ThermometerModel(Model):
    __tablename__ = "thermometr_readings"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    timestamp: Mapped[datetime]
    temperature: Mapped[float]
    humidity: Mapped[float]
    location: Mapped[LocationEnum] = mapped_column(Enum(LocationEnum))
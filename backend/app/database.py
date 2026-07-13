from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from datetime import datetime
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.config import settings

DB_URL = f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@localhost:{settings.db_port}/{settings.postgres_db}"
engine = create_async_engine(DB_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)    

class Model(MappedAsDataclass, DeclarativeBase):
    pass

async def get_db():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_db)]

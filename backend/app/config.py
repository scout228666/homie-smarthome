from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_PORT: int
    POSTGRES_DB: str
    DB_HOST: str

    class Config:
        env_file = BASE_DIR / ".env"
        extra = "ignore"

settings = Settings()

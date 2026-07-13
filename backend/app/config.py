from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_PORT: int
    POSTGRES_DB: str

    class Config:
        env_file = ".env"

settings = Settings()
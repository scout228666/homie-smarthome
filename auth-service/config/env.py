from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    debug: bool = False
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str = "5432"
    jwt_secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Roster System API"
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "sqlite:///./roster.db")

    class Config:
        env_file = ".env"

settings = Settings()

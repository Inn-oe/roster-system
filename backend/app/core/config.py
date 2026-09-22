import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Roster System API"
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "postgresql://user:password@localhost:5432/roster")

    class Config:
        env_file = ".env"

settings = Settings()

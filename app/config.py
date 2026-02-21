from pydantic import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/autodevx"
    REDIS_URL: str = "redis://redis:6379"
    PROJECT_ROOT: str = "./workspace"

    class Config:
        env_file = ".env"


settings = Settings()

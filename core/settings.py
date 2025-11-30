from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_provider: Optional[str] = None
    ollama_model: Optional[str] = None
    ollama_url: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
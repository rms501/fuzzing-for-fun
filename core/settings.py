from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_provider: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
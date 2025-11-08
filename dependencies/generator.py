from fastapi import Depends

from core.exceptions import ModelProviderNotFound
from services.generator_service import GeneratorService
from services.llm_clients.base_client import BaseClient
from core.settings import settings
from services.llm_clients.ollama_client import OllamaClient


def get_llm_client() -> BaseClient:
    if settings.model_provider == "ollama":
        return OllamaClient()

    raise ModelProviderNotFound()


def get_generator_service(llm_client: BaseClient = Depends(get_llm_client)) -> GeneratorService:
    return GeneratorService(llm_client)
from core.exceptions import ModelProviderNotFound
from core.settings import settings
from services.llm_clients.base_client import BaseClient
from services.llm_clients.ollama_client import OllamaClient


def get_llm_client() -> BaseClient:
    if settings.model_provider == "ollama":
        return OllamaClient(settings.ollama_model, settings.ollama_url)

    raise ModelProviderNotFound()
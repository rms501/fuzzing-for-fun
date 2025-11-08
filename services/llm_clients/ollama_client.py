from services.llm_clients.base_client import BaseClient


class OllamaClient(BaseClient):

    def generate(self, prompt: str):
        pass
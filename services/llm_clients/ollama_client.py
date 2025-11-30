from core.exceptions import PromptNotFound
from services.llm_clients.base_client import BaseClient

from ollama import Client


class OllamaClient(BaseClient):

    def __init__(self, model: str, url: str):
        self.model = model
        self.client = Client(host=url)

    # TODO: Add type hinting for output.
    def generate(self, system_prompt: str, user_prompt: str):
        if not system_prompt or user_prompt:
            raise PromptNotFound()

        return self.client.generate(self.model, system_prompt + user_prompt)
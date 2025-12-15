from core.exceptions import PromptNotFound
from services.llm_clients.base_client import BaseClient

from ollama import Client


class OllamaClient(BaseClient):

    def __init__(self, model: str, url: str):
        self._model = model
        self._client = Client(host=url)

    # TODO: Add type hinting for output.
    def generate(self, system_prompt: str, user_prompt: str):
        if not system_prompt or not user_prompt:
            raise PromptNotFound()

        output = self._client.generate(self._model, system_prompt + "\n\n" + user_prompt)

        return output
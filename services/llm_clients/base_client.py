from abc import ABC, abstractmethod


class BaseClient(ABC):

    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str):
        pass
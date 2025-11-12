from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseGenerator(ABC):

    @abstractmethod
    def generate(self) -> BaseModel:
        pass

    @abstractmethod
    def generate_llm(self) -> BaseModel:
        pass

    @abstractmethod
    def generate_fallback(self) -> BaseModel:
        pass
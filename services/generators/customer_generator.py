import uuid

from faker import Faker

from models.customer import Customer
from services.generators.base_generator import BaseGenerator
from services.llm_clients.base_client import BaseClient
from services.prompt_provider import PromptProvider


class CustomerGenerator(BaseGenerator):

    def __init__(self, llm_client: BaseClient):
        self._llm_client = llm_client
        self._fake = Faker()

    def generate(self) -> Customer:
        return self.generate_llm()

    def generate_llm(self) -> Customer:
        prompt_provider = PromptProvider()
        self._llm_client.generate(prompt_provider.system_prompts["customer"], prompt_provider.user_prompts["customer"])

    def generate_fallback(self) -> Customer:
        return Customer(
            id=uuid.uuid4(),
            first_name=self._fake.first_name(),
            last_name=self._fake.last_name(),
            email=self._fake.email(),
            phone=self._fake.phone_number(),
            dob=self._fake.date_of_birth(),
            is_active=self._fake.boolean(),
            signup_date=self._fake.date_time()
        )
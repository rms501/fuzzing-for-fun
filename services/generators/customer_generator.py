import uuid

from faker import Faker

from models.customer import Customer, Address
from services.generators.base_generator import BaseGenerator
from services.llm_clients.base_client import BaseClient


class CustomerGenerator(BaseGenerator):

    def __init__(self, llm_client: BaseClient):
        self.fake = Faker()

    def generate(self) -> Customer:
        return self.generate_fallback()

    def generate_llm(self) -> Customer:
        pass

    def generate_fallback(self) -> Customer:
        return Customer(
            id=uuid.uuid4(),
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            email=self.fake.email(),
            phone=self.fake.phone_number(),
            dob=self.fake.date_of_birth(),
            address=Address(
                street=self.fake.street_address(),
                city=self.fake.city(),
                state=self.fake.state(),
                postal_code=self.fake.postalcode()
            ),
            is_active=self.fake.boolean(),
            signup_date=self.fake.date_time()
        )
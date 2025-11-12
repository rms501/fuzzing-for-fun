from fastapi import Depends

from dependencies.clients import get_llm_client
from services.generators.customer_generator import CustomerGenerator
from services.llm_clients.base_client import BaseClient

def get_customer_generator(llm_client: BaseClient = Depends(get_llm_client)) -> CustomerGenerator:
    return CustomerGenerator(llm_client)
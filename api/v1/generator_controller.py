from fastapi import APIRouter, Depends

from dependencies.generators import get_customer_generator
from models.customer import Customer
from services.generators.customer_generator import CustomerGenerator

router = APIRouter(prefix="/generate")

@router.post("/customers", response_model=Customer)
def generate_customers(customer_generator: CustomerGenerator = Depends(get_customer_generator)):
    return customer_generator.generate()
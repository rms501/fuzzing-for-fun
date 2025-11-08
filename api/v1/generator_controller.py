from fastapi import APIRouter, Depends, HTTPException

from core.exceptions import ModelProviderNotFound
from dependencies.generator import get_generator_service
from services.generator_service import GeneratorService


router = APIRouter()

@router.post("/generate")
def generate(generator_service: GeneratorService = Depends(get_generator_service)):
    try:
        pass
    except ModelProviderNotFound:
        raise HTTPException(status_code=500, detail="Invalid model provider configuration.")
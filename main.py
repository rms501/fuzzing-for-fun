import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.v1 import generator_controller
from core.exceptions import ModelProviderNotFound, PromptNotFound

app = FastAPI()
app.include_router(generator_controller.router)

@app.exception_handler(ModelProviderNotFound)
async def model_provider_not_found_exception_handler(request: Request, exception: ModelProviderNotFound):
    return JSONResponse(
        status_code=500,
        content={"message": "Invalid models provider configuration."}
    )

@app.exception_handler(PromptNotFound)
async def prompt_not_found_exception_handler(request: Request, exception: PromptNotFound):
    return JSONResponse(
        status_code=500,
        content={"message": "Invalid prompt configuration."}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
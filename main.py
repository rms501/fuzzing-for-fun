from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.v1 import generator_controller
from core.exceptions import ModelProviderNotFound

app = FastAPI()
app.include_router(generator_controller.router)

@app.exception_handler(ModelProviderNotFound)
async def sql_alchemy_error_exception_handler(request: Request, exception: ModelProviderNotFound):
    return JSONResponse(
        status_code=500,
        content={"message": "Invalid models provider configuration."}
    )
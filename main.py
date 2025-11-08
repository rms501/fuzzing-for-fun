from fastapi import FastAPI

from api.v1 import generator_controller


app = FastAPI()
app.include_router(generator_controller.router)
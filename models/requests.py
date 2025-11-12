from pydantic import BaseModel


class FuzzRequest(BaseModel):

    rules: list[str]
    format: str

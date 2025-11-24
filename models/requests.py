from pydantic import BaseModel


class FuzzRequest(BaseModel):
    rules: list[str]
    output_format: str

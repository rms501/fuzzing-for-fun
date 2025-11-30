from pydantic import BaseModel

from models.enums import OutputFormat


class CustomerRequest(BaseModel):
    output_format: OutputFormat

from datetime import date, datetime
from typing import Optional, Annotated
from uuid import UUID

from pydantic import BaseModel, constr, EmailStr


class Customer(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[Annotated[str, constr(pattern=r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')]]
    dob: Optional[date]
    is_active: bool = True
    signup_date: datetime
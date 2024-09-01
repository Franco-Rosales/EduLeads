from pydantic import BaseModel, Field, validator
from typing import Optional
import re

class PersonBase(BaseModel):
    name: str
    surname: str
    email: str
    address: Optional[str] = None
    phone: Optional[str] = Field(None, regex=r'^\d{10}$')

    @validator('phone')
    def validate_phone(cls, v):
        if v and not re.match(r'^\d{10}$', v):
            raise ValueError('El número de teléfono debe tener exactamente 10 dígitos.')
        return v

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    id: int

    class ConfigDict:
        orm_mode = True


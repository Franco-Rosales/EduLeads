from pydantic import BaseModel, Field
from typing import Optional

class PersonBase(BaseModel):
    name: str
    surname: str
    email: str
    dni: int = Field(..., ge=0, description="Documento Nacional de Identidad numérico")
    address: Optional[str] = None
    phone: Optional[str] = None

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    id: int

    class ConfigDict:
        orm_mode = True


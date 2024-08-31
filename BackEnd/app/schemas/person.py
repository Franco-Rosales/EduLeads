from pydantic import BaseModel
from typing import Optional

class PersonBase(BaseModel):
    name: str
    surname: str
    email: str
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


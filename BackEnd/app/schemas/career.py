from pydantic import BaseModel
from typing import Optional

class CareerBase(BaseModel):
    name: str
    description: Optional[str] = None

class CareerCreate(CareerBase):
    pass

class CareerUpdate(CareerBase):
    pass

class Career(CareerBase):
    id: int

    class Config:
        orm_mode = True



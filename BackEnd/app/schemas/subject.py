from pydantic import BaseModel
from typing import Optional, List

class SubjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    

class SubjectCreate(SubjectBase):
    career_ids: List[int]

class SubjectUpdate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int

    class Config:
        orm_mode = True

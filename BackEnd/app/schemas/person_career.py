from pydantic import BaseModel
from typing import Optional

class PersonCareerCreate(BaseModel):
    person_id: int
    career_id: int
    time_taken: Optional[int] = None

class PersonCareer(BaseModel):
    person_career_id: int 
    person_id: int
    career_id: int
    time_taken: Optional[int] = None

    class Config:
        orm_mode = True

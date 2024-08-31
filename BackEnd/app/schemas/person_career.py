from pydantic import BaseModel
from typing import Optional

class PersonCareerCreate(BaseModel):
    person_id: int
    career_id: int
    time_taken: Optional[int] = None

class PersonCareer(BaseModel):
    person_id: int
    career_id: int
    time_taken: Optional[int] = None

    class ConfigDict:
        orm_mode = True


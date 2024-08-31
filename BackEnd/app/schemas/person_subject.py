from pydantic import BaseModel
from typing import Optional

class PersonSubjectCreate(BaseModel):
    person_id: int
    subject_id: int
    career_id: int
    times_taken: Optional[int] = None
    enrollment_year: Optional[int] = None

class PersonSubject(BaseModel):
    person_id: int
    subject_id: int
    career_id: int
    times_taken: Optional[int] = None
    enrollment_year: Optional[int] = None

    class ConfigDict:
        orm_mode = True


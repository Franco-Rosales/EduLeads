from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.person_career_service import PersonCareerService
from app.schemas.person_career import PersonCareerCreate, PersonCareer
from app.database import get_db
from typing import List

router = APIRouter(prefix="/person-careers", tags=["person-careers"])

@router.post("/", response_model=PersonCareer, status_code=status.HTTP_201_CREATED)
def create_person_career(person_career: PersonCareerCreate, db: Session = Depends(get_db)):
    """Inscribe a una persona en una carrera después de validar los datos."""
    try:
        person_career_service = PersonCareerService(db)
        return person_career_service.create_person_career(person_career)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{person_id}", response_model=List[PersonCareer])
def get_person_careers(person_id: int, db: Session = Depends(get_db)):
    """Obtiene todas las carreras en las que está inscrita una persona."""
    person_career_service = PersonCareerService(db)
    return person_career_service.get_person_careers(person_id)

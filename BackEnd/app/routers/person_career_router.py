from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.services.person_career_service import PersonCareerService
from app.schemas.person_career import PersonCareerCreate, PersonCareer, PersonCareerResponse
from app.database import get_db
from typing import List, Optional

router = APIRouter(prefix="/person-careers", tags=["person-careers"])

@router.post("/", response_model=PersonCareer, status_code=status.HTTP_201_CREATED)
def create_person_career(person_career: PersonCareerCreate, db: Session = Depends(get_db)):
    """Inscribe a una persona en una carrera después de validar los datos."""
    try:
        person_career_service = PersonCareerService(db)
        return person_career_service.create_person_career(person_career)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/", response_model=List[PersonCareer])
def get_person_careers(db: Session = Depends(get_db)):
    """Obtiene todas las inscripciones de personas en carreras."""
    person_career_service = PersonCareerService(db)
    return person_career_service.get_person_careers_all()

@router.get("/{person_id}", response_model=List[PersonCareer])
def get_person_careers(person_id: int, db: Session = Depends(get_db)):
    """Obtiene todas las carreras en las que está inscrita una persona."""
    person_career_service = PersonCareerService(db)
    return person_career_service.get_person_careers(person_id)


@router.get("/paginated/", response_model=List[PersonCareerResponse])
def get_person_careers_paginated(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    person_career_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    """Obtiene inscripciones a carreras con paginación y filtro opcional por ID de inscripción."""
    person_career_service = PersonCareerService(db)
    return person_career_service.get_person_careers_paginated(skip=skip, limit=limit, person_career_id=person_career_id)
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.services.person_subject_service import PersonSubjectService
from app.schemas.person_subject import PersonSubjectCreate, PersonSubject, PersonSubjectResponse
from app.database import get_db
from typing import List, Optional

router = APIRouter(prefix="/person-subjects", tags=["person-subjects"])

@router.post("/", response_model=PersonSubject, status_code=status.HTTP_201_CREATED)
def create_person_subject(person_subject: PersonSubjectCreate, db: Session = Depends(get_db)):
    """Inscribe a una persona en una materia después de validar los datos."""
    try:
        person_subject_service = PersonSubjectService(db)
        return person_subject_service.create_person_subject(person_subject)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/", response_model=List[PersonSubject])
def get_person_subjects(db: Session = Depends(get_db)):
    """Obtiene todas las inscripciones de personas en materias."""
    person_subject_service = PersonSubjectService(db)
    return person_subject_service.get_person_subjects_all()

@router.get("/{person_id}", response_model=List[PersonSubject])
def get_person_subjects(person_id: int, db: Session = Depends(get_db)):
    """Obtiene todas las materias en las que está inscrita una persona."""
    person_subject_service = PersonSubjectService(db)
    return person_subject_service.get_person_subjects(person_id)

@router.get("/paginated/", response_model=List[PersonSubjectResponse])
def get_person_subjects_paginated(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    person_subject_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    """Obtiene inscripciones a materias con paginación y filtro opcional por ID de inscripción."""
    person_subject_service = PersonSubjectService(db)
    return person_subject_service.get_person_subjects_paginated(skip=skip, limit=limit, person_subject_id=person_subject_id)
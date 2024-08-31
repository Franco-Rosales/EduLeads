from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.subject_service import SubjectService
from app.schemas.subject import SubjectCreate, SubjectUpdate, Subject
from app.database import get_db
from typing import List

router = APIRouter(prefix="/subjects", tags=["subjects"])

@router.post("/", response_model=Subject, status_code=status.HTTP_201_CREATED)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    """Crea una nueva materia después de validar los datos."""
    try:
        subject_service = SubjectService(db)
        return subject_service.create_subject(subject)
    except ValueError as e:
        print("me fui por aca")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{subject_id}", response_model=Subject)
def get_subject(subject_id: int, db: Session = Depends(get_db)):
    """Obtiene una materia por su ID."""
    subject_service = SubjectService(db)
    subject = subject_service.get_subject_by_id(subject_id)
    if not subject:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Materia no encontrada")
    return subject

@router.get("/", response_model=List[Subject])
def get_all_subjects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene todas las materias con paginación."""
    subject_service = SubjectService(db)
    return subject_service.get_all_subjects(skip, limit)

@router.get("/subjects_by_career/{career_id}", response_model=List[Subject])
def get_subjects_by_career(career_id: int, db: Session = Depends(get_db)):
    """Obtiene todas las materias que pertenecen a una carrera específica."""
    subject_service = SubjectService(db)
    subjects = subject_service.get_subjects_by_career_id(career_id)
    if not subjects:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron materias para esta carrera")
    return subjects

@router.put("/{subject_id}", response_model=Subject)
def update_subject(subject_id: int, subject_update: SubjectUpdate, db: Session = Depends(get_db)):
    """Actualiza una materia existente después de validar los datos."""
    try:
        subject_service = SubjectService(db)
        return subject_service.update_subject(subject_id, subject_update)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{subject_id}", response_model=bool)
def delete_subject(subject_id: int, db: Session = Depends(get_db)):
    """Elimina una materia por su ID."""
    subject_service = SubjectService(db)
    if not subject_service.get_subject_by_id(subject_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Materia no encontrada")
    return subject_service.delete_subject(subject_id)


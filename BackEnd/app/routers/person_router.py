from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.person_service import PersonService
from app.schemas.person import PersonCreate, PersonUpdate, Person
from app.database import get_db
from typing import List

router = APIRouter(prefix="/persons", tags=["persons"])

@router.post("/", response_model=Person, status_code=status.HTTP_201_CREATED)
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    """Crea una nueva persona después de validar los datos."""
    try:
        person_service = PersonService(db)
        return person_service.create_person(person)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{person_id}", response_model=Person)
def get_person(person_id: int, db: Session = Depends(get_db)):
    """Obtiene una persona por su ID."""
    person_service = PersonService(db)
    person = person_service.get_person_by_id(person_id)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Persona no encontrada")
    return person

@router.get("/", response_model=List[Person])
def get_all_people(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene todas las personas con paginación."""
    person_service = PersonService(db)
    return person_service.get_all_people(skip, limit)

@router.put("/{person_id}", response_model=Person)
def update_person(person_id: int, person_update: PersonUpdate, db: Session = Depends(get_db)):
    """Actualiza una persona existente después de validar los datos."""
    try:
        person_service = PersonService(db)
        return person_service.update_person(person_id, person_update)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{person_id}", response_model=bool)
def delete_person(person_id: int, db: Session = Depends(get_db)):
    """Elimina una persona por su ID."""
    person_service = PersonService(db)
    if not person_service.get_person_by_id(person_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Persona no encontrada")
    return person_service.delete_person(person_id)

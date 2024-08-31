from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.career_service import CareerService
from app.schemas.career import CareerCreate, CareerUpdate, Career
from app.database import get_db
from typing import List

router = APIRouter(prefix="/careers", tags=["careers"])

@router.post("/", response_model=Career, status_code=status.HTTP_201_CREATED)
def create_career(career: CareerCreate, db: Session = Depends(get_db)):
    """Crea una nueva carrera después de validar los datos."""
    try:
        career_service = CareerService(db)
        return career_service.create_career(career)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{career_id}", response_model=Career)
def get_career(career_id: int, db: Session = Depends(get_db)):
    """Obtiene una carrera por su ID."""
    career_service = CareerService(db)
    career = career_service.get_career_by_id(career_id)
    if not career:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrera no encontrada")
    return career

@router.get("/", response_model=List[Career])
def get_all_careers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene todas las carreras con paginación."""
    career_service = CareerService(db)
    return career_service.get_all_careers(skip, limit)

@router.put("/{career_id}", response_model=Career)
def update_career(career_id: int, career_update: CareerUpdate, db: Session = Depends(get_db)):
    """Actualiza una carrera existente después de validar los datos."""
    try:
        career_service = CareerService(db)
        return career_service.update_career(career_id, career_update)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{career_id}", response_model=bool)
def delete_career(career_id: int, db: Session = Depends(get_db)):
    """Elimina una carrera por su ID."""
    career_service = CareerService(db)
    if not career_service.get_career_by_id(career_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrera no encontrada")
    return career_service.delete_career(career_id)


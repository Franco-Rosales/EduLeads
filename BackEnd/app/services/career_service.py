from sqlalchemy.orm import Session
from app.models.career import Career
from app.schemas.career import CareerCreate, CareerUpdate
from app.repositories.career_repository import CareerRepository
from typing import List

class CareerService:
    def __init__(self, db: Session):
        self.db = db
        self.career_repository = CareerRepository(db)

    def create_career(self, career: CareerCreate):
        """Crea una nueva carrera después de validar los datos."""
        # Validaciones
        if not career.name:
            raise ValueError("El nombre de la carrera es obligatorio.")
        
        # Crear carrera
        return self.career_repository.create_career(career)

    def get_career_by_id(self, career_id: int):
        """Obtiene una carrera por su ID."""
        career = self.career_repository.get_career_by_id(career_id)
        if career is None:
            raise ValueError("La carrera no existe.")
        return career

    def get_all_careers(self, skip: int = 0, limit: int = 100) -> List[Career]:
        """Obtiene todas las carreras con paginación."""
        return self.career_repository.get_all_careers(skip, limit)

    def update_career(self, career_id: int, career_update: CareerUpdate):
        """Actualiza una carrera existente después de validar los datos."""
        career = self.get_career_by_id(career_id)
        if career is None:
            raise ValueError("La carrera no existe.")
        
        # Validaciones
        if career_update.name and not career_update.name:
            raise ValueError("El nombre de la carrera no puede ser vacío.")
        
        # Actualizar carrera
        return self.career_repository.update_career(career_id, career_update)

    def delete_career(self, career_id: int) -> bool:
        """Elimina una carrera por su ID."""
        career = self.get_career_by_id(career_id)
        if career is None:
            raise ValueError("La carrera no existe.")
        return self.career_repository.delete_career(career_id)


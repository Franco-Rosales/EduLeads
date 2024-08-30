from sqlalchemy.orm import Session
from app.repositories.person_career_repository import PersonCareerRepository
from app.schemas.person_career import PersonCareerCreate

class PersonCareerService:
    def __init__(self, db: Session):
        self.db = db
        self.person_career_repository = PersonCareerRepository(db)

    def create_person_career(self, person_career: PersonCareerCreate):
        """Crea una nueva relación entre una persona y una carrera después de validar los datos."""
        # Validaciones
        if not person_career.career_id:
            raise ValueError("El ID de la carrera es obligatorio.")
        if not person_career.person_id:
            raise ValueError("El ID de la persona es obligatorio.")
        if person_career.time_taken < 0:
            raise ValueError("El tiempo de cursado no puede ser negativo.")

        # Crear relación
        return self.person_career_repository.create_person_career(person_career)

    def get_person_careers(self, person_id: int):
        """Obtiene todas las carreras en las que está inscrita una persona."""
        return self.person_career_repository.get_person_careers(person_id)

from sqlalchemy.orm import Session
from app.repositories.person_career_repository import PersonCareerRepository
from app.schemas.person_career import PersonCareerCreate, PersonCareerResponse
from typing import List

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
    
    def get_person_careers_all(self):
        """Obtiene todas las inscripciones de personas en carreras."""
        return self.person_career_repository.get_person_careers_all()

    def get_person_careers(self, person_id: int):
        """Obtiene todas las carreras en las que está inscrita una persona."""
        return self.person_career_repository.get_person_careers(person_id)


    def get_person_careers_paginated(self, skip: int = 0, limit: int = 10, person_career_id: int = None) -> List[PersonCareerResponse]:
        """Obtiene inscripciones a carreras con paginación y filtro opcional por ID."""
        person_careers = self.person_career_repository.get_person_careers_paginated(skip, limit, person_career_id)
        return [
            PersonCareerResponse(
                person_career_id=pc.person_career_id,
                person_name=f"{pc.person.name} {pc.person.surname}",
                career_name=pc.career.name
            )
            for pc in person_careers
        ]

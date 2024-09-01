from sqlalchemy.orm import Session
from app.repositories.person_subject_repository import PersonSubjectRepository
from app.schemas.person_subject import PersonSubjectCreate

class PersonSubjectService:
    def __init__(self, db: Session):
        self.db = db
        self.person_subject_repository = PersonSubjectRepository(db)

    def create_person_subject(self, person_subject: PersonSubjectCreate):
        """Crea una nueva relación entre una persona y una materia después de validar los datos."""
        # Validaciones
        if not person_subject.subject_id:
            raise ValueError("El ID de la materia es obligatorio.")
        if not person_subject.person_id:
            raise ValueError("El ID de la persona es obligatorio.")
        if not person_subject.career_id:
            raise ValueError("El ID de la carrera es obligatorio.")
        if person_subject.times_taken < 0:
            raise ValueError("La cantidad de veces cursada no puede ser negativa.")
        if person_subject.enrollment_year < 1900:
            raise ValueError("El año de inscripción es inválido.")

        # Crear relación
        return self.person_subject_repository.create_person_subject(person_subject)
    
    def get_person_subjects_all(self):
        """Obtiene todas las inscripciones de personas en materias."""
        return self.person_subject_repository.get_person_subjects_all()

    def get_person_subjects(self, person_id: int):
        """Obtiene todas las materias en las que está inscrita una persona."""
        return self.person_subject_repository.get_person_subjects(person_id)

    def get_person_subjects_paginated(self, skip: int = 0, limit: int = 10, person_subject_id: int = None):
        """Obtiene inscripciones a materias con paginación y filtro opcional por ID."""
        person_subjects = self.person_subject_repository.get_person_subjects_paginated(skip, limit, person_subject_id)
        return [
            {
                "person_subject_id": ps.person_subject_id,
                "person_name": f"{ps.person.name} {ps.person.surname}",
                "subject_name": ps.subject.name,
                "career_name": ps.career.name
            }
            for ps in person_subjects
        ]
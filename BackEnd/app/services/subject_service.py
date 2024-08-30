from sqlalchemy.orm import Session
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate, SubjectUpdate
from app.repositories.subject_repository import SubjectRepository
from typing import List

class SubjectService:
    def __init__(self, db: Session):
        self.db = db
        self.subject_repository = SubjectRepository(db)

    def create_subject(self, subject: SubjectCreate):
        """Crea una nueva materia después de validar los datos."""
        # Validaciones
        if not subject.name:
            raise ValueError("El nombre de la materia es obligatorio.")
        
        if not subject.career_ids:
            raise ValueError("Debe especificar al menos una carrera.")
        
        # Crear materia
        return self.subject_repository.create_subject(subject)

    def get_subject_by_id(self, subject_id: int):
        """Obtiene una materia por su ID."""
        subject = self.subject_repository.get_subject_by_id(subject_id)
        if subject is None:
            raise ValueError("La materia no existe.")
        return subject

    def get_all_subjects(self, skip: int = 0, limit: int = 100) -> List[Subject]:
        """Obtiene todas las materias con paginación."""
        return self.subject_repository.get_all_subjects(skip, limit)
    
    def get_subjects_by_career_id(self, career_id: int) -> List[Subject]:
        """Obtiene todas las materias que pertenecen a una carrera específica."""
        return self.subject_repository.get_subjects_by_career_id(career_id)

    def update_subject(self, subject_id: int, subject_update: SubjectUpdate):
        """Actualiza una materia existente después de validar los datos."""
        subject = self.get_subject_by_id(subject_id)
        if subject is None:
            raise ValueError("La materia no existe.")
        
        # Validaciones
        if subject_update.name and not subject_update.name:
            raise ValueError("El nombre de la materia no puede ser vacío.")
        
        # Actualizar materia
        return self.subject_repository.update_subject(subject_id, subject_update)

    def delete_subject(self, subject_id: int) -> bool:
        """Elimina una materia por su ID."""
        subject = self.get_subject_by_id(subject_id)
        if subject is None:
            raise ValueError("La materia no existe.")
        return self.subject_repository.delete_subject(subject_id)


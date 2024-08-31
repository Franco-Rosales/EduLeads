from sqlalchemy.orm import Session
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate, SubjectUpdate
from app.models.career import Career
from app.models.subject_career import SubjectCareer


class SubjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_subject_by_id(self, subject_id: int) -> Subject:
        """Obtiene una materia por su ID."""
        return self.db.query(Subject).filter(Subject.id == subject_id).first()

    def get_all_subjects(self, skip: int = 0, limit: int = 100) -> list[Subject]:
        """Obtiene todas las materias con paginación."""
        return self.db.query(Subject).offset(skip).limit(limit).all()
    
    def get_subjects_by_career_id(self, career_id: int) -> list[Subject]:
        """Obtiene todas las materias que pertenecen a una carrera específica."""
        return (
            self.db.query(Subject)
            .join(SubjectCareer)
            .filter(SubjectCareer.career_id == career_id)
            .all()
        )

    def create_subject(self, subject: SubjectCreate) -> Subject:
        """Crea una nueva materia y la asocia con carreras."""
        db_subject = Subject(name=subject.name, description=subject.description)
        self.db.add(db_subject)
        self.db.flush()  # Se hace un flush para obtener el ID de la materia antes de asociarla

        # Asociar las carreras
        for career_id in subject.career_ids:
            db_career = self.db.query(Career).filter(Career.id == career_id).first()
            if db_career:
                subject_career = SubjectCareer(subject_id=db_subject.id, career_id=db_career.id)
                self.db.add(subject_career)
            else:
                raise ValueError(f"La carrera con ID {career_id} no existe.")

        self.db.commit()
        self.db.refresh(db_subject)
        return db_subject

    def update_subject(self, subject_id: int, subject: SubjectUpdate) -> Subject:
        """Actualiza una materia existente."""
        db_subject = self.get_subject_by_id(subject_id)
        if db_subject is None:
            return None
        for key, value in subject.model_dump(exclude_unset=True).items():
            setattr(db_subject, key, value)
        self.db.commit()
        self.db.refresh(db_subject)
        return db_subject

    def delete_subject(self, subject_id: int) -> bool:
        """Elimina una materia por su ID."""
        db_subject = self.get_subject_by_id(subject_id)
        if db_subject is None:
            return False
        self.db.delete(db_subject)
        self.db.commit()
        return True

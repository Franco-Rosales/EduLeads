from sqlalchemy.orm import Session, joinedload
from app.models.person_subject import PersonSubject
from app.schemas.person_subject import PersonSubjectCreate

class PersonSubjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_person_subject(self, person_subject: PersonSubjectCreate) -> PersonSubject:
        """Crea una nueva relación entre una persona y una materia."""
        db_person_subject = PersonSubject(**person_subject.model_dump())
        self.db.add(db_person_subject)
        self.db.commit()
        self.db.refresh(db_person_subject)
        return db_person_subject
    
    def get_person_subjects_all(self) -> list[PersonSubject]:
        """Obtiene todas las inscripciones de personas en materias."""
        return self.db.query(PersonSubject).all()

    def get_person_subjects(self, person_id: int) -> list[PersonSubject]:
        """Obtiene todas las materias en las que está inscrita una persona."""
        return self.db.query(PersonSubject).filter(PersonSubject.person_id == person_id).all()

    def get_person_subjects_paginated(self, skip: int = 0, limit: int = 10, person_subject_id: int = None):
        """Obtiene inscripciones a materias con paginación y filtro opcional por ID."""
        query = self.db.query(PersonSubject).options(
            joinedload(PersonSubject.person), 
            joinedload(PersonSubject.subject),
            joinedload(PersonSubject.career)
        )

        if person_subject_id is not None:
            query = query.filter(PersonSubject.person_subject_id == person_subject_id)

        return query.offset(skip).limit(limit).all()
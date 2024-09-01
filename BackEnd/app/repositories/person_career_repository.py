from sqlalchemy.orm import Session, joinedload
from app.models.person_career import PersonCareer
from app.schemas.person_career import PersonCareerCreate

class PersonCareerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_person_career(self, person_career: PersonCareerCreate) -> PersonCareer:
        """Crea una nueva relación entre una persona y una carrera."""
        db_person_career = PersonCareer(**person_career.model_dump())
        self.db.add(db_person_career)
        self.db.commit()
        self.db.refresh(db_person_career)
        return db_person_career
    
    def get_person_careers_all(self) -> list[PersonCareer]:
        """Obtiene todas las inscripciones de personas en carreras."""
        return self.db.query(PersonCareer).all()

    def get_person_careers(self, person_id: int) -> list[PersonCareer]:
        """Obtiene todas las carreras en las que está inscrita una persona."""
        return self.db.query(PersonCareer).filter(PersonCareer.person_id == person_id).all()


    def get_person_careers_paginated(self, skip: int = 0, limit: int = 10, person_career_id: int = None):
        """Obtiene inscripciones a carreras con paginación y filtro opcional por ID."""
        query = self.db.query(PersonCareer).options(
            joinedload(PersonCareer.person),  
            joinedload(PersonCareer.career) 
        )

        if person_career_id is not None:
            query = query.filter(PersonCareer.person_career_id == person_career_id)

        return query.offset(skip).limit(limit).all()
from sqlalchemy.orm import Session
from app.models.person_career import PersonCareer
from app.schemas.person_career import PersonCareerCreate

class PersonCareerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_person_career(self, person_career: PersonCareerCreate) -> PersonCareer:
        """Crea una nueva relación entre una persona y una carrera."""
        db_person_career = PersonCareer(**person_career.dict())
        self.db.add(db_person_career)
        self.db.commit()
        self.db.refresh(db_person_career)
        return db_person_career

    def get_person_careers(self, person_id: int) -> list[PersonCareer]:
        """Obtiene todas las carreras en las que está inscrita una persona."""
        return self.db.query(PersonCareer).filter(PersonCareer.person_id == person_id).all()

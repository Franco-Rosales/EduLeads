from sqlalchemy.orm import Session
from app.models.career import Career
from app.schemas.career import CareerCreate, CareerUpdate


class CareerRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_career_by_id(self, career_id: int) -> Career:
        """Obtiene una carrera por su ID."""
        return self.db.query(Career).filter(Career.id == career_id).first()

    def get_all_careers(self, skip: int = 0, limit: int = 100) -> list[Career]:
        """Obtiene todas las carreras con paginación."""
        return self.db.query(Career).offset(skip).limit(limit).all()

    def create_career(self, career: CareerCreate) -> Career:
        """Crea una nueva carrera."""
        db_career = Career(**career.dict())
        self.db.add(db_career)
        self.db.commit()
        self.db.refresh(db_career)
        return db_career

    def update_career(self, career_id: int, career: CareerUpdate) -> Career:
        """Actualiza una carrera existente."""
        db_career = self.get_career_by_id(career_id)
        if db_career is None:
            return None
        for key, value in career.dict(exclude_unset=True).items():
            setattr(db_career, key, value)
        self.db.commit()
        self.db.refresh(db_career)
        return db_career

    def delete_career(self, career_id: int) -> bool:
        """Elimina una carrera por su ID."""
        db_career = self.get_career_by_id(career_id)
        if db_career is None:
            return False
        self.db.delete(db_career)
        self.db.commit()
        return True

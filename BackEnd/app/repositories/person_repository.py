from sqlalchemy.orm import Session
from app.models.person import Person
from app.schemas.person import PersonCreate, PersonUpdate

class PersonRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_person_by_id(self, person_id: int) -> Person:
        """Obtiene una persona por su ID."""
        return self.db.query(Person).filter(Person.id == person_id).first()

    def get_all_people(self, skip: int = 0, limit: int = 100) -> list[Person]:
        """Obtiene todas las personas con paginación."""
        return self.db.query(Person).offset(skip).limit(limit).all()
    
    def get_person_by_email(self, email: str) -> Person:
        """Obtiene una persona por su email."""
        return self.db.query(Person).filter(Person.email == email).first()


    def create_person(self, person: PersonCreate) -> Person:
        """Crea una nueva persona."""
        db_person = Person(**person.model_dump())
        self.db.add(db_person)
        self.db.commit()
        self.db.refresh(db_person)
        return db_person

    def update_person(self, person_id: int, person: PersonUpdate) -> Person:
        """Actualiza una persona existente."""
        db_person = self.get_person_by_id(person_id)
        if db_person is None:
            return None
        for key, value in person.model_dump(exclude_unset=True).items():
            setattr(db_person, key, value)
        self.db.commit()
        self.db.refresh(db_person)
        return db_person

    def delete_person(self, person_id: int) -> bool:
        """Elimina una persona por su ID."""
        db_person = self.get_person_by_id(person_id)
        if db_person is None:
            return False
        self.db.delete(db_person)
        self.db.commit()
        return True

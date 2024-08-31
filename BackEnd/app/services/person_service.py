from sqlalchemy.orm import Session
from app.models.person import Person
from app.schemas.person import PersonCreate, PersonUpdate
from app.repositories.person_repository import PersonRepository
from typing import List

class PersonService:
    def __init__(self, db: Session):
        self.db = db
        self.person_repository = PersonRepository(db)

    def create_person(self, person: PersonCreate):
        """Crea una nueva persona después de validar los datos."""
        # Validaciones
        if not person.email:
            raise ValueError("El correo electrónico es obligatorio.")
        if self.email_exists(person.email):
            raise ValueError("El correo electrónico ya está registrado.")
        if len(person.phone) < 7:
            raise ValueError("El número de teléfono debe tener al menos 7 dígitos.")
        
        # Crear persona
        return self.person_repository.create_person(person)

    def get_person_by_id(self, person_id: int):
        """Obtiene una persona por su ID."""
        person = self.person_repository.get_person_by_id(person_id)
        if person is None:
            raise ValueError("La persona no existe.")
        return person

    def get_all_people(self, skip: int = 0, limit: int = 100) -> List[Person]:
        """Obtiene todas las personas con paginación."""
        return self.person_repository.get_all_people(skip, limit)
    
    def email_exists(self, email: str) -> bool:
        """Verifica si el email ya está registrado en la base de datos."""
        return self.person_repository.get_person_by_email(email) is not None


    def update_person(self, person_id: int, person_update: PersonUpdate):
        """Actualiza una persona existente después de validar los datos."""
        person = self.get_person_by_id(person_id)
        if person is None:
            raise ValueError("La persona no existe.")
        
        # Validaciones
        if person_update.email and not person_update.email:
            raise ValueError("El correo electrónico no puede ser vacío.")
        if person_update.phone and len(person_update.phone) < 7:
            raise ValueError("El número de teléfono debe tener al menos 7 dígitos.")
        
        # Actualizar persona
        return self.person_repository.update_person(person_id, person_update)

    def delete_person(self, person_id: int) -> bool:
        """Elimina una persona por su ID."""
        person = self.get_person_by_id(person_id)
        if person is None:
            raise ValueError("La persona no existe.")
        return self.person_repository.delete_person(person_id)


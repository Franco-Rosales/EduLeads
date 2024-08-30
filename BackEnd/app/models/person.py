from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(String)
    phone = Column(String)
    subjects = relationship('PersonSubject', back_populates='person')
    careers = relationship('PersonCareer', back_populates='person')

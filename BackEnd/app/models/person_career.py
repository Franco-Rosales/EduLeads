from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class PersonCareer(Base):
    __tablename__ = 'person_careers'
    person_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    career_id = Column(Integer, ForeignKey('careers.id'), primary_key=True)
    time_taken = Column(Integer)
    person = relationship('Person', back_populates='careers')
    career = relationship('Career', back_populates='people')

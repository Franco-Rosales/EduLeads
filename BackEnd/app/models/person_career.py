from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class PersonCareer(Base):
    __tablename__ = 'person_careers'
    person_career_id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    career_id = Column(Integer, ForeignKey('careers.id'))
    time_taken = Column(Integer)
    person = relationship('Person', back_populates='careers')
    career = relationship('Career', back_populates='people')

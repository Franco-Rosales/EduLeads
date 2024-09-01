from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class PersonSubject(Base):
    __tablename__ = 'person_subjects'
    person_subject_id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    career_id = Column(Integer, ForeignKey('careers.id'))
    times_taken = Column(Integer)
    enrollment_year = Column(Integer)
    person = relationship('Person', back_populates='subjects')
    subject = relationship('Subject', back_populates='people')
    career = relationship('Career')

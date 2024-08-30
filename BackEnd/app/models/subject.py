from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.subject_career import SubjectCareer

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    careers = relationship('SubjectCareer', back_populates='subject')
    people = relationship('PersonSubject', back_populates='subject')



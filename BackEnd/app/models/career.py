from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.subject_career import SubjectCareer

class Career(Base):
    __tablename__ = 'careers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    subjects = relationship('SubjectCareer', back_populates='career')
    people = relationship('PersonCareer', back_populates='career')


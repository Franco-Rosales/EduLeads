from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class SubjectCareer(Base):
    __tablename__ = 'subject_careers'
    subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)
    career_id = Column(Integer, ForeignKey('careers.id'), primary_key=True)
    subject = relationship('Subject', back_populates='careers')
    career = relationship('Career', back_populates='subjects')



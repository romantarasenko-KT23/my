from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    group = Column(String, nullable=False)
    grade = Column(Float, default=0.0)
    email = Column(String, unique=True, nullable=False, index=True)

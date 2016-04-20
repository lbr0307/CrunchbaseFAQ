from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship
from database import Base

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    object_id = Column(String(64), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    birthplace = Column(String(128), nullable=True)
    affiliation_name = Column(String(128), nullable=True)

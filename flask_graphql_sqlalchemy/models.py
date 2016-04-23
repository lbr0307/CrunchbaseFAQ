from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Date
from sqlalchemy.orm import backref, relationship
from database import Base

class Degrees(Base):
    __tablename__ = 'degrees'
    id = Column(Integer, primary_key=True)
    object_id = Column(String(64), nullable=False)
    degree_type = Column(String(32), nullable=False)
    subject = Column(String(255), nullable=True)
    institution = Column(String(64), nullable=True)
    # graduated_at = Column(Date, nullable=True)
    # created_at = Column(DateTime, nullable=True)
    # updated_at = Column(DateTime, nullable=True)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    object_id = Column(String(64), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    birthplace = Column(String(128), nullable=True)
    affiliation_name = Column(String(128), nullable=True)

class Investor(Base):
    __tablename__ = 'investor'
    id = Column(Integer, primary_key=True)
    object_id = Column(String(64), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    birthplace = Column(String(128), nullable=True)
    affiliation_name = Column(String(128), nullable=True)
    degree_type = Column(String(32), nullable=False)
    subject = Column(String(255), nullable=True)
    institution = Column(String(64), nullable=True)

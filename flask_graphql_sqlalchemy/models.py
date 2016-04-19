from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship
from database import Base


# class Degree(Base):
#     __tablename__ = 'degree'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)


# class Fund(Base):
#     __tablename__ = 'fund'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)


# class People(Base):
#     __tablename__ = 'people'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     # Use default=func.now() to set the default hiring time
#     # of an Employee to be the current time when an
#     # Employee record was created
#     hired_on = Column(DateTime, default=func.now())
#     degree_id = Column(Integer, ForeignKey('degree.id'))
#     fund_id = Column(Integer, ForeignKey('fund.id'))
#     # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
#     degree = relationship(Degree, backref=backref('degree', uselist=True, cascade='delete,all'))
#     fund = relationship(Fund, backref=backref('fund', uselist=True, cascade='delete,all'))


# class Degree(Base):
#     __tablename__ = 'degree'


# class Fund(Base):
#     __tablename__ = 'fund'


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    object_id = Column(String(64), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    birthplace = Column(String(128), nullable=True)
    affiliation_name = Column(String(128), nullable=True)

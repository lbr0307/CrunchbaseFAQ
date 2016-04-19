from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect, create_engine, MetaData, Table, select, Column, String, Integer, ForeignKey
from sqlalchemy.engine import reflection
from sqlalchemy.orm import scoped_session, sessionmaker, mapper, relationship, backref
from sqlalchemy.ext.automap import automap_base

# SCHEMA_NAME = '2013snapshot'
# engine = create_engine('mysql+mysqldb://root:sync@localhost', convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# metadata = MetaData()
# metadata.reflect(bind = engine, schema = SCHEMA_NAME)
# Base = declarative_base()
# Base.query = db_session.query_property()
# # Base = automap_base(metadata = metadata)
# # Base.prepare()

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()



def init_db():
    from models import People
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    peter = People(object_id = '111', first_name = 'John', last_name = 'Peter', birthplace = 'Pittsburgh', affiliation_name = 'CMU')
    db_session.add(peter)
    db_session.commit()
    #People = Base.classes.cb_people
    # it = db_session.query(People).filter(People.first_name == 'Roni')
    # for i, itt in enumerate(it):
    #     print itt.first_name

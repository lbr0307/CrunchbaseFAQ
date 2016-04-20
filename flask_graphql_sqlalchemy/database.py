from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect, create_engine, MetaData, Table, select, Column, String, Integer, ForeignKey
from sqlalchemy.engine import reflection
from sqlalchemy.orm import scoped_session, sessionmaker, mapper, relationship, backref
from sqlalchemy.ext.automap import automap_base

# Preparation for reading
SCHEMA_NAME = '2013snapshot'
engine_read = create_engine('mysql+mysqldb://root:sync@localhost', convert_unicode = True)
db_session_read = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine_read))
metadata = MetaData()
metadata.reflect(bind = engine_read, schema = SCHEMA_NAME)
Base_Automap = automap_base(metadata = metadata)
Base_Automap.prepare()

# Writing, since we need export engine_write and Base to other files, we make it global
engine_write = create_engine('sqlite:///database.sqlite3', convert_unicode = True)
db_session_write = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine_write))
Base = declarative_base()
Base.query = db_session_write.query_property()

def read_bd():
    CB_PEOPLE = Base_Automap.classes.cb_people
    #data = db_session_read.query(CB_PEOPLE).filter(CB_PEOPLE.object_id == 'Roni')

    # Fetch all the data from table cb_people
    find = select(['*']).select_from(CB_PEOPLE)
    rs = db_session_read.execute(find)
    return rs.fetchall()

def write_db(data):
    from models import People
    db_session_write.query(People).delete()
    for i, item in enumerate(data):
        # Convert the bitstring to unicode
        Id = unicode(str(item[0]), errors='replace')
        objectId = unicode(str(item[1]), errors='replace')
        firstName = unicode(str(item[2]), errors='replace')
        lastName = unicode(str(item[3]), errors='replace')
        birthPlace = unicode(str(item[4]), errors='replace')
        affiliationName = unicode(str(item[5]), errors='replace')
        #row = People(object_id = item.object_id, first_name = item.first_name, last_name = item.last_name, birthplace = item.birthplace, affiliation_name = item.affiliation_name)
        #row = People(object_id = item.object_id, first_name = item.first_name, last_name = item.last_name, birthplace = item.birthplace, affiliation_name = item.affiliation_name)
        row = People(id = Id, object_id = objectId, first_name = firstName, last_name = lastName, birthplace = birthPlace, affiliation_name = affiliationName)
        db_session_write.add(row)

    db_session_write.commit()   

def init_db():
    write_db(read_bd())

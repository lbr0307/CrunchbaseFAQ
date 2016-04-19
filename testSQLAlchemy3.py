from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect, create_engine, MetaData, Table, select, Column, String, Integer, ForeignKey
from sqlalchemy.engine import reflection
from sqlalchemy.orm import sessionmaker, mapper, relationship, backref
from sqlalchemy.ext.automap import automap_base

# Global vars
SCHEMA_NAME = '2013snapshot'
Base = declarative_base()
engine = create_engine('mysql+mysqldb://root:sync@localhost')

if __name__ == "__main__":
	metadata = MetaData()
	metadata.reflect(bind = engine, schema = SCHEMA_NAME)

	# we can then produce a set of mappings from this MetaData.
	Base = automap_base(metadata = metadata)
	# calling prepare() just sets up mapped classes and relationships.
	Base.prepare()

	session = sessionmaker()
	session.configure(bind = engine)
	s = session()

	People = Base.classes.cb_people
	# find = select('*').select_from(People)
	# rs = s.execute(find)
	# allData = rs.fetchall() 
	#print allData
	
	# Find the people with first name 'Roni' in cb_peoples table
	it = s.query(People).filter(People.first_name == 'Roni')
	for i, itt in enumerate(it):
		print itt.last_name


	Relationships = Base.classes.cb_relationships
	# Find the people with tile 'VP, GM & Editor In Chief - Clinical Decison Support (UpToDate)' in cb_relationships table
	it = s.query(Relationships).filter(Relationships.title == 'VP, GM & Editor In Chief - Clinical Decison Support (UpToDate)')
	for i, itt in enumerate(it):
		print itt.person_object_id 

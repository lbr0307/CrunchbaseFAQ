from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect, create_engine, MetaData, Table, select, Column, String, Integer, ForeignKey
from sqlalchemy.engine import reflection
from sqlalchemy.orm import sessionmaker, mapper, relationship, backref
from sqlalchemy.ext.automap import automap_base

# Global vars
SCHEMA_NAME = '2013snapshot'
Base = declarative_base()
engine = create_engine('mysql+mysqldb://root:sync@localhost')

class People(Base):
	__tablename__ = 'cb_people'
	id = Column(Integer, primary_key=True)
	object_id = Column(String(64), nullable=False)
	first_name = Column(String(128), nullable=False)
	last_name = Column(String(128), nullable=False)
	birthplace = Column(String(128), nullable=True)
	affiliation_name = Column(String(128), nullable=True)
	# def __repr__(self):
	# 	return "<People(first_name='%s', last_name='%s', birthplace='%s')>" % (self.first_name, self.last_name, self.birthplace)

# cb_people_table = Table('cb_people', metadata,
#             Column('id', Integer, primary_key=True),
#             Column('object_id', String(64), nullable=False),
#             Column('first_name', String(128), nullable=False),
#             Column('last_name', String(128), nullable=False),
#             Column('birthplace', String(128), nullable=True),
#             Column('affiliation_name', String(128), nullable=True),           
#         )


if __name__ == "__main__":
	""" Using inspector to get the 11 table names from schema '2013snapshot'
	It is working, but is there a way to get the real data in each table 
	just using inspector?
	"""
	inspector = inspect(engine)
	table_name_list = []
	
	[table_name_list.append(SCHEMA_NAME + '.' + table_name) for table_name in inspector.get_table_names(SCHEMA_NAME)]
	#print table_name_list


	metadata = MetaData()
	metadata.reflect(bind = engine, schema = SCHEMA_NAME)
	cb_people_table = metadata.tables['2013snapshot.cb_people']

	mapper(People, cb_people_table, non_primary=True)

	session = sessionmaker()
	session.configure(bind = engine)
	s = session()
	# find = select('*').select_from(People)
	# rs = s.execute(find)
	# allData = rs.fetchall() 
	# print allData

	# Select the information on the people whose object_id equals 223303 in table cb_people
	selecting = select([cb_people_table]).where(cb_people_table.c.object_id == 'p:223303')
	# print select
	rs = s.execute(selecting)
	allData = rs.fetchall() 
	print allData

	# Select the information on the people who graduate from CMU in table cb_degrees_table
	cb_degrees_table = metadata.tables['2013snapshot.cb_degrees']
	selecting = select([cb_degrees_table]).where(cb_degrees_table.c.institution == 'Carnegie Mellon University')
	rs = s.execute(selecting)
	allData = rs.fetchall() 
	print allData

	# Get one row from table cb_funds
	cb_funds_table = metadata.tables['2013snapshot.cb_funds']
	selecting = select([cb_funds_table])
	rs = s.execute(selecting)
	allData = rs.fetchone() 
	print allData
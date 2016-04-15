from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect, create_engine, MetaData, Table
from sqlalchemy import select
from sqlalchemy.engine import reflection

""" Using inspector to get the 11 table names from schema '2013snapshot'
	It is working, but is there a way to get the real data in each table 
	just using inspector?
"""
Base = declarative_base()
engine = create_engine('mysql+mysqldb://root:sync@localhost')
inspector = inspect(engine)

for table_name in inspector.get_table_names('2013snapshot'):
	print table_name
	for column in inspector.get_columns(table_name, '2013snapshot'):
		print column

""" I think if I want to get the data out of the tables, I need to use
	metadata and to reflect it using the line 38.
	However, the error message is like this:

		File "build/bdist.macosx-10.11-x86_64/egg/sqlalchemy/sql/schema.py", line 3620, in reflect
  		File "build/bdist.macosx-10.11-x86_64/egg/sqlalchemy/engine/base.py", line 2055, in table_names
  		File "<string>", line 2, in get_table_names
  		File "build/bdist.macosx-10.11-x86_64/egg/sqlalchemy/engine/reflection.py", line 42, in cache
  		File "build/bdist.macosx-10.11-x86_64/egg/sqlalchemy/dialects/mysql/base.py", line 2663, in get_table_names
  		File "build/bdist.macosx-10.11-x86_64/egg/sqlalchemy/sql/compiler.py", line 2677, in quote_identifier
  		File "build/bdist.macosx-10.11-x86_64/egg/sqlalchemy/dialects/mysql/mysqldb.py", line 73, in _escape_identifier
		AttributeError: 'NoneType' object has no attribute 'replace'

	Is there a way to solve this?
"""
meta = MetaData()
meta.reflect(bind = engine)



# class People(Base):
# 	__tablename__ = 'cb_people'

# 	id = Column(Integer, primary_key=True)
# 	object_id = Column(String(64), nullable=False)
# 	first_name = Column(String(128), nullable=False)
# 	last_name = Column(String(128), nullable=False)
# 	birthplace = Column(String(128), nullable=True)
# 	affiliation_name = Column(String(128), nullable=True)
# 	def __repr__(self):
# 		return "<People(first_name='%s', last_name='%s', birthplace='%s')>" % (self.first_name, self.last_name, self.birthplace)

# print People.__table__
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# Session.configure(bind=engine)
# session = Session()
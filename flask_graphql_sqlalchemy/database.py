from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect, create_engine, MetaData, Table, select, Column, String, Integer, ForeignKey
from sqlalchemy.engine import reflection
from sqlalchemy.orm import scoped_session, sessionmaker, mapper, relationship, backref
from sqlalchemy.ext.automap import automap_base
import sys
import csv

# Preparation for reading
SCHEMA_NAME = '2013snapshot'
engine_read = create_engine('mysql+mysqldb://root:sync@localhost', convert_unicode = True)
db_session_read = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine_read))
metadata = MetaData()
metadata.reflect(bind = engine_read, schema = SCHEMA_NAME)
Base_Automap = automap_base(metadata = metadata)
Base_Automap.prepare()

# Writing, since we need export engine_write and Base to other files, we make it global
engine_write = create_engine('sqlite:///database.sqlite3', convert_unicode = False)
db_session_write = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine_write))
Base = declarative_base()
Base.query = db_session_write.query_property()

def read_bd():
    CB_PEOPLE = Base_Automap.classes.cb_people
    CB_DEGREES = Base_Automap.classes.cb_degrees
    CB_INVESTMENTS = Base_Automap.classes.cb_investments
    #data = db_session_read.query(CB_PEOPLE).filter(CB_PEOPLE.object_id == 'Roni')

    # Fetch all the data from table cb_people
    find_PEOPLE= select(['*']).select_from(CB_PEOPLE)
    find_DEGREES= select(['*']).select_from(CB_DEGREES)
    find_INVESTMENTS= select(['*']).select_from(CB_INVESTMENTS)
    rs_PEOPLE = db_session_read.execute(find_PEOPLE)
    rs_DEGREES = db_session_read.execute(find_DEGREES)
    rs_INVESTMENTS = db_session_read.execute(find_INVESTMENTS)
    return (rs_PEOPLE.fetchall(), rs_DEGREES.fetchall(), rs_INVESTMENTS.fetchall())

dict_people_degree = {}
def write_db(data):
    from models import People, Degrees, Investor
    Base.metadata.create_all(engine_write)
    db_session_write.query(People).delete()
    db_session_write.query(Degrees).delete()
    db_session_write.query(Investor).delete()

    for i, item in enumerate(data[0]):
        # Convert the bitstring to unicode
        Id = unicode(str(item[0]), errors='replace')
        objectId = unicode(str(item[1]), errors='replace')
        firstName = unicode(str(item[2]), errors='replace')
        lastName = unicode(str(item[3]), errors='replace')
        birthPlace = unicode(str(item[4]), errors='replace')
        affiliationName = unicode(str(item[5]), errors='replace')
        row = People(id = Id, object_id = objectId, first_name = firstName, last_name = lastName, birthplace = birthPlace, affiliation_name = affiliationName)
        if birthPlace != 'None' and affiliationName != 'None' and affiliationName != 'Unaffiliated':
            if not dict_people_degree.has_key(objectId):
                tempList = []
                tempList.append(firstName)
                tempList.append(lastName)
                tempList.append(birthPlace)
                tempList.append(affiliationName)
                dict_people_degree[objectId] = tempList
        db_session_write.add(row)


    for i, item in enumerate(data[1]):
        # Convert the bitstring to unicode
        Id = unicode(str(item[0]), errors='replace')
        objectId = unicode(str(item[1]), errors='replace')
        degreeType = unicode(str(item[2]), errors='replace')
        Subject = unicode(str(item[3]), errors='replace')
        Institution = unicode(str(item[4]), errors='replace')
        # graduatedAt = unicode(str(item[5]), errors='replace')
        # createdAt = unicode(str(item[6]), errors='replace')
        # updatedAt = unicode(str(item[7]), errors='replace')
        row = Degrees(id = Id, object_id = objectId, degree_type = degreeType, subject = Subject, institution = Institution)
        if dict_people_degree.has_key(objectId):
            if degreeType != 'None' and Subject != 'None' and Institution != 'None':
                tempList = dict_people_degree[objectId]
                tempList.append(degreeType)
                tempList.append(Subject)
                tempList.append(Institution)
                dict_people_degree[objectId] = tempList
            else:
                del dict_people_degree[objectId]
        db_session_write.add(row)

    dict_investors_in_people_degrees = {}
    for i, item in enumerate(data[2]):
        investorObjectId = unicode(str(item[3]), errors='replace')
        if dict_people_degree.has_key(investorObjectId):
            if len(dict_people_degree[investorObjectId]) != 7:
                del dict_people_degree[investorObjectId]
                continue
            dict_investors_in_people_degrees[investorObjectId] = dict_people_degree[investorObjectId]

    for objectId, attrList in dict_investors_in_people_degrees.iteritems():
        firstName = attrList[0]
        lastName = attrList[1]
        birthPlace = attrList[2]
        affiliationName = attrList[3]
        degreeType = attrList[4]
        Subject = attrList[5]
        Institution = attrList[6]
        row = Investor(object_id = objectId, first_name = firstName, last_name = lastName, birthplace = birthPlace, affiliation_name = affiliationName, degree_type = degreeType, subject = Subject, institution = Institution)
        db_session_write.add(row)

    createTrainingFileForANN(dict_people_degree, dict_investors_in_people_degrees)
    db_session_write.commit()

'''
    This function creates a list of labled training instances suitable for ANN training.
    Each instance have 5 effective attributions:
            birthplace
            affiliation_name
            degree_type
            subject
            institution
    and a lable:
            "1": is an investor
            "0": is not an investor
'''

def createTrainingFileForANN(dict_people_degree, dict_investors_in_people_degrees):
    trainingFile = []
    with open('trainingFile.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name', 'birthplace', 'affiliation_name', 'degree_type', 'subject', 'institution', 'lable']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for key, value in dict_people_degree.iteritems():
            if len(value) == 7:
                dictRow = {}
                dictRow['first_name'] = u' '.join(value[0]).encode('utf-8').strip()
                dictRow['last_name'] = u' '.join(value[1]).encode('utf-8').strip()
                dictRow['birthplace'] = u' '.join(value[2]).encode('utf-8').strip()
                dictRow['affiliation_name'] = u' '.join(value[3]).encode('utf-8').strip()
                dictRow['degree_type'] = u' '.join(value[4]).encode('utf-8').strip()
                dictRow['subject'] = u' '.join(value[5]).encode('utf-8').strip()
                dictRow['institution'] = u' '.join(value[6]).encode('utf-8').strip()
                if dict_investors_in_people_degrees.has_key(key):
                    value.append('1')
                    trainingFile.append(value)
                    dictRow['lable'] = '1'
                    writer.writerow(dictRow)
                else:
                    value.append('0')
                    trainingFile.append(value)
                    dictRow['lable'] = '0'
                    writer.writerow(dictRow)



def init_db():
    write_db(read_bd())

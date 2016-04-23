from flask import Flask
from database import db_session_write, init_db
from flask_graphql import GraphQL
from schema import schema

app = Flask(__name__)
app.debug = True

default_query = '''
{
  allPeoples {
    edges {
      node {
        id,
        objectId,
        firstName,
        lastName,
        birthplace,
        affiliationName
      }
    }
  }
}'''.strip()

'''
{
  allDegrees {
    edges {
      node {
        id,
        objectId,
        subject,
        institution
      }
    }
  }
}
'''
'''
{
  allInvestors {
    edges {
      node {
        id,
        objectId,
        firstName,
        lastName,
        birthplace,
        affiliationName,
        degreeType,
        subject,
        institution
      }
    }
  }
}
'''

GraphQL(app, schema = schema, default_query = default_query)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session_write.remove()

if __name__ == '__main__':
    init_db()
    app.run()

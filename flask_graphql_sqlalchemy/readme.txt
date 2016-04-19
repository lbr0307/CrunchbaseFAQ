This is just a toy sample on combining SQLAlchemy with GraphQL and run it with flask framwork. I am still working on mapping the python class in it with MySQL tables. There seems to be some problem on converting class type.

run it with:

  $ python app.py
  
and then query on:
  
  localhost:5000/graphiql

with the query:

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
}

This is a test on table '2013snapshot.cb_people' using flask+graphene+sqlalchemy framework.
First, I fetch all the data from table '2013snapshot.cb_people' and rewrite them into mapped People class that can be queried by GraphQL. Now you can query all the data related to cb_people table using self-defined query as follows.


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

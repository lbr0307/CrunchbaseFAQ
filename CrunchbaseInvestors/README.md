```bash
# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate
```

Now we can install our dependencies:

```bash
pip install -r requirements.txt
```

Now setup our database:

```bash
# Setup the database
./manage.py migrate

```

Now you should be ready to start the server and test on the file "iiiii.json":

```bash
./manage.py testserver iiiii

```

Now head on over to
[http://127.0.0.1:8000/graphiql](http://127.0.0.1:8000/graphiql)
and run some queries like:
```bash

query {
  allInvestors(name_Icontains: "Jay") {
    edges {
      node {
        id,
        name,
        institution
      }
    }
  }
}

```
```bash

query {
  allInvestors(institution_Icontains: "Carnegie") {
    edges {
      node {
        id,
        name,
        institution
      }
    }
  }
}

```

and

```bash

query {
  investor(id: "SW52ZXN0b3JOb2RlOjEyMQ==") {
    name,
    institution
  }
}

```

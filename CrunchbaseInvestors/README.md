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

# query {
#   allInvestors(institution_Icontains: "Carnegie", people_Name_Icontains: "Diane Loviglio") {
#     edges {
#       node {
#         id,
#         name,
#         institution,
# 				people {
#           id,
# 					name,
#           birthPlace,
#           affiliationName
#       	}
#     	}
#   	}
# 	}
# }

```

and

```bash

query {
  allPeoples {
  	edges {
    	node {
				name,
        birthPlace,
        investors {
          edges {
            node {
              name,
              institution
            }
          }
        }
    	}
  	}
	} 
}

```

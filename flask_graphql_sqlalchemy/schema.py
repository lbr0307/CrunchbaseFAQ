import graphene
from graphene import relay
from graphene.contrib.sqlalchemy import (SQLAlchemyConnectionField, SQLAlchemyNode)
from models import People as PeopleModel

schema = graphene.Schema()

@schema.register
class People(SQLAlchemyNode):
    class Meta:
         model = PeopleModel

class Query(graphene.ObjectType):
    node = relay.NodeField(People)
    all_peoples = SQLAlchemyConnectionField(People)

schema.query = Query

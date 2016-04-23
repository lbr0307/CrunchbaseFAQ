import graphene
from graphene import relay
from graphene.contrib.sqlalchemy import (SQLAlchemyConnectionField, SQLAlchemyNode)
from graphene.contrib.sqlalchemy.options import SQLAlchemyOptions
from models import People as PeopleModel
from models import Investor as InvestorModel
from models import Degrees as DegreesModel

schema = graphene.Schema()


@schema.register
class People(SQLAlchemyNode, SQLAlchemyOptions):
    class Meta:
        model = PeopleModel


@schema.register
class Degrees(SQLAlchemyNode):
    class Meta:
        model = DegreesModel


@schema.register
class Investor(SQLAlchemyNode):
    class Meta:
        model = InvestorModel


class Query(graphene.ObjectType):
    node = relay.NodeField(People)
    all_peoples = SQLAlchemyConnectionField(People)
    all_degrees = SQLAlchemyConnectionField(Degrees)
    degrees = relay.NodeField(Degrees)
    all_investors = SQLAlchemyConnectionField(Investor)
    investors = relay.NodeField(Investor)

schema.query = Query

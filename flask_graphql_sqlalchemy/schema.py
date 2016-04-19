import graphene
from graphene import relay
from graphene.contrib.sqlalchemy import (SQLAlchemyConnectionField, SQLAlchemyNode)
from models import People as PeopleModel
# from models import Fund as FundModel
# from models import Degree as DegreeModel

schema = graphene.Schema()


@schema.register
class People(SQLAlchemyNode):
    class Meta:
        model = PeopleModel


# @schema.register
# class Degree(SQLAlchemyNode):

#     class Meta:
#         model = DegreeModel


# @schema.register
# class Fund(SQLAlchemyNode):

#     class Meta:
#         model = FundModel
#         identifier = 'id'


class Query(graphene.ObjectType):
    node = relay.NodeField(People)
    all_peoples = SQLAlchemyConnectionField(People)
    # all_funds = SQLAlchemyConnectionField(Fund)
    # fund = relay.NodeField(Fund)

schema.query = Query

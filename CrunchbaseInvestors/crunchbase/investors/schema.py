from crunchbase.investors.models import People, Investor
from graphene import ObjectType, relay
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode

class PeopleNode(DjangoNode):

    class Meta:
        model = People
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'investors': ['exact', 'icontains', 'istartswith'],
        }
        # filter_fields = ['name', 'investors']
        filter_order_by = ['name']


class InvestorNode(DjangoNode):

    class Meta:
        model = Investor
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'institution': ['exact', 'icontains'],
            'people': ['exact', 'icontains'],
            'people__name': ['exact', 'icontains'],
        }
        filter_order_by = ['name', 'people__name']


class Query(ObjectType):
    people = relay.NodeField(PeopleNode)
    all_peoples = DjangoFilterConnectionField(PeopleNode)

    investor = relay.NodeField(InvestorNode)
    all_investors = DjangoFilterConnectionField(InvestorNode)

    class Meta:
        abstract = True

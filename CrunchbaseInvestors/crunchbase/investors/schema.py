from crunchbase.investors.models import Investor
from graphene import ObjectType, relay
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode


# Graphene will automatically map the User model's fields onto the UserType.
# This is configured in the UserType's Meta class (as you can see below)
# class CategoryNode(DjangoNode):

#     class Meta:
#         model = Category
#         filter_fields = ['name', 'ingredients']
#         filter_order_by = ['name']


class InvestorNode(DjangoNode):

    class Meta:
        model = Investor
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            #'notes': ['exact', 'icontains'],
            #'category': ['exact'],
            #'category__name': ['exact'],
            'institution': ['exact', 'icontains'],
        }
        filter_order_by = ['name']


class Query(ObjectType):
    #category = relay.NodeField(CategoryNode)
    #all_categories = DjangoFilterConnectionField(CategoryNode)

    investor = relay.NodeField(InvestorNode)
    all_investors = DjangoFilterConnectionField(InvestorNode)

    class Meta:
        abstract = True

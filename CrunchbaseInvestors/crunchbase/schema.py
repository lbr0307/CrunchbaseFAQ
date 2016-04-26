import crunchbase.investors.schema
import graphene


class Query(crunchbase.investors.schema.Query):
    pass

schema = graphene.Schema(name = 'Crunchbase Schema')
schema.query = Query

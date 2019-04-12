# Graphene
import graphene
# Schemas
import auth.schema

# Mutations

class Query(auth.schema.Query,
            graphene.ObjectType):
    pass


class Mutations():
    pass


schema = graphene.Schema(query=Query)

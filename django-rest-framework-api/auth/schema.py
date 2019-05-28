# # Django
# from django.contrib.auth.models import User
# # Grphene
# import graphene
# from graphene_django.types import DjangoObjectType

# class CurrentUserNode(DjangoObjectType):

#     class Meta:
#         model = User
#         interfaces = (graphene.relay.Node, )

# class Query(object):
#     current_user = graphene.Field(CurrentUserNode)

#     def resolve_current_user(self, info):
#         if not info.context.user.is_authenticated:
#             return None
#         return info.context.user

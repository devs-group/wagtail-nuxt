import graphene
from graphene_django import DjangoObjectType

from home.models import HomePage


class HomePageNode(DjangoObjectType):
    class Meta:
        model = HomePage


class Query(graphene.ObjectType):
    # home
    home_page = graphene.Field(HomePageNode)

    def resolve_home_page(self, info):
        return HomePage.objects.first()


schema = graphene.Schema(query=Query)

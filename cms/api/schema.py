import graphene
from graphene_django import DjangoObjectType

from home.models import HomePage, InfoCard


class HomePageNode(DjangoObjectType):
    class Meta:
        model = HomePage


class InfoCardNode(DjangoObjectType):
    image = graphene.String(width=graphene.Int())

    def resolve_image(self, info, width=860):
        if not self.image:
            return ""

        return self.image.get_rendition('width-%s' % width).url

    class Meta:
        model = InfoCard


class Query(graphene.ObjectType):
    # HomePage
    home_page = graphene.Field(HomePageNode)

    def resolve_home_page(self, info):
        return HomePage.objects.first()

    # InfoCard
    info_card = graphene.Field(InfoCardNode, id=graphene.Int())
    info_cards = graphene.List(InfoCardNode)

    def resolve_info_card(self, info, id):
        return InfoCard.objects.get(pk=id)

    def resolve_info_cards(self, info):
        return InfoCard.objects.all()


schema = graphene.Schema(query=Query)

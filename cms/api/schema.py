import graphene
from graphene_django import DjangoObjectType

from .models import InfoCard


class InfoCardNode(DjangoObjectType):
    image = graphene.String(width=graphene.Int())

    def resolve_image(self, info, width=860):
        if not self.image:
            return ""

        return self.image.get_rendition('width-%s' % width).url

    class Meta:
        model = InfoCard


class Query(graphene.ObjectType):
    info_card = graphene.Field(InfoCardNode, id=graphene.Int())
    info_cards = graphene.List(InfoCardNode)

    def resolve_info_card(self, info, id):
        return InfoCard.objects.get(pk=id)

    def resolve_info_cards(self, info):
        return InfoCard.objects.all()


schema = graphene.Schema(query=Query)

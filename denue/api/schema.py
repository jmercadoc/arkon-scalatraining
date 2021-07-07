import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoListField
from graphene_gis.converter import gis_converter 

from api.models import ComercialActivity, Stratum, ShopType, Shop


class ComercialActivityNode(DjangoObjectType):
    class Meta:
        model = ComercialActivity
        filter_fields = ['name']
        interfaces = (relay.Node, )


class StratumNode(DjangoObjectType):
    class Meta:
        model = Stratum
        filter_fields = ['name']
        interfaces = (relay.Node, )


class ShopTypeNode(DjangoObjectType):
    class Meta:
        model = ShopType
        filter_fields = ['name']
        interfaces = (relay.Node, )


class ShopNode(DjangoObjectType):
    class Meta:
        model = Shop
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    comercial_activity = relay.Node.Field(ComercialActivityNode)
    all_comercial_activities = DjangoFilterConnectionField(
                                    ComercialActivityNode
                                    )

    stratum = relay.Node.Field(StratumNode)
    all_stratums = DjangoFilterConnectionField(
                                    StratumNode
                                    )

    shop_type = relay.Node.Field(ShopTypeNode)
    all_shop_type = DjangoFilterConnectionField(
                                    ShopTypeNode
                                    )

    shop = relay.Node.Field(ShopNode)
    all_shops = DjangoFilterConnectionField(ShopNode)

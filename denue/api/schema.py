import graphene
import graphql_geojson

from django.contrib.gis.geos import Point
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_geojson.filters import GeometryFilterSet, DistanceFilter
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


class ShopFilter(GeometryFilterSet):
    position__distance_lte = DistanceFilter(
        field_name='position',
        lookup_expr='distance_lte')

    class Meta:
        model = Shop
        fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'position': ['exact']
        }


class ShopNode(DjangoObjectType):
    class Meta:
        model = Shop
        filterset_class = ShopFilter
        interfaces = (relay.Node, )


class NearbyShopsNode(graphql_geojson.GeoJSONType):
    class Meta:
        model = Shop
        interfaces = [relay.Node]
        filterset_class = ShopFilter
        geojson_field = 'position'


class Query(graphene.ObjectType):
    comercial_activity = relay.Node.Field(ComercialActivityNode)
    comercial_activities = DjangoFilterConnectionField(
                                    ComercialActivityNode
                                    )

    stratum = relay.Node.Field(StratumNode)
    stratums = DjangoFilterConnectionField(
                                    StratumNode
                                    )

    shop_type = relay.Node.Field(ShopTypeNode)
    shop_types = DjangoFilterConnectionField(
                                    ShopTypeNode
                                    )

    shop = relay.Node.Field(ShopNode)
    shops = DjangoFilterConnectionField(ShopNode, max_limit=50)
    nearby_shops = DjangoFilterConnectionField(
        NearbyShopsNode,
        max_limit=5
        )


def get_or_create(model, name):
    name = name.lower()
    element = model.objects.filter(name=name)
    if not element:
        element = model.objects.create(name=name)
        return element
    return element[0]


class CreateShop(graphene.relay.ClientIDMutation):
    shop = graphene.Field(ShopNode)

    class Input:
        name = graphene.String(required=True)
        business_name = graphene.String(required=True)
        activity = graphene.String()
        stratum = graphene.String()
        address = graphene.String(required=True)
        phoneNumber = graphene.String()
        email = graphene.String()
        website = graphene.String()
        shopType = graphene.String()
        lat = graphene.Float(required=True)
        long = graphene.Float(required=True)

    def mutate_and_get_payload(root, info, **input):
        name = input.get('name')
        business_name = input.get('business_name')
        activity = input.get('activity')
        stratum = input.get('stratum')
        address = input.get('address')
        phone_number = input.get('phoneNumber')
        email = input.get('email')
        website = input.get('website')
        shop_type = input.get('shopType')
        lat = input.get('lat')
        long = input.get('long')

        ca = get_or_create(ComercialActivity, activity)
        s = get_or_create(Stratum, stratum)
        st = get_or_create(ShopType, shop_type)
        p = Point(long, lat)

        shop = Shop(
            name=name,
            business_name=business_name,
            activity=ca,
            stratum=s,
            address=address,
            phone_number=phone_number,
            email=email,
            website=website,
            shop_type=st,
            position=p
        )
        shop.save()

        return CreateShop(shop=shop)


class Mutation(graphene.AbstractType):
    create_shop = CreateShop.Field()

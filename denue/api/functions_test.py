from django.contrib.gis.geos import Point

from api.models import ComercialActivity, Stratum, ShopType, Shop
from fixtures.utilities import *


def create_comercial_activity(items_len=1):
    for item in range(items_len):
        yield ComercialActivity.objects.create(
            name=generate_string() + str(item)
            )


def create_stratum(items_len=1):
    for item in range(items_len):
        yield Stratum.objects.create(
            name=generate_string() + str(item)
            )


def create_shop_type(items_len=1):
    for item in range(items_len):
        yield ShopType.objects.create(
            name=generate_string() + str(item)
            )


def create_shop(items_len=1):
    for item in range(items_len):
        name = generate_string() + str(item)
        business_name = generate_string()
        address = generate_string(20, 150)
        email = 'user1@test.com'
        website = 'www.test.com'
        position = Point(5, 23)

        activity = next(create_comercial_activity())
        stratum = next(create_stratum())
        shop_type = next(create_shop_type())
        shop = Shop.objects.create(
            name=name,
            business_name=business_name,
            activity=activity,
            stratum=stratum,
            address=address,
            email=email,
            website=website,
            shop_type=shop_type,
            position=position,
            )

        yield shop

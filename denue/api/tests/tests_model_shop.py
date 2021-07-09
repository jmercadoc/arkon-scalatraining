
from django.test import TestCase

from api.models import Shop

from api.tests.functions import create_shop


class ShopTestCase(TestCase):

    def setUp(self):
        self.shop = next(create_shop())

    def test_shop_get_by_name(self):
        shop = Shop.objects.get(name=self.shop.name)
        self.assertEqual(shop.name, self.shop.name)

    def test_shop_get_by_comercial_activity(self):
        shop = Shop.objects.get(activity__name=self.shop.activity.name)
        self.assertEqual(shop.name, self.shop.name)

    def test_shop_get_by_stratum(self):
        shop = Shop.objects.get(stratum__name=self.shop.stratum.name)
        self.assertEqual(shop.name, self.shop.name)

    def test_shop_get_by_shop_type(self):
        shop = Shop.objects.get(shop_type__name=self.shop.shop_type.name)
        self.assertEqual(shop.name, self.shop.name)

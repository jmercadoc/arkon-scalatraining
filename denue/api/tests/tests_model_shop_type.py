from django.test import TestCase

from api.models import ShopType

from api.tests.functions import create_shop_type


class ShopTypeTestCase(TestCase):

    def setUp(self):
        self.shop_type = next(create_shop_type())

    def test_commercial_activity_get_by_name(self):

        shop_type = ShopType.objects.get(name=self.shop_type.name)
        self.assertEqual(shop_type.name, self.shop_type.name)
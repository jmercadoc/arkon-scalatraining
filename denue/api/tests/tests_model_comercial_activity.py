from django.test import TestCase

from api.models import ComercialActivity
from api.tests.functions import create_comercial_activity


class ComercialActivityTestCase(TestCase):

    def setUp(self):
        self.comercial_activity = next(create_comercial_activity())

    def test_commercial_activity_get_by_name(self):
        comercial_activity = ComercialActivity.objects.get(
            name=self.comercial_activity.name
            )
        self.assertEqual(comercial_activity.name, self.comercial_activity.name)


from django.test import TestCase

from api.models import Stratum

from api.tests.functions import create_stratum


class StratumTestCase(TestCase):

    def setUp(self):
        self.stratum = next(create_stratum())

    def test_commercial_activity_get_by_name(self):
        stratum = Stratum.objects.get(name=self.stratum.name)
        self.assertEqual(stratum.name, self.stratum.name)

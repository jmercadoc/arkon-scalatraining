from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase

from denue.schema import schema
from api.tests.functions import *


class ComercialActivityTestCase(GraphQLTestCase):

    def setUp(self):
        self.client = Client(schema)
        self.comercial_activities = list(create_comercial_activity(items_len=3))

    def test_comercial_activity_query(self):
        name = 'allComercialActivities'
        body = """
            edges{
                node{
                    name
                }
            }
        """
        query = build_graphql_query(name, body)

        executed = self.client.execute(query)
        expected = build_response_expected(self.comercial_activities, name)

        self.assertEqual(executed['data'], expected)

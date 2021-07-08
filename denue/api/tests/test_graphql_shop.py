from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase

from denue.schema import schema
from api.tests.functions import *


class ShopTestCase(GraphQLTestCase):

    def setUp(self):
        self.client = Client(schema)
        self.stratums = list(create_shop(items_len=10))

    def test_shop_query(self):
        name = 'shops'
        body = """
            edges{
                node{
                    name
                }
            }
        """
        query = build_graphql_query(name, body)

        executed = self.client.execute(query)
        expected = build_response_expected(self.stratums, name)

        self.assertEqual(executed['data'], expected)

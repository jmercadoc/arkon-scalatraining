from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase

from denue.schema import schema
from api.tests.functions import *


class ShopTypeTestCase(GraphQLTestCase):

    def setUp(self):
        self.client = Client(schema)
        self.shop_types = list(create_shop_type(items_len=3))

    def test_shop_type_query(self):
        name = 'shopTypes'
        body = """
            edges{
                node{
                    name
                }
            }
        """
        query = build_graphql_query(name, body)

        executed = self.client.execute(query)
        expected = build_response_expected(self.shop_types, name)

        self.assertEqual(executed['data'], expected)

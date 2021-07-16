from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase
from graphql_relay import to_global_id


from denue.schema import schema
from api.tests.functions import *
from api.schema import ShopNode


class ShopTestCase(GraphQLTestCase):

    def setUp(self):
        self.client = Client(schema)
        self.shops = list(create_shop(items_len=10))

    def test_shops_query(self):
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
        expected = build_response_expected(self.shops, name)

        self.assertEqual(executed['data'], expected)

    def test_shop_query_get_by_id(self):
        name = 'shop'
        parameters = "$id: ID!"
        variables_str = "id: $id"
        body = "name"
        item = self.shops[0]
        shop_id = to_global_id(ShopNode._meta.name, item.id)

        variables = {
           "id":  shop_id
        }

        query = build_graphql_query_with_parameters(
                name,
                body,
                parameters=parameters,
                variables=variables_str
            )
        executed = self.client.execute(query, variables=variables)
        expected = build_shop_response_expected(item, name)

        self.assertEqual(executed["data"], expected)

    def test_shops_query_get_by_position(self):
        name = 'shops'
        parameters = "$position: Geometry!"
        variables_str = "position: $position"
        body = """
        edges {
            node {
                name
            }
        }
        """
        item = self.shops[0]

        variables = {
            "position": {
                "type": "Point",
                "coordinates": [
                    item.position.x,
                    item.position.y
                ]
            }
        }

        query = build_graphql_query_with_parameters(
                name,
                body,
                parameters=parameters,
                variables=variables_str
            )
        executed = self.client.execute(query, variables=variables)
        expected = build_response_expected([item], name)
        self.assertEqual(executed["data"], expected)

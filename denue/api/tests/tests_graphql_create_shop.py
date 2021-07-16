from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase
from graphql_relay import to_global_id


from denue.schema import schema
from api.tests.functions import *
from api.schema import ShopNode


class CreateShopTestCase(GraphQLTestCase):

    def setUp(self):
        self.client = Client(schema)
        self.shop = {
            "name": generate_string(),
            "business_name": generate_string(),
            "activity": generate_string(),
            "stratum": generate_string(),
            "address": generate_string(),
            "shop_type": generate_string(5, 10),
            "lat": generate_float(-90, 90),
            "long": generate_float(-180, 180)
        }

    def test_create_shop_mutation(self):
        name = 'createShop'
        input = """
        input: {{
            name: "{name}",
            businessName: "{business_name}",
            activity: "{activity}",
            stratum: "{stratum}",
            address: "{address}",
            shopType: "{shop_type}",
            lat: {lat},
            long: {long}
        }}
        """.format(
            name=self.shop["name"],
            business_name=self.shop["business_name"],
            activity=self.shop["activity"],
            stratum=self.shop["stratum"],
            address=self.shop["address"],
            shop_type=self.shop["shop_type"],
            lat=self.shop["lat"],
            long=self.shop["long"]
            )
        body = """
            shop{
                name
                businessName
                activity{
                    name
                }
                stratum{
                    name
                }      
            }
        """
        query = build_graphql_mutation(name, body, input)
        executed = self.client.execute(query)
        executed = dict(executed["data"])
        expected = build_mutation_response_expected(self.shop, name)
        self.assertEqual(executed, expected)

import json
import itertools
from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase


from denue.schema import schema
from api.functions_test import *


def build_graphql_query(query_name, query_select):
    query = """
        query{{
        {query_name}{{
            {query_select}
        }}
    }}
    """.format(query_name=query_name, query_select=query_select)

    return query


def build_comercial_activity_expected(items):

    def activity(ca):
        return {
            'node': {
                    'name': ca.name
            }
        }

    comercial_activity = map(activity, items)
    expected = {
        'allComercialActivities': {
            'edges': list(comercial_activity)
            }
        }

    return expected


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
        expected = build_comercial_activity_expected(self.comercial_activities)

        self.assertEqual(executed['data'], expected)

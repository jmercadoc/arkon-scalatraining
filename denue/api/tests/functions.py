from django.contrib.gis.geos import Point

from api.models import ComercialActivity, Stratum, ShopType, Shop
from fixtures.utilities import *


def create_comercial_activity(items_len=1):
    for item in range(items_len):
        yield ComercialActivity.objects.create(
            name=generate_string() + str(item)
            )


def create_stratum(items_len=1):
    for item in range(items_len):
        yield Stratum.objects.create(
            name=generate_string() + str(item)
            )


def create_shop_type(items_len=1):
    for item in range(items_len):
        yield ShopType.objects.create(
            name=generate_string() + str(item)
            )


def create_shop(items_len=1):
    for item in range(items_len):
        name = generate_string() + str(item)
        business_name = generate_string()
        address = generate_string(20, 150)
        email = 'user1@test.com'
        website = 'www.test.com'
        position = Point(5, 23)

        activity = next(create_comercial_activity())
        stratum = next(create_stratum())
        shop_type = next(create_shop_type())
        shop = Shop.objects.create(
            name=name,
            business_name=business_name,
            activity=activity,
            stratum=stratum,
            address=address,
            email=email,
            website=website,
            shop_type=shop_type,
            position=position,
            )

        yield shop


def build_graphql_query(query_name, query_select):
    query = """
        query{{
        {query_name}{{
            {query_select}
        }}
    }}
    """.format(query_name=query_name, query_select=query_select)

    return query


def build_graphql_query_with_parameters(name, select, parameters, variables):
    query = """
        query {name}({parameters}){{
        {name}({variables}){{
            {select}
        }} 
    }}
    """.format(
        name=name,
        select=select,
        parameters=parameters,
        variables=variables)

    return query


def build_graphql_mutation(name, select, input):
    query = """
        mutation {name} {{
        {name}({input}){{
            {select}
        }} 
    }}
    """.format(
        name=name,
        select=select,
        input=input)

    return query    


def build_response_expected(items, name):

    def activity(ca):
        return {
            'node': {
                    'name': ca.name
            }
        }

    comercial_activity = map(activity, items)
    expected = {
        name: {
            'edges': list(comercial_activity)
            }
        }

    return expected


def build_shop_response_expected(item, name):

    expected = {
        name: {
            'name': item.name            
            }
        }

    return expected


def build_mutation_response_expected(item, name):

    expected = {
        name: {
            'shop': {
                'name': item["name"],
                'businessName': item["business_name"],
                'activity': {'name': item["activity"].lower()},
                'stratum': {'name': item["stratum"].lower()}
            }
        }
    }

    return expected

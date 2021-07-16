import requests

from pymonad.tools import curry
from pymonad.promise import Promise


class Service():

    def get_csrftoken(self, session, url):
        session.get(url)
        if 'csrftoken' in session.cookies:
            csrftoken = session.cookies['csrftoken']
        else:
            csrftoken = session.cookies['csrf']

        return csrftoken

    def get_session(self, url):
        self.session = requests.Session()
        self.session.get(url)

    def execute_query(self, url, json, headers):
        request = self.session.post(
            url,
            json=json,
            headers=headers
            )

        if request.status_code == 200:
            return request.json()
        else:
            print('error: {}'.format(request.status_code))
            return None

    def make_query(self, query, variables, url):
        self.get_session(url)
        csrftoken = self.get_csrftoken(self.session, url)
        headers = {'X-CSRFToken': csrftoken}
        json = {'query': query, 'variables': variables}

        return self.execute_query(url, json, headers)

    def build_graphql_mutation(self, name, select, input):
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

    def build_input(self, shop):
        address = '{calle} {Num_Exterior} {Num_Interior} {Colonia} {CP} {Ubicacion}'
        address = address.format(
            calle=shop['Calle'],
            Num_Exterior=shop['Num_Exterior'],
            Num_Interior=shop['Num_Interior'],
            Colonia=shop['Colonia'],
            CP=shop['CP'],
            Ubicacion=shop['Ubicacion']
        )

        return """
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
            name=shop["Nombre"],
            business_name=shop["Razon_social"],
            activity=shop["Clase_actividad"],
            stratum=shop["Estrato"],
            address=address,
            shop_type=shop["Tipo"],
            lat=shop["Latitud"],
            long=shop["Longitud"]
            )

    @curry(3)
    async def execute_mutation(self, api, shop):
        name = 'createShop'
        select = """
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
        input = self.build_input(shop)
        query = self.build_graphql_mutation(name, select, input)

        return self.make_query(
            query=query,
            variables=None,
            url=api)

    @curry(5)
    async def insert_shops(self, api, success, error, shops):
        execute = self.execute_mutation(api)
        for _, shop in enumerate(shops):

            await Promise.insert(shop).then(execute).then(success).catch(error)

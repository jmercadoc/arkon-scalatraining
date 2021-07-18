import os
import sys
import unittest
import asyncio

from dotenv import dotenv_values

from scrapper import Scrapper
from service import Service

sys.path.append(os.getcwd()[:-8] + '/app/denue/fixtures')
import utilities


class TestScrapper(unittest.TestCase):

    def test_scrapper(self):
        service = 'https://www.inegi.org.mx/app/api/denue/v1/consulta'
        method = 'BuscarEntidad'
        condition = 'todos'
        federal_entity = '01'
        initial_registration = 1
        final_registration = 5

        config = dotenv_values(".env")
        RENUE_API_KEY = config['RENUE_API_KEY']

        scrapper = Scrapper(
            token=RENUE_API_KEY,
            service=service
        )

        data = scrapper.get_data_denue(
                method=method,
                condition=condition,
                federal_entity=federal_entity,
                initial_registration=initial_registration,
                final_registration=final_registration
                )

        self.assertEqual(len(data), final_registration)

    def test_execution_mutaion(self):

        async def async_func(GRAPHQL_API, shop, response):
            response = await service.execute_mutation(GRAPHQL_API, shop)

        name = utilities.generate_string()
        shop = {
                'CLEE': '01001621111005611000000000U0',
                'Id': '9331895',
                'Nombre': name,
                'Razon_social': '(H) CONSULTORIO AGUASCALIENTES, AGS. ',
                'Clase_actividad': 'Consultorios de medicina general del sector privado',
                'Estrato': '0 a 5 personas',
                'Tipo_vialidad': '',
                'Calle': '', 'Num_Exterior': '',
                'Num_Interior': '', 'Colonia': '',
                'CP': '',
                'Ubicacion': 'AGUASCALIENTES, Aguascalientes, AGUASCALIENTES',
                'Telefono': '',
                'Correo_e': '',
                'Sitio_internet': '',
                'Tipo': 'Fijo',
                'Longitud': '-102.27535500',
                'Latitud': '21.87969991',
                'tipo_corredor_industrial': '',
                'nom_corredor_industrial': '',
                'numero_local': ''
                }

        config = dotenv_values(".env")        
        GRAPHQL_API = config['GRAPHQL_API']

        service = Service()

        loop = asyncio.get_event_loop()
        coroutine = async_func(GRAPHQL_API, shop)        
        loop.run_until_complete(coroutine)
        # response = execute_mutation(shop)

        # self.assertEqual(response['data']['createShop']['shop']['name'], name)
        service.session.close()


if __name__ == "__main__":
    unittest.main()

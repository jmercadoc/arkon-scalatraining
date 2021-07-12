import unittest
from dotenv import dotenv_values

from scrapper import Scrapper


class TestScrapper(unittest.TestCase):

    def test_scrapper(self):
        service = 'https://www.inegi.org.mx/app/api/denue/v1/consulta'
        method = 'BuscarEntidad'
        condition = 'todos'
        federal_entity = '01'
        initial_registration = 1
        final_registration = 5

        config = dotenv_values("../../.env")
        RENUE_API_KEY = config['RENUE_API_KEY']

        scrapper = Scrapper(token=RENUE_API_KEY)

        data = scrapper.get_data_denue(
                service=service,
                method=method,
                condition=condition,
                federal_entity=federal_entity,
                initial_registration=initial_registration,
                final_registration=final_registration,
                token=RENUE_API_KEY)

        self.assertEqual(len(data), final_registration)


if __name__ == "__main__":
    unittest.main()

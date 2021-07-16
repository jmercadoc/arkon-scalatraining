import sys
import asyncio

from dotenv import dotenv_values

from scrapper import Scrapper
from service import Service


def success(response):
    print('shop {} inserted'.format(
        response['data']['createShop']['shop']['name']
    ))


def error(err):
    print('Error: ', err)


def main(
        service='https://www.inegi.org.mx/app/api/denue/v1/consulta',
        method='BuscarEntidad',
        condition='todos',
        federal_entity='01',
        initial_registration=1,
        final_registration=10
        ):

    config = dotenv_values(".env")
    RENUE_API_KEY = config['RENUE_API_KEY']
    GRAPHQL_API = config['GRAPHQL_API']
    scrapper = Scrapper(
        token=RENUE_API_KEY,
        service=service
        )

    shops = scrapper.get_data_denue(
            method=method,
            condition=condition,
            federal_entity=federal_entity,
            initial_registration=initial_registration,
            final_registration=final_registration
            )

    service = Service()
    insert = service.insert_shops(GRAPHQL_API, success, error)

    asyncio.run(insert(shops))


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 7:
        service = argv[1]
        method = argv[2]
        condition = argv[3]
        federal_entity = argv[4]
        initial_registration = argv[5]
        final_registration = argv[6]

        main(
            service,
            method,
            condition,
            federal_entity,
            initial_registration,
            final_registration
        )
    else:
        main()

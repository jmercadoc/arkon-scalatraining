import sys
from dotenv import dotenv_values

from scrapper import Scrapper


def main(
        service='https://www.inegi.org.mx/app/api/denue/v1/consulta',
        method='BuscarEntidad',
        condition='todos',
        federal_entity='01',
        initial_registration=1,
        final_registration=100
        ):

    config = dotenv_values(".env")
    RENUE_API_KEY = config['RENUE_API_KEY']

    scrapper = Scrapper(token=RENUE_API_KEY)

    url = scrapper.build_denue_query(
            service=service,
            method=method,
            condition=condition,
            federal_entity=federal_entity,
            initial_registration=initial_registration,
            final_registration=final_registration,
            token=RENUE_API_KEY)

    print(url)

    # TODO Retrieve data from DENUE
    # TODO Retrieve execute create shop


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

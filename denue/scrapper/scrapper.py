import json
import requests


class Scrapper():

    def __init__(self, token):
        self.token = token

    def build_denue_query(
            self,
            service,
            method,
            condition,
            federal_entity,
            initial_registration,
            final_registration,
            token
            ):

        url = f'{service}/{method}/{condition}/{federal_entity}/{initial_registration}/{final_registration}/{token}'

        return url.format(
            service=service,
            method=method,
            condition=condition,
            federal_entity=federal_entity,
            initial_registration=initial_registration,
            final_registration=final_registration,
            token=token)

    def get_data_denue(
        self,
        service,
        method,
        condition,
        federal_entity,
        initial_registration,
        final_registration,
        token
    ):
        url = self.build_denue_query(
            service,
            method,
            condition,
            federal_entity,
            initial_registration,
            final_registration,
            token
            )

        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('error: {}'.format(str(response.status_code)))
            return None

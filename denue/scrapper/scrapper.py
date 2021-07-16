import json
import requests


class Scrapper():

    def __init__(self, token, service):
        self.token = token
        self.service = service

    def build_denue_query(
            self,
            method,
            condition,
            federal_entity,
            initial_registration,
            final_registration
            ):

        return f'{self.service}/{method}/{condition}/{federal_entity}/{initial_registration}/{final_registration}/{self.token}'

    def get_data_denue(
        self,
        method,
        condition,
        federal_entity,
        initial_registration,
        final_registration
    ):
        url = self.build_denue_query(
            method,
            condition,
            federal_entity,
            initial_registration,
            final_registration
            )

        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('error: {}'.format(str(response.status_code)))
            return None

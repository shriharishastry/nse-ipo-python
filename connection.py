import requests
import json


class Connection(object):
    def __init__(self):
        self._session = requests.Session()
        self.base_url = "v1/{end_point}"
        self._session.headers = {
            "Accept": "application/json"
        }

    def get_full_path(self, endpoint):
        return self.base_url.format(**{"end_point": endpoint})

    def make_request(self, endpoint, method, data=None):
        if not data:
            data = dict()
        response = self._session.request(
            method=method, url=self.get_full_path(endpoint), data=json.dumps(data)
        )
        return self.process_response(response)

    @staticmethod
    def process_response(response):
        if response.status_code in [200, 201, 202]:
            result = response.json()
        else:
            raise ValueError("Error while fetching : {}".format(response.text))
        return result

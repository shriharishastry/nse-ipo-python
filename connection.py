import requests
import json

from config import API_ENDPOINT_MAP
from exceptions import ServerException, ClientRequestException, RedirectionException


class Connection(object):
    def __init__(self, env, access_token=None):
        self._session = requests.Session()
        self.env = env
        self.base_url = "{base_url}{version}/{end_point}"
        self._session.headers = {
            "Accept": "application/json",
        }
        if access_token:
            self._session.headers['Authorization'] = "Bearer {}".format(access_token)

    def get_full_path(self, endpoint):
        return self.base_url.format(
            **{"end_point": endpoint, "version": "v1", "base_url": API_ENDPOINT_MAP[self.env]}
        )

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
        elif response.status_code > 500:
            raise ServerException("Internal server error : {}".format(response.reason))
        elif response.status_code > 400:
            raise ClientRequestException("Error : {}".format(response.reason))
        elif response.status_code > 300:
            raise RedirectionException("Error : {}".format(response.reason))
        else:
            raise ValueError("Error while fetching : {}".format(response.text))
        return result

import requests
import logging
import json


class Connection(object):
    def __init__(self):
        self._session = requests.Session()
        self._session.headers = {
            "Accept": "application/json"
        }

    def get_full_path(self, endpoint):
        return endpoint

    def make_request(self, url, method, data=None, stream=False):
        if not data:
            data = dict()
        response = self._session.request(
            method=method, url=self.get_full_path(url), data=json.dumps(data), stream=stream
        )
        return self.process_response(response, stream)

    @staticmethod
    def process_response(response):
       pass

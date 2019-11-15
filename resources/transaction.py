

class Transactions(object):
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        return self.connection.make_request("transactions", "GET", {})

    def add(self, req_body):
        return self.connection.make_request("transactions", "POST", req_body)

    def fetch(self):
        return self.connection.make_request("transactions/fetch", "POST", {})

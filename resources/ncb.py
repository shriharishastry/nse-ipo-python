class Ncb(object):
    def __init__(self, connection):
        self.connection = connection

    def validate(self):
        pass

    def add(self):
        return self.connection.make_request("ncb/add", "POST", {})

    def fetch(self):
        return self.connection.make_request("ncb/fetch", "POST", {})

    def mismatches(self):
        return self.connection.make_request("ncb/mismatches", "POST", {})

    def all(self):
        return self.connection.make_request("ipomaster", "GET", {})

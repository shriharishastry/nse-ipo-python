
class IPOMaster(object):
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        return self.connection.make_request("ipomaster", "GET", {})

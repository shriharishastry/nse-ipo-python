class EForms(object):
    def __init__(self, connection):
        self.connection = connection

    def validate(self):
        pass

    def add(self):
        return self.connection.make_request("eforms/add", "POST", {})

    def query(self):
        return self.connection.make_request("eforms/query", "POST", {})

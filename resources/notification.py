class Notification(object):
    def __init__(self, connection):
        self.connection = connection

    def validate(self):
        pass

    def all(self):
        return self.connection.make_request("notifications", "GET", {})

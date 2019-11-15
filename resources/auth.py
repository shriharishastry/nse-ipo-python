class Auth(object):
    def __init__(self, connection):
        self.connection = connection

    def login(self, member, username, pwd):
        req_body = {
            'member': member,
            'loginId': username,
            'password': pwd
        }
        return self.connection.make_request("login", "POST", req_body)

    def reset_password(self, member, username, pwd, new_pwd):
        req_body = {
            'member': member,
            'loginId': username,
            'password': pwd,
            'newPassword': new_pwd
        }
        return self.connection.make_request("changePassword", "POST", req_body)

    def logout(self):
        return self.connection.make_request("logout", "GET", {})

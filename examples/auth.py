from api import NseIPO

# Login API
api = NseIPO()
login_response = api.Auth.login('1234', 'username', 'pwd')

# Logout API
api.Auth.logout()

# Reset Password
api.Auth.reset_password('1234', 'username', 'pwd')


from api import NseIPO

# Resource api
api = NseIPO()

# Get all the IPO Master from the NSE
login_response = api.IPOMaster.all()

# Get all the EForms
api.EForms.all()


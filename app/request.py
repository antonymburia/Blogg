import urllib.request,json
from .models import Quote

# getting the api endpoint
api_url=None

def configure_request(app):
    global api_url

    api_url = app.config['API_URL']

def get_quotes():
    pass


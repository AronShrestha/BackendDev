from hubspot import HubSpot

import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

api_client_key = os.environ.get('CLIENTID')



def get_token():
    token = HubSpot().auth.oauth.tokens_api.create(
        grant_type =  "refresh_token",
        redirect_uri = os.environ.get('REDIRECT_URI')
        
    )
import jwt

import datetime
import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

secrete = os.environ.get('SECRETE')
# print("our secrete :", secrete, type(secrete))


def encode(**kwargs):
    """
    Utility function that generates the JWT token based on provided arguments
    
    """
    payload = {
        "userID": kwargs['user_id'],
        "username":kwargs['username'] ,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    token = jwt.encode(payload, secrete, algorithm="HS256")
    return token


def decode(token: str):
    """
      This function decodes and returns a dictionary of values encoded on provided JWT token.
    
    """
    try:
        decode_token = jwt.decode(token, secrete, algorithms="HS256")

    # todo
    # except jwt.ExpiredSignatureError:
    #     raise TokenError("Expired token")
    # except jwt.DecodeError:
    #     raise TokenError("Invalid token")
    # except jwt.InvalidTokenError:
    #     raise TokenError("Invalid token")

    except:
        return None
    return decode_token


# token = encode(user_id=1, username="aron")
# print(token)

# decoded = decode(token)
# print(decoded)
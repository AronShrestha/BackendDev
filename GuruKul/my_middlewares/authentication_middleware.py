from typing import Union
from starlette.authentication import (
    AuthCredentials, AuthenticationBackend, AuthenticationError, BaseUser,  
    # SimpleUser
    )
from typing import Tuple
import base64
import binascii
from starlette.requests import HTTPConnection


from utilities.tokennizer import decode
from database.database_config import session_local
from database.model.user_model import User


class AuthenticatedUser(BaseUser):
    def __init__(self, User) -> None:
        self.id = User.id
        self.username = User.username
        self.email = User.email
        self.is_active = User.is_active
        self.role = User.role


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection)\
          -> Union[Tuple[AuthCredentials, BaseUser], None]:
        if "Authorization" not in conn.headers:
            return 
        auth = conn.headers["Authorization"]

        # will be in format 'Bearer <token>'
        try:
            schema, token = auth.spit()
            decoded_token = decode(token)

            if not decoded_token:
                raise ValueError("Token invalid")                    
            db = session_local()
            user = db.query(User).filter(User.id == decoded_token['userID'])
            if not user:
                raise ValueError("Invalid User")
        except ValueError:
            raise AuthenticationError("Invalid or Expired token!")
        return AuthCredentials(["authenticated"]), AuthenticatedUser(User)

# s = SimpleUser("aron")
# print(s.username)

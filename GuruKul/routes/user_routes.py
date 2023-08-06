from starlette.routing import Mount,Route
from api.user_endpoint import user_register, user_login


user_route = [
    Route("/signup", user_register, methods=["POST"]),
    Route("/login", user_login, methods=["POST"])
]
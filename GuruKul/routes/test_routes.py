from starlette.routing import Mount,Route
from api.starter_test import start_test_point


test_route = [
    Route("/", start_test_point)
]
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler



from routes.test_routes import test_route
from routes.user_routes import user_route
from database.model import user_model
from database.database_config import engine
from graphql_endpoints.typedef import schema


def on_start():
    print("Starting the server")


# Create GraphQL App instance
graphql_app = GraphQL(
    schema,
    debug=True,
    websocket_handler=GraphQLTransportWSHandler(),
)

# Create custom routes wrapping default ones provided by Ariadne
async def graphql_route(request):
    # Insert custom logic there

    return await graphql_app.handle_request(request)

routes = [
    Mount("/test", routes=test_route),
    Route("/graphql_route/", graphql_route, methods=["GET", "POST", "OPTIONS"]),
    Mount("/user", routes=user_route)
]

user_model.Base.metadata.create_all(bind=engine)




app = Starlette(
                debug=True,
                routes=routes,
                on_startup=[on_start]
)
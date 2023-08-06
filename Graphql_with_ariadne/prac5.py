# Handling arguments

from ariadne import make_executable_schema, ObjectType
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from starlette.applications import Starlette
from starlette.routing import Route, WebSocketRoute


type_def = """
    type Query{
        holidays(year: Int): [Strng]!
    }

"""

query = ObjectType("Query")

@query.field("holidays")
def resolve_holidays(*_, year=None):
        if year:
             return 

# Create executable schema instance with the new "post" type
schema = make_executable_schema(type_def, query)

# Create GraphQL App instance
graphql_app = GraphQL(
    schema,
    debug=True,
    websocket_handler=GraphQLTransportWSHandler(),
)

# ... Rest of the code remains the same ...

# Create custom routes wrapping default ones provided by Ariadne
async def graphql_route(request):
    # Insert custom logic there

    return await graphql_app.handle_request(request)


async def websocket_route(websocket):
    # Insert custom logic there
    await graphql_app.handle_websocket(websocket)


# Create Starlette App instance using custom routes
app = Starlette(
    routes=[
        Route("/graphql/", graphql_route, methods=["GET", "POST", "OPTIONS"]),
        WebSocketRoute("/graphql/", graphql_app.handle_websocket),
    ],
)
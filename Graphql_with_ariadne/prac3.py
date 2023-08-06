from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from starlette.applications import Starlette
from starlette.routing import Route, WebSocketRoute

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()


@query.field("hello")
def resolve_hello(_,info):
    request = info.context['request']
    user_agent = request.headers.get("user-agent", "guest")

    return "Hello world! ,%s" % user_agent


# Create executable schema instance
schema = make_executable_schema(type_defs, query)

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
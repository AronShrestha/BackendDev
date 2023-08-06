from ariadne import make_executable_schema, ObjectType
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from starlette.applications import Starlette
from starlette.routing import Route, WebSocketRoute

type_defs = """
    type Query {
        hello: String!
        message: String!
        user: User

    }

    type User {
        first_name: String!
        last_name: String!
        username: String!
    }


"""

query = ObjectType("Query")



@query.field("hello")
def resolve_hello(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello World"

@query.field("message")
def resolve_hello(_, info):

    return "This the message from the root"


@query.field("user")
def resolve_user(_, info):
    return {"first_name": "Deepu", "last_name": "Gupta", "username": "deepu_g"}

user = ObjectType("User")


@user.field("username")
def resolve_username(obj, *_):
    return f"{obj['first_name']} {obj['last_name']}"



# Create executable schema instance with the new "post" type
schema = make_executable_schema(type_defs, query, user, post)

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
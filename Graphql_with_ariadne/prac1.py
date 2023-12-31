from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from starlette.applications import Starlette

type_defs ="""
type Query{
    hello : String!
}

"""
query = QueryType()

@query.field("hello")
def resolver_hello(*_):
    return "hello world"


# Create executable schema instance
schema = make_executable_schema(type_defs, query)

#Mount Ariadne GraphQl as sub-application for Starlette

app = Starlette(debug = True)

app.mount("/graphql",GraphQL(schema, debug=True))
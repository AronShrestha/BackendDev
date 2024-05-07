from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from api.schema.graphql_schema_loader import load_schema


type_defs = load_schema()
schema = make_executable_schema(
type_defs,
[
    
]
)
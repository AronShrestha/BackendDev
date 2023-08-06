from .user import users
from .query import querries,query
from ariadne import EnumType, make_executable_schema
from database.model.user_model import Role


type_defs =[
    users,
    querries
]

schema = make_executable_schema(type_defs, query, 
                 # Wrap Python enum in EnumType to give it explicit name in GraphQL schema
                                # EnumType("Role",Role)        
                                )
from ariadne import QueryType
from services.users import get_users



# schema defination for queries 

querries = """
    type Query{
    users: [User]
    userRegister: User
    }

"""

query = QueryType()  # use generic ObjectType("Query")


@query.field("users")
async def resolve_users(*_):
    return await get_users()
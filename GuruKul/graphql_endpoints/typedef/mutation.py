from ariadne import ObjectType
from services.user_authentication import user_register, user_login

#schema defination for mutation 
mutations ="""
    type Mutation{
        register(email: String, role: String, username: String, password: String ): userRegister
    }

"""

mutation = ObjectType("Mutation")

@mutation.field("register")
async def resolve_user_register(_, info, input: dict):
    
users = '''
type User{
    id: Int
    email: String
    role: String
    is_active: Boolean
    username: String
    password: String
}
type User_login{
    id: Int
    email: String
    role: String
    is_active: Boolean
    username: String
}
'''


# enum Role{
#     teacher
#     student
# }
# todo
# note Role is enum type and we need to import its class
# and Wrap Python enum in EnumType to give it explicit name in GraphQL schema
# example :EnumType("PostWeightEnum", PostWeight)
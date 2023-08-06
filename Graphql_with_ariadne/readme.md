# Graphql with ariadne 

In Ariadne we use Schema Defiition Lannguage(SDL) for declaring GraphQL schemas
We will start by defining the special type Query that GraphQL services use as an entry point for all reading operations.

Using the SDL, our Query type definition will look like this:
type_defs = """
    type Query {
        hello: String!
    }
"""

The type Query { } block declares the type, hello is the field definition, String is the return value type, and the exclamation mark following it means that the returned value will never be null

## Validating Schema 
In Ariadne schema validation can be done by "gql" utility.
It takes a single argument( a GraphQL string) like :
from ariadne import gql

type_defs = gql("""
    type Query {
        hello String!
    }
""")
gql validates the schema and raises a descriptive GraphQLSyntaxError, if there is an issue, or returns the original unmodified string if it is correct.

If we try to run the above code now, we will get an error pointing to incorrect syntax within our type_defs declaration:

graphql.error.syntax_error.GraphQLSyntaxError: Syntax Error: Expected :, found Name

GraphQL request (3:19)
    type Query {
        hello String!
                ^
    }

Using gql is optional; however, without it, the above error would occur during your server's initialization and point to somewhere inside Ariadne's GraphQL initialization logic, making tracking down the error tricky if your API is large and spread across many modules.

## Resolver 
It's a function that is mediating between APU consumers and the application's business logic. In Ariadne every GraphQL type has fields, and every field has a resolver function that takes care of returning the value that the client has requested.



### In Ariadne every field resolver is called with at least two arguments: the query's parent object, and the query's execution info that usually contains a context attribute. The context is GraphQL's way of passing additional information from the application to its query resolvers.


#### In Ariadne the process of adding the Python logic to GraphQL schema is called binding to schema, and special types that can be passed to make_executable_schema's second argument are called bindables. QueryType (introduced earlier) is one of many bindables provided by Ariadne that developers will use when creating their GraphQL APIs.



## Detail on Query of graphQL(generaly for get data we do Query and mutation for delete and update)
### For GraphQL its very essential to give typedef and resolver
a) <Typedef> is given as string, used to define kinda Schema.
Some important necessary stufs "!" for not null, [] for getting array ...
In typedef it's very essential to define Query that is used to get data from the server and {muation to update ,post and del data}
b)example of argument based:
type_def:type Query{
        getTodos : [Todo]
        getUsers: [User]
        getUser(id :ID!):User
        }
        here "getUser(id :ID!):User" is the argument based typedef and resolver(will discuss more on resolver after this example) for it is:
query = ObjectType("Query")
@query.field("getUser")
def resolve_user_by_id(_, info,id):
    id = int(id)
    for i in range(len(USER)):
        if id == USER[i]['id']:
            return USER[i]

        Here since object type is Query {cz defined as "type Query{}"} so we need to set this resolver field as Query (which is a root type)
        We have taken id as paramter to get it from client to give them access to particular user and rest is logic.


c)<Resolver> : It is used to give resquested data. It takes in general two main argument and others.   
i) obj (or parent or root): This parameter represents the result of the parent resolver. In other words, it holds the data returned by the resolver of the parent field. For top-level fields (fields at the root of the query), this parameter is usually None. However, for nested fields, this parameter will contain the data returned by the resolver of the parent field, and the resolver can use it to access relevant information for the current field.

ii) info: This parameter contains important information about the execution state of the GraphQL query. It is an instance of the GraphQLResolveInfo class and provides details such as the field name, field type, AST (Abstract Syntax Tree) nodes, and more. It can be used to understand the context of the current field and make decisions based on that context.

iii)other arguments: Additional parameters might be present based on the specific arguments provided in the GraphQL query. For example, if a field has arguments specified in the schema (e.g., getUser(id: ID!): User), the resolver function will receive these arguments as additional parameters. These arguments are used to customize the data retrieval based on the user's request.
Eg:  1) type Query{
        getTodos : [Todo]
        getUsers: [User]
        getUser(id :ID!):User
        }
        here obj = Query so owe need ObjectType("Query")
    2)      type Todo{
     id:ID!,
     title:String!,
     completed:Boolean
     user : User

     }
     her obj= Todo , (Todo carries it's data for each call) and we need ObjectType("Todo")
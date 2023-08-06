# # Handling arguments

from ariadne import make_executable_schema, ObjectType
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from starlette.applications import Starlette
from starlette.routing import Route, WebSocketRoute
import json

DATA =[]
USER =[]

with open('todo.json') as f:
    DATA = json.load(f)

with open('user.json') as f:
    USER = json.load(f)

type_def = """
     type User{
        id : ID!
        name : String!
        email : String!
        phone : String!
        

     }
     type Todo{
     id:ID!
     title:String!
     completed:Boolean
     userId :ID
     user : User

     }

        type Query{
        getTodos : [Todo]
        getUsers: [User]
        getUser(id :ID!):User

        }
        type Mutation{
        addTodo(title: String!, completed: Boolean, userID: ID):Todo
        updateTodo(id:ID! ,title: String!, completed: Boolean, userID: ID):Todo
        removeTodo(id :ID!):Boolean
        }

"""
#here [Todo] as in square bracket expects the array of todos obj

query = ObjectType("Query")

@query.field("getTodos")
def resolve_todo(_, info):
    return DATA


@query.field("getUsers")
def resolve_user(_, info):
    return USER


@query.field("getUser")
def resolve_user_by_id(_, info,id):
    id = int(id)
    for i in range(len(USER)):
        if id == USER[i]['id']:
            return USER[i]


todo = ObjectType("Todo")

@todo.field("user")
def resolver_user(todo, info):
    """
    for every user field in TODOS it gets called and then for every todo we get userId and match that userID with user data (i.e USERS) id and return th correct user
    """
    user_id = todo.get('userId')
    print("User id :", user_id)
    for user in USER:
        if user_id == user['id']:
            return user



# Create executable schema instance with the new "post" type

mutation = ObjectType("Mutation")

@mutation.field("removeTodo")
def resolver_remove_todo(_, info, id ):
    changed = False
    id = int(id)
    for i in range(len(DATA)):
        if id == DATA[i]['id']:
            DATA.remove(DATA[i])
            changed = True
            break
    if changed:
        with open('todo.json', 'w') as f:
            json.dump(DATA, f)
        return True
    return False

@mutation.field("addTodo")
def resolver_add_todo(_,info, title, completed, userID):
    todo ={
        'id':0,
        'title':title,
        'completed':completed,
        'userId':userID
    }
    print(" Adding new todo", todo)
    DATA.append(todo)
    with open('todo.json', 'w') as f:
            json.dump(DATA, f)
    return todo


@mutation.field("updateTodo")
def resolver_add_todo(_,info, id,title=None, completed=None, userID=None):
    index = 0
    found = False
    id = int(id)
    for i in range(len(DATA)):
        if DATA[i]['id'] == id:
            index = i
            found = True
            break

    if title == None:
        title = DATA[index]['title'] 

    if completed == None:
        completed = DATA[index]['completed'] 

    if userID == None:
        userID = DATA[index]['userId'] 

    if found == True:
        DATA[index]['title'] = title 
        DATA[index]['completed'] = completed
        DATA[index]['userId'] = userID

        #write to database only is changes are made
        with open('todo.json', 'w') as f:
                json.dump(DATA, f) 

    return DATA[index]







schema = make_executable_schema(type_def, query, todo, mutation)

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




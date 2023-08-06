import contextlib

import sqlalchemy
from starlette.applications import Starlette
from starlette.config import Config
from starlette.responses import JSONResponse
from starlette.routing import Route

from  model.task_datahouse import database
from views.curd import get_todos, add_todo, update_todo, delete_todo


#defining the context manager
@contextlib.asynccontextmanager
async def lifespan(app):
    await database.connect()
    yield 
    await database.disconnect()


routes=[
    Route("/todo", endpoint=get_todos, methods=["GET"]),
    Route("/todo", endpoint=add_todo, methods=["POST"]),
    Route("/todo", endpoint=update_todo, methods=["PUT"]),
    Route("/todo", endpoint=delete_todo, methods=["Delete"])
]
    
app = Starlette(
    routes = routes,
    lifespan = lifespan
)
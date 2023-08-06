Explored on interaction with database , and made CURD endpoints.
```from starlette.responses import JSONResponse
from model.task_datahouse import todo,database
from starlette.datastructures import QueryParams
from sqlalchemy import create_engine, select

#Writing curd logic and endpoint here 
async def get_todos(request):
    query = todo.select()
    result = await database.fetch_all(query)
    content = []
    # try:
    for res in result:
        content.append({
            "name":res['name'],
            "description": res["description"],
            "completed" : res["completed"],
            "created_at": res["created_at"]
        })
    # except Exception as e:
    #     return JSONResponse({"Error Message":f"Nothing to show {e}"})
    return JSONResponse(content)


async def add_todo(request):
    data = await request.json()
    print("Data got from client :",data)
    query = todo.insert().values(
                name=data['name'],
                description = data["description"],
                completed = data["completed"]
    )
    await database.execute(query)
    return JSONResponse({
"Success":"Created a todo"
    }
    )

async def update_todo(request):

    data = await request.json()
    # Access the query parameters using the `query_params` attribute of the request
    query_params  = QueryParams(request.query_params)

     # Access individual query parameters by their keys
    todo_id = int(query_params.get("id"))
    querry = select(todo).where(todo.c.id == todo_id)
    result = await database.fetch_one(querry)
    if result is not None:
        update_query =(
            todo.update().where(
            todo.c.id == todo_id
            ).values(**data)
        )
        await database.execute(update_query)

        res = {
            "id":todo_id,
            "updated":dict(result)

        }
        return JSONResponse(res)
    else:
        # Return a response indicating that the data was not found
        return JSONResponse({"message": "Todo not found"}, status_code=404)


async def delete_todo(request):
    query_params  = QueryParams(request.query_params)
     # Access individual query parameters by their keys
    todo_id = int(query_params.get("id"))
    querry = select(todo).where(todo.c.id == todo_id)
    result = await database.fetch_one(querry)
    if result is not None:
        delete_query = (
            todo.delete().where(
            todo.c.id == todo_id
            )
        )

        await database.execute(delete_query)
        # Return a response indicating success
        return JSONResponse({"message": "Todo deleted successfully"})
    else:
        # Return a response indicating that the data was not found
        return JSONResponse({"message": "Todo not found"}, status_code=404)
````

    



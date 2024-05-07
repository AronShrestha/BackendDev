from fastapi import APIRouter 

GraphqlRouter = APIRouter(
    prefix = "/graphql",
    tags = ["graphql", "v1"]

)
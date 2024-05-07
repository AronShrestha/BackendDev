from fastapi import FastAPI


from api.config import API_VERSION


app = FastAPI()
ROUTE_PREFIX = f"/api/{API_VERSION}"


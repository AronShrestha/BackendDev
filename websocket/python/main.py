from fastapi import FastAPI, WebSocket


WEB_SOCKET_ROUTE = f"/ws"
app = FastAPI()


@app.get("/")
async def get():
    return {"message":"I am listening"}


@app.websocket(WEB_SOCKET_ROUTE)
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"Sending from the server: {data}")
        print("data",data)
        print("done")
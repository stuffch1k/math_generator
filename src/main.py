from fastapi import FastAPI
import uvicorn 
from models.model import *
from database import database
from api import router

app = FastAPI()
app.include_router(router)

app.state.database = database

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

@app.get("/")
def main():
    return "Main"

# if __name__=="__main__":
#     uvicorn.run("main:app", host='127.0.0.1', port=8081, reload = True)

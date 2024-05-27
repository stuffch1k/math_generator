from fastapi import FastAPI
import uvicorn 
from api import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def main():
    return "Main"

# if __name__=="__main__":
#     uvicorn.run("main:app", host='127.0.0.1', port=8081, reload = True)

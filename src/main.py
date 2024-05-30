from fastapi import FastAPI
import uvicorn 
from api import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.0.109",
    "http://192.168.0.109:3000",
    "https://overwrought-salt.surge.sh"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return "Main"

# if __name__=="__main__":
#     uvicorn.run("main:app", host='127.0.0.1', port=8081, reload = True)

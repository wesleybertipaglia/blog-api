import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import create_db
from src.controllers import *

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)

create_db()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return 'Welcome to store API 🎉'

# routes
app.include_router(auth_router, prefix='/auth')

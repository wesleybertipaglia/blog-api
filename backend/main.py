import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.database import create_db
from src.routes import *

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)

create_db(seed=False)
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
    return 'Welcome to Blog Sphere API 🌐'

# routes
app.include_router(user_router, prefix='/users', tags=['Users'])
app.include_router(post_router, prefix='/posts', tags=['Posts'])
app.include_router(comment_router, prefix='/comments', tags=['Comments'])
app.include_router(like_router, prefix='/likes', tags=['Likes'])
app.include_router(follow_router, prefix='/follows', tags=['Follows'])
app.include_router(auth_router, prefix='/auth', tags=['Auth'])

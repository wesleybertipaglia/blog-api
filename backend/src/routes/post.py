"""Post routes module."""

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.post import Post, PostList, PostSingle
from src.controllers.post import PostController
from src.core import Security

router = APIRouter()
db: Session = next(get_db())
security = Security()

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[PostList])
async def list(skip: int = 0, limit: int = 10):
    """List all posts with pagination. (skip: int = 0, limit: int = 10) -> List[PostList]."""
    return PostController(db).list(skip=skip, limit=limit)

@router.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=List[PostList])
async def list_by_user(user_id: str, skip: int = 0, limit: int = 10):
    """List all posts from a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[PostList]."""
    return PostController(db).list_by_user(user_id=user_id, skip=skip, limit=limit)

@router.get('/current', status_code=status.HTTP_200_OK, response_model=List[PostList])
async def list_my_posts(token: str = Depends(security.oauth2_scheme), skip: int = 0, limit: int = 10):
    """List all posts from the current user with pagination. (token: str, skip: int = 0, limit: int = 10) -> List[PostList]."""
    return PostController(db).list_my_posts(token=token, skip=skip, limit=limit)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=PostSingle)
async def get(id: str):
    """Get a post by id. (id: str) -> PostSingle."""
    return PostController(db).get(id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostSingle)
async def create(post: Post, token: str = Depends(security.oauth2_scheme)):
    """Create a post. (post: PostSingle, token: str) -> PostSingle."""
    return PostController(db).create(post=post, token=token)

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=PostSingle)
async def update(id: str, post: PostSingle, token: str = Depends(security.oauth2_scheme)):
    """Update a post by id. (id: str, post: PostSingle, token: str) -> PostSingle."""
    return PostController(db).update(id=id, post=post, token=token)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str, token: str = Depends(security.oauth2_scheme)):
    """Delete a post by id. (id: str, token: str) -> JSONResponse."""
    return PostController(db).delete(id=id, token=token)

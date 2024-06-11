"""Post routes module."""

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.post import Post, PostList, PostSingle
from src.controllers.post import PostController

router = APIRouter()
db: Session = next(get_db())

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[PostList])
async def list(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    """List all posts with pagination. (skip: int = 0, limit: int = 10) -> List[PostList]."""
    return PostController(db).list(skip=skip, limit=limit)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=PostSingle)
async def get(id: str, db: Session = Depends(get_db)):
    """Get a post by id. (id: str) -> PostSingle."""
    return PostController(db).get(id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostSingle)
async def create(post: Post, db: Session = Depends(get_db)):
    """Create a post. (post: PostSingle) -> PostSingle."""
    return PostController(db).create(post)

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=PostSingle)
async def update(id: str, post: PostSingle, db: Session = Depends(get_db)):
    """Update a post by id. (id: str, post: PostSingle) -> PostSingle."""
    return PostController(db).update(id=id, post=post)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str, db: Session = Depends(get_db)):
    """Delete a post by id. (id: str) -> JSONResponse."""
    return PostController(db).delete(id)